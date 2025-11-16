
!pip install biopython
from Bio import AlignIO
import math
import csv
from collections import Counter
import statistics

# Define constants
STANDARD_AA = set('ACDEFGHIKLMNPQRSTVWY')
EXCLUDED = set('X')
GAP = '-'

def shannon_entropy(column):
    """Compute Shannon entropy for one alignment column (bits)."""
    filtered = [res for res in column if res != GAP and res not in EXCLUDED]
    if not filtered:
        return 0.0
    total = len(filtered)
    counts = Counter(filtered)
    entropy = 0.0
    for res, count in counts.items():
        p = count / total
        entropy -= p * math.log2(p)
    return entropy


def analyze_alignment_entropy(alignment_file, output_csv):
    print("=" * 70)
    print(f"📊 Analyzing alignment: {alignment_file}")
    print("=" * 70)

    alignment = AlignIO.read(alignment_file, "fasta")
    nseq = len(alignment)
    ncol = alignment.get_alignment_length()

    print(f"   Sequences: {nseq}")
    print(f"   Length: {ncol} positions\n")

    results = []
    entropy_values = []

    # Calculate entropy per position
    for i in range(ncol):
        column = [str(record.seq[i]).upper() for record in alignment]
        filtered_col = [c for c in column if c != GAP and c not in EXCLUDED]

        entropy = shannon_entropy(column)
        entropy_values.append(entropy)

        counts = Counter(filtered_col)
        consensus = counts.most_common(1)[0][0] if counts else "-"
        conservation = counts[consensus] / len(filtered_col) if filtered_col else 0.0

        row = {
            "Position": i + 1,
            "Consensus": consensus,
            "Shannon_Entropy": round(entropy, 4),
            "Conservation": round(conservation, 4),
            "Non_Gap_Count": len(filtered_col),
            "Gap_Count": column.count(GAP),
            "X_Count": sum(c in EXCLUDED for c in column)
        }

        for res, freq in counts.items():
            row[f"Freq_{res}"] = round(freq / len(filtered_col), 4)

        results.append(row)

    # Compute overall variance of entropy
    variance_entropy = statistics.variance(entropy_values) if len(entropy_values) > 1 else 0.0

    # Write to CSV
    freq_fields = sorted({k for row in results for k in row.keys() if k.startswith("Freq_")})
    fieldnames = ["Position", "Consensus", "Shannon_Entropy", "Conservation",
                  "Non_Gap_Count", "Gap_Count", "X_Count"] + freq_fields

    with open(output_csv, "w", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(results)

    print("\nEntropy analysis is complete! The results have been saved to:", output_csv)
    print("The average Shannon Entropy across your dataset is {:.4f} bits.".format(statistics.mean(entropy_values)))
    print("The variance of the Shannon Entropy is {:.4f} bits².".format(variance_entropy))


    sorted_by_entropy = sorted(results, key=lambda x: x['Shannon_Entropy'])
    print("\n Most conserved positions (lowest entropy):")
    for r in sorted_by_entropy[:5]:
        print(f"Position {r['Position']}: {r['Consensus']} (entropy: {r['Shannon_Entropy']:.4f})")

    print(f"\n Least conserved positions (highest entropy):")
    for r in sorted_by_entropy[-5:][::-1]:
        print(f"   Position {r['Position']}: {r['Consensus']} (entropy: {r['Shannon_Entropy']:.4f})")


if __name__ == "__main__":
    alignment_file ="/content/NSP2A_COMBINED_FREQ_DENV2 (2).fasta"
    output_csv = "nsP2A_DENV2_Com_Entropy.csv"

    analyze_alignment_entropy(alignment_file, output_csv)

