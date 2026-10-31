# Chapter 22: Measurement, Standard Parts, and Repeatable Manufacturing

## Chapter Objectives

Upgrade "able to make it" to "able to make the same thing over and over": establish a classification language for errors, a thread standard with interchangeability, a gauge system with comparison measurement, a regime for preserving and transferring measurement references, and the bootstrap manufacture of the first generation of precision measuring tools (micrometer, vernier, comparator). **Standardization is not a capability machines come with; it is an institution formed jointly by measurement, machining, and inspection.**

## Capability Boundaries

**What can be done:** first-version thread standard of 3–4 specifications; a go/no-go gauge system and gauge-block sets; micrometer repeatability ≤0.01 mm; tap threading and a defined-torque fastening regime; parts interchangeable between two workshops.

**Explicitly cannot be done:** higher-grade gauge blocks (flatness and temperature-control limits); optical measurement (Chapters 24, 27); constant workshop temperature (after Chapters 13, 28).

**External dependencies:** a thread standard locks in the moment it is published—**the cost of revising a standard is scrapping the entire inventory**; trial-assembly verification is mandatory before publication.

## Pre-Work Verification (check off each item)

| # | Verification item | Criterion | Source |
|---|---|---|---|
| 1 | Thread cutting | Change-gear-cut thread pitch matches the master lead screw (pair-checked) | Chapter 20 |
| 2 | Hardening and lapping | After lapping, working faces show contact spots in continuous patches against a surface plate | Chapters 19, 20 |
| 3 | Standard-bar system | Three-bar mutual check on file; gauge blocks wring together and hold | Chapter 3 + this chapter |
| 4 | Error record system | One card and one number per gauge | Chapters 3, 4 |
| 5 | Temperature discipline | Precision measurement at a fixed time of day (most stable temperature); part and gauge soaked together ≥ half an hour | This chapter |
| 6 | Lathe condition | Annual inspection records on file (guideways, spindle) | Chapter 20 |

---

### 22.1 Why Standard Parts Are the Foundation of Industry

The threads of Chapter 20 are "numbered matched pairs"—if one breaks, the whole machine must be reworked. Standard parts solve this: **any nut threads onto any screw of the same specification**. Three transitions:
1. Repair no longer depends on the original craftsman (the engineering answer to the Chapter 4 knowledge-inheritance problem);
2. Parts can be made in one place and stocked centrally (the premise of division of labor; the physical basis of the multi-workshop collaboration of Chapter 37);
3. Designs are expressed as "standard-parts catalog + drawings" (the drafting system of Chapter 42).

The cost of interchangeability is **tolerance**: each dimension is assigned an allowed range (e.g., 10 mm ±0.1 mm), and all parts are guaranteed to fall within that range.

### 22.2 Dimensional, Form, and Position Errors

The three error classes are stated separately so that inspection has a place to start:

| Class | Definition | Inspection tools |
|---|---|---|
| Dimensional error | Deviation of the actual size from the nominal value | Snap gauges, micrometer, limit gauges |
| Form error | Imperfection of a single feature itself (not straight, not flat, not round) | Straightedge + spotting, three-point roundness, surface plate |
| Position error | Deviation of relationships between features (not parallel, not perpendicular, not coaxial) | Square, string line, dial indicator on a mandrel |

Example: a shaft whose diameter passes but which is bent (form out of tolerance); once assembled, the gear face runs out (position out of tolerance). On the process card, each key feature gets three columns; the inspection sheet is executed exactly as written (the format source of the Chapter 42 tolerance-callout card).

### 22.3 Thread Standards and Interchangeability

#### 22.3.1 The Four Elements of the Standard

