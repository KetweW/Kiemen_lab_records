# Neurotrophins: Discovery, Mechanism, Development, and Disease — A Horizontal–Vertical Review

> **Research date:** 15 May 2026
> **Provisional reference frame:** mammalian (mouse + human), embryonic to adult, peripheral and central nervous systems, with cancer-neuroscience emphasis on perineural invasion.
> **Task type:** Mechanism-dominated (with a problem–technique coupling layer for the cancer sections, because conclusions depend strongly on co-culture / xenograft / microfluidic platforms).
> **Evidence labels used below:** **[E1]** multi-study / cross-system consensus · **[E2]** key primary studies, model-bounded · **[E3]** single study / emerging / preprint. Access: **[A]** full-text verified · **[B]** abstract-level. Background facts widely accepted in the field are left unlabelled to avoid label inflation.

---

## I. Object Definition and Analytic Boundary

**Neurotrophins (NTs)** are a structurally homologous family of secreted growth factors that share a cystine-knot fold and signal through the Trk receptor tyrosine kinase family and the pan-neurotrophin receptor p75NTR. In mammals the family has four members:

| Standard name | Aliases / older names | Canonical high-affinity receptor | Co-receptor |
|---|---|---|---|
| NGF (β-NGF) | Nerve growth factor; *NGF* (gene) | TrkA (*NTRK1*) | p75NTR (*NGFR*) |
| BDNF | Brain-derived neurotrophic factor | TrkB (*NTRK2*) | p75NTR |
| NT-3 | Neurotrophin-3 (HDNF / NGF-2 in early literature) | TrkC (*NTRK3*); weakly TrkA, TrkB | p75NTR |
| NT-4/5 | Neurotrophin-4, Neurotrophin-5, NT-4/5 (originally cloned twice, same gene) | TrkB | p75NTR |

**Important boundary clarifications (executed before analysis to prevent the high-risk confusions flagged by this skill):**

- **Family boundary.** The "neurotrophin family" does *not* include GDNF/neurturin/artemin/persephin (GDNF family ligands, GFLs → RET/GFRα); ciliary neurotrophic factor (CNTF, IL-6 family); FGFs; or IGF-1. In cancer-neuroscience texts these are often grouped under "neurotrophic factors," but the receptor logic, signaling pathways, and developmental dependencies are different. This review treats GDNF only when needed for context (perineural invasion).
- **Pro vs mature forms.** Each neurotrophin is synthesised as a ~30 kDa precursor (proneurotrophin) and proteolytically cleaved by furin or proconvertases (intracellular) or plasmin / matrix metalloproteinases (extracellular) to release the ~13 kDa mature dimer. The pro and mature forms have *opposite* biological actions in many contexts.
- **Receptor isoforms.** TrkB and TrkC each have truncated isoforms lacking the kinase domain (TrkB.T1, TrkC-T1), which can act as dominant-negatives or decoys. Bulk receptor measurements without isoform resolution are easy to mis-interpret.
- **PNI scope clarification.** Classical *perineural invasion* (PNI) is a PNS phenomenon (pancreatic, prostate, head-and-neck, colorectal, cervical, biliary cancers). "PNI in CNS" is not a standard term; the closest CNS-relevant phenomena are (1) *perineural spread* of cutaneous / head-and-neck malignancies retrogradely along cranial nerves into the intracranial compartment, and (2) the recently described *neural-circuit hijacking* by gliomas (BDNF/TrkB-driven neuron-to-glioma synapses). Both are addressed in §VI–VII below, with the distinction kept explicit.

---

## II. Executive Summary

- **Most settled conclusion.** Neurotrophins are limiting target-derived survival factors during nervous-system development; absence of NGF, BDNF, or NT-3 (or their cognate Trk receptors) produces highly stereotyped, cell-type-specific neuronal losses in peripheral ganglia, validated across NGF/BDNF/NT-3/TrkA/TrkB/TrkC knockouts. **[E1, A]**
- **Biggest mechanistic surprise of the last 25 years.** Proneurotrophins are not inert precursors. ProNGF, proBDNF, and proNT-3, when secreted, bind a p75NTR + sortilin complex with sub-nanomolar affinity and induce apoptosis or growth-cone collapse. The "yin/yang" of pro vs mature ligand fundamentally reframes neurotrophin biology. **[E1, A]**
- **Biggest current technical edge.** Conclusions about which neurotrophin matters where depend strongly on the platform — bulk gene expression, IHC, conditional knockout, scRNA-seq of DRG subtypes, microfluidic axon chambers, and patient-derived organoids all yield partly non-overlapping pictures. Subtype resolution of DRG and sympathetic neurons has been substantially rewritten by scRNA-seq. **[E2]**
- **Most actionable disease frontier.** Cancer neuroscience: NGF/TrkA, BDNF/TrkB, and GDNF/RET axes converge on perineural invasion in the PNS and, in a structurally different but mechanistically related way, on neuron-to-glioma synapses in the CNS. Several druggable nodes (anti-NGF antibodies, pan-Trk inhibitors, RET inhibitors, AMPA-receptor blockers) are in or have completed clinical trials. **[E1–E2, A]**
- **Most under-investigated Missing Link.** A unified, quantitative framework that explains how the same NGF/TrkA axis is *trophic* (developmental survival), *nociceptive* (adult pain), *neurotoxic* (proNGF/p75 in AD), and *pro-tumorigenic* (perineural invasion) — without invoking different molecules but only different cellular contexts. The contextual logic is still empirical, not predictive.

---

## III. Vertical Chronicle — How the Field Was Built

The neurotrophin story is unusually well-documented because the founding experiments are tightly linked to specific enabling tools. The pattern that repeats is: **a tractable embryological model + a new biochemical or molecular tool → a discontinuous jump in understanding**.

### 1. 1934–1948 · The pre-NGF problem (enabling tech: limb-bud ablation in chick)
Viktor Hamburger removed limb buds from chick embryos and observed that motor and sensory neurons innervating the missing limb fail to develop or die. His interpretation was that targets supply an *inductive* signal that recruits neurons. The data, however, also admitted an alternative interpretation he didn't favour: that excess neurons are produced and that the target *selects* survivors by supplying a limiting factor.

### 2. 1948–1954 · The mouse-sarcoma experiments — birth of NGF (enabling tech: heterologous tumour graft + silver staining of nerves)
Elmer Bueker, a former Hamburger student, transplanted fragments of mouse sarcoma 180 onto chick embryos and noticed that sensory nerve fibres densely invaded the tumour. Rita Levi-Montalcini, working in Hamburger's lab, repeated and extended this with sarcoma 37 and applied silver-staining histology to map the response. She showed (i) sympathetic ganglia near the tumour were grossly enlarged, (ii) the effect propagated even when no direct vascular contact was permitted (tumour grafted onto the chorioallantoic membrane), implying a *diffusible humoral factor*, and (iii) the same factor stimulated sensory and sympathetic neurite outgrowth in culture. Her 1954 paper with Hamburger laid the foundation. By transferring tumour pieces to chick embryos she established a mass of cells "full of nerve fibres" — a halo of nerves around the graft that even invaded veins but spared arteries flowing back from the tumour, suggesting a tumour-released diffusible substance. **[E1, A]**

