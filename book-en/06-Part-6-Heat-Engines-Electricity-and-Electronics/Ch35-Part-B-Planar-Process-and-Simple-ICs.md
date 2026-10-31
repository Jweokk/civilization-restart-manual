---

# Chapter 35 · Part B: Planar Process and Simple Integrated Circuits (35.B)

> Continues from Part A: the wafer now enters oxidation / photolithography / diffusion / metallization / packaging. The end-of-chapter fixed blocks (parameter master table / failure modes / acceptance, etc.) are placed at the end of this Part B file.
### 35.B.0 Part B Introduction: Failure in the Surface World Is Random

## Pre-Start Verification (Part B)

| 1 | Wafer | Cleared by Part A: mirror finish + parallelism record |
| 2 | Materials | Item-by-item check against the 35.B material unlock status declaration (current state of the chromium / silver / HF three lines) |
| 3 | High temperature | Diffusion-furnace temperature control handled per the Chapter 34 not-yet-unlocked status |

## 35.B Material Unlock Status Declaration (new this round; read first)

Three key materials of Part B are **not yet unlocked**; unlock conditions are given item by item. While locked, this chapter is positioned as a **development-assault roadmap**, not an executable chapter:

| Material | Use | Status | Unlock condition |
|---|---|---|---|
| Dichromate (gelatin photosensitive resist) | Photoresist | Chrome ore source not surveyed (Class-C dependency, Chapter 19); hexavalent chromium strongly carcinogenic | Chromite → chromate line (new section added to Chapter 23); or the alternative system "albumin–iron-salt photosensitive resist" (registered, pending verification) |
| HF/BHF | Window etching | Frozen at Section 23.14 | Unlocked once the five conditions of Section 23.14 are all met (calcium preparation via the Section 23.9.4 calcium chloride line, sealed enclosure, burn treatment, waste-acid neutralization, dedicated crew) |
| Silver paste (fine silver powder) | Interconnect | Silver ore "registered only, not pursued" (Chapter 16); no cupellation silver-recovery line | Lead-ore cupellation → silver nitrate → reduced silver powder line (new section added to Chapter 23); with no silver, interconnect downgraded to registered status |

**First-article trial order**: first run the chromium-free, silver-free alternative line "albumin–iron-salt resist + copper interconnect" to verify the process window; the original chromium/silver/HF three lines advance per their unlock conditions.


Part B enters the surface world: the oxide layer is only half a micrometer thick, pattern line widths half a millimeter — at every scale, **a single grain of dust is a workpiece**. In Part A a failure ruins one ingot, and the test-piece system intercepts it; in Part B a failure ruins one pattern, intercepted by **wafer-by-wafer, layer-by-layer visual inspection + witness-wafer calibration + yield statistics**. The handover interface between the two parts is a single rule: the wafer travels with its card. Part B rejects any wafer whose Part A records are incomplete — this is not bureaucracy; it is the only chain of responsibility when troubleshooting.

### 35.B.1 Part B Materials List

| Material | Acceptance standard | Minimum specification | Acceptable substitute (penalty) | Signs of a bad lot | Consumption |
|---|---|---|---|---|---|
| Grade A/B wafers | Wafer travel card complete in all five columns | Grade A from Part A for devices | Grade B as witness wafers only | No card; fingerprints; water stains | 5–10 wafers per wafer run |
| High-purity water | Distillation grade of Chapter 26 | No suspended matter; self-proven by the water-film test | Boiled rainwater (particle-laden; coarse rinsing only) | Has odor; floating film | 5–10 L per wafer run |
| HF / buffered etchant | Concentration registered per Chapter 26 | HF, 40% grade | — | Turbid (already contaminated) | 50–100 mL per window-etching batch |
| Saturated ammonium fluoride solution | Residual crystals at the bottle bottom | Self-made (HF neutralized with ammonia) | Dilute pure HF (etches 3–5× faster; undercutting runs away; ragged window edges) | — | Same as above |
| Gelatin | Odorless; fully soluble, no residue | Purified hide glue | Fish glue (harder; develops slower) | Putrid odor (already moldy); turbid after dissolving | 8–10 g per batch |
| Ammonium dichromate | Orange-red crystals | Stored dark and dry | Potassium dichromate (lower solubility; the resist solution crystallizes easily) | Deliquesced and caked; darkened color | 1.5–2.5 g per batch |
| Boric acid / ammonium dihydrogen phosphate | Chapters 23, 34 | Dry, no caking | Borax (contains sodium; use with caution and register) | Absorbs moisture and cakes | 1–5 g per furnace run |
| Sodium hydroxide | Industrial grade | Chapter 26 | Potassium carbonate (weaker anisotropy) | Heavy sodium carbonate contamination | 150–400 g per bath |
| Fine silver powder / glass frit | No grittiness between fingertips | Classified by ball milling and water elutriation | Cut-up silver-foil flakes (coarse paste; high open-line rate) | Blackened (oxidized into clumps) | 5–10 g silver powder per batch |
| Rosin, turpentine | Chapters 8, 26 | — | Honey as vehicle (much foaming during binder burnout) | Cloudy turpentine | 2–4 g per batch |
| Copper sulfate, dilute HF | Chapter 26 | For staining | — | — | 5–10 mL per junction-depth measurement |

### 35.B.2 Part B Tools List

| Tool | Source chapter | Precision requirement | Calibration before use |
|---|---|---|---|
| Two-zone oxidation/diffusion furnace | 12, 25, 34 | Main furnace ±5 °C; source furnace ±10 °C | Thermocouple cross-check + measured three-point furnace-temperature profile |
| Steam-generation flask and gas line | 26 + this chapter | Water-bath thermometer in place | Dry empty run to drive off residual water |
| Slow-rotation coating table / concentric-circle glass rod | 21 + this chapter | Table surface level | Leveled with a bubble level |
| Carbon arc lamp (with condenser and light shroud) | 32, 24 | Lamp distance lockable | Re-verify the day's sensitivity with the witness-wafer time gradient before exposure |
| Exposure clamping fixture | 21 + this chapter | Four-point symmetric screw pressure + compliant backing pad | One trial press with a verification wafer |
| Photomasks (≥2 working masks per pattern) | 42.7 + 35.B.7 of this chapter | Distortion calibration on file | Polarity checklist |
| Constant-temperature water bath and thermometer | 25 | ±2 °C | Two-point check: ice water / boiling water |
| Etching baths (dedicated labels) | 26 | HF bath and alkali bath stored physically apart | — |
| Screen-printing station (silk mesh on frame, squeegee) | 15, 26 | Uniform mesh tension | One blank print to check uniformity |
| Probe test station | 24, 27, 31 | Micropositioner travel covers the chip area | Probe tips inspected under a microscope; regrind when dull |
| Simple clean enclosure | 35.B.15 of this chapter | Wet cleaning; oilcloth floor; vessels covered | Daily settling-dust check (glycerin-coated slide laid flat for 1 h; count particles) |

### 35.B.3 The Road to Integration: From Discrete Components to the Planar Process

**What an integrated circuit is** (retained from Section 35.1): in a discrete-component circuit (Chapter 33), the transistor, resistors and capacitors are each packaged separately and joined by wires — **the wiring takes up volume, and every solder joint is a failure point**; an integrated circuit puts the transistor, resistors and the rest **inside the same semiconductor substrate, with interconnection completed on the chip** — wires become patterns on the substrate surface, and the "soldering" between components becomes process steps. Three benefits: small size, fewer joints (reliability), proportional replication (one wafer produces several chips at once).

**First-article route choice (an engineering decision, not an ideology)** (retained from Section 35.2):

