# Chapter 27 · Part A Temperature and Pressure Instruments (27.1–27.3)

> This part and Part B share chapter number 27. Part A = the two quantities temperature/pressure; Part B = the two quantities flow/vacuum + the four-quantity calibration chain and calibration system.

# Chapter 27 From Mechanical Instruments to Precision Measurement

## Chapter Objectives

Upgrade the "manual comparison every time" measurement of the previous two chapters into **a standing system of instruments and apparatus**: indicating mechanisms built from springs and levers; **instruments, calibration chains, and process cards for each of the four physical quantities — temperature, pressure, flow, vacuum**; repeatable calibration methods; optical magnification of readings; the strict language of the three error concepts (error, sensitivity, resolution); a calibration-record system; and the decision procedure for "is this instrument good enough." Version 1 crammed temperature, pressure, and flow into a single section with "one segment each," while vacuum got only its name mentioned in the C list — the review comments pointed out that **the four instrument classes differ completely in principle, calibration method, and sensor fabrication, and after splitting the space evenly, none of them could explain clearly how to be accepted**. Version 2 gives each of the four quantities its own section, its own process card, and its own hook into the calibration chain (traced to the Chapter 3/22/25 standards). The instrument industry is the closing act of Part 5 — it turns measurement capability from "a laboratory action" into "workshop routine."

## Capability Boundaries

**What can be done:**