Goedert (cited in The Lancet obituary) emphasised the conceptual inversion: Hamburger had read the limb-ablation data as the loss of an attractive "inductive" factor; Levi-Montalcini postulated instead that the tissue normally produces something that *prevents nerve cells from dying*, and she set out to purify it. She turned out to be right. This reframed nervous-system development as a *selection* problem rather than an induction problem — the seed of the neurotrophic theory.

### 3. 1956–1960 · Purification — NGF as a protein (enabling tech: snake venom assay, mouse submandibular gland as super-source)
Stanley Cohen joined the laboratory in 1953 and applied biochemistry. Two extraordinary lucky breaks: snake venom (added as a putative nuclease control) turned out to be even more potent than the tumour, and the mouse submandibular gland of adult males proved to be the richest natural source. Cohen purified NGF protein in 1960. A sensory or sympathetic neuron reacted within 30 seconds to NGF addition; one billionth of a gram per ml exerted potent growth-promoting effects. **[E1]**

The clinching in-vivo demonstration came when anti-NGF antibodies were injected into neonatal mice and essentially abolished the sympathetic nervous system — a "beautiful experiment" that proved NGF was physiologically required, not merely sufficient, for vertebrate sympathetic development. "It proved beyond any doubt that NGF was physiologically essential for the functioning of the vertebrate nervous system." **[E1, A]**

In 1986 Levi-Montalcini and Cohen shared the Nobel Prize in Physiology or Medicine.

### 4. 1982–1992 · The family expands (enabling tech: protein purification from pig brain, then PCR cloning by homology)
For ~30 years NGF was the only known neurotrophin. In 1982 Yves-Alain Barde and Hans Thoenen purified a second factor from pig brain that supported survival of embryonic chick sensory neurons that NGF could not save; it was named brain-derived neurotrophic factor (BDNF). Sequencing was hard because the protein was so scarce. In 1989 Leibrock, Lottspeich, Hohn, Hofer, Hengerer, Masiakowski, Thoenen, and Barde reported the molecular cloning of BDNF in *Nature*, revealing it as a structural homologue of NGF — the first concrete evidence that NGF had relatives. **[E1, A]**

This unlocked a homology-cloning gold rush. Maisonpierre, Belluscio, Squinto, Ip, Furth, Lindsay, and Yancopoulos cloned NT-3 in 1990 by exploiting NGF–BDNF sequence similarity. NT-4 (independently cloned as NT-5 in mammals) followed in 1991–1992. NT-6 was found in teleost fish but has no mammalian orthologue. **[E1, A]**

### 5. 1991 · Trk receptors identified (enabling tech: cell-based binding + receptor cloning)
Until 1991 the molecular identity of high-affinity NGF binding was contested. Multiple groups (Kaplan, Hempstead, Squinto, Klein, Barbacid, Parada) converged on the conclusion that the proto-oncogene *trk* (TrkA), originally found as a colon-cancer fusion partner, was the NGF receptor tyrosine kinase. TrkB (BDNF, NT-4) and TrkC (NT-3) followed within months. This established the canonical pairing:

- NGF → TrkA → nociceptive and sympathetic neurons
- BDNF, NT-4 → TrkB → mechanoreceptive, hippocampal, cortical neurons
- NT-3 → TrkC → proprioceptive neurons (and TrkB/TrkA in some contexts)

All neurotrophins also bind p75NTR (a TNF-receptor-superfamily member) with low affinity, and p75NTR can contribute to high-affinity Trk binding or otherwise modulate Trk function. **[E1, A]**

### 6. 2001–2005 · Proneurotrophins as physiological death ligands (enabling tech: cleavage-resistant mutants, sortilin biochemistry)
Hempstead's group (Lee, Kermani, Teng, Hempstead 2001 *Science*) showed that proNGF — long assumed to be a non-secreted intermediate — is in fact secreted and binds p75NTR to *induce* apoptosis. Nykjaer and colleagues in 2004 identified sortilin (a Vps10p-domain protein) as the missing co-receptor: "Sortilin specifically recognises the prodomains of proNGF, proBDNF, and proNT-3 and forms a co-receptor complex with p75NTR to convey proneurotrophin-induced apoptotic signaling at subnanomolar concentrations." In 2005 Teng and colleagues extended this to proBDNF, demonstrating that proBDNF is secreted, binds sortilin, and in sympathetic neurons co-expressing sortilin and p75NTR it kills cells at sub-nanomolar concentrations, while mature BDNF (but not proBDNF) activates TrkB. **[E1, A]**

This created the "yin/yang" model of neurotrophin action: the same locus, post-translational processing, and the ligand-receptor stoichiometry of the local cellular microenvironment together determine whether a neurotrophin promotes survival or death.

### 7. 2003–2014 · The signaling endosome formalised (enabling tech: compartmented Campenot chambers, fluorescent NGF, microfluidics)
A long-standing question was how a signal received at the axon terminal — sometimes a metre away from the soma — sustains transcription-dependent survival programmes in the cell body. The signaling-endosome model crystallised: NGF binds TrkA at the distal axon, the complex is internalised into a Rab5-positive early endosome, matures into a transport-competent form, and is carried by dynein along microtubules back to the soma where it activates CREB-dependent transcription. In this model the NGF/TrkA endosome stays signalling-active throughout retrograde transport, sustaining downstream PI3K-Akt and Ras-ERK signalling; coronin-1 prevents lysosomal fusion at the soma so that signaling endosomes can be recycled. **[E1, A]** A particularly elegant control showed that NT-3, despite sharing TrkA at high concentrations, cannot sustain retrograde survival because the NT-3/TrkA complex dissociates in the acidic early endosome — so the endosomal compartment itself enforces ligand specificity. **[E2, A]**

### 8. 2019–2023 · Cancer neuroscience opens (enabling tech: patient-derived xenografts, optogenetics in xenografts, patch-clamp on glioma cells)
Although Levi-Montalcini's original system was *tumour*-derived nerve growth, the medical preoccupation for decades was developmental neurobiology. The pendulum has swung back. Two converging streams now anchor neurotrophin biology in oncology:

- **PNS — perineural invasion.** PNI is now formally recognised as a "fifth route" of cancer metastasis. NGF, BDNF, and GDNF axes between tumour cells, Schwann cells, and nerves are the dominant molecular substrate (§VI).
- **CNS — neural-circuit hijacking by gliomas.** Monje and colleagues showed that glioma cells form electrophysiologically functional AMPA-receptor-mediated synapses with neurons. The 2023 *Nature* paper went further: "BDNF–TrkB signalling promotes malignant synaptic plasticity… signalling through TrkB to CaMKII, BDNF promotes AMPA receptor trafficking to the glioma cell membrane, resulting in increased amplitude of glutamate-evoked currents. BDNF–TrkB signalling also regulates the number of neuron-to-glioma synapses. Blocking TrkB genetically or pharmacologically abrogates these effects and substantially prolongs survival in xenograft models of paediatric glioblastoma and diffuse intrinsic pontine glioma." **[E2, A]** This is a recent finding from a single research programme, and animal models, but the mechanistic detail is unusually deep.

---

## IV. Horizontal Comparison — Mechanism

### IV.1 The two receptor classes

**Trk receptor tyrosine kinases** are single-pass transmembrane proteins with an extracellular ligand-binding cassette (immunoglobulin-like and leucine-rich repeats) and an intracellular tyrosine-kinase domain. Ligand binding induces dimerisation and trans-autophosphorylation of conserved tyrosines (Y490, Y785 in TrkA numbering), which create docking sites for adaptors. Recruitment of Shc/Grb2/SOS launches Ras → MAPK/ERK (differentiation); IRS-1/PI3K → Akt activates pro-survival programmes by inhibiting BAD and forkhead transcription factors; PLCγ1 → IP3/DAG generates Ca²⁺ release and PKC activation regulating synaptic plasticity. **[E1, A]**

A useful axis-of-bias observation: "Some studies have suggested that NGF/TrkA coupling causes preferential activation of the Ras/MAPK pathway, whereas NT-3/TrkC coupling causes preferential activation of the PI3 pathway." This is a tendency, not a rule, and depends on cellular context. **[E2, A]**

**p75NTR** is a TNF-receptor-superfamily member with a death domain in its cytoplasmic tail. It binds all four mature neurotrophins with low affinity and binds proneurotrophins with high affinity in complex with sortilin. p75NTR does not have intrinsic catalytic activity; signaling is via recruited adaptors:

- **NRAGE, NADE, NRIF, TRAF6** → JNK activation, ceramide production, p53 / caspase signalling → apoptosis in the appropriate context.
- **TRAF6 → NF-κB** → pro-survival, particularly in Schwann cells and certain neurons.
- **Rho/Rac modulation** → growth-cone collapse / retraction (especially under proNGF + SorCS2).

A representative review summary captures the duality: "Pathways regulated by p75NTR include PI3K/AKT, MAPK, cAMP/PKA, and NF-κB, which can serve functions such as survival, antidegeneration, synaptic stability, but also apoptosis depending on adaptor recruitment and cell context". **[E1, A]**

The interplay matters: "Association of TrkB with p75NTR was necessary for optimal downstream signaling of the PI3K-Akt pathway, but not the Erk pathway, in hippocampal neurons… BDNF was unable to rescue p75NTR-knockout neurons from trophic withdrawal, suggesting p75NTR facilitates the ability of TrkB to activate PI3K and promote neuronal survival." So even where p75NTR is not the apoptotic gateway, it tunes Trk output. **[E2, A]**

### IV.2 Pro vs Mature — the yin/yang

| Property | Pro-form | Mature form |
|---|---|---|
| Receptor preference | p75NTR + sortilin (sub-nM) | Trk (kinase-active) |
| Dominant signal | JNK, ceramide, NF-κB | Ras-ERK, PI3K-Akt, PLCγ |
| Cellular outcome | Apoptosis, growth-cone collapse, LTD enhancement | Survival, differentiation, LTP |
| Regulation | Furin/PC cleavage intracellularly; plasmin/MMP-7 extracellularly | Downstream of proteolysis |

The implication is that **the secretion-to-cleavage ratio is itself a regulated variable** that can switch the same molecule from a survival to a death cue, with consequences for nervous-system sculpting (§V) and disease (§VI). In Alzheimer's disease in particular, brain proNGF accumulates while mature NGF is reduced, plausibly contributing to basal-forebrain cholinergic atrophy.

### IV.3 Retrograde signaling endosome — long-distance survival
A defining feature of neurons is the spatial separation between the site of trophic signal (axon terminal) and the genome (cell body). NGF/TrkA is internalised into a Rab5-positive early endosome (a pinocytic process facilitated by "Pincher"), matures with Rac1/cofilin recruitment that depolymerises local F-actin, and is then carried by dynein along microtubules towards the soma. Actin depolymerisation in distal axons is essential for retrograde trafficking of TrkA signaling endosomes; NT-3/TrkA endosomes lack these actin-regulatory components, which explains why NT-3 cannot support retrograde survival even though it activates TrkA. **[E2, A]** This is a mechanistically satisfying explanation for the long-puzzling "ligand-specificity-in-the-endosome" phenomenon.

The somatic readout is CREB-dependent transcription of survival genes; BAX translocation to mitochondria is held back, and the BH3-only proteins Bim, Puma, Bmf, and Dp5 are kept off. "NGF deprivation activates the mitochondrial pathway of apoptosis in sympathetic neurons; the expression of four BH3-only members (Dp5, Bim, Puma, Bmf) increases after NGF withdrawal." **[E1, A]**

### IV.4 Receptor cross-talk and modulatory partners
- **Sortilin** — death co-receptor for pro-forms.
- **SorCS2** — partners with p75 for proNGF-induced growth-cone collapse in sympathetic neurons.
- **NRH2 / PLAIDD** — p75 homologue that modulates sortilin trafficking.
- **NRP1 (Neuropilin-1)** — emerging co-receptor for mature NGF/TrkA in pain signalling (recent therapeutic interest).
- **Truncated TrkB.T1, TrkC.T1** — kinase-dead isoforms acting as decoys or scaffolds.

This combinatorial receptor logic is why the same ligand can drive opposite cellular outcomes depending on which co-receptor partners are co-expressed at what stoichiometry.

---

## V. Roles in Nervous-System Development

### V.1 The neurotrophic hypothesis, formally
Approximately half of neurons generated during embryogenesis die before adulthood. The neurotrophic hypothesis — empirically grounded by Levi-Montalcini's anti-NGF experiments and supported across the family — states that targets secrete a *limiting* amount of trophic factor, only those axons reaching and competing successfully for that supply survive, and the rest are eliminated by programmed cell death. This converts a developmental matching problem ("how do we generate the right number of presynaptic neurons for a given target field?") into a quantitative selection problem.

"The mechanism that determines the survival of an optimal number of neurons during development is explained by the neurotrophic hypothesis. Supplements of additional targets or appropriate neurotrophic factors rescue them from death." **[E1, A]**

### V.2 Knockout phenotypes — the most informative experiment per gene
Mouse loss-of-function studies map each NT and Trk onto specific neuronal populations, with striking specificity:

| Gene knocked out | Major phenotype |
|---|---|
| *Ngf* / *Ntrk1* (TrkA) | Loss of most TrkA⁺ nociceptive and thermoceptive DRG neurons; loss of sympathetic neurons; loss of basal-forebrain cholinergic phenotype; early postnatal lethality |
| *Bdnf* / *Ntrk2* (TrkB) | Vestibular ganglion neuron loss; sensory and motor deficits; lethal in first weeks |
| *Nt3* / *Ntrk3* (TrkC) | Loss of TrkC⁺ proprioceptors → severe ataxia; loss of subsets of cochlear, cardiac sympathetic, and mechanoreceptive sensory neurons; lethal |
| *Nt4* | Modest sensory neuron loss; viable into adulthood — the "odd one out" |
| *Ngfr* (p75NTR) | Sensory deficits, abnormal sympathetic innervation, but viable; reveals modulatory rather than essential role |

"Lack of functional NGF, BDNF and NT3 genes results in severe neuronal deficits and early postnatal death. NT4 is unique among the neurotrophins; the absence of NT4 results in limited sensory neuron loss but these mice do not die early, suggesting that NT4-dependent neurons are not critical for survival. Phenotypic analyses of mice lacking TrkA, B and C confirm that TrkA is the functional receptor for NGF, TrkB acts as the primary receptor for BDNF and NT4, and NT3 signals primarily through TrkC." **[E1, A]**

### V.3 Developmental switches — DRG and sympathetic ganglia
DRG neurons are not born committed to one neurotrophin dependency. "TrkA is expressed in nociceptive and thermoceptive sensory neurons; TrkC, the high-affinity receptor for NT-3, is expressed in proprioceptive neurons; and TrkB, the receptor for BDNF and NT-4, is expressed in less specifically characterized touch neurons." **[E1, A]** During early embryogenesis many DRG neurons express both TrkC and TrkA and depend on NT-3; later they down-regulate TrkC and switch to NGF/TrkA dependency. "trkA is expressed continuously in most neurons at both early and late stages, whereas trkC mRNA is downregulated in the majority of the neurons at later stages." **[E2, A]**

In the trigeminal and nodose/petrosal ganglia, NT-3 → NT-4 → BDNF act sequentially as different target tissues become innervated and competent to support distal axons. This is *not* redundancy — it is temporal handoff. **[E2, A]**

A particularly elegant cross-regulation:
"NGF/TrkA signaling suppresses NT3/TrkA signaling, sharpening the developmental switch from NT3- to NGF-dependent functions. p75NTR signaling at the axon terminus can locally regulate axonal growth cone collapse. However, p75NTR also can signal retrogradely from the axon terminus to the soma to induce neuronal cell death." The same receptor (TrkA) is read differently by the same cell depending on which ligand engages it. **[E2, A]**

### V.4 CNS roles in development and plasticity
BDNF is the dominant CNS neurotrophin in postnatal and adult brain. Its functions span:

- **Survival and differentiation** of cortical, hippocampal, striatal, GABAergic interneurons; particular importance for parvalbumin⁺ interneuron maturation.
- **Activity-dependent secretion** from glutamatergic synapses, with both autocrine and paracrine action.
- **Long-term potentiation (LTP).** BDNF is necessary for hippocampal LTP induction and maintenance; TrkB signalling drives AMPA-receptor insertion and dendritic spine remodelling. "BDNF is a key regulator of synaptic plasticity… (1) the Val-Met polymorphism in the pro-domain affects activity-dependent BDNF secretion and short-term, hippocampus-mediated episodic memory; (2) pro-BDNF and mBDNF, by interacting with their respective p75NTR and TrkB receptors, facilitate LTD and LTP, two common forms of synaptic plasticity working in opposing directions." **[E1, A]**
- **Long-term depression (LTD).** proBDNF binding p75NTR enhances LTD; this is the synaptic-level manifestation of the yin/yang principle.
- **Myelin plasticity.** BDNF promotes developmental and activity-dependent myelination by oligodendrocyte-lineage cells. **[E2]**

NGF in the adult CNS is most consequential for the basal-forebrain cholinergic neurons (BFCNs) of the nucleus basalis of Meynert and the septal nuclei, which project widely to cortex and hippocampus. NGF withdrawal in these neurons triggers a progressive, cholinergic-selective atrophy that is highly relevant to Alzheimer's disease (§VI.2). NT-3 and NT-4 play more focal CNS roles (cerebellar Purkinje cell development, certain brainstem populations) and are less centrally implicated in adult CNS plasticity.

---

## VI. Roles in Disease

### VI.1 Pain — the adult NGF surprise (PNS)
Although NGF is a developmental survival factor, in the adult its dominant role in TrkA⁺ DRG nociceptors is *modulatory*: sensitisation. Locally produced NGF (by injured tissue, mast cells, fibroblasts, immune cells in response to IL-1β, TNF-α) binds TrkA on peripheral nociceptive terminals, drives expression of TRPV1, Nav1.8, BDNF, substance P, and CGRP, and produces hyperalgesia. "Loss-of-function mutations in NGF signaling lead to congenital insensitivity to pain. Stephen McMahon and others showed that NGF sensitises adult tissue damage and injury-sensing neurons (nociceptors) in the dorsal root ganglion, thereby promoting pain." **[E1, A]**

This unlocked **tanezumab**, a humanised monoclonal antibody that sequesters NGF and prevents TrkA activation. "Tanezumab is a humanized monoclonal IgG2 antibody that blocks NGF from activating trkA receptors on nociceptive neurons. The inhibition of NGF in acute and chronic painful states is a novel mechanism of action, unlike opioids and NSAIDs." **[E1, A]** Phase 3 trials demonstrated meaningful pain reduction in moderate-to-severe osteoarthritis, low back pain, and bone-metastasis cancer pain. The development programme was, however, repeatedly placed on partial FDA clinical hold owing to two safety signals: **rapidly progressive osteoarthritis (RPOA)** and **anatomical changes in sympathetic ganglia**. Tanezumab was ultimately not approved by the FDA in the form submitted; the clinical-development story is now treated as a cautionary case study of the cost of perturbing a single neurotrophin axis chronically in adults. "A separate FDA partial clinical hold was placed on all NGF-Ab programs from 2012 to 2015 due to anatomical changes seen in the sympathetic nervous system." **[E1, A]**

### VI.2 Neurodegeneration — NGF and Alzheimer's disease (CNS)
Cholinergic-neuron loss is one of the earliest and most consistent cellular signatures of AD; severity correlates with dementia score better than amyloid plaque density alone. Because NGF is the trophic factor for basal-forebrain cholinergic neurons, NGF supplementation has been pursued therapeutically for ~25 years.