- Route A (**Kilby-style hybrid**): the transistor is made on a germanium substrate, and resistors and capacitors are attached as discrete small pieces inside the same package and interconnected — **"integration" starts at the package level**; lowest process threshold; validates that the whole value chain works;
- Route B (planar process): build devices and interconnects layer by layer on a silicon wafer by oxidation–photolithography–diffusion — true integration, and the main development target of this chapter;
- Decision: **A first, to prove out packaging and testing; B as the main development assault** — the first "integrated circuit" may take form A, honestly labeled with its integration level;
- Point-contact parallel route (germanium; the Chapter 33 cat's-whisker structure made three-terminal): its process is independent of the planar process and advances simultaneously as Plan B — wherever the planar process gets stuck, that is the fallback, not an upgrade.

**Why transistors can be integrated** (retained from Section 35.3): the transistor's three regions are essentially two adjacent pn junctions in one crystal — **selective doping creates multiple devices on the same wafer**: doped regions are the components, undoped regions are substrate and isolation; a resistor = a suitably doped silicon strip (its value set by length, width and doping); a capacitor = two conductor layers sandwiching an oxide layer (the Chapter 33 capacitor structure in miniature). The universality of the planar process: oxidation (masking) → photolithography (window opening) → diffusion (doping/shaping) → metallization (interconnect) — **this four-step cycle builds circuits of any number of layers** — which is exactly why it is worth the assault.

### 35.B.4 Bird's-Eye View of the Full Flow and First-Article Design

Full flow (step details in 35.B.5–35.B.11; the Section 35.4 flow retained with layer annotations):

```
Wafer cleaning → thermal oxidation (grow the masking oxide) → coat resist → contact exposure → develop (pattern transferred into the resist)
→ HF etch to open windows (pattern transferred into the oxide) → strip resist → high-temperature diffusion (doping into the windows)
→ re-oxidation / re-lithography (next layer) → metallization (interconnect) → dicing → packaging → test
```

**Layer count of the first-article layout (the honest count)**: an npn-plus-resistor DTL gate needs **four-mask overlay** — a base (boron) mask, an emitter (phosphorus) mask, a contact-hole mask, and an interconnect screen mask. Every added mask multiplies the yield by another factor; layer count is a cost locked in at design time.

**Acceptance of each cycle**: visual inspection (magnifier/microscope) + spot checks (resistivity / junction characteristics) — the Chapter 22 "first-article inspection + spot-check" system replicated on a chip.

### 35.B.5 Thermal Oxidation: Masking Layer, Passivation Layer, and Dielectric

**Oxidation system**: quartz-tube furnace (main furnace 1000–1200 °C) + upstream steam-generation flask (distilled-water bath at 60–95 °C; the hotter the water, the denser the steam) + gas flow (dry air or oxygen, small and steady — set by counting bubbles through a bubbler bottle at 2–5 bubbles per second; empirical value, to be back-calibrated from the oxidation rate).

**Dry versus wet oxidation** (retained from Section 35.6): wet oxidation (carrier gas carries steam into the furnace) grows about 3–5× as fast as dry oxidation (empirical rule; calibrate in the field with stepped wafers from the same furnace: pull test pieces at different times within one run to form a step ladder). The first masking oxidation uses wet oxidation: **wet oxidation at 1100 °C gives about 0.4–0.6 μm/h; dry oxidation about 0.08–0.15 μm/h** (empirical values; must be calibrated against stepped samples from this furnace).

**Target thickness and its basis**: the first masking oxide is **0.4–0.6 μm**. Basis: boron diffused 1–2 h at 1100 °C is blocked only by an oxide ≥0.4 μm (empirical; field verification method: the masking witness wafer — place in the same furnace run a fully oxidized witness wafer with no windows; after diffusion measure its front-side sheet resistance; a clear rise means the masking leaked — thicken the oxide and retry).

**Two thickness measurement methods**:

1. **Color-chart lookup** (retained from Section 35.6): the oxide's interference color steps with thickness (gray → blue → yellow-green → orange-red; each level corresponds to a step of a few hundred nanometers). Make the color chart yourself from **stepped samples**: within one furnace run pull small pieces in sequence at 15/30/45/60/90 min; labeled and arranged, they become that furnace's color chart — the chart belongs to the furnace, not to the book;
2. **Weighing method** (balance sensitivity 0.1 mg): weight difference Δm before and after oxidation; thickness = Δm/(ρ·A), taking SiO₂ density as 2.2 g/cm³. Dimensional sanity check: a 30 mm wafer has area 7.1 cm²; a 0.5 μm oxide weighs 7.1 × 2.2 × 5 × 10⁻⁵ ≈ 0.78 mg — resolvable on the balance, corresponding to a thickness resolution of about 0.06 μm — **barely usable; guard against dust and moisture, and weigh quickly inside the balance case**; weighing three wafers together and averaging is steadier.

**Three functions of the oxide layer** (retained from Section 35.6): **diffusion masking** (dopant atoms cannot pass through intact oxide), **surface passivation** (protects the junction regions), **capacitor dielectric**. Insulation: between the two interconnect levels, separate by re-oxidation or a spin-coated organic insulating layer (a thin wax/resin layer; Chapter 8 materials).

**Failures and inspection**: white haze spots (dirty steam or a damp furnace tube — change the water, dry the tube); pinholes (dust particles shadowing the growth — look for bright-spot clusters with a dark-field magnifier; pinholed wafers are scrapped: diffusion leaks through the pinholes into the substrate); uneven thickness (wafers stacked too densely; unstable gas flow — stand wafers upright in a single layer with spacing ≥10 mm).

### 35.B.6 The Photosensitive Resist: Dichromate–Gelatin System and Same-Day Sensitivity Calibration

**Photosensitivity ladder** (retained from Section 35.5): start with a natural bitumen photosensitive layer (hardens in light, developed with turpentine — a formulation of the same family as history's first photograph; bitumen is registered in Chapter 26; for teaching and practice only); **the workhorse is dichromate + gelatin** — hardens on exposure, develops in clean water, with better resolution and edge quality.

**Preparation** (empirical ratios; calibration method in Card 35-02): put 8 g gelatin into 100 mL distilled water; first cold-soak 30 min to swell, then melt in a 40–50 °C water bath; after cooling below 35 °C (feels warm, not hot, to the touch) stir in 1.5–2.5 g ammonium dichromate (mass ratio roughly gelatin:salt = 4:1 to 5:1; more salt means faster exposure but a faster dark reaction and edge bleeding); filter once through fine cloth or absorbent cotton; **store in an amber bottle, protected from light, in a cool place; shelf life 3–7 days** (empirical; past expiry, re-verify with a small test-piece exposure — rely on tests, not the calendar).

**Why "same-day calibration" is mandatory** (one of the review-mandated blocks): dichromate gelatin has no stable "standard sensitivity" — the resist age keeps changing (the dark reaction slowly self-hardens), the salt ratio varies batch to batch, and lamp distance and weather keep changing. **"Standard exposure time" is not a constant; it is that day's value, measured with witness wafers for every batch of resist.** The two calibration methods:

1. **Time-gradient method (primary)**: coat and dry a witness wafer (a scrap Grade B wafer or a glass plate), cover with an opaque shutter, and during exposure advance it one step every 15 s, forming an exposure ladder of 15/30/45/…/180 s; after development, read with a magnifier: **the shortest fully hardened step is t_min; production exposure is 1.5 × t_min** (a safety factor; empirical — for the first month record the t_min distribution batch by batch; once stable it may be tightened to 1.3);
2. **Ink step-tablet method (auxiliary; monitors the light source)**: make a density step tablet by building up ink in 10 levels on a paper strip, lay it on the resist, expose a fixed time, and after development record the ink level corresponding to the surviving step — drift in the tablet reading is the alarm for drift in the light source or the resist's age.

**Dark reaction (silent failure)**: unexposed resist also hardens slowly in storage. Criterion: if film remains on the developed unexposed witness, the resist is scrapped. **The first thing to do at the start of every working day is to run an unexposed control.**

**Coating** (retained from Section 35.5 and quantified): drip 0.2–0.3 mL of resist onto the wafer center and spread with the concentric-circle glass rod, or place on the slow-rotation table (hand-cranked or slow mechanism, 60–120 r/min) to spread even; level and air-dry in the shade. Target dry film thickness **1–3 μm** (too thick blurs the edges in development; too thin gives pinholes). Calibration: coat a glass witness plate the same way and weigh — dimensional sanity check: 2 μm of dry gelatin (density about 1.3 g/cm³) on a 7 cm² plate ≈ 1.8 mg, resolvable on a 0.1 mg balance.

◎ Spreading feel: the glass rod rides on the surface without scraping the wafer; the resist spreads without stringing marks. Practice: spread 20 glass practice plates; check uniformity via stain depth after dyeing. Compensation for misjudgment: weigh 1 wafer per batch as a sample, and after development check with a magnifier for runs and edge pooling.

**Development and hard bake**: soak-rinse in 30–40 °C water for 1–3 min; the criterion is **the unexposed region fully dissolved and the water running clear with no gelatin threads**; rinse in cold water, air-dry in the shade; hard bake at 80–100 °C for 15–30 min (empirical; must be calibrated: an under-baked film lets the etchant seep under edges, an over-baked film cracks — check by test-etching a witness wafer). Quick check for a good hard bake: a light fingernail scratch leaves no white mark (◎; compensation: one test-etched witness wafer per batch).

[Card 35-02 Dichromate–Gelatin Photosensitive Resist: Preparation and Calibration] (eight fields)

1. **Input materials**: 8 g gelatin, 1.5–2.5 g ammonium dichromate, 100 mL distilled water, filter cloth; several glass witness plates and Grade B silicon witness wafers. Defective materials forbidden: moldy-smelling gelatin, deliquesced ammonium dichromate.
2. **Tools required**: water bath (±2 °C); thermometer (two-point checked); amber bottles; slow-rotation table or concentric-circle glass rod; carbon arc lamp; darkroom or red-light area; magnifier.
3. **Operating sequence and control points**: ① cold-soak the gelatin in cold water 30 min; ② melt at 40–50 °C until fully dissolved, no residue; ③ **cool below 35 °C before adding the salt** (adding it early accelerates the dark reaction); ④ filter into the amber bottle; ⑤ at the start of the day first run the **unexposed control** and the **time-gradient calibration**; ⑥ coat 0.2–0.3 mL per wafer; ⑦ air-dry in the shade; ⑧ expose 1.5 × t_min; ⑨ develop in warm water until the water runs clear; ⑩ hard-bake 15–30 min.
4. **Empirical parameters and calibration methods**: gelatin:salt = 4:1–5:1 (higher salt ratio = faster exposure but faster dark reaction — set the level with the twin indicators of t_min and the unexposed control); t_min measured same-day by the time-gradient method; shelf life 3–7 days, judged by test exposure; film thickness 1–3 μm calibrated by witness-wafer weighing.
5. **Process observation record items**: resist batch number, preparation date, that day's t_min, development water temperature and duration, hard-bake duration — entered in the run record for that batch of wafers.
6. **Accept / rework / scrap criteria**: accept = unexposed control fully dissolves + t_min readable + coating weight within the band; rework = film thickness out of band (strip the resist and recoat; the wafer is recoverable); scrap = film remains on the unexposed control (dark reaction gone too far; discard the whole bottle), or moldy-smelling resist.
7. **Common failures and troubleshooting order**: development not clean → first check for underexposure (review the t_min record) → check resist age (unexposed control) → check development water temperature; pattern-edge bleeding → first check for salt ratio too high → check insufficient hard bake; dense pinholes → check for coating dust (clean-enclosure settling dust over limit) → check film too thin.
8. **L1/L2/L3 evidence**: L1 = one successful time-gradient calibration record + intact pattern after development; L2 = same resist batch, calibration stable 3 days running (t_min drift <30%) + 10 wafers coated within spec; L3 = resist formula, shelf life and calibration procedure all in the ledger; a different person reproduces from the records.

### 35.B.7 Photomasks: From Enlarged Drawing to Working Mask

The photomask is the mother of patterns. **The three drawing-side standards come from Chapter 42, Section 42.7, and are executed directly in this chapter**: first, the **enlarged-drawing system** — the layout is drawn at 5:1 or 10:1 (Chapter 3 scribing + Chapter 20 scraped flat base plate); all dimensions annotated on the enlarged drawing = the final actual dimensions on the mask; the scale field reads "10:1, reduced to 1:1". Second, the **black/white region definition** — only pure ink black (light-blocking region) and pure blank (light-transmitting region) are allowed on the drawing; gray and smudging are invalid; fill black within the lines and verify by holding the drawing up to the light with no mottling. Third, the **alignment crosses** — one at each of the four corners of every mask and one at the center of the pattern area; cross-center distances use datum-based dimensioning (chained dimensioning is forbidden on mask drawings, Section 42.3.1).

**Mask-making flow**:

1. Draw the enlarged layout per Cards 42-01/46-02 of Chapter 42; add the M prefix to the drawing number (42.7); drawing and process card are numbered and frozen together;
2. **Microphotography** (Chapter 24 lenses + Chapter 26 wet-plate/film sensitizing) rephotographs the drawing to target size — **lens distortion is the source of mask error; it must be calibrated before use**: photograph a standard grid plate (made by Chapter 20 scribing), measure the grid pitches under a microscope, and obtain the actual magnification difference between center and edge; distortion >1% means shrink the field of view or change the lens (dimensional sanity check: 1% distortion over a 20 mm field = 0.2 mm, already eating forty percent of the 0.5 mm line-width margin);
3. **Honest declaration of the first-mask feature size**: **millimeter scale** (0.5–1 mm line width/spacing; empirical) — a single chip holds only a few devices; sub-millimeter line widths are listed as an upgrade route; this chapter makes no promise.

**Master-mask system** (transplanted from Section 42.5.1): the microphotographic result is the **master mask**, the single original; it stays in the archive and never leaves; only copies may be made from it inside the archive; **working masks** are contact-copied from the master (each numbered); a damaged one is replaced with a fresh copy. Layout changes follow the Section 42.6 four-step change process: **changing one parameter = opening a new mask version; verbal change instructions are forbidden**.

**Polarity checklist (new in this chapter; guards against the silent disaster of "the whole mask mirrored")**: dichromate gelatin is a **negative resist** — exposed areas harden and remain, protecting the oxide; so on the mask, **where light passes, the resist hardens and the oxide is kept; where the mask blocks light, the resist develops away and HF etches = a window**. Therefore the light-blocking regions on the mask = the future doped window regions. From enlarged drawing to working mask there is one microphotography step, possibly followed by one more copy step — **each rephotographing inverts the image once**. The polarity checklist is signed off mask by mask: ① the enlarged drawing has noted "black = window"; ② given whether this mask has passed through an odd or even number of inversions, deduce whether the mask's black regions should equal the designed window regions; ③ **mask verification wafer**: expose a scrap wafer through the mask by the full formal process; after etching the windows, check item by item against the design logic table (window count, orientation) — if it does not match, the whole mask is void and must be remade; "using it wrong-way-round on purpose" is forbidden (mirroring stands substrate and windows on their heads entirely).

### 35.B.8 Contact Exposure and Overlay Alignment

**The optics ledger of contact printing (review-mandated block 2: gap control)**:

- **The penumbra formula**: edge-blur width ≈ gap × angular diameter of the light source. Dimensional sanity check: the carbon arc's effective luminous diameter is about 5 mm; at a lamp distance of 400 mm the angular diameter is about 0.0125 rad; at a 0.3 mm gap the penumbra is about 2 μm, at a 3 mm gap about 38 μm — for 0.5 mm line widths, the penumbra itself is not fatal;
- **The gap's real harm lies in two places**: first, **dust and lint prop up local gaps** — there the pattern edges blur and dust-shadow defects remain; this is the leading explanation for "only one pattern bad on the same wafer"; second, **oblique and scattered light enters the gap**, partially fogging the resist so that it does not develop clean and the edges turn ragged;
- **Four engineering countermeasures**: ① **collimate the light source** — add a condenser (Chapter 24) or move a point source farther away, to shrink the angular diameter; ② **clamping mechanism** — three-point/four-point symmetric screw-pressure frame + compliant backing pad (felt or soft rubber sheet); tighten until "the backing pad is compressed about one third of its thickness" (a read-by-eye criterion; empirical — set the level with verification wafers, then fix it); ③ **dust removal before pressing** — rubber-blower puff + soft brush, done inside the clean enclosure; ④ **contact-state self-check** — observe the mask–resist interface under oblique white light: at near contact you see uniform interference fringes (Newton's-rings-like); no fringes, and the mask shifts visibly when nudged — that is a macroscopic gap; re-clamp.

**Verification-wafer system**: outside the pattern cells, every working mask **must carry a three-level line-pair test corner target (0.25/0.5/1 mm)**; on each exposure batch, read the first developed wafer's test target edges with a magnifier — a sharp edge defines "the effective resolution of this batch's contact state" and is entered in the run record; if the 0.5 mm level is soft, stop the batch and check clamping and dust removal.

**Alignment** (retained from Section 35.5): overlays of two or more masks align by **reference flat + mask alignment crosses** (Chapter 20 datum thinking); under the magnifier first rough-align (reference flat against the positioning strip), then fine-tune (crosses coincide); **overlay criterion: cross coincidence between the two masks ≤ half of the finest line width on the mask** (same as Section 42.7; no separate number) — millimeter-scale layouts matched to millimeter-scale precision; self-consistent.

[Card 35-03 Masked Contact Exposure] (eight fields)

1. **Input materials**: resist-coated, shade-dried wafers (wafer travel cards present); working mask (numbered, polarity checklist signed, test targets complete); verification wafer (a Grade B scrap wafer coated with the same resist batch).
2. **Tools required**: exposure fixture (four-point symmetric screw pressure + compliant backing pad; trial-pressed once with a verification wafer before use); carbon arc lamp with condenser and light shroud; magnifier; soft brush and rubber blower; timer.
3. **Operating sequence and control points**: ① same-day sensitivity calibration first (Card 35-02); ② blow the wafer free of dust; inspect visually, particle-free; ③ mask face down, aligned to the reference flat and the crosses; ④ **clamp symmetrically in stages to one-third backing compression**; ⑤ check the interface fringes under oblique light; no fringes, or visible relative shift, means release and re-clamp; ⑥ expose 1.5 × t_min (record lamp distance and clock time); ⑦ release and remove the wafer; never look at the arc with the bare eye (light shroud).
4. **Empirical parameters and calibration methods**: exposure = 1.5 × t_min (same-day time-gradient method); lamp distance 300–500 mm (fixed thereafter; any move means recalibration); clamping read by eye from the backing-pad compression (empirical — set the level with verification wafers).
5. **Process observation record items**: mask number, polarity-check conclusion, lamp distance, exposure seconds, contact-fringe state, test-target reading.
6. **Accept / rework / scrap criteria**: accept = pattern complete after development, test-target edges sharp at the 0.5 mm level, crosses aligned to ≤ half line width; rework = local pattern defects and the wafer recoverable (strip the resist and recoat; rework limited to 2 times per wafer — the third defect is scrapped, to prevent accumulated surface damage); scrap = wafer cracked by pressing, mask broken (switch to the spare mask; scrap the wafer with the cause recorded).
7. **Common failures and troubleshooting order**: one single pattern bad on a wafer → first check for dust propping the mask at that spot (inspect the mask against the light) → check for a local clamping gap; whole-wafer edge blur → check for uneven clamping (diagonal screw order) → check for resist beading at the wafer edge (re-check chamfer and coating); whole batch fogged and developing dirty → check the exposure dose (review t_min and lamp distance) → check resist age.
8. **L1/L2/L3 evidence**: L1 = verification-wafer test-target record + one successful exposure; L2 = same mask, 10 consecutive wafers with exposure pass rate ≥80% (empirical; requires statistics) + recorded overlay-cross deviations; L3 = the batch numbers of mask, wafer and resist can be cross-checked in the run record; a different person reproduces per the card.

### 35.B.9 Wet Etching: Window Opening and Anisotropic Rates

In Part B, etching has two objects, two chemistries, two physics: **etching silicon dioxide (window opening) is isotropic** — it etches sideways and downward at the same rate, so window walls are undercut; **etching silicon (hot alkali) is anisotropic** — rates differ by tens of times between crystal planes; this is the most directly measurable evidence that crystal orientation exists (Section 34.5), and it is where the first mask's real use lies. No rate value in this book is promised as a constant: **every bath is field-calibrated** (review-mandated block 3).

**Buffered hydrofluoric acid (BHF) etches silicon dioxide**:

- Mixing: mix HF (40% grade) with saturated ammonium fluoride solution at 1:3 to 1:7 by volume (the ammonium fluoride is self-made by neutralizing HF with ammonia, Chapter 26; saturation is proven by residual crystals at the bottle bottom). Why buffered: pure HF etches far too fast (it would eat through the full first-mask thickness within a minute) and its concentration swings violently as the reaction proceeds, so rates are not repeatable; the buffer presses the rate into the 0.05–0.15 μm/min range (empirical; must be calibrated), and **the reaction products are soluble and no crust forms on the surface**;
- **Rate calibration method (mandatory for every bath)**: etch a stepped oxide sample (the color-chart ladder of 35.B.5, thicknesses known) for timed intervals and record the time needed to etch through each step — the through-criterion is the **water-drop test**: SiO₂ is hydrophilic and holds a uniform water film; where the etch has broken through and silicon is exposed, the drop beads up (direct reuse of the Section 34.7 water-film test; stopwatch timing);
- **The ledger of isotropic undercutting**: lateral undercut = vertical etch depth, so the window bottom ends up effectively about 2 × oxide thickness (0.8–1.2 μm) wider than the mask pattern — negligible for millimeter line widths, but the concept must go on file: it is the first wall on any future fine-line route [Background/outlook: in a sub-millimeter line-width era, undercutting and film thickness become the same order of magnitude, and dry etching (no liquid; etches directionally) becomes inevitable — listed on the upgrade route, not implemented];
- **The safety margin of over-etching**: HF barely attacks bare silicon — the window-opening step is naturally tolerant of over-etch, which is why it is chosen for opening windows; but over-etching keeps gnawing at the resist film's edges (edge seepage); cap it at 1.3–1.5× the breakthrough time (empirical; set with a test-etched witness wafer).

**Anisotropic etching of silicon in hot alkali**:

- Mixing: 30–40% (mass) sodium hydroxide solution, 75–85 °C constant-temperature water bath (Chapter 25 thermometer standing watch), lidded to prevent concentration (weigh the liquid each shift; top up with distilled water to the starting value);
- Rate and anisotropy ratio (empirical ranges; field calibration mandatory): the (100) plane about 0.3–0.8 μm/min; the {111} planes 20–50× slower — the anisotropy ratio is a function of temperature and concentration: lower temperature and higher concentration strengthen the anisotropy but roughen the surface;
- **Calibration method**: open a large 5×5 mm window in the oxide of a (100) wafer and etch 30–60 min; back-calculate the pit depth by **weighing** (Δm/(ρ·A), silicon density 2.33 g/cm³ — dimensional sanity check: a 5×5 mm window etched 30 μm deep = 0.75 mm³ ≈ 1.75 mg, resolvable on a 0.1 mg balance); examine the pit walls by **angle-lap and staining** (35.B.10): with normal anisotropy the pit walls are flat and the ridge lines dead straight (self-stopped on the {111} planes); rough, ragged pit walls mean weak anisotropy or lost temperature control;
- **The three real uses in the first mask** (no exaggeration): ① **dicing guide grooves** — pre-etch shallow grooves along the dicing streets; cleaved dicing runs straighter with less edge chipping; ② **preparatory process for mesas/isolation** (second-generation devices and later); ③ **crystal-orientation teaching** — the rate difference inside one bath is physical evidence of crystal orientation; register it in the materials register;
- Failures and control: a ±5 °C temperature swing drifts the rate by ten to twenty percent (thermostat the water bath); concentrated alkali roughens the surface and scrambles the rates (the weigh-and-top-up discipline); agitation affects mass transfer — **calibration and production must use the same agitation pattern** (manual agitation 1–2 cycles/s; written into the card).

**Universal etching discipline**: HF bath and alkali bath stored physically apart, dedicated labels, dedicated fixtures (cross-contamination scraps the whole bath); one fixture per wafer; timing starts at immersion; after etching, go straight into a large-volume rinse bath to quench the reaction.

[Card 35-04 Wet Etching] (eight fields)

1. **Input materials**: developed and hard-baked wafers (pattern complete and on file); BHF (1:3–1:7, freshly mixed or calibrated that day); 30–40% NaOH solution; stepped oxide samples; rinse bath (≥5 L distilled water).
2. **Tools required**: constant-temperature water bath (±2 °C); thermometer (two-point checked); dedicated fixtures and timer; magnifier; balance; stopwatch.
3. **Operating sequence and control points**: ① bath at temperature and stable for 10 min; ② **first etch a stepped sample to re-verify the day's rate**; ③ immerse the wafer and agitate in the fixed pattern (1–2 cycles/s); ④ **for BHF window opening, judge breakthrough by the beading water drop; after breakthrough continue for ≤0.3–0.5× the calibrated breakthrough time, then leave the bath**; ⑤ rinse immediately with a large flow to stop the reaction; ⑥ after rinsing, remove resist residue with a gentle brush; ⑦ inspect window edges and film edges under the microscope; ⑧ alkali silicon etch in the other bath under the same rules; verify pit depth by weighing.
4. **Empirical parameters and calibration methods**: BHF rate 0.05–0.15 μm/min (same-day, on a stepped sample); NaOH (100) rate 0.3–0.8 μm/min, {111} 20–50× slower (large-window weighing + angle-lap staining); temperature 75–85 °C (±2 °C water bath); agitation 1–2 cycles/s (calibration and production use the same pattern).
5. **Process observation record items**: bath temperature, bath age (times used), calibrated breakthrough time, actual etch time, weighed pit depth, edge-quality rating — entered in the etching column of the run record.
6. **Accept / rework / scrap criteria**: accept = all windows fully through (multi-point water-drop test) + edges clean, no undercut seepage + (alkali etch) pit ridge lines dead straight; rework = windows not fully through (strip the resist, re-oxidize thinner and redo the whole wafer — witness wafers only; device wafers are not reworked but scrapped — the contamination risk of interlayer rework outweighs the benefit); scrap = resist film floating off over a large area (hard-bake failure), seepage beyond one tenth of the line width, collapsed alkali-etch pit walls.
7. **Common failures and troubleshooting order**: ragged window edges → first check the hard bake (test-etched witness wafer) → check whether the BHF is too concentrated (go from 1:3 to 1:6) → check for over-vigorous agitation; windows not etching through → check the oxide thickness (back to the color chart) → check for bath temperature too low → check BHF aging (re-verify with a stepped sample); rough alkali-etched surface → check temperature → check concentration (the weigh-and-top-up discipline) → check for aluminum/iron contamination (vessel discipline).
8. **L1/L2/L3 evidence**: L1 = stepped-sample rate calibration record + one successful window opening (micrograph on file); L2 = same bath, 10 consecutive wafers with breakthrough-time range <20% (empirical; requires statistics) + photographs/tracings of anisotropic pit shapes; L3 = rate ledger kept per bath, bath-age vs. rate curve retrievable; a different person reproduces it.

### 35.B.10 Diffusion, Junctions, and Device Formation

**The diffusion process** (retained from Section 35.7, upgraded to a two-step method): the windowed wafer shares the furnace with the dopant source — **predeposition** (source present; constant surface concentration) + **drive-in** (source withdrawn; fixed total dose; surface concentration flattens and the junction drives deeper). Temperature × time are the only two knobs (direct application of the Chapter 25 thermal regime):

- Source and source temperature: boric acid (p-type; first baked to B₂O₃ and loaded into a boat) goes in the upstream temperature zone; ammonium dihydrogen phosphate (n-type) the same way. **There is no book constant for source temperature; set it by a search procedure**: hold wafer temperature at 1050–1100 °C, start the source temperature at the low setting and add +50 °C per furnace run, measuring sheet resistance on a witness wafer each run until it enters the band — **the boron predeposition target band is 20–60 Ω/□** (empirical; must be field-calibrated);
- Drive-in: withdraw the source boat (or push it to the cold end); hold the main furnace at 1100–1150 °C for 1–4 h; **junction depth targets: base 1–2 μm, emitter 0.8–1.5 μm** (empirical; measured by angle-lap staining; no furnace-time formula is promised).

**Junction depth measurement (angle-lap + staining; retained from Section 35.7, detailed)**: wax-mount a small chip onto a 5–10° bevel block and lap a bevel; paint the surface with staining solution (5% copper sulfate solution plus a little HF) — p regions copper-plate and darken, n regions stay bright, and the boundary line is the junction; read the junction width along the bevel with the microscope eyepiece reticle, and multiply by the cotangent of the bevel angle to get the junction depth. Dimensional sanity check: a 2 μm junction shows as about 19 μm on a 6° bevel — readable with the reticle (Chapter 24).

**Sheet-resistance monitoring (the witness-wafer system; retained from Section 35.7)**: each furnace run gets witness wafers (Grade B wafers, same furnace, same pattern or fully open) measured with the four-point probe (Chapter 34) — **run-to-run drift beyond ten percent halts the furnace for investigation** (the Chapter 22 spot-check thinking). The direction of the drift is itself diagnostic: sheet resistance uniformly low = source temperature too high or flow too large; uniformly high = source exhausted (change the boat) or furnace temperature too low.

**Parasitic doping of the back and edges (a silent failure new in this chapter)**: during diffusion the wafer back and edges are exposed to the dopant vapor just the same — a junction on the back means leakage and thoroughly scrambled breakdown characteristics. Countermeasures: before diffusion, **keep oxide on the back and edges** (first mask: double-sided oxidation, windows opened on the front only), or after diffusion lap 20–30 μm off the back (the lapping recovery flow). Criterion: a diode whose reverse characteristic is abnormally soft with heavy leakage — lap the back first and re-measure; improvement confirms the diagnosis.

**Device choice** (retained from Section 35.7): **the first device = a diode–transistor logic gate (DTL) made of a single npn structure + a resistor** — simplest structure and process, validating the full chain of "multilayer patterns + doping + interconnect". The point-contact parallel route (germanium) advances per the Plan B of 35.B.3; neither blocks the other.

[Background/outlook: ion implantation uses an electric field to set doping depth and dose directly, retiring trial-and-error methods like the "source-temperature search" — it needs high-voltage equipment and beam-current measurement; listed as a long-term condition; this chapter makes no promise.]

### 35.B.11 Metal Interconnect and Electrodes

**First choice: fired silver paste** (retained from Section 35.8 and quantified) — **it sidesteps aluminum's electrolytic scale-up problem** (the Hall process requires enormous electric power and cryolite; a registered unlock item of Chapter 32):

- Paste mix (mass ratios; empirical; must be calibrated): fine silver powder 75–80% + low-melting glass frit 3–6% + vehicle (rosin in turpentine) 15–20%. Mix until it hangs on the squeegee as a continuous band without dripping; slumped printed lines = too much vehicle; open lines = too little;
- Screen printing: a 40–60 mesh silk screen on a frame, positioned to the mask with the reference-flat positioning strip (Chapter 26 printing thinking); the squeegee prints lines in one pass — the mesh opening must be ≥ about one fifth of the line width, or the paste clogs (rule of thumb); print **four test lines** on a witness wafer with every batch;
- Firing: first binder burnout, bake 150–250 °C for 10–20 min (if the organics are not expelled fully, the fired lines blister and open); then peak in the furnace at **750–850 °C held 10–20 min** (over a hundred degrees below silver's melting point of 962 °C, to keep the silver from balling; criteria: line surface continuous silvery-white, no balling, no brown carbonized spots);
- Inspection: continuity (Chapter 31); line resistance measured on the test lines by four-point probe/two-probe method as **sheet resistance**, target of order ≤0.1 Ω/□ (empirical; must be calibrated for this paste — fired silver's conductivity is roughly thirty to fifty percent of bulk silver's; register it honestly); adhesion criterion: a base score remains after knife-scraping (the glassy phase has bitten into the oxide) and there is no wholesale peeling;
- Electrode lead-out and bonding: fine gold/silver wire joined to the bond pads by thermocompression (a heated tool tip pressed weld; 250–350 °C, 300–800 g hung on the tool handle, 1–3 s; empirical; must be calibrated) or by soldering (rosin flux, soldering iron at 250–300 °C);
- Vias (interlayer connection; retained from Section 35.8): where the upper-level pattern must connect through, print a large silver pad that pierces the insulating layer for pressure contact — the crude millimeter-scale way; reliability first.

◎ Thermocompression feel: as the tool tip presses down, you feel the wire "settle without slipping". Practice: press-weld 30 bonds on scrap wafers. Compensation for misjudgment: the pull test — after bonding hang a 50–100 g weight on the wire and pull; **the wire breaks while the joint holds = pass**; sample ≥3 bonds per batch.

[Card 35-05 Metal Interconnect] (eight fields)

1. **Input materials**: wafers with contact holes open; silver paste (formula on file; mixed the day it is used); 40–60 mesh silk screen on frame; fine gold/silver wire ≥0.1 mm; rosin, solder.
2. **Tools required**: screen-printing station (blank print checked for uniformity before use); squeegee; firing furnace (peak control ±15 °C); heated bonding tool and weights; moving-coil meter; four-point-probe or two-probe line-measurement station.
3. **Operating sequence and control points**: ① mix the silver paste same-day and print four test lines on a witness wafer; ② align the screen to the mask (reference flat + crosses); ③ print lines in one squeegee pass — **no touch-up pass**; ④ binder burnout 150–250 °C for 10–20 min; ⑤ firing peak 750–850 °C for 10–20 min; ⑥ measure test-line sheet resistance and file it; ⑦ knife-scrape adhesion spot check; ⑧ bond the lead wires; spot-check bonds with pull tests.
4. **Empirical parameters and calibration methods**: paste mix 75–80/3–6/15–20 (fine-tune with the twin indicators of test-line open rate and sheet resistance); firing peak 750–850 °C (balling on the line surface sets the upper limit; adhesion sets the lower); thermocompression 250–350 °C × 1–3 s + 300–800 g weight (level set by pull-test pass rate).
5. **Process observation record items**: paste batch number, firing furnace number and profile, test-line sheet resistance, open-line count, pull-test spot-check results — entered in the interconnect column of the run record.
6. **Accept / rework / scrap criteria**: accept = network continuity matches the layout + test-line sheet resistance in band + adhesion and pull spot checks passed; rework = local open lines (repair with solder-bridge dots, register each repair point; ≤3 repair points, beyond that scrap); scrap = large-area balling or blistering (re-oxidation and re-opening windows is no longer worth it), adhesion peeling across the whole wafer.
7. **Common failures and troubleshooting order**: open lines → first check for thin paste (review the test lines) → check for clogged mesh (wash the screen) → check squeegee speed; balling → check firing over-temperature → check insufficient binder burnout; poor adhesion → check frit content too low → check firing peak too low; bond lifting → check bond-pad oxidation (refire the silver) → check tool temperature.
8. **L1/L2/L3 evidence**: L1 = one acceptable printed line + test-line data; L2 = whole-wafer interconnect network continuity passing + pull-test spot-check records; L3 = paste formula and firing profile in the ledger, open-line rate tabulated per batch and retrievable; a different person reproduces it.

### 35.B.12 On-Wafer Testing of Individual Devices

(Retained from Section 35.9) **Wafer-level on-chip testing**: a self-built probe station — microscope (Chapter 24) + micropositioner stage (Chapter 27) + two or three spring probes (fine wire ground to points, Chapter 31): diode characteristics (conducts forward, blocks reverse), transistor β (a small change in base current producing a large change in collector current; moving-coil meter reading ratio); curve recording: I–V curves hand-plotted point by point (Chapter 25 recording regime) — **device parameter cards linked to wafer number and furnace number** (a transplant of the Chapter 22 traceability system: a bad chip traces back to the bad furnace run, and via the wafer travel card back to the bad ingot — the responsibility chain of the two parts closes here).

### 35.B.13 Verifying the Simplest Integrated Logic Function

(Retained from Section 35.10) Logic criterion table (standalone tests, nothing else connected):

| Item | Test | Pass standard |
|---|---|---|
| Single-transistor switch | Base powered/de-powered controls a lamp | Lamp on/off repeatable |
| Inverter (NOT gate) | Input high → output low | Output inverts for both input states; stable over 10 repeats |
| Two-input AND/OR (DTL) | Four input combinations | Truth table entirely correct |
| Two-gate cascade | First gate's output drives the second | Logic still correct after cascading |

Environmental tests: warming in the palm (parameters drift within tolerance), light tapping (poor contact = dry joint) — **the three reliability moves: temperature, vibration, time**.

### 35.B.14 Why the First Chip Must Be Extremely Crude

(Retained from Section 35.11) The yields of the process steps multiply: oxidation 95% × lithography 90% × diffusion 90% × metallization 95% … after ten steps half is gone (empirical; requires field statistics) — **the simpler the design, the fewer the steps, the higher the yield**. Three disciplines of crude design: line widths at three or more times the process limit, to leave margin; all patterns of right angles and straight lines (masks easy to draw, etching easy to do); redundant design (build three identical circuits side by side on the same chip; at test, enable whichever is best). **First-mask integration target (registered): 2–6 devices and 1 logic gate per chip** — this is already the realistic ceiling of this route; density gains come from the long iteration of yield gains (Chapter 36).

### 35.B.15 From Laboratory Samples to Repeatable Manufacture

(Retained from Section 35.12 and joined to the Chapter 42 version system) **Statistical process control, the beginning**: record for every wafer (cleaning bath run / oxidation furnace number / resist batch / exposure time / weather and humidity) — classify the yield data of the first 50 wafers by defect type (the electrical version of the Chapter 4 failure classification); yield ramp-up priority: first wipe out "total-wipeout" defects (parameters outside the process window), then attack "random defects" (dust, particles); the realistic version of clean operation — **the six rules of the simple cleanroom: enclosed cell + wet cleaning + oilcloth floor + personnel dress code + vessels covered at all times + daily settling-dust slide counts** (dust is the chief of random defects; the payoff is immediate; verify with yield data); version control: process cards and photomasks numbered and frozen together — **mask drawing numbers take the M prefix and merge into the Chapter 42 drawing-library version system (the Section 42.6 four-step change process); changing one parameter = opening a new version; verbal change instructions are forbidden**.

### 35.B.16 Bottlenecks That Cannot Be Crossed: Cleanliness, Material Purity, Equipment, and Metrology

(Retained from Section 35.13) The honest list (what is still missing to "rebuild a modern chip industry"):

1. Cleanliness: modern-grade cleanrooms (filtered laminar flow, particle-count monitoring) — today there is only "simple clean measures + yield statistics";
2. Material purity: continuous, stable supply of electronic-grade chemicals and gases (the Chapter 34 L3 gap);
3. Equipment: step-and-repeat photolithography (sub-micron), ion implantation (doping precision), epitaxial growth — all products of multiple generations of industrial iteration;
4. Metrology: sub-micron line-width measurement, trace impurity analysis (ppb level), inline defect inspection — **what cannot be measured cannot be built** (the ultimate embodiment of Iron Law 4 of the General Outline);
5. Economies of scale: the design–process–test–packaging division-of-labor system (the collaboration of tens of thousands; an echo of the Chapter 1 population-and-division-of-labor question).

**Conclusion**: this route can reach "handcraft-process-grade integrated circuits" (millimeter features, a handful of gates integrated, reproducible small batches); it is a genuine integrated circuit — real materials, real devices, real logic, real verification — but it is not the modern chip industry. Admitting this boundary is the final brick in this manual's credibility.

---

## Parameter Master Table

**Part A 35.A (bulk-material parameters)**:

| Parameter | Value | Calibration method | Location |
|---|---|---|---|
| Silicon melting point | 1414 °C | Physical constant; temperature control referenced to it | 35.A.4 |
| Substrate resistivity target band | 1–10 Ω·cm (n-type) | Four-point probe on head-and-tail samples of every ingot | 35.A.3 |
| Master alloy phosphorus content | 0.05–0.1% (mass) | Charge calculation + per-ingot resistivity iteration | 35.A.3 |
| Pull rate (body section) | 0.3–1 mm/min | Read from the diameter–time curve | 35.A.4 |
| Necking | 2–4× pull rate; neck diameter 3–5 mm; length 10–20 mm | Surface smooth, free of lumps | 35.A.4 |
| Rotation | 5–20 r/min | Uniform swirl marks on the melt surface | 35.A.4 |
| Pulling chamber vacuum | 1–10 Pa | McLeod gauge (Chapter 33) | 35.A.4 |
| Cutting speed | 3–8 mm/h | Measured on this machine's first ingot | 35.A.6 |
| Wire diameter / kerf | 0.3–0.5 mm / 0.5–0.8 mm | Inferred from measured kerf | 35.A.6 |
| Wafer thickness / five-point range | 0.4–0.6 mm / <0.1 mm | Micrometer, five points | 35.A.6 |
| Abrasive-removal rule | Each stage ≥3× the previous stage's grit size | Back-checked from polishing time | 35.A.6 |
| Polishing duration | 1–3 h per face | Dark-field criterion | 35.A.6 |
| Resistivity uniformity | Five-point range <20% | Four-point probe | 35.A.7 |

**Part B 35.B (surface-process parameters)**:

| Parameter | Value | Calibration method | Location |
|---|---|---|---|
| Wet oxidation rate (1100 °C) | about 0.4–0.6 μm/h | This furnace's stepped samples | 35.B.5 |
| Dry oxidation rate | about 0.08–0.15 μm/h | Same | 35.B.5 |
| Masking oxide target thickness | 0.4–0.6 μm | Color chart + weighing | 35.B.5 |
| Resist mix | 8 g gelatin per 100 mL water + 1.5–2.5 g ammonium dichromate | Twin indicators: t_min and unexposed control | 35.B.6 |
| Resist shelf life | 3–7 days | Daily unexposed control | 35.B.6 |
| Dry film thickness | 1–3 μm | Witness-wafer weighing | 35.B.6 |
| Exposure time | 1.5 × t_min | Same-day time-gradient method | 35.B.6/8 |
| Development / hard bake | 30–40 °C, 1–3 min / 80–100 °C, 15–30 min | Water runs clear in development / fingernail scratch + test etch | 35.B.6 |
| Overlay accuracy | ≤ half line width | Cross-mark deviation reading | 35.B.8 |
| BHF mix / rate | HF:ammonium fluoride solution 1:3–1:7; 0.05–0.15 μm/min | Stepped sample + water-drop beading | 35.B.9 |
| NaOH silicon etch | 30–40%, 75–85 °C; (100) 0.3–0.8 μm/min; {111} 20–50× slower | Large-window weighing + angle-lap staining | 35.B.9 |
| Predeposition | 1050–1100 °C, 15–60 min; boron target 20–60 Ω/□ | Source-temperature search procedure + witness wafer | 35.B.10 |
| Drive-in | 1100–1150 °C, 1–4 h | Junction depth measured by angle-lap staining | 35.B.10 |
| Junction depth targets | Base 1–2 μm, emitter 0.8–1.5 μm | Angle-lap staining | 35.B.10 |
| Drift halt line | Witness-wafer sheet-resistance drift >10% | Witness-wafer ledger | 35.B.10 |
| Silver paste mix (mass) | silver 75–80 / frit 3–6 / vehicle 15–20 | Test-line open rate + sheet resistance | 35.B.11 |
| Firing | binder burnout 150–250 °C, 10–20 min; peak 750–850 °C, 10–20 min | Line-surface balling / adhesion criteria | 35.B.11 |
| Thermocompression bonding | 250–350 °C, 300–800 g weight, 1–3 s | Pull-test pass rate | 35.B.11 |
| First-mask line width | 0.5–1 mm | Mask declaration + test targets | 35.B.7 |

## Failure Modes and Diagnosis

**Part A (bulk-material failures — ordered from most common to hardest to detect)**:

| Symptom | Candidate causes | Verification | Disposition | Prevention |
|---|---|---|---|---|
| Ingot pulls polycrystalline | Thermal shock, vibration, bad seed | Broken ridge line + acid-etched cross-section of the head sample | Downgrade the whole ingot to test pieces | Never skip necking; keep the ring-watch records |
| Sliced wafers bowed / tapered | Insufficient wire tension; thin slurry; guide worn off-axis | Knife-edge straightedge light-gap test + five-point micrometer | Lap to correct | Tension set with quantified weights |
| Wafer warpage | One-sided over-lapping | Look for the under-gap on a flat plate + five points | Lap the other face symmetrically | Alternate faces in stages |
| Polishing scratches will not come out | Fine-lapping damage not removed; abrasive grades mixed | Dark-field scattering | Back to polishing / back to fine lapping | Abrasives graded; dedicated tray per grade |
| Resistivity off-band | Master alloy charge miscalculated; segregation fluctuation | Four-point probe on head-and-tail samples | Use downgraded by segments | Iterate the master-alloy account ingot by ingot |
| Iron contamination (hardest to detect) | Contact with steel vessels/tools | Abnormal resistivity temperature coefficient (34.7) + abnormal junction characteristics | Re-melt and re-purify | Quartz/ceramic discipline (34.2) |

**Part B (pattern-process failures — ordered from most common to hardest to detect)**:

| Symptom | Candidate causes | Verification | Disposition | Prevention |
|---|---|---|---|---|
| Missing corners and open lines after development | Dust; underexposure; aged resist | Magnifier + review of t_min and the unexposed control | Strip the resist and recoat (limit 2 times) | The six clean rules + same-day calibration |
| Ragged window edges / edge seepage | Insufficient hard bake; BHF too concentrated; over-vigorous agitation | Test-etched witness wafer + microscope | Device wafers scrapped | Time the hard bake; fix the buffer ratio |
| A single pattern bad on one wafer | Dust propping the mask; local clamping gap | Inspect the mask against the light; check the backing pad | Downgrade that wafer to witness duty | Pre-press blow-off + fringe self-check |
| Masking failure (doping outside the windows too) | Oxide too thin or pinholed | Masking witness-wafer sheet-resistance comparison | Scrap the wafer | Oxide step ladder + dark-field pinhole check |
| Overlay offset beyond limit | Loose positioning strip; careless alignment | Cross-mark deviation reading | Downgrade to a looser-tolerance layer | Alignment procedure made into a card |
| Silver-paste open lines / balling | Thin paste; insufficient burnout; firing over-temperature | Test lines + microscope | Solder-bridge repair, ≤3 points | The test-line system |
| β / sheet-resistance drift (hard to detect) | Source/furnace temperature drift; source exhausted | Witness-wafer ledger trends | Halt the furnace and investigate (halt beyond ten percent) | Witness-wafer system + periodic thermocouple checks |
| Back-side parasitic junction (hard to detect) | Back exposed during diffusion | Soft diode reverse characteristic — lap the back and retest | Lap off 20–30 μm of the back | Double-sided oxidation, windows on the front only |
| Whole mask mirrored (hardest to detect; largest loss) | Miscounted odd/even copy inversions | Mask verification wafer checked against the design logic table | Scrap the batch; remake the mask | Polarity checklist, dual signature (35.B.7) |

## Process Card Index

| Card number | Name | Use | Card location (eight fields) | Copy to workstation |
|---|---|---|---|---|
| 35-01 | Slicing and Polishing | Multi-wire slicing, chamfering, two-stage lapping, mirror polishing, the five inspections | End of 35.A.6 (Part A) | Slicing room / Lapping room |
| 35-02 | Dichromate–Gelatin Resist Preparation and Calibration | Mixing resist, same-day sensitivity calibration, coating, development and hard bake | End of 35.B.6 | Darkroom / Coating station |
| 35-03 | Masked Contact Exposure | Clamping, gap self-check, exposure timing, overlay alignment | End of 35.B.8 | Exposure bench |
| 35-04 | Wet Etching | BHF window-etch rate calibration, anisotropic silicon etching | End of 35.B.9 | Etching room (two baths kept apart) |
| 35-05 | Metal Interconnect | Silver-paste mixing and screen printing, firing, bonding and pull-test sampling | End of 35.B.11 | Printing / Firing / Bonding stations |

All five cards carry the full eight fields and copy out on a single sheet: the Part A card files with Part A, the four Part B cards with Part B; the card number is the workstation copy number, and revisions go through the Chapter 42 four-step change procedure.

## Acceptance Criteria L1/L2/L3

- **L1 (phenomenon observed)**: Part A — one single-crystal ingot (uniform-diameter section ≥30 mm, head sample on file), 1 wafer passing slicing and polishing (dark field + water film + five-point thickness); Part B — microphotographic mask made (grid distortion calibration on file, polarity checklist signed); one successful time-gradient sensitivity calibration; photolithography–etching pattern transferred into the oxide (lines complete under the magnifier); a single junction (diode) measured on-wafer.
- **L2 (acceptable product repeatable)**: Part A — ≥10 good wafers from one ingot, five-point four-point-probe range <20%, the wafer-travel-card system running; Part B — a single planar transistor with on-wafer β on target and repeatable (three or more wafers in the batch); one testable logic gate via hybrid integration (Kilby-style); BHF and anisotropy rate ledgers established; yield statistics begun (complete-flow data for a first batch of ≥20 wafers).
- **L3 (system level: materials, spares, records, succession)**: planar-process DTL gates in small batches (yield steady at double-digit percentages; empirical; requires long-term statistics); the probe–packaging–test loop running; the process-card and photomask version-freeze regime enforced (merged into the Chapter 42 drawing library); Part A wafer supply line with wafer output rate ≥60% for three consecutive ingots — **"repeatable manufacture" achieved; "sustainable production" handed to Chapter 36**.

## Labor, Staffing, and Consumption

| Item | Staff | Labor hours (empirical; must be field-calibrated) |
|---|---|---|
| Pulling one ingot (30–50 mm × 60–100 mm, including melt-charge watch) | 2, rotating | 1–2 days/ingot |
| Slicing one ingot (3–4 wires wound in parallel) | 1 tending | 5–8 days/ingot (yields 40–60 wafers) |
| Lapping + polishing one wafer | 1 | 0.3–0.5 person-days |
| Full flow for one batch of 10 wafers, Part A | 2 | 2–3 weeks |
| One oxidation run (including heating-ladder samples) | 1 | 0.5 day |
| Resist mixing + same-day calibration | 1 | 0.5 day (daily) |
| Lithography for a batch of 10 (coat–expose–develop–etch) | 2 | 1 day |
| One diffusion run (predeposition + drive-in + angle-lap staining) | 2 | 1–1.5 days |
| Interconnect + on-wafer test for a batch | 2 | 1–2 days |
| One Part B wafer run (10 wafers, four-mask overlay) | 2–3 dedicated | 5–8 days |
| First integrated circuit development (including failed rework) | 2–3 | 3–6 months |
| Consumption | Per wafer run: 5–10 wafers, 50–100 mL HF, 1–2 g ammonium dichromate, 5–10 g silver powder, several carbon arc rods | Entered in the materials ledger |

## Safety Boundaries

- **The HF red line holds for the whole chapter** (Chapter 26): gloves and goggles, calcium preparation on hand, HF bath with dedicated labels; the ammonium fluoride solution under the same rules;
- **Hexavalent chromium red line (new in this chapter)**: dichromate dust and solutions — skin ulcers, sensitization by inhalation; weigh in a shallow tray by the wet method, wearing gloves and apron; **collect the waste liquid separately, reduce it with ferrous sulfate solution (orange-red turning green is the proof), then precipitate with lime; direct discharge is strictly forbidden** (Chapter 26 poison protocols);
- Hot alkali silicon etching: 80 °C alkali dissolves soapy fats and scalds — face shield, long-handled fixtures, splash lip on the bath rim;
- Diffusion source vapor inhalation risk — furnace-area ventilation + masks (35.B.10); dopants and acids stored in separate cabinets per Chapter 26;
- Arc-light exposure injures the eyes — light shroud and filter; looking directly at the carbon arc is forbidden (35.B.8);
- Pulling-zone high temperature and quartz crucible shatter risk: goggles, isolation shield (same rules as Chapter 34);
- Dicing swarf and silver-powder dust: goggles + wet paste mixing, wet cleaning;
- All electrical testing follows the Chapter 32 protocol (de-energize before rewiring).

## A. Existing Tool List (partial)

Wafer materials chain (Chapter 34 purification, zone refining, four-point probe); the low-vacuum ladder and McLeod gauge (Chapter 33); glass lampworking and quartzware (Chapters 14, 26); diffusion furnaces and temperature control (Chapters 12, 25); HF and photosensitive chemistry (Chapter 26); lenses and microscopy (Chapter 24); planar datums and knife-edge straightedges (Chapter 20); measuring instruments and the traceability system (Chapter 22); the electrical measurement system (Chapters 30–33); ceramic packaging (Chapters 11–12); printing and silk screen (Chapters 26, 15); silver (Chapters 16–17); drawing and the version system (Chapter 42).

## B. New Tools Introduced in This Chapter

Part A: the necking pull program and ring-watch recording method; the master-alloy doping iteration method; the roll-lapping–cleavage-orientation–reference-flat system; multi-wire slicing with quantified tension (Card 35-01); the chamfering protocol; the two-stage-lapping 3× rule; the five-item inspection of dark field–water film–five points; A/B/C grading and wafers traveling with their cards. Part B: the wet-oxidation system and the stepped-sample color chart, oxide thickness by weighing; **the dichromate–gelatin resist and same-day sensitivity calibration (time-gradient + ink step-tablet methods, Card 35-02)**; mask enlarged drawings–microphotography and grid-distortion calibration, the master–working-mask system, the **polarity checklist**; **the contact-exposure clamping fixture and gap control (fringe self-check + test-target verification wafers, Card 35-03)**; **BHF window etching and anisotropic silicon etching with rate ledgers (Card 35-04)**; two-step diffusion and the source-temperature search, masking witness wafers, angle-lap staining junction measurement, back-side parasitic precautions; silver-paste screen printing–firing interconnect with pull-test sampling (Card 35-05); the self-built probe station; the four-piece logic truth-table verification set; the three disciplines of crude design and redundant design; the six rules of the simple cleanroom and settling-dust counts; the yield statistics and defect classification system; the honest list of "uncrossable bottlenecks".

## C. Unresolved Dependencies

- Sub-millimeter photolithography (photosensitive material and optics upgrades; dry etching);
- Ion implantation and epitaxy (a generational equipment gap);
- ppb-level metrology (a generational gap in analytical chemistry);
- Precise crystal orientation (X-ray);
- Aluminum electrolysis (the unlock item for aluminum interconnect; registered in Chapter 32);
- Modern-grade cleanrooms (filtered laminar flow and particle counting);
- Packaging at scale and automated testing (begins in Chapter 36).

## Next-Step Dependencies

- Chapter 36: from repeatable to sustainable — the test system, failure analysis, the ramp route for complex logic, and an honest statement of capability boundaries;
- Chapter 42 loop-back: the three mask-drawing standards and the drawing-library version system (M-series drawing numbers) are consumed and frozen by this chapter; this chapter's process cards merge into its four-step change process;
- Whole-book loop-back: this chapter is the grand confluence of the six lineages — measurement (Chapters 3→22→27→34), materials (Chapters 8→23→26→34), precision (Chapter 20 planar datums → mask base plates → reference flats), energy (Chapters 6→28→32 electricity and arc light), and knowledge carriers (Chapters 45→46 paper, ink, and drawings) all arrive here. **The first integrated circuit validates not the chip, but the entire dependency graph.**
