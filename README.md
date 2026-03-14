# 🧬 Retrospective Evolutionary Analysis of Dengue Virus Isolates Circulating in India (2012–2024)

This repository contains code for a **temporal evolutionary analysis of Dengue Virus (DENV)** isolates circulating in India between **2012 and 2024**.

The analysis investigates evolutionary patterns across **all structural and non-structural proteins** of the virus. All four DENV serotypes are included, while sequence batches indicating **cross-serotype recombination events** are excluded to ensure cleaner intra-serotype evolutionary comparisons.

The primary goal of this analysis is to **calibrate viral mutational frequency across protein sequences over time**.

While mutational frequency provides a broad overview of protein plasticity, examining **diversity at each position** reveals deeper insight into the range of evolutionary variability that specific residues exhibit. This helps capture the **transient nature of evolutionary hotspots**, which may stabilize or fluctuate during outbreaks.

---

# 📊 Diversity per Position (0–1)

Residue diversity values are interpreted as follows:

| Diversity Value | Interpretation |
|----------------|---------------|
| **0** | Fully conserved (no variation) 🟢 |
| **0 – 0.3** | Highly conserved 💚 |
| **0.3 – 0.6** | Moderately variable 🟡 |
| **0.6 – 1** | Highly variable 🔴 |

---

# 🔍 Entropy & Shannon Entropy

Entropy is used to measure the **variability or uncertainty at each position** in a protein multiple sequence alignment (MSA).

- **High entropy** → greater amino acid diversity 🌈  
- **Low entropy** → highly conserved positions 🔒  

Entropy values are computed using **Shannon entropy**, which quantifies the distribution of amino acids at each alignment position.

---

# ✨ Special Feature of This Code

Instead of only calculating entropy values, the pipeline performs a **comprehensive position-wise evolutionary analysis**, including:

- Consensus amino acid determination  
- Residue frequency profiling  
- Gap and unknown residue tracking  
- Conservation estimation  
- Statistical summaries of entropy across positions  

This provides a detailed **residue-level evolutionary landscape** for each viral protein.

---

# 🛠️ Requirements

To run this code, install the following Python packages:

- **biopython** – reading and parsing multiple sequence alignments (MSA) 🧬  
- **math** – logarithmic calculations for Shannon entropy 📐  
- **csv** – exporting computed results 📊  
- **collections.Counter** – counting amino acid frequencies 🧮  
- **statistics** – computing mean and variance of entropy 📝  

---

# 📤 Outputs

For each protein analyzed, the code generates a **CSV file containing position-wise evolutionary features**.

## Output Columns

| Feature | Description |
|-------|-------------|
| **Position** | Alignment position (1-indexed) 🆔 |
| **Consensus** | Most frequent amino acid at that position 🔑 |
| **Shannon_Entropy** | Entropy value representing diversity (0–1) 🌈 |
| **Conservation** | Fraction of sequences matching the consensus residue 💚 |
| **Non_Gap_Count** | Number of sequences with valid amino acids ✅ |
| **Gap_Count** | Number of sequences containing alignment gaps ➖ |
| **X_Count** | Number of sequences with unknown residues ❓ |
| **Freq_[AA]** | Fraction of each amino acid at that position 🧬 |

---

# 🔬 Applications

The resulting dataset provides a **position-wise map of viral protein diversity**, which can be applied to:

- 🧬 **Temporal hotspot dynamics analysis**  
- 🌱 **Protein plasticity mapping**  
- 🤖 **Machine learning models for evolutionary or functional studies**  

---

# 🧠 Evolutionary Insight

Entropy is computed relative to a **consensus sequence derived from the alignment across all years**.

This enables tracking how each residue’s diversity **deviates from consensus over time**, revealing:

- **Transient evolutionary hotspots** 🔥  
- **Stable conserved positions** 🛡️  

Such insights are valuable for understanding **viral adaptation, immune escape, and structural constraints in DENV proteins**.
