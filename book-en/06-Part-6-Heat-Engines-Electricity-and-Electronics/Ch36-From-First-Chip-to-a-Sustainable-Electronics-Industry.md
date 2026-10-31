# Chapter 36: From the First Chip to a Sustainable Electronics Industry

## Chapter Objectives

Advance Chapter 35's "repeatable manufacture" into "a sustainable electronics industry": test circuits and the failure-analysis system, the ramp route from single devices to complex logic, packaging, connections, and heat dissipation, the manufacture and repair of basic electronic equipment, the chemicals-and-materials ledger of the electronics industry, the organization of the move from laboratory to stable production, and — equally important — **an honest list of "which modern technologies cannot yet be rebuilt"**.

## Minimum Prerequisites

| Capability | Source |
|---|---|
| Repeatable planar process and small-batch yield data | Chapter 35 |
| Electrical test system and instrument regime | Chapters 31–33 |
| Ceramic packaging, silver paste, bonding | Chapter 35 |
| Chemical supply lines (acids/HF/dopants/high-purity water) | Chapters 26, 34 |
| Process cards and version management | Chapters 4, 22, 35 |

## Capability Boundary

**What can be done:** line production of small-batch logic devices (ramp levels 2–3) and of the five classes of practical equipment; a closed loop of burn-in screening and failure analysis; a simple positive-pressure clean room; a monthly operating account.

**Explicitly cannot be done:** the items listed in the Section 36.8 list (submicron photolithography, ion implantation, ten-thousand-gate scale, the modern ecosystem, ultrapure continuous supply, the precision sensor family) — **the list itself is this chapter's honest boundary**.

**External dependencies:** Chapter 35 yield data (no production line without yield data); linkage with chemical supply-cutoff contingency plans (Chapters 26/34).

## Pre-Start Verification (check off item by item)

| # | Verification item | Criterion | Source |
|---|---|---|---|
| 1 | Planar process | Chapter 35 L2 (single-gate yield in double digits) | Chapter 35 |
| 2 | Test master | Four-array layout run through ≥3 furnace batches | This chapter |
| 3 | Electrical test system | Meters cleared by release slips; test-point voltage table regime on record | Chapters 27, 31–33 |
| 4 | Four-column chemical ledger | High-purity water/HF/acids/dopants each with "source – monthly consumption – stock – substitute" | Chapters 26, 34 |
| 5 | Clean room | Positive-pressure ventilation + two-stage filtration built (see 36.7) | This chapter + Chapter 13 |
| 6 | Burn-in bench | Fire-patrol regime in place for continuously powered stations | This chapter |
| 7 | Personnel | Two-person backup per workstation, target past halfway across the seven workstations | Chapters 41, 43 |

---

### 36.1 How to Manufacture Test Circuits

