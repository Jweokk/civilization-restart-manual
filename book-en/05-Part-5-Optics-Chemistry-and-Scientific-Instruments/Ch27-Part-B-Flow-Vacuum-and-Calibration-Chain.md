---

# Chapter 27 · Part B: Flow, Vacuum, and the Four-Quantity Calibration Chain (27.4–27.11)

> Continues from Part A. The "gauge-selection table" for the four quantity classes and the calibration-chain overview belong to this part.

### 27.4 Flow Measurement: The Reference Is a Bucket and a Clock; the Engineering Pieces Are Weirs and Pitot Tubes

#### 27.4.1 Volume–Time Method: The Acceptance Reference for All Flowmeters

**Principle**: flow rate = standard volume ÷ fill time. Calibration chain: volume is fixed by the weighing method (mass traces to the Chapter 3/25 balances, density traces to Chapter 25), time traces to the Chapter 3 timekeeping reference — **the source of the flow quantity is likewise mass × time**.

- **Standard bucket**: trust no "scale markings", only weighing — total weight after filling the bucket with water − empty bucket weight = net water weight; divide by the water density at the prevailing water temperature (for 10–25 ℃ take 1 kg/L, error <0.3%, acceptable to take directly; for greater accuracy use the Chapter 25 density table) to obtain the actual volume V; chisel-mark the bucket body and enter it in the ledger;
- **Timer**: a drip water clock or a pendulum stroke counter (Chapter 3); acceptance method: over 10 consecutive full-bucket timings the range ≤2%; if out of tolerance, replace the timer;
- **Operation**: at the same flow rate measure 3 buckets consecutively and take the median; for large flows (>100 L/min) use a 200 L large bucket or a two-bucket relay;
- **Order-of-magnitude sanity check**: bucket 50 L, pipe flow 20 L/min → full bucket 2.5 min, timing error on the order of 1 s → flow error <1%; the bucket method is more than adequate. If the flow is 500 L/min, a full bucket takes only 6 s and the timing error starts at 5% — **switch to a larger bucket or change to the weir method**. Even a reference has an applicable range; that is the first lesson.

#### 27.4.2 Tipping-Bucket Flowmeter (first-edition content, retained)

- **Flowmeter (positive-displacement)**: a fixed-volume bucket tips and is counted — the water fills the standard bucket, which then tips over and empties; each tip advances one notch; mechanical counter = ratchet and pawl (Chapter 21) + dial. Daily flow = tip count × bucket volume (accumulated automatically in the ledger). adds one item: **the bucket volume is re-verified once per season with the volume–time method** (buckets wear and foul); if the bucket volume changes by >2%, repair the bucket and update the ledger coefficient.

#### 27.4.3 Weir Method: A Head–Flow Lookup Table for Open-Channel Flow

Applicable to: open channels, waterwheel supply flumes, drainage ditches — situations where the pipe cannot be capped and led into a bucket.

**Structure**:

- The weir plate (3 mm thin steel sheet, or a wooden board sheathed with iron sheet) stands in the channel, with a 90° V-notch cut into it; the downstream face of the notch is filed into a 45° edge — ◎ hand-feel: lightly scraping the edge backward with a fingertip gives a "scratched" feel with no rounded bluntness; practice method: cut 10 notches on scrap board; compensation: the drip test — the water nappe should lift completely off the plate face by 2–3 mm without clinging to the wall; clinging flow = dull edge or insufficient chamfer;
- Flow steadying upstream of the weir: a straight channel reach ≥10 times the maximum head upstream of the weir plate; the crest is ≥150 mm above the downstream water surface, and the cavity beneath the nappe's lower edge is vented to atmosphere (visually confirm bubbles churning under the nappe — an unvented clinging flow can make readings low by 10%-order; the empirical value must be calibrated by comparison before and after venting);
- **Water-level point gauge**: the measurement point sits 200–400 mm upstream of the notch (3–4 times the maximum head, clear of the falling-water disturbance); the needle tip is lowered slowly until it touches the water surface (read when the tip and its mirror image just meet, visually; resolution 0.5 mm), or use a hook gauge; **zero point = the needle tip just touching the apex of the weir V**; re-zero before each calibration.

**Calibration (self-made lookup table)**: empirical formula for a 90° triangular weir Q = 1.4·H^2.5 (Q: m³/s; H: head on the weir, m; coefficient range 1.34–1.42). **The empirical formula serves design estimation only; acceptance must be by direct measurement**: set 6 head steps (20/40/60/80/100/150 mm); at each step record the gauge reading H and the volume–time-method flow Q simultaneously (3 buckets per step, take the median), yielding a six-point lookup table; chisel a plate and hang it beside the weir; in use, look up the table and interpolate. Interpolation error between two steps ≤2% (verified by re-measuring an inserted step; empirical value, must be calibrated). **Free-overfall criterion**: the nappe lifts completely clear and no water backs up downstream of the weir — if the downstream water level submerges the notch, this table is void (submerged weirs have their own formulas, not covered in this book; when submergence occurs, switch to direct measurement by the volume–time method).

**Order-of-magnitude sanity check**: H=100 mm → Q = 1.4×0.1^2.5 ≈ 4.4 L/s ≈ 266 L/min; a 50 L bucket fills in about 11 s, timing error 2–3% — a critical step. Disposition: for this step switch to a 200 L large bucket, or time it as "measure the total over 5 minutes and take 1/5".

