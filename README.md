#Retrospective Evolutionary Analysis of Dengue Virus Isolates Circulating in India (2012–2024)
This code is part of a temporal analysis of DENV, focusing on the retrospective evolutionary patterns of all structural and non-structural proteins of the virus. The analysis covers all four serotypes and inspects sequences while excluding batches that show clades indicating cross-serotype recombination events, ensuring cleaner intra-serotype comparisons.
The goal of this analysis is to calibrate viral mutational frequency across protein sequences over time. While mutational frequency provides a broad picture of protein plasticity, examining diversity at each position offers deeper insight into the range of plasticity a specific position exhibits. This reflects the transient nature of evolutionary hotspots, which may stabilize or fluctuate during outbreaks.

Diversity per position (0–1):

0 → fully conserved (no variation) 🟢

0–0.3 → highly conserved 💚

0.3–0.6 → moderately variable 🟡

0.6–1 → highly variable 🔴

#🔍 Entropy & Shannon Entropy
Entropy measures the variability or uncertainty at a specific position in a protein sequence alignment.
<img width="945" height="141" alt="image" src="https://github.com/user-attachments/assets/2a5f5d23-7e0e-4501-9dbc-5549b7a07770" />

High entropy → greater diversity 🌈

Low entropy → highly conserved positions 🔒
✨ Special Feature of This Code

We do not just calculate position entropy. Instead:
🛠️ Requirements

To run this code, you need:

biopython → for reading and parsing multiple sequence alignments (MSA) 🧬

math → for logarithmic calculations (Shannon entropy) 📐

csv → for exporting results 📊

collections.Counter → for counting amino acid frequencies 🧮

statistics → for computing mean and variance of entropy
📝 Outputs

For each protein, the code generates:

CSV file with position-wise features:

Feature	Description
Position	Alignment position (1-indexed) 🆔
Consensus	Most frequent amino acid at that position 🔑
Shannon_Entropy	Entropy value (0–1) 🌈
Conservation	Fraction of sequences matching consensus 💚
Non_Gap_Count	Number of sequences with valid amino acid ✅
Gap_Count	Number of sequences with a gap ➖
X_Count	Number of sequences with unknown residue ❓
Freq_[AA]	Fraction of each amino acid at that position 🧬

This output provides a position-wise map of viral protein diversity, useful for:

🧬 Temporal hotspot dynamics

🌱 Protein plasticity mapping

🤖 ML-based evolutionary or functional studies
Entropy is computed relative to a consensus sequence, built from the alignment across all years 📅

This allows tracking how each position’s diversity deviates from consensus, capturing temporally transient hotspots 🔥 and stable positions 🛡️
