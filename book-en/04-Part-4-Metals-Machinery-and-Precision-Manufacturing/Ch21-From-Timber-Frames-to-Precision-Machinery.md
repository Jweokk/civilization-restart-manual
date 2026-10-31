# Chapter 21: From Timber Frames to Precision Machinery

## Chapter Objectives

Build a **mechanical power-transmission system** on top of machine-tool capability: the manufacture and inspection of shafts, bearings, gears, and cranks; estimation of transmission ratios and efficiency; and the power upgrade from human/animal power to water/wind power, culminating in a "line-shaft workshop" style mechanical shop — the mechanical parent of every machine in Part 6 (steam engine, generator).

## Capability Boundary

**Can do:** layout-and-filing of approximate teeth on wooden/cast-iron gears and acceptance by meshing (transmission-ratio fluctuation at the ±5% level; usable only for speed change and counting, not for precision indexing); plain-bearing systems; water-wheel/windmill power with a line-shaft workshop (multi-station continuous operation).

**Explicitly cannot do:** rolling bearings and higher speed limits (requires grinding capability, long-term); batch precision finishing of metal gears (partially mitigated by the standard-parts regime in Chapter 22); breaking the power ceiling set by hydrology/wind regime (steam power arrives in Chapter 28).

**External dependencies:** siting data for a stable water source or stable wind regime (Chapter 2 resource archive); attendant labor (the water-wheel gate is the speed governor, so a machine attendant is required).

## Pre-Start Verification (check each item)

| # | Verification item | Criterion | Source |
|---|---|---|---|
| 1 | Lathe | Spindle radial runout ≤0.05 mm; test-bar turning to standard | Chapter 20 |
| 2 | Scraping capability | Proficient in the bush contact-band method (middle band ≥60%) | Chapter 20 |
| 3 | Castings & forgings | Gear blanks/crank blanks cast without shrinkage cavities (rings clear when struck) | Chapters 17, 18 |
| 4 | Keys & pins | Matched-and-numbered fitting system in use | Chapter 20 |
| 5 | Belt material | Leather/thick fabric joints with staggered stitching | Chapter 15 |
| 6 | Siting data | Flow Q and head H (measured in dry season) or ≥1 season of annual wind records | Chapters 2, 3 |
| 7 | Measurement | Proficient in the runout check (scribe + test bar) and string-line alignment | Chapter 20 |
| 8 | Timber | Rim stock fully dried (monthly weight-check method) | Chapter 7 |

---

### 21.1 Shafts, Wheels, Gears, and Cranks

**Shafts**: forge the blank, then turn it between centers on the lathe; straightness check for long shafts — rotate the shaft one full revolution and measure radial runout with a scribe at multiple cross-sections; locate with a shoulder/pin hole at the shaft ends. The higher the speed, the tighter the runout requirement (water-wheel shafts ≤0.5 mm; machine-tool spindles to the Chapter 20 standard).

**Wheels**: wooden wheels (segmented mortise-and-tenon rim + hot-shrunk iron hoop — heat the hoop, fit it on, and let it shrink-grip as it cools); cast-iron wheels are turned on their inner circle after casting and keyed to the shaft. **Keyed joints**: cut a rectangular keyway in both shaft and hub (chisel + file, matched and numbered); the key transmits torque and prevents relative rotation.

#### 21.1.1 Gear Layout Approximation Method (an unfolding of the involute, verifiable step by step)

Tooth-cutting route when no dedicated machine tool exists:

1. **Fix the module and tooth count**: pitch circle diameter D = m×z (module m: 4–6 mm for power transmission, 2–3 mm for instruments; z = number of teeth). Two meshing gears **must share the same module**; transmission ratio i = z₂/z₁;
2. **Draw the pitch circle and base circle**: base circle diameter = D×cos 20° ≈ 0.94×D (20° is the common pressure angle; the approximation suffices for this route's accuracy);
3. **Divide the pitch equally**: divide the pitch circle into z equal parts by the cord-wrapping method or an angle plate (Chapter 3), and draw each tooth's centerline;
4. **Unfold the tooth profile (circular-arc approximation of the involute)**: with each division point on the base circle as center, and as radius the distance "from that point to the intersection of the tooth flank with the pitch circle," draw an arc — the arc is the approximate tooth flank. Procedure: first make a full-scale (1:1) tooth-profile template on stiff paper/wood board (a 5-tooth segment suffices); after verifying with the template that two teeth roll against each other without interference, use the template to lay out the lines on the wheel blank;
5. **Chisel and file to shape**: chisel first, then file, leaving 0.5 mm for finishing; smooth the tooth flanks with a file + oilstone;
6. **Meshing check**: apply marking compound and roll the pair — the contact patch should sit at mid-flank and cover ≥1/3 of the tooth height (empirical value, must be field-calibrated); leave tip clearance of 0.2×m to prevent jamming; set backlash by the standard "slight rock when hand-turned, rotation without binding" (about 0.05–0.15 mm, ◎ hand-feel; compensation: insert paper strips of known thickness to measure the rock);
7. Cast-iron gears: recast from a wooden pattern carrying the tooth shape (Chapter 17), then dress the allowance by hand.

**Honest positioning of first-generation gears**: tooth-profile error produces transmission-ratio fluctuation at the ±5% level (empirical value) — acceptable for power transmission, speed change, and counting; precision indexing (e.g., the precise indexing of the Chapter 22 lead-screw change gears) requires selecting the most accurate pair, tagging it "indexing-grade," and managing it separately.

[Card 21-03 Gear Layout Approximate Tooth-Cutting] (eight fields)

1. **Input materials**: gear blank (wood/cast iron, cast free of shrinkage cavities, rings clear when struck); stiff paper or thin board (for the 1:1 tooth template — a 5-tooth segment suffices); marking compound; paper strips (for backlash).
2. **Tools required**: dividing and layout tools (Chapter 3 cord-wrapping method / angle plate); scribe and straightedge; chisel, file, oilstone; shaft brackets for the marking-compound roll. Calibration source: pitch circle computed from module and tooth count; base circle approximated as 0.94×D.
3. **Sequence and control points**: (1) fix module and tooth count (m = 4–6 mm for power transmission, 2–3 mm for instruments; meshing gears must share the module) → (2) draw the pitch circle D = m×z and the base circle ≈0.94×D (20° pressure angle) → (3) divide into z parts by cord-wrapping or angle plate and draw the tooth centerlines → (4) swing arcs from the base-circle division points to unfold the profile; **make the 1:1 template first (5-tooth segment) and only lay out on the blank after the template rolls without interference** → (5) chisel first, then file, leaving 0.5 mm for finishing; polish with file + oilstone → (6) apply marking compound and roll to check the contact patch, leave tip clearance 0.2×m, measure backlash with paper strips. Control point: laying out on the blank with an unverified template scraps the whole wheel.
4. **Empirical parameters and calibration**: D = m×z; base circle ≈0.94×D; tip clearance 0.2×m; contact patch central and ≥1/3 of tooth height (empirical value, must be calibrated to local conditions); backlash 0.05–0.15 mm (paper-strip method, ◎); tooth count ≥12 (discipline); single-stage ratio ≤1:5; center distance = m×(z₁+z₂)/2, with slotted bracket holes leaving ±2 mm. Calibration: chalk both gears and turn 10 revolutions, counting the difference in driven revolutions; if fluctuation exceeds the ±5% class, pick the most accurate pair, tag it "indexing-grade," and manage it separately.
5. **Observations to record**: per pair — module/tooth count / measured pitch and base circles / dividing error (span across first and last tooth) / template roll result / contact-patch position and share of tooth height / measured tip clearance and backlash / pair number.
6. **Pass / rework / scrap criteria**: pass = contact patch central and ≥1/3 of tooth height + slight rock and no binding when hand-turned + tip clearance 0.2×m; rework = patch toward tip or root (correct the profile or adjust center distance through the slots), backlash off (fine-tune at the slots and recheck); scrap = template error that scrambles the tooth spacing, or a broken tooth (recast / new blank).
7. **Common failures and diagnosis order**: (1) loud periodic noise (pitch error large → backlash wrong); (2) rapid tooth-face wear (patch toward tip/root → no oil); (3) binding when hand-turned (tip clearance below 0.2×m); (4) unequal rock in the two directions (bevel-gear back-cone layout off — see Section 21.10).
8. **L1 / L2 / L3 evidence**: L1 = one pair with a conforming contact patch + template kept on file; L2 = three pairs paired-numbered with contact-patch and backlash records on file; L3 = a second person cuts one conforming pair from this card alone.

**Crank mechanism**: crank pin (eccentric pin) + connecting rod + slider, interconverting rotation↔reciprocation. Manufacturing points: check crank-pin-to-main-shaft parallelism with a try square + double-jaw caliper gauge; scrape the big-end and small-end bores of the rod to fit their pins. The crank is the common interface for the Chapter 28 steam engine and the Chapter 12 bellows reciprocating drive.

### 21.2 Transmission Ratio and Mechanical Efficiency

- Single-stage ratio: gears i = z₂/z₁; belts i = D₂/D₁ (reduce about 3–5% for slip, empirical value);
- Multiply ratios through for multi-stage series; **multiply efficiencies through as well**;
- Typical efficiencies (empirical values, must be field-calibrated): flat belt 0.94–0.97, open gear pair 0.95–0.98, plain bearing 0.98 per pair, chain/rope 0.9–0.95;
- Estimation: output power = input × product of the stage efficiencies. Replace estimates with measurements using the Chapter 25 brake-dynamometer method; retest quarterly.

**Design discipline**: no stage above 1:5 for speed increase/reduction; reversal must use gears, never a crossed belt (a crossed belt wears more than twice as fast, empirical value).

### 21.3 Plain Bearings and Lubrication

Structure: bearing housing (cast iron or hardwood) + bearing bush (bronze is best, Chapter 17; grease-soaked hardwood as a substitute for low-speed service). Scrape-fit the bush bore to the shaft (Section 20.4 contact-band method) and cut an X-shaped oil groove in the **non-load-bearing zone** (a groove cut in the load-bearing zone destroys the oil film — the oil film is the plain bearing's life).

[Card 21-01 Scraping Bearing Shells and Measuring Clearance] (eight fields)

1. **Input materials**: bearing-bush blanks (bronze preferred; hardwood soaked in grease for low-speed service); an inspected journal; marking compound; a thin copper/leather shim set; lead wire about 1 mm in diameter (Chapter 31 fine lead wire, or a hammered thin sheet); lubricant (animal fat, vegetable oil, graphite-powder grease).
2. **Tools required**: scraper (Section 20.4 scraping technique); bearing housing; flat pad for lead crushing; micrometer (Chapter 22, to read the crushed lead thickness); chisel and scraper for the oil groove; wax chip (compensation for the hand temperature check). Calibration source: crown clearance measured by lead crush, never replaced by feel.
3. **Sequence and control points**: (1) mate the bush to the housing, bush-back-to-bore contact ≥60% → (2) apply marking compound to the journal, assemble, rotate → (3) scrape the high spots until **the contact band sits centrally and covers ≥60% of bush length** → (4) fit shims to set clearance, recheck the crown clearance by lead crush → (5) cut the X-shaped oil groove in the **non-load-bearing zone** (a groove in the loaded zone destroys the oil film) → (6) reassemble, hand-turn, and run 30 min to read the temperature rise. Control point: both the contact band and the crown clearance must pass before reassembly; one alone does not close the job.
4. **Empirical parameters and calibration**: crown clearance = 1–1.5‰ of shaft diameter (empirical value, must be calibrated to local conditions; about 0.03–0.05 mm on a φ30 shaft); bush-back contact ≥60%; contact band ≥60% of bush length; temperature-rise red line ≈60 ℃. Calibration: change shims one step at a time, log temperature rise and vibration per step, and adopt the smallest clearance that passes both "hand-turning smooth" and "≤60 ℃ after 30 min."
5. **Observations to record**: per bush pair — shaft diameter / crushed lead thickness (crown clearance) / contact-band position and length share / oil-groove position / hand-turning feel after reassembly / temperature rise at 30 min / position of bright wear marks after running.
6. **Pass / rework / scrap criteria**: pass = contact band central and ≥60% of bush length + crown clearance within 1–1.5‰ + temperature rise ≤60 ℃; rework = contact band off to one side (bored crooked or shaft misaligned — keep scraping and recheck alignment); scrap = bush cracked (recast).
7. **Common failures and diagnosis order**: (1) rapid heating (clearance too small → blocked oil groove → dirty oil); (2) shaft polished bright on one side (shaft system misaligned, correct by string line); (3) iron filings embedded in the bush (oil unfiltered — change oil, wash the bush); (4) knocking vibration (clearance too large — remove shims and reset).
8. **L1 / L2 / L3 evidence**: L1 = one bush pair passing both contact band and crown clearance; L2 = quarterly temperature-rise records for three bush pairs on file; L3 = a second person scrapes one pair from this card alone and meets the standard.

Lubricants: animal fat (low speed, heavy load), vegetable oil (higher speeds), graphite powder mixed into grease (high-temperature service). Lubrication regime: oil every shift, hand-check temperature rise (60 ℃ ceiling; wax chips as compensation); oil cup + wick drip feed for unattended stations.

### 21.4 From Hand Tools to Water Power

The problem with human power: ~0.1 kW-class sustained output, cannot be paralleled, drifts with fatigue. Animal power: 0.5–0.7 kW-class, requires fodder and veterinary care. **Any process whose daily energy consumption exceeds 10 person-days, or that requires all-day continuous operation (grinding flour, blowing blast, sawing timber, forging), should be upgraded to water/wind power** (account for the upgrade in the Chapter 38 energy ledger):

| Signal | Action |
|---|---|
| Forging depends on man-powered sledgehammers; daily output locked to the hammer count | Build a water-powered drop hammer |
| Air blast limits furnace temperature and capacity | Water-powered blast |
| Grinding/sawing occupies more than 2 people | Water-powered grinding/sawing |

### 21.5 Water Wheels, Windmills, and Mechanical Transmission

**Three water-wheel types** (power P = 1000×Q×H×η watts, Q = flow in m³/s, H = head in m, 1000 is a water-density-order constant):
- Undershot wheel: head <2 m, η ≈ 0.3–0.4 (empirical value);
- Breastshot wheel: 2–4 m, η ≈ 0.5;
- Overshot wheel: ≥4 m, η ≈ 0.6–0.7, **preferred whenever attainable**.

Order-of-magnitude sanity-check example: Q = 0.05 m³/s (small-stream class), H = 3 m, η = 0.5 → P ≈ 1000×0.05×3×0.5 = 75 W class — **enough for grinding and blast, not enough for a forging hammer**; the 500 W class requires Q×H raised threefold or more. **Compute the site before building**; starting work because "the water looks strong" is not allowed.

Construction: wooden wheel body (mortise-and-tenon + hot-shrunk iron hoop), shaft to this chapter's runout standard; the sluice channel and gate control flow (**the gate is the governor**); provide a drainage bypass in winter-freeze regions. Siting data (flow, head, ice season) goes into the resource archive.

**Windmill**: a multi-sail wheel (6–12 sails) with high starting torque, suited to pumps and mills; a tail vane keeps it aimed into the wind automatically; storm protection: sails can be furled / blades can be folded. Suited to: regions with high mean annual wind speed and scarce water power (a top priority for the Part 10 desert and island editions).

**Energy storage (smoothing fluctuation)**: an upper reservoir pond (release water to drive the wheel — equivalent energy storage), a flywheel (smooths second-scale fluctuation), a suspended-weight drop hammer (potential energy storage to drive forging).

[Card 21-04 Water-Wheel Siting and Power Estimation] (eight fields)

1. **Input materials**: siting data — flow Q (m³/s, measured in the dry season), head H (m, measured in the dry season), ice-season records; ≥1 season of water-source or wind records (Chapters 2, 3 resource archive).
2. **Tools required**: measuring line and ranging rods, timer (Chapter 3), field instruments for flow and head, resource-archive sheets. Calibration source: Q and H must be measured in the dry season and archived; estimation is not allowed.
3. **Sequence and control points**: (1) measure Q and H in the dry season over several days and archive the steady value → (2) choose the type by head: <2 m undershot, 2–4 m breastshot, ≥4 m overshot (preferred whenever attainable) → (3) compute P = 1000×Q×H×η → (4) compare the order of magnitude with the intended duty (grinding/blast vs forging hammer) → (5) if short, change the site first (raise H or lift Q×H threefold or more) before discussing construction → (6) after construction measure actual output against the estimate and retest quarterly. Control point: **compute the site before building**; starting because "the water looks strong" is not allowed.
4. **Empirical parameters and calibration**: P = 1000×Q×H×η (W); η = 0.3–0.4 undershot, ≈0.5 breastshot, 0.6–0.7 overshot (empirical values, must be calibrated to local conditions); sanity-check example Q = 0.05, H = 3, η = 0.5 → 75 W class (enough for grinding and blast only); the 500 W class needs Q×H raised threefold or more; water-wheel shaft radial runout ≤0.5 mm. Calibration: replace the estimate with a measured output by the Chapter 25 brake-dynamometer method, retest quarterly, and if output decays >10% check channel silting / worn paddles / leaking gate in that order.
5. **Observations to record**: per site — measurement date and season / Q / H / type chosen / η used / computed P / intended duty and power required / measured output after construction / quarterly retest values / ice-season and low-flow records.
6. **Pass / rework / scrap criteria**: pass = dry-season Q and H on file with computed P ≥ the power the duty requires; rework = output short (change the site, combine channels to raise Q, add head, or downgrade the duty to grinding and blast); scrap = the stream dries in the low season with no bypass, or freezes off in winter (site abandoned, choose another).
7. **Common failures and diagnosis order**: (1) output far below the estimate (Q taken at high water → channel leakage → paddles set too shallow); (2) output decaying season by season (channel silting → worn paddles → leaking gate); (3) runaway (load dropped suddenly while the gate was not lowered — machine-attendant regime plus stepwise load shedding).
8. **L1 / L2 / L3 evidence**: L1 = measured Q and H record plus the power calculation sheet for one site; L2 = measured output versus estimate on file after construction; L3 = quarterly retest curve showing no decay >10%, merged into the Chapter 39 inspection regime.

### 21.6 How Mechanical Power Is Distributed to Multiple Machines

**Line-shaft workshop layout**: main shaft (water-wheel shaft) → bevel gears reverse the drive → line shaft run along the roof ridge (in segments, one clutch fork per segment) → to each machine a drop pulley + flat belt + tension pulley. Each machine can be clutched independently (belt-shifting fork); a failed machine is disconnected without stopping the whole line.

Layout discipline: line shaft ≥2.5 m above the floor to prevent entangling people; a bearing housing every 3–4 m; drive direction aligned with the process flow (raw material in → finished product out, no backtracking).

[Card 21-02 Belt Tensioning and Slip Control] (eight fields)

1. **Input materials**: leather/thick fabric belt (joints staggered, Chapter 15); belt wax or rosin; chalk.
2. **Tools required**: tension pulley; belt-shifting fork (fitting or removing a belt while running is forbidden); driver and driven pulleys (D₁, D₂ known); timer (Chapter 3). Calibration source: slip measured by counting chalk lines, not judged by eye.
3. **Sequence and control points**: (1) press the mid-span with a finger and estimate deflection — 10–20 mm is right (◎) → (2) chalk a line on both pulleys, run under load for 10 driver revolutions, count the driven pulley's actual revolutions → (3) compute slip = (10×i − actual)/(10×i); above 2% means action → (4) three remedies in order: raise the tension pulley → rub wax/rosin on the belt face → if the belt is too wide or the pulley too small, change the pulley and add a tension pulley to increase wrap → (5) remeasure slip and run 1 h, then feel belt temperature. Control point: **measure before treating** — "it looks slack so tighten it" is not allowed.
4. **Empirical parameters and calibration**: mid-span deflection 10–20 mm (◎, empirical value, must be calibrated to local conditions); full-load slip <2% (criterion); belt stage ratio i = D₂/D₁, with about 3–5% deducted for slip (empirical value); flat-belt efficiency 0.94–0.97; after 1 h running the belt is "bearable to the hand indefinitely." Calibration: take three consecutive slip readings at the same load, use the steady value, and repeat after treatment for comparison.
5. **Observations to record**: per check — belt deflection / i (D₂/D₁) / driven revolutions per 10 driver revolutions / slip / remedy applied / slip after remedy / belt temperature at 1 h / belt-face and joint condition.
6. **Pass / rework / scrap criteria**: pass = full-load slip <2% + belt temperature bearable to the hand after 1 h; rework = slip still over 2% (retension and remeasure); scrap = belt torn (restitch with the joint staggered).
7. **Common failures and diagnosis order**: (1) slips the moment it starts (insufficient tension → oil on the pulley); (2) slips only as load rises (belt strength insufficient — widen); (3) knocking noise (joint too thick — plane it down); (4) shiny belt face (polished by slipping — apply wax).
8. **L1 / L2 / L3 evidence**: L1 = one measured slip reading brought below 2%; L2 = three consecutive months of weekly chalk-method records on file; L3 = a second person completes tensioning and slip control from this card alone and meets the standard.

### 21.7 Mechanical Wear, Clearance, and Vibration

Troubleshooting table (ordered by frequency):

| Symptom | Check first | Check next |
|---|---|---|
| Whole-machine vibration | Loose anchor/frame bolts | Shaft system misalignment (string-line check) |
| Localized knocking | Bearing clearance out of tolerance (recheck by lead crush) | Excessive backlash / broken tooth |
| Periodic abnormal noise | Loose key (one knock per revolution) | Belt joint slapping |
| Temperature rise | Lubrication interrupted | Contact band off-loaded to one side (re-scrape the bush) |

Maintenance regime: daily check (listen, feel temperature, inspect oil); weekly check (tighten fasteners, chalk-method belt tension); annual check (disassemble and inspect bearing bushes, measure tooth thickness — replace when wear exceeds 10% of tooth thickness; empirical value, must be calibrated). All items enter the Chapter 39 inspection checklist.

### 21.8 From Single Machines to a Mechanical Workshop

Workshop minimum configuration (build in order): water wheel + line shaft → sawing station → grinding station → forging station (water-powered drop hammer) → lathe station → blast station (feeding back into metallurgy). **The workshop is a living dependency graph**: every station's capability upgrade automatically benefits everything downstream.

---

### 21.9 Water-Powered Drop Hammer: Construction and Acceptance

Human-powered forging output is locked to the hammer count (Section 21.4 already ran the upgrade numbers): a sledgehammer operator with a 7 kg hammer raised 2 m delivers about 140 J per blow (= 7×9.8×2) and is exhausted after a dozen-odd blows per minute; the water-powered drop hammer converts the water wheel's continuous rotation into intermittent heavy blows — a 40 kg-class head, a 1 m-class drop, ≈400 J per blow, dozens of blows per minute, and no fatigue. It is also the breakthrough piece for the Section 21.5 conclusion that "small-stream-class water power suffices for grinding and blast, not for the forging hammer": **the drop hammer consumes not instantaneous power but stored energy** — the wheel spends a full slow revolution lifting the hammer, and the blow is released in an instant.

Five principal components:

| Component | Material/method | Key criterion |
|---|---|---|
| Forging timber frame | Hardwood posts (≥200×200 mm stock) + mortise-and-tenon beams + two-way diagonal braces + footing stones | After 30 min of no-load blows, recheck by plumb line: post verticality change ≤5 mm/m |
| Anvil block | Hardwood block buried ≥1 m and tamped, with anvil iron on top (Chapter 18 forging, ≥60 kg) | Under heavy blows the anvil iron visibly jumps <3 mm; no radiating cracks in the ground around the block |
| Hammer head + hammer rod | First article may be chiseled from hard stone (chisel a wedge socket, band with iron rings); production parts in cast/wrought iron (Chapters 17, 18) | A stone hammer that loses an edge is scrapped; the iron hammer must ring clear when struck (no shrinkage cavities, Chapter 17 method) |
| Lifting mechanism | Cam strike-board type or water-wheel hook-claw direct-lift type (see below) | Full hand-turn check: hammer reaches position, releases cleanly, no double-strike |
| Safety and release | Over-top safety pin + foot-pedal release linkage | The pin must be inserted for any maintenance/pause; release pedal has 20–40 mm of dead travel |

**Two lifting mechanisms**:
- **Cam strike-board type**: on a camshaft (or directly on the water-wheel shaft) mount a pair of antler-shaped wooden cams (profile design per the Section 21.11 cam method); as they rotate they press down the hanging board at the tail of the hammer rod and lift the hammer head; past the cam's highest point the hammer disengages and falls freely to strike. Stroke is changed by swapping cams — large stroke for thick stock, small stroke for finishing.
- **Water-wheel hook-claw type**: hooks on the wheel rim directly catch a cross-pin on the hammer rod, lift it over top, disengage, and it drops. Fewest parts, but stroke and rhythm are locked to the water wheel (stroke ≈ rim height at the hook point; rhythm = wheel rpm × number of hooks).

**Over-top safety pin**: when the hammer rod is raised to its highest position, a person inserts an iron pin into the pin hole of the support beneath the rod and the hammer head hangs supported — maintenance, changing stock, long conversations, end of shift: **the pin goes in for all four situations**. Make the pin plate with two holes (the near hole supports the hammer head; the far hole carries the rod's own weight), and chain the pin to the frame so it cannot be lost. A drop hammer without its safety pin must never be left unattended (same discipline tier as the Section 21.5 rule of dropping the gate and hanging a tag for water-wheel maintenance).

**Foot-pedal release**: pedal → pull rod → catch pawl; the smith controls release timing by foot (turning the stock and aligning it are done while the hammer hangs). The linkage uses rigid links throughout, **never rope** — rope's elastic stretch makes release timing drift. The pedal is designed with **20–40 mm of dead travel**: pressing first traverses the dead zone, and only past it does the release act, preventing an accidental half-stroke press. ◎ Hand-feel: the craft of release lies in the "listen to the strike, turn the stock" rhythm — the instant the hammer note falls, turn the stock, and by the time turning is done the hammer is back; practice method: strike cold scrap 200 times with no work under it, drilling nothing but the turning rhythm, until turning with the hands while counting blows with the ears can both be done without error; compensation: nail a scale board beside the pedal so new workers check their press depth against the scale; remove the scale after two weeks.

**Blow-energy rough calculation**: E (J) ≈ 10 × hammer weight (kg) × drop height (m). Order-of-magnitude sanity check: 40 kg×1.2 m ≈ 480 J, roughly the single-blow energy of 3–4 sledgehammer operators taking turns. Note that drop height means the **actual free-fall distance from the release point to the anvil face** — if the cam keeps dragging the hammer rod after the release point, energy is discounted. Verify energy with the **lead-column comparison method**: with lead columns of one specification (φ20×30 mm), strike one with a hand sledge of known weight from a known height and one with the drop hammer under test; the ratio of compressed heights ≈ the ratio of energies (lead's plastic work is approximately proportional to compression — approximation, must be field-calibrated: first strike three columns with the same hammer to verify that compression repeats within ±10%, then compare the two hammers).

**Practice and acceptance (50 blows, two passes)**: no-load blows for 30 min (listen to the frame, watch the anvil block, feel the guide-bore temperature) → strike cold iron stock 50 blows → re-tighten the entire frame once (wedges, pins, footings) → strike 50 more → recheck. Acceptance criteria: **no loosening at any joint after the 50 blows** (mortise joints do not rock when pushed by hand, wedge faces do not sound dull when re-struck), hammer-rod guide-bore temperature bearable to the hand indefinitely, no visible offset of the hammer head from the anvil center.

[Card 21-05 Water-Powered Drop Hammer: Construction and Acceptance] (eight fields)

1. **Input materials**: fully dried hardwood — 4 posts + assorted beams and braces (about 1.5 m³ total, dried per the Chapter 7 monthly weight check); anvil iron ≥60 kg (Chapter 18 forging); hammer head in cast/wrought iron ≥30 kg (or hard stone ≥50 kg); iron hoops, wedge keys, and safety pin — ≥5 kg iron in total; footing stones.
2. **Tools required**: woodworking chisels, adze, auger (Chapter 7); plumb bob, spirit level, string line (Chapter 3); forging and casting (Chapters 17, 18); φ20×30 mm lead columns and a hand sledge of known weight (energy comparison). Calibration source: drop height measured as the actual free fall from the release point to the anvil face, not the cam stroke.
3. **Sequence and control points**: (1) set the footing stones (tamp until they do not sink underfoot; pit deeper than the local frost depth) → (2) raise the frame and plumb it (vertical ≤10 mm/m) → (3) bury the anvil block (≥1 m deep, tamped) → (4) fit the hammer rod and guide frame (guide clearance 3–5 mm per side; scrape-fit once after the wooden guides heat up) → (5) fit the lifting cam/hooks and hand-turn the full cycle (hammer reaches position, releases cleanly, no double-strike) → (6) fit the safety pin and pedal release (dead travel 20–40 mm) → (7) 30 min of no-load blows, three checks (frame sound, anvil-block jump, guide temperature) → (8) 50 blows on cold stock + re-tighten the whole frame → (9) 50 more blows for acceptance. Control point: **the over-top safety pin goes in for all four situations** (maintenance, changing stock, long conversations, end of shift).
4. **Empirical parameters and calibration**: drop height 0.8–1.5 m, stepped by stock thickness (set anvil-face height with blocking); rhythm 60–120 blows/min (count blows for 1 min and log; half-closing the gate lowers it); single-blow energy E ≈ 10×hammer weight×drop height (40 kg×1.2 m ≈ 480 J); guide clearance 3–5 mm per side; frame verticality ≤10 mm/m, post verticality change after no-load blows ≤5 mm/m; pedal dead travel 20–40 mm (◎, scale-board compensation). Calibration: strike three lead columns with the same hammer and confirm compression repeats within ±10% before comparing two hammers (empirical value, must be calibrated to local conditions).
5. **Observations to record**: the 30 min no-load three-check results / plumb-line verticality recheck every 50 blows / hammer note (dull = striking air or the stock shifted; crisp = solid) / "crack" from the frame / lead-column compression heights / which joints were re-tightened and by how much / blows per minute.
6. **Pass / rework / scrap criteria**: pass = 50-blow two passes with no joint loosened (mortise joints do not rock by hand, wedge faces do not sound dull when re-struck) + lead-column comparison meets the energy target + guide-bore temperature bearable to the hand + no visible offset of the head from the anvil center; rework = an individual wedge loose (drive it tight, then 50 more blows for extended observation); scrap = post cracked / anvil block displaced (redo the part; propping-up improvisation is not allowed).
7. **Common failures and diagnosis order**: (1) off-center blows (hammer-anvil misalignment — recheck by plumb line); (2) fails to release (hook-claw curve wrong — file to the template); (3) double-strike (release pawl slow to return — add counterweight); (4) frame gradually shaking (braces missing or wedges loose — stop, re-tighten, add bracing).
8. **L1 / L2 / L3 evidence**: L1 = no-load three-check record + 50-blow two passes on cold stock; L2 = lead-column comparison sample and 100-blow re-tightening record on file; L3 = a second person builds one from this card alone and passes acceptance.

### 21.10 Gear-Train Ratio Design and the Change-Gear Table

Section 21.2 set the "no stage above 1:5" discipline; this section provides look-up combinations so gearing is no longer improvised on the spot. **Minimum tooth count 12** (fewer, and the approximate tooth profiles interfere with each other); **prefer tooth counts of 12, 15, 16, 18, 20, 24, 30, 36, 40, 48, 60** — counts built from 2×3×5 factors, which the cord-wrapping dividing method (Chapter 3) divides most easily and with the least cumulative error.

Common-ratio change-gear table:

| Target ratio | Combination (driver z₁→driven z₂) | Use |
|---|---|---|
| 1:2 | 16→32, 18→36, 20→40 | Speeding up mills and saws; most common |
| 1:3 | 15→45, 16→48, 20→60 | Blast air |
| 1:4 | 15→60, 18→72, 20→80 | Large reduction |
| 1:5 | 14→70, 16→80 | Discipline ceiling; used only at the limit |
| 2:3 | 24→36, 30→45 | Fine-trim stage |
| 3:4 | 24→32, 30→40 | Fine-trim stage |

**Two-stage series example**: from the water wheel at 6 r/min up to the line shaft at 60 r/min, total ratio 1:10 — take 1:5×1:2 (14→70, 20→40) in two stages; a single stage may not swallow 1:10. Decomposition principle: **factor the total ratio into a product of factors each ≤1:5, and take every factor from the table's combinations**; efficiencies multiply through as well (Section 21.2); for two open gear pairs estimate 0.95² ≈ 0.90.

**Center-distance layout**: center distance of two gears = m×(z₁+z₂)/2. Lay out and bore the shaft brackets to this, making the holes slotted (leave ±2 mm of adjustment); after assembly apply marking compound and roll the pair (Section 21.1.1), inspect the contact patch, and fine-tune the center distance through the slots until it passes — **the center distance is grown into place, not scribed into place**.

**Reversing bevel gears (straight-tooth approximation)**: for a 90° shaft angle, use a pair of bevel gears with **equal tooth counts** to reverse the drive. Method:
1. Turn both blanks to their pitch cones, each with a half-cone angle of 45°;
2. Lay out using the **back-cone unfolding approximation**: on the unfolded back-cone surface, a bevel gear's teeth are approximately the tooth profile of a plane gear of the same tooth count — make one tooth-profile template by the Section 21.1.1 template method, bend it against the cone face at the large end, and lay out;
3. After chiseling and filing, apply marking compound, roll, and fit: the contact patch should sit **toward the large end** (bevel gears carry load concentrated at the large end), with clearance left at the small end to prevent binding;
4. Criteria: full hand-turning without binding; back-and-forth rock visually equal in both directions; backlash still by the paper-strip method (Section 21.1.1).
Bevel-gear ratio fluctuation is larger than that of cylindrical gears (±8% class, empirical value; must be field-calibrated: draw chalk lines on driver and driven, rotate together for 10 turns, and count the difference in driven revolutions) — **use only for reversing and low-speed stages**, never for indexing.

**Gear pairing regime**: stamp paired numbers on each gear pair (A-1↔B-1, continuing the Chapter 20 matched-and-numbered system); when worn out, **replace as a pair, never singly** — new teeth meshed with old inevitably worsen the contact patch, voiding the inspection.

### 21.11 Three Classes of Intermittent Mechanisms

To turn continuous rotation into intermittent motion, three basic classes in rising complexity: ratchet (easiest), cam (middle), escapement (hardest — registered only). The drop hammer's rhythm, the winch's anti-reverse, the feed's measure — all live in these three devices.

**1. Ratchet (hold-back/feed)**: a saw-toothed ratchet wheel + a swinging pawl. One swing of the pawl pushes the wheel through 1–3 teeth; on the return stroke the pawl slides back along the tooth backs and the wheel stands still; a second, hold-back pawl bears against the tooth backs so the wheel can only turn one way — winches, jacks, and machine feeds all rely on it for safety.

| Item | Parameter/method |
|---|---|
| Ratchet body | Cast (wooden pattern with the teeth formed directly, Chapter 17) or hardwood with chiseled teeth; 12–24 teeth |
| Tooth shape | Working face near-radial (the pushing face); back face at a steep ~45° angle (so the pawl slides back without effort) |
| Pawl | Forged iron, tip hardened (Chapter 19); **tip angle 45–60° — too blunt and it will slip teeth** |
| Pressing | A spring plate (bent from thick steel) or a weighted lever, constantly pressing the pawl toward the tooth roots |
| Acceptance | Hang 1/2 rated load and attempt to reverse: the wheel must not slip even half a tooth |

Feed-per-stroke rough calculation: each swing advances one circular pitch = π×D/z. Example: φ120 mm, 18 teeth → ≈21 mm per tooth — adequate for rough feed; for finer steps, add teeth, or reduce the pawl's swing with a lever (a 3:1 lever ratio → ~7 mm per tooth).

[Card 21-06 Ratchet Mechanism: Fabrication and Acceptance] (eight fields)

1. **Input materials**: ratchet blank (cast iron/hardwood) ×1; forged-iron pawls ×2–3 (1 in use, 2 spare); thick steel spring plate or weighted lever ×1 set; pawl pivot; a test weight of 1/2 the rated load.
2. **Tools required**: chisel, file (Chapter 7); forging and water quenching (Chapters 18, 19); angle plate and dividing tools (Chapter 3); oilstone; sling and weight for the reverse test. Calibration source: pawl tip angle checked against an angle gauge or template, not by eye.
3. **Sequence and control points**: (1) divide the rim and lay out the teeth (12–24 teeth, Chapter 3 dividing method) → (2) chisel the teeth: **back-face bevel first, working face last; the working face must not be beveled backward** (a backward bevel means the pawl cannot push or slips teeth) → (3) forge the pawls and quench only the 10–15 mm tip section → (4) fit the pawl pivot and pressing parts → (5) swing 100 times unloaded → (6) reverse test under 1/2 rated load. Control point: the chiseling direction on the working face and the length of the hardened tip.
4. **Empirical parameters and calibration**: 12–24 teeth; working face near-radial, back face at about 45°; pawl tip angle 45–60° (criterion); pawl swing = tooth pitch×1.5; advance per swing = one circular pitch = π×D/z (φ120, 18 teeth ≈21 mm; a 3:1 lever gives the 7 mm class per tooth); no slip of even half a tooth in reverse. Calibration: make three pawls at 45/52/60°, mount and compare; discard the dullest setting that slips teeth and enter the usable settings in the ledger (empirical value, must be calibrated to local conditions).
5. **Observations to record**: tooth-slipping sound (rapid clicking) / where the pawl tip is polished (back = normal sliding return, working face = insufficient pressing) / tip curling after 100 swings / slip amount and load step in the reverse test / three-pawl angle comparison result.
6. **Pass / rework / scrap criteria**: pass = no slipping under the loaded reverse test + no tip curling after 100 swings; rework = regrind the tip angle (file + oilstone) and retest; scrap = crack in the pawl body (reforge and requench).
7. **Common failures and diagnosis order**: (1) slips teeth in reverse (tip too blunt → insufficient pressing → working face chiseled backward); (2) drags the wheel on the return stroke (back-face angle too small — increase it); (3) loose pawl pivot (swing direction wanders — re-bore and fit a new pivot).
8. **L1 / L2 / L3 evidence**: L1 = one ratchet passing the 1/2-load reverse test; L2 = reverse-test record plus the pawl-angle setting ledger on file; L3 = a second person makes one from this card alone and meets the standard.

**2. Cam (field-expedient design of the motion-time curve)**: a cam = a wheel with the "desired motion timetable" carved into its profile; the follower (a roller or a flat plate) rides the profile — however high the profile, that far it travels. **Wooden cam template method**, five steps:
1. **Tabulate the motion**: horizontal axis = cam angle 0–360°, vertical axis = follower travel. Example: 0–120° rise 100 mm (pressing the hammer / pushing a plate), 120–200° dwell (holding pressure / clearing stock), 200–360° return (spring or weight return);
2. Draw the base circle (leave ≥20 mm of margin for a flat-face follower at the smallest radius);
3. Draw radial lines at 15° or 30° divisions (Chapter 3 dividing method; the finer the division, the truer the curve);
4. Mark on each radial the travel corresponding to that angle and connect the points into a smooth curve with a French curve/flexible rule — **no kinks allowed in the rise segment** (a kink = a sudden change of follower velocity = a shock source; wear there doubles, empirical value);
5. Saw the curve into a thin board and file it smooth: that is the **wooden cam template**; then copy it onto the cam blank (wood/cast iron) by laying out from the template.
Criteria: the template and the follower mate over the full travel (light-gap check ≤0.5 mm); mount the cam, rotate it one turn with a scribe fixed to the follower drawing on paper, compare against the design curve, deviation ≤1 mm (empirical value, must be field-calibrated: if "the template passes but the traced circle is out," the difference is the assembly eccentricity — adjust the center and retrace, and enter the calibration conclusion in the ledger). Applications: drop-hammer lifting rhythm (Section 21.9), reworking the bellows push-pull rhythm (Chapter 12), counting and alarm triggering.

**3. Escapement (the seed of timekeeping)** [background/outlook]: escapement wheel + pallet fork + pendulum, cutting the gear train's continuous torque into equal, isochronous drops — the heart of a clock. At this manual's present stage, a clock-grade escapement cannot be manufactured (it needs hardened precision grinding and a stored-energy mainspring, beyond this chapter's capability), so **register the requirement; do not open the project**; timekeeping currently uses the Chapter 3 water clock and sundial. The upgrade hook left behind: if the gear trains (this chapter) and the lathe (Chapter 20) both reach L3, and the shift regime and astronomical observation genuinely require stable timekeeping, re-evaluate starting from the anchor escapement — the escapement is the "farthest downstream" of this chapter's gear trains, not this chapter's task.

### 21.12 Flywheel Energy Storage and the Burst Red Line

A flywheel = a rotating reservoir: machines that "eat large amounts of energy intermittently" — forge hammers, punches and shears, reciprocating pumps — use the flywheel to store the non-working phases' work into rotation and release it in the working instant (Section 21.5 mentioned flywheels smoothing second-scale fluctuation; this section gives the arithmetic and the red line).

**Storage rough calculation**: E (J) ≈ ½×m×v². Count only the **heavy rim** (the mass of the iron hoop or rim ring, kg) — spokes and hub contribute little; ignore them in the rough calculation; v = rim linear speed (m/s) = π×D×n/60. Order-of-magnitude sanity check: iron hoop 60 kg, v = 10 m/s → E ≈ 0.5×60×100 = 3000 J, about 6 blows of 480 J each (consistent in order of magnitude with the Section 21.9 single-blow energy).

**Fluctuation discipline**: an energy draw ΔE per blow causes a speed drop Δv/v ≈ ΔE/(2E). Requiring ≤10% speed drop per blow gives **E≥5×ΔE — flywheel storage should be ≥5× the energy consumed per working stroke** (design discipline). Calibration method: draw a chalk line on the rim and count revolutions for 10 seconds before and after the blow; if the drop exceeds 10%, add rim weight or reduce blows per minute.

**Burst red line**: a flywheel's stored energy all becomes tangentially flying fragments at the instant of bursting, and cast iron fractures without warning. Why cast iron is speed-limited: a rotating rim is under centrifugal tensile stress; cast iron is weak in tension, and at excessive rim speed it bursts from the spoke roots or from **shrinkage cavities** — a shrinkage cavity is a crack source (the Chapter 17 "rings clear when struck" acceptance is a life-saving item here, not a formality).

| Wheel type | Rim linear-speed red line | Note |
|---|---|---|
| Wooden wheel (mortised rim) | ≤20 m/s | Empirical value; enter in the ledger after field calibration |
| Cast-iron wheel | ≤25 m/s | Same; take the lower bound for large diameters |
| Wooden wheel + hot-shrunk iron hoop | Managed at ≤20 m/s | **Preferred structure**, see below |

Red-line calibration method: for the first article of a new wheel type (not installed on a production machine), spin it unloaded, raising speed stepwise to 1.15× the red line; if 10 min of monitoring shows no abnormal noise and the post-stop inspection shows no cracks, the red line is approved; clear the area for the test, and stand **off the tangent** of the wheel's plane (fragments fly along tangents — never stand on a tangent). After installation the line must never be exceeded under any circumstance; recompute the linear speed with v = π×D×n/60 whenever fitting a belt pulley — **changing the pulley = changing the linear speed**; every pulley change must be recomputed, and the recomputed value written on a spoke.

**Why the wooden flywheel + iron hoop is preferred**: a fully cast iron wheel bursts with no warning; a segmented mortised wooden rim with a peripheral hot-shrunk iron hoop lets each material do what it does best — the iron hoop takes the centrifugal tension (metal is strong in tension), the wooden spokes take bending (wood's bending strength suffices); moreover, a failing wooden wheel first creaks audibly and shows visible cracks (good warning behavior, which brittle cast iron lacks). Large-diameter low-speed flywheels at the line-shaft end always prefer this structure; cast-iron flywheels are reserved for small-diameter high-speed stations, and each is individually sound-tested by striking. Acceptance of the iron hoop itself: after hot-shrinking and cooling, strike and listen for a solid sound, and a knife tip cannot be inserted between hoop and rim (if it can = loose; re-heat and re-shrink).

**Static balancing (mandatory before installation)**: rest the flywheel on two horizontal knife-edge rails and spin it; if it always stops at the same angle, the heavy side hangs at the bottom; remove weight opposite the heavy side (bore holes in a wooden wheel and plug with lead; locally chisel/file a metal wheel) until it stops at any angle. An unbalanced wheel is strictly forbidden on high-speed shafts (the Safety Boundary section has already set the Iron Law; this is the ground-level method).

### 21.13 Pump and Valve System (universal fluid-machinery components, closing gap C5)

Piston pump (single-acting): pump body (cast iron/hardwood cylinder with a honed bore — per the Chapter 28 cylinder process) + piston (leather-cup seal) + a pair of check valves. **The check valve is the pump's soul**: the flap valve (hinged, for low-pressure water) and the conical-seat valve (lapped seal, per Chapter 28, for medium pressure). Criterion: if the pump "sucks but will not deliver," check the outlet valve first; "delivers but will not suck," check the inlet valve first — this valve-order diagnostic goes into the failure-modes table. Suction lift's physical ceiling ≈8 m (atmospheric pressure); deep wells use two stages in relay (per Chapter 28). Stop valves: the plug valve (lapped tapered plug, per the Chapter 22 taper-pin process) and the gate valve (flat sliding plate), two types; pipe standardization: ceramic pipe bell-and-spigot joints (Chapter 11) + oakum sealing, a three-step pipe-diameter series (25/40/60 mm, same family as the Chapter 12 anemometer). [Process Card 21-07 Check-Valve Fabrication and Pressure Test] key point: pressurize in reverse at 1.5× working pressure; no back-leakage = pass.

**Capability boundary: this edition builds positive-displacement pumps only, never centrifugal pumps.** A centrifugal pump throws water outward with an impeller, and lift grows with speed — which demands accurately cast twisted blades, a rotor that has been dynamically balanced, and a clearance between impeller and volute measured in fractions of a millimeter. All three sit outside what Chapter 21 can deliver, and at this stage's power levels (waterwheel, animal, human, mostly in the hundreds of rpm) a positive-displacement pump wins on both efficiency and reliability. Therefore:

- **Small flow, higher lift** (raising water from a well, irrigating high fields, feeding a boiler) → piston or diaphragm pump, section 21.13;
- **Large flow, low lift** (irrigating broad fields, drainage) → not a pump: use a scoop wheel, a waterwheel lifting directly, or a gravity canal (Chapter 29);
- **Silty water** (mine drainage, muddy streams) → diaphragm pump first; a piston's leather cup is cut through by grit. A worn cup shows as falling output with no leak in the body.

This boundary is written down so that no one later treats "there is no centrifugal pump in the book" as a gap to be forced. By the time a centrifugal pump is genuinely needed, the prerequisite is a machine tool that can balance a rotor and a foundry that can cast thin twisted blades — and that is no longer Chapter 21's problem.

## Master Parameter Table

| Parameter | Value | Class |
|---|---|---|
| Base-circle coefficient | ≈0.94×pitch circle (20° pressure angle) | Design approximation |
| Tooth tip clearance | 0.2×m | Empirical |
| Meshing contact patch | Centered on the flank, ≥1/3 of tooth height | Criterion |
| Tooth backlash | 0.05–0.15 mm (paper-strip method) | Empirical |
| First-generation gear ratio fluctuation | ±5% class | Honest boundary |
| Single-stage ratio limit | 1:5 | Discipline |
| Bush crown clearance | 1–1.5‰ of shaft diameter (lead-crush method) | Empirical |
| Bearing temperature-rise red line | ≈60 ℃ | Empirical |
| Belt deflection | 10–20 mm; full-load slip <2% | Criterion |
| Water-wheel power | P≈1000×Q×H×η; η by the three types | Estimation |
| Line shaft above floor | ≥2.5 m | Discipline |
| Radial runout (water-wheel shaft) | ≤0.5 mm | Empirical |
| Drop-hammer single-blow energy | E≈10×hammer weight×drop height (J) | Estimation |
| Drop-hammer release pedal dead travel | 20–40 mm | ◎ hand-feel (scale-board compensation) |
| Hammer-rod guide clearance (per side) | 3–5 mm | Empirical |
| Minimum tooth count | ≥12 | Discipline |
| Bevel-gear ratio fluctuation | ±8% class | Honest boundary |
| Ratchet pawl tip angle | 45–60° | Criterion (three-pawl comparison calibration) |
| Cam rise segment | No kinks; traced-circle deviation ≤1 mm | Discipline + empirical |
| Flywheel storage multiple | E≥5×energy per stroke (speed drop ≤10%) | Discipline |
| Rim linear-speed red line | Wood ≤20 m/s, cast iron ≤25 m/s | Empirical (calibrated by overspeed test) |

## Failure Modes and Diagnostics

| Symptom | Candidate causes (by probability) | Verification | Remedy |
|---|---|---|---|
| Bearing heats rapidly | Clearance too small; blocked oil groove; dirty oil | Lead-crush recheck; inspect oil | Reshim and reset; clear the groove; change oil |
| Shaft polished bright on one side | Shaft system misaligned | String-line method | Move the bearing housing and realign |
| Loud periodic gear noise | Large pitch error; improper backlash | Marking-compound roll recheck | Dress the teeth; adjust center distance |
| Rapid tooth-face wear | Contact patch toward tip/root; no oil | Marking-compound recheck | Correct the tooth profile; lubricate |
| Full-load slip | Insufficient tension; glazed belt face; small wrap angle | Chalk slip method | Tension / wax / add a tension pulley |
| One knock per revolution | Loose key | Hand-turn and locate by ear | New key, matched and numbered |
| Water-wheel output decaying season by season | Channel silting; worn paddles; leaking gate | Flow retest against the archive | Dredge / replace paddles / repair the gate |
| Runaway (load suddenly dropped) | No governing — the wheel gate not lowered in step | Observation record | Machine-attendant regime + shed load stepwise |
| Drop-hammer frame gradually shaking | Loose tenons/wedges; missing braces; footing stones untamped | No-load-blow watch + plumb-line recheck; push the mortise joints | Stop, drive the wedges, re-tighten; add bracing; redo the footings |
| Pawl tip chipping / reverse slipping | Tip angle too blunt; tip not hardened; insufficient pressing | Measure the tip angle; file-test hardness; check the pressing parts | Regrind or replace the pawl and requench; add counterweight |
| Flywheel noise gradually worsening | Poor static balance; loose iron hoop; rim crack | Knife-edge static-balance recheck; sound-test the hoop by striking; inspect the rim for cracks | Stop, remove weight, rebalance; re-shrink the hoop; scrap a cracked wheel |

## Process Card Index

## Acceptance Standards

- **L1**: a gear pair's marking-compound rolled contact patch meets target; the crank-connecting-rod assembly hand-turns smoothly through the full cycle; the water wheel runs wet with output measured (force-measuring method) and recorded.
- **L2**: a line-shaft workshop with ≥3 stations runs continuously for a full day; measured transmission efficiency ≥70% of the estimate; bush lead-crush records and temperature-rise records on file; chalk slip-method acceptance performed.
- **L3**: all four wear parts — bushes, keys, belts, gears — can be remade in this workshop (mother-machine closed loop); water-wheel winter maintenance institutionalized; quarterly power retests do not decay by >10%; the inspection checklist merges into the Chapter 39 regime. Evidence: inspection records, output-retest curves, spares ledger.

## Work-Hours, Manpower, and Consumption

| Item | Manpower | Work-hours (empirical values) |
|---|---|---|
| A pair of wooden gears (layout + chiseling/filing) | 2 people | 3–5 days |
| Scraping one pair of bearing bushes | 1 person | 1 day |
| One water wheel (incl. channel and gate) | 6–10 people | 30–60 days (civil works take half) |
| Line-shaft workshop (3 stations) | 4 people | 15–25 days |
| Consumption | Grease every shift, belt wax, timber | Enter in the Chapter 38 ledger |

## Safety Boundary

- Line shaft and belts: guard rails + belt crossover bridges; **removing or fitting belts while running is strictly forbidden (use the belt-shifting fork)**; sleeves bound tight (Iron Law Seven).
- Water wheel: maintenance requires first dropping the gate, cutting the water, and hanging a tag.
- Flywheels: overspeed strictly forbidden (flywheel burst energy is lethal); unbalanced wheels strictly forbidden on high-speed shafts.
- Water-powered drop hammer: an over-top safety pin is mandatory whenever the hammer head is raised.
- Fit wooden guards over gear-mesh zones; before maintenance, disengage the clutch fork and hang a tag.

## A. Existing Tools List

Woodworking and mortise-and-tenon joinery (Chapter 7); casting/forging/bronze (Chapters 17, 18, 19); lathe, scraping, three-plate lapping (Chapter 20); leather and fabric (Chapter 15); measurement and archive regime (Chapters 3, 4).

## B. New Tools Introduced in This Chapter

Shaft-system inspection procedures (radial runout / string-line alignment); keyed-joint specification; **gear layout approximation method (with the tooth-template regime) and marking-compound meshing inspection**; crank-connecting-rod assembly; **bush scraping + lead-crush clearance measurement** and the lubrication regime; the three water-wheel types and the siting power formula; windmill and furling protection; line-shaft workshop layout and clutch forks; **belt tensioning and the chalk slip-rate method**; the wear troubleshooting table and the daily/weekly/annual inspection regime; **the water-powered drop hammer (forging timber frame + safety pin + foot-pedal release, with the lead-strike energy comparison method)**; **the ratio change-gear table and bevel-gear reversing (back-cone unfolding approximation, paired-numbering regime)**; **intermittent mechanisms: the ratchet (hold-back/feed) and the wooden cam template method (escapement registered, not opened)**; **the flywheel storage arithmetic, rim linear-speed red lines, and the knife-edge static-balance method**.

## C. Unresolved Dependencies

Rolling bearings and higher speed limits (grinding capability, long-term); steam power (Chapter 28); batch precision finishing of metal gears (partially mitigated in Chapter 22); precision-indexing gears (bridged by the matched-selection regime).

## Next-Step Dependencies

Chapter 28: the steam engine's crank, flywheel, and bearings directly reuse this chapter's specifications. Chapter 29: the power-choice framework takes this chapter as its baseline. Chapters 31–32: the generator shop is the line-shaft workshop plus electrical stations. Chapter 12: water-powered blast feeds back into metallurgy. The Part 10 environment editions: the water wheel/windmill are the first power routes for the rainforest, island, and desert editions. Chapter 39: the annual inspection merges into the inspection-checklist regime.
