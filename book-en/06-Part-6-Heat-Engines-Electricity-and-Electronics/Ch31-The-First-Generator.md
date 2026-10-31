# Chapter 31 The First Generator

## Chapter Goals

Achieve the continuous conversion of mechanical work → electrical energy: master the principle of electromagnetic induction, conquer electricity's hidden bottleneck—**bulk drawing of insulated copper wire**—establish the manufacturing system of magnets, iron cores, coils, and the commutator, build a hand-cranked generator and connect it to a water wheel for continuous supply, complete the electrolytic calibration of current, and run through the bootstrap loop of "using the first generator to build a better second one."

**Honest boundary (stated at the outset)**: measuring a voltage ≠ establishing a power industry. Continuous supply still requires insulation, conductors, bearings, speed regulation, protection, maintenance, and load management—that is the entire territory of Chapter 32.

## Capability Boundary

**Can do:** rotating-magnet → self-excited generators; a drawing–insulation–winding production line; troubleshooting "spinning but no power" by the table; continuous supply at the hundred-watt–kilowatt level (empirical values, must be field-calibrated).

**Explicitly cannot do:** AC instruments and wattmeters (listed under C); storage batteries at scale (lead–acid requires more sulfuric acid and lead-plate engineering); high-voltage insulation and long-distance transmission (Chapter 32); precision measurement of megohm-level insulation resistance—this chapter has only two rough field methods, **leakage-current rough testing + the withstand-voltage test** (see Section 31.4.3).

**External dependencies:** continuous prime power (water wheel / steam engine, Chapters 21/28) and a dedicated machine attendant (the meter-reading system, Iron Law 7).

## Pre-Work Verification (Check Off One by One)

| # | Verification item | Criterion | Source |
|---|---|---|---|
| 1 | Electromagnet and galvanometer | The galvanometer can reliably detect the order of magnitude of a single cell's short-circuit current | Chapter 30 |
| 2 | Drawing dies | Hardened-steel dies with ≥4 aperture stages (3→1 mm class); smooth conical die mouth (no chipping visible at 10x magnification) | Chapters 19, 20 |
| 3 | Micrometer | For measuring wire diameter; zeroed | Chapter 22 |
| 4 | Insulating varnish | Boiled from shellac/rosin + drying oil; brushed on a copper rod and dried, it does not conduct under the spark test | Chapters 8, 23 |
| 5 | Lathe and bearings | Rotor journal roundness ≤0.05 mm; bearings run free ≥10 min with acceptable temperature rise | Chapters 20, 21 |
| 6 | Copper stock | Copper rod ≥2 kg, surface free of oxide scale (pickled or sanded) | Chapters 17–18 |
| 7 | Drive | Water wheel / line shaft with step-pulley speed control; belt slip <2% | Chapter 21 |
| 8 | Recording system | Meter-reading logbook and winding record sheets in place | Chapter 25 |

---

### 31.1 The Principle of Electromagnetic Induction