1. **Unified thread form**: 60° V-form triangular thread with flat crest and flat root (stronger, and resists seizure);
2. **Pitch series**: banded by diameter, one standard pitch per band (the first version's 3–4 specifications cover the main uses—better too few than too many):

| Specification | Pitch | Tap-drill diameter (steel/iron) | Main uses |
|---|---|---|---|
| M6×1 | 1 mm | 5.0 mm | Instruments, small parts |
| M10×1.5 | 1.5 mm | 8.5 mm | Machine tools, general use |
| M16×2 | 2 mm | 14 mm | Frames, boilers |

**Tap-drill formula**: tap drill ≈ major diameter − pitch (steel/iron); for soft material (copper, hardwood) use major diameter − 0.5×pitch (threads bite deeper into soft material). Tap drill too small = the tap twists off during tapping; too large = crossed, stripped threads—**before tapping, drill by the table first, and verify the drill diameter with a snap gauge**.

3. **Tolerance zones**: lower deviation on the bolt's major diameter, upper deviation on the nut's minor diameter, so any combination of conforming parts has flank clearance;
4. **Source of the standard**: the lathe's master lead screw + change gears cut the first batch of standard screws; or the finest hand-made screw serves as the "prototype standard," and all gauges are calibrated against it.

The standard is written up, numbered, and archived (Chapter 4); revisions go through version management (Chapter 42 change control).

#### 22.3.2 Taps and Tapping (The Volume Solution for Internal Threads)

Hand-fitted nuts (the Section 20.5 template method) cannot do volume. Tap making and tapping:

- **Tap making**: turn a standard external thread on the lathe (M10×1.5) → file/chisel 3–4 chip flutes along the axis (flutes deep enough to pass below the thread root) → grind a cutting lead of 3–5 threads at the end (head tapering smaller; it guides first, cuts after) → quench and temper (brown-yellow) → straighten. Tap wrench: wooden handle / iron frame with a square hole that fits over the tap's square tail;
- **Tapping procedure**: ① drill the tap-drill hole per the table ② chamfer the hole mouth (prevents a turned-up lip) ③ enter the tap and check squareness in two directions with a square ④ every half turn, **back off a quarter turn** to break the chip (◎ hand-feel: a sudden torque rise means back off immediately; forcing = broken tap) ⑤ drip oil (mandatory on steel) ⑥ first run the taper tap (long cutting lead) through, then the second tap (short cutting lead) to finish sizing;
- **Broken-tap removal**: a broken tap is tapping's number-one accident. Removal method: anneal (heat the tap locally to dark red to soften it), then tap it back out counterclockwise with a punch; if it cannot be removed, the workpiece is scrapped (a hardened broken tap cannot be drilled)—**hence the tapping discipline: verify squareness, break chips promptly, stop the instant torque spikes**.

[Card 22-01 Tapping] (eight fields)

1. **Input materials**: a conforming tap-drill hole (drilled per the tap-drill table, drill diameter verified with a snap gauge); a tap (turned to the standard external thread, then 3–4 chip flutes cut, quenched and tempered brown-yellow, straightened); tapping oil (mandatory on steel); the workpiece, clamped.
2. **Tools required**: tap wrench (wooden handle / iron frame with a square hole over the tap's square tail); drills and snap gauge; try square (squareness checked in two directions); oil can; punch and a heating furnace (for annealing out a broken tap). Calibration source: tap drill checked against major diameter − pitch; thread form calibrated to the prototype standard (Section 22.3.1, item 4).
3. **Sequence and control points**: (1) drill per the tap-drill table → (2) chamfer the hole mouth to prevent a turned-up lip → (3) enter the tap and check squareness in two directions with a square → (4) every half turn **back off a quarter turn** to break the chip (◎ back off the instant torque spikes; forcing = broken tap) → (5) drip oil → (6) run the taper tap through, then the second tap to size → (7) inspect with go/no-go gauges. Control point: **squareness, chip breaking, stop on torque spike** — break one and the tap snaps.
4. **Empirical parameters and calibration**: tap drill ≈ major diameter − pitch (steel/iron): M6×1→5.0 mm, M10×1.5→8.5 mm, M16×2→14 mm; soft material (copper, hardwood) −0.5×pitch (the tap-drill formula is empirical, must be calibrated to local conditions); thread form 60° V with flat crest and root; 3–4 chip flutes, deep enough to pass below the root; cutting lead 3–5 threads; back a quarter turn per half turn (hard rule). Calibration: inspect the first hole with go/no-go gauges and log where torque spiked, hole by hole, to fix the chip-breaking rhythm for that batch of material.
5. **Observations to record**: per hole — specification / measured tap drill / two-direction squareness check / number of chip breakings / where torque spiked / which tap (taper or second) / go/no-go result.
6. **Pass / rework / scrap criteria**: pass = go gauge threads smoothly over the full length + no-go gauge enters ≤2 turns; rework = local binding (back the tap out, rework that section, pass again); scrap = crossed threads or a broken tap that cannot be extracted.
7. **Common failures and diagnosis order**: (1) threads slip with no bite (tap drill too large → soft-material formula misapplied); (2) tap twists off (tap drill too small → not square → chips not backed off); (3) thread form spoiled after tapping (second tap not used to size).
8. **L1 / L2 / L3 evidence**: L1 = one tap drives 10 holes through and passes go/no-go; L2 = tapping scrap rate <10% on file; L3 = taps can be remade locally and gauges trace back to the standard bar in a closed loop.

#### 22.3.3 Bolt Preload: The Defined-Torque Fastening System

Bolts working loose are the number-one source of assembly accidents; overtightening is the number-one source of fractures. A regime for the era without torque wrenches:

- **Defined-torque pull line**: scribe a "pull line" on the wrench bar (at 200 mm from the bolt center, empirical value); the operator pulls steadily with one hand and stops exactly at the line—200 mm × 15–20 kg of force ≈ 3–4 kgf·m in magnitude (the general preload band for M10; order-of-magnitude sanity check: the breaking torque of an M10 bolt is about 60–80 N·m, i.e., 6–8 kgf·m; the working band takes 1/2 of that; empirical value, must be field-calibrated);
- **Calibration method**: take a connection that can be tested to destruction, increase force step by step until bolt stretch becomes measurable (measure overall bolt length with a micrometer) or the threads strip / the bolt breaks; take 1/3–1/2 of that as the working torque band;
- **Hand-feel bands (◎; compensation: the defined-torque line)**: snug into place (for anti-loosening situations) → half tight (routine) → full torque line (sealing and load-bearing);
- **Three locking methods**: double-nut jam locking (bottom nut tightens, top nut locks); cotter pins (pin match-fitting, Chapter 20); wire lacing (bolt groups laced head-to-tail, so any one bolt loosening is restrained by its neighbors);
- **Vibration sites must use locking**—every bolt on line shafts, waterwheels, and hammer frames (vibration environments, Chapter 21 + the weekly tightening items on the Chapter 39 inspection checklist).

[Card 22-04 Torque-Limited Tightening and Locking] (eight fields)

1. **Input materials**: standard bolts and nuts (M6×1 / M10×1.5 / M16×2); locking parts (second nut, cotter pin, lacing wire); the parts being joined.
2. **Tools required**: wrench with a "pull line" scribed on the bar at 200 mm from the bolt center; one-hand pull (the operator judges it); a connection that may be tested to destruction (for calibration); micrometer (to measure overall bolt length for stretch). Calibration source: the working band comes from a destruction test, not from "how tight it feels."
3. **Sequence and control points**: (1) set the band by joint type — snug (anti-loosening duty) / half tight (routine) / full torque line (sealing and load-bearing) → (2) verify the pull line at 200 mm on the wrench bar → (3) pull steadily with one hand and stop exactly at the line → (4) choose the locking method: double-nut jam (bottom tight, top locks), cotter pin, wire lacing (group laced head-to-tail so any one loosening is held by its neighbors) → (5) vibration sites must be locked (line shafts, waterwheels, hammer frames) → (6) weekly re-tightening enters the inspection checklist. Control point: **stop at the line** — past the line is over-tight.
4. **Empirical parameters and calibration**: pull line at 200 mm from the bolt center (empirical value, must be calibrated to local conditions); one-hand force 15–20 kg ≈ 3–4 kgf·m (the general M10 preload band); M10 breaking torque about 60–80 N·m (6–8 kgf·m), with the working band at 1/2 of it. Calibration: take a connection that may be tested to destruction, raise force stepwise until bolt stretch is measurable (micrometer on overall length) or the threads strip / the bolt breaks, and take 1/3–1/2 of the breaking value as the working band; the three hand-feel bands are compensated by the defined-torque line.
5. **Observations to record**: per joint — specification / band used (snug, half tight, full torque) / locking method / pull-line position / re-tightening interval and result / fracture location on any broken bolt.
6. **Pass / rework / scrap criteria**: pass = pulled to the line without exceeding it + locking parts in place + no loosening within one re-tightening interval; rework = torque short (step up a band, re-tighten, recheck the locking); scrap = bolt broken at the neck (over-tight — drop a band and replace the bolt).
7. **Common failures and diagnosis order**: (1) loosens in service (no locking → torque short); (2) bolt fractures (over-tight beyond the breaking value → vibration fatigue; a neck fracture means over-tight); (3) nut backs off (double nuts not jammed, or wire not laced).
8. **L1 / L2 / L3 evidence**: L1 = pull line calibrated with a destruction-test basis on file; L2 = every bolt at vibration sites locked and weekly inspection records on file; L3 = torque bands and locking methods written into the process card, with a second person assembling to it and passing.

#### 22.3.4 Pin Joints and Interference Fits

- **Parallel pins**: ream the hole to size (the reamer is made the same way as a tap, but with straight edges and no flutes), and drive the pin with an interference of the 0.01–0.03 mm class (empirical value). Striking feel (◎): with a wooden mallet it enters smoothly for the first 2/3 of its length; the last 1/3 needs a heavier hammer and a backing block—"easy first, tight last" is a conforming interference; loose all the way in = insufficient interference (go one pin size up); immovable from the start = excessive interference (ream the hole again);
- **Taper pins**: the reamer carries a 1:50 taper; the pin is seated when, after driving, the large end stands slightly proud—**a taper pin can be removed and reinstalled repeatedly without losing locating accuracy** (superior to the parallel pin; used for locations that will be serviced);
- **Interference sleeve fitting** (gears/pulleys on shafts): turn the hub bore to shaft diameter −0.05 mm class, heat the hub (boiling water / hot-oil bath) so it expands, slip it on, and let it cool and grip tight—the precision version of Chapter 21's "burn-on sleeve method."

[Card 22-05 Pin Fitting and Interference Fits] (eight fields)

1. **Input materials**: parallel pins or taper pins (1:50 taper); gear/pulley and shaft (hole to be reamed); reamer (straight edges, no flutes; taper reamer with 1:50 taper); thin oil.
2. **Tools required**: tap/reamer wrench; wooden mallet and a heavy hammer with backing block; heating bath (boiling water or hot oil); micrometer; snap gauge. Calibration source: interference computed from measured pin diameter minus measured hole diameter, not judged by the sound of the blow.
3. **Sequence and control points**: (1) ream the hole to size (1:50 taper reamer for taper pins) → (2) clear chips and oil → (3) drive the parallel pin with 0.01–0.03 mm class interference: the wooden mallet takes it smoothly for the first 2/3 of the length, the last 1/3 needs the heavy hammer and backing block → (4) drive the taper pin until the large end stands slightly proud (it can be removed and refitted repeatedly without losing location) → (5) interference sleeve fitting: turn the hub bore to shaft diameter −0.05 mm class, heat the hub to expand it, slip it on, let it shrink and grip, in one continuous motion (hands never enter the bore). Control point: **"easy first, tight last" is the only conforming interference.**
4. **Empirical parameters and calibration**: parallel-pin interference 0.01–0.03 mm (empirical value, must be calibrated to local conditions); taper pin 1:50, seated with the large end slightly proud; sleeve fit hub bore = shaft diameter −0.05 mm class, heated in boiling water / hot-oil bath. Calibration: on the first pair record pin diameter, hole diameter, actual interference, and striking feel, turning "2/3 easy, 1/3 heavy hammer" into that workshop's hand-feel baseline.
5. **Observations to record**: per pair — measured pin and hole diameters / interference / striking feel (share of the easy section) / taper-pin stand-proud amount / heating method and fitting result / number of assembly cycles.
6. **Pass / rework / scrap criteria**: pass = easy first then tight, fully seated, taper pin slightly proud; rework = excessive interference, will not drive (ream again or drop one pin size); replace = goes in loose all the way (insufficient interference — go one pin size up).
7. **Common failures and diagnosis order**: (1) pin will not drive (interference too large → hole reamed small); (2) pin works loose (interference short — "loose all the way in"); (3) sleeve will not grip (hub bore turned large or insufficient heating — remake the fit).
8. **L1 / L2 / L3 evidence**: L1 = one pin fit meeting "easy first, tight last"; L2 = interference and hand-feel records on file, taper pin surviving repeated assembly without losing location; L3 = a second person fits one pair from this card alone and meets the standard.

### 22.4 Gauges, Plug Gauges, and Comparison Measurement

**Go/no-go gauges** (checking whether a size lies inside the tolerance band, ten times faster than taking readings):
- Plug gauge (checks holes): the go end is made to the lower limit of the tolerance band (should pass), the no-go end to the upper limit (should stop);
- Snap gauge (checks shafts): same logic, reversed;
- Thread gauges: go gauge (full thread form; should thread over the full length), no-go gauge (truncated thread form; should stop within 2 turns);
- Manufacture: hardened steel, lapped working faces, calibrated against a micrometer and standard parts—**a gauge is "a standard part in its limit form."** Scrap criterion: a go end that will not go, or a no-go end that goes, is scrap.

[Card 22-02 Making and Calibrating Go/No-Go Gauges] (eight fields)

1. **Input materials**: hardened steel blanks (Chapter 19 brown-yellow temper band); standard parts (prototype screw / standard blocks); 20 test parts of known size distribution (pre-sorted with a micrometer).
2. **Tools required**: lapping plate (the Chapter 20 three-plate set); micrometer (five-point checked); standard parts; stamp and handle stock; compartmented box and thin oil. Calibration source: calibrated against standard parts by the comparison method — **never by direct absolute measurement**.
3. **Sequence and control points**: (1) set the two end sizes — plug gauge go end at the lower limit of the tolerance band (should pass), no-go end at the upper limit (should stop); snap gauge for shafts, same logic reversed → (2) form, then harden and temper → (3) lap the working faces until contact spots form a continuous patch on the plate → (4) calibrate go and no-go ends against standard parts by comparison → (5) stamp "GO/NO-GO" and the gauge number on the handle → (6) inspect 20 test parts of known distribution; every verdict must be correct. Control point: the go end and the no-go end are made to opposite limits of the band — **they must never come out the same size**.
4. **Empirical parameters and calibration**: go end = lower limit of the band, no-go end = upper limit (reversed for a snap gauge on shafts); thread gauges — go gauge with full thread form should thread the full length, no-go with truncated form should stop within 2 turns; working faces lapped to continuous contact spots. Calibration: sort the 20 test parts with a micrometer first, then inspect; only an all-correct verdict set counts as calibrated. Temperature discipline: soak together ≥ half an hour; re-inspection interval every 200 inspections or monthly, whichever comes first (empirical value, must be calibrated to local conditions).
5. **Observations to record**: per gauge — specification / measured go and no-go sizes / deviation from the standard part / lapping contact-spot condition / verdicts on the 20 test parts / re-inspection date and conclusion.
6. **Pass / rework / scrap criteria**: pass = all verdicts correct on 20 test parts of known distribution; rework = go end falsely stopping from burrs or dirt (clean, deburr, recalibrate); scrap = the gauge itself out of tolerance (go end will not go, or no-go end goes).
7. **Common failures and diagnosis order**: (1) go end falsely stops (burrs on the working face → dirt); (2) batch misclassification (temperature — when the gauge-to-part difference is hand-detectable, soak both half an hour and re-inspect); (3) no-go end goes (no-go worn small — scrap and remake).
8. **L1 / L2 / L3 evidence**: L1 = one plug gauge and one snap gauge calibrated against standard parts; L2 = periodic re-inspection records unbroken for three months; L3 = every gauge remade locally and traced back to the standard bar.

**Comparison measurement**: do not measure the absolute size; measure "the difference from a standard part." Standard parts (the gauge-block idea): lap-copy standard blocks of the 10, 20, 50 mm class from the standard bar; if two blocks push together and hold (wringing force), flatness is conforming. Comparator stand + pointer: see Section 22.8.

### 22.5 How to Establish Standard Length and Standard Angle

- **Length**: the standard bar is the source → three replica bars mutually checked at intervals (for any two bars, the differences across three orientations sum to zero; this detects drift of a single bar) → gauge-block sets propagate downward;
- **Temperature correction (written down)**: the thermal expansion coefficient of iron is about 11.7×10⁻⁶/℃—a 1 m iron bar lengthens 0.0117 mm per 1 ℃ rise. Precision comparisons record the temperature and note "measured at X ℃." Discipline: concentrate precision measurement in the daily window of most stable temperature, and soak bar and part together ≥ half an hour before comparing;
- **Angle**: the right-angle reference = the isosceles-triangle diagonal method + the square-flip self-check (Chapter 20); standard angle blocks are made by turning regular-polygon bar stock—the chord angles of an equally divided circle self-verify (a full-circle 360° closure check, **with the closure error distributed equally back to each angle**—the key to bootstrapping the angle system).

### 22.6 From Individual Craftsmen to a Unified Process

The unification three-piece set:
1. **Process card**: operation number → equipment → workholding → cutting parameters → inspection points → gauge numbers. For any one nominal part there is only one current-version process card across all workshops (version system, Chapter 42);
2. **First-article inspection**: the first piece of every batch is measured in full dimension and must pass before the batch proceeds;
3. **Sampling + records**: sample 10% per batch (empirical value, must be field-calibrated); any out-of-tolerance piece triggers 100% inspection of the whole batch.

Division of labor unfolds along the process card: a layout worker need not understand quenching, but must understand his own inspection points (the interface to the Chapter 37 skill matrix and the Chapter 43 master–apprentice assessments).

### 22.7 How to Maintain Measurement References

- **Reference pyramid**: source (standard bars / surface plates) → transfer artifacts (gauge blocks, gauges) → working tools (calipers, micrometers). **Only the upper may calibrate the lower; lower-calibrates-upper is strictly forbidden**;
- **Periodic mutual checks**: source artifacts mutually checked every six months; transfer artifacts checked against source quarterly; working tools checked against transfer artifacts monthly; anything knocked or dropped goes for calibration immediately;
- **Environmental discipline**: gauges are not stored mixed with tools, never used on moving parts, never used on hot parts (measure after cooling), and are oiled and returned to their places after use;
- **Archives**: one card per gauge (number, calibration records, next calibration date); a lost gauge is immediately demoted to a teaching piece (the gauge page of the Chapter 39 inspection checklist).

### 22.8 How to Make Better Measuring Tools

**Micrometer** (the fruit of lead-screw bootstrapping): an M10×1.5 lead screw—thimble advance of 1.5 mm per revolution, with 30 graduations around the thimble at 0.05 mm each; a 10-division vernier scribed around the thimble pushes the reading down to 0.005 mm (empirical value, must be calibrated). Key points: lapped lead screw, wring-fitted anvil flatness, C-frame stiffness, **ratchet constant pressure** (a consistent measuring force is the precondition of repeatability).

[Card 22-03 Micrometer Verification] (eight fields)

1. **Input materials**: micrometer (M10×1.5 lead screw — 1.5 mm advance per thimble revolution, 30 graduations at 0.05 mm each, a 10-division vernier reading down to 0.005 mm); gauge-block set (1/2/5/10/20/50) or standard parts of known size; gauge card.
2. **Tools required**: gauge blocks or standard parts; silk cloth; thin oil; gauge card (number, calibration records, next calibration date). Calibration source: the check reference is the gauge-block set, whose own upstream is the standard bar (Section 22.7 reference pyramid — only upper calibrates lower).
3. **Sequence and control points**: (1) zero — close the anvil and read zero, log the deviation on the card → (2) five-point gauge-block check covering the full range → (3) repeatability — range of ten measurements on the same part → (4) once a month, plus immediately after any knock → (5) out-of-tolerance handling: clean and recalibrate, or record an error table and correct by segment, or make a new lead screw. Control point: **hold the frame, not the anvil** — hand heat is the first source of reading drift.
4. **Empirical parameters and calibration**: lead screw M10×1.5; thimble 30 graduations × 0.05 mm; 10-division vernier → reading down to 0.005 mm (empirical value, must be calibrated to local conditions); indication error ≤0.01 mm; repeatability — ten-measurement range ≤0.01 mm; verification interval once a month plus after any knock. Calibration: record the deviation at each of the five points as an error table, and write the segment corrections onto the gauge card.
5. **Observations to record**: per verification — zero deviation / five-point indication errors / ten-measurement range / verification date / knocks and repairs.
6. **Pass / rework / scrap criteria**: pass = indication error ≤0.01 mm and repeatability ≤0.01 mm; rework = clean and recalibrate (dust inside the ratchet); scrap = lead-screw wear out of tolerance (make a new screw).
7. **Common failures and diagnosis order**: (1) reading drifts (hand heat — hold the frame, not the anvil); (2) uneven error across travel (local lead-screw wear — record an error table and correct by segment); (3) poor repeatability (ratchet constant pressure lost, or dust on the anvil face — strip, clean, recalibrate).
8. **L1 / L2 / L3 evidence**: L1 = zero and five-point records on the card; L2 = ten-measurement repeatability ≤0.01 mm on file with three unbroken months of periodic calibration; L3 = error tables complete for every micrometer in the shop and segment correction in practice.

**Vernier caliper**: main scale in 1 mm divisions; vernier of 10 divisions spanning 19 mm total—the offset alignment amplifies 10×, giving readings of the 0.1 mm class.

**Comparator**: lever amplification (two 1:10 stages = 1:100) + pointer + dial, with ball or knife-edge probe types. The comparator turns "comparing against a standard part" into an assembly-line motion (instrumentation continues in Chapter 27).

---

### 22.9 Serializing the Thread Gauge Set: One Set of Four and the Gauge Library

Section 22.4 produced "a single gauge"; this section upgrades it into an institutional asset of "one set per specification, shared by all workshops"—on the day the thread standard is published, the gauge set must be mustered alongside it.

**One set of four**. Every thread specification gets a full set of four gauges:

| Item | What it checks | Go/no-go criterion |
|---|---|---|
| Thread plug gauge, GO | Nut internal thread | Should thread through the full length |
| Thread plug gauge, NO-GO | Nut internal thread | Should stop within 2 turns |
| Thread ring gauge, GO | Screw external thread | Should thread through the full length |
| Thread ring gauge, NO-GO | Screw external thread | Should stop within 2 turns |

Plain plug gauges for tap-drill holes and outside-diameter snap gauges are provisioned separately under Section 22.4 and do not count against these four. Fully outfitting the first three specifications (M6/M10/M16) = 12 thread gauges + 6 plain gauges—this is the minimum gauge list for publication day.

**Manufacturing division**. Each specification designates one **master gauge**, made by the standards worker (the dedicated gauge custodian—the first specialized post created by the Section 22.6 process-card division of labor) per the Section 22.2 process card, with three lines engraved on the body (specification, GO/NO-GO, serial number), sealed in red lacquer in the gauge library, and forbidden from daily use. **Working gauges** (used at workstations) are copied by each workshop against the master gauge by the comparison method. A **check gauge** is also made separately for each specification: a ring gauge's internal thread cannot be measured directly with a micrometer, so the check plug gauge is the ring gauge's "ruler"—use the no-go end size to calibrate the GO gauge and the go end size to calibrate the NO-GO gauge, cross-exposing wear.

**Stock and issue**. The gauge library is attached to the accounting office (the physical-goods page of the Chapter 4 archive system):
1. At least 2 sets of working gauges per specification—one in use, one on standby; during calibration rotation, draw the standby set;
2. Four entries on every issue record: who drew it, date, gauge number, and the batch number being inspected; return and sign off at end of shift—one gauge gone missing = inspection of that specification suspended;
3. Stored in compartmented wooden boxes, working faces up, thinly oiled; never stored in the same box as cutting tools or other tools (knocking is the number-one cause of gauge death).

**Wear and scrapping cycle**. A go gauge gets looser with use (a plug gauge's go end wears small; a ring gauge's go end wears large), and quietly accepting out-of-tolerance parts into stock is the most silent failure. First-version cycle: **recheck against the check gauge every 200 inspections or every month (whichever comes first)** (empirical value; calibration method: sample 20 borderline parts and tally the misclassification rate; a rate >5% halves the cycle); two consecutive failed rechecks halve the cycle again and trigger an investigation of usage practice. Scrap criteria: the go end lost (the check gauge detects go-end size drift) or the no-go end lost (the no-go end passes 2 turns) means scrap and remake; demoted pieces are stamped "X" and moved out of the gauge library for teaching use.

### 22.10 Keys and Splines: The Torque Upgrade Route and Match-Fitted Splines

**The three-level torque route** (choose the level by need, not by "bigger is better"):

| Level | Form | Torque band (steel shaft/steel hub) | Calibration method |
|---|---|---|---|
| Level 1 | Single flat key | Same magnitude as the M10 preload band, about 3–5 kgf·m | Destructive test: crush-break the key or crush the keyway; take 1/3 of the failure value as the working band |
| Level 2 | Double keys (180° apart) | Single key ×1.5 (not ×2: the load between two keys is uneven, empirical value) | Same comparison test; record which key breaks first |
| Level 3 | Spline, 4–6 keys equally spaced | Single key ×3–4 | Same |

Key-size empirical rule: **key width ≈ shaft diameter / 4, rounded to a whole number** (10–16 mm shafts take 4–5 mm keys; 16–24 mm take 6–8 mm); square keys for shafts below 16 mm. Assembly criteria: the key enters the shaft keyway as a light press (thumb pressure seats it) and enters the hub keyway with a push-slide or light tap. Beyond 1.5× the shaft diameter, a longer key carries no more load—the extra length is only wasted effort. Before cutting keyways in batches, first make a keyway go/no-go snap gauge (the go/no-go idea of Section 22.4).

**The spline dilemma of this generation**: all the keyways of a spline bore are equally spaced around the bore wall; broaching (a broach pulls all keyways in one stroke) requires a high-tonnage press and a full broach set, which this generation cannot build—spline bores can only be **match-fitted**.

**Four steps of match-fitting a spline (layout—chisel—file—color-spot fitting)**:
1. **Layout**: color the hole end face; with an angle block (Section 22.5 equal-division self-check) lay out 4 or 6 equally spaced keyway lines and carry them onto the bore wall; connect the lines on both faces and verify the equal division (misalignment = the indexing is already wrong; this is the cheapest point to scrap);
2. **Chisel the keyways**: chisel along the lines, leaving 0.3–0.5 mm of allowance around; check keyway depth preliminarily with the snap gauge;
3. **Rough file**: file each keyway to the layout lines in rotation, leaving a uniform ~0.1 mm on the key flanks—finishing one keyway completely before starting the next is the number-one source of indexing drift;
4. **Color-spot fitting (◎)**: first make the **match-fitting spline shaft** (keys cut to nominal size; it serves as the color-marking master gauge); coat the key surfaces with red lead powder mixed with machine oil into a paste, insert it into the bore, rotate it back and forth through a small angle for several turns, withdraw it, and read the contact spots on the key flanks—lightly file from where the spots are heaviest, alternating over 2–3 keys, until the contact spots on all key flanks are uniformly distributed along the key length and the assembly pushes in over its full travel with no abrupt change in tightness.

◎ Practice method: lay out 4 equally spaced keyways on scrap and run the complete chisel—file—color-mark sequence on at least 2 pieces before touching real parts. ◎ Compensation: do not rely on "feels about right"—the acceptance evidence is spot coverage (contact spots on each key flank ≥2/3 of the key length) plus a thin paper slip (0.05 mm class) that will not enter the key flank.

**Interchangeability boundary**: a match-fitted spline is a one-to-one pair, with no interchange. Stamp matched-pair numbers at assembly (continuing the Chapter 20 matched-pair numbering convention) and record the pair numbers in the archive; if the shaft fails, copy it using the original shaft as the master gauge (the master-gauge method restores that pair's interchangeability); if the bore fails, the whole set is re-matched. When key-flank play becomes hand-detectable (about the 0.1 mm class), impact noise appears in the drive—judged rework.

[Card 22-07 Match-Fitted Splines] (eight fields)

1. **Input materials**: the finished spline-bore part (bore bored / reamed to size, wall still to be keyed); one match-fitting spline shaft (keys cut to nominal size, hardened — it serves as the color-marking master gauge); red lead powder + machine oil (mixed to a paste); marking color (for the bore end face); a keyway go/no-go snap gauge (made first, on the Section 22.4 go/no-go idea); 0.05 mm class thin paper slips (final check); an angle block (for the equal division).

2. **Tools required**: scriber and square; angle block (equal-division self-check, Section 22.5 closing-error equalization); narrow chisel and hammer; one coarse and one fine file (in matched condition); bench vise (to hold the bore part against turning); red lead dish and brush; snap gauge (preliminary keyway depth); thin paper slips; matched-pair number stamps; match-fitting record card. Calibration source: equal division from the angle block, keyway depth from the snap gauge, final acceptance from spot coverage plus the paper slip — never "it feels about right".

3. **Sequence and control points** (layout → chisel → rough-file in rotation → color-spot fitting → final check → stamp): ① **Layout** — color the bore end face, lay out 4 or 6 equally spaced keyway lines with the angle block and carry them onto the bore wall. Control point: connect the lines on both faces and verify the equal division — **misalignment means the indexing is already wrong, and this is the cheapest point to scrap**. ② **Chisel the keyways** — chisel along the lines leaving 0.3–0.5 mm of allowance, check depth preliminarily with the snap gauge. ③ **Rough file** — file each keyway to the lines in rotation, leaving a uniform ~0.1 mm on the key flanks. Control point: finishing one keyway before starting the next is the **number-one source of indexing drift**. ④ **Color-spot fitting** — coat the key surfaces with the red lead and oil paste, insert into the bore, rotate back and forth through a small angle several turns, withdraw and read the spots on the key flanks. ⑤ **Correct the spots** — file lightly from where the spots are heaviest, alternating over 2–3 keys, each round bounded by an insertion trial. ⑥ **Accept** — until the spots on all key flanks are uniformly distributed along the key length (each flank ≥2/3 of the key length) and the assembly pushes in over its full travel with no abrupt change in tightness. ⑦ **Final check** — a 0.05 mm class paper slip will not enter the key flank. ⑧ **Stamp and file** — stamp matched-pair numbers at assembly (the Chapter 20 matched-pair convention) and record the pair numbers. Control point: at least 2 practice pieces before any real part (lay out 4 keyways on scrap and run the full chisel–file–color sequence).

4. **Empirical parameters and calibration**: chiselled allowance 0.3–0.5 mm (empirical; first-piece calibration — log the actual hours and scrap rate of the chisel and file steps and take the lowest total cost); rough-file allowance on the key flank 0.1 mm; final check a 0.05 mm class paper slip will not enter the key flank (criterion); spot coverage ≥2/3 of the key length; key width ≈ shaft diameter / 4 rounded (10–16 mm shafts take 4–5 mm keys, 16–24 mm take 6–8 mm, square keys below 16 mm); splines 4–6 keys equally spaced, torque about ×3–4 of a single key (empirical, destructive-test calibration); beyond 1.5× the shaft diameter a longer key carries no more load; play detectable by hand (about the 0.1 mm class) means impact noise in the drive and is judged rework; a 4-key pair (including the match-fitting shaft) takes 2 people 3–5 days.

5. **Observations to record**: bore part and match-fitting shaft numbers, pair number; number of keyways and the equal-division check (do the lines on the two faces coincide); measured chiselled allowance; snap-gauge keyway depth; a spot sketch after every color round, keyed by keyway number (which key, where the spot sits and how far it runs); filing rounds; the paper-slip result; how the push-in feels; play re-measured.

6. **Pass / rework / scrap criteria**: pass = spots uniformly distributed along all key flanks (≥2/3 of the key length) + full travel smooth with no abrupt tightness + no play + paper slip will not enter; rework = an individual key flank over-marked (correct that key alone); equal division sound but the allowance filed away (loose throughout) → fit a new match-fitting shaft; scrap = equal division mislaid (unrecoverable after chiselling), bore mouth chipped, or a keyway chiselled through the bore wall.

7. **Common failures and diagnosis order** (by frequency): ① the assembly sticks halfway → barrelled key flank (file rocking; spots concentrated at both ends proves it) — shorter strokes, lighter cuts, look at the spots often; ② loose throughout → allowance filed away, fit a new match-fitting shaft (demote the old one to practice master); ③ bell-mouthed bore, loose at entry → chisel chipping at the keyway edge — chamfer the bore mouth and refit; ④ keyways of unequal depth → one keyway finished before the next (the number-one source of indexing drift) — go back to filing in rotation; ⑤ spots only at one end → taper on the key flank or the keyway floor — check the shaft key face against the bore axis; ⑥ impact noise in the drive, play detectable by hand → flank clearance at the 0.1 mm class, judged rework and refitted; ⑦ the lines on the two faces do not coincide (indexing off) → scrap and re-lay out at the layout stage; it cannot be patched after chiselling.

8. **L1 / L2 / L3 evidence**: L1 = one 4-key spline pair completed and passing the paper-slip, spot and push-in criteria, with the spot sketch on file; L2 = ≥3 pairs (different bore parts) completed with pair numbers matching the archive, and a second person able to reproduce the same feel from the archive; L3 = the match-fitting archive bound up (including scrap and rework causes counted), plus one successful copy made from the match-fitting shaft as master (old shaft fails → the master restores interchangeability for that pair).

### 22.11 Gear Tolerances and Center-Distance Measurement

A gear carries one more layer of conformity criteria than a shaft or a bore: not only must its own dimensions pass, it must also "get along well with its mating gear once installed in the housing." The first-version gear tolerance governs only three things: tooth thickness, center distance, and the double mesh check.

**Tooth thickness**. The detailed procedure for direct fine measurement of tooth thickness (gear-tooth caliper with both jaws spanning the tooth perpendicular, fine-feed reading) is developed in the Chapter 25 gear chapter; this chapter sets the criterion: **the range of tooth thickness across the teeth of one gear ≤0.05 mm** (empirical value; calibration method: tally the range distribution tooth by tooth over the first batch of 10 gears, then write it into the standard). Uneven tooth thickness has preview value: if a periodic "clunk" appears in operation (one per revolution), check the tooth-thickness range first, then check shaft bending.

**The measuring-rod method for center distance**. The center distance between the housing's two shaft bores determines backlash and contact position—however accurately you measure a single bore's diameter, you cannot compute the center distance from it; both bores must be measured together:
1. Two hardened, polished measuring rods (diameters d₁, d₂, verified at ten points with a micrometer, measured values recorded in the rods' file records) are inserted into the two shaft bores, sized so they fit snug without falling;
2. Measure the maximum **outside** distance between the two rods, L_out, with a micrometer/caliper; then the center distance A = L_out − (d₁+d₂)/2. If the bores are large, measure the **inside** distance L_in; then A = L_in + (d₁+d₂)/2;
3. Criterion: **center-distance tolerance ±0.05 mm per 100 mm of center distance** (empirical value; calibration method: trial-assemble a pair of verified conforming gears, tabulate measured center distance against crushed-lead backlash, and set the plant's own standard).

The measuring rods go into the gauge library and are rechecked periodically under the Section 22.9 system—a rod worn 0.01 mm small shifts the center-distance reading by the 0.005 mm class.

**Backlash and contact-pattern double check**. Two criteria govern two separate things—mutually independent, not interchangeable:
- **Backlash** (governs "loose or not"): empirical value = **3%–5% of the module** (low-speed drive band). Measure by the lead-crushing method: lay a lead wire across the mesh of two teeth, bar the drive around one full revolution so it is rolled, remove it, and measure the thinnest point of the flattened spot with a micrometer—that is the normal backlash—more reliable than probing curved tooth flanks with feeler stock. Backlash too small = thermal expansion seizes the drive after running; too large = reversal impact (the source of noise and tooth-flank pitting);
- **Contact pattern** (governs "aligned or not"): coat the pinion's tooth flanks with red lead, bar it around under load for 10–20 revolutions, and read the contact traces on the gear's tooth flanks. Pass = the contact pattern sits at the middle of the flank and covers **≥40% of the face width** (empirical value; calibration method: after one season of running, strip the first installed gears for inspection and back-set the band from those without pitting); pattern toward the tooth tip / root = center distance too small / too large (locate it against the measuring-rod readings); pattern toward one side = the two axes are not parallel (correct the bearing seats or the housing joint face);
- **Order**: first measure the center distance with the rods (static; the housing can still be reworked), then lead-crushing + color marking (final verdict after final assembly)—reversing the order misdiagnoses a contact-pattern problem as a center-distance problem, and a housing is bored for nothing.

### 22.12 Gauge-Block Manufacture and Wringing

Gauge blocks are the companion standard parts of the Section 22.8 comparator: a set of hardened-steel rectangular blocks of differing thickness (uniform cross-section 30×9 mm) whose two large working faces are lapped until they "push together and hold." The Chapter 3 standard bar is the length source; gauge blocks break the source into pieces that can be combined into any size—the middle tier of the Section 22.7 reference pyramid is complete from here on.

**Manufacturing sequence** (derived from the three-plate technique; carried out throughout on the Chapter 20 surface plate):
1. Cut and rough-machine the blank, leaving a lapping allowance of 0.10–0.15 mm on both faces;
2. Quench and temper (Chapter 19 brown-yellow band), then **naturally age ≥7 days**: stack the blocks, weight them down, and let them rest—the number-one killer of gauge blocks is later distortion; aging cannot be skipped;
3. Rough lapping: coarse plate + coarse abrasive, lap until tool marks and black scale are gone; check parallelism at ten points across the four corners with a micrometer; only when the range is of the ≤0.02 mm class may fine lapping begin;
4. Fine lapping: dry-lap on an abrasive-charged plate, **rotating the block 90° in place every 10–20 strokes** (to cancel one-directional loading), and lap until blocks **wring together and hold**—after cleaning, push two blocks together and lift one; if it carries the other, that is this generation's flatness pass criterion (a substitute criterion for the era without optical flats; higher grades: see Capability Boundaries);
5. Length calibration: zero the comparator against the standard bar and compare; the center length and the four-corner readings (parallelism = four-corner range ≤0.002 mm, empirical value; calibration method: tally what the first batch of 10 blocks actually achieves, then write it into the standard) are recorded together on the gauge card.

**Wringing technique (◎), the three-step wring**:
① **Clean**: wipe each working face twice with silk cloth in one direction only; fingers never touch the working faces (the fingerprint oil film is the number-one obstacle to wringing);
② **Press**: align the two working faces and press lightly; when viscous resistance is felt, wringing has begun;
③ **Slide**: slide back and forth 5–10 mm along the long edge two or three times, rotate 90° and slide once more; when the feel turns from tacky to slick, it is done.

◎ Practice method: take two rough-lapped scrap blocks and practice wringing 20 times a day for 3 consecutive days; the pass line = 10 consecutive wrings all holding, and after wringing the lower block does not drop when lifted vertically. ◎ Compensation: do not trust hand-feel—"lifts without dropping" is physical evidence; if blocks will not wring, check oil film and burrs against the failure-mode table first, and suspect flatness last.

**Gauge-block set and combination table**. The first-version set is 6 blocks: one each of 1, 2, 5, 10, 20, 50 mm. Combine by "picking from the largest block down"; examples:

| Target size | Combination |
|---|---|
| 3 | 2+1 |
| 7 | 5+2 |
| 17 | 10+5+2 |
| 38 | 20+10+5+2+1 |
| 63 | 50+10+2+1 |
| 88 | 50+20+10+5+2+1 |

The six blocks combine into 63 sizes in total (2⁶−1). A size that cannot be built (e.g., 44) does not take the forced-fit route; it takes the comparison route: stack the nearest combination, zero against it, and read the difference on the comparator (the proper meaning of the Section 22.8 comparison measurement). Combination discipline: **one stack ≤4 blocks** (each additional wringing face adds another share of wringing-failure risk, empirical value); after combining, recheck the stack once against the standard bar, to cover the small errors sandwiched into the wringing faces; when done, separate immediately, wipe clean, oil, and return each block to its compartment—gauge blocks left in the wrung state for long periods seize by stress corrosion, an accident of the scrapping class.

[Card 22-06 Gauge-Block Manufacture and Wringing] (eight fields)

1. **Input materials**: hardened steel blanks (uniform section 30×9 mm, Chapter 19 brown-yellow temper band); coarse and fine abrasives; silk cloth; thin oil; weights for aging.
2. **Tools required**: abrasive-charged fine-lapping plate (the best of the three plates, Chapter 20); coarse lapping plate; micrometer; standard bar; comparator; compartmented wooden box. Calibration source: length referred to the standard bar, zeroed on the comparator.
3. **Sequence and control points**: (1) saw and rough-machine, leaving 0.10–0.15 mm lapping allowance on both faces → (2) harden and temper, then **natural aging ≥7 days** (stacked under weights, undisturbed) → (3) rough-lap until tool marks and black scale are gone; check parallelism at four corners and ten points, and only enter fine lapping when the range is ≤0.02 mm → (4) fine-lap with **a 90° rotation in place every 10–20 strokes**, until the block wrings and holds → (5) calibrate length: zero against the standard bar, record center length and four-corner readings on the card. Control point: aging cannot be skipped; rotation cannot be skipped.
4. **Empirical parameters and calibration**: section 30×9 mm; lapping allowance 0.10–0.15 mm (empirical value, must be calibrated to local conditions); aging ≥7 days; rough-lap four-corner range ≤0.02 mm; fine-lap rotation every 10–20 strokes; parallelism four-corner range ≤0.002 mm (empirical value, written into the standard after tallying the first 10 blocks); set of six blocks 1/2/5/10/20/50 (63 combinations); one stack ≤4 blocks. Wringing in three moves: clean (two unidirectional wipes with silk cloth, fingers never touching the working face) → press (align and press lightly; the onset of tackiness means wringing has begun) → slide (reciprocate 5–10 mm along the long edge two or three times, rotate 90°, slide once more).
5. **Observations to record**: per block — wringing result per face (pass/fail) / ten-point length readings / fine-lapping stroke count / four-corner range / stacking records.
6. **Pass / rework / scrap criteria**: pass = wrings and holds (lifting one block carries the other) + length and parallelism archived; rework = local failure to wring (return to the plate and re-lap that face); scrap = distortion (insufficient aging), or fine lapping breaking through to black scale (allowance insufficient).
7. **Common failures and diagnosis order**: (1) wrings at once but slides tacky (oil film or sweat — wipe again and re-wring); (2) edges wring but the center does not (center low, monotonous lapping path — add indexing); (3) comparator reading drifts (instrument not settled — calibrate the instrument first); (4) blocks seize after long storage in the wrung state (not separated after use — a scrapping-class accident).
8. **L1 / L2 / L3 evidence**: L1 = wringing records of the first 3 blocks + ten-point reading sheets; L2 = two consecutive batches passing + complete gauge cards; L3 = closed-loop records tracing the whole block set back to the standard bar.

## Parameter Summary Table

| Parameter | Value | Class |
|---|---|---|
| First-version thread specifications | M6×1 / M10×1.5 / M16×2 | Standard |
| Tap-drill formula | Major diameter − pitch (steel); soft material −0.5×pitch | Empirical |
| Thread form | 60° V-form, flat crest and root | Standard |
| Tapping chip-breaking | Back a quarter turn per half turn | Hard rule |
| Defined-torque pull line | 200 mm from center, one-hand pull band (≈3–4 kgf·m, M10) | Empirical, calibrated to failure values |
| Pin interference | 0.01–0.03 mm ("easy first, tight last" feel) | Empirical |
| Taper-pin taper | 1:50 | Standard |
| Interference sleeve fit | Bore at −0.05 mm class, hot shrink | Empirical |
| Go/no-go gauge scrap | Go end will not go, or no-go end goes | Criterion |
| Micrometer repeatability | Range of ten measurements on one part ≤0.01 mm | L2 criterion |
| Sampling rate | 10% of a batch | Empirical |
| Temperature discipline | Soak together ≥ half an hour; record measurement temperature | Hard rule |
| Gauge recheck cycle | Every 200 inspections or every month (whichever first) | Empirical, calibrated to misclassification rate |
| Gauge stock | ≥2 sets of working gauges per specification + 1 check gauge + sealed master gauge | Institutional |
| Key-width rule | Shaft diameter/4 rounded; double keys ×1.5, spline ×3–4 torque | Empirical, destructive-test calibrated |
| Spline post-chisel allowance | 0.3–0.5 mm; final check: 0.05 mm-class paper slip does not enter the key flank | Empirical, first-article calibrated |
| Tooth-thickness range | ≤0.05 mm across the teeth of one gear | Empirical, first-batch statistics |
| Gear backlash | Module ×3%–5% (measured by the lead-crushing method) | Empirical |
| Contact-pattern criterion | Mid-flank, ≥40% of face width | Empirical |
| Center-distance tolerance | ±0.05 mm/100 mm (measuring-rod method) | Empirical, trial-assembly calibrated |
| Gauge-block set | 1/2/5/10/20/50, six blocks; one stack ≤4 blocks | Institutional |
| Gauge-block parallelism | Four-corner range ≤0.002 mm; aging ≥7 days | Empirical, first-batch statistics |

## Failure Modes and Diagnosis

| Symptom | Candidate causes (by probability) | Verification | Action |
|---|---|---|---|
| Nut will not thread onto a same-specification screw | Thread form/pitch out of tolerance; tolerance zones designed without clearance | Recheck with thread gauges | Re-cut the thread; revise the tolerance zones |
| Tap twists off during tapping | Tap drill too small; not square; chips not backed off | Check the three items in order | New part, re-drill, re-tap; restate the discipline |
| Threads slip after tapping | Tap drill too large; soft-material formula misapplied | Re-measure the tap drill | Redo one specification larger |
| Bolt loosens in service | No locking used; torque insufficient | Tightening items on the inspection checklist | Double nut/wire lacing; defined-torque line |
| Bolt fractures | Overtightened (past the failure value); vibration fatigue | Read the fracture location (neck = overtightened) | Lower the torque band; change the locking method |
| Pin will not drive in | Interference too large | Trial-fit with gauge blocks | Re-ream the hole |
| Pin works loose | Interference insufficient ("loose all the way in") | Recheck by feel | Go one pin size up |
| Batch dimensions shift suddenly | Tool wear; gauge wear | Compare the first article against history; send the gauge for calibration | Change the tool; recondition the gauge |
| Micrometer reading drifts | Hand heat; dust in the ratchet | Remeasure a cold part; disassemble and wash | Hold the frame, not the anvil; clean |
| Parts from two workshops will not assemble | Drift of each side's references; drawing versions inconsistent | Cross-check gauge blocks; check drawing versions | Complete the five interface items of Chapter 42 |
| Gauge blocks will not wring (no hold when pushed together) | Oil film/sweat fingerprints; edge burrs; fine lapping incomplete | Dry-wipe twice with silk cloth and re-wring; drag the edges across a copper plate to deburr and re-wring | Still no hold = back to the plate and re-lap that face |
| Spline push-in binds | Barrel-shaped key flanks (file rocking); key indexing out of tolerance; key-flank burrs | Color-mark and read the spot positions; connect lines on both faces to verify the indexing | Barrel shape = color-spot fitting; indexing wrong = scrap and re-layout; burrs = dress the edges with an oilstone |
| Gear center distance out of tolerance (abnormal backlash) | Housing bores misplaced; worn rods misread; wrong assembly shims | Remeasure with rods + micrometer; cross-check rods against check rods | Correct the bores with fitted sleeves; send the rods for calibration; reselect the shims |

## Process Card Index

Cards 22-01 through 22-07 are all full eight-field cards, copyable as single sheets.

## Acceptance Criteria

- **L1**: publish the first-version thread standard (≥3 specifications) with 10 trial-assembly interchange groups all succeeding; one plug-gauge set and one snap-gauge set each calibrated against standard parts and passing; a batch of 20 parts all passing go/no-go inspection; one tap threading through 10 holes.
- **L2**: micrometer repeatability ≤0.01 mm (ten-measurement range on file); the periodic calibration system running for three months without a miss; tapping scrap rate <10% (records on file); the defined-torque line calibrated with destructive-test evidence.
- **L3**: all gauges locally remakable and traceable to the standard bar (closed loop); cross-site interchange of standard parts succeeding (two workshops assembling each other's parts, with the five interface items complete); temperature correction the workshop-wide default discipline. Evidence: calibration archives, interchange records, destructive-test records.

## Labor Hours, Manpower, and Consumables

| Item | Manpower | Hours (empirical values) |
|---|---|---|
| One tap (turn—flute—quench—straighten) | 1 person | 1–1.5 days |
| One go/no-go gauge set | 1 person | 2–3 days |
| One micrometer | 2 people | 5–8 days |
| A batch of 20 standard bolts (including first inspection) | 2 people | 2–3 days |
| Monthly calibration of all gauges | 1 person | Half a day/month |
| One gauge group (four gauges, including the check gauge) | 1 person | 8–12 days |
| One gauge block (rough lap—fine lap—calibration) | 1 person | 1–2 days |
| One match-fitted spline pair (4 keys, including the match-fitting shaft) | 2 people | 3–5 days |
| Consumables | Hardened steel stock, abrasives, oil | Entered in the Chapter 38 ledger |

## Safety Boundaries

- Gauges are forbidden as tools (no prying, striking, or doubling as layout scribers)—a demoted gauge is a demoted measurement system;
- Measure hot workpieces only after cooling (double risk: burns + ruined gauge);
- Rotate bare-handed gauge-block wringing every 10 min (oil contamination and hand-temperature drift);
- The workpiece must be clamped and fixed while tapping (a workpiece that spins along = hand injury); wear eye protection against broken-tap chips;
- Hot-shrink assembly: gloves dry and thick, hub/sleeve preheated evenly, assembly motion done in one go (never a hand in the bore).

## A. Existing Tool Inventory

Standard bars and the three-bar mutual check (Chapter 3); thread cutting and the master lead screw (Chapter 20); three plates and lapping (Chapter 20); hardened steel (Chapter 19); process record system (Chapters 4, 8).

## B. New Tools Added in This Chapter

The three-class error inspection language; the thread standard (thread form/pitch series/tolerance zones/**tap-drill table**) and thread go/no-go gauges; **taps, reamers, and tap wrenches (with the tapping chip-breaking discipline)**; **the defined-torque fastening line and the three locking methods**; **pin match-fitting hand-feel criteria, taper pins, and interference hot-shrink fitting**; the plug/snap gauge system; gauge-block sets and the wring test; angle blocks and the closure-error equal-division method; the process card + first-article inspection + sampling system; the reference pyramid and the periodic calibration archive; the micrometer (with ratchet constant pressure), vernier caliper, and lever comparator; **thread gauge-set serialization and the gauge-library system (master gauge/working gauge/check gauge, three tiers)**; **the key—double-key—spline torque upgrade route and the match-fitted spline process**; **the measuring-rod center-distance method and the backlash/contact-pattern double check**; **the gauge-block set (1/2/5/10/20/50) and the wringing system**.

## C. Unsolved Dependencies

Higher-grade gauge blocks (flatness and temperature-control limits); optical measurement (Chapters 24, 27); constant workshop temperature (after Chapters 13, 28); thread grinding (long term).

## Next-Step Dependencies

Chapter 27: the comparator and pointer mechanisms are the parent of the instrument industry. Chapters 31–32: motor parts are produced under this chapter's tolerance system. Chapter 34: wafer thickness and photomask dimensions are a far-generation extension of this chapter's measurement system. Chapter 36: a reproducible electronics industry = this chapter's system replicated in the electrical domain. Chapters 37–39: process cards, sampling, and calibration archives merge into the skill matrix and the inspection-checklist system. Chapter 42: tolerance callouts and version control are the drawing face of this chapter's system.
