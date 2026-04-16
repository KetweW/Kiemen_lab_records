# Perineural Invasion in PDAC: Mechanisms of Neuron–Cancer Interaction
## A Deep Double-Track Literature Field Map

> **Research Date:** April 16, 2026  
> **Provisional Reference Frame:** Human PDAC tissue + mouse models (KPC, orthotopic); embryonic pancreatic innervation as developmental comparator  
> **Task Type:** Mechanism-dominant (with problem–technology coupling where spatial/single-cell evidence reshapes mechanistic conclusions)  
> **User Goal:** Build a structured literature field map for thesis foundation (Decision A)

---

## I. Object Definition & Analytical Boundaries

**Standard Name:** Perineural Invasion (PNI) in Pancreatic Ductal Adenocarcinoma (PDAC)

**Aliases / Related Terms:** Cancerous neural invasion (CNI), neurotropism, neural invasion, nerve infiltration. PNI is distinct from *lymphovascular invasion* and *direct nerve destruction*. PNI specifically denotes cancer cell migration along, around, or through nerve fascicles—not merely compression or displacement of adjacent nerves.

**Species/Disease Context:** This report focuses on human PDAC and the KPC (Pdx1-Cre; KrasG12D/+; Trp53R172H/+) mouse model, with developmental comparisons drawn from murine and zebrafish embryonic pancreatic innervation.

**Boundary with Adjacent Concepts:**

- **PNI vs. Neural Remodeling (PANR):** PNI describes cancer cell invasion of the perineural space. Pancreatic Cancer-Associated Neural Remodeling (PANR) describes increased nerve density, hypertrophy, and altered nerve fiber composition within the tumor. These are related but mechanistically separable phenomena—PANR can precede and facilitate PNI.
- **PNI vs. Tumor Innervation / Axonogenesis:** Tumor-directed axonogenesis (neo-neurogenesis) is the process by which tumor-derived signals recruit new nerve fibers into the tumor mass. PNI is the reverse direction: cancer cells invading nerves. Both processes coexist and are bidirectional.
- **PNI vs. Cancer-Associated Pain:** PNI is the histological event; cancer-associated pain is one downstream clinical consequence, mediated by nerve damage, neuroinflammation, and nociceptor sensitization within the perineural niche.

---

## II. Executive Summary

**Most Stable Conclusions:**

1. PNI is near-universal in PDAC (70–100% incidence), present even in early precursor lesions (PanIN), and is an independent negative prognostic factor for overall survival and disease-free survival. [E1][A]
2. The neuron–cancer interaction is bidirectional: cancer cells secrete neurotrophins (NGF, GDNF, BDNF, Artemin) that promote axonogenesis, while nerve-derived chemokines (CXCL12, CX3CL1) and neurotrophic factors attract cancer cells toward nerves. [E1][A]
3. Schwann cells undergo c-Jun–dependent dedifferentiation into a "repair-like" state that actively guides cancer cell migration along tumor-activated Schwann cell tracks (TASTs). [E2][A]
4. The axon guidance gene family is the most frequently mutated gene family in PDAC (whole-exome sequencing), indicating deep genomic entanglement between axon guidance and pancreatic oncogenesis. [E2][A]

**Largest Current Controversy:**

Whether PNI is primarily a cancer-cell-autonomous invasion process (cancer cells actively seeking nerves) or a microenvironment-orchestrated event (Schwann cells, macrophages, and fibroblasts collectively building "invasion highways"). The 2025 Cancer Cell integrated sc/snRNA-seq + spatial transcriptomics study suggests it is the latter—a multicellular ecosystem with distinct spatial niches.

**Largest Evidence Boundary:**

Most mechanistic studies rely on 2D co-culture (DRG explant models) or the KPC GEMM. The 3D architecture of the perineural niche, the temporal dynamics of invasion, and the role of specific neuronal subtypes (sympathetic vs. sensory vs. parasympathetic) have only recently become accessible through Trace-n-Seq and spatial transcriptomics. Extrapolation from mouse models to human PNI remains under-validated at the single-cell level.

**Most Valuable Missing Link (for your thesis):**

The systematic comparison of molecular programs active during embryonic pancreatic innervation (e.g., NCC migration, SCP–axon co-migration, Netrin/Slit/Sema guidance) with those reactivated in PDAC PNI. The 2025 Netrin-1 study (Nature Communications) directly demonstrates that Netrin-1—an embryonic axon guidance cue—is re-expressed in precancerous lesions and drives sympathetic remodeling, providing a concrete molecular example of developmental co-option.