**The Faraday experiment (reproducible with Chapter 30's equipment alone)**:
1. Connect a galvanometer across the coil's two ends; thrust a bar magnet in quickly—deflection; hold it still inside—return to zero; pull it out—deflection in the opposite direction;
2. Conclusion: **a changing magnetic flux induces a voltage in the coil**; the key is "changing"—a constant magnetic field generates nothing;
3. All three kinds of change work: magnet moves, coil moves, field strength changes;
4. Induced voltage ∝ rate of change of flux—**strong magnet, many turns, fast rotation** are the three essentials of a generator.

### 31.2 Conductor, Magnetic Field, and Relative Motion

- **Rotating-magnet type**: permanent magnet bars rotate, stationary coils sense—the simplest structure, with no leads and no brushes on the rotor (on the excitation side); drawbacks: the magnet's weight rides on the rotor and speed is limited;
- **Rotating-coil type**: coils rotate in a fixed magnetic field—the modern route, but it requires slip rings / a commutator;
- The first machine uses the **rotating-magnet type + stationary coils**: reduce the electrical complexity to a minimum and secure a stable first power source first.

### 31.3 Making Magnets, Iron Cores, and Coils

**The magnet bootstrap dilemma and its solution**: a large electromagnet needs a large magnetizing current, and a large current needs a generator—a dead loop. Solution sequence (the bootstrap chain):
1. Magnetize steel rods with natural lodestone (Chapter 16) → small permanent magnets;
2. Fit the small permanent magnets into the first small generator (rotating-magnet type) → the first stream of continuous current;
3. Use that current to excite a larger electromagnet → magnetize larger steel parts → stronger permanent magnets → a larger generator;
4. Amplify the loop until the self-excited generator comes within reach (residual-magnet build-up—a bootstrap route that genuinely occurred in engineering history).

[Card 31-01 Magnetizing and Residual-Magnetism Recovery] (eight fields)

1. **Input materials**: high-carbon steel parts awaiting magnetization (hardened state); an excitation coil (as many turns as possible, wire diameter ≥1 mm); a battery bank (several voltaic piles in series, Chapter 30); a standard magnet (the attraction reference).
2. **Tools required**: coil and battery-bank leads; dry gloves (one-hand working habit, see the safety boundary); a tray of iron nails (attraction counting); the magnet archive book. Pre-use calibration: count and register the standard magnet's nail pickup first — it is the denominator of the "ninety percent" criterion.
3. **Operating sequence and control points**: place the steel part in the coil along its axis → energize → hold a few seconds → break, **repeating 5–10 times always in the same direction** (reversal = demagnetization) → measure attraction immediately after magnetizing (compare the nail count against the standard magnet) → register in the magnet archive. Control points: axial placement; the same direction every time, never reverse mid-run; take the part out only after the break.
4. **Empirical parameters and calibration**: 5–10 make-break cycles (empirical values, to be calibrated to local conditions); pass line = attraction reaching ninety percent of a comparable standard part (empirical criterion, the standard's nail count registered first); the retest interval follows the decay observed — magnetism decaying within days means the steel was never hardened.
5. **Process observation and recording items**: part number and steel grade; hardening date; coil turns and wire diameter; battery-bank series count; make-break count and direction; nail count (part / standard); retest date and amount of decay.
6. **Pass / rework / scrap criteria**: pass = attraction reaches ninety percent of a comparable standard part. Rework = short of ninety percent: re-magnetize in reverse (first demagnetize with reverse make-break, then magnetize forward). Scrap = the steel's carbon content is too low (soft iron will not hold magnetism; switch to high-carbon steel).
7. **Common failures and troubleshooting order**: (1) no magnetism after magnetizing (first check for insufficient current → add battery banks → if still nothing, the steel grade is wrong); (2) weaker each cycle or polarity reversed (the direction was changed mid-run, which demagnetizes); (3) magnetism decaying within days (the steel was never hardened — switch to hardened parts).
8. **L1 / L2 / L3 evidence**: L1 = one part magnetized with its attraction registered; L2 = the attraction comparison record (part and standard nail counts) in the magnet archive; L3 = the retest interval in the inspection checklist, so monthly decay is traceable.

**Iron core (field shoe)**: turn a soft-iron forging into a horseshoe / C shape; scrape the two pole faces flat and parallel; **make the pole-shoe area as large as possible** (a short, wide flux path); laminations against eddy currents are a Section 31.10 upgrade.

### 31.4 Coil Winding and Insulating Materials (Electricity's Hidden Bottleneck)

#### 31.4.1 Wire Drawing (The Birth of Copper Wire)

1. Drawing dies: drill holes in hardened steel plate—the hole is conical (large entrance, small exit); the aperture series runs from 3 mm down below 1 mm in steps, each step reduced by 10–20% (empirical value);
2. Drilling and the cone: a small-hole drill + a hardened steel needle to lap the hole wall (fine abrasives, Chapter 9); register each aperture by "how snugly a known wire passes through";
3. Drawing: point one end of the copper rod, thread it through the die, grip with tongs, and pull with a winch; **lubrication**: soap solution / grease; **anneal once at every die step** (dull-red heat, Chapter 18) to prevent brittle breaks;
4. Wire gauge system: die number = wire number; register wire diameters measured with the micrometer into a table—the wire-selection table mapping **thick wire for long-distance transmission, fine wire for coils** is built on it.

Three checks for drawing failures: broken wire (insufficient annealing or a chipped die hole—inspect the die at 10x magnification); grooves on the wire surface (the die hole has worn grooves—move to the next die or re-lap); uneven wire diameter (unsteady drawing speed—the winch must run at even speed, by feel ◎; compensation: caliper-gauge spot checks every meter).

[Card 31-05 Wire Drawing and Annealing] (eight fields)

1. **Input materials**: copper rod (≥2 kg, surface free of oxide scale, pickled or sanded); hardened-steel drawing dies, ≥4 aperture stages (3→1 mm class); soap solution / grease lubricant; annealing fuel (Chapter 18).
2. **Tools required**: winch and tongs; pointing tool; micrometer (Chapter 22, zeroed); 10x magnifier (die-mouth chipping); annealing furnace; caliper gauge (per-metre spot checks). Pre-use calibration: zero the micrometer; register each die aperture by "how snugly a known wire passes through".
3. **Operating sequence and control points**: point one end of the rod and thread the die → grip with tongs, pull with the winch (even speed, by feel ◎) → lubricate (soap solution / grease) → draw one stage → **anneal once (dull red, Chapter 18)** → change to the next die, each stage reducing 10–20% → register the diameter with the micrometer, die number = wire number, and build the wire-gauge table. Control points: **one anneal at every stage, never skip one (a skipped anneal means a brittle break)**; even winch speed (the source of uneven diameter); inspect every die at 10x for a chipped mouth before use.
4. **Empirical parameters and calibration**: 10–20% reduction per stage (empirical values, to be calibrated to local conditions; set the steps from the first coil's break rate and diameter deviation); anneal color = dull red (Chapter 18); every diameter is measured with the micrometer and registered — never inferred from the die number.
5. **Process observation and recording items**: copper batch number; die-number sequence and each aperture's registered size; annealing date and fire color per stage; per-metre caliper spot-check values; break count and fracture appearance; finished diameter and length.
6. **Pass / rework / scrap criteria**: pass = diameter within the stage tolerance + a clean groove-free surface + no dead cracking when bent. Rework = uneven diameter (slow the pull and redraw, or drop one die size and redraw). Scrap = a brittle fracture face (that length was under-annealed: cut it off and redraw) or a surface groove too deep to reassign to a finer duty (back to the furnace; it does not enter a winding).
7. **Common failures and troubleshooting order**: (1) wire breaks (first check that every stage was annealed → then inspect the die mouth at 10x for chipping); (2) grooves on the wire surface (the die hole has worn a groove → move to the next die or re-lap); (3) uneven diameter (unsteady pull → even winch speed, per-metre caliper checks).
8. **L1 / L2 / L3 evidence**: L1 = one coil drawn and a "die number – diameter – resistance" table produced; L2 = 100 m of 1.5 mm wire (annealing included) completed at the labor-table unit, with spot-check records on file; L3 = the wire-gauge table becomes the basis of wire selection (coarse for long spans, fine for coils), and die lapping / die-change intervals enter the inspection checklist.

#### 31.4.2 Slot Insertion, Binding, and Varnish Dipping (The Winding's Mechanical Life Is Decided Here)

A coil is not done merely by being "wound on"—the centrifugal force and vibration of the spinning rotor will fling loose turns about and chafe through their insulation. Procedure:

1. **Slot insulation**: line the core slots first with oiled paper / varnished cloth (Chapters 10, 15), folded over at both ends to protect the slot mouth—**copper wire must never touch iron directly**;
2. **Slot insertion** (feel ◎): press the coil into the slots turn by turn / bundle by bundle with a bamboo or hardwood packing board; **never strike the wire directly with an iron tool** (a pierced skin means an interturn short); insert the bottom layer first, lay interlayer insulation paper, then insert the top layer;
3. **Slot wedges**: drive bamboo wedges into the slot mouths to press the turns tight (loose = wear and short circuits after days of running);
4. **End-winding binding**: bind the coil's two ends that project from the core (the end windings) densely to the frame / binding rings with grease-soaked hemp cord—the lashing runs perpendicular to the turns, one knot every 5–10 turns; the end windings see the largest centrifugal force, **an unbound end winding = a time-delayed short circuit**;
5. **Varnish dipping and hardening**: immerse the whole winding in warm, thin insulating varnish, lift it out to drain, and dry it (half a day in the residual-heat zone by the furnace mouth)—the varnish cements the turns into a hard mass that resists chafing and moisture. Test continuity and leakage once before and once after dipping to confirm the dipping did no harm.

[Card 31-02 Winding Slot Insertion, Binding, and Varnish Dipping] (eight fields)

1. **Input materials**: qualified enameled / cotton-covered wire (spot-checked by the spark method); slot insulation paper (oiled paper / varnished cloth, Chapters 10, 15); interlayer insulation paper; bamboo wedges; grease-soaked hemp cord; insulating varnish (Chapters 8, 23, warm and thin).
2. **Tools required**: bamboo or hardwood packing board (pressing the wire, **never strike the wire with an iron tool**); scissors; dipping tank and drain rack; drying spot (the residual-heat zone at the furnace mouth); galvanometer + battery bank (continuity and leakage retest before and after dipping, Section 31.4.3). Pre-use calibration: spark-method spot check of the wire; leakage rough test per Section 31.4.3 (battery bank ≥3× operating voltage in series with the galvanometer).
3. **Operating sequence and control points**: slot insulation (folded over at both ends to protect the mouth; **copper wire must never touch iron**) → insert the bottom layer → lay interlayer insulation paper → insert the top layer (pressed in with the wooden board, no iron tool on the wire) → drive the bamboo wedges (a solid, not hollow, tap) → bind the end windings (perpendicular to the turns, one knot every 5–10 turns) → dip (immersed in warm thin varnish, drained, dried half a day in the furnace-mouth residual heat) → test continuity and leakage once before and once after dipping. Control points: interlayer paper is mandatory; wedges driven tight; **an unbound end winding is a time-delayed short circuit**; always retest before and after dipping.
4. **Empirical parameters and calibration**: one knot per 5–10 turns on the end windings (procedure); slot insulation = oiled paper / varnished cloth with copper never touching iron (hard rule); drying = half a day in the furnace-mouth residual-heat zone (empirical); leakage rough test = battery bank ≥3× operating voltage in series with the galvanometer, no deflection or a slight one passing; withstand voltage = 2× operating voltage for 1 min (hard rule). These are empirical values, to be calibrated to local conditions.
5. **Process observation and recording items**: any pierced insulation during insertion (local black spots / exposed copper); the wedge tap sound; the number of end-winding knots and their spacing; whether the varnish film covers evenly; continuity and leakage readings before and after dipping.
6. **Pass / rework / scrap criteria**: pass = continuity normal + leakage rough test passed + the end turns cannot be pushed by hand. Rework = local insulation puncture (strip, re-insulate, re-bind). Scrap = interturn short (unwind and rewind; the wire can be reclaimed).
7. **Common failures and troubleshooting order**: (1) insulation pierced during insertion (an iron tool was used on the wire → press in with the wooden board); (2) abnormal temperature rise after days of running (end-winding chafing short → re-dip and re-bind); (3) the slot wedge pops out (it was not driven tight); (4) leakage worse after dipping (moisture not driven out → back to the furnace for a supplementary bake and retest).
8. **L1 / L2 / L3 evidence**: L1 = one winding completing insertion, binding, and dipping with continuity and leakage retested; L2 = the winding record sheet (turns / wire diameter / measured DC resistance) + the dipping record in the machine archive; L3 = the withstand-voltage and leakage retests adopted as the winding release criteria, with dipping records under annual archive review.

#### 31.4.3 Rough Field Acceptance of Insulation (In an Age Without a Megger)

- **Leakage-current rough test**: a battery bank (≥3x operating voltage) in series with a galvanometer, one end to the winding and the other to the core—no deflection or a slight one means leakage passes; a clear deflection = damp (dry out and retest) or broken insulation (locate and patch);
- **Withstand-voltage test**: on new and repaired windings, apply 2x operating voltage for 1 min with no breakdown and no smoke—only a pass allows installation;
- Extra tests in the wet season: always test leakage before starting up after rain (moisture is the leading cause of insulation breakdown; fuse linkage in Chapter 32).

### 31.5 Mechanical Drive and Rotor Structure

- Rotor (rotating-magnet type): steel shaft + permanent magnets fastened (keyed); **dynamic balance**: the static balance test (it stops at any position on knife edges) must pass, or high-speed vibration will destroy the bearings;
- Bearings and speed: plain bearings + oil-slinger-ring lubrication; count speed by the tripping tab clicker (Chapter 25);
- Drive: water wheel / steam engine via belt step pulleys for speed control—**speed regulation is the first gate of voltage stability**: speed fluctuation = voltage fluctuation.

### 31.6 How to Measure Output Voltage and Current

- **Galvanometer upgrade (moving-coil type)**: a light coil (of self-made enameled wire) sits between the pole shoes of a horseshoe permanent magnet; current through the coil deflects it, and hairsprings (Chapter 27) restore it—the moving-coil meter merges with the Chapter 27 pointer-mechanism craft;
- **Current calibration (the electrolytic copper method)**: copper-salt electrolytic cells in series; the cathode's weight gain per unit time (on a balance) = the absolute scale of current; the **copper coulometer** becomes the local current standard;
- Voltage measurement: standard resistance wire + conversion from current readings (the Ohm relation, Chapter 30).

### 31.7 DC and AC Generation

- The rotating-magnet type naturally outputs **alternating current** (the magnetic poles pass the coil alternately);
- **Commutator**: copper half-rings on the rotor shaft, the coil's two ends joined to the two halves, stationary carbon brushes touching them alternately—current direction in the external circuit stays constant (pulsating DC); several coil sets + a multi-segment commutator (Section 31.10) smooth the pulsation;
- DC suits electrolysis, electroplating, battery charging, and simple lighting; **a transformer works only on AC**—step-up long-distance transmission depends on AC; the dispute between the routes goes to Chapter 32.

#### 31.7.1 Making and Bedding In Carbon Brushes (Consumables, Made Locally)

- **Formula (empirical starting point, must be field-calibrated)**: graphite powder (natural graphite ore, or dense hardwood charcoal ground and passed through a fine sieve) 70% + copper filing powder (copper filed and sieved) 25% + binder (shellac varnish or thick syrup / dextrin) 5%; knead into a dough, press into blocks in a wooden mold, shade-dry, then dry in the residual heat at the furnace mouth, then bury in charcoal embers and slowly burn to red heat (sintering improves conductivity)—inspect the finished brush on both resistance and hardness: a brush of the same size should show clearly lower resistance than a pure charcoal block (series galvanometer comparison), and a fingernail should leave a shallow mark without crumbling or powdering;
- **Bedding in (mandatory order)**: after fitting a new brush, wrap fine sandpaper around the commutator (grit face toward the brush) and work the brush back and forth under hand pressure 20–30 times—the brush face takes on the concave arc that matches the commutator; after bedding in, run 30 min unloaded before loading;
- Brush pressure: spring-press until "the brush body will not slide down out of the holder, yet can be pushed by feel" (empirical; calibration method: the twin indicators of sparking and brush temperature—big sparks = too little pressure; a hot brush = too much);
- Life: replace a brush when its face has worn to 1/3 of its height (register the interval; it feeds the Chapter 39 inspection checklist); when the commutator surface blackens and grooves, dress it with a fine oilstone held against the rotating surface.

[Card 31-03 Carbon Brush Making and Bedding-In] (eight fields)

1. **Input materials**: graphite powder (natural graphite ore, or dense hardwood charcoal ground and passed through a fine sieve); copper filing powder (copper filed and sieved); binder (shellac varnish, or thick syrup / dextrin); stock for pressing in a wooden mold.
2. **Tools required**: wooden mold (block forming); fine sieve; balance (weighing the mix, Chapter 25); series galvanometer (brush-resistance comparison, Section 31.6); fine sandpaper (bedding in); spring-loaded brush holder (pressure test); a fingernail (rough hardness check). Pre-use calibration: a pure charcoal block of the same size is the resistance reference — only a clearly lower galvanometer deflection passes; hardness passes when a fingernail leaves a shallow mark without crumbling or powdering.
3. **Operating sequence and control points**: batch the mix (graphite 70 / copper powder 25 / binder 5, parts by mass) → knead into a dough → press into blocks in the wooden mold → shade-dry → dry in the residual heat at the furnace mouth → bury in charcoal embers and burn slowly to red heat (sintering raises conductivity) → double inspection (resistance comparison + hardness scratch) → fit to the machine → **bed in**: wrap fine sandpaper around the commutator (grit face toward the brush), work the brush back and forth under hand pressure 20–30 times until the face takes the arc that matches the commutator → run 30 min unloaded → load. Control points: stop at red heat (over-burning turns it to ash); bedding in must produce the matching arc (loading an unbedded brush means sparking); set brush pressure so that "the brush will not slide out of the holder, yet can be pushed by feel".
4. **Empirical parameters and calibration**: the 70/25/5 formula is an empirical starting point: empirical values, to be calibrated to local conditions (graphite and copper-powder grit set the mix), judged by the resistance-plus-hardness double inspection. Brush-pressure calibration: the twin indicators of sparking and brush temperature — big sparks = too little pressure, a hot brush = too much. Bedding in 20–30 strokes and 30 min of unloaded running are empirical values. Life criterion: replace when the face has worn to 1/3 of its height, and register the interval.
5. **Process observation and recording items**: per batch — graphite and copper-powder source and sieve mesh, mix ratio, drying and sintering heat, resistance comparison result, hardness scratch result; at fitting — bedding strokes, unloaded running time, spark size, brush temperature, replacement date and cumulative running hours.
6. **Pass / rework / scrap criteria**: pass = resistance clearly below a same-size pure charcoal block + a fingernail leaves a shallow mark without crumbling + small sparks and a brush that is not hot after 30 min unloaded + stable sparking under load. Rework = the arc does not match (grind it in further); the resistance or hardness check fails (re-batch and remake that batch). Scrap = the sinter cracks, or the block crumbles and powders when pinched (remake the whole batch; no picking through it).
7. **Common failures and troubleshooting order**: (1) heavy sparking (first check pressure too low → then an arc that was never bedded in); (2) a hot brush (pressure too high); (3) fast face wear and powdering (hardness short — bad mix or bad sintering; remake); (4) the commutator blackens and grooves (dress with a fine oilstone held against the rotating surface, the surface-film rule of 31.11); (5) sparking returning after tens of hours (the brush has worn to 1/3; replace it).
8. **L1 / L2 / L3 evidence**: L1 = one batch of brushes (10 pieces including sintering, the labor-table unit) passes the resistance and hardness double inspection and is registered; L2 = the fitting, bedding-in, and unloaded-running record plus the first month's spark and brush-temperature readings; L3 = the brush replacement interval entered in the Chapter 39 inspection checklist, with the "resistance + hardness" double check adopted as the batch release criterion.

### 31.8 Generator Losses, Heating, and Faults

| Loss | Symptom | Countermeasure |
|---|---|---|
| Copper loss (I²R) | Coils too hot to touch | Thicker wire / limit the current |
| Iron loss (eddy currents) | Core hotter than the coils | Laminated core (Section 31.10) |
| Friction loss | Bearing temperature rise | The lubrication regimen of Chapter 21 |
| Brush loss | Sparking and wear | Brush pressure / bedding in / dressing the segments |

#### 31.8.1 "Spinning but No Power" Troubleshooting Table (This Chapter's First Diagnostic Table—Many Causes, One Symptom; Verify in Order, No Skipping)

| No. | Suspect | Verification method | Action |
|---|---|---|---|
| 1 | **Residual magnetism lost** (most common on self-excited machines) | Voltmeter on the output terminals, turn slowly: no needle movement at all = suspect residual magnetism; or remove the field magnet and compare its attraction against the archive | Re-magnetize per Card 31-01: connect the field winding to the battery bank and make-break 5–10 times (mind the direction) |
| 2 | Broken circuit in the winding | Galvanometer + battery in series, test continuity segment by segment (field winding, armature winding, lead-out wires tested separately) | Resolder the joint (tin soldering) and re-wrap the insulation |
| 3 | **Brushes off the neutral plane** | Fine-adjust the brush-holder angle and watch the voltmeter—the position with the highest reading is the neutral plane | Loosen the brush-holder bolts, set to the highest voltage, and refasten (scribe a witness line to prevent renewed misalignment) |
| 4 | Dirty commutator, oil film | Inspect visually for black film and oil stains | Dress with fine sandpaper held against the rotating surface until the copper color is uniform |
| 5 | Speed too low / belt slip | Measure the actual speed by tab counting; measure belt slip by the chalk-line method | Tighten the belt / shift the step pulley (Chapter 20) |
| 6 | Interturn short | Abnormally large no-load current + local overheating | Rework per Card 31-02 (strip and re-wrap) |
| 7 | Magnet fitted backward / demagnetized | Compare attraction against the magnet archive | Re-magnetize or reverse the pole orientation |

**Troubleshooting discipline: go through 1 to 7 in order—the first four steps take ten minutes and cover ninety percent of real cases. One rewind takes weeks; skipping steps and tearing things apart blindly is the greatest waste.**

**Temperature-rise red line**: if the hand cannot bear it for long (about 60 ℃, empirical), shed load—enforce the varnish's heat ceiling conservatively (the wax-chip compensation method is in Chapter 20).

[Card 31-04 "Spinning but No Power" Troubleshooting] (eight fields)

1. **Input materials**: one faulty machine (no need to strip it first); the magnet archive (attraction comparison records); the winding record sheet and the machine archive; a spare battery bank (for re-magnetizing).
2. **Tools required**: moving-coil voltmeter (Section 31.6); galvanometer + battery (section-by-section continuity and polarity); tripping-tab counter (speed measurement, Chapter 25); chalk (belt-slip line method); fine sandpaper (dressing the commutator); wrench (brush-holder bolts); 10x magnifier. Pre-use calibration: meter zero and range cleared by the Chapter 27 release slip.
3. **Operating sequence and control points**: strictly in the order 1→7 of the 31.8.1 table, **no skipping**: (1) residual magnetism lost (turn slowly and watch for any needle movement; or remove the field magnet and compare its attraction against the archive); (2) broken winding (galvanometer + battery, segment by segment: field winding, armature winding, and lead-outs tested separately); (3) brushes off the neutral plane (fine-adjust the holder angle; the highest reading is the neutral plane; scribe a witness line afterwards); (4) dirty commutator, oil film (look for black film and oil stains; dress with fine sandpaper held against the rotating surface until the copper is uniform); (5) speed too low / belt slip (measure speed by tab counting, slip by the chalk-line method); (6) interturn short (abnormally large no-load current + local overheating; rework per Card 31-02); (7) magnet reversed / demagnetized (compare against the archive; re-magnetize or reverse the poles). Control points: the first four steps take ten minutes and cover ninety percent of real cases; **one rewind takes weeks — skipping steps and tearing the machine apart blindly is the greatest waste**.
4. **Empirical parameters and calibration**: temperature-rise red line ≈60 ℃ (the hand cannot bear it long) → shed load (empirical). The neutral-plane criterion = the highest voltmeter reading, refined to the midpoint of the span where three consecutive points differ by ≤2% (Section 31.12). Residual-magnetism criterion = no needle movement at all on a slow turn. All of these are empirical values, to be calibrated to local conditions (machine and instrument differences set the criteria).
5. **Process observation and recording items**: date and machine number; which step in the order scored the hit; the measured value at every step (needle swing, segment continuity, holder angle against voltage, speed count, no-load current, attraction comparison); the action taken and the retest result.
6. **Pass / rework / scrap criteria**: pass = the order locates a single dominant cause and, once it is handled, no-load voltage returns to 90–105% of the old archive curve (the Section 31.14 acceptance basis). Rework = residual symptoms remain after one fix (go back to the untested items on the table; do not strip the machine). Scrap / out of service = winding burnout or interturn shorts in patches (rule a rewind, Section 31.14).
7. **Common failures and troubleshooting order**: (1) residual magnetism lost (most common on self-excited machines); (2) broken winding; (3) brushes off the neutral plane; (4) dirty commutator, oil film; (5) speed too low or belt slip; (6) interturn short; (7) magnet reversed / demagnetized — that is, the 31.8.1 table order; skipping straight to stripping the machine is recorded as a violation.
8. **L1 / L2 / L3 evidence**: L1 = one real fault worked through the table with records kept; L2 = that machine's no-load characteristic before and after; L3 = the table written into the duty procedure, with the recurrence interval of like faults registered in the machine archive.

### 31.9 From Hand Cranking to Continuous Supply

1. A hand-cranked bench prototype (verify the principle + calibrate the instruments);
2. Connect to the line shaft driven by the water wheel—**the birth of the continuous power source**;
3. First rules of load management: as load rises and falls, speed changes (and voltage with it)—the water-wheel gate is the coarse adjustment; the dedicated machine attendant records per the meter-reading system (voltage / current / temperature rise);
4. **Crude voltage stability first**: a lighting bank with a constant load is cheaper than "precision speed control"—fix the usage pattern before anything else.

### 31.10 How to Build a Better Second Generator

Four upgrades (each one spends capability earned by the first generation):
1. **Laminated core**: stack and rivet thin soft-iron sheets, brush varnish between sheets for insulation—eddy-current losses drop sharply;
2. **Multiple coils, multi-segment commutation**: smoother output pulsation, more current;
3. **Self-excitation**: the field magnets become electromagnets, excited by a small fraction of the machine's own output—**starting relies on residual magnetism** (the steel's faint residual magnetism gives the first wisp of voltage, and positive feedback amplifies it)—the terminal form of the magnet bootstrap chain;
4. **Volume production of moving-coil meters**, feeding back into whole-machine measurement.

Honest ceiling: this route can reliably light a lighting bank, drive electrolysis and electroplating, and power a telegraph (hundred-watt–kilowatt class; empirical values, must be field-calibrated); the bottleneck to larger scale and longer distance lies in line losses and insulation—the frontier of Chapter 32.

### 31.11 Detailed Commutator Manufacturing Rules (From Two Segments to Many)

The commutator is the part with the tightest tolerances on the whole machine and the gravest consequences of failure: eccentric outer circumference = the brushes bounce once per revolution = sparking; weak inter-segment insulation = inter-segment flashover (the prelude to ring fire). This section gives the full procedure for a multi-segment machine (8–12 segments); the first, two-segment machine follows it at half scale—the two-segment machine's commutation slots are wide and filing suffices; on a multi-segment machine, mica undercutting is mandatory.

**Structure and Blanking**

1. Segment count: once the commutator's outer diameter D is set, take segment thickness 3–5 mm and mica thickness 0.5–1.0 mm (empirical starting point: the higher the inter-segment voltage, the thicker the mica; taking 1.0 mm on the first two-segment machine costs nothing); the segment count n = round[πD ÷ (segment thickness + mica thickness)]; once rounded, the inter-segment gap must not exceed 0.5 mm—if it does, make it up with thin copper filler strips;
2. Copper segments: saw and file cold-rolled / cold-drawn copper bar into wedge-shaped cross-sections (a dovetail, narrow inside and wide outside, for the clamping ring's dovetail groove), and scrape flat the two contacting sides—fit criterion: hold two segments together against the light and no continuous bright line may show; thickness difference within a batch ≤0.1 mm (micrometer sample of 3 segments);
3. Inter-segment insulation: first choice is split natural mica (identification: it splits into 0.5 mm layers and neither burns nor cracks in a flame; talc-like material that crumbles to powder at a single tear is rejected). Compensation: 2–3 layers of varnished cloth / oiled paper—the performance penalty is poor heat resistance and fast wear; permitted only on low-temperature small machines, with the replacement interval registered in the archive. Cut the mica to the copper segment's side profile, 1 mm oversize on all four sides, and turn everything flush after assembly.

**Clamping Rings, Shrink Fitting, and Turning True**

4. Assembly: stack the copper segments and mica alternately onto the sleeve's dovetail; tighten the V-shaped clamping rings at both ends (with mica rings between the clamping rings and the copper segments, so the commutator cannot short to the shaft) with diagonally opposed bolts **in three progressive passes**, one full circuit per pass, tapping the segments' inner rings home against the sleeve with a wooden mallet as you go; fastening criterion = the segments cannot be budged by hand and the tapping sounds solid (a hollow sound = some segment not seated);
5. **Shrink-fit reinforcement**: heat the clamping rings to dull red and fit them hot (the hot-shrinking method, Chapter 18); contraction as they cool adds clamping force—after hot fitting, striking is forbidden and the assembly is never taken apart again (taking it apart = redoing the whole set);
6. **Turning true**: mount the assembly between lathe centers and take the outer circumference in one light pass—**the cut must not stop midway** (a stopped cut leaves a step = a periodic brush bounce once per revolution); measure radial runout over the full circumference with a fixed scriber + feeler gauges; criterion ≤0.1 mm (empirical value; calibration method: accept at 0.1 mm first, and if residual sparking remains after every other cause on the "spinning but no power" table is excluded, tighten to 0.05 mm and refit the brush holders). **Dynamic balance must be retested** (the static balance method of Section 31.5): the commutator assembly changes the rotor's center-of-gravity distribution—testing only the shaft's static balance is the same as not testing.

**Mica Undercutting (The Make-or-Break Operation of Multi-Segment Machines)**

7. After turning, the mica sits flush with the copper—but mica wears far more slowly than copper, and within tens of running hours it stands proud as ridges; the brushes vibrate on the ridges at high frequency, and sparking follows. So a newly built multi-segment machine must be undercut, and undercut again in service as the sparking dictates:
   - **Undercut depth = measured mica thickness + 0.5 mm (typically 1–1.5 mm)**; slot width = the natural width of the inter-segment groove; **no widening permitted** (widening = the copper edges become thin blades, which crumble into filings in service; copper filings conduct = inter-segment short);
   - **Hook knife**: break a 60–80 mm length off a worn-out hand hacksaw blade (high-carbon steel, the same stock family as the Chapter 19 files); grind a 20–30° single-facet edge on one end with an oilstone and bend out a hooked tip—the hook lets the blade body ride along the copper face while the hooked tip reaches the slot bottom;
   - **Technique ◎**: fit a crank handle to the shaft end and index segment by segment (or index at the lathe's slowest speed); keep the angle between blade and copper face under 15°; insert the hooked edge into the slot and **pull only, never push** (pushing = slipping that gnaws the copper edge); shave down layer by layer until no bright mica gleam shows at the slot bottom; misjudgment compensation: probe the slot with a vertical sewing needle—the tip touches bottom and the needle drawn along the slot bottom makes no shrill sound (scraping copper sounds shrill, scraping mica sounds draggy); a bright rolled burr on the copper edge = gnawing copper; stop at once and regrind the edge;
   - **Practice method**: grind two knives first (the first is bound to be ruined; keep it as a lesson) and put in a full 30 scrapes on the practice piece before touching the real machine—the practice piece is a milled wooden board, half of each slot holding scrap mica and half holding a copper strip; acceptance criteria identical to the real machine in every respect: flat slot bottom, unwidened walls, no rolled burr on the copper edges;
   - Finishing: blow clean with the bellows + sweep the filings with a brush (**copper filings conduct; residue in the slots is an inter-segment short**), wipe with paper until no black powder comes off, and lightly remove burrs from the copper edges with fine sandpaper; at every brush change, needle-probe the full circumference as well—dust from new-brush wear deposits in the slots; this item enters the inspection checklist as a fixed line.
8. **Guarding against "burn and wobble" in service**: if brush sparking is left unattended, or an inter-segment flashover occurs, the copper segments overheat locally, annealing to a blue tint, and the clamping rings loosen with heat—the symptom is radial runout growing month by month (known as commutator wobble). Rule: the monthly commutator check must include a runout retest (merged into the same inspection checklist as the brush replacement interval, Section 31.7.1); above 0.1 mm, first re-tighten the clamping rings and then retest the dynamic balance; a locally blued segment is dressed with a fine oilstone held against the rotating surface (Section 31.7.1); bluing over half the segment = back on the lathe to re-cut the outer circumference.
9. **Reading the surface film (the commutator's "skin")**: a well-running commutator carries a uniform tan-brown oxide film—tan-brown = good film (self-lubricating and protective; minimum wear); glossy black = oil-mist carbon fouling (no oil in the brush zone; see the safety boundary); striped bright marks = brush pressure so high it wore through the film. Remedy: dress off a bad film with fine sandpaper held against the rotating surface until copper color shows, then regrow the film (a new film takes roughly tens of hours; somewhat heavier sparking during that period is normal—register and observe; do not rush to adjust the brushes).

[Card 31-06 Commutator Mica Undercutting] (eight fields)

1. **Input materials**: 1 commutator already fastened and turned true (radial runout ≤0.1 mm, verified); 1 worn hand hacksaw blade per machine (a spring-steel strip may substitute; performance penalty = poor edge retention, grind often); 1 sewing needle; 1 small piece of fine sandpaper; 1 brush-and-bellows set.
2. **Tools required**: oilstone (Chapter 9, to grind the edge); 10x magnifier (residual fiber and burrs); lathe or crank-handle stand (Chapter 20, for indexing). Pre-use calibration: test-scrape 5 slots on the practice piece with the freshly ground edge; only a passing slot profile allows work on the real machine.
3. **Operating sequence and control points**: (1) scribe-mark all mica slots around the circumference; (2) index segment by segment, pull-scraping with the hooked edge; (3) blow out the filings every 5 slots; (4) needle-probe every slot to verify "bottom touched, copper untouched"; (5) re-inspect the full circumference, deburr, and retest runout and dynamic balance. Control points: **shave only mica, never gnaw copper** — at the first bright rolled burr, stop and regrind the edge; blade-to-copper angle under 15°; **pull only, never push**; slot width must not be widened (widening turns the copper edge into a thin blade that crumbles into filings, and conducting filings mean an inter-segment short).
4. **Empirical parameters and calibration**: undercut depth = measured mica thickness + 0.5 mm (typically 1–1.5 mm). Calibration: tear a sample from the same mica batch and measure it with the micrometer (calculating from nominal thickness is forbidden); after the first machine, re-verify the set value within 0.8–2 mm against sparking and brush wear, and transcribe it to the ledger.
5. **Process observation and recording items**: the scraping sound (shrill = gnawing copper; draggy = shaving mica); copper edge color (a bright rolled burr = knife damage); slot-bottom sheen (residual fiber); enter in the machine archive under "undercutting".
6. **Pass / rework / scrap criteria**: pass = needle probing over the full circumference finds no residue on any slot bottom + no bright-white scratches on the copper under the magnifier. Rework = localized residual fiber (re-scrape those spots). Scrap = knife damage to a copper segment deeper than 0.3 mm (re-cut the outer circumference and undercut again).
7. **Common failures and troubleshooting order**: (1) widened slot walls (edge angle too large → regrind a narrower edge); (2) uneven residual fiber on the slot bottom (unsteady pull stroke → back to the practice piece for more practice); (3) gnawed copper (feed too hard or the edge has rolled → regrind; switch to shallow, multiple passes).
8. **L1 / L2 / L3 evidence**: L1 = 1 practice piece, passed, kept as a retained sample; L2 = 1 full-circumference needle-probe record of the real machine, into the machine archive; L3 = the depth set value and the re-undercut interval into the inspection checklist, transcribed to the ledger.

### 31.12 Voltage Regulation (Field Rheostat, Neutral-Plane Scale, and Characteristic Curves)

That a machine generates electricity is merely the passing grade; only **adjustable, reproducible voltage** counts as fit for duty—otherwise lamps flare and dim, electrolysis currents surge and sag, and every downstream process suffers. Three things: the field rheostat, the brush-position scale, and the characteristic curves.

**Slide-wire field rheostat (adjusting excitation = the master gate of voltage)**

- Connection point: wired in series in the field (excitation) winding circuit—less excitation, weaker field, lower voltage; the reverse raises it. This is the least troublesome means of voltage regulation on a shunt self-excited machine, and it consumes no main-circuit power;
- Frame: a porcelain tube or hardwood tube (length 200–300 mm, diameter 30–40 mm, no cracks), held at both ends by brackets on an insulating baseboard;
- Resistance wire: **iron wire, 1–1.5 mm—iron's resistivity is about 6 times copper's (empirical value; calibration: cut 10 m, measure the resistance, back-calculate and register ohms per meter)**; anneal to dull red and air-cool; the oxide scale formed in the fire is itself the turn-to-turn insulation and must not be scratched during assembly; wind with 1/2 wire-diameter spacing between turns to prevent overlap. Wrong-material self-check: it is iron wire only if a magnet attracts it; if not, you mistakenly took copper wire (a "rheostat" wound of copper wire has no resistance—installing it installs nothing);
- Total resistance, empirical starting point: **0.5–1.5 times the field winding's DC resistance**—a regulation band covering "full excitation down to about forty percent"; calibration method: first wind a full 1x and install; on trial runs record a "slider position vs. voltage" table; if the high-voltage end cannot be adjusted = resistance too small, wind on more; if the low-voltage end collapses too fast = cut short or parallel sections; transcribe the set value to the ledger;
- Sliding arm: a spring brass strip pressing on file-brightened contact strips, with a 20 mm dead zone at each end of the travel; every 10 turns, scrape the varnish and bring out a tap to a porcelain-board binding screw (a jumper backup should the sliding contact fail);
- Scale plate: with a voltmeter on the output terminals, record one reading for every 10 turns of slider travel; one pass over the full travel yields the "position vs. voltage" table; copy it out in large characters and post it beside the rheostat—**the machine attendant operates by the scale, never by feel**;
- **Division of duties between the gate and the rheostat (never use them in reverse)**: the water-wheel gate governs speed (coarse adjustment, the energy side); the rheostat governs excitation (fine adjustment, the voltage side). Using the rheostat to brute-force a speed deficit = power wasted as heat in the resistance; using the gate to fine-tune voltage = slow response that harms the other loads.

**Fine brush-position adjustment and the neutral-plane scale**: cut an arc-shaped slotted hole in the brush-bracket base, fitted with a brass dial and pointer (the Chapter 27 dial center-punching and scribing craft). The "highest-voltage position" of step 3 in Section 31.8.1 is refined into a reproducible zero: near the peak, move the brush holder in 1–2 mm steps and record the voltage each time; **set the zero at the midpoint of the span where three consecutive points differ by ≤2%**, and center-punch 3 marks on each side as the scale; after every disassembly and remounting of the brush holder, recheck against zero—a 2 mm misalignment shows up at once as lost voltage and sparking. Register the zero set value in the machine archive (date, peak voltage, and the rheostat scale recorded together).

**Measured speed–voltage characteristic curve (linked to the Chapter 25 power-measurement counting method)**

1. Fix the rheostat at its rated scale; take 5–7 stable speed points on the water-wheel gate from small to large; at each point measure by tab counting 3 times and average, recording the no-load voltage at the same time;
2. Draw the curve on graph paper (or in ink on a planed board): the low-voltage section should be a straight line passing near zero (induced voltage ∝ speed, Section 31.1); a clear bend away from the line = the magnetic circuit approaching saturation or instrument error—register it, do not correct it;
3. Three uses of the curve: **back out the rated speed** (follow the straight line to the point matching the nameplate set voltage); **find the build-up speed** (the lowest point where the curve clearly lifts off zero; below it a self-excited machine will not excite); **judge decay** (voltage at the same speed down more than 10% from last month = demagnetization or brush-position drift; check the brush position first, then the magnet archive);
4. Supplementary load-characteristic test: at rated speed, add lighting-bank load step by step, recording (load step, voltage, rheostat scale after compensation)—this table is the body of the machine attendant's duty manual.

[Card 31-07 Field Rheostat] (eight fields)

1. **Input materials**: 1 porcelain / hardwood tube (200–300 mm, diameter 30–40 mm, no cracks); 15–30 m total of annealed iron wire, 1–1.5 mm (magnet-tested, oxide scale intact); 1 spring brass strip (clock-spring steel may substitute; performance penalty = it fatigues easily, replace often); 1 insulating baseboard, 10 binding screws.
2. **Tools required**: lathe winding crank (Chapter 20); micrometer (recheck of wire diameter, Chapter 22); moving-coil voltmeter and galvanometer (Section 31.6); tin-soldering tools (for the taps). Pre-use calibration: first sample-test 10 m of the iron wire's resistance; a difference over 10% from the ledger's registered value = a different batch; re-mark the ohms per meter.
3. **Operating sequence and control points**: (1) anneal the iron wire to dull red and air-cool (this forms the oxide insulation layer); (2) wind evenly and closely with 1/2 wire-diameter turn spacing, **turns must not touch one another (contact = that section's resistance vanishes)**; (3) every 10 turns, scrape the varnish and solder out a tap; (4) file the contact strips bright and set the sliding arm's pressure until "pushing it by hand meets a weighty drag"; (5) measure and post both tables over the full travel — "resistance vs. scale" and "voltage vs. scale". Control points: no turn-to-turn contact; measure the full travel, never work by feel.
4. **Empirical parameters and calibration**: total resistance = 0.5–1.5 times the field winding's resistance (empirical starting point, to be calibrated to local conditions); the regulation band must cover ±20% of rated voltage to pass, and if it falls short, wind more on or cut short, transcribing the set value to the ledger; iron's resistivity is about 6 times copper's (empirical value; calibration: cut 10 m, measure, and back-calculate the ohms per meter).
5. **Process observation and recording items**: sparking at the slider (an occasional faint blue arc is tolerable; a continuous arc = stop using it and dress the contact surface); local red glow on the tube body (overcurrent or interturn short); tap temperature rise (a precursor of a loose joint).
6. **Pass / rework / scrap criteria**: pass = smooth over the full travel with no jumps + a regulation band covering ±20% of rated. Rework = sparking at isolated contacts (brighten with fine sandpaper, adjust the arm pressure). Scrap = interturn shorts in patches (proven by jumps in section-by-section resistance measurement; rewind that tube).
7. **Common failures and troubleshooting order**: (1) voltage unmoved across the whole travel (copper wire used by mistake — verify with a magnet); (2) a jump at one point (oxidized contact surface or a loose tap — brighten / re-solder); (3) no resistance in the middle section (turns touching — locate by section-by-section resistance measurement).
8. **L1 / L2 / L3 evidence**: L1 = full-travel resistance record of one tube; L2 = both tables (resistance / voltage vs. scale) into the machine archive; L3 = the set value and the sliding-arm service interval into the inspection checklist, transcribed to the ledger.

### 31.13 Before Paralleling (First Lesson of Two Machines on One Bus)

One machine is a power source; two machines are a system—get paralleling wrong and both break together. This chapter sets only three rough rules and one forbidden zone; full paralleling, protection, and small grids are the next chapter's territory.

1. **Polarity check (the first gate of paralleling; getting it wrong means burning both)**: the magnetic-needle method (the Chapter 30 Oersted experiment)—run one lead from each machine parallel past the same magnetic needle; make-break each machine's circuit momentarily, one at a time; **deflection in the same direction = polarities agree**. Or the center-zero galvanometer method: interconnect the two machines' positive terminals through a galvanometer, and the negatives to each other; turn the second machine slowly; **the needle kicking backward = polarities opposite**; stop, swap that machine's lead-out wires, and verify again. Once checked, stamp or scratch "+/−" on both machines' output terminals and register it permanently in the machine archive;
2. **Voltage check**: before paralleling, both machines at no load and at the same rated speed; **terminal voltage difference ≤5%** (empirical value; calibration method: with two machines of the same type, parallel them first and record the difference; before extending to dissimilar machines, first compare no-load characteristic curves, Section 31.12). The higher-voltage machine carries the bus first; adjust the second to **2–3% above the bus** before closing—after closing, the new machine immediately takes its share of load and its terminal voltage settles back to the bus value, with the least shock;
3. **Rough load sharing**: **same-shaft drive preferred**—drive both machines from the same line shaft / the same water-wheel belt; their speeds are locked by one shaft, neither can run away from the other, and once the voltages are brought close, current sharing settles automatically; the attendant watches only the total current and both machines' temperature rise. If each must truly be driven separately (two water wheels), watch the ammeter surge after closing: **if the surge exceeds half of rated, open the switch at once**, re-adjust the voltage and parallel again; try the open-and-readjust cycle at most three times; three failures = the machines' characteristics differ too much—switch to same-shaft drive or shed load and find the cause. After paralleling, read both machines' currents every 10 min; once the sharing ratio is stable, resume the normal meter reading;
4. **The reverse-charging forbidden zone**: if at the instant of closing the new machine's terminal voltage is below the bus, the bus backfeeds the new machine and it turns motor (reverse rotation, overheating, burned winding). Hard rule: **close only when the new machine's measured terminal voltage is ≥ bus + 2% before paralleling**; after closing, the ammeter should kick forward (the new machine delivering); if it kicks backward, open at once. One violation goes straight into the accident record (the Chapter 25 accident system);
5. **Registering the isolated-grid concept of frequency**: a DC island grid has no word "frequency," but it has an equivalent—**the water wheel's speed is the pulse of the whole grid**: every lamp added pulls the speed down a notch and the voltage down with it; the attendant on duty watches two lines: speed (tab counting, measured every shift) and voltage (meter reading), with the gate making the compensation. This notion that "generation and consumption balance every second" enters the operating procedures with this chapter; practice the feel of that balance on a single machine first—the next chapter's paralleling and frequency regulation are all built on this foundation.

### 31.14 The Full Rewind Procedure (Overhaul Rules)

**Repair-or-rewind ruling**: localized interturn shorts, localized punctures = rework per Section 31.4.2 (strip and re-wrap); burnout, interturn shorts in patches, insulation aged brittle throughout = rule a rewind. No major overhauls for minor ailments—rewinding one stator winding costs 4–6 labor-days (see this chapter's labor table) and is a comprehensive examination of the entire winding production line.

1. **Stripping the old wire and the stripping record (record first, act second—the order may not be reversed)**: before stripping, sketch the connection diagram in pencil (lead-out positions, jumper routing, slot-numbering scheme); strip slot by slot, filling in the stripping record sheet as you go:

   | Item | How recorded | Purpose |
   |---|---|---|
   | Turns per slot | Count one slot, record it; cross-check the cumulative total at the last slot | The sole basis for the rewind turn count |
   | Wire diameter | Micrometer, 3 points averaged | Basis for choosing new wire / reuse |
   | Pitch | Slots spanned (e.g., slots 1–4) | Wire placement positions for insertion |
   | End extension length | Wooden rule / calipers, both sides | Winding-form end dimensions |
   | Slot insulation | Material + layer count | Materials list |

   Pin the record sheet to the machine archive for good—**for the rewind, every parameter defers to the record sheet; memory is forbidden** (rewinding from memory = booking an appointment for a second accident).

2. **Old-wire recovery**: burn the whole coil briefly at dull red in the furnace (cleans off the old varnish and anneals in one) → air-cool → pickle off the oxide scale (the copper pickle, Chapter 17) → re-measure the diameter with the micrometer. Criteria: shrinkage ≤2% = set aside directly for reuse; shrinkage >2% or a necked spot = back through the drawing dies one size down and reassign to fine-wire duties. **Copper annealed three or more times coarsens in grain and turns brittle**—it may serve only in field windings of many fine turns that see no vibration, and is forbidden in armatures (armatures see heavy centrifugal force and vibration; brittle wire breaks first);
3. **Making the winding form**: a hardwood form in two halves (openable to release the coil); size the core from the old coil's measurements: inner-loop length and width = core dimensions + slot insulation thickness; end radius converted from the old end extension; nail turn-counting pegs along the form's edge. Winding tension ◎: pull by hand until springy, to the point where the wire takes no sharp set; misjudgment compensation: micrometer the wire once every 20 turns—**diameter drawn down over 2% = tension too great; slack off at once** (thinned wire has uneven resistance and overheats locally in service);
4. **Insertion and the two-dip two-bake schedule**: insert per the full Section 31.4.2 procedure (slot insulation, interlayer paper, wedges driven tight, ends bound knot by knot). Execute the dipping and drying schedule (furnace-mouth residual-heat zone + wax-chip temperature compensation, Chapter 12):
   - Pre-bake 60–80 ℃ × 2 h to drive off moisture—**if the moisture is not driven out, the varnish seals it inside: slow rot**;
   - First dip: varnish at 40–50 ℃ (if too thick, add turpentine and thin until "a film lifts on a wooden stick and breaks in intermittent flow"); immerse until bubbling stops, drain 1 h;
   - First bake: 60–70 ℃ × 2 h with a slow ramp, then 90–100 ℃ × 4 h;
   - Once cooled through and the leakage rough test passes (Section 31.4.3), second dip and second bake on the same schedule, with the last bake extended 2 h;
   - Criteria: the varnish film glossy and blister-free; a fingernail tap sounds solid (a hollow, dull sound = the varnish did not penetrate; back to the furnace for a supplementary bake).
5. **Rewind acceptance (against the old archive; all three must pass before entry into service)**:
   - Withstand voltage: 2x operating voltage for 1 min (the hard rule of Section 31.4.3);
   - DC resistance: measured value within ≤5% of the value computed from the record sheet—a double check of wire diameter and turn count;
   - **No-load characteristic comparison**: at the same speed and the same rheostat scale, no-load voltage between 90–105% of the old archive curve passes; below 90%, troubleshoot in order: turns short (check the record sheet) → wire diameter wrong → air gap enlarged (eccentric assembly) → magnets demagnetized (step 1 of Section 31.8.1); above 105% usually means extra turns were wound—register a corrected curve at the same time, and **never wave it through as "a gain"** (extra turns = the excitation demand changes, the rheostat scale changes wholesale, and the attendant operating by the old scale loses control).

---

## Master Parameter Table

| Parameter | Value | Class |
|---|---|---|
| Drawing step reduction | 10–20% per step; one anneal per step | Empirical |
| Die-hole inspection | No chipping at 10x magnification; register wire-pass snugness | Criterion |
| Slot insulation | Oiled paper / varnished cloth; copper never touches iron | Hard rule |
| End-winding binding | One knot per 5–10 turns, grease-soaked hemp cord | Procedure |
| Withstand-voltage test | 2x operating voltage, 1 min | Hard rule |
| Carbon brush formula | Graphite 70 / copper powder 25 / binder 5 (parts by mass) | Empirical starting point |
| Brush replacement criterion | Replace at 1/3 remaining height | Procedure |
| Neutral plane | Brush holder set to the highest-voltage position | Criterion |
| Temperature-rise red line | ≈60 ℃ (hand cannot bear it long) → shed load | Empirical |
| Run-in period meter reading | Voltage / current / temperature rise, twice per shift | System |
| Mica segment thickness | 0.5–1.0 mm (take the upper limit at high inter-segment voltage) | Empirical starting point |
| Undercut depth | Measured mica thickness + 0.5 mm (typically 1–1.5 mm) | Procedure |
| Commutator radial runout | ≤0.1 mm (rechecked with scriber + feeler gauges) | Criterion |
| Rheostat total resistance | 0.5–1.5 times the field winding's resistance | Empirical starting point |
| Paralleling conditions | Polarities agree + new machine's terminal voltage = bus + 2–3% | Hard rule |
| Rewind resistance deviation | ≤5% (against the value computed from the record sheet) | Criterion |
| Rewind no-load voltage | 90–105% of the old archive curve | Criterion |
| Two-dip two-bake schedule | 60–80 ℃×2h→90–100 ℃×4h, two rounds | Procedure |

## Failure Modes and Diagnosis

| Symptom | Candidate causes (by probability) | Verification | Action |
|---|---|---|---|
| Spinning but no power | Seven causes, one symptom | **In the order of the Section 31.8.1 table** | See the table |
| Low voltage | Speed too low / weak residual magnetism / interturn short | Counter / magnet archive / no-load current | See the table |
| Heavy brush sparking | Brush position off / brush pressure low / commutator oil film | The neutral-plane adjustment method | Re-position / replace brush / dress |
| Abnormal temperature rise after days of running | End-winding chafing short / damp | Leakage rough test | Re-dip and re-bind / dry out |
| Bearing over-temperature | Lubrication / lost dynamic balance | The three checks of Chapter 21 | Clean the oil ways / redo the static balance |
| Burnt smell from the coils | Overload / interturn short | Stop at once and inspect | Limit the load / rework per Card 31-02 |
| Wire breaks (drawing) | Insufficient annealing / chipped die mouth | Check the annealing records / inspect the die under magnification | Anneal again / change the die |
| Magnetism decays month by month | Soft steel grade / vibration demagnetization | Retest against the magnet archive | Switch to high-carbon steel and re-magnetize |
| Brush wear spikes after undercutting; slot edges blackened | Undercut too deep, scoring the copper face / residual fiber left in the slots | Inspect the slot edges at 10x for bright-white knife marks; needle-probe the slot bottoms | Re-scrape the residual fiber; knife marks over 0.3 mm: re-cut the outer circumference and re-undercut (Card 31-06) |
| Voltage jumps during regulation; sparking at the slider | Thick oxide on the sliding contact / arm pressure too low / loose tap | Locate the jump by section-by-section resistance measurement | Brighten the contact, adjust arm pressure; re-solder the tap (Card 31-07) |
| No excitation after rewind, or no-load voltage far below the old value | Turns short / wire diameter wrong / connections reversed / air gap too large | Item-by-item check against the stripping record sheet + DC resistance comparison | Correct per the record sheet; resistance deviation >5% means mandatory rework (Section 31.14) |
| Ammeter kicks backward at closing; the new machine spins freely | Reversed polarity / new machine's voltage below the bus (reverse charging) | Verify polarity by the magnetic-needle method; compare the two machines' terminal voltages | Open at once; swap the leads, adjust to bus + 2–3%, and parallel again (Section 31.13) |

## Process Card Index

## Acceptance Criteria

- **L1**: all three modes of change reproduced in the Faraday experiment; the hand-cranked machine lights one carbon-filament lamp / drives bubbling in electrolysis.
- **L2**: the drawing–insulation–winding line produces qualified wire (spark-method spot checks + the withstand-voltage test passed); water-wheel-driven continuous supply for a full shift with complete meter readings; the copper coulometer completes one calibration; the "spinning but no power" table used on at least one real fault, with records kept.
- **L3**: the second-generation machine (laminations + self-excitation) in service and feeding back into instrumentation; the three wear items—carbon brushes, bearings, enameled wire—all made locally; the magnetizing archive and brush replacement intervals entered in the Chapter 39 inspection checklist; the power ledger merged into Chapter 38. Evidence: machine archive (winding sheets, withstand-voltage records), meter-reading logbooks, fault-troubleshooting records.

## Labor Hours, Manpower, and Consumption

| Item | Manpower | Labor hours (empirical) |
|---|---|---|
| Drawing 100 m of 1.5 mm wire (incl. annealing) | 2 people | 2–3 days |
| One stator / field-yoke winding (insertion, binding, dipping) | 2 people | 4–6 days (dipping and drying another half day) |
| A batch of carbon brushes (10 pieces, incl. sintering) | 1 person | 2 days |
| First machine final assembly and commissioning | 4 people | 10–15 days |
| Fault troubleshooting (per the table) | 1–2 people | 0.5 h–2 h |
| Consumption | Per machine: copper 2–5 kg, varnish 0.5 kg, paper and hemp as needed | Into the Chapter 38 ledger |

## Safety Boundary

- Shut down before any grid connection / wiring; discharge Leyden-jar-type devices before touching;
- The temperature-rise red line is the load-shedding line; no oil and no dust in the brush-spark zone (oil mist meeting sparks = flash fire);
- A drawing wire that snaps whips back and can injure the eyes—wear eye protection; at the annealing furnace, follow the forging rules;
- Handle copper-salt liquids for electrolytic calibration under the Chapter 26 chemical management rules (never ingest; waste liquid goes to the Chapter 49 disposal line);
- The magnetizing battery bank's series voltage is fairly high; wear dry gloves and practice one-hand operation (a prelude to the Chapter 32 electrical safety).

## A. Existing Tool Inventory

Electromagnet and galvanometer, voltaic pile (Chapter 30); hardened steel and abrasives (Chapters 19, 9); lathe / bearings / step pulleys (Chapters 20, 21); wax-resin varnish (Chapters 8, 23); paper and hemp yarn (Chapters 10, 15); balance and counting (Chapter 25); pointer mechanism and hairsprings (Chapter 27).

## B. New Tools Added in This Chapter

The Faraday induction experiment procedure; the rotating-magnet first generator; the magnet bootstrap chain and the magnetizing card; drawing dies, the anneal-and-draw process, and the wire gauge–resistance table; the three insulation crafts—enameled, cotton-covered, paper-covered; the insertion–binding–dipping procedure with leakage rough testing and the withstand-voltage test; the dynamic balancing procedure; the commutator, the carbon brush formula, and the bedding-in system; the moving-coil galvanometer; the copper coulometer current standard; the seven-step "spinning but no power" troubleshooting table; the four-way loss table; the temperature-rise red line; line-shaft grid connection and the meter-reading system; the second-generation machine's four upgrades; the commutator manufacturing and mica undercutting procedure (hook knife and practice piece); the slide-wire field rheostat and its scale plate; the brush-holder neutral-plane dial; the paralleling polarity / voltage checks and the reverse-charging forbidden zone; the full rewind procedure and the two-dip two-bake schedule; the speed–voltage characteristic curve.

## C. Unresolved Dependencies

Transformers and the AC system (Chapter 32); storage batteries at scale; high-voltage insulators and outdoor lines (Chapter 32); AC meters and wattmeters (the precision-instrument line).

## Dependencies for the Next Step

Chapter 32: lines, insulators, fuses, the telegraph, and small grids. Chapter 33: stable supply unlocks continuous vacuum-pump operation and filament testing. Chapters 34–35: electrolysis and electroplating are unit operations of the ultrapure-materials route. Chapter 36: the electronics industry = the combination of power supply + devices + chemistry. Chapters 38–39: the power ledger and wear-part inspection.