#### 27.4.4 Pitot Tube: Reading Flow Velocity from Pressure Difference

**Principle**: the stagnation pressure at the impact opening (total pressure) = static pressure + dynamic pressure, with dynamic pressure = ½ρv². Connect the total-pressure opening and the static-pressure opening to the two legs of a U-tube respectively; the liquid-column difference is the dynamic pressure. For measuring water flow with water as the indicating liquid: ρgh = ½ρv² → **v = √(2gh)** (h = water-column difference, g=9.8 m/s²). Worked example: h=50 mm → v≈0.99 m/s; h=200 mm → v≈1.98 m/s. **Do not take readings when the water-column difference is <25 mm** (reading error is large); switch to the inclined-tube micromanometer (27.3.1).

**Construction**: two copper tubes, φ3 mm — the total-pressure tube has a φ1.5 mm impact opening at its tip and is bent into an L shape (opening facing squarely into the oncoming flow); the static-pressure tube runs parallel to the flow with 4 φ1 mm side holes (evenly spaced, ≥3 tube diameters from the tip). Simplified version: a single tube measures total pressure only, with static pressure taken from a hole in the pipe wall — easy to make, error of 5% order (empirical value; calibration method below).

**Pipe installation**: the Pitot tube passes through a stuffing box (Chapter 22 threaded joints + Chapter 15 grease-soaked leather packing) and is inserted to the pipe centerline; ◎ alignment hand-feel: loosen the stuffing box, rotate the probe slowly, and lock it when the U-tube reading is maximal (maximum reading = facing the oncoming flow); practice method: practice 5 times on a straight pipe section; compensation: rotating ±10° fore and aft changes the reading by ≤5%, which judges alignment acceptable.

**Center-to-mean conversion**: velocity is greatest at the pipe centerline; the cross-sectional mean velocity ≈0.8–0.85× the center value (turbulent empirical value). **This-tube calibration**: compare the whole pipe once against the volume–time method and derive this tube's "center coefficient" = mean/center; enter it in the ledger; recalibrate when the pipe diameter changes or the flow changes greatly. If the flow visibly appears laminar (slow flow in a small pipe), do not use this empirical value; calibrate separately with the bucket method.

**Flow** = mean velocity × cross-sectional area (inner diameter measured in two directions with the Chapter 22 micrometer). **Measuring air flow**: dynamic pressure is small (air at v=5 m/s has a dynamic pressure of only about 1.5 mm water column) — an inclined-tube micromanometer is mandatory; usable for duct velocities in the 3–10 m/s band; do not read below 3 m/s.

**Pipe-flow worked example (order-of-magnitude sanity check demonstration)**: a pipe of 50 mm inner diameter, center-point water-column difference 128 mm → center velocity v=√(2×9.8×0.128)≈1.58 m/s; this tube's center coefficient 0.82 → mean velocity ≈1.30 m/s; cross-sectional area π×0.025²≈1.96×10⁻³ m² → flow ≈2.55 L/s ≈153 L/min. Cross-check: a 200 L bucket fills in about 78 s, timing error <1% — the whole chain is of reasonable magnitude and may be entered in the ledger.

[Card 27-03 Weir Flow Calibration] (eight fields)

1. **Input materials**: one weir plate (3 mm thin steel sheet or board sheathed with iron sheet); point gauge (needle tip + vernier, resolution 0.5 mm); standard bucket (volume fixed by weighing, 50–200 L, bucket number in the ledger); timer.
2. **Tools required**: square (90° verification of the notch); fine file (45° chamfer of the edge); level and plumb line; Chapter 3 layout tools; full volume–time-method set (27.4.1).
3. **Operating sequence and control points**: ① lay out – saw – file the notch to 90°±0.5° (check the light gap with a square) ② 45° edge on the downstream face — **control point: drip test with the nappe lifting off the plate face** ③ stand the plate plumb, crest ≥150 mm above downstream ④ gauge zero point — **control point: needle tip just touching the V apex** ⑤ set 6 head steps (20–150 mm), 3 timed buckets per step — **control point: measurement point 3–4 times the maximum head from the weir** ⑥ record the six H-Q points; chisel the table plate.
4. **Empirical parameters and calibration**: Q=1.4H^2.5 is for estimation only (coefficient range 1.34–1.42; empirical value, calibrate to local conditions — the six measured steps are that local calibration); the lookup table defers to direct measurement; interpolation error ≤2% (re-measure an inserted step); upstream straight reach ≥10 times the maximum head; visual venting criterion; the weir table is qualified when the table-derived flow deviates from the bucket method by ≤5%.
5. **Process observation and recording items**: gauge reading at each step, fill time per bucket, net bucket weight, water temperature, nappe state (lifted/clinging), table plate number and date — enter into the weir ledger.
6. **Pass / rework / scrap criteria**: accept = six points monotonic + same-step re-measurement repeat ≤2% + interpolation verified + deviation from the bucket method ≤5%; rework = dull edge (after re-filing, **re-calibrate the entire table**); scrap = warped weir plate (straightedge light gap on the plate face >1 mm), or downstream submergence that cannot be remedied.
7. **Common failures and troubleshooting order**: symptom "table-derived flow differs from the bucket method by 8%" — ① gauge zero point drifted (re-touch the V apex) ② measurement point too close to the falling-water zone (watch the surface disturbance) ③ nappe clinging to the wall (check venting) ④ table plate out of date (fouling and notch wear change the geometry) — troubleshoot in order; at each step, if present, correct it and re-measure.
8. **L1 / L2 / L3 evidence**: L1 = a record of two step points agreeing with the bucket method to ≤5%; L2 = six-step table plate + quarterly re-verification records; L3 = the weir ledger incorporated into hydraulic production scheduling and waterwheel output calculation (Chapter 38 account book), with quarterly re-verification continued for half a year.

