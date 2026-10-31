# Chapter 34 From Minerals to Semiconductor-Grade Materials

## Chapter Objectives

Walk the materials chain "silicon-bearing minerals → metallurgical silicon → high-purity silicon → single crystal → wafer" to its end, and establish the means of testing material quality. **This chapter is where the whole book is most prone to unrealistic leaps**: making silicon is not the same as making silicon fit for chip production. Purity, crystal defects, dopant distribution, surface condition — each demands dedicated equipment, measurement, and quality control; this chapter's task is to quantify that distance, and to state how far one can go under low-industrialization conditions and what is missing where one cannot.

## Minimum Prerequisites

| Capability | Source |
|---|---|
| Quartz / quartz sand identification | Chapters 2, 14 |
| Arc-furnace-grade electricity, carbon electrodes | Chapters 12, 32 |
| Distillation, chloride chemistry, HF | Chapter 26 |
| High-temperature furnaces and temperature control, thermocouples | Chapters 12, 25, 33 |
| Wire drawing (cutting wire), abrasive polishing | Chapters 9, 24, 31 |
| Resistivity measurement, spectroscopy | Chapters 30–33 |

## Capability Boundary

**Can do:** high-purity polysilicon (distillation route) + small single crystals (Czochralski pulling, centimeter scale) + mirror wafers; zone refining accepted against the "along-rod resistivity curve"; purity monitoring by the three-piece set: four-point probe + temperature coefficient + water-film test.

**Explicitly cannot do:** direct detection of electronic grade beyond 6N or of impurities below the ppm level (monitored indirectly by electrical methods; registered honestly); large-diameter low-dislocation standards; the silane route (purer and riskier; not implemented); a cleanroom system (Chapter 35 mitigates with simplified clean handling).