- **The test master (your own "test wafer")**: with every process revision, run the test layouts in the same furnace batch — diode array (oxidation/diffusion uniformity), resistor bars (sheet-resistance distribution), transistor array (β distribution), interconnect chains (metallization continuity and via yield) — **process problems must show up first on the test layouts before the production layouts' yield can possibly ramp**;
- Test circuit boards: copper-clad board (copper foil hot-pressed onto a wooden base board; materials per Chapters 17, 18) made into boards by the screen-print-etch method (a scaled-up version of Chapter 35's photolithography route) — the stage for soldering and assembly;
- The burn-in bench: rows of units powered on and baked (rated voltage, continuous power for days) — **infant-mortality devices die on the burn-in bench, not in the user's hands** (the basic screening method).

[Card 36-01 Test Master Run In-Furnace] (eight fields)

1. **Input materials**: the four-array test layout (20 isolated diodes, 10 resistor strips, 10 transistors, 20 serpentine interconnect lines; the layout runs in the same furnace as the product version); Grade A/B wafers (travel card with all five columns); the run's product wafers as controls.
2. **Tools required**: four-array mask (Chapter 35, 35.B.7 master/working-mask system, drawing number with the M prefix); probe station (microscope + micro-positioner + spring probes, 35.B.12); four-point probe (Card 34-04); moving-coil meter (Chapter 31, release slip valid); per-run batch record sheet (**one pen per array, one column per run**).
3. **Operating sequence and control points**: ① run the test master in the same furnace as the product wafers → ② measure sheet-resistance distribution on the resistor strips → ③ measure forward/reverse ratio diode by diode → ④ measure β and breakdown on the transistor array → ⑤ measure continuity on the serpentine lines (**open-line count = interconnect yield**) → ⑥ transcribe all four into the run's batch record and onto the four trend curves. Control points: **process problems must surface on the test master first, or product yield has no basis for climbing**; **the four-array layout must have run for ≥3 furnaces** before this chapter's pre-start verification passes.
4. **Empirical parameters and calibration**: the criteria come from the 36.9 interpretation table — diode forward/reverse median drift <30%; resistor-strip same-wafer range <15%; transistor array records the β median and distribution width; interconnect yield counted by open lines. Four curves drawn over one month make process drift visible on the sheet (same format as the 36.7 control chart). These figures are **empirical values that must be calibrated against this line's statistics**.
5. **Observations to record**: run number and date, item-by-item readings of the four arrays (median / range / open-line count), comparison with the previous three runs, failure pointers (a whole-array shift = furnace temperature or dopant batch variance; wide scatter = surface cleanliness; clustered opens = etching or step coverage).
6. **Pass / rework / scrap criteria**: pass = all four readings in band and the curves not drifting; rework = one item out of band (that run's product wafers are downgraded to witness wafers, the run record is reviewed, the run is repeated); scrap = all four out of band (judged a process-window failure: stop the line, investigate, scrap the whole product batch).
7. **Common failures and diagnosis order**: (1) diode forward/reverse ratio shifts across the array → first check furnace temperature → check dopant batch variance; (2) wide scatter on one wafer → first check surface cleanliness (water-film test, settling-dust count); (3) wide resistor-strip range → first check whether pre-deposition time ran away; (4) clustered interconnect opens → first check etching (undercut / lateral etch) → check step coverage.
8. **L1 / L2 / L3 evidence**: L1 = the test master run once in-furnace with all four array readings on file; L2 = ≥3 furnaces with the four curves able to show drift; L3 = array data cross-checkable against run and batch numbers, monthly trend charts bound into volumes, a second person reproducing from this card. **Boundary: this card judges only "is the process drifting"; sub-micron linewidth and in-line defect inspection are a generational metrology gap — see the 35.B.16 metrology list and the 36.8 table.**

### 36.2 How to Establish Device Testing and Failure Analysis

**The three-failure-questions regime**: for every failed unit, answer — at which process step did it die (process defect)? Under which kind of stress did it die (design margin)? At which hour did it die (infant mortality/wear-out)?

- Failure files: a three-level progression — numbering – appearance (recorded by magnifier/micro-photography) – electrical test data – teardown (decapping – microscopic examination – angled section lapping). Teardown is the "autopsy": cold joints, broken aluminum/silver layers, diffusion spikes, and oxide pinholes each have their own morphology; build a **failure atlas** (Chapter 2's illustrated-catalog idea transplanted to devices);
- Pareto discipline: rank each month's failures by type; **the top two types consume all corrective effort** (the most common mistake is changing five parameters at once, which cannot be attributed — the engineering form of Chapter 25's single-variable discipline).

[Card 36-02 Three Failure Questions and the Three-Level Autopsy] (eight fields)

1. **Input materials**: the failed unit (scene preserved, not re-powered); the run/wafer number and batch code from the time of failure plus the travel card; 1–2 good units of the same batch as controls; packaging material and consumables for dissection.
2. **Tools required**: magnifier and microscope (photographic record, Chapter 24); electrical test bench (moving-coil meter, release slip valid); opening tools (file / blade / hot stage, chosen by packaging level); bevel-and-polish jig (Chapter 20 lapping + Chapter 35, 35.B.10 staining); failure file forms and the **failure atlas**.
3. **Operating sequence and control points**: ① answer the **three failure questions** first — which process step did it die in (process defect)? which stress did it die of (design margin)? at which hour did it die (early failure / wear-out)? → ② number it and photograph the appearance → ③ reproduce electrically (record open/short and parameter shift) → ④ dissect in **three ascending levels**: opening → microscopic inspection → bevel and polish → ⑤ compare the morphology against the atlas (cold solder joints, silver/aluminium layer breaks, diffusion spikes, oxide pinholes each have their own look) → ⑥ file it and count it into the monthly Pareto. Control points: **the autopsy may not skip a level** (opening before photographing = evidence destroyed), and every level leaves a record.
4. **Empirical parameters and calibration**: the criterion is morphological comparison, not a number; **Pareto discipline: rank failures by type every month and spend all corrective effort on the top two types** (changing five parameters at once makes attribution impossible); work-hour empirical values: one furnace batch (master included) tested and filed by 2 people in 1 day; the monthly Pareto and control chart by 1 person in half a day — **empirical, to be corrected against this line's measurements**. Three packaging checks for returned units: bond wire broken (under- or over-pressure), glaze-seal crack (thermal differential), silver paste lifting (under-firing).
5. **Observations to record**: number, appearance features, electrical data, findings at each autopsy level, atlas morphology number, the three answers, disposition (change process / change design / extend burn-in), running count of the same type.
6. **Pass / rework / scrap criteria**: pass (analysis valid) = all three questions answered, morphology matched to the atlas, disposition justified; rework = insufficient evidence (re-photograph / re-measure, then re-judge — never guess); scrap (analysis void) = evidence destroyed (opened without records, destroyed by re-powering) — the unit counts in the tally but is not an analysis sample.
7. **Common failures and diagnosis order**: (1) the same failure keeps recurring → first check whether the top two Pareto types were actually corrected → then check whether several parameters were changed at once; (2) the three questions cannot all be answered → first check whether the travel card and run records are complete (a broken archive breaks the responsibility chain) → repair the record system; (3) no morphology visible after dissection → first check magnification and lighting → check the bevel angle → switch criteria per the atlas; (4) the verdict contradicts the field report → first check whether re-powering altered the scene.
8. **L1 / L2 / L3 evidence**: L1 = a failure file established with the first ten cases given the three-level analysis; L2 = the failure atlas taking shape, a monthly Pareto issued every month, corrective records for the top two types; L3 = the five-column repair monthly report feeding back (equipment number / failed location / failed component full code / batch code / disposition) plus a comparable "field failure rate × post-burn-in retention rate", a second person reproducing from this card. **Boundary: this card delivers failure attribution and morphological criteria; sub-micron defect localization and trace composition analysis are a generational metrology gap (35.B.16 metrology list, 36.8 table) and are not built here.**

### 36.3 From Single Devices to More Complex Logic

- The ramp ladder (move up one level only after each level's yield is stable):

| Level | Integrated content | Criterion |
|---|---|---|
| 1 | Single gate (Chapter 35) | Yield in double digits |
| 2 | Gate + gate (flip-flop) | The two gates interact correctly |
| 3 | Adder/register | Truth table/timing passes |
| 4 | Simple oscillation and counting | Frequency division correct |
| 5 | Small sequential control | A practical post replacing relay logic |

- **The relay-and-discrete-transistor transition strategy** (do not force it): relays for low-speed control and heavy-current interfaces (Chapter 33); chips only for the logic core — the two device classes are mixed by "cost × reliability × speed"; this was the norm across decades of electronics history, not a compromise;
- Memory route registration: magnetic cores (ferrite rings + threaded wires; ferrite direction per Chapter 23) in parallel with flip-flop arrays — **in the short term do not count on semiconductors to unify memory density**.

### 36.4 Packaging, Connections, and Heat Dissipation

- Packaging tiers: test pieces (wax seal + glass cap); small batch (ceramic DIP: porcelain body per Chapters 11–12 + silver-paste wiring + glazed-seal lid); harsh environments (oil immersion/resin potting);
- The connector library: pins and sockets (stamping/casting per Chapter 17 + standard parts per Chapter 22), wiring-harness color codes (pigments per Chapter 8) — **connection reliability is whole-machine reliability** (historical data: the bulk of faults is always in connectors and solder joints);
- Thermal design: copper heat sinks for power components (fin-area estimates field-calibrated against the "hand-temperature red line", Chapter 27), ventilation paths (Chapter 13's architectural thinking in miniature) — **heat is the second killer of electronic devices (after dust)**.

### 36.5 How to Manufacture and Repair Basic Electronic Equipment

First batch of practical equipment (ranked by settlement value):

1. **Telegraph terminals** (the complete lineage of Chapters 30–32: sounder code → relays → crystal/tube detection) — communication is coordination;
2. Power rectifiers (vacuum diode/selenium alternative routes registered) — turning the grid into laboratory power;
3. Simple instruments (mass-producing the moving-coil meter: movement per Chapter 27 + meter core per Chapter 31) — the re-diffusion of measurement capability;
4. Alarms and control (water level/fire alarm/timing sequences) — automatic control entering daily life;
5. Audio amplification (carbon-granule microphone + transistor + iron-diaphragm speaker) — morale engineering (not to be underestimated).

**The repair regime**: every unit gets drawings + a component list + a test-point voltage table (the "medical record card"); the repair shop keeps a three-tier spare-parts stock (wear-prone/common/slow-turnover); **repair data flows back by design** — what failed where and why, fed monthly into the Section 36.2 failure analysis.

### 36.6 The Chemical and Material Systems the Electronics Industry Depends On

**The electronics-chemistry ledger (inventoried monthly)**: high-purity water (largest consumption), HF, sulfuric/hydrochloric acid, dopants, solvents (alcohol/turpentine), photosensitive materials, silver and gold (bonding wire) — each listed in four columns: "source – monthly consumption – stock – supply-cutoff substitute"; the **supply-cutoff substitution plan** is the core of industrial resilience (example: an HF cutoff = the etching line stops → the glass shop's fluorspar stock links to Chapter 26's red-line reserve).

The materials division-of-labor table: quartzware (Chapters 14, 34), ceramics (Chapters 11–12), glass (tube envelopes), metals (copper/silver/iron/nickel), organics (wax/resin/paper/silk mesh) — the electronics industry is the **master customer of the whole book's materials lineage**; a supply-cutoff shock propagates backward along the dependency graph (this is the monthly live exercise of the general outline's "four questions of the tool lineage").

### 36.7 From Laboratory Manufacture to Stable Production

**The simple clean room (dust is the number-one killer of electronic devices)**:
- **Positive-pressure ventilation**: a fan supplies air to the room through two-stage filtration (rough filter: wet burlap/felt layer to block coarse dust; fine filter: multilayer fine cloth/paper filters), with **indoor pressure slightly higher than outdoor** — air leaks outward through the door gap instead of dust leaking inward. Acceptance criterion (◎ rule-of-thumb method): hold a fine thread at the door gap; the thread drifting outward = positive pressure established; drifting inward = fan failure or clogged filter;
- Airlock and clothing change: enter through a small transition room first; outer garments are not carried in; workstations are kept away from the door;
- The wet-mopping regime: wet-mop daily (dry sweeping that raises dust = a crime); wipe vessels before they enter or leave;
- Personnel discipline: no woolen garments inside (they shed fibers); no touching crystal faces with bare hands during operation (finger cots/tweezers);
- The graduated regime: photolithography and diffusion stations are strictest (a small positive-pressure room); test and packaging stations are more lenient — **spend clean-room resources where they matter most**.

**The batch yield control chart (the yield dashboard)**:
1. Record every furnace batch: wafers started → survivors at each process step → final good units; a per-step yield table;
2. Plot per-furnace yield as a **control chart** (furnace number on the horizontal axis, yield on the vertical axis; center line = the mean of the last 10 furnaces; upper and lower control limits = mean ±3σ (±2σ serves only as a warning line); empirical values that must be field-calibrated);
3. Reading rules: a single point beyond a control limit = a special cause in that furnace (check that furnace's records); 5–7 consecutive points drifting the same direction = the process is degrading systematically (check abrasive/reagent/temperature-control drift, Chapter 39);
4. **The discipline of the yield ramp: change one variable at a time, then watch the control chart for 10 furnaces before judging** — an "improvement" that changes five parameters at once cannot be attributed (sister clause of the Pareto discipline).

**The organizing three-piece set (the final form of Chapter 4's regime)**:
1. **Line division of labor**: seven workstations — cleaning/oxidation/photolithography/diffusion/metallization/testing/packaging — each station's process card on the wall, first-article inspection + sampling checks (Chapter 22's regime implemented in full);
2. **The personnel ladder**: three tiers — apprentice – technician – process engineer — with two-person backup at every critical workstation ("sick leave must not paralyze the line");
3. **The monthly operating account**: inputs (power/chemicals/labor hours) × outputs (good units/grades) + the failure Pareto — **the electronics industry must be as auditable as a farm** (the electronics page of Chapter 38's energy-and-materials account).

[Card 36-03 Simple Clean Room: Positive Pressure and Acceptance] (eight fields)

1. **Input materials**: a closable small room (Chapter 13 building thinking in miniature, doors and windows closable); coarse filter material (wet burlap / felt layer); fine filter material (multi-layer fine cloth / paper filter); oilcloth (floor); wiping cloths and wet-mop gear; glycerol-coated slides (settling-dust count); a length of fine thread (positive-pressure criterion).
2. **Tools required**: supply fan + two-stage filter box (Chapter 13 ventilation); adjustable airflow (set by the door-gap thread criterion); magnifier; staff dress (no wool garments; finger cots / bamboo tweezers).
3. **Operating sequence and control points**: ① fit the two filter stages (coarse catches big dust, fine catches fine dust) → ② the fan supplies air into the room so that **indoor pressure is slightly above outdoor** → ③ acceptance: hold a fine thread at the door gap — **thread blows outward = positive pressure holds; inward = fan failed or filter clogged** → ④ airlock and changing (enter through a small transition room, outerwear stays outside, work positions away from the door) → ⑤ **wet-mop daily** (dry sweeping raises dust = an offence; wipe vessels on the way in and out and keep them covered) → ⑥ count settling dust daily (glycerol-coated slide laid flat 1 h, then count particles) → ⑦ grading: photolithography and diffusion positions strictest (positive-pressure cubicle), test and packaging positions looser. Control points: the positive-pressure check is done **before anyone enters**, not once at commissioning.
4. **Empirical parameters and calibration**: the criterion is **the thread at the door gap blowing outward** (the only field criterion that works without a pressure gauge); settling dust is checked daily by "glycerol-coated slide laid flat 1 h, particles counted," with the baseline built for this room (**empirical, must be calibrated**); filter replacement is triggered by "the thread turning from outward to inward" or a rising particle count, never by the calendar. **Boundary: laminar-flow filtration and particle-count monitoring (a modern cleanroom) are not built by this card — outside the capability line (35.B.16, item 1).**
5. **Observations to record**: daily positive-pressure verdict (outward / inward), settling-dust count, wet-mop and wiping execution, dress-code violations, filter replacement dates, shift temperature and humidity, correlation with this room's yield.
6. **Pass / rework / scrap criteria**: pass = the door-gap thread blowing outward every day and the settling-dust count inside this room's baseline; rework = thread blowing inward (check clogged filter / fan / door-seal leaks, re-verify after repair), count above baseline (mop more often, change the fine filter); scrap (decommission) = still inward after repair, or the room's yield data shows dust as the dominant cause and it cannot be brought down.
7. **Common failures and diagnosis order**: (1) contamination at the same spot on devices → first apply the door-gap thread test (has pressure been lost?) → check for bare-hand contact → repair the fan and change filters, restate the discipline; (2) settling-dust count rising day by day → first check whether the fine filter is due → check whether mopping stopped → check staff dress; (3) pressure intermittent → first check fan power and belt → check the door seal → check whether the two filter stages are fitted backwards; (4) yield does not improve with cleanliness → the dominant cause is not dust (switch to reagent batch variance and temperature control).
8. **L1 / L2 / L3 evidence**: L1 = one positive-pressure acceptance passed (outward-thread record) + a settling-dust baseline established; L2 = a full month of daily records, documented filter changes, and a comparable yield-versus-dust-count record for the room; L3 = cleanliness grading (strict / loose zones) in force, dress and mopping spot checks bound into a file, a second person reproducing from this card.

[Card 36-04 Batch Yield Control Chart] (eight fields)

1. **Input materials**: per-run charge count, survivors after each process step, final good-unit count (step-by-step yield table); run and batch numbers (matched to travel cards and master records); the previous 10 runs' yield data (to set the center line).
2. **Tools required**: per-run batch record sheet (charge → survivors → good units, three columns); control-chart paper (run number on the horizontal axis, yield on the vertical); calculating aids (Chapter 3 slide rule / longhand, for mean and σ); monthly Pareto sheet (shared with Card 36-02).
3. **Operating sequence and control points**: ① record survivors by process step for each run → ② compute step yields and final yield → ③ plot on the control chart: **center line = mean of the last 10 runs, control limits = mean ±3σ (±2σ is a warning line only)** → ④ read the chart by the interpretation rules → ⑤ send abnormal runs back through the run record (three checks: contamination / reagent batch variance / temperature control) → ⑥ summarize monthly into the operating account. Control points: **one point per run, points may not be pooled**; after a process change, start a new segment rather than mixing it into the old one.
4. **Empirical parameters and calibration**: limits from the last 10 runs' mean ±3σ, with ±2σ as warning only (**empirical, to be calibrated to this line's run count and spread**); interpretation: **a single point outside a control limit = a special cause in that run**; **5–7 consecutive points drifting one way = the process is degrading systematically** (check abrasive / reagent / temperature-control drift); **single-variable window: change one variable at a time and watch 10 runs on the chart before judging** — an "improvement" that moves five parameters at once cannot be attributed.
5. **Observations to record**: run number, charge count, survivors per step, step yields, final yield, mean and σ, marked out-of-limit points and drift segments, the run's three-check conclusions, the change made and the run where it took effect.
6. **Pass / rework / scrap criteria**: pass = the chart in control (no points outside limits, no 5–7-point one-way drift); rework (disposition) = single point outside → review that run's record and file a failure analysis; systematic drift → replace items one by one (clogged filter / abrasive-grade contamination / aged vessels) and start a new segment; scrap (stop decision) = no convergence after item-by-item replacement, or yield falling below the line's accountable floor — stop the line and re-assess the process window.
7. **Common failures and diagnosis order**: (1) yield collapses in a single run → first run the three checks on that run's record (contamination / reagent batch / temperature control); (2) yield falls run after run → interpret as drift, first check clogged filters and abrasive-grade contamination → check vessel aging → check temperature-control drift; (3) yield drops after a change → first check whether something else was moved at the same time (single-variable discipline broken) → roll back and redo; (4) no trend visible on the chart → first check whether points were pooled or run numbers mis-recorded.
8. **L1 / L2 / L3 evidence**: L1 = one control chart built over 10 consecutive runs; L2 = chart and monthly Pareto in the same volume, out-of-limit runs with attribution records, 10-run observation records after every change; L3 = the monthly operating account (input × output + failure Pareto) accountable for half a year, a second person reproducing from this card. **Boundary: this card only makes drift visible and attributable; climbing to ten-thousand-gate yields is the exponential patience listed in the 36.8 table, beyond this card.**

### 36.8 Which Modern Technologies Cannot Yet Be Rebuilt

**The honest list (the boundary within this settlement's generation)**:

| Technology | Blocker | Unlock route |
|---|---|---|
| Submicron photolithography | A generational gap in optics and photosensitive materials | Decades of iteration on photomask–lens–chemistry |
| Ion implantation | Equipment complexity | Long-term accumulation of diffusion processes as the substitute |
| Large-scale integration (ten-thousand-gate class) | Yield × cleanliness × metrology | The exponential patience of the yield ramp |
| The modern storage and computing ecosystem | A co-evolved hardware–software division of labor | Generations of accumulated population and specialization |
| Continuous ultrapure gas/chemical supply | Analytical and engineering systems | Generational extension of the Chapter 26/34 routes |
| The precision sensor family | Compounded materials and processes | Gradual growth alongside the whole-machine industry |

**Stating the boundary is not surrender; it is a roadmap**: when the next generation opens this section, they should know that each row's "unlock route" is their list of problems to attack — the final form of this manual is to let the reader know clearly: **what we hold now, what we can build next, what is still missing, and which dreams must be left to those who come after.** (The closing of the general outline's Chapter 1 "ultimate standard".)

---

### 36.9 The Test Master: Four-Array Layout and Item-by-Item Interpretation

The test master is not "just throw it in the batch" — the four arrays each carry explicit interpretation criteria (recorded per furnace batch):

| Array | Layout | What it checks | Pass interpretation | What failure points to |
|---|---|---|---|---|
| Diode array | 20 isolated diodes | Oxidation/diffusion uniformity | Forward/reverse ratio recorded unit by unit; median drift <30% | Whole-batch drift = furnace temperature/dopant batch difference; large scatter = surface cleanliness problem |
| Resistor bars | Long-bar diffused resistors ×10 | Sheet-resistance distribution | Spread within one wafer <15% (empirical value) | Drift = predeposition time out of control |
| Transistor array | 10 devices | β distribution and breakdown | β median and distribution width recorded | Wide = uneven base diffusion |
| Interconnect chains | Serpentine metal lines ×20 | Metallization continuity and vias | Continuity test: the number of broken chains is the interconnect yield | Break points clustered = corrosion/poor step coverage |

Interpretation regime: **one pen per array, one column per furnace** — four curves drawn over a month; process drift shows itself on the chart (same format as the Section 36.7 control chart).

### 36.10 Three-Tier Packaging Process in Detail

- **Tier 1 · wax seal + glass cap (test pieces)**: the die is silver-paste sintered onto a porcelain substrate → wire bonding (thermocompression: fine silver wire pressed onto aluminum/silver pads, ◎ hand-feel — pressure judged by "the wire deforms but does not break"; practice method: bond 50 points on scrap dies and record the pull-to-break force) → glass cap wax-sealed. Life target: days-class (for verification only);
- **Tier 2 · ceramic DIP (small batch)**: dual-inline porcelain cavity (porcelain parts per Chapters 11–12), silver-paste wiring, die sintering, bonding, glazed-seal porcelain lid — glaze-seal criterion: continuity retest unchanged after 10 min in boiling water (initial hermeticity check);
- **Tier 3 · potting (harsh environments)**: machine-level devices potted in resin/bitumen — electrical testing must be completed before potting (nothing can be repaired after potting); potting bubbles are removed by vacuum impregnation (reusing the Chapter 33 vacuum bench).

The three packaging failure checks (inspect rework units for these first): broken bond wire (under/over thermocompression), glaze-seal cracks (thermal gradient), silver-paste delamination (insufficient sintering).

### 36.11 Acceptance Criteria Table for the First Five Classes of Equipment

| Equipment | Core criteria (L2 delivery line) |
|---|---|
| Telegraph terminal | Two-point transmission/reception of 100 code groups, error rate <2% (empirical value); contact life ≥10⁵ operations by sampling test |
| Power rectifier | Output ripple invisible to the eye as lamp flicker; full-load voltage drop <10% |
| Moving-coil meter | Reading difference against a reference meter (a master meter calibrated by a copper coulometer) <5%; daily zero drift <half a division |
| Alarm controller | 20 simulated triggers: 0 false alarms, 0 missed alarms |
| Audio amplifier | Speech intelligible (human-ear acceptance + two-person intercom for 10 minutes at a no-fatigue level) |

Every unit ships with a "medical record card": drawing number, component list, **test-point voltage table** (marking each point's normal voltage range) — the repairer checks point by point against the card (using Chapter 32's three-piece test set).

### 36.12 Electronics Chemistry Four-Column Ledger Template (Monthly Inventory)

| Item | Source | Monthly consumption | Stock | Supply-cutoff substitution plan |
|---|---|---|---|---|
| High-purity water (largest consumption) | Chapter 26 distillation line | ___ L | ___ | Lowest line-stop priority, fastest to restore |
| HF | 23.9 + fluorspar (Chapter 26 red-line reserve) | ___ | ___ | **Fluorspar stock linkage**: when HF stock falls below 2 months, fluorspar purchasing is locked immediately |
| Sulfuric/hydrochloric acid | 23.9 | ___ | ___ | Green vitriol / saltpeter earth as two mutually backing sources |
| Dopants (boron/phosphorus sources) | Chapters 23/26 | ___ | ___ | No substitute — **stock red line 6 months** |
| Silver (bonding wire/silver paste) | Chapter 17 by-product recovery | ___ | ___ | Recover silver from scrapped devices |

Rule: **the fifth column must be filled in for every chemical at the moment it enters the store** — the supply-cutoff plan is part of the warehousing procedure, not a meeting agenda item for after the fact.

---

### 36.13 The Component Library and Naming Conventions

**The preferred-value series table (fix the shelf first, then design the circuit)**: self-made resistors (wirewound/diffused) and capacitors (paper-wax/mica) are not produced one by one to each circuit's calculated values; they take values from standard series — **at design time, snap values to the nearest series value and let the components constrain the drawings in return**:

| Series | Values per decade | Paired tolerance | Applicable positions |
|---|---|---|---|
| E3 simplified series | 1.0 / 2.2 / 4.7 | ±50% (wide) | Wide-tolerance positions: filtering, bleed, coarse bias setting, etc. |
| E6 extended series | 1.0 / 1.5 / 2.2 / 3.3 / 4.7 / 6.8 | ±20% | Critical positions: divider ratios, gain calibration, etc. |

Stock reserve: resistors 10 Ω–1 MΩ, capacitors 500 pF–2 µF, with ≥20 pieces in stock per value step (empirical value; rechecked as twice the previous month's requisition consumption); any value step touching the red line of two months' consumption goes onto next month's production order — inventoried the same day as the Section 36.12 chemistry ledger: one desk, two ledgers.

**The naming rule (class – value – batch, three segments)**: every component entering the store gets a label —
- Class code: R resistor, C capacitor, L inductor, D diode, T transistor, X connector;
- Value code: a letter stands in for the decimal point (4K7 = 4.7 kΩ, 2U2 = 2.2 µF); devices without a nominal value, such as D/T, instead carry a grade number (T-3 = third grade by β median; grade boundaries are revised yearly against the Section 36.9 transistor array data);
- Batch code: four digits for year and month (2603 = March of year 2603), traceable back to that furnace batch's master record (36.1).

Example: **R-4K7-2603** = a 4.7 kΩ resistor of the March-2603 batch. If any of the three segments is missing from the label, the storekeeper has the right to refuse issue — a component with an incomplete name is a component of unknown origin.

**Shelving and requisition registration**:
- Shelves are divided into cells by "class × series value", and each cell label is a printed specimen of the naming rule; one tray per cell; a mixed cell is reported as an incident;
- Requisition slips have five columns: equipment number / full name code / quantity / requisitioner / purpose; accounts are reconciled against slips at month-end; **the ledger's decrease must equal the number installed**, and any shortfall is traced slip by slip;
- First in, first out: for one value held in several batches, the earlier batch is issued first — only then does failure analysis have a traceable "batch × operating hours" data chain;
- Substitution rule: when a value step is out of stock, nearest-neighbor substitution is allowed, but **the substitution must be written back to the medical record card and the component list on the spot** (the source gate of Section 36.16's drawing-vs-reality consistency clause).

### 36.14 Printed-Circuit Board Process in Detail

**Self-made copper-clad board**: copper foil (0.05–0.1 mm thick, rolled or electrolytic by-product, Chapter 17) + base board (five layers of 1–2 mm thin boards crossed lengthwise and crosswise, impregnated with phenolic or tung-oil resin; laminating experience inherited from Chapter 18), hot-pressed into a board. Hot-press parameters (empirical values): 140–160 °C, hold 20–30 min, with screw rods at the four corners plus hardwood spacer blocks distributing the pressure evenly. **Field-calibration method**: make three trial press boards from the same batch of material, processed at three settings — 130 / 150 / 170 °C — and run a crosshatch check after cooling: scribe a 1 mm square grid with the knife tip cutting fully through the copper foil; the setting at which fingertip peeling lifts no skin is the qualified one. Transcribe the qualified setting's parameters into the ledger and copy them thereafter without retesting. Two board-surface acceptance checks: a water film on the copper face that stays unbroken for 30 s = cleanliness passed; with a steel straightedge held against the face and measured across the diagonal, warp <5 mm/m.

**Comparison of the two board-making methods (both are scaled-up applications of Chapter 35's photolithography route)**:

| Method | Resist film | Minimum line width (empirical value) | Boards per run | Suitable for |
|---|---|---|---|---|
| Photoresist method | Chapter 35 photoresist + development | 0.5–1 mm | A few boards | Test master boards, dense-trace boards |
| Screen-print method | Silk-screen stenciled resist ink (asphalt-varnish family) | 1.5–2 mm | Dozens of boards | Batch production of coarse boards |

Board selection rule: line width <1.5 mm or more than 50 traces → the photoresist method; everything else → screen print without exception — **photoresist is slow but precise, screen print fast but rough; using the wrong direction wastes yield** (Chapter 25's "match, don't maximize").

**Drilling and annular rings**: uniformly etch first, drill second — the residual copper traces on the copper face serve as drill-template guides, so the drill wanders less. Center-punch the points, then start the holes with a hand drill (Chapter 22's bench-work hole-starting method); use only two hole sizes, 1.0 and 1.5 mm, to reduce bit changes and wrong fits. Annular ring (pad) design: ring outer diameter ≥ hole diameter + 2 mm, i.e., ring width ≥1 mm (empirical value, including margin for hand-drilling eccentricity). Three-way criteria: with eccentric drilling, a narrowest remaining ring ≥0.5 mm = pass; a broken ring with the trace still continuous = reworkable (solder a loop of fine copper wire along the remnant ring); a broken trace = scrap and remake.

**Single-sided boards only (the honest boundary)**: double-sided boards require through-hole metallization — electroless copper on hole walls needs palladium activation and an electroless copper plating line, which this generation cannot build; **place it on the Class-C list**. The routing rules therefore harden: on a single-sided board traces must not cross; crossings are jumped with a jumper wire, **≤10 jumper wires per board** (empirical value; exceeding the limit means the layout fails and goes back to the artwork for rearrangement — no "a few more jumper wires would still work"). Mirror check before committing a board: the solder-side routing drawing is drawn mirrored from the copper face, and two people each verify it before the board is made — a mirror error, once it appears, scraps the whole board; it is the most expensive error.

[Card 36-06 Self-Made Copper-Clad Board] (eight fields)

1. **Input materials**: copper foil 0.05–0.1 mm (rolled or electrolytic by-product, Chapter 17; hold it against the light — no pinholes or sand holes); base board, five layers of 1–2 mm thin board crossed lengthwise and crosswise (impregnated with phenolic or tung-oil resin, laminating experience inherited from Chapter 18; press it with a finger beforehand — no liquid should ooze out); resin mixed fresh for the job (leftover glue from overnight is discarded); hardwood spacer blocks (to spread the load at the four corners).
2. **Tools required**: hot-press frame (cast-iron platens + four screw rods, Chapters 17–18 foundry/forge/woodwork); kiln-mouth waste-heat position or a drying oven (Chapter 12 furnace-temperature management); thermometer (Chapter 25 calibrated piece, platen temperature logged every 10 min); crosshatch knife and a 1 mm grid template; steel straightedge (water-film and warp checks); centre punch and hand drill (1.0 and 1.5 mm bits only); fine sand and degreaser (copper-face preparation).
3. **Operating sequence and control points**: ① cut to size — foil and base board cut with an edge allowance to the board drawing → ② degrease the copper face with fine sand and verify cleanliness by the water-film test (**unbroken for 30 s**) → ③ stack — copper face outward, five thin boards crossed lengthwise and crosswise, four-corner screw rods with hardwood spacers spreading the pressure → ④ hot-press — 30 min up to the setting → hold 20–30 min → ⑤ **cut the heat and cool naturally; opening the press for a fast cool is forbidden** (fast cooling means delamination) → ⑥ take out the board, crosshatch + water-film recheck, measure warp with the straightedge held across the diagonal → ⑦ transcribe the parameters into the batch ledger. Control points: the heat-up rate counts as much as the hold time (copy the three-board gradient setting once fixed); **uneven pressure (a missing spacer) is the number-one cause of blistering**.
4. **Empirical parameters and calibration**: hot-press **140–160 ℃, hold 20–30 min**; **field-calibration method** — press three trial boards from the same batch of material at 130 / 150 / 170 ℃, and after cooling run the crosshatch: a 1 mm square grid scribed with the knife tip cutting fully through the foil, where fingertip peeling lifts no skin, marks the qualified setting; transcribe that setting into the ledger and copy it thereafter without retesting. Two board-surface acceptance checks: water film on the copper face unbroken for 30 s, and warp <5 mm/m measured across the diagonal with the straightedge against the face; annular ring outer diameter ≥ hole diameter + 2 mm (ring width ≥1 mm). All of these are **empirical values that must be calibrated to local conditions** — resin grade, moisture content of the thin boards and the platens' heat capacity all shift the qualified setting.
5. **Observations to record**: platen temperature every 10 min; colour of resin bleed at the edges (pale yellow = normal, dark brown = overheated); blister location and area; crosshatch result (lifting or not, grid count); water-film standing time; warp reading; source batch numbers of foil and resin — all into that batch's card.
6. **Pass / rework / scrap criteria**: pass = crosshatch shows no lifting (no skin lifts on a 1 mm grid under a fingertip) + water film unbroken for 30 s + warp <5 mm/m; reworkable = local blistering — cut it out, keep clear of the trace area and use the board downgraded; scrap = delamination or widespread blistering (remake the board), or pinholes in the foil (missed before etching, certain to open a trace afterwards).
7. **Common failures and troubleshooting order** (by frequency): (1) blistering → first check whether the base board was dried through (moisture — the commonest false "resin problem"), then whether a spacer was left out (uneven pressure), and finally the resin ratio and whether overnight leftover glue was used; (2) poor adhesion, crosshatch lifting → first check the copper-face degreasing (a failed water film means under-degreased), then whether the setting ran low; (3) delamination → check whether the press was opened for a fast cool, and whether the hold time was long enough; (4) warp out of tolerance → check whether the five thin boards really crossed lengthwise and crosswise, and whether cooling was even (one side chilled); (5) traces open after etching → check the foil for pinholes (a skipped against-the-light inspection).
8. **L1 / L2 / L3 evidence**: L1 = the first board kept as a wall sample + its crosshatch and water-film record; L2 = three consecutive boards' crosshatch records on file with the setting and hold time in the same table; L3 = the parameters transcribed into the batch ledger with foil/resin source batch numbers attached, and a second person pressing a board from this card alone passing the crosshatch and water-film acceptance.

### 36.15 Whole-Machine Burn-In and Field Deployment

**Burn-in bench tiers** (turning the Section 36.1 burn-in bench into a formal procedure):

| Tier | Conditions | Duration (empirical value) | Coverage | Criterion |
|---|---|---|---|---|
| Ambient tier | Full-load power at room temperature, test points recorded every 24 h | 72 h | All units | No opens or shorts; key test-point drift <5% |
| High-temperature tier | Powered inside an insulated box at 50–60 °C | 24 h | All harsh-environment posts; 10% sample of routine batches | Same as above, and power components stay within the hand-temperature red line (Chapter 27) |

The high-temperature source is a kiln-mouth waste-heat warming room or a flue-gas warming box (kiln-temperature experience per Chapter 12): hang thermometers at three points inside the box; if the readings at any two points differ by <5 °C at 10 min, the box temperature passes; retest once at each change of season. **A burn-in run whose records have a gap (more than 1 missed recording point) is treated as not burned in, and the clock restarts** — the cost of rerunning will itself force the watch-keeping discipline into being.

**The deployment kit's three protections** (a universal base kit + heavier additions per the environment editions of Part 10):
- Universal base kit: moisture protection = wax-paper wrapping + desiccant (quicklime in cloth bags, replaced as soon as it cakes with absorbed moisture); dust protection = cloth cover + oiled paper over the openings; vibration protection = the wooden box lined and stuffed full with wood shavings/felt — **a silent shake test is the packing acceptance criterion** (shake the wooden box; no sound of objects shifting inside);
- Environment aggravation items (the details of each environment edition follow Part 10):

| Environment | Primary threat | Deployment kit additions | Details |
|---|---|---|---|
| Island/coastal | Salt fog and humidity | Resin potting + wax-sealed outer cover; desiccant replaced monthly | Chapter 50 |
| Desert | Dust and static | Double-layer oiled paper, felt filter on air intakes, dust blown out weekly | Chapter 51 |
| Permafrost | Low-temperature brittle cracking | Thick felt lining; a warm-up-30-min-before-power-on procedure | Chapter 52 |
| Rainforest | Mold and moisture | Full potting; lime-wash brushed on the wooden box's inner walls | Chapter 53 |

**The transport and installation acceptance sheet** (one per box, signed for by two people):
1. Unpacking inventory: box lining intact; the three-piece set (36.16) and the spare-parts bag complete;
2. Visual inspection: no transport cracks, potting uncracked, every terminal hand-tugged and retightened;
3. Before power-on: the measured supply voltage differs from the nameplate by <10%;
4. Power-on: first 10 min unloaded, then check point by point against the test-point card (meter ranges per Chapters 31–33);
5. Trial run: 30 min loaded; test points rechecked with no drift;
6. Dual-sign filing: the acceptor and the head of the using post both sign, and a copy enters the equipment file — **signing is the transfer of responsibility; no sheet, no machine accepted**.

[Card 36-05 Burn-In Screening] (eight fields)

1. **Input materials**: complete units or devices awaiting screening (electrically passed, medical-record card and three-piece set present); rated-voltage supply (Chapters 31–32); spares and record cards.
2. **Tools required**: burn-in rack (rows of powered positions, **fire patrol in the continuously powered area**); holding oven or kiln waste-heat warm room (high-temperature tier, Chapter 12 furnace experience); three-point thermometer set (oven uniformity); test-point voltmeter (Chapters 31–33 meter ranges); timer and inspection log.
3. **Operating sequence and control points**: ① set conditions by tier: **ambient tier = full-load powered at room temperature for 72 h (all units), test points read every 24 h; high-temperature tier = 50–60 ℃ in a holding oven for 24 h (all units for harsh-environment posts, 10% sampling for routine batches)** → ② verify oven temperature first: hang three thermometers, **any two reading within <5 ℃ over 10 min** means the oven passes (re-check at season change) → ③ power up for continuous burn-in → ④ log at each point → ⑤ re-measure test points off the rack → ⑥ record the screening verdict. Control points: **a gap in the burn-in record (more than one missed reading) means the unit counts as un-burned-in and the clock restarts** — the cost of a rerun is what enforces watch discipline.
4. **Empirical parameters and calibration**: 72 h ambient for all units, 24 h at 50–60 ℃ for the high tier (**empirical, to be calibrated to this line's early-failure rate**); criteria: no open or short circuit, key test points drifting <5%; the high tier adds "power components below the hand-temperature red line" (Chapter 27). Duration calibration: **a first-month field early-failure rate <2% means screening is sufficient** (empirical, reviewed quarterly); if higher, first lengthen the ambient tier, then check deployment protection.
5. **Observations to record**: equipment number / batch code, tier, start and end times, test-point readings every 24 h, three oven thermometers, gaps and missed readings, off-rack re-measurement values, verdict and destination (release / downgrade / repair).
6. **Pass / rework / scrap criteria**: pass = no open or short circuit throughout, test-point drift <5%, record without gaps; rework (rerun) = record gaps or more than one missed reading (clock restarts as un-burned-in), a single point drifting over 5% but recovering on re-measurement (extend one tier and re-screen); scrap = failure during burn-in (entered in the failure file and analysed per Card 36-02), still drifting after re-screening.
7. **Common failures and diagnosis order**: (1) early failure in the field → first check whether burn-in was completed and long enough → check whether the record has gaps (equivalent to no burn-in) → extend burn-in; (2) power components overheating in the high tier → first check whether oven temperature exceeded 50–60 ℃ → check heat sinks (hand-temperature red line) → reduce loading density; (3) uneven oven temperature → first check the three-thermometer spread → check heat-source layout and air path; (4) clustered failures in one batch → check the batch code (component batch) → hand over to the Card 36-02 Pareto.
8. **L1 / L2 / L3 evidence**: L1 = one batch completing the 72 h ambient tier with a complete record; L2 = both tiers, oven verification and the rerun-on-gap rule all executed and filed; L3 = records correlating the first-month field early-failure rate with burn-in duration, the repair monthly report fed back into a bound volume, a second person reproducing from this card. **Boundary: this card screens out early failures; it does not improve design margin or wear-out life — that belongs to the design stage (the second question in 36.2) and is not built here.**

### 36.16 Drawing Archives and Succession

**The three-piece-set regime**: every in-service equipment type must have all three items — "whole-machine drawing — component list — test-point card" (the Section 36.11 medical record card made institutional); if any one is missing, new deployments of that type are suspended:
- Drawings: one whole-machine circuit diagram + one mirrored solder-side PCB routing diagram; drawing number = type number;
- Component list: every component listed with its full name code (36.13); substituted parts carry a star, with the substitution record attached;
- Test-point card: each test point's normal voltage/range listed point by point (meters per Chapters 31–33); made of thick cardstock, wax-sealed against moisture, and traveling with the machine.

Change discipline: **every revision must be made on the three-piece set on the spot, with the change column filled in** (four items: what changed / why / when / who approved) — "modify the machine first and patch the drawing later" counts as not changed at all. The three-piece set's material selection, transcription, and disaster-backup succession belong to the knowledge-media volume (Chapter 42); this chapter governs one thing only: **the content must never lag behind the physical machine**.

**The repair-data monthly report (feeding back into 36.2)**: the repair shop's monthly report has five columns — equipment number / failed location / failed component's full name code / batch code / disposition. At month-end it merges into the Section 36.2 Pareto for a **cross-comparison of field failure rate against post-burn-in survival rate**: when the field rate is clearly too high, cross-check by "batch × deployment environment" to distinguish insufficient screening from inadequate three-protection. The monthly report also calibrates Section 36.15's burn-in durations: a field first-month infant-mortality rate <2% (empirical value, rechecked quarterly) means screening is sufficient; if it is higher, first lengthen the ambient tier's duration, then check the deployment protections.

**The backup-unit regime**: critical posts (telegraph terminals, alarm control, water-supply control types) each get one backup unit:
- The backup unit is powered for 1 h every month and run through the test-point card point by point — **a backup unit that is never powered on equals no backup unit** (capacitor aging and contact oxidation spare no one);
- A primary/backup switchover drill once a quarter: the backup unit runs loaded until the next scheduled inspection, and the former primary moves to the repair slot;
- Linked with the three-tier spare-parts stock (36.5): parts for repair-slot replacements are drawn first from the "slow-turnover" tier, and each withdrawal goes onto the replenishment production order.
[Card 36-07  ] (eight fields)
1. **Input materials**: drawings on mulberry-bark paper or with waxed-face covers; component lists on ordinary machine-made paper; test-point cards on thick cardstock + wax seal; ink always water-resistant ink (fading-prone inks forbidden);
2. **Tools required**: drawing pens and straightedge templates (measurement and drafting per Chapter 3); meters (Chapters 31–33, cleared by release slips);
3. **Sequence and control points**: finalize the drawing → **two people cross-check the mirrored routing diagram** → count the component list item by item from the drawing (**never copy an old list**) → fill in the test-point card's values on the measured prototype → number the three pieces, bind them into the set, and shelve;
4. **Empirical parameters and calibration**: 2–3 person-days to build the file for each type (empirical value; recheck by component count: about 1 person-day per hundred components); all four change-column items mandatory;
5. **In-process observation record**: the three-number check — drawing component count = component-list row count = as-built count, recorded on the file-establishment sheet;
6. **Three-way criteria**: pass = three pieces complete + the three numbers agree + the test-point card holds measured values; reworkable = missing piece completed and reverified; scrap = two or more drawing-vs-reality mismatches, retest and redraw;
7. **Failure troubleshooting order**: the three numbers do not balance → first check for unregistered substitutions, then for revisions missing change-column entries, finally for counting slips;
8. **L1/L2/L3 evidence**: L1 the first type's prototype has its physical three-piece set on file; L2 100% coverage of in-service types by three-piece sets; L3 no "modify first, patch later" entries in the change column for six consecutive months.

---

## Master Parameter Table

| Parameter | Value | Category |
|---|---|---|
| Positive-pressure acceptance | Thread at the door gap drifts outward | Criterion |
| Clean-room grading | Strict for photolithography/diffusion; lenient for test/packaging | Regime |
| Control chart lines | Mean of the last 10 furnaces ±3σ (±2σ only a warning line) | Empirical |
| Drift reading | 5–7 consecutive points in one direction = systematic degradation | Empirical |
| Single-variable window | Observe 10 furnaces after each change | Discipline |
| Burn-in screening | Rated voltage, continuous power for days | Procedure |
| Ramp criterion | Level up only after each level's yield is stable | Discipline |
| Thermal red line | Heat-sink hand-temperature red line (Chapter 27) | Criterion |
| Component series values | E3 (1.0/2.2/4.7) with ±50%; E6 with ±20% | Standard |
| Stock red line | ≥20 pieces per step; falling below twice monthly consumption triggers a replenishment order | Empirical |
| Hot-press board making | 140–160 °C, 20–30 min (three-board gradient calibration) | Empirical |
| Annular ring width | ≥1 mm (narrowest point after eccentric drilling ≥0.5 mm) | Empirical |
| Jumper-wire limit | ≤10 per board; over the limit, back to the artwork for rearrangement | Discipline |
| Burn-in tiers | Ambient 72 h for all units; high-temperature 50–60 °C for 24 h | Procedure |
| Box temperature uniformity | Three-point thermometers; 10 min reading difference <5 °C | Criterion |
| Packing criterion | Silent shake test = vibration protection passed | Criterion |
| Field infant-mortality rate | First month <2% = screening sufficient (rechecked quarterly) | Empirical |
| Backup unit | Powered 1 h monthly; quarterly primary/backup switchover drill | Procedure |

## Failure Modes and Diagnostics

| Symptom | Candidate causes (by probability) | Verification | Action |
|---|---|---|---|
| Yield plunges in a single furnace | Special cause (contamination/reagent batch difference/temperature control) | Three checks against that furnace's records | File into failure analysis |
| Yield declines slowly furnace by furnace | Systematic degradation (clogged filters/abrasive-grade contamination/vessel aging) | Control-chart drift reading | Renew items one by one |
| Infant mortality at the user end | Burn-in skipped/duration too short | Operating-hours records of returned units | Lengthen burn-in |
| Failures concentrated in connectors/solder joints | Connection workmanship (the historical bulk) | Failure atlas statistics | Soldering training + sampling inspection |
| Contamination at the same spot on devices | Clean-room pressure loss/bare-handed operation | Door-gap thread method; finger-cot discipline | Repair fan, replace filters; restate discipline |
| Chemical supply cutoff stops the line | No contingency reserve | Stock column of the four-column ledger | Activate the plan (fluorspar → HF linkage) |
| Two-person backup fails | Overlapping sick leave | Workstation duty roster | Chapter 37 redundancy rules |
| Copper-clad board blisters/delaminates | Base board not dried through, holds moisture (most common); missing spacer blocks, uneven pressure; wrong resin mix ratio | Blister location distribution (edges = pressure, center = moisture); compare against same-batch trial press boards | Mild cases: cut out and downgrade away from trace areas; severe cases: press a new batch; check parameters in the ledger |
| Pad annular ring lifts | Over-etching (undercut through pinholes in the resist); poor copper-foil-to-base-board adhesion; soldering iron overheated after long idle | Examine the peeled cross-section (a bright copper face = poor adhesion; an undercut copper edge = over-etching) | Shorten etching and strengthen rinsing; time-limited soldering training (<3 s per joint, empirical value) |
| Drawing does not match the machine | Repair substitutions never written back; revision changed the machine but not the drawing | Monthly spot-check of one unit, verified item by item against the three-piece set | Restate the change-column regime; write substitutions back on the spot (36.13, 36.16) |

## Process Card Index

## Labor Hours, Manpower, and Consumption

| Item | Manpower | Hours (empirical value) |
|---|---|---|
| Clean-room conversion (positive pressure + two-stage filtration) | 3 people | 3–5 days |
| Testing and filing for one furnace batch (including the master) | 2 people | 1 day |
| Monthly Pareto and control chart | 1 person | Half a day/month |
| One burn-in round (days-long bake) | 1 person on watch | 3–5 days/batch |
| Consumption | High-purity water (largest), HF, acids, silver | Entered in the Chapter 38 ledger |

***

## A. Inventory of Existing Tools (partial)

The planar-process line and yield regime (Chapter 35); electrical testing and instruments (Chapters 27, 31–33); ceramic packaging (Chapters 11–12); the chemical supply lines (Chapters 26, 34); the standard-parts and process-card regime (Chapter 22).

## B. New Tools Added in This Chapter

The test master (four arrays: diode/resistor/transistor/interconnect); the burn-in screening bench; the three failure questions and the three-level "autopsy" procedure, the failure atlas, the monthly Pareto; the five-level logic ramp ladder and the relay mixing strategy; the parallel magnetic-core memory route; the three packaging tiers and heat-sink design; the first five classes of practical equipment and the medical-record-card repair regime; the monthly electronics-chemistry ledger and the supply-cutoff plans; the seven-workstation line + three-tier personnel + monthly operating account; the "cannot-rebuild list" with item-by-item unlock routes; the component library's E3/E6 series values and the "class–value–batch" naming and requisition regime; self-made copper-clad board and the two single-sided board-making methods (photoresist/screen print); whole-machine burn-in tiers, the three-protection deployment kit, and the installation acceptance sheet; the drawing-archive three-piece set, the repair monthly-report feedback, and the backup-unit regime.

## C. Unresolved Dependencies

- The generational ramp of yield and cleanliness (the Section 36.8 table);
- Generational upgrading of metrology and analytical instruments;
- Double-sided boards and through-hole metallization (the electroless copper line on hole walls — the generational boundary declared in 36.14);
- Greater power and population specialization (the population topics of Part 10's environment editions).

## Safety Boundary

- All chemical red lines inherited from Chapters 26, 35; fire patrols in the burn-in bench's continuously powered zone;
- Glass/ceramic shards from teardown decapping are handled as sharps; burn protection at the bonding thermocompression station;
- Repairing high-voltage equipment (grid side) follows Chapter 32's two-person procedure.

## Acceptance Standards

- **L1**: The test master runs in-furnace; failure files are established and the first ten three-level analyses are completed.
- **L2**: Flip-flop-level (ramp level 2) yield reaches target; the burn-in screening regime operates; at least three of the first five equipment classes are in active service.
- **L3**: The monthly operating account is auditable for six consecutive months; a supply-cutoff drill has been run at least once; two-person backup across the seven workstations is fully institutionalized — **the electronics industry becomes a sustainable organ of the settlement**.

## Next-Step Dependencies

- Chapters 50–53: how electronic capability is arranged and combined in different environments (the island's communication-first priority, the desert's remote-controlled irrigation, the permafrost's low-temperature reliability, the rainforest's moisture-proof packaging);
- The loop back to the general outline: this chapter is the contemporary apex of the "information lineage" among the six great lineages — the thousand-year leap from oral experience to electronic computation closes its loop here.