**Phase 1 ex-vivo gene therapy (Tuszynski et al., 2005).** Autologous fibroblasts engineered to express NGF were stereotactically implanted into the basal forebrain of eight mild-AD patients. The trial was safe; PET 18F-FDG uptake increased; "After mean follow-up of 22 months in six subjects, no long-term adverse effects of NGF occurred. Evaluation of the Mini-Mental Status Examination and Alzheimer Disease Assessment Scale–Cognitive subcomponent suggested improvement in the rate of cognitive decline. Serial PET scans showed significant increases in cortical 18-fluorodeoxyglucose. Brain autopsy from one subject suggested robust growth responses to NGF." **[E2, A]** Subsequent AAV2-NGF Phase 2 (CERE-110) was safe and demonstrated sustained expression, but did not significantly improve cognition. "In a recent clinical trial for AD, intraparenchymal AAV2-NGF delivery was safe but did not improve cognition. NGF gene expression persisted for at least 7 years at sites of AAV2-NGF injection." **[E2, A]** Post-mortem analysis identified inadequate spatial coverage of the nucleus basalis as a likely reason for the cognitive miss — the biology may still be valid even though that particular delivery approach was insufficient.

A complementary line of evidence: in AD brain, proNGF accumulates while mature NGF and TrkA are reduced, plausibly contributing to a *toxic* (p75/sortilin-mediated) rather than *trophic* (TrkA-mediated) signaling state on cholinergic neurons. Small-molecule **p75NTR modulators** (e.g. LM11A-31) that bias signaling away from death have entered clinical evaluation. **[E2–E3, B]**

### VI.3 Psychiatric disease — BDNF Val66Met (CNS)
A common single-nucleotide polymorphism in the *BDNF* prodomain (rs6265, c.196G>A, Val66Met) is one of the most-studied genetic variants in psychiatric neuroscience. The Met allele impairs activity-dependent trafficking of BDNF to dendrites and reduces depolarisation-evoked secretion. "In the mammalian brain, BDNF is synthesized as proBDNF, then cleaved into mature BDNF by the tPA/plasmin system. A common SNP rs6265 at codon 66 in the pro-domain converts valine to methionine. This amino acid substitution affects dendritic trafficking of pro-BDNF and alters the regulated secretion of BDNF." **[E1, A]**

Phenotypic correlates in humans include reduced hippocampal volume, impaired episodic memory, blunted LTP-like responses on TMS or sensory paradigms, and modest susceptibility associations with depression, anxiety disorders, and schizophrenia. The effect sizes are small and the cohort heterogeneity is large, so the variant should not be over-interpreted as a "depression gene"; it is better understood as a tractable handle on activity-dependent BDNF biology in humans.

### VI.4 Perineural Invasion — the PNS frontier of cancer neuroscience
Perineural invasion (PNI) is the histological finding of cancer cells within the nerve sheath or encircling ≥33% of a nerve circumference. It is recognised in pancreatic ductal adenocarcinoma (PDAC, ~80–100% of cases), prostate, head-and-neck squamous, adenoid cystic carcinoma, cervical, colorectal, biliary, and gastric cancers. Clinically it predicts poor local control, distant relapse, neuropathic pain, and reduced overall survival. "Perineural invasion (PNI) occurs when tumor cells invade the nerve sheath and/or encircle more than 33% of the nerve circumference. PNI is a common feature in various malignancies and is associated with tumor invasion, metastasis, cancer-related pain, and unfavorable clinical outcomes." **[E1, A]**

The molecular logic of PNI is a **bidirectional crosstalk** organised around neurotrophic and axon-guidance axes:

**Tumour → nerve (neuritogenesis, attraction of nerve fibres):**
- Cancer cells secrete **NGF, BDNF, GDNF, artemin (ARTN)** → bind TrkA, TrkB, GFRα–RET → axon outgrowth toward the tumour. "Cancer cells release neurotrophins like NGF, BDNF, GDNF, and artemin, which bind to receptors on nerve cells, promoting neurite outgrowth toward the tumor." **[E1, A]**
- This is functionally the **same molecular toolkit** Levi-Montalcini observed in 1948 with sarcoma 180 — the tumour-secreted "nerve-growth factor" of her chick embryo experiments is the prototype of cancer-secreted neurotrophin in PNI.

**Nerve → tumour (chemotaxis of cancer cells onto nerves):**
- Schwann cells and neurons secrete **GDNF, NGF, ARTN, CXCL12 (SDF-1)** → bind RET, TrkA, CXCR4 on tumour cells → directed migration along nerves. "Neural structures release factors such as NGF, GDNF, ARTN, and CXCL12, which act as chemoattractants for cancer cells expressing corresponding receptors." **[E1, A]**

**Schwann-cell reprogramming — a recently appreciated central node:**
Schwann cells in the perineural niche revert to a *repair-like, dedifferentiated, c-Jun-positive* state — the same programme that normally enables axon regeneration after nerve injury. In the tumour context, this generates **tumour-activated Schwann cell tracks (TASTs)** that mechanically guide cancer cells along nerves. "SCs play critical roles in cancer invasion, as tumor-activated Schwann cell tracks (TASTs) dynamically form migration pathways for cancer cells through c-Jun-dependent reprogramming, analogous to nerve repair processes." **[E2, A]**

The reprogramming can be initiated by tumour-derived neuropeptides, extracellular vesicles, and neurotrophins themselves:
- "Neuromedin B (NMB) produced by cervical cancer cells induces PNI by reprogramming Schwann cells, including driving their morphological and transcriptional changes, promoting their proliferation and migration, and initiating PNI by secreting CCL2 and directing axon regeneration." **[E2, A]**
- "NGF activates autophagy of SCs via the p75NTR/AMPK/mTOR axis. Cancer-cell-derived NGF upregulates ATG7 expression in Schwann cells; this autophagy promotes the outgrowth of nerve axons, acting as a bridge in PNI in pancreatic cancer." **[E2–E3, A]**
- "Pancreatic-cancer-derived extracellular vesicles activate Schwann cells via IL-8/CCL2, priming them to enhance cancer-cell invasiveness." **[E3, A]**

**Adhesion and matrix remodelling.** L1CAM, NCAM, MMPs (especially MMP-2 and MMP-9), and laminin/integrin α6β1 interactions glue cancer cells to nerves and degrade the perineurium so that cells can enter the endoneurial space.

**Pain via the same axes.** Cancer-derived NGF and BDNF that promote PNI also sensitise nociceptive afferents that have invaded the tumour. "NGF activates receptor tyrosine kinase A (TrkA) and NGF receptors (NGFR), inducing SP and CGRP release and modulating inflammatory cytokine levels… BDNF-TrkB signaling facilitates PNI and nociceptive behavior in HNC models. Members of the GDNF family, including GDNF, neurturin (NRTN), and Artemin, enhance TRPV1 receptor sensitivity, intensifying pain perception." **[E2, A]** Pancreatic-cancer pain — historically described as among the most severe in oncology — is in large part a perineural-niche phenomenon.