**External dependencies:** hundred-kilowatt-scale continuous power (the arc furnace's first gate — the Part 10 environment versions judge "admission to semiconductors" on exactly this one item); a quartz/ceramic vessel closed loop (**iron tools are strictly forbidden from contact**).

## Pre-Work Verification (check one by one)

| # | Verification item | Criterion | Source |
|---|---|---|---|
| 1 | Power grid | Arc-furnace-grade continuous supply verified in the field (Chapter 32 L2) | Chapter 32 |
| 2 | Chlorine and HF | Gas generation, absorption barrels, two-person procedures all in place | Chapter 26 |
| 3 | Thermometers and thermocouples | Low range: 58 ℃ glass thermometer usable; **continuous temperature measurement at the 1400 ℃ level not unlocked** (platinum–rhodium thermocouple listed as Class C; iron–constantan's 750 ℃ ceiling **must not be passed off** as suitable) — crystal-pulling temperature control is executed via the power–melt-surface calibration curve + slump-cone set (temperature cones)/visual observation, with errors honestly filed | Chapters 25, 27 |
| 4 | Iron-free vessels | A set of quartz/ceramic/graphite vessels; steel mortar replaced with ceramic mortar | Chapters 11, 14 |
| 5 | Four-point probe | Equally spaced four-needle rack built; moving-coil meter cleared by release slip | Chapters 31, 27 |
| 6 | Chapter 33 interface | Vacuum ladder and McLeod gauge usable (reused in the reduction and degassing steps) | Chapter 33 |
| 7 | Rectification-ratio archive | Chapter 33 comparison table in hand — the motivation and acceptance baseline for "why purify" | Chapter 33 |

---

### 34.1 Silicon-Bearing Minerals versus Silicon Materials

- Quartz (vein quartz, quartzite, high-purity sand): SiO₂; **the dividing line between glass-grade sand and semiconductor-grade sand is impurities** — glass tolerates iron at the per-mille level (it only colors the glass), while every step of the semiconductor route is a fight against impurities at the few-parts-per-million level;
- Three grades of silicon material (register table):

| Grade | Purity (approx.) | Use |
|---|---|---|
| Metallurgical-grade silicon | 98–99% | Alloys, upgrade feedstock |
| Polysilicon (high purity) | 99.999% (5N) and above | Crystal-pulling feedstock |
| Single-crystal silicon ingot | 5–6N + crystal integrity | Wafers |

- Germanium route (registered in parallel, **downgraded to long-term** — the sphalerite by-product depends on a zinc smelting line that is not built): sphalerite smelting yields enriched germanium as a by-product (Chapter 16); **point-contact and alloy devices tolerate impurity levels more leniently than the silicon planar process** — silicon as the main line, germanium as the validation route for pioneering devices (Chapter 35's first article is prototyped in germanium; the main line runs silicon).

### 34.2 From Mineral Feedstock to Metallurgical Silicon

**Carbothermal reduction (the feasible small-scale route)**:

1. Feedstock: hand-picked quartz (hand selection + acid pickling to remove the iron skin, Chapter 26), charcoal/coke (Chapters 6, 23), metered to the reduction ratio (theoretical carbon quantity + registered excess);
2. Furnace type: crucible-type resistance furnace (carbon electrodes + refractory clay lining, Chapter 12; power supplied by the Chapter 32 grid — **this is the first strategic return on "the grid exists"**);
3. Product: crude silicon mixed with iron — **tapped silicon dissolves iron**, and iron is the number-one electrically active impurity (carrier killer), so **iron tools are strictly forbidden from any downstream contact** (the ceramic/graphite/quartz vessel discipline is established from here on);
4. Crush the crude silicon (steel mortar swapped for ceramic/quartz mortar), acid leach (hydrochloric acid + hydrofluoric acid to wash off surface oxides and metals — the full Chapter 26 acid procedure applies).

Yield and power consumption go into the ledger: the arc route is power-hungry — **without hundred-kilowatt-scale continuous electricity there is no metallurgical silicon** — this is the first gate in the Part 10 environment versions' judgment of "whether the local site can take the semiconductor route."

### 34.3 Why Semiconductors Need Higher Purity

- Establish the doping concept first: semiconductor conductivity is decided by vanishingly small amounts of impurities — **foreign atoms at the one-ppm level can shift resistivity by several orders of magnitude** (an engineering statement under the knowledge-preservation background);
- Three corollaries: ① no purity control = no device control (parameter drift is unpredictable); ② "deliberately added impurities" (doping) and "accidental impurities" (contamination) are two different things — the former is a knob, the latter is noise; ③ the ability to measure purity is as important as the ability to purify (cannot measure = cannot control);
- Target register: wafer-grade silicon requires harmful metallic impurities down to below the ppm order, and controlled dopants accurate to a relative error of a few per mille — **in the language of Chapter 26's "four-tier purity ladder": this chapter is the sprint from industrial purity to high-purity/electronic grade**.

### 34.4 Purification, Crystallization, and Material Defects

**Chemical purification route (distillation, main route)**:

1. Silicon powder reacts with chlorine (obtained by salt electrolysis or the hydrochloric acid–oxidizer method; Chapter 26 gas collection) → silicon tetrachloride (a liquid, boiling point about 58 °C, within the Chapter 25 thermometer range);
2. **Fractional distillation**: silicon tetrachloride is separated from impurity chlorides (different boiling points; iron/titanium/boron chlorides) by multi-stage distillation — a direct scale-up of the Chapter 26 fractionating column; purity is controlled by the number of distillation passes and by intermediate-fraction management;
3. Reduction: pure silicon tetrachloride reduced by red-hot metal — **honest downgrade: the zinc smelting line is not built (Chapter 16: "no condensation-collection means, zinc abandoned"), and the magnesium/sodium routes are not unlocked either, so this chapter currently stops at crude silicon + acid pickling; SiCl₄ reduction is listed as a Class-C dependency to be cracked, and its unlocking depends on the Chapter 17 zinc-line unlock-conditions chapter going first**;
4. Vessels throughout: quartz/ceramic/glass (Chapters 14, 26), to forestall new contamination.

**Zone refining (physical method, polysilicon → higher purity)**:

- Apparatus: a polysilicon rod laid horizontally in a quartz boat; a slit resistance furnace (or a row of multi-flame torches) forms a narrow molten zone that traverses slowly;
- Principle (segregation): most impurities are more soluble in the liquid phase — as the molten zone passes, impurities are "swept" toward the rod tail; **repeat over many passes**, then cut off the tail end;
- **Molten-zone travel speed (this chapter's core parameter)**: too fast and the impurities have no time to segregate — purification fails; too slow and heat and time costs run away. **Empirical starting point: 1–3 cm per hour (slow setting)**, must be field-calibrated — run one rod in three segments at three speeds, compare the rise of each segment's resistivity-along-rod curve, and take the setting with the best "rise per hour." **The criterion is not the speed number; it is the curve**;
- Effect verification: measure resistivity segment by segment (Section 34.7) and plot the "along-rod curve" — purity improvement is curve rise; this is the direct evidence of whether purification works.

**Crystallization (Czochralski pulling)**:
1. Polysilicon melted in a quartz crucible (about 1414 ℃, thermocouple + instrument temperature control);
2. Dip the **seed crystal** into the melt surface and pull upward with slow rotation; first-article seed source: picked from crystal nuclei that form spontaneously in a slowly cooled melt (cross-section inspection);
3. Diameter control = manual feedback on pull rate and temperature (the first version accepts centimeter-scale diameters; **empirical pull-rate starting point 0.5–2 cm/h**, needs calibration — the pull rate over the diameter-stable section is this run's optimum, copied into the furnace archive);
4. Single-crystal criteria: straight crystal edges on the surface; mirror cross-section without polycrystalline mottling; dislocations revealed as etch pits (after acid etching, pit rows = outcrops of dislocation lines, viewed under a magnifier).

**Defect list** (each item paired with one inspection): grain boundaries (cross-section mottling), dislocations (etch pits), impurity striations (resistivity fluctuation around the circumference), cracks and bubbles (inspection against light).

[Card 34-01 Zone Refining] (eight fields)

1. **Input materials**: the polysilicon rod to be purified (acid-pickled crude silicon from 34.2 or purified charge from 34.4, cross-section inspected, **with a no-iron-contact record**); a quartz boat (transparent, no cracks, no clustered bubbles, bore long enough for the whole rod); atmosphere after the dry purge of 34.10 — a wet vessel hydrolyses silicon tetrachloride and scraps the whole rod (red line).
2. **Tools required**: slit resistance furnace (or the Chapter 14 lamp-worker multi-flame torch row); quartz boat and long charging tongs (quartz/ceramic tips); lead-screw/rail translation stage (Chapter 21) driven by hand or a counterweight; drip timer (Chapter 25) to check constant speed; four-point probe and moving-coil meter (Card 34-04), micrometer (Chapter 22); scribing needle (to cut the pass number on the rod end); along-rod curve paper (Card 25-07) and furnace archive.
3. **Operating sequence and control points**: ① scribe the pass number and direction on the rod end → ② load the boat — rod horizontal, quartz/ceramic vessels throughout, **no iron contact** → ③ strike the molten zone — align the slit, and fix the zone width by the visual "bright band" holding constant (◎) → ④ traverse the whole rod at the chosen speed setting, **at constant rate**, checking start and finish against the drip timer → ⑤ log the pass number when a pass ends, then return or reverse for the next → ⑥ measure resistivity segment by segment (Card 34-04, five readings on one piece with range <10%) and plot the along-rod curve → ⑦ stop when the curve no longer rises and **cut the tail as a whole section**. Control points: **the molten zone must not "break band"** (a break band = heat-source fluctuation; void the pass and run it again); change the speed and segregation fails, the curve stops moving at once; **the criterion is the curve, not the speed number**.
4. **Empirical parameters and calibration**: molten-zone travel speed, empirical starting point **1–3 cm/h (slow setting)**; number of passes typically **3–10**, with "the curve no longer rises" as the end point; the tail is the impurity-enriched section and is **cut off as a whole — never ground down and reused**. Calibration: run one rod in three segments at three speeds, compare the rise of each segment's along-rod resistivity curve, take the setting with the best "rise per hour," copy it into the furnace archive and follow it thereafter. Work-hours reference: one rod, 5 passes, 2 people on rotation, 1–2 days (work-hours table). All of these are **empirical values that must be calibrated to local conditions** — rod diameter, furnace type and heat-source form all affect segregation efficiency.
5. **Observations to record**: start/finish time and actual speed of every pass; whether the zone "breaks band" and when; bright-band width; colour change of the rod surface (first sign of fresh contamination); pass number and direction; segment resistivity readings (measurement-point map, spot temperature); length of tail cut off; record of vessels and hand contact (no-iron discipline).
6. **Pass / rework / scrap criteria**: pass = the along-rod curve rises monotonically and, with the tail cut, the middle sections meet the resistivity target (Card 34-04 five-reading range <10%, inside the target band); rework = insufficient curve rise → add passes (still within 3–10); a middle-section drop → check the no-iron-discipline record and re-run the rod in quartz/ceramic vessels; scrap = cracked rod (reload and re-run, that rod downgraded); confirmed vessel contamination that does not recover on a re-run (the charge is contaminated throughout — downgrade or return to the furnace).
7. **Common failures and troubleshooting order** (by frequency): (1) the curve does not move → check speed first (too fast, no time to segregate), then whether the heat source broke band, and slow down for a re-run; (2) middle-section resistivity drops → check the no-iron-discipline record (iron vessels are this chapter's number-one contamination source) and re-run in quartz/ceramic; (3) rod cracks → check the heat-up/cool-down rate and whether the boat gripped the rod (thermal stress), reload and cool slowly; (4) tail not cut clean and the middle never qualifies → the cut is too short (the impurity-rich tail must go as a whole); (5) the curve steps or breaks → traverse jamming or heat-source power jumping (check lead screw, rails and supply).
8. **L1 / L2 / L3 evidence**: L1 = one rod through one pass with the along-rod resistivity curve on file; L2 = one rod of 3–10 passes with a monotonically rising curve and the middle sections meeting the target after the tail cut, curve and speed setting both on file; L3 = curves from several rods comparable side by side, the three-speed calibration on record, and a second person running one rod from this card alone obtaining a comparably reproducible curve.

[Card 34-02 Czochralski Single-Crystal Pulling] (eight fields)

1. **Input materials**: polysilicon charge (purified per Section 34.4, with a no-iron-contact record); quartz crucible (transparent, no clustered bubbles, no cracks, bore large enough for the charge); seed crystal (mirror cross-section, no mottling — or picked from nuclei formed spontaneously in a slowly cooled melt, cross-section inspected); argon (backfilled after evacuation, Chapter 33 vacuum ladder); graphite support and carbon-felt heat shield (Chapter 12).
2. **Tools required**: pulling furnace (graphite heater + crucible lift/rotation mechanism, Chapters 12 and 21); vacuum pump and McLeod gauge (Chapter 33); a 20–30 mm viewing hole in the top cover + a double-pane quartz window 100–150 mm above the hole (panes about 10 mm apart: the inner pane blocks silicon vapor, the outer blocks spatter) + a dark filter; power control (single section in the first version); calipers (Chapter 22, as visual-judgment compensation); furnace archive sheet. **Temperature: continuous measurement at the 1400 ℃ level is not unlocked** (Chapter 25, Class C) — pulling temperature control runs on the power–melt-surface calibration curve plus visual judgment, with the error filed honestly.
3. **Operating sequence and control points**: charge (crucible rim level with, or 10–20 mm below, the heater's top edge; set with shim plates on the first run and copied into the furnace archive) → evacuate and backfill argon → melt until the surface is mirror-bright with no dross (dross = the charge is unacceptable; shut down) → dip the seed (a bright ring appears, the seed does not melt thin) → **necking** (to suppress dislocations) → shoulder and body → tail-off and lift → cool in the furnace; **the shield may be opened only below 200 ℃ on the thermocouple**. Control points: read the diameter once a minute; **adjust power in ±3% steps**, wait 1–3 min and read again; a single adjustment must not exceed ±5% (one big step is enough to snap the thin neck); **nitrogen is strictly forbidden at molten-silicon temperature** (it forms a silicon nitride skin) — permitted only in the cooling stage after the ingot has fully frozen, and registered.
4. **Empirical parameters and calibration**: silicon melting point ≈1414 ℃ (physical reference); empirical pull-rate starting point 0.5–2 cm/h (Section 34.4), and the pull rate over the diameter-stable section is this run's optimum, copied into the furnace archive; power–melt-surface calibration: after melting, fix pull rate and rotation, start from the baseline power at "diameter stable," step ±3% each time, wait 5 min, read the diameter once, repeat for 5–6 points to get this run's "power deviation — diameter change" curve (thermal lag about 1–3 min; self-calibrated every run, since charge size and crucible age both matter). Visual compensation: measure the pulled section with calipers; practise the feel on 3 scrap-ingot runs, watching only and not pulling, and pull a real ingot only once the estimate error has converged to ±0.5 mm. All of these are **empirical values that must be calibrated to local conditions**.
5. **Observations to record**: run number and batch, charge weight and crucible age, diameter readings (per minute / per 10 min), power and every adjustment size, pull rate and rotation speed, whether the molten zone "breaks band," mechanical vibration, power-failure events (time / duration / response / loss), shield-opening temperature — all into the furnace archive.
6. **Pass / rework / scrap criteria**: pass = body diameter within ±1 mm of target, straight crystal edges, mirror cross-section with no polycrystalline mottling (confirmed by acid-etching the head test slice), dislocation etch-pit rows not dense; rework = thin neck snaps / crown drops (change seed, re-neck, trim power in ≤±3% steps, add anti-vibration pads to the furnace); scrap = mottled cross-section (polycrystalline — the whole ingot is downgraded to test material or returned to the furnace), quartz crucible explosion.
7. **Common failures and diagnosis order**: (1) crystal break / crown drop → first check for a sudden power rise or pull-rate drop (review the archive's power–pull-rate curve) → check mechanical vibration → change seed and re-neck; (2) ingot turns polycrystalline (edges interrupted, mottled cross-section) → first check thermal shock and vibration → check seed dislocations → never skip the necking stage; (3) diameter runs away → first check whether the power–diameter curve was self-calibrated for this run → check whether a single adjustment crossed ±5% → check window deposition blocking the view; (4) explosion on opening → check whether the shield was opened before the thermocouple fell below 200 ℃, and whether the crystal was jerked out of the melt during an outage (red line).
8. **L1 / L2 / L3 evidence**: L1 = one centimeter-scale single crystal with an acid-etched mirror head slice on file; L2 = a furnace archive holding this run's power–melt-surface curve plus pull-rate and diameter logged section by section, with two consecutive ingots meeting the body criterion; L3 = monthly output in the ledger, crystal-break rate classified by outage versus handling, and a second person pulls an ingot from this card alone. **Boundary: large diameters (above ten centimeters), low-dislocation industrial standards, and automatic diameter control are not built by this card — outside the capability line** (this chapter's Class-C items; the background box at the end of 35.A).

### 34.5 Crystal Orientation and Crystal Quality

- Crystal orientation concept (engineering formulation): a single crystal cleaves/etches differently along different directions — **a cross-section cleaved along the cleavage plane is flat and bright** (it opens with a light knife tap); orient dicing with the cleavage plane as the datum (saves sawing and grinding);
- Orientation marking: a flat is ground on the ingot end as the "reference flat," and all subsequent photolithography alignment (Chapter 35) takes it as the coordinate datum — **the first "datum" on the wafer is the same idea as the Chapter 20 surface-plate datum** (a transplant of the precision-manufacturing philosophy: everything starts from a datum);
- Quality grading table: pulled ingots are sorted into three classes by (dislocation density / resistivity uniformity / diameter uniformity) — top class becomes device wafers, middle class becomes test wafers, low class returns to the furnace.

### 34.6 Wafer Cutting, Grinding, and Polishing

1. **Cutting**: steel wire (Chapter 31 wire drawing) + abrasive slurry (Chapter 9 carborundum grade) with reciprocating sawing (many wires wound in parallel to cut many wafers at once); slices are cut thick, leaving a grinding allowance;
2. **Grinding**: cast-iron lapping plate (Chapter 20) + progressively finer abrasives, alternating between the two faces (parallelism measured at multiple points with the Chapter 22 micrometer);
3. **Polishing**: pitch polishing lap (a direct transplant of the Chapter 24 lens process) + fine iron-oxide-red abrasive to a mirror finish; **surface quality is inspected by "no scratch scattering under dark-field illumination"** (magnifier + obliquely aimed lamp);
4. Cleaning: soap solution → acid pickle → distilled-water rinse → **no cloth touches the face; dry upright in the shade** (cloth fibers are a contamination source);
5. Flatness archive: each wafer numbered + thickness/parallelism recorded (the Chapter 22 system extended to wafers).

[Card 34-03 Wafer Cut-Grind-Polish, Three Operations] (eight fields)

1. **Input materials**: single-crystal ingot (a 34-02 pass, reference flat ground, quality grade on file); steel wire (Chapter 31 drawn, 0.3 mm class, one class per saw); abrasive slurry (Chapter 9 carborundum grade + water, ratio set so the slurry does not dry out, registered); graded abrasives (coarse to fine, stored in separate containers); red iron oxide (Chapter 24 water-elutriated grade); pitch lap material (Chapter 24); soap solution, dilute hydrochloric acid, distilled water (Chapter 26).
2. **Tools required**: reciprocating saw / multi-wire saw (Section 34.12 tooling: winding frame, classed spacers, tension counterweight wheel); cast-iron lapping plate (Chapter 20, marking-compound mutual-lapping check passed); pitch lap (pressed flat, no press marks); micrometer 0.01 mm (zero checked on gauge blocks); knife-edge straightedge and surface plate; dark-field lamp + 3–5× magnifier. Wafer thickness and kerf: calibrated on the first cut (**spacer thickness = target wafer thickness + measured kerf width**; spacers stored sorted in ±0.05 mm classes).
3. **Operating sequence and control points**: ① mount and align (reference flat against the locating stop; the first version cuts square at 90°; one plate mounted all facing the same way) → ② saw (constant feed, slurry never dries, stop at once on a wire break) → ③ unload and de-wax in hot soapy water → ④ lap: cast-iron plate + graded abrasives, **alternating faces and running each face in stages** (one heavy single-face pass is the source of warpage) → ⑤ polish: pitch lap + fine red iron oxide to a mirror → ⑥ cleaning chain: soap → dilute hydrochloric acid → distilled-water rinse → **no cloth on the face; stand upright and air-dry in the shade** → ⑦ number every wafer into the flatness archive. Control points: parallelism measured with the micrometer at several points; surface quality judged by **no scratch scattering under dark-field illumination**, never by how bright it looks.
4. **Empirical parameters and calibration**: this chapter **gives no fixed times, pressures, or abrasive concentrations for lapping and polishing** — the setting is back-derived from the outcome criteria: first-article five-point thickness range <0.05 mm and edge chipping <1 mm (Section 34.12); wafers are accepted on "mirror finish + no scratch scattering in dark field + thickness/parallelism archive" (parameter master table). Will not polish bright = fine lapping fell short (go back one abrasive grade); abrasives are **stored in separate graded containers**, and coarse grains carried over from an earlier stage are the main cause of scratches. The times and concentrations so fixed are **empirical values that must be calibrated to this plate and this saw**.
5. **Observations to record**: wafer number, kerf width and machine time, lapping/polishing time and abrasive batch per face, dark-field scratch count, five-point thickness and parallelism, chip location and size, cleaning bath number and date — item by item into the wafer archive.
6. **Pass / rework / scrap criteria**: pass = mirror finish, no scratch scattering in dark field, five-point thickness and parallelism on file, no chip reaching the mirror region; rework = thickness still within allowance → rescue at the next lapping grade; residual scratches → back to polishing for 30 min and re-inspect; scrap = cracks and hidden cracks (hairlines under side lighting), chips out of the mirror region, lapped through in thickness.
7. **Common failures and diagnosis order**: (1) scratches after polishing → first check whether abrasives were mixed (coarse grains from an earlier stage) → check the lap for press marks → check cloth and settled dust; (2) wafer cracks or edge chipping → first check abrasive grit and feed (finer abrasive, slower feed) → check that mounting really bonded (a solid note when tapped with a wooden handle); (3) uneven thickness / warpage → first check tension uniformity → check whether faces were alternated and whether one face was over-lapped; (4) haze on the surface → check the cleaning chain for a skipped acid pickle and the water for suspended matter.
8. **L1 / L2 / L3 evidence**: L1 = one mirror wafer + dark-field observation record; L2 = several pass wafers from the same ingot + complete thickness / parallelism / wafer-number archive (traceable ingot number to wafer number); L3 = batch archives bound into volumes, and a second person makes a pass wafer from this card alone. **Boundary: this card reaches only as far as "no scratch scattering in dark field"; quantitative acceptance of micro-topography and sub-micron metrology is not built here — outside the capability line** (sub-micron linewidth measurement is a Chapter 35 Class-C item).

### 34.7 Surface Contamination and Material Inspection

- **Resistivity (simplified four-point probe)**: four equally spaced needles pressed on the wafer face; the outer pair carries current, the inner pair measures voltage (Chapter 31 moving-coil meter) — the ratio converts to resistivity; a shape-correction table is self-made (same material, pieces of different sizes cross-checked against each other);
- **Resistivity temperature coefficient**: reuse the Chapter 33 test — resistivity falling as temperature rises (negative coefficient) is the semiconductor signature; **an anomalous coefficient = a clue to metal contamination**;
- **Thermoelectric and photosensitivity spot checks** (the Chapter 33 three observations): batches are sampled; abnormal ones isolated;
- **Spectroscopy** (Chapter 24 spectroscope + Chapter 26 flame colors): emission-line spot checks for trace metals — limited sensitivity; register honestly that "only coarser contamination can be detected; below the ppm level, monitoring must be indirect, by electrical methods";
- **Surface cleanliness**: water-drop spread test (a clean hydrophilic surface spreads water into an even film; oily spots make droplets bead up) — a zero-cost, high-information field criterion.

[Card 34-04 Four-Point-Probe Measurement] (eight fields)

1. **Input materials**: the wafer or test slice to be measured (clean, dry, no oil film); a standard wafer or a piece of the same material of known resistance (for cross-checking); distilled water and soap solution (pre-measurement cleaning).
2. **Tools required**: equally spaced four-needle rack (four needles at equal spacing, tips level, spring-loaded contact); moving-coil meter (Chapter 31, cleared by release slip); constant-current source or battery pack + series resistor; micrometer for thickness (Chapter 22); thermometer (Chapter 25, to record spot temperature); the self-built "shape-correction table" and "resistivity–impurity concentration table" (kept in the archive).
3. **Operating sequence and control points**: ① clean and dry → ② press the four equally spaced needles on the wafer face, **the outer pair carries current, the inner pair measures voltage** → ③ read current and voltage and convert to resistivity by the ratio (corrected with the shape table) → ④ measure five points on the same wafer (center + four edges) → ⑤ record the spot temperature → ⑥ register by batch. Control points: equal needle pressure (uneven pressure scatters the readings), never re-press the same spot, and the measurement counts only when **five readings on one wafer show a range <10%**.
4. **Empirical parameters and calibration**: repeatability criterion = five readings on one wafer with range <10% (parameter master table, L2 criterion; **empirical, must be calibrated to local conditions**); the shape-correction table is self-built by cross-checking pieces of the same material in different sizes; the conversion table starts from the Chapter 33 rectification comparison data and theoretical curves, gaining one self-check point each time a doping batch is blended and converging step by step on this line's true curve — the table lives in the archive and **converting from memory is forbidden** (Section 34.13). Temperature: resistivity falling as temperature rises (negative coefficient) is the semiconductor signature, and **an anomalous coefficient is a clue to metal contamination**, so the temperature must be recorded at every measurement.
5. **Observations to record**: wafer/batch number, measurement-point map, current and voltage readings, converted resistivity, five-point range, spot temperature, conversion-table version, operator and date.
6. **Pass / rework / scrap criteria**: pass = five-point range <10% and resistivity inside the target band (table version noted); rework = range over 10% → reclean, re-measure at constant temperature, take five new points clear of defects; scrap = still scattered on re-measurement and accompanied by an anomalous temperature coefficient (judged metal-contaminated; the sample is downgraded or returned to the furnace).
7. **Common failures and diagnosis order**: (1) readings drift month to month → first check surface contamination (water-film test, Card 34-05) → check whether spot temperature went unrecorded → re-measure at constant temperature; (2) wide five-point range → first check needle-pressure uniformity → check whether points landed on chip edges or defects → check thickness uniformity; (3) converted value disagrees with the assay → first check the table version → check whether the shape correction was applied → re-plot a self-check point.
8. **L1 / L2 / L3 evidence**: L1 = five-point readings and range recorded for one wafer; L2 = five-point range <10% on consecutive wafers + table version on file; L3 = wafers issued graded by resistivity, measurement records cross-checkable against ingot and furnace numbers, a second person reproducing from this card. **Boundary: direct detection of impurities below the ppm level is not built here — the four-point probe yields only an indirect electrical quantity, which lies outside the capability line** (Section 34.7, this chapter's Class-C items).

[Card 34-05 Water-Film Cleanliness Test] (eight fields)

1. **Input materials**: distilled water (Chapter 26, no suspended matter); the wafer or tool surface to be checked (after cleaning, wet or already dry, but always compared in the same state); one known-clean reference wafer (retained from the same batch).
2. **Tools required**: dedicated clean dropper or glass rod (not oil-contaminated); oblique lamp (dark field or side light); 3–5× magnifier; absorbent paper / dry cloth (to blot edges only, never to wipe the face).
3. **Operating sequence and control points**: ① work in the clean enclosure or a draught-free spot → ② drop one drop of distilled water at the wafer center (or rinse the whole wafer and stand it upright) → ③ observe the spread pattern under side light → ④ compare with the reference wafer by the same method → ⑤ record and judge → ⑥ anything judged oily goes back through the cleaning chain and is re-checked. Control points: **the water and the vessel must themselves be clean** (oil in the drop misjudges the whole wafer), no draught and no dust, and the comparison must be same-batch, same-method.
4. **Empirical parameters and calibration**: this test has **no numerical threshold** — the criterion is morphological: a clean hydrophilic surface spreads the water into an even film, while oily spots make droplets bead up (Section 34.7); the baseline is established on site with the "known-clean wafer" and is an **empirical value that must be calibrated to local water and surface condition**. The same principle is reused downstream as the etch-through criterion (SiO₂ wets evenly; where etching breaks through to silicon the drop beads, Section 35.B.9), so this card is the starting point of a line-wide criterion.
5. **Observations to record**: wafer/tool number, water temperature and water batch, description of the spread pattern (even film / local contraction / fully beaded), reference-wafer number, verdict and disposition, re-check result.
6. **Pass / rework / scrap criteria**: pass = the water spreads into an even film with no contracting spots; rework = local contraction → back through the cleaning chain, then re-check; scrap = still fully beaded on re-check (organic film or wax residue has penetrated, or the surface is damaged) — the wafer is downgraded to a witness / test wafer.
7. **Common failures and diagnosis order**: (1) the whole wafer beads although cleaning was not skipped → first check whether the water or the dropper carries oil → check whether the last cleaning stage wiped the face with cloth → check whether de-waxing was complete; (2) the film spreads evenly yet pinholes or edge bleed appear downstream → this test cannot see particles or metal ions (capability boundary); check settling dust and the acid-pickle record instead; (3) results vary from run to run → first check draught and dust at the station (move to a draught-free spot) → check whether the reference wafer is itself contaminated.
8. **L1 / L2 / L3 evidence**: L1 = one test record + the retained reference wafer; L2 = every wafer enters the five inspections with a verdict recorded (Section 35.A.7) and a closed re-check loop; L3 = the reference wafer is renewed on schedule, verdicts are cross-checked between operators, and the criterion is written into the wafer travel card. **Boundary: this card detects oil and organic film only; particles, metal ions and ppm-level impurities are invisible to it — those are monitored indirectly by electrical methods, outside the capability line** (Section 34.7, this chapter's Class-C items).

### 34.8 From Material Preparation to Semiconductor Processing

**The "materials-readiness checklist" this chapter delivers** (release conditions for Chapter 35 to start work):

| Item | Criterion | Level |
|---|---|---|
| Wafers | Single crystal, mirror finish, parallelism on file | L2 start |
| Purity monitoring | The three-piece set: resistivity curve + temperature coefficient + water-film test | L2 start |
| Dopant stock | boric acid, phosphate types (Chapter 23 feedstock library) | Ready |
| HF/oxidation/diffusion furnace temperatures | Chapter 12, 26 capabilities + temperature control at spec | Ready |

**Honest boundary (this chapter's conclusion)**: this route stably reaches L2 — "high-purity polysilicon + small single crystals + qualified wafers"; beyond-6N electronic grade, large diameters, and low-dislocation industrial standards (L3) require long iteration of equipment and metrology — **Chapter 35's first integrated circuit is built on this honest starting point**: small size, crude design, germanium and silicon tried in parallel.

---

### 34.9 Metallurgical-Grade Silicon Capacity Account: How to Compute One Furnace End to End

Section 34.2 only covered "how to smelt"; this section covers "what one furnace run costs, how much it yields, and what to do when the power cuts out" — without this account, the Part 10 judgment "can we enter semiconductors" has no numbers to consult.

**Reaction and charge ratio**: SiO₂ + 2C → Si + 2CO↑. Molar masses: SiO₂ 60.1, C 12.0, Si 28.1, which yields two constants: per kilogram of quartz, theoretical carbon requirement 0.40 kg and theoretical silicon output 0.467 kg.

**One-furnace worked example (registered baseline furnace, 100 kg charge)**:

| Item | Number | Notes |
|---|---|---|
| Quartz charge | 100 kg | weighed dry after hand-picking + acid pickling |
| Theoretical carbon need | 40 kg | 0.40 × 100 |
| Actual charcoal/coke charged | 50 kg | carbon ratio 1.25 (25% excess: covers CO escape, charge burn-off, and moisture; in the first month correct this factor with "crude-silicon assay + slag carbon content") |
| Theoretical silicon yield | 46.7 kg | 0.467 × 100 |
| Actual crude silicon recovered | 32–40 kg (empirical) | Loss items: SiO volatilization escape, material hanging on slag and crucible walls, crushing and screening losses; measure this line's actual recovery rate in the first month and transcribe it into the ledger |
| Power consumption | 500–800 kWh (budget) | Industrial large furnaces: 11–13 kWh/kg; small crucible furnaces carry a larger heat-loss share; budget 15–20 kWh/kg in the first month and correct with measured data |

Sanity-range check: 500–800 kWh ≈ 6–8 h of full load on a hundred-kilowatt grid, i.e. "one furnace = one full day's full-load power window" — carbothermal reduction must be scheduled into a night-shift block of continuous supply; fragmented daytime power cannot strike even one arc.

**Electrode and fuel-charcoal account**: electrode consumption is registered as the "per-furnace weigh-in/weigh-out difference" (industrial reference order of magnitude 0.08–0.12 kg electrode per kg silicon; build this line's own factor in the first month); the 50 kg of charcoal per furnace is checked against the Chapter 6, 23 fuel-charcoal production capacity — if one kiln firing yields 300 kg of charcoal, one kiln load covers only 6 furnace runs; charcoal is not something you can burn whenever you please.

**Monthly capacity extrapolation and scheduling logic**: 3 furnace runs per week × 4 weeks = 400–480 kg of crude silicon per month. But the downstream chlorination line (Section 34.10) can process only tens of kilograms per month — the bottleneck is downstream, not upstream. Scheduling conclusion: the metallurgical line needs only 4–6 furnace runs per month; the remaining power windows go back to other loads; **the semiconductor line consumes the capacity of the chain's narrowest link, not the capacity of its longest link**.

**Impact of power failure on the line** (degraded operation and protected-power tiers: see Chapter 40):

- Arc furnace loses power mid-run: the melt begins to freeze and crust within 10–20 min; after power returns the charge "bridges" and the arc cannot strike in; the usual outcome is a whole furnace scrapped plus a cracked crucible. Contingency: stop charging the moment power fails; after power returns, re-strike the arc at low power; if it will not strike within 30 min, shut down and clear the furnace — do not force it.
- Chlorination-reduction line loses power: heating stops, and silicon tetrachloride condenses and blocks the piping; the chlorine generator keeps releasing residual chlorine while the absorption-tower pump has stopped — **the absorption-tower circulation pump must be connected to the highest tier of the protected power supply**.
- The semiconductor line as a whole is entered on Chapter 40's "tier-1 protected load" list (same tier as medical cold storage); an outage over 2 h triggers the chlorination line's "full-stop and seal-up" procedure: close valves, drain everything, seal with dry nitrogen; after power returns, warm the piping segment by segment per the restart procedure.

### 34.10 Chlorination-Line Material Closed Loop: Three Accounts — Chlorine, Silicon Tetrachloride, Zinc

The chlorination line is the chapter's largest consumer of chemicals; without a closed loop it becomes "the more you produce, the poorer you get." This section establishes three accounts, all entered in this chapter's materials ledger.

**Chlorine recovery and regeneration**:

- Reduction tail gas and distillation non-condensables all go through two-stage alkaline absorption (Chapter 26): the first stage's concentrated lye catches the bulk, the second stage's dilute solution catches the remainder; the outlet is checked with wet starch–potassium-iodide paper — no blueing within 30 s means fully absorbed; hang the paper at the discharge outlet, check once per batch, and record after each check.
- The absorption product is a hypochlorite solution (sodium hypochlorite / bleach liquor), **do not pour it away**: decant into dark ceramic jars, keep sealed from light, register it into the warehouse, and return it to the Chapter 23 feedstock library as an oxidizer (for water treatment and bleaching rinses), crediting the chlorine account by conversion.
- Chlorine balance account: register per batch "chlorine charged in kg / tail-gas recovery converted to kg / net consumption in kg." Net consumption persistently more than 30% above the theoretical value = a system leak or failed absorption; stop the line and hunt leaks point by point with ammonia solution test paper (Chapter 26 method).

**Silicon-tetrachloride storage and handling red lines**:

- Properties dictate discipline: boiling point about 58 ℃; violent hydrolysis on contact with water, SiCl₄ + 2H₂O → SiO₂ (hydrated) + 4HCl↑ — the white fog is hydrochloric acid mist, and cloudiness is silica gel.
- Storage: ground-glass bottles or quartz ampoules, ground joints sealed with dry paraffin; bottles stand upright in a bed of dry sand, and the sand tray sits inside a lye tray (double containment); storeroom temperature <25 ℃, far from water sources, the alkali store, and heat sources. The quantity stored at a single point must not exceed twice a batch's usage; draw more only when that is used up.
- Handling: a dry, ventilated spot, dry gloves and dry tools; before opening, check the bottle mouth for white fog or pooled liquid; dispense by dry inert-gas pressure or siphon, and never point the bottle mouth at anyone.
- Spill response: cover with dry sand and absorb; the sand goes into a lye bucket for neutralization; **hosing with water is strictly forbidden** — washing with water creates an acid-fog accident and a silica-gel slip accident on the spot simultaneously.
- Contamination diagnosis: for fractions with cloudy liquid or excessive residue after evaporation, let stand to see silica-gel layering and test for chloride ion with silver nitrate solution (Chapter 26); fractions confirmed hydrolysis-contaminated are scrapped and re-distilled — never used "well enough."

**Zinc chloride recovery loop from the zinc-reduction by-product**:

- The materials account of SiCl₄ + 2Zn → Si + 2ZnCl₂: per 1 kg of silicon produced, 4.65 kg of zinc consumed (2×65.4/28.1) and 9.7 kg of zinc chloride produced (2×136.3/28.1). Order-of-magnitude check: **zinc is the chlorination line's largest material flow** — without recovery, monthly consumption runs to the hundred-kilogram scale, which the Chapter 17 zinc-ore smelting capacity simply cannot carry; the closed loop is a question of "can it continue," not of "whether to save."
- Recovery process (**activated after the zinc line is unlocked**): zinc chloride in the condensation zone is periodically melted out and canned → hydrolyzed to zinc oxide, then carbon-reduced to regenerate zinc granules → recharged into the reduction furnace, weighed and registered before charging.
- Recovery-rate criterion: back-calculate the recovery rate from the books — "zinc charged − zinc carried out in product − zinc remaining in waste residue"; first-quarter target ≥85%; below 80%, stop the line and hunt for leaks (common ones: material escaping the condensation zone, zinc not washed from residue, scale at can bottoms not cleaned).
- By-product disposition order: re-smelting regeneration is first priority; surplus zinc chloride may be registered for soldering flux and wood preservation (Chapter 23), but "re-smelting first" remains the discipline.

---

### 34.11 Pulling-Furnace Thermal Field and Power Control

Section 34.4 gave the operating steps for Czochralski pulling; this section gives "how to arrange the furnace, how to adjust power, what to do when power fails" — nine times out of ten, pulling fails because there is no stable feedback rule between the thermal field and the operator's hand.

**Thermal field layout (three layers, inside out)**:

1. Quartz crucible (holds the charge), seated on a graphite support; the crucible rim level with, or 10–20 mm below, the top edge of the heater — too high and the melt surface sits far from the heater, wasting power; too low and the meniscus is invisible through the viewing port; set this height with crucible shim plates before the first charge and copy it into the furnace archive.
2. A graphite heater (barrel-shaped; Chapter 12 furnace work) surrounds the crucible; the first version can run on a single power section; the advanced version switches to independently regulated upper and lower sections (upper controls the melt surface, lower controls the gradient) — registered as an upgrade item.
3. Carbon-felt/graphite heat-retention shield with a 20–30 mm diameter viewing hole in the top cover; 100–150 mm directly above the hole, a double-pane quartz-glass observation window (about 10 mm between panes: the inner pane blocks silicon vapor deposition, the outer pane blocks accidental spatter); the viewing position adds a dark filter — the melt surface is far too bright, and judging diameter with the naked eye both damages the eye and misjudges.

The thermal-field goal in two sentences: small radial temperature difference near the melt surface (the whole face melts together; nothing freezes at the rim); ample axial heat removal at the already-pulled crystal end (the crystal slightly colder than the melt surface, aiding impurity expulsion and diameter stability). In an era without quantitative measurement, use "no frozen ring at the rim and an intact meniscus on the melt surface" as the visual criterion.

**Power–melt-surface calibration curve (this furnace's first curve)**:

- Principle: melt-surface diameter is a function of heating power, lagging about 1–3 min (thermal inertia). More power and the diameter grows; less power and it shrinks; this relation differs from run to run (charge size and crucible age both matter), so **it must be self-calibrated for every run**.
- Calibration method: after melting completes, fix the pull rate and rotation speed; starting from the baseline power at "diameter stable," adjust power/voltage by ±3% each step, wait 5 min, read the diameter once; repeat for 5–6 points to obtain this run's "power deviation — diameter change" curve, copied into the furnace archive.
- Operating logic: read the diameter once a minute → deviation beyond ±1 mm from target → look up the curve for the corresponding adjustment → wait 1–3 min and read again. **A single adjustment must not exceed ±5%** — one big step is enough to snap the thin neck.
- The thermocouple reads the crucible bottom or heater temperature, not the melt-surface temperature; **the diameter reading is the proxy variable for melt-surface state**. "Watch the diameter, adjust the power" is this run's first operating discipline; ◎ practice method for visual meniscus judgment: run 3 practice furnaces on scrap ingots — watch only, do not pull — comparing per-minute estimated diameters against measured ones; only when the estimation error converges to ±0.5 mm may a real ingot be pulled; misjudgment compensation: measure the diameter of the already-pulled section with calipers in place of eyeballing.

**Power-failure protection**:

- The instant power fails: stop pulling, stop rotation; seed crystal and growing ingot stay in place — **jerking them up out of the melt is strictly forbidden** (a red-hot crystal quenched abruptly shatters; flying fragments injure people and wreck the crucible).
- Short outage (power back within 10 min): reheat at low power, relocate the working point from the calibration curve; pulling may resume.
- Long outage: let the melt freeze naturally; close the viewing port, keep the furnace chamber sealed, and let the whole furnace cool slowly; **the shield may be opened only after the thermocouple has dropped below 200 ℃** — cold-air shock from opening the shield while hot is the number-one cause of quartz-crucible explosion and ingot cracking (crucible-explosion protection: see this chapter's Safety Boundary).
- Atmosphere discipline: inert atmosphere throughout pulling — evacuate, then backfill with argon (reusing the Chapter 33 vacuum ladder); **at molten-silicon temperatures nitrogen forms a silicon nitride skin**; it is permitted only in the cooling stage after the ingot has fully frozen, and must be registered in the furnace archive; before re-melting after power returns, re-evacuate and switch back to argon.
- Every power-failure event (time, duration, response, losses) is entered into the furnace archive — this archive is both raw material for Chapter 40's degraded-operation contingency plans and the original account for "crystals-lost-per-outage" statistics.

### 34.12 Wafering Tooling in Detail: Multi-Wire Saw, Mounting, and First-Article Inspection

The "multiple wires wound in parallel" that Section 34.6 mentions in one line is in fact a complete tooling system; sawing an ingot into scrap is a furnace of electricity burned for nothing. This section lifts slicing from "gambling on luck" to "a process with first-article inspection."

**Multi-wire saw frame and wire-spacing spacers**:

- Structure: two wire-winding rolls (spacing = ingot length + 100 mm winding allowance); the roll faces are divided by spacers into wire channels, and steel wire is wound back and forth, one strand at a time, into a wire array; the frame material is unrestricted (wood or steel both work) — the no-iron discipline governs surfaces that touch silicon material, and what touches inside the kerf is steel wire, abrasive slurry, and water.
- Wire: Chapter 31 drawn steel wire, 0.3 mm-class diameter, sorted by a wire gauge; only one class of wire may be used on a given saw (mixed diameters = chaotic wafer thickness).
- Spacers: **spacer thickness = target wafer thickness + measured kerf width**. Kerf width = wire diameter + abrasive grit size + wobble; it cannot be computed on paper, so calibrate on the first cut: saw through a scrap ingot section, measure kerf width and wafer thickness with a micrometer, and derive this saw's factor. Example: target thickness 0.5 mm, measured kerf 0.6 mm → spacer 1.1 mm (spacers are stored sorted in ±0.05 mm classes; spacers worn by more than 0.05 mm are downgraded or retired).
- Tension counterweight: single-wire tension is applied by an end counterweight wheel; start at 2–5 kg and calibrate three settings — cut three sections of the same ingot at 2 / 3.5 / 5 kg respectively and pick the setting by comparing wafer-thickness deviation and wire-break count. Too loose and the kerf snakes; too tight and wires break. Tension-uniformity criterion ◎: pluck the wires unloaded and listen — the whole array at one pitch is uniform; misjudgment compensation: press the midpoint of a wire with a fixed weight and measure displacement; adjacent wires' displacement difference <10%.

**Mounting and orientation alignment**:

- Bond: rosin–beeswax 1:1 mixed-melt wax (or the Chapter 24 optical-cement recipe); hot-mounting temperature = wax softening point + 20–30 ℃, heated with a water bath or hot plate; **direct flame on the ingot is strictly forbidden** (thermal shock cracks the ingot; the loss is counted as a whole ingot).
- Orientation alignment: the ingot's reference flat (Section 34.5) is seated against the tooling plate's locating stop, at the prescribed angle to the wire's reciprocating direction (the first version cuts square at 90°, registered in the archive); ingot sections on one plate are mounted facing the same way, so later dicing along the cleavage plane saws cleanly.
- Post-mounting check: tap the ingot section lightly with a wooden handle and listen — a solid note means bonded; a hollow note = not bonded; reheat and re-press; after bonding, let it stand until the wax is fully cold and set before sawing (sawing while hot = the ingot section shifts mid-cut).

**First-article inspection after slicing**:

1. First wafer, mandatory inspection: five-point micrometer thickness (center + four corners), range <0.05 mm means thickness acceptable; check cracks against light; inspect edges for chipping with a magnifier; number entered into the thickness archive.
2. In-process sampling: 1 wafer in every 10 re-measured; 2 consecutive out-of-tolerance wafers stop the machine; troubleshooting order: slurry concentration → single-wire tension → spacer displacement.
3. Three-way disposition: thickness out of tolerance but within allowance → rescued by the grinding step; edge chipping over 1 mm or a through-going crack → scrapped and returned to the furnace; systematic whole-batch thickness deviation → stop the machine and recalibrate spacers and tension; already-cut pieces graded and registered by measured thickness.

[Card 34-07 Multi-Wire Saw Wafering] (eight fields)

1. **Input materials**: single-crystal ingot (reference flat on file, mounting face ground flat); steel wire of one 0.3 mm class (sorted by wire gauge — **only one class on a given saw**; mixed diameters mean chaotic wafer thickness); abrasive slurry (carborundum + water, ratio set so the slurry does not dry out, slurry batch number registered); rosin–beeswax 1:1 mixed-melt wax (or the Chapter 24 optical-cement recipe).
2. **Tools required**: wire-winding frame (roll spacing = ingot length + 100 mm winding allowance) with spacers stocked in ±0.05 mm classes; end tension counterweight wheel (2–5 kg); wire gauge (Chapter 31); micrometer (Chapter 22, five-point thickness); hot plate or water bath for mounting (**no direct flame**); tooling-plate locating stop (orientation); wooden handle (to tap the ingot section and listen); first-article record and thickness archive sheet.
3. **Operating sequence and control points**: ① calibrate on the first cut — saw a scrap ingot section, measure kerf width and wafer thickness with the micrometer and derive this saw's factor: **spacer thickness = target wafer thickness + measured kerf width** (example: 0.5 mm wafer + 0.6 mm kerf = 1.1 mm spacer) → ② wind the wires — one class of wire wound back and forth into the array; pluck the unloaded array and listen, one pitch across the whole row means uniform tension → ③ mount — hot-mounting temperature = wax softening point + 20–30 ℃, water bath or hot plate; a solid note when the ingot is tapped with a wooden handle means bonded, a hollow note means reheat and re-press; let it stand until the wax is fully cold and set → ④ orient — reference flat against the stop, the first version cutting square at 90°, registered → ⑤ saw — **constant feed** logged pass by pass, **the slurry must never dry out** (top it up at once; dry cutting burns the wire), **stop at once on a wire break** (a broken end caught in the kerf destroys the whole array) → ⑥ first-article inspection — five-point thickness on the first wafer (centre + four corners) with range <0.05 mm, cracks checked against the light, chipping under a magnifier → ⑦ re-measure 1 wafer in every 10; two consecutive out-of-tolerance wafers stop the machine. Control points: spacer thickness comes only from the first-cut calibration, **never from paper arithmetic**; tension is set by three trial settings, and the middle one is where to start.
4. **Empirical parameters and calibration**: wire diameter 0.3 mm class; **spacer thickness = target wafer thickness + measured kerf width** (kerf = wire diameter + abrasive grit + wobble, which cannot be computed on paper, so it is calibrated on the first cut; spacers stored in ±0.05 mm classes, those worn beyond 0.05 mm downgraded or retired); single-wire tension **2–5 kg, three settings** tried by cutting three sections of the same ingot at 2 / 3.5 / 5 kg and choosing by wafer-thickness deviation and wire-break count; first-article **five-point range <0.05 mm, edge chipping <1 mm**; tension-uniformity criterion ◎ = one pitch across the array when plucked unloaded, misjudgment compensation = press a wire midpoint with a fixed weight and measure displacement, adjacent wires differing <10%. Calibration = first-cut scrap-ingot calibration + three-setting tension trial, both entered in the wafering archive. All of these are **empirical values that must be calibrated to local conditions**.
5. **Observations to record**: kerf sound (a screech = slurry drying, top up at once); array swing amplitude; slurry colour (going black = abrasive dulled, change the whole tub) and slurry batch number; feed per reciprocation; number and position of wire breaks; first wafer's five-point thickness and range; chip location and size (**concentrated on one side = mounting problem, even all round = feed problem**); spacer class and tension setting.
6. **Pass / rework / scrap criteria**: pass = first-article five-point range <0.05 mm, chipping <1 mm, no cracks against the light, number entered in the thickness archive; rework = thickness out of tolerance but still within the grinding allowance → rescued at the grinding step (Card 34-03); chipping <1 mm outside the mirror region → downgraded to a test wafer; scrap = chipping over 1 mm or a through-going crack (returned to the furnace); a systematic whole-batch thickness offset → stop the machine and recalibrate spacers and tension, then grade the already-cut pieces by measured thickness.
7. **Common failures and troubleshooting order** (by frequency): (1) uneven thickness → first check whether single-wire tension is uniform (pluck and listen), then slurry concentration wobble (top up or change the tub); (2) the kerf snakes → tension too loose (step up a setting); (3) edge chipping → first whether the feed is too fast, then whether the abrasive is too coarse, finally whether the mounting really bonded (tap and listen); (4) wire breaks → tension too tight or the wire is worn (change wire, drop a setting); (5) kerf screeching and slurry drying → topping-up missed (dry cutting burns the wire — stop the machine at once).
8. **L1 / L2 / L3 evidence**: L1 = first-article record (five-point thickness, chipping and cracks all three on file); L2 = a whole batch's thickness archive (wafer numbers traceable to the ingot number, spacer and tension settings on file); L3 = a batch–wire-class–slurry-batch cross-reference table complete, and a second person sawing one ingot from this card alone passing first-article inspection.

---

### 34.13 Doping Master Alloy: Turning "Weighing Micrograms" into "Weighing Milligrams"

What Chapter 35 needs as dopants is not raw materials (boric acid and phosphates are raw materials) but **silicon-based master alloys of known concentration** — charging microgram-scale pure dopant directly into the melt cannot be weighed on a field balance, nor dissolved in a short melt time. The master alloy raises the weighing-precision requirement from the microgram level to milligrams and above; it is the only realistic doping method for a small site.

**Master alloy preparation**:

- Concentration design: the master alloy's target concentration is set at the 0.1% mass-fraction level (10⁻³) — higher, and the per-run dose falls back under a milligram and cannot be weighed; lower, and the master alloy's own homogeneity is hard to guarantee. The first version makes two lines: boron (p-type) and phosphorus (n-type).
- Materials: high-purity silicon fragments (qualified material from the middle sections of zone-refined rods, crushed to 5–10 mm chunks); boron source: boric acid (Chapter 23), first dehydrated and pre-fired into boric oxide lumps, then crushed (**register: this route introduces oxygen and hydrogen; the actual concentration is set by assay, not by charge calculation**); phosphorus source: red phosphorus granules made from phosphates under a reducing atmosphere (Chapter 26 reduction conditions); when the phosphorus source is short, the master alloy makes only the boron line first, with n-type made up later by Chapter 35 vapor-phase diffusion — registered honestly.
- Melting and blending: charge the quartz crucible, evacuate, backfill with argon (Chapter 33 ladder); heat to 1414 ℃ until the melt clears (a mirror-like reflection on the liquid surface is the melt-cleared criterion); stir with a graphite rod or rock the furnace by hand for 5–10 min, hold 10 min more to promote homogenization, then cast into a preheated graphite mold as small ingots under 50 g, engraving the batch number on the ingot face.
- Cooling: mold cooling suffices; once fully cooled, bag by batch and enter into this chapter's ledger.

**Assay: back-calculating concentration with the four-point probe**:

- Cut a 2 mm-thick sample wafer from the ingot's middle, measure resistivity with the four-point probe (Section 34.7), and look up the self-built "resistivity — impurity concentration" table to back out the concentration. **Self-building the lookup table**: start from the Chapter 33 rectification comparison data and theoretical curves; each time a batch is blended, plot one self-check point using the "known charged amount," converging step by step on this line's true curve; the table lives in the archive — converting from memory is forbidden.
- Double criterion: a p-type master alloy's temperature coefficient must be negative — an anomalous temperature coefficient signals metal contamination (Section 34.7); that batch is downgraded or scrapped.
- Segregation correction: boron's segregation coefficient is near 1, so the head-to-tail concentration difference in the ingot is small and the whole ingot is usable; **phosphorus's segregation coefficient is about 0.35 — rich at the head, lean at the tail** — phosphorus master alloy must have resistivity measured section by section along the ingot, with concentration labeled by section; draw material by section; averaging over the whole ingot is not allowed.

**Dosing-ratio worked example (100 g charge, p-type, target resistivity about 1 Ω·cm)**:

1. Target concentration: from the table, 1 Ω·cm p-type corresponds to an acceptor concentration of about 1.4×10¹⁶ cm⁻³ (approximate; updated with table revisions);
2. Melt volume: 100 g ÷ 2.33 g/cm³ ≈ 42.9 cm³;
3. Boron atoms needed: 1.4×10¹⁶ × 38.9 ≈ 6.0×10¹⁷ atoms = 1.0×10⁻⁶ mol = 1.08×10⁻⁵ g ≈ 11 μg of pure boron;
4. Master alloy at 0.1% boron (1 mg per gram) → master alloy needed: 11 μg ÷ 0.001 ≈ 11 mg;
5. Order-of-magnitude check: 11 mg sits right at the lower limit of the field balance (10 mg-class resolution). Two engineering fixes: ① blend more at once — scale the charge up to 500 g, raising master alloy usage to 55 mg, inside the balance's reliable zone; ② a diluted grade — further dilute the 0.1% master alloy with pure silicon into a 0.01% standby grade, raising usage to the hundred-milligram scale. **Register both, and choose per the current batch's charge size**.
6. Burn-off correction: melting and casting incur losses; start the first month at +15% pre-charge, and back-derive the correction factor batch by batch from the "target concentration − assayed concentration" difference, transcribed into the ledger — the next crew may not work from memory.

[Card 34-06 Doping Master Alloy Preparation] (eight fields)

1. **Input materials**: high-purity silicon fragments (qualified material from the middle of a zone-refined rod, crushed to 5–10 mm chunks); boron source = boric acid (Chapter 23), first dehydrated and pre-fired into boric oxide lumps, then crushed; phosphorus source = red phosphorus granules made from phosphates under a reducing atmosphere (Chapter 26); quartz crucible; preheated graphite mold; argon (Chapter 33 vacuum ladder). Defective materials forbidden: deliquesced boric acid, silicon with an oxidized yellow skin or metallic bright spots.
2. **Tools required**: vacuum-backfill furnace (Chapter 33); thermocouple (Chapter 25, 1414 ℃ class); balance (10 mg resolution); four-point probe (Card 34-04); slicing and flattening tooling (to take a 2 mm-thick sample slice from the middle); graphite stirring rod; batch-number engraving tool; batch-number–concentration ledger and lookup table.
3. **Operating sequence and control points**: ① pre-fire the boric acid to dehydrate it into lumps and crush (**register: this route introduces oxygen and hydrogen; the actual concentration is set by assay, not by the charge calculation**) → ② charge, evacuate, backfill argon → ③ heat to 1414 ℃ until the melt clears (mirror-like reflection is the melt-cleared criterion) → ④ stir with a graphite rod or rock the furnace 5–10 min → ⑤ hold 10 min to homogenize → ⑥ cast into the preheated graphite mold as an ingot under 50 g, engraving the batch number on its face → ⑦ after cooling, cut a 2 mm sample slice from the middle → ⑧ measure resistivity with the four-point probe and back out the concentration from the table → ⑨ for the phosphorus line, measure section by section along the ingot and label the concentration per section. Control points: melt-cleared means mirror reflection (casting before the melt clears = an inhomogeneous ingot); casting too cold leaves shrinkage cavities.
4. **Empirical parameters and calibration**: master alloy concentration at the 0.1% mass-fraction level (higher, and the per-run dose falls back under a milligram and cannot be weighed; lower, and its own homogeneity is hard to hold); melting at 1414 ℃, rocking 5–10 min + 10 min hold; pre-charge burn-off starting at +15%, with the correction factor back-derived batch by batch from the "target concentration − assayed concentration" difference (**empirical, must be calibrated**); the concentration table is self-built (method in Card 34-04) and converting from memory is forbidden. Dosing worked example: a 100 g charge targeting about 1 Ω·cm p-type needs about 11 mg of master alloy (right at the field balance's lower limit) — two engineering fixes: scale the charge to 500 g (dose rises to 55 mg) or dilute the 0.1% alloy into a 0.01% standby grade (dose rises to the hundred-milligram scale); register both and choose per the batch's charge.
5. **Observations to record**: batch number, blend ratio and charge weights, melt-cleared time and rocking/hold duration, ingot weight and face mottling (mottling = not homogeneous), assayed resistivity and back-calculated concentration, sign of the temperature coefficient, segregation section table for the phosphorus line, burn-off correction factor, destination and grams drawn.
6. **Pass / rework / scrap criteria**: pass = assayed concentration on file and a normal temperature coefficient (p-type must be negative); rework = inhomogeneous ingot (re-homogenize once in the furnace and re-assay), concentration off (correct the factor for the next batch); scrap = anomalous temperature coefficient (metal contamination — check the no-iron discipline), mixed batches (adjacent batches differing by >20% not stored apart — the whole lot is demoted to test material).
7. **Common failures and diagnosis order**: (1) concentration off → first check the burn-off estimate (review the correction factor) → check charge weighing and whether the boric acid was fully dehydrated → correct the next batch; (2) inhomogeneous ingot (face mottling) → first check the rocking time → check whether the melt fully cleared → check casting temperature; (3) anomalous temperature coefficient → first check whether iron tools touched the vessels → check the silicon batch → downgrade or scrap that batch; (4) large head-to-tail difference in phosphorus ingots → inevitable segregation (coefficient about 0.35); the remedy is section-by-section labeling and drawing by section, not rework; (5) batch-to-batch drift → check balance calibration and whether two batches' burn-off factors were mixed.
8. **L1 / L2 / L3 evidence**: L1 = one batch's assay sheet with the concentration on file; L2 = a continuous batch-number–concentration ledger, a complete phosphorus section table, dual-signature material-draw records; L3 = table and burn-off factor iterated batch by batch and auditable, Chapter 35 drawing material by "ingot weight + target resistivity → lookup table → grams" in a closed loop, a second person making a batch from this card. **Boundary: the master alloy only solves "can it be weighed," not purity — the alloy's own metal contamination is still held in check by the no-iron discipline and the temperature-coefficient criterion; electronic grade beyond 6N is not built here, outside the capability line.**

**Batch-variance register and material-draw system**:

- Every master alloy batch is registered with: batch number, blend ratio, assayed concentration, segregation section table (mandatory for the phosphorus line), destination and usage. If two adjacent batches' assayed concentrations differ by more than 20% → store the two batches separately, each labeled; **mixing batches is strictly forbidden** — mixed batches mean unknown concentration, and the whole lot is demoted to test material.
- Material-draw system: Chapter 35 draws material by "ingot weight + target resistivity → look up the calculation table → grams to draw," with dual-signature verification; the calculation table and the batch-number ledger are kept in the same volume, as part of this chapter's production-line archive.

---

## Parameter Master Table

| Parameter | Value | Class |
|---|---|---|
| Silicon three grades | Metallurgical 98–99% / poly 5N / single crystal 5–6N + integrity | Grading |
| Molten-zone speed | 1–3 cm/h starting; the curve decides the optimum | Empirical |
| Purification passes | 3–10 passes (endpoint: the curve no longer rises) | Empirical |
| Crystal-pulling rate | 0.5–2 cm/h (copied from the diameter-stable section) | Empirical |
| Silicon tetrachloride boiling point | ≈58 ℃ (boiling-range control point) | Physical |
| Silicon melting point | ≈1414 ℃ | Physical |
| Four-point-probe repeatability | Five measurements on one wafer, range <10% | L2 criterion |
| Wafer acceptance | Mirror finish + no scratch scattering in dark field + thickness/parallelism archive | Criterion |
| No-iron discipline | Quartz/ceramic/graphite vessels, throughout | Red line |
| Carbon charge ratio | Theoretical carbon ×1.25 (first-month correction by slag carbon content) | Empirical |
| Metallurgical silicon power budget | 15–20 kWh/kg (first-month measured correction) | Empirical |
| Zinc loop account | 4.65 kg zinc consumed and 9.7 kg ZnCl₂ produced per kg silicon; recovery ≥85% | Ledger |
| Power trim amplitude | ≤±3% per step; thermal lag 1–3 min (curve calibrated per furnace run) | Empirical |
| Shield-opening temperature | Open the shield only below 200 ℃ on the thermocouple | Red line |
| Spacer thickness | Wafer thickness + measured kerf width (first-cut calibration; sorted in ±0.05 mm classes) | Calibration |
| Single-wire tension | 2–5 kg, three settings fixed by test cuts | Empirical |
| Wafering first-article check | Five-point thickness range <0.05 mm; edge chipping <1 mm | L2 criterion |
| Master alloy concentration | 0.1% mass-fraction level (four-point-probe back-calculation assay) | Calibration |
| Master alloy pre-charge burn-off | +15% starting point, corrected batch by batch | Empirical |
| Batch-variance tolerance | Adjacent batches with assayed concentration difference >20%: mixing forbidden | Red line |

## Failure Modes and Diagnosis

| Symptom | Candidate causes (by probability) | Verification | Response |
|---|---|---|---|
| Zone-refining curve flat | speed too fast; heat-source fluctuation breaks the band | three-speed comparison | slow down; stabilize the heat source |
| Mid-section resistivity falls instead | vessel contamination (iron!) | check the no-iron discipline execution record | switch to quartz/ceramic vessels and redo |
| Czochralski crystal break | pull-rate/temperature fluctuation; too many seed dislocations | review the furnace archive | lower pull rate; change seed |
| Wafer cracks during slicing | cutting abrasive too coarse / feed too fast | check chip-out on the fracture face | finer abrasive, slower feed |
| Scratches after polishing | abrasive mixed (coarse grains from an earlier stage) | dark-field scattering | store abrasives in graded containers |
| Resistivity drifts month to month | surface contamination / temperature-coefficient interference | water-film test; re-measure at constant temperature | re-clean; record temperature |
| Wide distillation boiling range | column too short / insufficient reflux | boiling-range records | build a taller fractionating column (Chapter 26) |
| Low crude-silicon yield | wrong carbon ratio / furnace temperature too low | review the ratio and power-consumption accounts | adjust the ratio (Chapter 38 ledger) |
| Unstable arc (arc drops, current swings) | electrode feed lags the sinking charge; charge bridging; voltage fluctuation | compare the current log with the feed notebook | feed electrodes with the charge; poke to break bridges; re-strike after current limiting |
| Silicon tetrachloride hydrolysis (white fog at bottle mouth, cloudy liquid) | water carried in by vessels; seal failure; moist air drawn in | let stand to see silica-gel layering; silver nitrate chloride test (Chapter 26) | scrap contaminated fractions and re-distill; dry-purge the whole line (Section 34.10) |
| Crystal break at the collar (thin neck snaps, crystal crown drops) | sudden power rise / sudden pull-rate drop; mechanical vibration; seed dislocations | review the furnace archive's power–pull-rate curve | adjust power slowly (≤±3% per step); add anti-vibration pads to the furnace body; change seed and re-neck |
| Wafer edge chipping | feed too fast; abrasive too coarse; poor bonding | look at the chip-out on the fracture face: concentrated on one side = bonding problem, even all around = feed problem | lower feed, change to finer slurry; reheat and re-bond (Section 34.12 first-article inspection) |

## Process Card Index

[Card 34-01] Zone refining (end of the zone-refining passage in 34.4) | [Card 34-02] Czochralski single-crystal pulling (end of 34.4) | [Card 34-03] Wafer cut-grind-polish, three operations (end of 34.6) | [Card 34-04] Four-point-probe measurement (end of 34.7) | [Card 34-05] Water-film cleanliness test (end of 34.7) | [Card 34-06] Doping master alloy preparation (end of 34.13) | [Card 34-07] Multi-wire saw wafering (end of 34.12)

Cards 34-02 to 34-06 carry all eight fields and can be copied out on a single sheet; 34-01 and 34-07 are still in summary form and await their eight fields.

## Labor, Hours, and Consumption

| Item | Manpower | Hours (empirical) |
|---|---|---|
| One carbothermal-reduction furnace run (incl. acid pickling) | 3 people | 2 days + power account |
| One chlorination–distillation–reduction cycle | 3 people | 3–5 days |
| One zone-refining rod (5 passes) | 2 people, rotating watch | 1–2 days |
| One Czochralski ingot (centimeter scale) | 2 people, rotating watch | half day–1 day |
| Wafer three operations (10 wafers) | 2 people | 2 days |
| One metallurgical-silicon furnace run (100 kg charge) | 3 people | 1 day + a continuous power window |
| Multi-wire sawing one ingot (20–30 wafers) | 2 people | 1 day |
| One master alloy batch (incl. assay) | 2 people | 1–2 days |
| Consumption | electricity, chlorine, acids, abrasives | entered in the Chapter 38 ledger |

***

## A. Existing Tool List (partial)

Quartz identification (Chapters 2, 14); arc furnace and grid (Chapters 12, 32); distillation/chlorination/HF (Chapter 26); temperature-controlled furnaces and thermocouples (Chapters 12, 25); wire drawing and abrasives (Chapters 9, 31); lens polishing (Chapter 24); electrical measurement and spectroscopy (Chapters 30–33).

## B. New Tools Added in This Chapter

Small carbothermal-reduction furnace and the crude-silicon acid-pickling procedure; the silicon chlorination–distillation–reduction purification line; zone-refining apparatus and the along-rod resistivity curve method; Czochralski single-crystal furnace (seed/rotation/pull-rate manual feedback); pulling-furnace power–melt-surface calibration curve and power-failure protection procedure; metallurgical-grade silicon capacity account (carbon ratio/power/electrode/actual-recovery factors); chlorination-line material closed loop (hypochlorite regeneration, SiCl₄ storage-and-handling red lines, zinc loop account); multi-wire saw tooling (spacer classes/tension counterweights) and the wafering first-article inspection system; doping master alloy preparation, four-point-probe back-calculation assay, and the material-draw system; cleavage orientation and the reference-flat datum system; the wafer three operations of multi-wire sawing, two-face grinding, and pitch mirror polishing; simplified four-point-probe measurement with shape-correction table; resistivity temperature-coefficient spot checks; the water-film cleanliness test; ingot quality grading and wafer-numbered archives; the "materials-readiness checklist" release system.

## C. Unresolved Dependencies

- Large-diameter single crystals and low-dislocation standards (equipment and thermal-field design iteration);
- Direct detection of impurities below the ppm level (indirect monitoring by electrical methods is the current plan; registered honestly);
- A clean-environment system (Chapter 35 mitigates with simplified clean handling);
- The silane route (purer but riskier; registered, not implemented).

## Safety Boundary

- Chlorine generation and use: ventilated spot + absorption barrel (lye), two-person operation (Chapter 26 gas procedures);
- Silicon tetrachloride releases heat and acid fog on contact with water — store and handle dry and sealed;
- The full HF red lines (Chapter 26) apply to every step of this chapter;
- Pulling-furnace high temperature and quartz-crucible explosion risk: goggles and isolation shields;
- Arc-furnace electrical operations follow the Chapter 32 high-voltage procedures.

## Acceptance Criteria

- **L1**: carbothermal reduction yields crude silicon, acid-pickled; the chlorination–distillation loop produces pure silicon tetrachloride (evidenced by a narrowing boiling range); one zone-refining run with a visible rise in the along-rod resistivity curve.
- **L2**: Czochralski small single crystal (mirror cleavage face); the wafer three operations produce mirror wafers (dark-field inspection + thickness archive); four-point-probe repeatability at spec (five measurements on one wafer, range < 10%; empirical values need field calibration).
- **L3**: poly–single-crystal–wafer line with stable monthly output entered in the ledger; quartz/ceramic vessel closed loop (no iron contamination); resistivity graded so Chapter 35 draws material by grade.

## Next-Step Dependencies

- Chapter 35: wafers + dopants + HF + furnace temperatures = the four raw materials of integrated circuits ready;
- Chapter 36: this chapter's purity monitoring system extends directly into production-line quality inspection;
- Chapter 25 (loop back): a further upgrade of thermocouple and temperature-control precision serves the diffusion furnaces;
- Part 10: electricity and quartz resources decide whether this environment holds the entry ticket to the semiconductor route.