### 27.5 Vacuum Measurement: One System, Three-Stage Gauge Selection

#### 27.5.1 Why Gauge Selection Must Be Split by Pressure Regime

Every kind of vacuum gauge covers only two or three orders of magnitude: a mercury gauge is capped by a 760 mm tube length, and the McLeod gauge has a limited compression ratio. **Using a gauge of the wrong range = reading a handsome false number** — connect a low-range gauge to a high-vacuum system, read "bottom of scale" and believe the target is reached: this is the number-one accident source in vacuum work (silent failure; the first lesson of Chapter 33 vacuum processing). So establish the gauge-selection regime first, then discuss building gauges.

**Pressure regimes and gauge-selection table** ( addition):

| Pressure regime | Absolute pressure range | Primary gauge | Resolution | Continuous/spot |
|---|---|---|---|---|
| Rough vacuum | 760–10 mmHg | Open U-tube mercury vacuum gauge | 1 mmHg | Continuous |
| Transition | 10–1 mmHg | Closed single-tube mercury gauge | 1–2 mmHg | Continuous |
| Low vacuum | 1–10⁻¹ mmHg | Closed gauge for trends + McLeod gauge spot-check confirmation | — | Mostly spot |
| High vacuum | <10⁻¹ mmHg | McLeod gauge (Chapter 33) + discharge-tube color indication | Qualitative to semi-quantitative | Spot |

#### 27.5.2 Open and Closed Mercury Vacuum Gauges

- **Open type**: one leg of the U-tube connects to the system, the other to atmosphere; the reading h = atmospheric pressure − system absolute pressure (i.e., the "degree of vacuum"); **absolute pressure = that day's barometer reading − h**. Advantage: easiest to build and maintain; limitation: h maxes out at the atmospheric pressure value, and the absolute pressure comes from "subtracting two large numbers" — dedicated to the rough-vacuum regime;
- **Closed single-tube type** (Torricelli type): a single tube sealed at one end is filled with mercury and inverted to stand in a mercury trough; above the mercury column top at the sealed end is itself an approximate vacuum (residual pressure of negligible order), and the system connects on the trough side — **the reading is the system absolute pressure, read directly over 0–760 mmHg**, with no same-day barometric correction needed. Manufacturing key points: fill with mercury free of bubbles (thin funnel + iron-wire guide for slow pouring; tap the tube section by section to expel bubbles); perform the inversion inside a tray; interpretation: a bubble column appearing at the tube top = failed filling, refill;
- **Mercury purity**: an oil film fouling the mercury shifts surface readings by 0.5–1 mmHg order — alkaline wash, water wash, filtering through chamois or pinhole paper until **the surface is mirror-bright** (acceptance criterion);
- **Reading apparatus**: both gauges are fitted with a vernier reading scale sliding along the tube (Chapter 22 vernier concept), resolution 0.5 mm; read the mercury surface at the **crown of the convex meniscus**, with the eye level with the crown to eliminate parallax; before each reading tap the tube stand lightly to drive bubbles off the walls;
- **Safety (hard rule)**: all mercury operations inside a white-porcelain/iron tray (spills seen at once); spilled mercury is immediately covered, mixed with sulfur powder, and collected (forming mercury sulfide reduces vaporization); mercury bottles stored under water seal; work in a ventilated place. Mercury poisoning symptoms are delayed in onset (silent failure); the occupational-protection regime is developed in Chapter 39 — this chapter only establishes the operating rules.

#### 27.5.3 McLeod Gauge (referenced by Chapter 33)

A compression-type vacuum gauge: take a known-volume sample of the system gas, compress it with a mercury column to a known small volume, read the mercury-column difference after compression, and back-calculate the original pressure from Boyle's law (P₁V₁=P₂V₂). Range roughly 10⁻¹–10⁻³ mmHg; spot readings (one compression, one reading). Structure and glassworking fabrication are in **Chapter 33**; this chapter only sets the regime: **all readings below 10⁻¹ mmHg are governed by the McLeod gauge**; mercury gauges serve only as evacuation-process indicators.

#### 27.5.4 Gauge-Switching Procedure During Evacuation (Putting the Gauge-Selection Regime into Practice)

1. Start of pumping: connect the open mercury gauge; the liquid-column difference climbs from 0;
2. When the liquid-column difference nears the local atmospheric pressure value (within 40 mmHg remaining) → switch to the closed gauge (absolute pressure read directly) — the open gauge has entered the unreliable "large-number subtraction" zone;
3. When the closed gauge's liquid column falls below 10 mm (reading uncertainty >10%) → switch to McLeod gauge spot readings; the closed gauge serves only for trends;
4. High-vacuum regime: McLeod gauge spot readings + discharge-tube color cross-check (Chapter 33); when the two disagree, the McLeod gauge rules;
5. Leak prevention in gauge-changing actions: grease the joints (Chapter 33 vacuum grease) or add a small U-shaped mercury-seal trap; **if the system pressure rises back >10% within 5 min after a gauge change, shut down and check the joints** (empirical value; calibrate to system volume: for small-volume systems substitute an absolute criterion of 5 mmHg).