**Therapeutic implications.** "Targeting neurotrophic axes (GDNF/RET, NGF/TrkA) and metabolic pathways (e.g., lactate transport) may disrupt nerve-tumor crosstalk, while reversing cholinergic immunosuppression or enhancing CD161⁺CD8⁺ T-cell cytotoxicity could reshape immune responses." **[E2, A]** Drugs already in or near the clinic that intersect with these axes include selective RET inhibitors (selpercatinib, pralsetinib), pan-Trk inhibitors (larotrectinib, entrectinib — currently approved for *NTRK*-fusion tumours but mechanistically relevant), anti-NGF antibodies (re-evaluated for cancer pain rather than chronic non-cancer pain after the RPOA experience), and β-blockers (for adrenergic-driven tumour growth, a related cancer-neuroscience axis not covered in detail here).

### VI.5 "Perineural invasion in the CNS" — definitional caution, with two real phenomena

The user's phrasing requires clarification because "PNI in the CNS" is not a standard pathological diagnosis. The CNS proper has neither Schwann cells nor the layered nerve sheath (perineurium/epineurium) that defines PNS perineural anatomy. Two distinct but real phenomena occupy the space the term suggests:

**(a) Perineural spread of head-and-neck or cutaneous cancers retrogradely along cranial nerves *into* the intracranial compartment.** This is well established radiologically and clinically. "Perineural spread is a well-recognized phenomenon in head and neck cancers. SCCs are the most frequent neoplasms to exhibit this behavior, followed by adenoid cystic carcinoma, lymphoma, and rhabdomyosarcoma. The trigeminal and facial nerves are most commonly affected. MRI is superior to CT in evaluation of soft tissue tumors and in its ability to discriminate between normal and tumor tissue, providing a more accurate assessment of intracranial spread to the Meckel cave, the cavernous sinus, the cisternal portion of the trigeminal nerve, and the facial nerve in the internal auditory canal." **[E1, A]** Cutaneous squamous-cell carcinoma and adenoid cystic carcinoma in particular use the trigeminal (V) and facial (VII) nerves as conduits from face/scalp/parotid up through the skull base into the cranial cavity. Mechanistically, the same NGF/TrkA and BDNF/TrkB axes documented in pancreatic PNI are implicated, but the histology and clinical management (often combined surgery and skull-base-directed radiotherapy) differ. Once tumour reaches the cisternal segment of a cranial nerve it is, in a meaningful sense, in the CNS — but the *route* was the PNS sheath.

**(b) Neural-circuit hijacking by gliomas — the closest CNS-intrinsic analogue.** Gliomas don't have PNS-style perineural sheaths to invade. Instead they appear to exploit **electrical and trophic features of healthy neural circuits** to grow and invade. The two best-characterised mechanisms both involve BDNF/TrkB:

- *Activity-dependent BDNF secretion drives glioma growth.* In healthy cortex, neuronal activity triggers BDNF release into the parenchyma where it acts on TrkB-bearing neurons and glia. Glioma cells express functional TrkB and intercept this signal; the response is proliferation and migration.
- *Neuron-to-glioma synapses are subject to BDNF-mediated potentiation.* Monje and colleagues showed that glioblastoma and DIPG cells form AMPAR-mediated post-synaptic structures opposite glutamatergic neurons. "BDNF–TrkB signalling promotes malignant synaptic plasticity and augments tumour progression… Signalling through TrkB to CAMKII, BDNF promotes AMPA receptor trafficking to the glioma cell membrane, resulting in increased amplitude of glutamate-evoked currents. BDNF–TrkB signalling also regulates the number of neuron-to-glioma synapses. Abrogation of activity-regulated BDNF secretion from the brain microenvironment or loss of glioma TrkB expression robustly inhibits tumour progression. Blocking TrkB genetically or pharmacologically… substantially prolongs survival in xenograft models of paediatric glioblastoma and diffuse intrinsic pontine glioma." **[E2, A]**

This is conceptually parallel to PNS PNI: in both cases, cancer cells exploit a neurotrophin/Trk axis that the host nervous system uses for normal trophic and plastic functions. The *anatomy* is different (sheath migration vs synapse formation), but the *receptor logic* is shared. The implication is that we should expect a partly overlapping pharmacology — pan-Trk inhibitors, BDNF/NGF axis antagonists — to be exploited across both peripheral PNI and CNS glioma indications, with disease-specific safety and efficacy profiles. **[E2, A]**

A separate CNS-glioma invasion mode worth flagging is **perivascular invasion**: glioma stem-like cells use blood vessels as scaffolds. The molecular drivers here include EphrinB2 and CXCR4, with neurotrophins playing a less central role. **[E2, B]**

---

## VII. Mismatch Analysis — What Older Techniques Missed, What Newer Ones Add

This step is required by the analytic framework and is particularly informative here because the neurotrophin field's history is a textbook example of how each new technology layer changed conclusions, not just resolution.

### What older techniques (bulk histology, ³H-thymidine, biochemical assays on whole ganglia) could not see
1. **Cell-type heterogeneity within ganglia.** DRG and trigeminal ganglion neurons were treated as roughly homogeneous "nociceptive" or "mechanoreceptive" populations. We now know there are at least 10–15 transcriptomically distinct DRG sub-types, each with characteristic Trk, p75, ion-channel, and neuropeptide expression. Bulk knockouts produced average phenotypes that obscured this.
2. **Pro vs mature ligand distinction.** Bulk Western blots run with antibodies that recognised both forms reported "NGF levels" or "BDNF levels" that conflated functionally opposite ligands.
3. **Endosomal compartmentalisation.** Static receptor-localisation data could not resolve the dynamic endosomal trajectories that we now know enforce ligand specificity.
4. **Schwann-cell plasticity in tumour context.** Standard histopathology of PNI documents *that* tumour cells are around nerves but not *what the Schwann cells are doing*. Recent work re-frames Schwann cells from passive bystanders to active orchestrators (TASTs).

### What older techniques would *mis*-see
1. **2D sections through 3D nerve-tumour interfaces** create the impression of "encirclement" or "skip lesions" that may be artefacts of section angle.
2. **Co-expression in tissue sections** has historically been read as direct functional interaction; in the perineural niche this is particularly dangerous because the relevant interactions are dynamic and may be transient.
3. **In situ hybridisation for receptor mRNA** can be discordant with surface receptor protein and active signaling state. NTRK1 transcript ≠ TrkA protein ≠ phospho-TrkA ≠ ligand-bound endosome.

