# Chapter 35 · Part A: Silicon and Wafer Material Preparation (35.A)

> This part and Part B share chapter number 35 (the files are split, the chapter number is not; the book-wide cross-reference "Chapter 35" remains valid). Part A = bulk material (purification / crystal pulling / slicing); Part B = planar processing (oxidation / photolithography / diffusion / interconnection). The two parts have different failure modes: Part A failures are silent (material problems cannot be seen on the spot), Part B failures are random (pattern problems fluctuate run by run).

# Chapter 35: The First Integrated Circuit (: Part A/Part B within the chapter)

> **Restructuring note (in response to review comments)**: the first edition crammed "turning silicon into wafers" and "turning wafers into circuits" into one chapter, and each side ended up only half written. The two tasks have completely different failure modes: **errors in bulk-material processes are whole-ingot, whole-batch, and silent** — pulled polycrystalline, dislocations in rows, resistivity off-band, iron contamination — none of it visible at the time, exposed only when a test slice is cut, and one failure ruins an entire ingot; **errors in surface-pattern processes are per-wafer, per-layer, and random** — one speck of dust ruins one pattern, one botched development smears one plate, one overlay misalignment kills one chip — visible at the time, but every failure is different. The former's discipline is test-slice inspection and archives; the latter's is layer-by-layer visual inspection and yield statistics; mixed into one chapter, each inevitably shortchanges the other. This edition splits into **Part A 35.A Silicon and Wafer Material Preparation** (purification handover, crystal pulling or zone refining, slicing, polishing) and **Part B 35.B Planar Processing and a Simple Integrated Circuit** (oxidation, photolithography, diffusion, etching, interconnection); each part carries its own complete materials, tools, steps, and parameters, and both share the chapter-end master parameter table, failure modes, acceptance criteria, and the three lists. The honest endpoint is unchanged: **Kilby-style hybrid integration, a few gates' worth of DTL, millimeter-scale line widths** — this chapter promises no upgrade beyond this endpoint.

## Chapter Objectives

**The ultimate challenge, strictly defined**: without a modern chip factory, and on top of the established base of materials, equipment, and measurement, manufacture and verify simple integrated circuits of **limited complexity**; at the same time, honestly mark out which links are feasible under low-industrialization conditions and which must rely on a more advanced industrial base.

**The three goals must not be conflated (the General Outline Iron Law landing in its final chapter)**:

| Goal | Meaning | This chapter's stance |
|---|---|---|
| Understanding integrated circuits | Explain the principles and the manufacturing links | Delivered by the whole chapter |
| Manufacturing simple devices | Manufacture and verify devices of limited complexity | Stretch goal |
| Rebuilding the modern chip industry | Continuous production of high-performance complex products | Explicitly out of scope; a conditions list is given |

The first chip is not a natural outcome of completing the earlier chapters but a concentrated assault — even with everything in place, one may still fall at cleanliness, defect rate, or some overlooked link.

**The deliverables of the two parts**:

| Part | Deliverable | Endpoint criterion |
|---|---|---|
| Part A 35.A | A device-grade pilot wafer line: crystal pulling — slicing — lapping and polishing — inspection and grading | The wafer travel-card system in operation, material issued to Part B by grade |
| Part B 35.B | A closed planar-processing loop and the first integrated circuit | Millimeter-scale line widths, 2–6 devices per chip, on-wafer verification of one DTL logic gate; Kilby-style hybrid integration goes first, to work through packaging and testing |

## Capability Boundary

**Can do:**