[Card 27-04 Vacuum Gauge Selection and Handover] (eight fields)

1. **Input materials**: the vacuum system to be measured (joints M10×1.5 or ground-glass, Chapter 33 specs); that day's barometer reading; mercury ≥500 g (washed to mirror-bright); two glass tubes φ8×900 mm (Chapter 14).
2. **Tools required**: open U-tube and closed single-tube mercury vacuum gauges (self-made per 27.5.2); McLeod gauge (drawn from Chapter 33, draw number entered in the ledger); mercury tray and sulfur powder; pinhole filter paper/chamois (filtering mercury); steel rule or vernier (reading column heights, Chapter 22).
3. **Operating sequence and control points**: ① judge the pressure regime — **control point: an unknown system always starts on the open gauge; connecting the McLeod gauge directly to draw conclusions is forbidden** ② connect the open gauge to the system and record h; absolute pressure = that day's barometer − h ③ when h has <40 mmHg remaining, switch to the closed gauge ④ when the closed liquid column is <10 mm, switch to McLeod gauge spot readings ⑤ grease/mercury-seal the joints at the gauge change — **control point: a >10% rise-back within 5 min after the change means stop and hunt leaks** ⑥ record the gauge used, the readings, and the gauge-change times for each stage.
4. **Empirical parameters and calibration**: regime thresholds 40/10 mmHg (empirical value; corrected after one McLeod-gauge cross-check in the boundary zone); closed gauge reads absolute pressure directly; open-gauge conversion formula; 10% rise-back as the leak criterion (changed to an absolute criterion according to system volume).
5. **Process observation and recording items**: gauge-change sequence, each gauge's readings and times, joint method, anomalies (bubble column at the tube top, dull mercury surface) — enter into the operating ledger of that vacuum apparatus.
6. **Pass / rework / scrap criteria**: accept = the two gauges connected simultaneously once in the handover zone with converted-reading difference ≤2 mmHg, and no missed judgments throughout; rework = leaking joints (re-grease or replace the mercury seal, then re-test); scrap = bubble column at the closed gauge's top (refill the mercury), mercury too dirty to wash (replace the mercury).
7. **Common failures and troubleshooting order**: symptom "McLeod gauge contradicts the closed gauge" — ① compression done too fast, entraining bubbles (re-measure) ② closed gauge mercury dirty (mirror-bright criterion) ③ the system itself fluctuating (pump stopped, temperature rising — watch the trend) ④ slight joint leak (rise-back method). Symptom "cannot pump down further" — ① the selected gauge has reached its lower limit (switch to the McLeod gauge to confirm the vacuum; not a pump fault) ② system leak (Chapter 33 leak-detection method) ③ pump fault (Chapter 33).
8. **L1 / L2 / L3 evidence**: L1 = one complete gauge-change sequence record; L2 = gauge-selection placards at all vacuum work sites + handover-zone mutual-verification records; L3 = the gauge-selection regime linked with the Chapter 33 McLeod gauge draw ledger, with quarterly mutual verification continued.

### 27.6 Four-Quantity Calibration Chain Overview ( addition)

The four instrument classes each form their own chain, and every chain traces back to a reference chapter already in this book:

| Quantity | Local reference | Transfer | Working | Traceability endpoint |
|---|---|---|---|---|
| Temperature | Ice point / local boiling point / reference wax batch — three phase-change points | Standard thermometer (quarterly three-point re-verification) | Working thermometers, thermocouple lookup tables | Chapter 3 equal-division scribing + Chapter 25 barometer (boiling-point correction) |
| Pressure | Deadweight tester (P=mg/A) | Mercury-column mutual verification (monthly) | Bourdon-tube pressure gauges, diaphragm gauges, U-tubes | Chapter 3/22 weights + Chapter 22 micrometer (piston area) |
| Flow | Standard bucket + timer (volume–time method) | Weir H-Q lookup table, bucket-volume coefficients | Weirs, tipping-bucket flowmeters, Pitot tubes (center coefficient) | Chapter 3/25 mass (volume fixed by weighing) + Chapter 3 timekeeping reference |
| Vacuum | Atmospheric pressure value + mercury column length | Open/closed mercury gauges | McLeod gauge spot readings (built in Chapter 33) | Chapter 3 length + Chapter 25 barometric reference |

This table is the first-hand material for the "27.11 are the instruments adequate" judgment: whenever any instrument reports a number, one must be able to answer along this table "whom you calibrate toward, and who calibrates toward you."

### 27.7 How to Build Instruments That Can Be Repeatedly Calibrated (first edition 27.3, retained)

The three requisites of calibrability; missing any one makes it a "toy," not an instrument:

1. **Comparable**: the instrument has standard interfaces (pressure port, thermometric well, weight hanger) and can be connected at any time to reference standards (U-tube, standard thermometer, standard weights);
2. **Adjustable**: two independent mechanisms for zero adjustment and slope adjustment (zero offset adjusted at the zero, full-scale deviation adjusted at the slope);
3. **Disassemblable for inspection**: modular movement (pointer mechanism separate from the pressure-sensing element; replace the diaphragm without replacing the dial).