---

## III. Longitudinal Tracing: How Did We Get Here?

### Phase 1: The Histological Era (Pre-2000)

PNI was first recognized as a histopathological feature in head and neck cancers (Batsakis, 1985) and subsequently identified as remarkably prevalent in PDAC. Early work was purely descriptive: pathologists noted cancer cells within the perineural space on H&E-stained sections. The mechanistic "why" was essentially unknown. **Enabling technology:** Standard histopathology and immunohistochemistry.

### Phase 2: The Neurotrophin Hypothesis (2000–2012)

The discovery that PDAC cells overexpress NGF, GDNF, and their cognate receptors (TrkA, RET/GFRα1) led to the "neurotrophin chemotaxis" model: tumor cells both secrete and respond to neurotrophic signals, creating a paracrine loop between cancer and nerve. Key milestones:

- **GDNF–GFRα1–RET axis:** GDNF binding to RET activates downstream KRAS signaling, upregulates MMP expression, and accelerates stress fiber formation—directly linking neurotrophin signaling to invasive cell motility. [E2][A]
- **NGF–TrkA axis:** HGF from pancreatic stellate cells activates c-Met on PDAC cells, triggering the mTOR–NGF pathway and boosting PNI. Systemic anti-NGF treatment in KPC mice inhibits tumor progression. [E2][A]
- **Sympathetic norepinephrine → β2-AR → NGF loop:** Sympathetic neurons supply norepinephrine, which upregulates NGF production in PDAC cells via β2-adrenergic receptors—a feedforward amplification circuit. [E2][A]
- **Artemin–GFRα3:** Artemin is another GDNF-family ligand implicated in PNI, acting through GFRα3 on both cancer and neural cells. [E2][B]
- **BDNF–TrkB:** Overexpressed in PDAC, but *levels do not independently correlate with PNI severity*, suggesting BDNF may play a permissive rather than instructive role. [E2][A]

**Enabling technology:** Immunohistochemistry, ELISA, cell migration/invasion assays, early GEMM models.

### Phase 3: Axon Guidance Cues Enter the Picture (2012–2019)

A paradigm shift occurred when researchers recognized that the same axon guidance molecules governing embryonic neural wiring are redeployed in PDAC PNI:

- **SEMA3D–PlexinD1:** SEMA3D secreted by PDAC cells activates PlexinD1 on nerves, promoting innervation. Knockdown of SEMA3D or neutralization of PlexinD1 abrogates PNI in orthotopic models (Chedotal lab, Gastroenterology 2019). [E2][A]
- **SLIT2–ROBO:** SLIT2 functions as a repulsive guidance cue. In PDAC, *SLIT2 expression is reduced*, effectively removing a molecular brake on cancer cell migration toward nerves—a loss-of-repulsion mechanism. [E2][A]
- **Netrin-1–DCC/UNC5B:** Netrin-1, a classical midline attractant, is re-expressed in precancerous pancreatic lesions (PanIN) and promotes sympathetic axon outgrowth through DCC. Inhibition of Netrin-1 disrupts sympathetic remodeling but paradoxically accelerates PanIN progression, suggesting Netrin-1-driven innervation plays a protective role in precancerous stages. (Hirt et al., Nature Communications 2025) [E2][A]
- **Whole-exome/genome sequencing revelation (Biankin et al., Nature 2012):** Exome sequencing of 142 early-stage PDAC patients revealed frequent and diverse somatic aberrations in axon guidance pathway genes, particularly SLIT/ROBO signaling (SLIT2 and/or ROBO1/2 affected 23% of patients). Structural variants of axon guidance genes were found in up to 25% of cancer genomes. These findings were independently validated by Sleeping Beauty transposon mutagenesis screens. [E1][A]

**Enabling technology:** GEMM models (KPC), orthotopic transplantation, DRG co-culture model, whole-exome sequencing.

### Phase 4: Schwann Cells as Active Architects (2016–2024)

The recognition that Schwann cells are not passive bystanders but active participants fundamentally reshaped the PNI paradigm:

- **c-Jun–dependent reprogramming:** PDAC cells activate Schwann cells, inducing c-Jun–dependent dedifferentiation into a repair-like/non-myelinating state—a process analogous to the Wallerian degeneration response after nerve injury. Markers: SOX2↑, c-Jun↑, GFAP↑, p75NTR↑. [E2][A]
- **Tumor-Activated Schwann Cell Tracks (TASTs):** Reprogrammed Schwann cells organize into linear tracks (resembling Büngner's bands) that function as physical migration highways for cancer cells (Deborde et al., Cancer Discovery 2022). [E2][A]
- **PGE₂–LIF–ADAMTS-1 axis:** PDAC-derived prostaglandin E₂ (PGE₂) drives Schwann cell dedifferentiation and secretion of LIF and ADAMTS-1, which degrade ECM and remodel the perineural niche (Signal Transduction and Targeted Therapy, 2026). [E2][A]
- **Schwann cell–CAF regulation:** Schwann cells regulate both tumor cells and cancer-associated fibroblasts in the PDAC microenvironment, positioning them as central orchestrators (Ferdoushi et al., Nature Communications 2023). [E2][A]
- **Schwann cell subtype heterogeneity:** The 2025 Cancer Cell study identified three distinct Schwann cell subsets, with TGFBI⁺ Schwann cells localizing at the leading edge of neural invasion, being induced by TGF-β signaling, and correlating with poor survival. [E2][A]

**Enabling technology:** Co-culture models, live imaging, lineage tracing, scRNA-seq.

### Phase 5: The Multicellular Ecosystem & Single-Neuron Resolution (2024–Present)

The most recent phase integrates single-cell and spatial multi-omics to reveal PNI as a spatially organized multicellular ecosystem:

- **Trace-n-Seq (Thiel et al., Nature 2025):** Retrograde axon tracing from pancreatic tumors to ganglia, followed by single-cell transcriptomics, characterized >5,000 individual sympathetic and sensory neurons innervating PDAC. Revealed cancer-specific neuronal reprogramming, novel neuron–cancer–microenvironment interactome, and a pancreatic-cancer nerve signature. Pharmacological denervation induces pro-inflammatory TME and enhances anti-PD-1 efficacy. [E2][A]
- **Integrated sc/snRNA-seq + spatial transcriptomics (Cancer Cell, 2025):** 62 samples from 25 PDAC patients mapped cellular composition across neural invasion statuses. Key findings: (a) tertiary lymphoid structures (TLS) co-localize with non-invaded nerves in low-NI tumors; (b) NLRP3⁺ macrophages and myofibroblasts surround invaded nerves in high-NI tumors; (c) a novel endoneurial NRP2⁺ fibroblast population was identified. [E2][A]
- **Spatial transcriptomics of PNI foci (Cancers, 2025):** Highlighted that PNI foci share gene expression signatures with nerve injury response, and identified endocannabinoid and polyamine metabolism as contributors to PNI and cancer pain. [E2][A]
- **ECM subversion mapping (Cancer Cell, 2024):** Mapped functional-to-morphological variation, revealing regional ECM subversion as a basis for nerve invasion. [E2][A]

**Enabling technology:** Trace-n-Seq, scRNA-seq, snRNA-seq, Visium spatial transcriptomics, multiplexed IHC.

---

## IV. Horizontal Comparison: Molecular Mechanisms by Functional Category

### IV.1 Neurotrophic Factor Signaling (Cancer → Nerve, Nerve → Cancer)

| Ligand–Receptor Axis | Source → Target | Function in PNI | Evidence Level |
|---|---|---|---|
| NGF → TrkA/p75NTR | PDAC cells ↔ Sensory neurons | Bidirectional chemotaxis; cancer cell survival; nociceptor sensitization | [E1][A] |
| GDNF → GFRα1/RET | Neural cells → PDAC cells | Activates KRAS signaling, MMP upregulation, cell polarization | [E2][A] |
| Artemin → GFRα3 | PDAC cells → Neural cells | Promotes cancer cell migration toward nerves | [E2][B] |
| BDNF → TrkB | PDAC cells (overexpressed) | Does not independently correlate with PNI severity; possibly permissive | [E2][A] |
| Nodal → (multiple) | PDAC cells | Upregulates NGF, BDNF, GDNF expression simultaneously | [E2][B] |
| HGF → c-Met → mTOR → NGF | PSCs → PDAC cells | Stellate cell–mediated amplification of NGF production | [E2][A] |

### IV.2 Axon Guidance Cues (Developmental Programs Reactivated)

| Molecule | Normal Embryonic Role | Role in PDAC PNI | Key Distinction |
|---|---|---|---|
| SEMA3D → PlexinD1 | Repulsive/attractive guidance of developing axons | PDAC-secreted SEMA3D activates PlexinD1 on nerves; promotes innervation and PNI | Paracrine directionality flipped: tumor recruits nerves |
| SLIT2 → ROBO | Repulsive midline guidance | SLIT2 expression *reduced* in PDAC; loss of repulsion permits cancer cell migration toward nerves | Loss-of-function rather than gain-of-function |
| Netrin-1 → DCC/UNC5B | Midline attraction of commissural axons | Re-expressed in PanIN; promotes sympathetic axon outgrowth; *protective* at precancerous stage | Context-dependent: protective early, possibly pro-invasive later |
| Ephrins/Eph receptors | Contact-dependent axon guidance | Mutated in PDAC exomes; functional role in PNI under-characterized | Genomic evidence precedes functional characterization |

**Critical observation:** The axon guidance gene family is the most frequently mutated gene family in PDAC whole-exome sequencing data. This is not merely correlative—it suggests that disruption of guidance cue balance is under positive selection during PDAC evolution.

### IV.3 Cell Adhesion Molecules (Physical Tethering)

| Molecule | Mechanism | Evidence |
|---|---|---|
| L1CAM | Secreted by Schwann cells; acts as chemoattractant; activates MAPK in cancer cells; upregulates MMP-2/MMP-9 via STAT3 | [E2][A] Anti-L1CAM Ab reduces PNI in KPC mice |
| NCAM1 | Membrane-mediated adhesion between cancer and neural cells | [E2][B] |
| MUC1–MAG (Siglec-4a) | MUC1 on cancer cells binds MAG on myelin; mediates cancer–nerve adhesion | [E2][B] |

### IV.4 Chemokine Axes (Nerve-Derived Chemoattraction)

| Axis | Source → Target | Downstream Signaling |
|---|---|---|
| CXCL12 → CXCR4 | Neural cells → PDAC cells | PI3K–AKT; also sequesters T cells to create immune-excluded phenotype |
| CX3CL1 → CX3CR1 | Neural cells → PDAC cells | PI3K–AKT; cancer cell directional migration |

### IV.5 Schwann Cell Reprogramming

**The Nerve Injury Analogy:**
After peripheral nerve injury, Schwann cells undergo c-Jun–dependent dedifferentiation, lose myelin markers, upregulate repair markers (SOX2, p75NTR, GFAP), and organize into Büngner's bands to guide axon regeneration. In PDAC, cancer cells hijack this same program:

| Feature | Nerve Injury (Physiological) | PDAC PNI (Pathological) |
|---|---|---|
| Trigger | Axotomy, Wallerian degeneration | Cancer cell–derived signals (PGE₂, exosomes, IL-8/CCL2) |
| Schwann cell state | Repair Schwann cell (c-Jun⁺, SOX2⁺) | Repair-like/dedifferentiated (c-Jun⁺, SOX2⁺, GFAP⁺) |
| Structural output | Büngner's bands (regeneration tracks) | TASTs (tumor-activated Schwann cell tracks = invasion highways) |
| Outcome | Axon regeneration, functional recovery | Cancer cell migration along tracks, PNI, metastasis |
| Resolved? | Yes (remyelination, re-differentiation) | No (persistent dedifferentiated state, chronic remodeling) |

**Newly identified paracrine loops:**

1. **PGE₂ → SC dedifferentiation → LIF + ADAMTS-1 secretion → ECM degradation → PNI** (Signal Transduction and Targeted Therapy, 2026)
2. **bFGF → SC activation → IL-33 secretion → TAM recruitment → M2 polarization → Cathepsin B → ECM degradation → PNI** (British Journal of Cancer, 2024)
3. **PDAC-derived EVs (IL-8/CCL2) → SC activation → PNI** (In Vitro Models, 2025)

### IV.6 Immune Cell Involvement (The Perineural Immune Niche)

Macrophages are the dominant immune cell type in the perineural niche and play a dual role:

- **ECM degradation:** TAMs secrete Cathepsin B, degrading collagen IV of the nerve sheath (perineurium), physically opening the perineural space for cancer cell entry.
- **Immunosuppressive remodeling:** The CXCL12/CXCR4 axis sequesters T cells away from invaded nerves, while PD-1/PD-L1 upregulation further dampens anti-tumor immunity.
- **Schwann cell–TAM paracrine loop:** The bFGF/IL-33 positive feedback loop between Schwann cells and TAMs sustains a pro-invasive, immunosuppressive perineural microenvironment.

**Spatial insight (Cancer Cell, 2025):** In low-neural-invasion tumors, tertiary lymphoid structures (TLS) co-localize with non-invaded nerves—suggesting that intact immune surveillance protects nerves. In high-NI tumors, NLRP3⁺ macrophages and myofibroblasts replace TLS around invaded nerves.

### IV.7 Autonomic Nervous System: Sympathetic vs. Parasympathetic

| Feature | Sympathetic Nerves | Parasympathetic Nerves | Sensory Nerves |
|---|---|---|---|
| Effect of ablation | Increases tumor growth (via CD163⁺ macrophage expansion) | Surgical vagotomy suppresses tumor growth | Capsaicin ablation prevents PNI, prolongs survival |
| Neurotransmitter axis | NE → β2-AR → NGF feedforward loop | ACh → M1 muscarinic receptor → tumor suppression? | Substance P, CGRP → neuroinflammation |
| Role in PNI | Complex—sympathetic tone may be protective early (Netrin-1 study) | Under-characterized in PNI specifically | Primary PNI route; sensory fibers are the predominant invaded nerve type |
| Pharmacological target | 6-OHDA denervation + anti-PD-1 synergy (Thiel et al. 2025) | Vagotomy studies | Capsaicin denervation |

**Critical nuance:** Sympathetic innervation appears context-dependent. Netrin-1–driven sympathetic remodeling is *protective* at the precancerous stage (inhibition accelerates PanIN progression), yet in established PDAC, pharmacological sympathetic denervation synergizes with immunotherapy. This temporal switch is a major unresolved question.

---

## V. Mismatch Analysis

### V.1 What Could Old Technologies Not See?

- **2D histology:** Cannot resolve the 3D topology of cancer cell infiltration within nerve fascicles, the distinction between endoneurial vs. perineurial vs. epineurial invasion, or the spatial relationship between PNI foci and immune niches.
- **Bulk RNA-seq / IHC:** Cannot distinguish heterogeneous Schwann cell subsets (e.g., TGFBI⁺ leading-edge SCs vs. non-invaded SCs vs. repair SCs), cannot resolve neuronal subtype-specific transcriptomes, and conflates tumor-adjacent and tumor-distal nerve signals.
- **Standard co-culture (DRG model):** Cannot replicate the multicellular perineural niche (macrophages, fibroblasts, immune cells are absent). DRG co-culture is essentially a two-body problem; PNI in vivo is an N-body problem.

### V.2 What Could Old Technologies Misinterpret?

- **IHC for nerve density → conflated with PNI severity:** Increased nerve density (PANR) and PNI are correlated but mechanistically separable. IHC-based studies may conflate the two, attributing PNI effects to nerve density and vice versa.
- **GDNF "expression" → assumed functional activity:** Transcript-level GDNF expression does not equal protein-level RET activation. Post-translational processing of GDNF family ligands and receptor complex formation (GFRα co-receptors) were rarely measured.
- **Spatial adjacency in IHC → assumed functional interaction:** Cancer cells near nerves were assumed to be interacting; many of these may be passive bystanders in a confined tissue compartment.

### V.3 What New Dimensions Have Emerging Technologies Added?

- **Trace-n-Seq:** First-ever single-neuron resolution of cancer-innervating neurons. Reveals neuron-type-specific reprogramming programs and enables construction of ligand–receptor interactomes between neurons and the TME.
- **Integrated scRNA-seq + spatial transcriptomics:** Resolves the spatial organization of the perineural niche at cellular resolution: which cell types surround invaded vs. non-invaded nerves, what signaling programs are spatially restricted to PNI foci.
- **3D tissue clearing + light-sheet microscopy:** Enables visualization of nerve fiber networks within intact tumors, resolving the true 3D topology of PNI that 2D sections miss. (Emerging but not yet widely applied to PDAC PNI specifically.)

### V.4 Do These New Dimensions Change Scientific Conclusions?

**Yes, in at least three ways:**

1. **From two-player to multi-player model:** The old model was "cancer cell ↔ nerve." Spatial transcriptomics reveals PNI as a spatially organized multicellular ecosystem: TGFBI⁺ Schwann cells at the invasion front, NLRP3⁺ macrophages surrounding invaded nerves, NRP2⁺ fibroblasts within the endoneurium, and TLS protecting non-invaded nerves. This changes the target space from single ligand–receptor pairs to microenvironment architecture.

2. **From uniform nerve to heterogeneous neuronal subtypes:** Trace-n-Seq reveals that sympathetic and sensory neurons undergo *different* reprogramming in response to PDAC. This changes the hypothesis space: different neuronal subtypes may promote or resist PNI through distinct mechanisms.

3. **From static to temporally dynamic:** The Netrin-1 study reveals that the same molecular cue can be protective (precancerous) or pathological (established cancer), depending on disease stage. This fundamentally challenges the assumption that PNI-associated molecules are uniformly pro-invasive.

---

## VI. Evidence Boundaries & High-Risk Misinterpretation Points

1. **Model system extrapolation risk:** The KPC mouse recapitulates many features of human PDAC, but murine pancreatic innervation density, autonomic nerve fiber ratios, and immune composition differ from human. Schwann cell subtype heterogeneity identified in human scRNA-seq may not map directly to mouse.

2. **Transcript ≠ Protein ≠ Function:** Many PNI-associated molecules (GDNF, Artemin, Semaphorins) are described at the mRNA level. Protein localization, receptor occupancy, and signaling pathway activation are less frequently validated. The jump from "gene X is upregulated in PNI⁺ tumors" to "gene X drives PNI" requires functional intervention.

3. **Spatial proximity ≠ Functional interaction:** Even in spatial transcriptomics data, co-localization of ligand and receptor gene expression does not prove functional signaling. Ligand–receptor inference tools (CellChat, NicheNet) generate hypotheses, not causal evidence.

4. **DRG co-culture limitations:** The DRG model remains the *only* widely used in vitro PNI assay. It uses sensory neurons exclusively (no sympathetic or parasympathetic components), lacks immune cells, and does not recapitulate the 3D perineurial barrier. Conclusions drawn from DRG co-culture about PNI mechanisms should be validated in vivo.

5. **Temporal confounding:** Cross-sectional studies (even spatial transcriptomics) capture a snapshot. PNI is a dynamic process—the temporal sequence of Schwann cell activation → ECM degradation → cancer cell infiltration → immune remodeling cannot be resolved from a single time point.

---

## VII. Next-Step Projections: Missing Links

### Missing Link 1: Systematic Developmental Co-Option Mapping

**What is missing:** A direct, gene-by-gene or pathway-by-pathway comparison of the molecular programs active during embryonic pancreatic innervation (NCC migration → SCP specification → axon co-migration → organ innervation) with those reactivated in PDAC PNI. The Netrin-1 and SEMA3D studies provide individual examples, but no systematic "co-option atlas" exists.

**Why it matters for your thesis:** This is the central hypothesis of your DBO proposal. A comprehensive mapping would transform the "co-option" claim from analogy to testable molecular framework.

**What evidence is needed:** (a) Temporal transcriptomics of embryonic pancreatic innervation at key developmental stages; (b) Matched comparison with PNI-associated transcriptomes from spatial/scRNA-seq; (c) Functional validation of shared programs using conditional knockout models.

### Missing Link 2: Schwann Cell Subtype–Specific Functional Roles

**What is missing:** The 2025 Cancer Cell study identified three Schwann cell subsets, but their causal roles are not yet functionally validated. Does ablation of TGFBI⁺ SCs specifically reduce PNI? Do the other subsets resist or promote invasion?

**Why it hasn't been solved:** Schwann cell subtype-specific Cre lines are limited, and conditional ablation in the tumor context is technically challenging.

### Missing Link 3: The Sympathetic Switch

**What is missing:** Why does sympathetic innervation appear protective in precancerous lesions (Netrin-1 study) but deleterious in established PDAC (denervation synergizes with immunotherapy)? What molecular switch occurs at the PanIN → PDAC transition?

**Why it matters:** This temporal paradox has direct therapeutic implications: when and how to target innervation.

### Missing Link 4: Sensory Neuron Subtype Specificity in PNI

**What is missing:** Sensory neurons are heterogeneous (nociceptors, mechanoreceptors, proprioceptors). Which subtypes are preferentially invaded? Trace-n-Seq provides the first molecular characterization, but the mapping of PNI preference to neuron subtype is incomplete.

---

## VIII. Actionable Recommendations for Literature Field Map (Decision A)

### Recommended Field Map Structure for Thesis Introduction

1. **Historical arc:** Histological observation → neurotrophin hypothesis → axon guidance cues → Schwann cell agency → multicellular ecosystem (Phases 1–5 above)
2. **Three mechanistic pillars:** Neurotrophic signaling (bidirectional chemotaxis), Axon guidance cue redeployment (developmental co-option), Schwann cell reprogramming (nerve injury analogy)
3. **The developmental thread:** Weave the embryonic pancreatic innervation program through each pillar—NCCs use the same guidance cues, SCPs undergo the same differentiation programs, and the same growth factors regulate both embryonic innervation and PNI
4. **The spatial revolution:** Frame the 2024–2025 spatial/single-cell studies as resolving the "two-player fallacy" and revealing the multicellular perineural niche

### Key Literature Anchors (by pillar)

**Foundational reviews:**
- Bapat et al. (2011), Cancer Research — Cellular and molecular mechanisms of PNI in PDAC [待验证：非搜索来源]
- Amit et al. (2016), Clinical Cancer Research — Mechanisms of PNI (general framework) [待验证：非搜索来源]
- Wang et al. (2021), Journal of Experimental & Clinical Cancer Research — Cellular and molecular mechanisms of PNI in PDAC (PMC8360640) [A]

**Axon guidance:**
- Slit2 in PDAC: He et al. (2014), Cancer Research — SLIT2 inhibits neural invasion (PMID: 24448236) [A]
- SEMA3D–PlexinD1: Chedotal group, Gastroenterology (2019) — Axon guidance molecules promote PNI in orthotopic tumors (PMC6707836) [A]
- Netrin-1 in PanIN: Hirt et al. (2025), Nature Communications — Neural function of Netrin-1 in precancerous lesions [A]

**Schwann cells:**
- Deborde et al. (2022), Cancer Discovery — Reprogrammed Schwann cells organize into dynamic tracks (PMC9533012) [A]
- PGE₂–SC dedifferentiation: Signal Transduction and Targeted Therapy (2026) [A]
- Schwann cell subtypes: Cancer Cell (2025) — Integrated sc/snRNA-seq + spatial transcriptomics [A]

**Single-neuron resolution:**
- Thiel et al. (2025), Nature — Characterization of single neurons reprogrammed by pancreatic cancer [A]

**Immune–neural crosstalk:**
- TAM–SC paracrine loop: British Journal of Cancer (2024) — bFGF/IL-33 loop (PMC10876976) [A]
- PNI and cold TME: Frontiers in Immunology (2025) — PNI and cold TME mechanisms [A]

---

## IX. Deeper Questions Worth Pursuing

1. **Does the PNI-associated Schwann cell repair program share a common epigenetic signature with embryonic SCP specification?** If c-Jun–dependent dedifferentiation in PNI recapitulates the NCC → SCP transition, chromatin accessibility (ATAC-seq) comparisons could reveal shared regulatory elements.

2. **What is the role of the endoneurial NRP2⁺ fibroblast population?** This novel cell type was identified in the 2025 Cancer Cell study but remains functionally uncharacterized. Does it form a structural scaffold for PNI? Does it communicate with Schwann cells?

3. **Can the "co-option" hypothesis be falsified?** What would disconfirm developmental co-option—finding PNI-specific programs with no embryonic counterpart? Or showing that embryonic guidance programs are not necessary for PNI?

4. **How does the perineurial barrier fail?** The perineurium (the collagenous sheath around nerve fascicles) is a physical barrier to invasion. Its breakdown—by MMP-2/9, Cathepsin B, ADAMTS-1—is necessary but under-studied compared to molecular chemotaxis.

5. **What is the contribution of exosomes/extracellular vesicles?** PDAC-derived EVs containing IL-8/CCL2 activate Schwann cells in vitro. But the cargo composition, neuronal uptake mechanisms, and functional consequences in vivo are poorly defined.

6. **Does metabolic reprogramming in the perineural niche (endocannabinoid/polyamine metabolism identified by spatial transcriptomics) represent a druggable vulnerability?**

---

## X. Literature Tracking

### 10.1 Original Research
- Thiel et al. (2025). Characterization of single neurons reprogrammed by pancreatic cancer. *Nature*. DOI: [accessed via search] https://www.nature.com/articles/s41586-025-08735-3
- He et al. (2014). Axon guidance factor SLIT2 inhibits neural invasion and metastasis in pancreatic cancer. *Cancer Research*. PMID: 24448236
- Chedotal group (2019). Axon guidance molecules promote perineural invasion and metastasis of orthotopic pancreatic tumors in mice. *Gastroenterology*. PMC6707836
- Deborde et al. (2022). Reprogrammed Schwann cells organize into dynamic tracks that promote pancreatic cancer invasion. *Cancer Discovery*. PMC9533012
- Schwann cell–TAM paracrine loop (2024). Tumour-associated macrophages and Schwann cells promote perineural invasion via paracrine loop in PDAC. *British Journal of Cancer*. PMC10876976
- Li et al. (2022). Sympathetic axonal sprouting induces changes in macrophage populations and protects against pancreatic cancer. *Nature Communications*. https://www.nature.com/articles/s41467-022-29659-w
- PGE₂ → SC dedifferentiation (2026). Prostaglandin E2-driven dedifferentiation of Schwann cells leads to perineural invasion in PDAC. *Signal Transduction and Targeted Therapy*. https://www.nature.com/articles/s41392-026-02648-x
- Hirt et al. (2025). Neural function of Netrin-1 in precancerous lesions of the pancreas. *Nature Communications*. https://www.nature.com/articles/s41467-025-62299-4
- HGF/c-Met pathway facilitates PNI via mTOR/NGF axis (2022). *Cell Death & Disease*. https://www.nature.com/articles/s41419-022-04799-5
- L1CAM induces PNI by upregulation of metalloproteinase expression (2018). *Oncogene*. https://www.nature.com/articles/s41388-018-0458-y
- Ferdoushi et al. (2023). Schwann cells regulate tumor cells and CAFs in the PDAC microenvironment. *Nature Communications*. https://www.nature.com/articles/s41467-023-40314-w
- Integrated sc/snRNA-seq + spatial transcriptomics (2025). *Cancer Cell*. https://www.cell.com/cancer-cell/fulltext/S1535-6108(25)00270-3
- Mapping functional to morphological variation reveals basis of ECM subversion and nerve invasion (2024). *Cancer Cell*. https://www.cell.com/cancer-cell/fulltext/S1535-6108(24)00079-5

### 10.2 Reviews / Systematic Reviews
- Wang et al. (2021). Cellular and molecular mechanisms of perineural invasion of PDAC. *J Exp Clin Cancer Res*. PMC8360640
- Crosstalk between peripheral innervation and PDAC (2023). *Neuroscience Bulletin*. https://link.springer.com/article/10.1007/s12264-023-01082-1
- Hallmarks of PNI in PDAC: new biological dimensions (2024). *Frontiers in Oncology*. https://www.frontiersin.org/journals/oncology/articles/10.3389/fonc.2024.1421067/full
- PNI and cold TME in pancreatic cancer (2025). *Frontiers in Immunology*. https://www.frontiersin.org/journals/immunology/articles/10.3389/fimmu.2025.1650117/full
- Perineural invasion in PDAC: recapitulating its importance and defining future directions. Lovecek (2025). *United European Gastroenterology Journal*. https://onlinelibrary.wiley.com/doi/pdf/10.1002/ueg2.70118
- PNI in PDAC: From molecules towards drugs of clinical relevance (2022). *Cancers*. PMC9739544
- Targeting PNI in pancreatic cancer (2024). *Cancers*. https://www.mdpi.com/2072-6694/16/24/4260
- Roles of the nervous system in pancreatic cancer (2021). *Mol Cancer*. PMC8452481
- Neural crest and sons: role of NCCs and SCPs in development and gland embryogenesis (2024). *Frontiers in Cell and Developmental Biology*. https://www.frontiersin.org/journals/cell-and-developmental-biology/articles/10.3389/fcell.2024.1406199/full
- Innervation of the pancreas in development and disease (2024). *Development*. https://journals.biologists.com/dev/article/151/2/dev202254/342500

### 10.3 Spatial Transcriptomics / Methods
- Spatial transcriptomics reveals novel mechanisms in PNI in PDAC (2025). *Cancers*. https://www.mdpi.com/2072-6694/17/5/852
- DRG co-culture model for in vitro PNI (2016). *JoVE*. PMID: 27167037

### 10.4 Genomics
- Biankin et al. (2012). Pancreatic cancer genomes reveal aberrations in axon guidance pathway genes. *Nature*. 491:399–405. https://www.nature.com/articles/nature11547
- Witkiewicz et al. (2015). Whole-exome sequencing of pancreatic cancer defines genetic diversity and therapeutic targets. *Nature Communications*. https://www.nature.com/articles/ncomms7744

### 10.5 Preprints
- Netrin-1 in precancerous lesions (bioRxiv version): https://www.biorxiv.org/content/10.1101/2025.05.14.654046v1.full [Note: peer-reviewed version now published in Nature Communications]

### 10.6 Recommended PubMed Search Strings for Gap-Filling
- Embryonic co-option: `("pancreatic innervation" OR "pancreas development") AND ("neural crest" OR "Schwann cell precursor") AND ("axon guidance" OR "Netrin" OR "Semaphorin" OR "Slit")`
- Schwann cell subtype functional validation: `("Schwann cell" OR "TGFBI") AND ("perineural invasion" OR "PNI") AND ("single-cell" OR "spatial transcriptomics") AND ("pancreatic cancer" OR "PDAC")`
- Temporal switch in innervation: `("sympathetic" OR "denervation") AND ("pancreatic cancer" OR "PDAC") AND ("immunotherapy" OR "checkpoint" OR "precancerous")`