- **Part A**: turning the Chapter 34 L2 wafers (small-diameter, mirror finish) into a production line — small-diameter single-crystal ingots (30–50 mm) produced with **necked pulling**, multi-wire slicing, edge chamfering, two-stage lapping, pitch mirror polishing, five inspections, and A/B/C graded issue;
- **Part B**: wet/dry thermal oxidation and thickness calibration (color chart + weighing method); **preparation of dichromate–gelatin photosensitive resist and same-day sensitivity calibration**; enlarged-drawing — microphotography photomask plates (interfacing with Chapter 42's Section 42.7 drafting standards); **photomask contact exposure with gap control**; **buffered-HF window etching and anisotropic etching of silicon (etch rates must be field-calibrated)**; two-step boron/phosphorus diffusion with witness-wafer sheet-resistance monitoring; silver-paste screen printing — fired-on interconnection, and thermocompression / solder bonding; on-wafer probe testing; Kilby-style hybrid integration; DTL gate truth-table verification.

**Explicitly cannot do (conditions listed, entered in the Class-C list):**

1. **Sub-millimeter line widths**: the first version works at 0.5–1 mm line width/pitch — anything finer needs better lenses, photosensitive materials, and alignment mechanisms (multiple generations of industrial iteration);
2. **Stepping-and-repeating photolithography, ion implantation, epitaxial growth**: products of an equipment-generation gap; this chapter registers them but does not attempt them;
3. **ppb-level metrology, sub-micron line-width measurement, in-line defect inspection**: what cannot be measured cannot be made (the ultimate expression of Iron Law Four of the General Outline);
4. **Aluminum interconnect**: electrolytic aluminum needs enormous electric power and cryolite (an unlock item registered in Chapter 32); this chapter substitutes sintered silver paste;
5. **Precise crystal orientation**: X-ray orientation is listed as a Class-C dependency; the first version gets by with cleavage orientation (± a few degrees), enough for millimeter-scale processes and anisotropic etching;
6. **Modern-grade cleanrooms**: replaced by "the six simple-cleanliness rules + yield statistics" (Section 35.B.15).

## Pre-Start Verification (tick each item; a missing item bars its corresponding process from starting)

**Part A (35.A) verification:**

| # | Verification item | Criterion | Source |
|---|---|---|---|
| A1 | Polysilicon feedstock | Chapter 34 purified product; resistivity curve along the rod on record; fracture bright gray and conchoidal, no oxidized yellow skin, no metallic bright spots | 34 |
| A2 | Quartz crucible | Transparent, no clustered bubbles, no cracks; inner diameter ≥ target ingot diameter +10 mm | 14, 34 |
| A3 | Seed crystal | Mirror cross-section free of polycrystalline mottling; length ≥30 mm; gripable; a selected single-crystal section from the previous run | 34 |
| A4 | Crystal-pulling furnace and lift-rotation mechanism | Temperature control ±5 °C (thermocouple cross-checked); pull rate 0.2–2 mm/min continuously adjustable; rotation 5–20 r/min | 12, 25, 34, 21 |
| A5 | Low-vacuum pump set | Pulling chamber evacuated to 1–10 Pa and held (McLeod gauge reading on record) | 33 |
| A6 | Reciprocating saw and steel wire | 0.3–0.5 mm cold-drawn steel wire; stroke ≥ ingot diameter +50 mm; reciprocation 30–80 strokes/min; tension adjustable with 1–3 kgf hanging weights | 21, 31 |
| A7 | Two grades of abrasive | One bottle each of W20 (20–28 μm) and W7 (5–7 μm); no coarse-grit grittiness under a finger rub (graded in Chapter 24) | 9, 24 |
| A8 | Lapping plate and polishing lap | Cast-iron plate passes the marking-compound mutual-lapping check; pitch polishing lap pressed flat, no press marks | 20, 24 |
| A9 | Measuring tools | Micrometer 0.01 mm (zero re-checked against gauge blocks); knife-edge straightedge with uniform light gap; balance sensitivity 0.1 mg (weights calibrated) | 22, 20, 3, 25 |
| A10 | Four-point probe | Five measurements on one wafer, spread <10% (the Chapter 34 L2 criterion, re-measured once) | 34 |

**Part B (35.B) verification:**

| # | Verification item | Criterion | Source |
|---|---|---|---|
| B1 | Wafers | Part A grades A/B, travel card with all five fields complete (ingot number / five-point resistivity / five-point thickness / cleaning record / grade) | This chapter, Part A |
| B2 | Oxidation and diffusion furnaces | Quartz tubes intact and uncracked; two temperature zones: main furnace reaches 1200 °C ±5 °C, source furnace reaches 900 °C ±10 °C; thermocouples within their calibration period | 12, 25, 34 |
| B3 | Hydrofluoric acid and fluorides | HF concentration registered (Chapter 26 procedures); saturated ammonium fluoride solution ≥100 mL (self-made by neutralizing HF with ammonia water; residual crystals at the bottle bottom prove saturation) | 26 |
| B4 | Dopants | Boric acid ≥50 g, ammonium dihydrogen phosphate ≥50 g; dry, sealed, no caking | 23, 34 |
| B5 | Photosensitive raw materials | Gelatin (purified from hide glue: swells without dissolving in cold water, dissolves completely in hot water with no residue, no putrid odor) ≥50 g; ammonium dichromate ≥10 g (orange-red crystals, in a light-shielded brown bottle) | 26, 16 |
| B6 | Photomask plates | Drawn to the three standards of Chapter 42's Section 42.7 and reduced to plates; grid-distortion calibration records on file; **polarity check sheet double-signed** (Section 35.B.7) | 46, 24, 26 |
| B7 | Exposure light source | Carbon arc lamp (Chapter 32 power supply), lamp distance fixable at 300–500 mm and fitted with a light shield; when the daylight procedure is used, record noon ±1 h and cloudless conditions | 32, 24 |
| B8 | Interconnection materials | Fine silver powder (no gritty feel under a finger rub) ≥20 g; low-melting glaze glass powder ≥5 g; one 40–60 mesh silk screen stretched on a frame; rosin, turpentine | 16, 17, 11, 15, 8 |
| B9 | Test station | Microscope with eyepiece micrometer, fine-motion stage, 2–3 spring probes, moving-coil meter (release slip in force) | 24, 27, 31, 33 |
| B10 | High-purity water and vessels | Distilled water ≥10 L; quartz/glass vessels kept dedicated, no iron tools stored among them (Chapter 34 discipline); the simple cleanliness chamber laid out per Section 35.B.15 | 26, 34 |

---

## Part A 35.A Silicon and Wafer Material Preparation

### 35.A.0 Part A Introduction: Bulk-Material Failures Are Silent

The defects Part A deals with — polycrystallinity, dislocations, cracks, resistivity off-band, iron contamination — **none of them is visible on the spot**. The surface of a polycrystalline ingot looks no different from single crystal while it is being pulled; an iron-contaminated batch of silicon still slices into bright mirror wafers. The overarching discipline of Part A is therefore **silent failure first**: for every process step, first establish the test-slice inspection for "how do we find out it was done wrong," then write "how to do it right." Nor is Part A's output just a polished piece of silicon — it is **a piece of silicon with an archive**: ingot number–wafer number, five-point resistivity, five-point thickness, cleaning and polishing records, grade. A wafer without an archive counts as scrap in Part B — when something goes wrong, there is no way to localize whether the material or the process was at fault.

### 35.A.1 Part A Materials List

| Material | Identification standard | Minimum specification | Acceptable substitute (cost) | Signs of a bad lot | Unit consumption |
|---|---|---|---|---|---|
| Polysilicon feedstock | Bright gray conchoidal fracture | Chapter 34 purified product, resistivity curve along the rod on record | Zone-refined re-purified stock (purer, more expensive) | Dull fracture, metallic bright spots, or oxidized yellow skin | 80–120 g per ingot |
| Quartz crucible | Transparent, rings clearly when struck | No cracks; inner diameter ≥ ingot diameter +10 mm | High-purity graphite crucible (ash contamination, resistivity uniformity worsens; downgrade honestly) | Clustered bubbles, cloudy patches | 1 per ingot (reusable several times) |
| Seed crystal | Mirror cross-section, no mottling | Length ≥30 mm | Picked from spontaneously nucleated slowly cooled melt | Snaps at the neck, mottled cross-section | 1 per ingot (recoverable) |
| Cold-drawn steel wire | Bright, rust-free | 0.3–0.5 mm | Music wire (more durable) | Knots, rust spots (crooked kerf) | 2–5 m per ingot |
| Abrasives (two grades) | Uniform grit feel under a finger rub | W20 and W7 in separate bottles | Garnet sand (cutting rate 30% slower) | The two grades mixed together, coarse grains present | 10–20 g coarse lapping and 5–10 g fine lapping per wafer |
| Red iron oxide | Fine, no sandy feel (the levigated grade of Chapter 24) | Polishing grade | Cerium oxide (faster, harder to source) | Contains coarse grains (the main cause of scratches) | 2–5 g per wafer |
| Pitch | For the polishing lap (Chapter 24) | Presses flat without brittle cracking | Beeswax cut with rosin (short lap-face life) | Softening point too high, too hard | 50–100 g per lap |
| Soap, dilute hydrochloric acid, distilled water | Chapter 26 procedures | Vessel grade | — | Suspended matter in the distilled water | 0.5–1 L of wash water per wafer |
| Chamfering whetstone | Fine grit | Handheld edge dressing | Fine sandpaper wrapped on a rod (wears out fast) | Coarse grit (bigger edge chips) | 10–30 passes per wafer |

### 35.A.2 Part A Tools List

| Tool | Source chapters | Precision requirement | Calibration before use |
|---|---|---|---|
| Crystal-pulling furnace + lift-rotation mechanism | 12, 25, 34 + 21 | Temperature control ±5 °C; pull rate 0.2–2 mm/min | Thermocouple cross-check (Chapter 25); pull rate measured once as actual lift per minute |
| Low-vacuum pump set + McLeod gauge | 33 | Pulling chamber 1–10 Pa | Check against the McLeod gauge calibration archive |
| Reciprocating saw | 21 + this chapter | Reciprocation 30–80 strokes/min, stroke ≥ ingot diameter +50 mm | Idle run to check wire whip <0.5 mm; hang the tension weights |
| Cast-iron lapping plate | 20 | Passes the marking-compound mutual-lapping check | Knife-edge straightedge in three directions + spot-blueing recheck |
| Micrometer | 22 | 0.01 mm | Zero re-checked against gauge blocks |
| Knife-edge straightedge, surface plate | 20 | Uniform light gap | Self-check and mutual check |
| Four-point probe | 34 | Five measurements on one wafer, spread <10% | Re-check on a standard wafer |
| Balance | 3, 25 | Sensitivity 0.1 mg | Weight calibration |
| Magnifier, microscope | 24 | 3–5× / with eyepiece micrometer | Eyepiece scale cross-check |

### 35.A.3 Handover from Chapter 34: Release Boundary and Substrate Selection

Chapter 34's four-piece "materials ready list" (wafers starting at L2 / the three-piece purity-monitoring set / dopant stock / HF and furnace temperatures) is Part A's intake port; Part A advances it from "starting at L2" to **device-grade specification**.

**Substrate selection (fixed for the first version, to reduce variables)**: n-type silicon, target resistivity band **1–10 Ω·cm** (an empirical range). Three reasons: too low (heavily doped) and the junction breakdown voltage will not climb; too high (near-intrinsic, e.g. >50 Ω·cm) and collector series resistance is large and drift between batches becomes significant; 1–10 Ω·cm sits in the middle and is the easiest for the four-point probe (Section 34.7) to resolve. The germanium route proceeds in parallel as registered in Chapter 34: germanium slices serve the Kilby-style hybrid track and the point-contact Plan B trials (Chapter 33); silicon wafers serve the main planar-process assault.

**The master-alloy method of doping (a worked dimensional sanity check)**: if the resistivity of the zone-refined/reduced stock is too high, phosphorus must be added to the pulling melt. Back-calculating from a target of 5 Ω·cm: donor concentration about 1×10¹⁵ cm⁻³; 100 g of silicon (about 43 cm³) needs about 4×10¹⁶ phosphorus atoms, i.e. a phosphorus mass of about **2×10⁻⁶ g — 2 micrograms**. A balance with 0.1 mg sensitivity is off by a factor of fifty: **phosphorus cannot be weighed in directly**. The correct approach is two-stage dilution: first smelt a small piece of **phosphorus–silicon master alloy** holding about 0.05–0.1% phosphorus by mass (melt silicon in a small crucible, charge in the 0.05–0.2 g of phosphorus that a balance can weigh, stir fast and cast into a thin sheet), then weigh 50–200 mg portions of the master alloy into the pulling melt. Cut a section from every ingot as soon as it is pulled and measure resistivity, and correct the next ingot's master-alloy charge by the deviation — **the dopant amount is closed in on ingot by ingot, not computed once and fixed for life**.

**Release criterion (mandatory for every ingot)**: the pulled ingot first gets a head test slice (see 35.A.4); only when the acid-etched cross-section confirms single crystal and the four-point probe puts resistivity in band are both items passed and may the whole ingot be sliced; failing that, the whole ingot is downgraded to test-slice stock or sent back to the melt.

### 35.A.4 The Single-Crystal Ingot: Crystal Pulling or Zone Refining

**Figure 35A-1 Crystal pulling and zone refining (schematic)**

```
 Czochralski pulling (Cz)          Zone refining (FZ)
   ┌─pull shaft─┐                    hot zone→  ██▓▓██
   │ seed crystal│                    rod   ░░░░░░░░ ←melt zone translated slowly
   ▼  ↓rotation │                          impurities "swept" toward the rod tail→cut the tail off
  ┌┴─────────┐                    multiple passes→resistivity curve rises along the rod
  │ molten silicon surface │←1414 °C
  └─quartz crucible─┘
```


**Choosing between the two routes (engineering decision table)**:

| Item | Czochralski pulling (Cz) | Zone refining (FZ) |
|---|---|---|
| Diameter | Shoulder shaping controllable; stable at centimeter scale | Limited by rod diameter and surface tension; tends thin |
| Purity | Oxygen and trace contamination dissolve in from the quartz crucible | No crucible contact; highest purity |
| Equipment difficulty | Crucible + lift-rotation mechanism (Chapter 21 parts) | Top and bottom chucks + translation of a narrow melt zone; the more elaborate mechanism |
| Place in this part | **Main route (producing ingots)** | Supplementary (the Chapter 34 apparatus; re-purifying high-resistivity stock) |

**The pulling-furnace environment**: silicon melted in an open furnace grows an oxide skin and no crystal can be pulled — connect the pulling chamber to the Chapter 33 piston pump and pump down to 1–10 Pa of low vacuum (no need for mercury-displacement-pump grade); this suppresses oxidation while keeping a safe observation window.

**The five stages of the pulling program** (each with an observable criterion):

1. **Melting the charge**: the whole charge melts clear and the melt surface is mirror-smooth with no floating dross (dross means the feedstock is unqualified — shut the furnace down);
2. **Dipping the seed**: lower the seed slowly until it touches the melt surface and rotate gently (5–20 r/min); when a bright ring appears in the melt surface around the seed and the seed neither melts back nor thins — the temperature is right;
3. **Necking (the key stage added in this chapter, to squeeze out dislocations)**: pull fast at 2–4 times the normal rate, thinning the crystal to 3–5 mm over a length of 10–20 mm — the dislocations already in the seed annihilate at the side surface of the thin neck and are not carried into the ingot body. Criterion: the neck surface is smooth, without lumps;
4. **Shoulder widening and constant diameter**: drop the pull rate to 0.3–1 mm/min and let the diameter widen slowly to target (30–50 mm), then hold it. Diameter feedback is read by eye: at the crystal–melt boundary on the melt surface there is a bright ring (the meniscus halo), **a steady ring width = a steady diameter**; a ring that suddenly widens means the crystal is thinning — cut power or pull rate, and vice versa;
5. **Tail-off**: once the ingot length (60–100 mm) is reached, speed up the pull and lift away, to prevent suck-back of the tail shrinkage cavity.

◎ Hand-feel for holding the diameter by watching the ring: fix your eyes on the slow change in the width of the meniscus bright ring and follow with your hand on the fine power adjustment. Practice method: melt down scrap feedstock and do dry pulls (no requirement to form an ingot), practicing shoulder widening — constant diameter for five rounds, recording four columns each round: "time — pull rate — power — visually read diameter". Misjudgment compensation: hand-feel is never the sole basis; during a formal ingot pull, record the visually read diameter every 10 min, plot the curve afterward and review it, and after two ingots you can back your ring-watching bias out of the curve.

**Silent failure and the inspection regime (ahead of every output target)**:

- **Polycrystallization**: the surface ridge lines (2–4 crystal edges running the ingot's length) break off, disappear, or go fuzzy — suspect it at visual inspection; confirmation relies on the **acid-etched cross-section of the head test slice** (the Chapter 34 method): a mirror-uniform cross-section means single crystal; mottling or radial patterns mean polycrystal. Polycrystalline ingots are barred from slicing;
- **Dislocations**: after acid etching, the test slice shows pits arrayed in rows (the Section 34.4 criterion) — caused by insufficient necking, or by temperature spikes or vibration during the pull; cut off and discard the sections where the pit rows are dense;
- **Resistivity off-band**: slice one piece from the ingot head and one from the tail and measure with the four-point probe; the ingot is released only if both ends sit inside the 1–10 Ω·cm band; if only one end is in band, downgrade by section.

[Background/Outlook: large-diameter ingots (ten centimeters and up) and automatic diameter control (infrared pyrometry feedback) are the next generation of pulling practice; they wait on the instrumentation industry maturing first, and this chapter promises none of it.]

### 35.A.5 Cylindrical Grinding, Orientation, and the Reference Flat

1. **Grind the circumference**: clamp the ingot and spin it, grinding to size on the disc to the target diameter ±0.1 mm — only then can slicing be concentric and the wafers round; inspect the ground surface under a magnifier for cracks (side-light it: a hairline mark is a crack — cut off and discard that section);
2. **Cleavage orientation** (the Section 34.5 method): tap the ingot end lightly to obtain a cleavage face, giving the azimuth of the {111} plane family;
3. **Grind the reference flat**: along the ingot's length, grind one flat band parallel to the cleavage direction (3–5 mm wide) — carried onto the wafer, this band is the **reference flat**: every Part B layout coordinate, overlay alignment, and dicing direction takes it as the datum (the wafer edition of Chapter 20's "everything starts from the datum"; the physical counterpart of Chapter 42's datum-style annotation). For an ingot whose reference flat is ground in the wrong direction, all of Part B's anisotropic etching and cleavage dicing is thrown off — **two people cross-check the cleavage mark before grinding**;
4. Honest declaration: cleavage orientation is accurate to a few degrees, which suffices for millimeter-scale line widths and anisotropic etching; precise orientation (X-ray diffraction) is listed as a Class-C dependency.

### 35.A.6 Slicing, Lapping, and Polishing

**Slicing (reciprocating wire saw)**: the steel wire (0.3–0.5 mm) is stretched taut and does its cutting carried in an abrasive slurry (30–50 g of W20 abrasive per 100 mL of water, stirred to a thin paste), cutting at 3–8 mm/h (for a 30–50 mm ingot; empirical values that must be calibrated on this machine's first ingot: if the cut is less than 15 mm deep after 4 h, change the slurry or re-tension the wire). Kerf loss is 0.5–0.8 mm per wafer; a single wire cutting one ingot (60–80 mm long yields 40–60 wafers 0.4–0.6 mm thick) takes more than 200 h — **multiple wires in parallel are mandatory** (the Section 34.6 method, 3–4 wires cutting together), so one ingot's worth of wafers comes out in a week. Wafer bow control: wire tension + guide follower; after cutting, give each wafer a first check by laying the knife-edge straightedge against the face and looking for light gaps.

◎ Pluck the stretched wire and listen: flick the tensioned wire with a finger; a high, clear, uniform tone with no muffled beats means the tension is right. Practice method: hang 1/2/3 kgf weights in turn on same-diameter wires and pluck-and-listen 20 times each, to build a pitch-to-tension feel. Misjudgment compensation: always set the wire tension quantitatively with hanging weights (1–3 kgf; empirical — fix the value after calibrating the wire-break rate on this saw); listening serves only as a quick check.

**Chamfering**: by hand on a whetstone, grind a symmetric 45° chamfer, 0.2–0.5 mm wide, onto the wafer edge — a right-angle knife edge is the source of edge chipping, and in Part B it makes resist pile up at the rim during coating (edge resist beads are a hotbed of dust and defects).

**Lapping (two stages)**: coarse-lap with W20, removing 60–100 μm per face (20–40 min); fine-lap with W7, removing 15–30 μm per face. Two Iron Laws: **each stage must remove ≥3 times the previous stage's grit diameter** (the damage-layer rule of thumb — the subsurface damage pressed in by the previous abrasive must be lapped away wholesale by the next; calibration method: if the wafer still will not brighten after more than 4 h of polishing following fine lapping, the lapping damage was not fully removed — go back to fine lapping); **alternate the two faces, and lap each face in segments** (removing too much from one face in one pass is the source of warpage, and warped wafers cannot be pressed tight against the photomask in Part B).

**Polishing**: a pitch polishing lap (Chapter 24) + red iron oxide in a water slurry (5–10 g per 100 mL of water), 1–3 h per face. Acceptance: under a dark-field lamp at an oblique angle with a magnifier, **no scratch scattering** (Section 34.6); the water-film test spreads uniformly (Section 34.7).

**Cleaning chain** (Section 34.6 retained and tightened): scrub both faces with a soft brush in soap solution → soak 5–10 min in dilute hydrochloric acid to strip metal contamination → rinse three times in distilled water → **no cloth touches the faces; stand upright and air-dry in the shade** (cloth fibers are a contamination source). After cleaning, hold wafers only by the edge, with finger cots on or with bamboo tweezers.

[Card 35-01 Slicing and Polishing] (eight fields)

1. **Input materials**: single-crystal ingot qualified by cylindrical grinding and orientation (head test slice on file); cold-drawn steel wire 0.3–0.5 mm; W20 and W7 abrasives; red iron oxide; pitch lap; soap, dilute hydrochloric acid, distilled water; chamfering whetstone. Batch per run: half an ingot or 10 wafers.
2. **Tools required**: reciprocating saw (before use, idle-run to check wire whip <0.5 mm and hang the tension weights); cast-iron plate (marking-compound mutual-lapping check before use); micrometer (zero re-checked against gauge blocks); knife-edge straightedge; dark-field lamp + magnifier; balance (sensitivity 0.1 mg, calibrated).
3. **Operating sequence and control points**: ① wax the ingot onto the fixture and mark the reference-flat direction with a scribed line; ② **first cut one 1 mm test slice and acid-etch it to verify single crystal; if it fails, stop cutting**; ③ slice with the wires laid out in parallel, **recording the cut depth every 30 min**, cutting rate 3–8 mm/h; ④ take the wafers off and remove the wax in hot soapy water; ⑤ **chamfer both faces at 45°, width 0.2–0.5 mm**; ⑥ coarse-lap with W20, 20–40 min per face; ⑦ fine-lap with W7, 20–40 min per face, **alternating faces**; ⑧ polish 1–3 h per face; ⑨ the full cleaning chain, **no cloth touching the faces, standing upright and air-drying in the shade**.
4. **Empirical parameters and calibration methods**: cutting rate 3–8 mm/h (fixed by actual measurement on this machine's first ingot); abrasive slurry ratio 30–50 g/100 mL (judged by the cutting rate: below 2 mm/h, replenish the abrasive or change the slurry); the 3× removal rule (back-checked through polishing time); wafer thickness 0.4–0.6 mm (micrometer at five points: center + four edges, spread <0.1 mm on a 40 mm wafer; empirical — must be calibrated to this plate's precision).
5. **In-process observation records**: kerf width, machine time per wafer, lapping and polishing time per face, dark-field scratch count, water-film condition, edge-chip count — enter each item into the wafer travel card.
6. **Accept / rework / scrap criteria**: accept = no scratch scattering under dark field + uniform water-film spread + five-point thickness spread <0.1 mm + no chip cutting into the mirror region; rework = residual scratches (back to polishing for 30 min and re-inspect), warpage (lap the reverse face symmetrically, re-measure the five points); scrap = cracks and hidden cracks (hairlines under side lighting), chips out of the mirror region, lapped through in thickness.
7. **Common failures and troubleshooting order**: crooked cut → first check wire tension (weights + listening) → check slurry concentration → check guide wear; will not polish bright → first check whether fine lapping went far enough (back-check the 3× rule) → check the iron-oxide slurry → check the pitch lap for press marks; wafer cracks → first check whether chamfering was skipped → check the cleaning temperature differential (thermal shock).
8. **L1/L2/L3 evidence**: L1 = 1 qualified wafer + dark-field observation record; L2 = ≥10 qualified wafers from the same ingot + complete thickness and resistivity archives; L3 = wafering yield ≥60% for 3 consecutive ingots (empirical — needs long-term statistics) + records of the travel-card system in operation.

### 35.A.7 Cleaning, Inspection, Grading, and the Wafer Travel Card

**The five inspections** (every wafer, in order): ① dark-field appearance (scratches, haze, particles); ② water-film test (grease films and organic residue); ③ thickness and parallelism (micrometer at five points, entered into the archive); ④ resistivity (four-point probe at five points: center + four edges; spread <20% counts as uniform — empirical, must be calibrated against this ingot); ⑤ reference-flat check (direction, completeness). Inspections are carried out wearing finger cots inside the simple cleanliness chamber.

**Grading table**:

| Grade | Criterion | Destination |
|---|---|---|
| Grade A | All five inspections pass | Part B device wafers |
| Grade B | Minor appearance scratches, thickness within spec | Witness wafers and process test slices (photosensitivity calibration, etch calibration, masking witness wafers) |
| Grade C | Resistivity off-band or morphology defects | Remelt stock or practice wafers |

**The wafer travel card** (five fields — the wafer edition of the Section 42.6.3 five pieces of accompanying information): ingot number–wafer number / five-point resistivity / five-point thickness / cleaning and polishing record (bath number, date, person) / grade. The card travels with the wafer; entering any Part B furnace means copying the card's ingot number into the furnace log — **when a wafer is scrapped in Part B, the card lets you trace responsibility back to its Part A step**.

What Part A delivers is not silicon wafers but **silicon wafers with archives**: with the archive, every failure in Part B can be pinned down to "material wrong or process wrong"; lose the archive, and everything Part A did counts for zero the moment troubleshooting starts.

---

## Part B 35.B Planar Processing and Simple Integrated Circuits


---

## Part A Fixed Blocks (Specific to 35.A)

## Part A Failure Modes and Diagnostics
See the "Failure Modes and Diagnostics" table, Group A, in Part B (bulk-material failures); Part A-specific criteria: rising resistivity curve, mirror-surface dark field, parallelism archive.

## Part A Process Card Index
## Part A Acceptance Criteria
**L1**: one zone-refining resistivity-curve lift; **L2**: a Czochralski-pulled small single crystal + three mirror wafers; **L3**: stable monthly wafer output + an iron-contamination-free closed loop (counted jointly with Part B's L3).

## Part A Work-Hours, Manpower, and Consumption

| Zone refining one rod (5 passes) | 2 people on rotating watch | 1–2 days |
| Czochralski pulling one ingot | 2 people on rotating watch | half a day – 1 day |
| The three wafer processes, 10 wafers | 2 people | 2 days |

## Part A Safety Boundary
The full HF/chlorine red-line set (Chapter 26); pulling-furnace high temperature and quartz shattering (goggles + shield); the arc furnace per the Chapter 32 high-voltage procedures.
## Part A Next-Step Dependencies
Wafers + dopants + HF + furnace temperature = the four major release items for Part B (35.B); the three-piece purity-monitoring set → Chapter 42 production-line quality inspection; resistivity grading lets Part B draw material by grade.