**Calibration procedure**: the five-point method (one point each at 0/25/50/75/100% of range) — the reference standard supplies the true value; read the instrument and record the deviation; if the deviation is linear, correct it by adjusting the slope; if nonlinear, draw a "correction curve," paste it on the back of the instrument, and correct readings from the curve. **After calibration, apply a lead seal (wax + numbered stamp)**; once opened it is void and must be recalibrated.

### 27.8 From Mechanical Amplification to Optical Reading (first edition 27.4, retained)

When mechanical amplification reaches its limit (the mechanism's own deformation eats up the amplification gains), switch to optical amplification:

- **Mirror-and-scale method**: an arc-shaped graduated scale placed beside the pointer plus a small plane mirror at the pointer's side (Chapter 24) — at reading, eye, pointer, and mirror image lie on one line, eliminating parallax; equivalent to raising the reading resolution by one grade;
- **Optical lever (king of micro-displacement)**: a mirror mounted at the point of micro-motion to be measured (e.g., thermal elongation of a metal rod, beam deflection); the light spot aimed at the mirror is reflected onto a distant scale, deflected at twice the mirror's angle — each additional 1 chi of mirror distance adds another grade of magnification; hundredfold magnitude is easily achieved (empirical value, must be field-calibrated). The "tiny quantities" left open in Chapter 25 — thermal expansion coefficients, magnetic deflection, beam deflection — all become measurable;
- **Telescope scale reading** (Chapter 24 telescope + graduated scale): read at distance without walking up (high-temperature/hazardous positions), combining parallax elimination with fine scale graduation.

### 27.9 Measurement Error, Sensitivity, and Resolution (first edition 27.5, retained)

Three concepts often conflated; they must be kept distinct:

| Concept | Definition | Criterion question |
|---|---|---|
| Resolution | The smallest perceptible scale interval | "How large is the smallest division?" |
| Sensitivity | The indication change caused by a unit change of input | "Add one unit — how many divisions does it move?" |
| Error (accuracy) | The deviation between indication and true value | "Compared with the reference standard, how large is the difference?" |

**High sensitivity does not mean accuracy**: a pointer amplified 100-fold, if its zero point drifts, gives readings that are splendid and entirely wrong. Errors are handled in two classes:

- **Systematic error** (one-directional, repeatable): correct by calibration — correction curve / zero adjustment / interchange method (unequal balance arms);
- **Random error** (two-directional, scattered): take the median of multiple measurements and report "median ± range"; if the range does not narrow with repetition = an uncontrolled variable exists; return to Chapter 25 Section 25.7 for troubleshooting.

**Three instrument-health questions** (weekly): Is the zero point right? Is it repeatable (do two readings at the same input agree)? Is the return difference large (difference between up-scale and down-scale readings)?

### 27.10 How to Establish Instrument Calibration Records (first edition 27.6, retained and expanded)

Each instrument gets one **calibration card**, containing: instrument number/name, reference standard number, all past calibration data (five-point deviation table), correction method (slope adjustment or curve), ambient temperature, calibrator, next calibration date.

**Interval tiers** (empirical value, must be field-calibrated): working instruments calibrated monthly; transfer-grade instruments calibrated quarterly; reference standards mutually cross-checked semi-annually (reusing the Chapter 22 pyramid). Three events — impact, overrange (driven to full scale), anomalous reading — trigger **immediate sending for calibration**. Each quarter, transcribe a copy of the complete calibration archive for off-site storage (fire protection, Chapter 4).

** additions: four new ledgers** (each in its proper place, transcribed into the Chapter 43 master ledger): thermometer calibration cards (three-mark positions, wax batch number); pressure gauge deadweight five-point records + calibration placard register (basis for Chapter 28 release); weir H-Q lookup table plates and the bucket-volume coefficient book (quarterly re-verification); Pitot tube center coefficients and cone–thermocouple lookup tables (summarized every 10 kiln firings). **For every parameter marked "empirical value, must be calibrated," the moment the calibrated value is settled, transcribe it into the ledger; the next batch of people need only look it up, not recall it.**

### 27.11 How to Judge Whether the Instruments Suffice to Support the Next Technology (first edition 27.7, retained)

Judgment procedure (four steps):

1. **Write out the measurement requirements of the next technology**: which quantity to measure, over what range, and what error is allowed (example: steam-engine trials need pressure at the 0–5 water-column level ±5%; a generator needs voltage comparable and current comparable in grade);
2. **Check against the existing instrument list**: is the range covered? Is the error up to standard? Do the interfaces match? — only when all three questions pass is it sufficient;
3. **When insufficient, two roads**: upgrade the instruments (this chapter's route) vs. modify the process to route around (example: if high pressure cannot be measured, lower the trial pressure and run an extrapolated comparison within the measurable region — **prefer lowering the specification; blind trial is forbidden**);
4. **Register the conclusion**: "Instrument prerequisites for the Chapter 28 steam trials = ×××, ×××; achieved on day ×" — the release slip for starting a technology.

This section turns "instruments" into explicit nodes on the dependency graph: **passing the instrument gate before any chapter begins work is the institutional floodgate that prevents technological leaps in the latter half of the book.** supplement: the release prerequisites for vacuum-class work must include "McLeod gauge in place" (Chapter 33) and gauge-selection placarding (27.5); otherwise Chapter 33 vacuum processing may not begin.

---

## Capability Boundary (Part B)

Can do: weir/Pitot-tube flow, open mercury vacuum gauge, the four-quantity gauge selection and calibration-chain overview. Cannot do: the McLeod gauge itself (Chapter 33); precision spirit levels; pressures in the high-pressure band (before the heavy-liquid gauge is unlocked).

## Pre-Start Verification (Part B)

| 1 | Mercury | ≥500 g and processed per the 16.12 mercury unlock procedure |
| 2 | Weir notch | Triangular-weir thin-plate notch machining complete |
| 3 | Chapter 25 | Volume–time reference on file |

## Master Parameter Table

| Parameter | Value | Class | Field calibration method |
|---|---|---|---|
| Ice-point equilibration time | ≥10 min, reading unchanged for 1 min | Hard rule | Reading unchanged after replenishing the ice |
| Local boiling-point empirical formula | t_b=100−(760−P)/27 ℃ (P: mmHg) | Empirical | Range over 10 consecutive clear days ≤0.5 ℃ |
| Beeswax reference point | Nominal 63 ℃ (62–65) | Empirical | This batch back-measured with a standard thermometer and entered in the ledger |
| Capillary uniformity | Column-length difference per ℃ between two segments ≤5% | Criterion | Revised statistically from the first batch of 20 |
| Three-point back-test tolerance | ≤±1 division; spot-check ≤±1.5 divisions | Criterion | Same-bath comparison at 30 ℃ |
| Iron–constantan sensitivity | About 50 μV/℃ | Empirical | Calibrate at 20 ℃ steps: boiling point / wax point / oil bath |
| Cold-junction binding acceptance | Conversion difference at a 40 ℃ bath ≤2 ℃ | Criterion | Water-bath comparison compensating for hand-feel |
| Thermocouple upper limit | Bare wire 500 ℃ / protection tube 750 ℃ | Empirical | Cross-checked in the same kiln against temperature cones |
| Pressure conversion | 1 atm=760 mmHg=10.34 m water column | Standard | — |
| Inclined-tube magnification ratio | 2.00±0.05 (30° inclination) | Empirical | Five-point comparison against the vertical tube |
| Liquid-temperature correction | Above 25 ℃, correct 0.15% per 10 ℃ | Empirical | Hot-water/cold-water comparison at equal pressure |
| Bourdon tube specification | Bronze 6×0.8 mm, ellipse 7×3.5, arc R35/270° | Empirical | Judged against the first-article sample with calipers |
| Free-end displacement | 2–4 mm (at working pressure) | Empirical | Measured point by point under deadweight at each pressure |
| Pressure-withstand test | 1.5× full scale, held 5 min | Hard rule | Soap-solution leak check + zero unchanged after re-pressurizing |
| Full-scale selection | 1.5× maximum working pressure (red line) | Empirical | Red line placed at the 2/3 point of the scale |
| Deadweight piston | d10.000 mm, A=78.5 mm²; 1 kg≈1.23 atm | Standard | Micrometer four-point measurement + mercury mutual verification |
| Deadweight mutual-verification point | Mercury difference 500 mmHg = hung weight 0.53 kg | Criterion | Once a month, entered in the ledger |
| Pressure gauge tolerance | Indication ≤2% of range, return difference ≤1 division | Criterion | Revised statistically from the first batch of 10 |
| Timer acceptance | Range over 10 full-bucket timings ≤2% | Criterion | — |
| Triangular-weir empirical formula | Q=1.4H^2.5 (m³/s, m) | Empirical | For estimation only; acceptance by direct measurement |
| Weir lookup table | 6 head steps measured directly; interpolation ≤2% | Criterion | Re-measure an inserted step |
| Weir installation | Upstream straight reach ≥10× maximum head; crest ≥150 mm above downstream; measurement point 3–4× maximum head from the weir | Hard rule | Visual check of nappe venting |
| Pitot tube | v=√(2gh), readings start at 25 mm water column | Standard | Whole-pipe comparison against the bucket method |
| Center coefficient | Mean/center ≈0.8–0.85 (turbulent) | Empirical | This-tube calibration by the volume–time method |
| Vacuum regime-switch thresholds | Open→closed: 40 mmHg remaining; closed→McLeod: 10 mmHg | Empirical | McLeod gauge cross-check in the boundary zone |
| Gauge-change leak criterion | Rise-back >10% in 5 min (small volume: 5 mmHg absolute) | Empirical | Calibrated to system volume |
| Handover-zone mutual verification | Converted-reading difference between the two gauges ≤2 mmHg | Criterion | One simultaneous connection |

## Failure Modes and Diagnosis

Ordered from "most common → hardest to detect":

| Symptom | Candidate causes (by probability) | Verification | Remedy |
|---|---|---|---|
| Thermometer mid-section off by 3 divisions (most common) | Mis-scribed segment; locally thick bore; wax batch drift | In order: segment-boundary marks → add bath points above and below → re-test the wax with a standard thermometer | Re-scribe; scrap after localizing the fault; back-measure again with a new batch |
| Thermometer drifting 1–2 divisions overall | Aging drift of the bulb volume; broken column or broken thread | Cool fully and re-check the broken column; same bath as the standard | Downgrade to a teaching piece; scrap |
| Thermocouple reading low | Loose cold-junction binding (cold end actually too warm); oxidized junctions | 40 ℃ water-bath comparison; inspect the junctions | Re-bind; re-solder the junctions |
| Thermocouple chain drifting as a whole (irregularly) | Galvanometer zero drift (Chapter 30 mechanism); third-metal contamination at the wire junctions | Disconnect the sensor and short the galvanometer to check the zero; check whether the junctions have been re-soldered | Re-measure after re-zeroing the galvanometer; cut out the contaminated section and re-solder the junctions |
| Boiling-point mark drifting >0.5 ℃ during the day | Inaccurate barometric empirical formula; salt mixed into the water bath (boiling point raised) | Cross-check with the barometer; re-measure with clean water | Correct the empirical-formula coefficient and enter it in the ledger; change the water |
| Pressure gauge hysteresis (up/down difference >1 division) | Residual wax inside the tube; loose pull-rod pin; insufficient hairspring preload | Re-test after boiling-washing; inspect the play visually; tap lightly and watch for jumps | Rework in order, then recalibrate |
| Pressure gauge zero not returning | Overrange bent the hairspring; permanent tube deformation (overpressure history) | Re-test the zero with deadweight; check the overrange records | Replace the movement; scrap the tube |
| Deadweight tester pressure will not rise | Piston leaking (excess clearance); pump or valve leaking | Judge the clearance from the sinking speed of the hung weight | Re-lap and fit the piston; repair the valve |
| Weir reading low by 10%-order | Nappe clinging to the wall (unvented); downstream water backing up | Look for bubbles under the nappe; measure the downstream level | Clean the edge / lower the downstream level, then re-calibrate the entire table |
| Table-derived flow does not match the bucket method | Gauge zero point drifted; measurement point in the falling-water zone; table plate out of date | Re-touch the V apex; watch the surface disturbance; check the re-verification date | Re-zero; move the measurement point; re-mark the table plate |
| Pitot tube reading low | Misalignment; plugged holes | Rotate the probe to find the maximum; blow through the holes | Lock at the maximum-reading position; clear the holes |
| False impression of vacuum "reached" (hardest to detect) | A low-range gauge reading "bottom of scale" misjudges the ultimate vacuum | Replace with the McLeod gauge and measure directly | Retrain on the gauge-selection table; placarding regime |
| Mercury-surface reading off by 1 mmHg order | Dirty mercury (oil film) | Mirror-bright surface criterion | Alkaline wash – water wash – filter |
| Kiln temperature "believed sufficient but actually under-fired" (hardest to detect) | Thermocouple chain reading systematically low with no cross-check | Compare in the same kiln against temperature cones | Establish a "cone–thermocouple" lookup ledger; the bent cone is the authority |

## Process Card Index

[Card 27-01] Glass thermometer three-point calibration (card at end of 27.2.2, Part A) | [Card 27-02] Spring-tube pressure gauge manufacture and deadweight calibration (card at end of 27.3, Part A) | [Card 27-03] Weir flow calibration (card at end of 27.4) | [Card 27-04] Vacuum gauge selection and handover (card at end of 27.5)

All four cards can be copied onto a single page and carry the full eight fields; the first two sit at the ends of their sections in Part A, the last two in this part.

## Acceptance Criteria

- **L1**: one helical spring stiffness card completed; one glass thermometer three-point calibrated with back-test ≤±1 division; pressure gauge vs U-tube five-point comparison deviation <1 division; optical lever measuring the thermal elongation of a metal rod; the weir producing two H-Q points agreeing with the bucket method to ≤5%; one complete vacuum gauge-change sequence (open→closed) completed.
- **L2**: at least 1 instrument of each of the four classes — temperature, pressure, flow, vacuum — in service with continuous monthly calibration records; the Bourdon-tube pressure gauge calibrated by five-point deadweight (indication ≤2% of range, return difference ≤1 division); the weir lookup table complete at all six steps with interpolation verified ≤2%; the Pitot tube's own center coefficient on file; the thermocouple lookup table complete (including cold-junction binding water-bath verification); return difference <half a division after hairspring anti-backlash work (empirical value, must be calibrated); the boiler pressure gauge calibration placard regime joined in writing with the Chapter 28 release clause.
- **L3**: the four-quantity calibration chain (27.6 master table) fully operating: quarterly re-verification of the standard thermometer, monthly mercury mutual verification of the deadweight tester, quarterly re-verification of the weir table, vacuum gauge-selection placarding linked with the Chapter 33 McLeod gauge — records continuous for half a year with no gaps; the first "instrument release slip" issued for Chapter 28; instruments locally repairable (tube replacement / spring replacement / diaphragm replacement / re-scribing dials) with the off-site archive copy (Chapter 4) in place.

## Labor Hours, Manpower, and Consumables

| Item | Manpower | Labor hours (empirical value) |
|---|---|---|
| Three-point calibration of one thermometer | 1 person | 0.5 days (including wax-point and ice-point equilibration waiting) |
| One thermocouple + lookup table (oil bath, point by point) | 2 people | 1–2 days (depends on the galvanometer being in place) |
| One Bourdon-tube pressure gauge (flattening – arc bending – movement assembly – calibration) | 2 people | 3–4 days |
| One deadweight tester (cylinder lapping and piston fitting) | 2 people | 5–8 days |
| Pressure gauge monthly calibration (deadweight five points, per gauge) | 1 person | 0.5 h/gauge·month |
| One triangular weir (plate + point gauge) + six-step lookup table | 2 people | 2–3 days |
| One Pitot tube + this-tube center coefficient | 1 person | 1 day |
| One closed mercury vacuum gauge (including washing the mercury) | 1 person | 0.5 days |
| Monthly full calibration (four instrument classes) | 1 person | 1 day/month |
| Consumables: mercury, rosin, beeswax, bronze tube, tin solder, abrasive, soybean oil | — | Enter into the Chapter 38 account book |

## Safety Boundary

- Pressure gauges are never used beyond range (driven to full scale means it has failed and is sent for calibration); the red line mark is the shutdown line;
- Deadweight tester and pressure-withstand testing: during loading, keep head and hands out of the space directly above the cylinder and directly in front of the dial; observe from behind a barrier; when the medium is oil, guard against slipping and fire;
- Three hard rules for mercury work: all operations inside a tray, spills immediately covered with sulfur and collected, storage in water-sealed bottles — mercury poisoning is delayed in onset; records of abnormal exposure go into the Chapter 39 occupational file;
- Oil-bath calibration (thermocouples) is limited to 250 ℃ (a margin of at least 30 ℃ below the flash point); keep fire-extinguishing sand beside the oil bath;
- Weir and open-channel work: guard against slipping and drowning; operate the point gauge crouched and steady on the upstream side; no work on rising water after rain;
- For the optical lever's lamp flame/condensed light, guard against fire; replace a cracked mirror at once (reading distortion);
- For spring making, the tempering step follows the Chapter 19 quench-and-temper safety rules.

## A. Existing Tool List (partial)

Tempered spring steel (Chapter 19); threads and gears, prototype comparator (Chapters 20–22); thermometers / U-tubes / flow methods (Chapter 25); magnifiers and mirrors (Chapter 24); knife-edge technique (Chapter 25); record-keeping archive regime (Chapters 4, 25); equal-division scribing and timekeeping (Chapter 3); weights and balances (Chapters 3, 25); barometer and mercury (Chapter 25); temperature cones (Chapter 12).

## B. New Tools Added in This Chapter

Leaf springs/helical springs/hairsprings and stiffness cards; lever–sector-gear pointer mechanism and hairspring anti-backlash; detachable thermometer interface standard; diaphragm pressure gauge; tipping-bucket flowmeter and mechanical counting; the three requisites of calibrability and the five-point calibration method + lead seal; mirror-and-scale method, optical lever, telescope scale reading; the three-way vocabulary of error/sensitivity/resolution and the handling of systematic/random errors; calibration cards and the interval-tier regime; instrument release slips (27.11 judgment procedure). ** four-quantity deepening**: temperature — three-point calibration chain, reference wax batch regime, top expansion chamber blank, thermocouple cold-junction binding compensation and cone–thermocouple lookup; pressure — inclined-tube micromanometer, spring-tube (Bourdon-tube) pressure gauge, deadweight tester (pressure-bootstrap reference), boiler calibration placard and maximum-record pointer; flow — standard bucket with volume fixed by weighing, weir method and H-Q lookup table, point gauge and venting criterion, Pitot tube and center coefficient; vacuum — open/closed mercury vacuum gauges, four-regime gauge-selection table, gauge-change leak-prevention procedure; four-quantity calibration chain overview (27.6).

## C. Unresolved Dependencies

- Mercury thermometers and high-temperature glass (glass-liquid thermometry above 110 ℃, vacuum-fill process);
- Noble-metal thermocouples (platinum) — continuous thermometry above 750 ℃ still relies on the semi-quantitative Chapter 12 temperature cones;
- Pirani / ionization vacuum gauges — continuous reading below 10⁻¹ mmHg (after the Chapters 30–33 electrical instruments);
- Deadweight calibration above 10 atm (cylinder and weight strength) — for now transitioned via dual-gauge mutual calibration + mercury-column comparison;
- Constant-temperature and vibration-isolated environments (building and overall industrial level).

## Next-Step Dependencies

- Chapters 28–29: pressure gauges (including calibration-placard release), thermometers, dynamometry, and flowmeters are the quantitative eyes of heat-engine development; the "instrument release slip" and "no ignition without a calibration placard" regimes directly serve trial safety;
- Chapters 30–31: the galvanometer (pointer mechanism + new sensing principle) is the electrical descendant of this chapter's mechanisms; the physical side of thermocouples and the constantan formula are developed in Chapter 30; after the galvanometer reaches L2, this chapter's thermocouple section is backfilled and upgraded;
- Chapter 33: the McLeod gauge and vacuum grease are supplied by Chapter 33; the gauge-selection placard regime is a start-of-work prerequisite for Chapter 33 vacuum processing;
- Chapter 34: the optical lever and precision temperature control are prerequisites for observing crystal growth;
- Chapters 37–39: the four-quantity calibration ledgers merge into spot checks and the skill matrix; occupational protection for mercury work belongs to Chapter 39;
- The Part 10 environment editions: the instrument maintenance regime is the universal prescription for keeping industrial capability under harsh conditions.