- Three-point calibration of glass (alcohol) thermometers: ice water 0 ℃ / local boiling point / beeswax 63 ℃, two-segment equal-division interpolation, three-point re-check deviation ≤±1 division;
- Thermocouple temperature chain: iron–constantan (iron–copper substitute) sensor + galvanometer reading + a glass thermometer tied to the cold junction for compensation, with a 0–500 ℃ lookup table;
- Bourdon-tube (spring-tube) pressure gauges of the 0–10 atm class, deadweight calibration, indication error ≤2% of range, return difference ≤1 division (empirical value, must be field-calibrated);
- The flow-rate trio: volume–time method (baseline) + open-channel triangular weir (with a self-made water-level–flow lookup table) + Pitot tube (calibrated for this tube's center coefficient); deviation between the weir table and the bucket method ≤5%;
- Three-band vacuum gauge selection: open/closed mercury vacuum gauges covering 760–1 mmHg; below 10⁻¹ mmHg, spot measurements with the McLeod gauge (built in Chapter 33);
- Mechanism and system aspects: spring/lever/sector-gear indicating mechanisms, hairspring backlash removal (return difference < half a division), five-point calibration and lead sealing, calibration cards and period grading.

**Explicitly cannot be done:**

- Glass-liquid thermometers above 110 ℃ (mercury thermometers require vacuum filling and high-temperature glass — far-term); bare-wire thermocouples above 500 ℃ (oxidation loss); continuous electrical temperature measurement above 750 ℃ (noble-metal thermocouples depend on platinum) — for the high-temperature band use the Chapter 12 temperature cones semi-quantitatively;
- Deadweight calibration above 10 atm (the strength ceiling of the weights and the cylinder) — higher pressures are handled in a degraded mode, by "dual-gauge cross-checking + mercury-column comparison";
- Continuous-reading vacuum gauges below 10⁻¹ mmHg (Pirani and ionization gauges are electrical instruments, for after Chapters 30–33);
- Workshop temperature control and vibration isolation (a matter of building and overall industrial level).

**External dependencies (counted on the C list):** standard weights and length standards (Chapters 3, 22); glass thermometer blanks (lampwork, Chapters 14, 25); tin-bronze tubing (Chapter 17); mercury and barometer (Chapter 25); galvanometer (Chapter 30 — the precondition for raising the thermocouple chain to Tier 3); McLeod gauge (Chapter 33 — the precondition for high-vacuum readings).

## Pre-Start Verification (Check Off Item by Item)

| # | Verification item | Criterion | Source |
|---|---|---|---|
| 1 | Tempered steel strip/wire, hardening technique | Elasticity test: deformation under a known force, residual deformation after unloading <5%, recorded on file | Chapter 19 |
| 2 | Threads and gears | Passes an M10×1.5 plug gauge; sector-gear–pinion mesh turns smoothly without binding | Chapters 20, 22 |
| 3 | Knife edges and pivots | Balance knife edge re-ground to pass (re-verified by the Chapter 25 indentation method) | Chapter 25 |
| 4 | Glass thermometer blanks | Capillary free of column breaks over its full length, sensing bulb free of cracks; blanks for three-point calibration must have a top expansion chamber | Chapters 14, 25 |
| 5 | Mercury and barometer | Mercury ≥500 g with a mirror-bright surface and no oil film; same-day barometer reading on file | Chapter 25 |
| 6 | Standard weights and balance | Weight set cross-checked against the Chapter 3 standard; balance sensitivity ≤0.5 g | Chapters 3, 25 |
| 7 | Bronze tubing and tin soldering | Outer diameter 6±0.2 mm, wall thickness 0.8±0.1 mm (three caliper spot checks); solder wets the tube surface into a continuous seam | Chapter 17 |
| 8 | Micrometer | Range across ten measurements ≤0.01 mm, recorded on file | Chapter 22 |
| 9 | Ledger and seals | Calibration card stock, numbering stamp, and lead-seal wax all on hand | Chapter 4 |
| 10 | Timer | Water clock or pendulum counter: 10 consecutive full-bucket timings with range ≤2% | Chapter 3 |

---

### 27.1 Springs, Levers, and Mechanical Indicating Mechanisms

**Springs (the power source of mechanical indication)**:

- Leaf spring: tempered steel strip (Chapter 19), cut to shape for its use; elasticity test: deform under a known force, release, and recover; residual deformation < 5% passes (empirical value, must be field-calibrated);
- Helical spring: steel wire close-wound on a mandrel to shape, then tempered to set (in the blue temper-color band); stiffness calibration: hang weights step by step and record the extension at each step, giving a straight "force–deformation" line — **one stiffness card per spring**;
- Hairspring: thin steel strip coiled into an Archimedean spiral (mandrel + hand coiling), used for the pointer's restoring torque.

**Lever and sector-gear magnification**: two routes from small displacement to large reading: the lever ratio (two 1:10 stages in series give 1:100); the toothed arc–pinion (a sector tooth arc drives a pinion — angular magnification, a large ratio from the small gear). Fabrication key points: knife-edge pivots (Chapter 25 balance knife-edge technique); fitting the tooth arc tooth by tooth (Chapter 20 tooth-correction method); hairspring removal of return play (the gear backlash is preloaded one-sidedly against one flank by the hairspring — **return difference is the instrument's number-one enemy**).

**The indicating-mechanism trio**: pointer (thin duralumin/copper sheet; thin copper when no aluminum is available — low mass, low inertia), dial (equal-division ruling, Chapter 3), zero adjuster (eccentric cam or threaded fine-shift plate).

The mechanisms of this section are the "meter movement" shared by all four instrument classes of this chapter: the protection shells and lookup tables of 27.2, the sector-gear drive of the 27.3 pressure gauge, the counting digit wheels of the 27.4 flowmeter, and the reading scale of the 27.5 vacuum gauge all take this section's springs, levers, and hairsprings as their skeleton.

### 27.2 Temperature Instruments: The Glass Thermometer Calibration Chain and the Thermocouple

#### 27.2.1 Removable Thermometers and Multi-Point Rounds (Version 1 content, retained)

- **Instrumenting temperature**: alcohol thermometers mounted in metal protection shells (Chapter 17); shells and threaded fittings (Chapter 22 standard threads) standardized — the "removable thermometer" becomes the standard interface for furnaces, kettles, and piping; multi-point temperature measurement (furnace top / furnace waist / furnace bottom) and inspection routes (two meter readings per shift).

#### 27.2.2 The Glass Thermometer Calibration Chain: Three Points Fix the Scale, Two Segments Divided Equally

**Why three points**: the capillary bore is uneven along its length; "linear equal division by column length" is only an approximation over short spans. Fix only the ice point and the boiling point, and mid-range deviation can reach several divisions with no way to detect it. Only by fixing three phase-transition points — cutting the range into two segments and dividing each equally — can mid-range deviation be detected and controlled.

**The three fixed points** (phase-transition reproduction, independent of any existing thermometer):

1. **Ice point 0 ℃**: mix crushed ice (≥500 g) with a little clean water — ice not fully melted, water not crusted over; insert the sensing bulb without touching the cup wall or bottom, equilibrate ≥10 min; record the mark only once the reading has held unchanged for 1 min. Self-check: after adding more crushed ice the reading must not move (movement = the ice has melted out or warm water got mixed in).
2. **Local boiling point**: a boiling-water bath, **open, with no lid** (a lid = raised vapor pressure, raised boiling point, reading voided). The local boiling point is not 100 ℃: **t_b = 100 − (760 − P)/27 ℃** (P is the same-day barometer reading, mmHg; empirical formula, error on the ±0.3 ℃ level — verification: repeat on 10 consecutive days of different weather; if the range >0.5 ℃, check the bath water's purity and the bulb's position). Rough altitude rule: the boiling point drops about 1 ℃ per 300 m of elevation.
3. **Beeswax point 63 ℃**: beeswax melts at 62–65 ℃ (nominal 63 ℃). Why beeswax as the third point: the **phase-transition plateau** — melting wax holds its temperature constant for several minutes, giving a wide reading window (rosin softens with no plateau; not used). The melting point drifts between sources; the system is: the workshop fixes one batch of beeswax as the "**reference wax**" (batch number entered in the ledger); the first batch's actual plateau temperature is reverse-measured once with an existing standard glass thermometer and put on file; from then on every calibration uses that batch, and when the batch runs out, the replacement batch must be reverse-measured again.

**Operating sequence**:

1. Scribe the three capillary marks (fine-file cross marks or ink dots): ice-point mark → wax-point mark → boiling-point mark, each mark following the equilibration criteria above;
2. **Uniformity check**: measure the two segment column lengths L₁ (ice-point mark → wax-point mark) and L₂ (wax-point mark → boiling-point mark); the column length per ℃ is L₁/63 and L₂/(t_b−63) respectively. If the two segments' per-℃ column lengths differ by >5% (empirical value, to be revised by statistics from the first batch of 20) → capillary bore unevenness exceeds limits; scrap that tube;
3. **Two-segment equal-division transfer**: divide the 0–63 ℃ segment equally by the per-℃ column length L₁/63 and the 63 ℃–to–boiling-point segment by L₂/(t_b−63), transferring the graduations with the Chapter 3 equal-division ruling method (divider trial divisions); draw a special mark at the segment boundary (63 ℃) to remind that a reading spanning the two segments faces two different scale values;
4. **Re-check and spot check**: re-measure each of the three points once; deviation ≤±1 division; separately compare in the same bath as the standard thermometer in warm water at about 30 ℃; deviation ≤±1.5 divisions (empirical value, must be calibrated).

**Scale interval**: 1 ℃ per division on the 0–63 ℃ segment, 2 ℃ per division above 63 ℃ (blanks with column length to spare: 1 ℃/division throughout — set per blank and written into the calibration card).

**Range ceiling and the expansion chamber**: at atmospheric pressure the alcohol column tops out around 78 ℃; to reach the boiling-point mark (99–100 ℃) the blank must be the **top-expansion-chamber type** (Chapter 14 lampwork: blow a φ6 mm expansion bulb at the top of the capillary, leaving a dry air cushion above the column before sealing), so that at 100 ℃ the column enters the expansion chamber instead of dead-ending. Blanks without an expansion chamber get only the ice point and wax point; above 80 ℃ the thermocouple takes over.

**The temperature-standard hierarchy (pyramid)**: 1 standard thermometer (used only to calibrate other thermometers, never enters the workshop; quarterly three-point re-verification; scrapped on any knock) → working thermometers (monthly one-point spot check against the standard + quarterly boiling-point re-verification). The structure is isomorphic with the Chapter 22 length-standard pyramid.

[Card 27-01 Glass Thermometer Three-Point Calibration] (eight fields)

1. **Input materials**: ungraduated thermometer blank (top-expansion-chamber type, capillary with no column breaks, 1 per run); crushed ice ≥500 g; 50 g of beeswax from the reference-wax batch (batch number in the ledger); 3 L clean water; same-day barometer reading.
2. **Tools required**: boiling-water bath pot ≥2 L (open); wax bath cup seated in a boiling-water double boiler (wax temperature stays under 100 ℃); dividers and scriber (Chapter 3; true the divider points to zero before use); fine flat file; timing water clock; standard thermometer (for reverse-measuring the wax batch and for spot checks).
3. **Operating sequence and control points**: ① ice-water bath, equilibrate ≥10 min, mark the ice point — **control point: record the mark only once the reading has held for 1 min**; ② mark the wax point during the solid–liquid coexistence period of the wax bath (bulb fully immersed, equilibrate ≥5 min) — **control point: the wax must be on its melting plateau; insert the thermometer as soon as it begins to clear overall**; ③ mark the boiling point in the open boiling-water bath (t_b=100−(760−P)/27); ④ measure L₁/L₂ — **control point: per-℃ column lengths of the two segments differing by >5% means scrap**; ⑤ transfer the two segments, each with its own equal division; ⑥ three-point re-check + 30 ℃ same-bath spot check.
4. **Empirical parameters and calibration**: beeswax nominal 63 ℃ (actual value per this batch's reverse measurement); scale 1 ℃/division (2 ℃/division above 63 ℃); re-check tolerance ±1 division; spot-check tolerance ±1.5 divisions (revised after statistics on the first batch of 20); boiling-point empirical-formula coefficient 27 mmHg/℃ (verified by the repeat range over 10 sunny days).
5. **Process observation and recording items**: lengths of the three marks from the bottom of the sensing bulb (mm), L₁, L₂, same-day barometric pressure, wax batch number, re-check deviations, spot-check deviations — entered on the thermometer calibration card (the card travels with the thermometer).
6. **Pass / rework / scrap criteria**: accept = three-point re-check ≤±1 division and spot check ≤±1.5 divisions; rework = graduations transferred to the wrong segment (grind off the graduations and re-rule, the three marks untouched, then repeat step ⑥); scrap = two-segment column-length ratio out of tolerance (uneven tube), cracked sensing bulb, a column break that will not rejoin.
7. **Common failures and troubleshooting order**: symptom "mid-range spot check off by 3 divisions" — first check for graduations transferred to the wrong segment (check whether the 63 ℃ segment-boundary mark lines up) → then check a locally wide bore section (add one temporary bath point above and below the deviating region to localize it) → then check wax batch drift (re-measure the wax plateau temperature with the standard thermometer).
8. **L1 / L2 / L3 evidence**: L1 = one qualified thermometer + calibration card; L2 = the standard thermometer's quarterly re-verification records + a monthly-check ledger for ≥10 working thermometers; L3 = the reference-wax batch ledger + scrap/downgrade records + a calibration-chain traceability chart (who calibrated whom, and when).

#### 27.2.3 The Thermocouple: Wiring a Temperature Difference to a Pointer

**The principle in one sentence**: join two different metal wires into a loop; when the two junctions sit at different temperatures, a thermoelectric EMF appears in the loop — an iron–constantan (copper–nickel alloy) pair gives about 50 μV/℃ (empirical value; calibration method below), so a 100 ℃ difference gives about 5 mV, enough to drive a galvanometer pointer. The physical mechanism, the constantan recipe, and wire purification are developed in Chapter 30; this chapter handles only the instrument face of "sensor + meter movement + calibration."

**How to build it**: 1.5 m each of iron wire and constantan wire (φ 0.5 mm class, drawn per Chapters 17, 19); twist the measuring-end tips together 5 turns, then tin-solder or forge-weld them into a junction (the third metal introduced by the solder is isothermal end to end and does not affect the EMF — the law of intermediate metals, proven in Chapter 30). With no constantan, substitute copper wire: the signal is roughly half as large and reading sensitivity drops one grade; note "substitute wire" on the calibration card.

**The rustic cold-junction compensation (empirical method)**: during calibration, bury the cold junction in ice water (0 ℃) and build the "temperature difference vs. divisions" lookup table; in the field the cold junction sits at room temperature, so **true temperature = galvanometer indication + cold-junction temperature**. Procedure: tie a small glass thermometer (a product of 27.2.2) to the cold-junction terminal; at every reading, read the tied thermometer first, then add. Tying requirement: wrap the sensing bulb and the two-wire junction tight with cloth strip — ◎ hand-feel: wrap until a light pull on the wires does not shift them, yet the wrap can still be undone at any time; practice method: after 20 practice wraps on scrap wire, immerse the whole assembly in a 40 ℃ warm water bath; if the converted indication difference between thermometer and thermocouple is ≤2 ℃, the wrap passes; compensation: water-bath comparison (replace the "tightness" hand-feel with a measurable bath temperature).

**Calibration**: reproduce the boiling point and the beeswax point as the two anchors; in a soybean-oil bath (stirred; liquid temperature restricted to below 250 ℃, keeping at least 30 ℃ of margin under the flash point), read in the same bath as the standard thermometer, one point every 20 ℃, and plot the "temperature difference vs. divisions" lookup table; iron–constantan is nearly linear from 0–400 ℃ and bends gradually above — **use the table throughout; never a straight line**.

**Tier declaration**: the reading mechanism (the galvanometer) belongs to Chapter 30's electrical instruments — until the galvanometer stability loop closes, this section is **Tier 2** (it can be built and used; reproduction and acceptance not yet closed-loop); backfill and raise the tier once the Chapter 30 galvanometer reaches L2.

**Ceiling**: 500 ℃ for bare wire (oxidation loss); 750 ℃ class once fitted with the Chapter 14 quartz/porcelain protection tube (empirical value; calibration method: mutual cross-check with the Chapter 12 temperature cones in the same kiln).

#### 27.2.4 The High-Temperature Band: Bringing the Temperature Cones Back In

The Chapter 12 temperature cones map their numbers to bend-over temperatures, covering roughly 600–1400 ℃. This chapter formally brings them into the temperature-quantity system, forming a three-band linkage: **glass thermometer (−20 to 110 ℃) → thermocouple (≤750 ℃, with protection tube) → temperature cones (600–1400 ℃)**. The 500–750 ℃ band is the overlap cross-check zone: cones + thermocouple go into the same kiln, are compared after firing, deviations go into the ledger, and a "cone number vs. thermocouple temperature" correspondence table is summarized every 10 kiln runs (empirical value, accumulated kiln by kiln). Division of labor: the thermocouple handles the **process curve** (heat-up rate, soak segments); the cones handle **end-point acceptance** (was the final temperature reached) — release of ceramic and metallurgical kilns is judged by cone bending; this is where the Chapter 12 system sits within this chapter's temperature chain.

### 27.3 Pressure Instruments: From the U-Tube to the Spring-Tube Pressure Gauge

#### 27.3.1 Four Reinforcements for the U-Tube Manometer (on the Chapter 25 Basis)

Chapter 25 already built the U-tube manometer; this chapter does not rebuild it, only adds four reinforcements:

1. **Conversions in writing** (at first occurrence): 1 atm = 760 mmHg = 10.34 m of water column; 1 mmHg = 13.6 mm of water column. Read low pressures (<0.3 atm) on a water column, high pressures on mercury;
2. **Liquid-temperature correction**: when the indicating liquid is above 25 ℃, correct by 0.15% per 10 ℃ (empirical value; calibration method: measure the same pressure once with hot water and once with cold; the difference is this device's correction amount);
3. **Inclined-tube micromanometer**: replace one arm with a glass tube inclined at 30°, ≥500 mm long, graduated along the tube — under the same pressure difference the slanted column length is 1/sin30° = 2 times the vertical height difference, magnifying the reading 2×; used for furnace negative pressure and duct pressure differences (the tens-of-millimeters-of-water-column class). Calibration method: compare five points at identical pressures against a vertical U-tube; a magnification ratio of 2.00±0.05 passes (empirical value, must be calibrated); if the inclination has been disturbed it must be recalibrated;
4. **Both arms the same diameter**: the extra capillary pressure difference makes the level in a fine tube read low — use glass tubes of the same diameter in both arms so the capillary effects cancel; before every reading, tap the tube frame lightly to drive off wall bubbles.

#### 27.3.2 The Diaphragm Pressure Gauge (Version 1 content, retained)

- **Pressure gauge (mechanical reading)**: structure — a sealed leather diaphragm (Chapter 15 grease-impregnated leather) or a thin copper diaphragm takes the pressure; the diaphragm's center pushes a lever–sector-gear–pointer train; the dial is graduated point by point against a U-tube manometer (Chapter 25); range covers 0 up to several times working pressure; **mark the overpressure red line in red paint**.

The diaphragm type is easy to make and suits low pressures and low pressure differences of 0–0.5 atm; for higher pressures, longer life, and smaller size, the answer is the spring tube.

#### 27.3.3 Manufacturing the Spring-Tube (Bourdon-Tube) Pressure Gauge

**Principle**: a bronze tube of flattened elliptical cross-section is bent into an arc of about 270°; the fixed end is open to the pressure medium, the free end sealed shut. Internal pressure pushes the elliptical cross-section toward circular — the surface areas of the outer and inner arcs are both unchanged, so a more circular cross-section necessarily increases the arc's radius of curvature; the tube straightens overall and the free end moves outward. At working pressure the free end displaces 2–4 mm (empirical value; calibration method: measure point by point under the deadweight method), amplified through link–sector gear–pinion–pointer (the 27.1 mechanism; total magnification on the order of 100×: a 2 mm displacement becomes a 200–400 mm arc travel of the pointer tip). Version 1's C list said "the Bourdon tube requires thin-wall tube drawing and welding upgrades" — Version 2's practical conclusion: Chapter 17 bronze tubing + Chapter 22 tin soldering are enough; silver soldering is unnecessary; strike it from the C list.

**Dimensions and materials** (empirical values, must be field-calibrated):

| Part | Specification | Criterion |
|---|---|---|
| Tin-bronze tube | OD 6 mm, wall 0.8 mm, length 200 mm | Wall thickness difference over three caliper points ≤0.1 mm; no pressure dents on the surface |
| Cross-section after flattening | flattened ellipse, major axis 7 mm × minor axis 3.5 mm | Minor axis by caliper 3.5±0.2 mm; a scrapped sample sawn open shows no wrinkles in the section |
| Arc | bend radius 35 mm, included angle 270°, fixed-end straight segment 25 mm / free-end straight segment 15 mm | Gap against the template ≤0.5 mm |
| Range | full scale = 1.5 × maximum working pressure (red line, Chapter 28) | The red line falls near the 2/3 point of the scale |

**Manufacturing sequence**:

1. Cut to length, then anneal (Chapter 17: about 600 ℃, hold 30 min, slow cool; empirical value, calibrate per batch: under-annealed tube cracks during bending);
2. **Fill with rosin**: fill the tube with molten rosin (prevents the section from collapsing dead during flattening and prevents wall wrinkling); wooden plugs in both ends;
3. **Die-press the ellipse**: file a semi-elliptical groove into each of a pair of hardened steel dies (semi-major axis 3.5, semi-minor axis 1.75 mm; closed, the dies form the 7×3.5 ellipse); close the dies and press flat — ◎ hand-feel: press until **the two die faces just meet at the seam, then stop**; add no extra hammer force (over-pressing wrinkles); practice method: press 10 scrapped tubes, saw each one open, inspect the section for wrinkles; compensation: judge acceptance by caliper measurement of the minor axis, never by hand-feel;
4. Heat to pour out the rosin, scrub the inner wall clean with hot lye water, then rinse with clean water — **residual wax is the number-one source of hysteresis**;
5. **Bend the arc**: the ellipse plane lies perpendicular to the bending plane — criterion: the major axis of the tube-end cross-section points at the bending form's center; bend slowly in segments against the R35 form; springback is 5°–10° (empirical value; record this batch's springback angle on the first piece) — bend the compensation to final position; ◎ hand-feel: slow bending with even force, seated to the form in one continuous pass; one hard jerk-bend is forbidden; practice method: bend 10 scrapped tubes and check each against the template; compensation: judge the template gap with a 0.5 mm feeler gauge or a thick paper shim;
6. Tin-solder the M10×1.5 fitting onto the fixed end (Chapter 22); tin-solder the free end shut and solder on the φ2 mm copper pin (to connect the link);
7. Fit the movement (27.1): link effective length 30 mm, sector-gear–pinion angular magnification about 1:10, hairspring preloaded to remove backlash;
8. **Pressure test**: pressurize by deadweight to 1.5 × full scale and hold 5 min — no leak at the fittings (soap-solution method), return to zero after unloading ≤1 division, zero point unchanged on second pressurization (a change = the tube has taken a permanent set);
9. Dot-mark calibration on the white blank dial (the 27.3.4 five-point method) → fit the formal graduated dial → install the gauge glass → lead seal (wax + numbering stamp).

**Quick reference**: hysteresis (same-point difference between rising and falling pressure >1 division) → check in order: residual wax in the tube (boil it out) → worn link pin hole (replace the pin) → insufficient hairspring preload (add 1/4 turn); indication drift → micro-leak at a solder seam (soap-solution method).

#### 27.3.4 The Deadweight Calibration Method: Bootstrapping the Pressure Standard

**Principle**: standard pressure = weight force ÷ piston area, P = mg/A. Mass traces to the Chapter 3/22 weights; diameter traces to the Chapter 22 micrometer — **the pressure quantity bootstraps locally from mass × length, depending on no purchased standard whatsoever**.

**The deadweight tester**:

- Cylinder–piston: a bronze cylinder (drill–ream–lap, Chapters 20, 22) paired with a hardened steel piston, diameter 10.000 mm (micrometer, four points in two directions, range ≤0.01 mm) → area 78.5 mm²; fit-clearance criterion: with lubricant applied, the piston slides slowly down under its own weight (about the 30 s/100 mm class, empirical value; calibration method: verified against the mercury-column comparison point); wobble visually indiscernible;
- Screw pressurizing pump: an M16×2 lead screw (Chapter 22) drives a small water cylinder (medium: water or castor oil); a tee on the cylinder branches to the gauge under calibration and to the piston column;
- Weights: 500 g×2, 1 kg×2, 2 kg×1, 5 kg×1 (verified on the Chapter 3 balance); the self-weight of the piston and tray is weighed on the balance, chisel-engraved on the tray rim, and counted into the zero-point pressure.

**Pressure-point table** (d = 10 mm piston, area 78.5 mm²):

| Applied load (incl. tray) | Pressure produced | Equivalent |
|---|---|---|
| 2 kg | 0.25 MPa | ≈2.5 atm ≈1870 mmHg |
| 4 kg | 0.50 MPa | ≈4.9 atm |
| 6 kg | 0.75 MPa | ≈7.4 atm |
| 8 kg | 0.99 MPa | ≈9.8 atm |

**Operation**: bleed the gauge cavity and the cylinder → hang the weights → rotate the piston slowly and continuously (about one turn per 2 s, to kill friction) → tap the case lightly and read → five points rising, five points falling; at each point the rising–falling difference ≤1 division; five-point indication error ≤2% of range.

**Cross-verification**: connect the tester to a 1 m mercury U-tube, pressurize to a mercury difference of 500 mmHg; the applied load should be 0.53 kg (a difference >2% means check the piston area, the weights, or the mercury column reading) — **cross-verify the deadweight tester once before each month's use**; record the cross-verification value in the ledger.

#### 27.3.5 Periodic Calibration of Boiler Pressure Gauges (the Chapter 28 Release Interface)

- Every in-service pressure gauge gets a **monthly check** (deadweight, five points); after calibration it is lead-sealed and hung with a **calibration tag** (this date / next date / calibrator);
- **Max-recording pointer**: a passive pointer is added inside the gauge, pushed by the working pointer to the highest value and not returning — overpressure leaves its evidence; the first item of the Chapter 28 boiler release check is precisely "has the max pointer touched the red line";
- **A boiler without a valid calibration tag must not be fired** (Chapter 28 release clause);
- Three events — a knock, over-travel, a suspicious reading — mean it goes straight back for calibration (consistent with the 27.10 period grading).

[Card 27-02 Spring-Tube Pressure Gauge Manufacture and Deadweight Calibration] (eight fields)

1. **Input materials**: tin-bronze tube 6×0.8×200 mm (Chapter 17, quantity per gauge); rosin 20 g; one pair of elliptical press dies (hardened); R35 tube-bending form; tin solder and flux; 1 × M10×1.5 fitting; φ2 mm copper pin; movement parts (sector gear–pinion–hairspring–pointer–white blank dial, self-made per 27.1).
2. **Tools required**: deadweight tester (27.3.4, d10.000 piston; cross-verify the mercury-column point before use); micrometer (Chapter 22; zero check + one gauge-block point before use); hand hammer and files; arc template (0.5 mm feeler gauge / thick paper shim); soap-solution brush (leak checking).
3. **Operating sequence and control points**: ① anneal ② fill with rosin ③ die-press the ellipse — **control point: stop when the die faces meet at the seam** ④ remove the wax and wash clean — **control point: rinse with solvent until no film remains** ⑤ bend the 270° arc (ellipse major axis pointing at the form center; compensate the springback with a corrective bend) ⑥ solder the fixed-end fitting + seal-solder the free end and solder the pin ⑦ **pressure test at 1.5 × full scale for 5 min (no leak / return to zero ≤1 division / zero unchanged on repressurizing)** ⑧ fit the movement ⑨ deadweight five-point dot-marking (five points each rising and falling) ⑩ formal dial + lead seal + calibration tag.
4. **Empirical parameters and calibration**: full scale = 1.5 × red line; 1 kg applied load ≈1.23 atm (d10 piston); five points = 0/25/50/75/100% of range; indication error ≤2% of range, return difference ≤1 division (empirical values; calibrate to local conditions — revise by statistics on the first batch of 10); springback angle 5°–10° (empirical value; calibrate to local conditions — record this batch's value on the first piece).
5. **Process observation and recording items**: measured minor axis after flattening, arc template gap, pressure-test curve (pressure–time), five-point rising/falling deviation table, calibrator and next due date — entered on the pressure gauge calibration card.
6. **Pass / rework / scrap criteria**: accept = five points ≤2% + return difference ≤1 division + pressure test passed; rework = hysteresis over limit (boil the residual wax out of the tube and reassemble; add 1/4 turn to the hairspring and recalibrate), dial dot-marks misplaced (change the dial and re-mark); scrap = permanent tube deformation (zero shifts on repressurizing), a seam that still leaks after two repair solders, damaged sector gear.
7. **Common failures and troubleshooting order**: symptom "indication reads low" — first rule out the reference (the deadweight tester itself: recheck the mercury-column cross-verification point, 500 mmHg≈0.53 kg), then check in order of frequency: ① residual-wax hysteresis in the tube (look at the rising–falling difference) ② worn link pin hole (inspect the slop visually, feel for wobble) ③ insufficient hairspring preload (pointer jump >1/4 division when tapped lightly). Symptom "pointer does not move" (by frequency) — ① fitting blocked ② tube flattened/collapsed (no displacement during the pressurized leak test) ③ movement jammed (check per 27.1).
8. **L1 / L2 / L3 evidence**: L1 = five-point deadweight record for one gauge; L2 = statistics ledger for the first batch of 10 + the monthly-check system put in writing; L3 = the deadweight tester's traceability file (weights/micrometer/mercury cross-verification records) + the calibration tag and max-recording pointer systems written up and linked to the Chapter 28 release.


---

## Part A Fixed Blocks (Specific to 27.1–27.3)

## Part A Process Card Index
[Card 27-01] Glass thermometer three-point calibration (card at end of 27.2.2) | [Card 27-02] Spring-tube pressure gauge manufacture and deadweight calibration (card at end of 27.3)

Both cards can be copied onto a single page and carry the full eight fields.

## Part A Acceptance Criteria
**L1**: one thermometer with two fixed points + one pressure gauge with one deadweight point; **L2**: temperature three points + pressure three stages all pass through the calibration chain; **L3**: merged into Part B's calibration system.

## Part A Safety Boundaries
Mercury thermometers banned (the cinnabar red line); mercury U-tubes follow the mercury discipline of Chapters 33/53; boiler gauges follow the Chapter 28 release clause.
## Part A Failure Modes and Diagnosis

| Symptom | Candidate causes (by probability) | Disposition |
|---|---|---|
| Two thermometers read far apart | uneven capillary / wrong fixed-point conditions | Re-calibrate the ice point three times; cross-check within the batch and grade |
| Pressure gauge loses pressure (during the hold) | seepage / gauge zero drift | Localize by staged pressure holds; re-zero and recalibrate |
| Bourdon tube lag | insufficient temper / uneven wall thickness | Remake with a new tube; register a downgrade |

## Part A Next-Step Dependencies
Pressure gauge → Chapter 32 boiler release; thermometer → all temperature control in Chapters 26/34/35; calibration chain → Part B's 27.10 overview.