### What newer technologies add
- **scRNA-seq of DRG, sympathetic, and trigeminal ganglia** has produced consensus subtype catalogues (Usoskin, Zeisel, Sharma, Renthal). Trk receptor logic now maps cleanly onto sub-types in human and mouse, with partial cross-species differences. **[E2]**
- **Conditional and inducible knockouts** separate developmental from adult roles of each NT/Trk pair.
- **Live imaging in microfluidic compartmented chambers** has validated and quantified the signaling-endosome model.
- **Patient-derived organoids, co-culture with dorsal-root-ganglion explants, and microfluidic axon-tumour chambers** allow direct measurement of cancer-nerve chemotaxis and Schwann-cell reprogramming. **[E2]**
- **Patch-clamp and optogenetics in glioma xenografts** have produced direct physiological evidence of neuron-to-glioma synapses and BDNF-mediated plasticity. **[E2]**

### Have these new tools *changed* conclusions, or only refined them?
- **Paradigm shifts.** ProNT biology, signaling-endosome compartmentalisation, Schwann-cell reprogramming in PNI, and glioma-neuron synapses each changed the *question* (not just the answer). These are not description upgrades.
- **Description upgrades.** Sub-type-resolved Trk expression maps refine but do not overturn the canonical NT–Trk pairing. They do, however, change *which drug targets at which subtype* one would propose.
- **Open.** Whether human neurotrophin biology recapitulates mouse closely enough for many translational claims is still incompletely settled — in particular for cortical BDNF biology (where humans have unique cell types and circuits), and for cancer neuroscience (where xenografts in immunodeficient mice cannot recapitulate the immune layer of the perineural niche).

---

## VIII. Evidence Boundaries and High-Risk Mis-interpretation Points

- **Model-system extrapolation.** Most knockout and rescue data are mouse. Human DRG neurons and human cortical BDNF biology differ enough in detail that any quantitative translation should be made cautiously.
- **Transcript vs protein vs function.** NTRK1/2/3 mRNA does not predict TrkA/B/C protein, nor signaling-competent receptor, nor active ligand-bound endosomes. Antibody-validation is non-trivial for Trk proteins.
- **Spatial proximity vs functional interaction.** In PNI tissue sections, nerve and tumour adjacency is necessary but not sufficient evidence of crosstalk. Functional validation requires co-culture, conditioned-media, and rescue experiments.
- **Observation vs causation.** Many human BDNF Val66Met associations and human serum-BDNF correlates are statistical and not yet linked to mechanism in a tissue-of-origin manner. Confounding by exercise, BMI, comorbidity, and antidepressant use is substantial.
- **Platform-driven artefacts in cancer neuroscience.** Microfluidic and xenograft conclusions depend strongly on Schwann-cell line choice (sNF96.2 vs primary), neuronal source (DRG explant vs iPSC neuron), and matrix composition. Drug efficacy in these systems should be triangulated across at least two platforms before clinical extrapolation. **[E2 caveat]**

---

## IX. Open Questions and Missing Links

1. **A unified model of context-dependent neurotrophin action.** Why does the same NGF/TrkA axis sustain BFCNs in development, hypersensitise nociceptors in adult inflammation, drive perineural invasion in PDAC, and become toxic (via proNGF/p75) in AD? Most current explanations are local and post-hoc. A predictive, quantitative framework is missing.
2. **Cross-talk between pro and mature pools.** What controls the ratio in vivo, and is it actively regulated in disease? Proteolytic balance (furin, plasmin, MMP-7, MMP-9) is a candidate convergence point.
3. **Combination of cancer-neuroscience axes.** PNI in PDAC involves NGF, BDNF, GDNF, axon-guidance ligands, chemokines, and Schwann-cell reprogramming simultaneously. Whether single-axis blockade is sufficient or whether multi-axis cocktails are required is unsettled.
4. **CNS-PNS unification.** Is glioma's neuron-circuit hijacking mechanistically a "central PNI"? If so, can we transfer pancreatic-PNI lessons (targeting Schwann-cell-like plasticity, anti-NGF antibodies, RET inhibitors) to CNS tumours, with TrkB blockade as a particularly attractive shared node?
5. **Why NT-4 is the "odd one out."** The mild knockout phenotype suggests either deep functional redundancy with BDNF or a role we still mis-measure (sub-population specificity, role in adult plasticity only, etc.).
6. **Human-specific BDNF biology.** Cortical cell types unique to primates and humans (e.g. specific interneuron classes) are not well captured by rodent BDNF/TrkB knockouts.

---

## X. Practical Synthesis for Different Audiences

- **For a developmental neurobiology audience.** Treat neurotrophins as a *limiting, target-derived, retrograde-signalling family* whose four members enforce population-level matching between presynaptic neurons and their targets. The yin/yang of pro vs mature forms and the sequential NT-switches during ganglion maturation are the contemporary refinements.
- **For a pain-medicine audience.** Adult NGF is the master sensitiser of TrkA⁺ nociceptors. Anti-NGF antibodies (tanezumab class) work for osteoarthritis, low back pain, and bone-metastasis cancer pain, but chronic systemic NGF blockade has cost (RPOA, sympathetic remodelling).
- **For a neurodegeneration audience.** BFCN-targeted NGF support remains conceptually sound for AD; clinical translation has been delivery-limited, not biology-limited. The proNGF / p75NTR toxic axis is the active counter-balance.
- **For a cancer-neuroscience or surgical-oncology audience.** Treat PNI as an *active, druggable, bidirectional* signalling niche organised around NGF/TrkA, BDNF/TrkB, and GDNF/RET, with Schwann-cell reprogramming as a recently appreciated convergence node. For head-and-neck and cutaneous tumours, perineural spread can reach the intracranial compartment via cranial-nerve conduits; imaging surveillance and skull-base-directed radiotherapy matter. For glioma, BDNF/TrkB blockade plus AMPAR antagonism (perampanel-class) is an emerging combination strategy with strong preclinical rationale.

---

## XI. Key References (verified in this research session)

### Foundational / discovery
- Levi-Montalcini R, Hamburger V. Effects of mouse sarcomas 180 and 37 on the spinal and sympathetic ganglia of the chick embryo. *J Exp Zool* 1953/1954. (Foundational.) **[E1, B]**
- Cohen S, Levi-Montalcini R. A nerve growth-stimulating factor isolated from snake venom. *PNAS* 1956. **[E1, B]**
- Levi-Montalcini R. The nerve growth factor 35 years later. *Science* 1987; 237: 1154–1162. **[E1, B]**
- Nobel Prize in Physiology or Medicine 1986 — press release, nobelprize.org. **[A]**
- *The Lancet* Obituary: Rita Levi-Montalcini. 2013. **[A]**

### Family expansion and receptor identification
- Barde Y-A, Edgar D, Thoenen H. Purification of a new neurotrophic factor from mammalian brain. *EMBO J* 1982; 1:549–553. **[E1, B]**
- Leibrock J, Lottspeich F, Hohn A, Hofer M, Hengerer B, Masiakowski P, Thoenen H, Barde Y-A. Molecular cloning and expression of brain-derived neurotrophic factor. *Nature* 1989; 341:149–152. **[E1, B]**
- Maisonpierre PC, Belluscio L, Squinto S, Ip NY, Furth ME, Lindsay RM, Yancopoulos GD. Neurotrophin-3: a neurotrophic factor related to NGF and BDNF. *Science* 1990; 247:1446–1451. **[E1, A]**
- Götz R et al. Neurotrophin-6 is a new member of the nerve growth factor family. *Nature* 1994; 372:266–269. **[E2, A]**

### Mechanism — signaling, retrograde transport, proneurotrophins
- Reichardt LF. Neurotrophin-regulated signalling pathways. *Phil Trans R Soc B* 2006. **[E1, A]**
- Lee R, Kermani P, Teng KK, Hempstead BL. Regulation of cell survival by secreted proneurotrophins. *Science* 2001; 294:1945–1948. **[E1, A]**
- Nykjaer A et al. Sortilin is essential for proNGF-induced neuronal cell death. *Nature* 2004; 427:843–848. **[E1, A]**
- Teng HK, Teng KK, Lee R, Wright S, Tevar S, Almeida RD, Kermani P, Torkin R, Chen Z-Y, Lee FS, Kraemer RT, Nykjaer A, Hempstead BL. ProBDNF induces neuronal apoptosis via activation of a receptor complex of p75NTR and sortilin. *J Neurosci* 2005; 25:5455–5463. **[E1, A]**
- Harrington AW et al. Recruitment of actin modifiers to TrkA endosomes governs retrograde NGF signaling and survival. *Cell* 2011; 146:421–434. **[E1, A]**
- Harrington AW, Ginty DD. Long-distance retrograde neurotrophic factor signalling in neurons. *Nat Rev Neurosci* 2013; 14:177–187. **[E1, A]**

### Development — knockouts and target dependence
- Snider WD. Functions of the neurotrophins during nervous system development: what the knockouts are teaching us. *Cell* 1994; 77:627–638. **[E1, B]**
- Kristiansen M, Ham J. Programmed cell death during neuronal development: the sympathetic neuron model. *Cell Death Differ* 2014; 21:1025–1035. **[E1, A]**
- Bibel M, Barde Y-A. Neurotrophins: key regulators of cell fate and cell shape in the vertebrate nervous system. *Genes Dev* 2000; 14:2919–2937. **[E1, B]**

### Pain
- McMahon SB et al. NGF and the dorsal root ganglion (multiple primary studies, 1990s–2000s).
- Hefti F. Pharmacology of nerve growth factor and discovery of tanezumab, an anti-NGF antibody and pain therapeutic. *Pharmacol Res* 2020. **[E1, A]**
- Mantyh PW et al. Anti-NGF therapy in cancer pain and arthritis. (Reviews.) **[E1]**

### Alzheimer's disease and NGF
- Tuszynski MH et al. A phase 1 clinical trial of nerve growth factor gene therapy for Alzheimer disease. *Nat Med* 2005; 11:551–555. **[E2, A]**
- Castle MJ et al. Postmortem analysis in a clinical trial of AAV2-NGF gene therapy for Alzheimer's disease identifies a need for improved vector delivery. *Hum Gene Ther* 2020. **[E2, A]**

### BDNF Val66Met
- Egan MF et al. The BDNF val66met polymorphism affects activity-dependent secretion of BDNF and human memory and hippocampal function. *Cell* 2003; 112:257–269. **[E1, B]**
- Chen Z-Y et al. Variant BDNF (Val66Met) alters the intracellular trafficking and activity-dependent secretion of wild-type BDNF. *J Neurosci* 2004; 24:4401–4411. **[E1, B]**

### Perineural invasion (PNS)
- Liebig C, Ayala G, Wilks JA, Berger DH, Albo D. Perineural invasion in cancer: a review of the literature. *Cancer* 2009; 115:3379–3391. **[E1, B]**
- Jurcak NR, Rucki AA, Muth S, Thompson E, Sharma R, Ding D et al. Axon guidance molecules promote perineural invasion and metastasis of orthotopic pancreatic tumors in mice. *Gastroenterology* 2019; 157:838–850. **[E2, B]**
- Hirth M et al. CCL2/CCR2 and CXCL10/CXCR3 in pancreatic cancer perineural invasion. **[E2, B]**
- Zhang Z et al. Significance and mechanisms of perineural invasion in malignant tumors. *Front Oncol* 2025. **[E1, A]**
- Frontiers (2024). Hallmarks of perineural invasion in pancreatic ductal adenocarcinoma: new biological dimensions. **[E1, A]**
- Bin J et al. Autophagic Schwann cells promote perineural invasion mediated by the NGF/ATG7 paracrine pathway in pancreatic cancer. **[E2, A]**
- Cervical cancer NMB-Schwann cell reprogramming paper (PMC11364772). **[E2, A]**

### Perineural spread (cranial nerves, CNS-adjacent)
- Williams LS et al. MRI-based zonal classification of perineural tumour spread along V and VII. **[E2, B]**
- Frontiers in Immunology 2025 — Perineural invasion as a neuro-immune niche in head and neck cancer. **[E1, A]**
- Insights into Imaging (2018). Easily detected signs of perineural tumour spread in head and neck cancer. **[E1, A]**

### Glioma neuroscience and BDNF/TrkB
- Venkatesh HS et al. Neuronal activity promotes glioma growth through neuroligin-3 secretion. *Cell* 2015; *Nature* 2017. **[E1, B]**
- Venkatesh HS et al. Electrical and synaptic integration of glioma into neural circuits. *Nature* 2019; 573:539–545. **[E1, B]**
- Taylor KR et al. Glioma synapses recruit mechanisms of adaptive plasticity. *Nature* 2023; 623:366–374. **[E2, A]**
- Monje M. The neuroscience of cancer (review). *Nature* 2024. **[E1, A]**

---

## XII. Recommended Next-Step Investigations

1. **Cross-platform replication** of glioma BDNF/TrkB findings in adult IDH-wildtype glioblastoma and adult-onset diffuse glioma (most current published evidence is in DIPG / paediatric GBM xenografts).
2. **Combinatorial blockade trials** in pancreatic PNI: anti-NGF + selective RET inhibitor + Schwann-cell-reprogramming inhibitor (c-Jun pathway), with neuropathic-pain endpoint as a secondary read-out.
3. **Pro-form-selective therapeutics.** Small molecules or biologics that selectively block proNGF or proBDNF interaction with sortilin (sparing mature-NGF/TrkA trophic signaling), particularly for AD and after spinal cord injury.
4. **Single-cell spatial profiling** of human PNI specimens with subcellular resolution (MERFISH, CosMx, Stereo-seq) to map Trk and p75 signaling states across the tumour-Schwann-cell-axon interface.
5. **Pharmacology of TrkB partial agonists.** Full agonists are problematic (epileptogenic, edema risk), but tuned ago-allosteric modulators could rescue BDNF deficits in AD or depression without driving glioma.

---

*End of report.*
