# Chapter 29 Power Selection, Load Characteristics, and Combined Operation

> Part 6 · Heat Engines, Electricity, and Electronics. This chapter is no longer just a selection table "comparing three kinds of power"; it answers three harder questions: **what kind of power the load actually needs** (torque–speed characteristic matching), **how multiple power sources are run together** (combined operation and switching), and **in what order to protect whom when power runs short** (allocation discipline).

## Chapter Objectives

- Establish a power-selection framework: waterwheel, windmill, atmospheric (Newcomen-type) steam engine, and animal power compared by the master-outline priority formula (survival contribution × resource availability × repeatable manufacture × support value).
- Establish a matching table between the **load-characteristic classification** (three classes: constant torque / impact torque / constant speed) and **power-source torque–speed characteristics** — mismatch is the hidden cause of "plenty of power that still cannot drive the load."
- Establish the hydrological-year and wind-regime annual ledger systems; the wind-pond-wheel energy-storage combination.
- Establish multi-source paralleling, base-load/interruptible-chain tiering, the power ledger, and the allocation priority order.

## Capability Boundaries

**Can do:** two-source paralleling and switching; locally measured characteristic curves for all four power types (rough measurement); power ledger and full-cost accounting driving source-expansion / load-reduction decisions.

**Explicitly cannot do:** high-pressure steam engines and greater output (Chapter 28's four unlock conditions); grid connection of electricity (Chapters 31–32); precision speed governing (constant-speed loads currently depend on the manual closed loop of "machine attendant + gate/valve" only).

## Pre-Work Verification (check each item)

| # | Verification item | Criterion | Source |
|---|---|---|---|
| 1 | Waterwheel/windmill | Built and accepted per Chapter 21 (measured output on record) | Chapter 21 |
| 2 | Steam engine (if any) | Chapter 28 L2 (hydrostatic test passed, stoking crew fully established) | Chapter 28 |
| 3 | Dynamometry | Proficient in the lift method / brake dynamometry; power reference on file | Chapter 25 |
| 4 | Annual ledger data | Hydrological or wind-regime monthly records ≥1 year (if insufficient, the installation decision is postponed) | Chapters 2, 3 |
| 5 | Line-shaft clutching | Belt-shifting forks and clutch forks complete | Chapter 21 |
| 6 | Meter-reading system | Machine attendant and power ledger in place | Iron Law Seven |

---

### 29.1 Why Not Every Environment Needs a Steam Engine

The essence of the steam engine: **turning fuel into work that is not constrained by hydrology or wind regime**. The price: fuel consumption (the sustainable harvesting rate is a hard constraint), the boiler safety system, and stoker labor. Three decision questions:
- Is water power enough all year round (including the ice season / dry season)? If yes, defer steam;
- Does the fuel regenerate faster than it is consumed? If not, steam is a fake upgrade that burns up the future;
- Is the demand a seasonal peak or a year-round base load? For seasonal peaks, a water-power + animal-power combination may be cheaper.

Historical corroboration: workshops on the eve of industrialization mostly ran on waterwheels for centuries — steam first gained its foothold in **deep-shaft mine drainage** (a scenario water power could not serve; Chapters 16 and 28), then expanded step by step.

### 29.2 Torque–Speed Characteristics of Sources and Loads (mismatch is a silent failure)

#### 29.2.1 The Three Load Classes

| Load class | Characteristic | Representative processes | Matching points |
|---|---|---|---|
| Constant torque | Resisting torque barely changes with speed | Water pumps, conveying, mill feeding | Starting torque must suffice; must still work at low speed |
| Impact torque | Peak torque is several times the mean | Forging hammers, crushing, shearing | Needs a large flywheel to smooth it + energy reserve for the peaks |
| Constant speed | Speed fluctuation directly damages quality | Flour fineness, turning, spinning | Needs speed governing (gate/valve/machine attendant) |

#### 29.2.2 Power-Source Characteristic Table (roughly measured curves; every point measured by dynamometry)

| Power source | Torque–speed shape | Starting torque | Fit to the three load classes |
|---|---|---|---|
| Overshot waterwheel | Low speed, high torque; torque nearly constant with flow | **Large** (full torque the moment the gate opens) | Excellent for constant torque; impact loads need a flywheel |
| Windmill | Torque fluctuates on the order of wind speed squared | Medium | Only interruptible loads, or smoothed through a storage pond |
| Atmospheric (Newcomen-type) steam engine | One force pulse per stroke, low speed | Medium-large (counterweight balancing) | Naturally suited to impact loads (forging hammers, pumps); weak for constant speed |
| Animal/human power | Constant torque, small power, fatigues | Small | Only light constant torque + intermittent duty |

**Mismatch diagnosis (the most useful table in this chapter)**: when the power is sufficient yet the load will not turn or will not turn steadily, check the match first —
- Pump will not start → insufficient starting torque (open the waterwheel gate fully / add weight to the engine's counterweight);
- Hammer blows grow slower and slower → flywheel not big enough, or a "constant-torque-type" source driving an impact load (add flywheel or change source);
- Flour alternately coarse and fine → a constant-speed load driven by a windmill (smooth with wind-pond-wheel or switch to a waterwheel);
- Belt slips frequently → load peaks exceed the belt's power transmission (not insufficient tension — check the peaks first; Section 21.6 chalk method).

[Card 29-01 Power–Load Matching Diagnosis] (eight fields)

1. **Input materials**: a list of load workstations (milling, forging, blast blowing, pumps, saws, miscellaneous — split into base-load chain / interruptible chain per 29.5); a power-source ledger (measured output and the "torque–speed form" record for waterwheel / windmill / atmospheric steam engine / animal power); the power ledger's meter-reading page (each source's output and each load's draw, copied daily); chalk lines on the wheel ends and the flywheel.
2. **Tools required**: dynamometry and the power reference (Chapter 25); belt-tensioning and pulley-face waxing materials (29.11); flywheel, stepped cone pulleys and belt-shifting fork (Chapter 21); the 21.6 chalk method (for belt slip). Calibration source: each source's torque–speed curve is roughly measured by dynamometry, never copied from a general table — local measured values go into the local version of the characteristic table (29.4, "measurement outranks the table").
3. **Operating sequence and control points**: (1) first sort the loads into the three classes (constant torque / impact torque / constant speed, 29.2.1); (2) match the symptom against the four mismatches (pump will not start = insufficient starting torque; hammer grows slower and slower = flywheel too small, or a constant-torque source on an impact load; flour alternately coarse and fine = a constant-speed load on a windmill; frequent belt slip = peaks exceed the belt's transmission); (3) measure power 3 times under the same conditions before the change and take the median as the baseline; (4) change exactly one thing per mismatch (add flywheel / change source / open the gate fully / add counterweight / change the speed ratio); (5) re-measure 3 times under the same conditions, take the median, and set it against the power ledger. **Control points: for belt slip check the peaks before talking about tension; one change at a time (single variable) — a high gain measured after several simultaneous changes is void.**
4. **Empirical parameters and calibration method**: single-source base-load ceiling ≤50% (downtime redundancy law, empirical value, must be field-calibrated); undershot-wheel rim-speed/flow ratio ≈0.4–0.5 (empirical, must be calibrated); belt tensioning + pulley waxing cuts transmission loss 3–5%, bearing re-scraping cuts friction at that point by about 20% (empirical values; calibration method = the 29.16 before–modify–after measurement); "shedding 10% of the load is often cheaper than adding 10% of source" (empirical judgment, verified against the power ledger); modification decision line = power gain ≥5% (dynamometry repeat spread ±2–3%; below that a real improvement cannot be told from measurement noise).
5. **In-process observation items**: the symptom in its own words (who saw it, under what conditions), the load-class verdict, the mismatch conclusion, the three before-measurements and their median, the three after-measurements and their median, belt sound and pulley-face press marks, bearing temperature, process-quality signals (mill tone going coarse / chips turning blue / thick-thin yarn).
6. **Accept / rework / scrap criteria**: accept = after-modification gain ≥5% under the same conditions, the symptom gone, and the ledger meter readings improved in step; rework = any gain <5% is recorded as "no significant improvement," and you go back to check whether two things were changed at once (a high gain from several changes measured together is void); scrap = the symptom persists and there is no gain after the single change, so source and load are judged fundamentally mismatched — move to a source change or a process change per 29.5, and never mask it by endlessly opening the gate or adding counterweight (explicitly forbidden in 29.13).
7. **Common failures and troubleshooting order** (by frequency): (1) frequent belt slip → check first whether load peaks exceed the belt's transmission (21.6 chalk method), then the tension; (2) pump will not start → check starting torque (open the waterwheel gate fully / add counterweight to the engine); (3) hammer growing slower → check flywheel inertia and source type (a constant-torque source on an impact load is a mismatch); (4) flour alternately coarse and fine → find the fluctuating source (a constant-speed load straight onto a windmill is a mismatch; smooth with wind-pond-wheel or change to a waterwheel); (5) output falling month by month → check tailwater backwater, sediment abrasion, blade wear (not a matching problem — go to 29.3).
8. **L1/L2/L3 evidence**: L1 = one matching-diagnosis case (symptom → mismatch → correction → re-measurement); L2 = the local measured characteristic table for the four power types + the power ledger with its monthly surplus/deficit settlement; L3 = a second person reaches the same mismatch verdict on the same symptom from this card alone and reproduces the ≥5% modification gain.

#### 29.2.3 Matching Waterwheel Blades to Flow Velocity (three upgrade checks)

1. **Blade angle of attack**: undershot-wheel blades are mostly flat plates, and output is sensitive to "the angle between blade and water flow" — on site, try the blade array at 3 angle settings (around 20°/35°/50°, empirical starting points), measuring power 15 min per setting and taking the best (single-variable method);
2. **Rim speed to flow velocity ratio**: the optimal rim speed of an undershot wheel is about 0.4–0.5 times the water velocity (empirical value, must be calibrated — compare by dynamometry: use the belt-shifting fork to change to another stepped-cone-pulley speed ratio and test);
3. **Submergence depth**: blades entering the water too deep add drag, too shallow waste work — fixed observation with the water-level staff gauge (Chapter 3), fine-tuned by the gate.

[Card 29-02 Waterwheel Angle of Attack and Speed-Ratio Optimization Trial] (eight fields)

1. **Input materials**: an undershot waterwheel (built and accepted under Chapter 21, with measured output on record); an adjustable flat-blade array (same batch of blades, angle settings interchangeable); stepped cone pulleys (at least two speed-ratio grades); water-level staff gauge (Chapter 3); trial record page.
2. **Tools required**: dynamometry (Chapter 25, power reference on file); belt-shifting fork (to change the speed ratio); angle templates (locating the 20° / 35° / 50° settings); gate winch. Calibration: complete all settings at one and the same water level on one and the same day, logging the gate opening setting by setting.
3. **Operating sequence and control points**: (1) fix the water level and gate opening and record the starting readings; (2) fit the 20° blade array and measure power for 15 min; (3) change to 35° and measure the same way for 15 min; (4) change to 50° and measure the same way for 15 min; (5) take the best setting as the installed angle; (6) with the belt-shifting fork change to the other cone-pulley ratio, keeping whichever puts the rim-speed/flow-velocity ratio in 0.4–0.5; (7) observe submergence depth against the staff gauge and trim with the gate. **Control points: one variable at a time (single-variable method); complete within one day at one water level — data across days is not comparable; re-calibrate as soon as the seasonal water level changes.**
4. **Empirical parameters and calibration method**: trial settings around 20° / 35° / 50°, best of the three (empirical starting points); rim-speed/flow ratio ≈0.4–0.5 (undershot wheel, empirical, must be calibrated); 15 min of dynamometry per setting, take the maximum; flow velocity by the float method (mean velocity ≈0.8 × surface velocity, empirical coefficient, smaller for rougher channels).
5. **In-process observation items**: output at each setting (15 min each, recorded setting by setting), actual blade angle (read against the template), rim speed and flow velocity and their ratio, submergence-depth reading, bearing temperature and vibration, tailwater level.
6. **Accept / rework / scrap criteria**: accept = the best setting beats the original installed angle with a gain ≥5% (decision line; dynamometry repeat spread ±2–3%) and three repeats at that setting give a steady median; rework = the three settings differ by <5% (cannot be told from noise) — check whether the blades really changed angle and whether the water level moved, then retest on the same day at the same level; scrap = blade fracture, shaft deformation or loose spokes (back to Chapter 21 overhaul; the trial record is void and the trial is redone).
7. **Common failures and troubleshooting order** (by frequency): (1) no difference among the three settings → the blades did not actually change angle (template not seated, fasteners loose) — verify the angle before measuring; (2) overall output below previous years → tailwater backwater or blade abrasion (check the staff gauge and inspect the blades, 29.3) — not an angle-of-attack problem; (3) two runs at the same setting far apart → water level or gate opening moved (return to step 1 and re-measure at a fixed level); (4) still short of load after the trial → load-side mismatch (go to Card 29-01) or the installed power was never enough (back to the 29.8 power estimate).
8. **L1/L2/L3 evidence**: L1 = one three-setting trial record (same day, same water level, three measurements included); L2 = the trial record on file with the installed angle fixed from it, and the rim-speed/flow ratio logged; L3 = a second person runs the trial from this card alone and the best angle lands on the same setting, with the output medians inside the decision line (<5%).

#### 29.2.4 The Windmill's Automatic Wind-Shedding Mechanism (storm self-protection)

The most dangerous operating condition for a windmill is a storm. Three lines of defense:
1. **Spring wind-shedding of the sail surface**: the canvas is fixed with press bars + elastic lashing (wood-slat springs / elastic rope knots) — when the wind exceeds the rated setting a corner of the sail blows open to vent pressure, and returns when the wind subsides (empirical practice; register its effectiveness after prototyping);
2. **Furling mechanism**: one person can furl all the sails within 1 min (Chapter 21) — pull-ropes run through the spokes to furl them; furl as soon as a storm warning is issued, **better to furl in vain than to gamble**;
3. **Tail-vane side deflection**: in extreme wind, the tail vane swings the windmill head 30°–60° sideways off the wind (hinge + stop pin).

[Card 29-03 Windmill Three-Level Wind Defense] (eight fields)

1. **Input materials**: canvas, press bars and elastic lashing (wood-slat springs or elastic rope knots); furling ropes (run through the spokes); tail-vane hinge and stop pin; 2 spare blade sets (a consumption item in the work-hour table); the wind-regime annual ledger page.
2. **Tools required**: furling rope gear and knots (Chapter 7); stop pin and hinge (Chapter 21 windmill parts); wind-strength grading per the wind-regime annual ledger and warnings (Chapters 2, 3); quarterly trial record page. Calibration: register the wind-shedding mechanism's effectiveness after prototyping (29.2.4); trial all three levels once a quarter.
3. **Operating sequence and control points**: (1) standing first level — spring wind-shedding of the sail surface: canvas held by press bars + elastic lashing, a corner blowing open to vent pressure when the wind exceeds the setting and returning when it drops (register effectiveness after prototyping); (2) on a storm warning, second level — furl: one person completes the whole furl within 1 min, pulling the ropes through the spokes; (3) in extreme wind, third level — tail-vane side deflection of 30°–60° off the wind (hinge + stop pin); (4) after the wind drops, re-set the sails level by level, checking blades and lashings first. **Control points: better to furl in vain than to gamble; the order must not be reversed (furl first, deflect second — step 1 of the 29.15 flood/high-wind shutdown sequence).**
4. **Empirical parameters and calibration method**: furl limit 1 person, 1 min (criterion); tail-vane deflection 30°–60°; wind-shedding = a corner opening automatically above the setting (empirical practice, effectiveness registered after prototyping — do not copy figures from elsewhere); 2 spare blade sets; trial the three levels quarterly; a windmill suits only interruptible loads or smoothing through a storage pond (29.2.2).
5. **In-process observation items**: furling time per event, deflection angle (stop-pin position), whether the shed corner opened and returned, canvas and lashing wear, blade cracks and main shaft after a storm, the day's grade in the wind-regime annual ledger.
6. **Accept / rework / scrap criteria**: accept = furl ≤1 min, the shed corner returns after opening, and one gale of ≥ force 8 (empirical order of magnitude) passed without damage; rework = the corner does not open or does not return — readjust the lashing tension, retest and re-register effectiveness; scrap = blade fracture or bent main shaft — change the blades, stop and overhaul, and file an honest damage analysis (acceptance L3 allows "or an honest damage analysis").
7. **Common failures and troubleshooting order** (by frequency): (1) storm damage → first check whether the wind-shedding mechanism failed (wreckage inspection + review of the prototyping record), then whether furling was delayed (restate the warning system); (2) shed corner not returning → slack lashing or rope knots stretched by water, readjust; (3) still overspeeding after deflection → stop-pin angle insufficient or hinge sticking, adjust the pin and oil it; (4) ordinary output low → sails under-tensioned or the shed corner permanently open (treat it as an output loss, not a storm problem).
8. **L1/L2/L3 evidence**: L1 = one trial of each of the three levels with times recorded; L2 = effectiveness register for the wind-shedding mechanism + wind-regime annual ledger + quarterly trial records; L3 = a record of passing one gale of ≥ force 8 (empirical order of magnitude) undamaged, or an honest damage analysis with corrective actions.

### 29.3 Waterwheels and Mechanical Power (annual ledger system)

Reuse Chapter 21 and upgrade three points:
1. **Hydrological annual ledger**: record flow and head month by month for a full year before fixing the waterwheel's specification — installing on the strength of a single day's observation is a common cause of rework;
2. **Ice-season and low-water countermeasures**: a drainage bypass for the ice season + an underwater ice screen; for the dry season, a "waterwheel + animal power" dual-drive interface (switched by clutch fork);
3. **Tailwater and sediment**: poor tailwater lowers output (backwater submerges the undershot wheel); sediment abrades the bearings — put a settling basin upstream.

Water power's advantages: zero fuel, continuous day and night, maintenance concentrated on the hydraulic works. Disadvantages: its output ceiling is locked by hydrology, and its siting is bound to the watercourse.

### 29.4 Heat Engines versus Natural Power

| Dimension | Waterwheel | Windmill | Atmospheric steam engine | Animal power |
|---|---|---|---|---|
| Output class | Medium-large (set by hydrology) | Small-medium | Medium | Small |
| Continuity | High (except ice/dry) | Intermittent | High (stoker shifts) | On the order of 8 h/day |
| Fuel cost | None | None | High (needs a sustainability audit) | Fodder land |
| Siting freedom | Bound to hydrology | Bound to wind regime | Bound to fuel and water | Anywhere |
| Maintenance focus | Hydraulic works + bearings | Blades + storm protection | Boiler safety + seals | Veterinary care + shoeing |
| Construction threshold | Medium | Medium | High (the full Chapter 28 set) | Low |
| Suited loads | Constant torque / constant speed | Interruptible loads | Impact / pump loads | Light constant torque |

**Measurement outranks the table**: each settlement measures the output of its local equipment by dynamometry and fills in a local version of the table.

### 29.5 How to Build a Mechanical Power Network

Reuse the Chapter 21 line-shaft system and add three items:
1. **Multi-source confluence**: the waterwheel main shaft and the steam engine are paralleled through clutches onto the same main line shaft — steam disengages when water is plentiful and engages in the ice season / dry season (**fuel is spent only during the hours "when water is not enough"** — the core throttling design of the fuel audit);
2. **Priority loads**: the line shaft is split into a "base-load chain" (milling, forging, blast blowing — interruption is immediate loss) and an "interruptible chain" (sawing, miscellaneous) — when power runs short, cut the interruptible chain first;
3. **Power ledger**: each source's output and each load's draw are copied down daily, and a monthly settlement of the "power surplus or deficit" is made — three consecutive months of deficit = must expand sources or shed load; gritting it out is not allowed (the ledger format goes into the Chapter 38 energy account).

### 29.6 How to Allocate Resources When Power Runs Short

Ordering principles:
1. **Protect agriculture and food processing** (milling, irrigation pumps) — the survival floor;
2. **Protect the mother-machine workstations** (forging, lathe — the self-maintenance of manufacturing capability);
3. **Protect the acquisition of fuel and water themselves** (timber saws, water pumps — the food of the power system);
4. Queue the rest by "most essentials produced per unit of power."

**Load-shedding design** (the reverse tool): tighten the belts, scrape the bearings to cut drag, stagger processes into the high-water hours. **Shedding 10% of load is often cheaper than adding 10% of source** (an empirical judgment; verify with the power ledger).

### 29.7 How Maintenance Cost Relates to Energy Supply

**Full-cost accounting**: the cost of a power type = construction amortization + fuel/fodder + maintenance labor hours + downtime loss. Typical empirical laws (need local calibration): the waterwheel's downtime loss is the smallest; windmill storm damage is a large tail risk (keep a spare-blade inventory); the steam engine needs frequent maintenance but permits planned overhauls; animal sickness and death is a sudden large loss (keep several animals for redundancy).

**Downtime redundancy law**: no single power source may carry >50% of the base load (empirical value, must be field-calibrated) — a layout in which a single point of failure stops the whole plant is a design error.

### 29.8 Field Measurement Method for Waterwheel Siting (the complete calculate-before-building procedure)

**Measuring flow Q (two methods cross-checked)**:
- **Volumetric method (reference)**: pick a tidy channel section, narrow the outflow with boards into a weir, and time with a seconds pendulum while filling a standard bucket (Chapter 25 flow-reference method) — 3 runs, take the median. Measured in the dry season it gives the "guaranteed flow Q_min"; measured in the rainy season, the "peak Q_max". Record both numbers: size the installation by Q_min (keeps turning through the dry spells), check the gate against Q_max (to prevent washout).
- **Float method (fast, over a long reach)**: measure 10 rod lengths of straight channel, time the float over the reach 3 times, and take the median as the surface velocity v_surf; **mean velocity ≈ 0.8 × v_surf** (empirical coefficient; the rougher the channel, the smaller the value); flow Q = mean velocity × wetted cross-sectional area. If the volumetric and float methods differ by >20%, the volumetric method governs, and the channel must be checked for leaks.
- **Weir method (long-term observation post)**: build a triangular weir at the head of the channel (Chapter 27 weir calibration card); thereafter the stage–discharge reference table is read day by day — this is the automation of the hydrological annual ledger.

**Measuring head H**: A-frame level + graduated rods passed segment by segment (Section 3.3 segmented leveling method), recording the spread of readings for each segment; if the closure error of the total head exceeds half a finger-width, re-measure. **Effective head = total head − headrace slope loss** (a drop of 1 finger-width per 10 paces of channel is a necessary loss; only what remains after deducting it is the usable head at the wheel).

**Power estimate and installation decision**: P = 1000 × Q_min × H_effective × η (η chosen by wheel type). Multiply the three numbers and set them against the load account (29.5): if it covers the base load, fix the site; if not, change the site or the wheel type — **"build it and then see" is not allowed** — rework of hydraulic works is counted in person-months.

### 29.9 Scheduling the Atmospheric Steam Engine as a Power Source

In combined operation the steam engine's position is the "dry-season substitute," and nearly all of its cost is fuel and labor:

| Item | Empirical value (needs field calibration) | Notes |
|---|---|---|
| Wood/coal consumption | On the order of 15–30 kg per horsepower-hour | Atmospheric-engine efficiency <1%; the fuel account is brutal — **run it only in the hours when water is not enough** |
| Stoking shift system | 2 people/shift × 4 shifts (two-person attendance red line) | Chapter 28 stoking establishment |
| Startup preparation | 1–2 h from lighting the fire to carrying load | Slow rise from a cold boiler (Chapter 28 procedure) — scheduling must include the startup segment |
| Cooling water | 2–4 m³ per shift | Water for jet condensation; in winter draw live water from under the ice |
| Best workstations | Forging hammers, crushing, water lifting (impact / pump loads) | Conclusion of the 29.2 characteristic table |

**Scheduling discipline**: light the boiler only when the power ledger has shown a water-power shortfall >20% for three consecutive days; once lit, plan on "at least one full day of running" (the fuel wasted on a cold start makes short firings uneconomical).

### 29.10 Paralleling Operating Procedure (Card 29-04 expanded)

Five steps for paralleling two sources onto the same main line shaft:
1. **Shut down before shifting**: engaging a clutch while running = flywheel injuries (red line). All paralleling operations are carried out with everything stopped;
2. **Pre-synchronize speeds**: first run the auxiliary source unloaded; adjust the waterwheel gate / steam-engine throttle valve so that the two sources' free-running speeds come close (criterion: paint a white line on each shaft end and judge by eye that the two lines pass at similar rates — exact synchronization cannot be measured without instruments; "approaching smoothness" is enough, because belt drive itself tolerates a lot);
3. **Engagement order**: engage the large-inertia source (waterwheel) first, then the small-inertia source (steam engine / animal power) — a large source carrying a small one is smoother than the reverse;
4. **Unloaded trial run, 10 min**: listen for beating sounds (a periodic "mm-mm" hum caused by a slight speed difference between the two sources is normal; sharp beating = the speed difference is too large — stop and readjust);
5. **Load step by step**: connect loads one at a time in base-load-chain priority order, watching belt slip and bearing temperature at each step.

**The take-offline (breakup) sequence is the reverse of engagement**: unload first, then stop the small source, and finally close the large source's gate — suddenly throwing off the load can send the waterwheel into a runaway (first row of the Chapter 29 failure table).

[Card 29-04 Multi-Source Paralleling Operation] (eight fields)

1. **Input materials**: the main line shaft (Chapter 21) and the two source main shafts; clutch (friction plates entered in the Chapter 38 ledger) and belt-shifting fork; any auxiliary source (atmospheric steam engine / animal power); chalk lines on the wheel ends and shaft ends; paralleling record page and switching-duration ledger.
2. **Tools required**: gate winch, throttle valve (Chapter 28); hourglass (10 s timing); listening rod (a wooden rod will do) for the beating sound; clutch fork. Calibration: the two sources' free-running speeds are judged "close and steady" by eye against the chalk lines — exact synchronization cannot be measured without instruments, and belt drive itself tolerates a lot.
3. **Operating sequence and control points**: (1) **shut down before shifting** — every paralleling operation is done with everything stopped (engaging a clutch while running = flywheel injuries, red line); (2) pre-synchronize speeds — start the auxiliary source unloaded and adjust gate/throttle until the free-running speeds come close (chalk line on each shaft end, judged by eye); (3) engagement order — the large-inertia source (waterwheel) first, then the small-inertia source; (4) unloaded trial run 10 min — listen for beating (a periodic "mm-mm" hum is normal; sharp beating = speed difference too large, stop and readjust); (5) load step by step — connect loads in base-load-chain priority order, watching belt slip and bearing temperature at each. **Control points: stop before engaging; the take-offline sequence is the reverse (unload → stop the small source → close the large source's gate); suddenly throwing off the load can send the waterwheel into a runaway.**
4. **Empirical parameters and calibration method**: unloaded trial run 10 min; paralleling retrofit 3 people, 3–5 days; fuel spent only in the hours "when water is not enough" — light the boiler only after the ledger shows a >20% shortfall for three consecutive days (system); mutual-backup switching duration: first drill ≤2 h, year-end average ≤1 h, a single run >4 h judged a failure (empirical values; calibrate local targets from quarterly measurements); single-source base load ≤50%.
5. **In-process observation items**: white-line counts of both sources when free-running, engagement order and times, the beating-sound verdict of the 10 min trial, belt slip and bearing temperature after each load is added, switching duration (from the order to the base-load chain running again), runaway precursors (wheel sound turning to a scream, white line blurring into a ring).
6. **Accept / rework / scrap criteria**: accept = continuous running after paralleling with no sharp beating, no belt slip, and switching duration within target; rework = sharp beating or belt slip appears — stop, re-adjust speeds, reload one load at a time; a switching overrun must have its cause recorded (a sticking clutch and an unoiled gate winch are the two most common); scrap = a flywheel-injury hazard or a runaway during engagement — apply "cut the source before seeking the cause" at once, and re-review the paralleling scheme before trying again.
7. **Common failures and troubleshooting order** (by frequency): (1) resonance noise after paralleling → the two speeds did not match but were engaged anyway (shut down, synchronize first); (2) switching overruns → sticking clutch (leading cause), dry gate winch (next); (3) slip as soon as load is applied → load peaks exceed the belt's transmission (check peaks first, 21.6 chalk method); (4) runaway on a thrown load → belt break / belt-shifting fork displaced / tool collapse at the load end (three checks in that order, and cut the source before investigating).
8. **L1/L2/L3 evidence**: L1 = one record of paralleling two sources and bringing up the base-load chain; L2 = paralleling record page + switching-duration ledger + base-load/interruptible chain grading in force; L3 = a full quarter's mutual-backup switching drill record (with the night-shutdown and runaway-command drills once each per year), and a second person completing the five steps from this card alone.

### 29.11 Load-Shedding and Peak-Staggering Checklist (turn "power shortage" into a scheduling problem)

| Measure | Order of savings (empirical values) | Execution cost |
|---|---|---|
| Belt tensioning + waxing the pulley faces | Transmission loss down 3–5% | Half a person-hour per machine |
| Re-scraping bearings (those with excessive clearance) | Friction at that point down 20% | Half a day of scraping per pair |
| Peak staggering: move flour milling to night (high-water hours) | Peak load down 10% | Schedule adjustment |
| Convert parallel processes to series (driven in turn on one shaft) | Peak shaving | Half a day of line-shaft rerouting |
| Stop or modify high-consumption, low-efficiency processes (e.g., stone mills replacing part of the ore crushing) | Depends on the process | Process evaluation |

**Post the staggering table on the wall**: divide the 24 hours into three tiers — "high-water / normal / low-water" — and write into each tier the list of loads allowed to run; the machine attendant executes by the table, not by on-the-spot judgment (the power version of the Chapter 37 scheduling system).

### 29.12 Registering Animal and Human Power as Power Resources

- **Human sustained power**: treadle/hand crank 50–80 W, capstan winding 60–100 W, pushing a mill 40–60 W (all sustainable on the scale of hours; double that as a peak is not sustainable — empirical values needing field calibration: measure your own crew's averages with the Chapter 25 lift method);
- **Animal power**: donkey/ox draft 300–500 W, 6–8 effective h per day; horses 500–700 W but fodder costs three times as much — **choose animals by "fodder cost per watt-hour"** (Chapter 38 account);
- **Human shift system**: any continuous human-power post longer than 0.5 h is scheduled per Chapter 37 (the ≤30 min single-person red line applies only to high-temperature posts in front of furnaces);
- Register them on the power ledger's "human and animal page" — they are components of the power network, not "human labor that does not count as power."

---

### 29.13 Speed Governing and Speed Holding (the complete manual closed-loop procedure)

The manual-procedure portion of this section is third tier (another person can reproduce it from the commands and criteria alone); the centrifugal governor portion is background/outlook (lacking full-scale installation and real-load validation; promotion conditions at the end of the chapter). Until a mechanical governor can be built, speed holding for constant-speed loads (class 3 of 29.2.1) relies on the manual closed loop of "machine attendant + actuator" — this section writes that loop out as commands, criteria, and records; improvisation on the spot is not allowed.

**Actuators and manual-control parameters (calibrate before taking the post)**:
- **Waterwheel gate**: field-calibrate an "opening–output" reference table — starting from no load, measure power once per finger-width of opening (Chapter 25 dynamometry, completed within one day at one and the same water level), giving the output increment per finger-width; write the table on a wooden board beside the gate. Once the water level has changed with the seasons, **the table must be re-calibrated at each change of season**; a table not re-calibrated for more than one season is treated as expired.
- **Steam-engine throttle valve**: calibrate a "turns–speed" reference — once unloaded and once loaded (on an atmospheric engine the two states differ greatly; keep both rows). Empirical starting point: 5–8 turns over the full travel, with output changing most steeply in the first 2 turns; commands use the "half-turn" as the smallest unit of action.
- **Windmills are outside this section**: wind cannot be controlled by hand, and constant-speed loads are forbidden from connecting directly to a windmill (29.2 mismatch table).

**Load-step response commands (waterwheel gate manual procedure)** — at the instant of connecting or disconnecting a constant-speed workstation, the command must be called out, and the gate may be moved only after the machine attendant repeats it back:
- Connecting: "Mill on!" — "Mill on!" — open the gate one finger-width and watch for 10 s: if the white-line count has dropped by no more than 10%, hold; if more than 10%, open another half finger-width; after three consecutive additions without stabilizing, stop and check belt slip and load jamming (endlessly opening the gate to mask a mismatch is not allowed).
- Disconnecting: "Mill off!" — repeat back — close half a finger-width first and listen to the wheel: if a growing continuous whine appears (a precursor of climbing speed), close another half finger-width; if there is no whine, hold.
- During single-person attendance the command system degrades into a timed system: check the white-line count once every 5 min; the records are still kept, without omission.

◎**White-line visual counting** (the core hand-feel of this section): paint a chalk line on the flywheel/wheel end (Chapter 21 marking method), count the passes of the line against a 10 s hourglass, and the ratio to the reference count is the fluctuation rate. Practice method: a new machine attendant starts by spinning the flywheel by hand while everything is stopped, completes 20 full 10 s counts, and may take the post only when counting the same line in a pair with a partner their counts differ by ≤1; compensation for misjudgment: paired counting + counts written to paper — concluding "the speed looks about right" is not allowed.

**Steam-engine throttle manual control**: the command "steam up/down N half-turns" is repeated back the same way. An atmospheric engine's speed naturally rises and falls with each stroke; judge always by the 10 s white-line count, and never chase smoothness stroke by stroke — adjusting the valve stroke by stroke sets up oscillation of the valve rod, and the more you adjust the messier it gets (an empirical lesson, entered in the failure table).

**Centrifugal governor pre-research [background/outlook]**: the mechanical centrifugal governor (a pair of weights + links connected to the throttle valve) is a prerequisite for stable operation in the age of electrical loads (Chapters 31–32) — electric loads will demand speed stability beyond the reaction speed of a manual closed loop. This chapter does only two steps of pre-research: (1) using the cast-iron and turning capability of the Chapter 21 flywheel process, prototype a pair of weights and links, sized at twice the local throttle-valve travel, as an observation model; (2) bench-test by hand crank to verify the direction of motion and the travel — as speed rises the weights swing outward and press the valve rod down to close; throughout, no sticking anywhere, and link travel is checked 1:1 against valve-rod travel. No prime mover is connected; nothing is installed on the engine. Full-scale installation and parameter tuning are postponed until electric loads appear.

**"Speed-holding three tiers" operation** (operating card 29-05): milling / turning / spinning — the three tiers each have an allowed fluctuation limit and observation criteria; the card text follows.

[Card 29-05 Speed-Holding Three-Tier Operation] (eight fields)

1. **Input materials**: a constant-speed load workstation (milling / turning / spinning, any one); chalk-line markings (one on the wheel end + one on the flywheel); a 10 s hourglass or pendulum clock; the record book's "speed-holding page."
2. **Tools required**: the gate/throttle valve and its "opening–output / turns–speed" reference table (sources: Chapter 21 gate, Chapter 28 throttle valve; calibration: re-calibrate at each change of season; more than one season un-recalibrated counts as expired); the hourglass (checked against the pendulum clock once a month, 10 s difference ≤0.5 s).
3. **Operating sequence and control points**: (1) start up unloaded and record the 10 s white-line reference count (3 runs, take the median); (2) confirm this tier's allowed fluctuation from the tier table; (3) every connect/disconnect of load gets its command called and repeated back before the gate is moved; (4) count once every 10 s; if out of tolerance, move the gate/valve per the command rules; (5) before shift handover and end of work, enter the day's fluctuations and dispositions in the speed-holding page. **Control points: repeat back before acting; counts must go on paper.**
4. **Empirical parameters and calibration method**: allowed fluctuation in three tiers — milling ≤±15%, turning ≤±10%, spinning ≤±8% (all deviations of the 10 s count from the reference; empirical values. Calibration method: back-calculate from one week's yield — the largest fluctuation at which the scrap/rework rate clearly rises is this crew's limit; transcribe the calibration result into the ledger); gate minimum action half a finger-width, throttle valve half a turn (fixed by the local reference tables).
5. **In-process observation items**: white-line count (every 10 s), belt sound (a sharp screech = precursor of slip), process-quality signals (mill tone turning coarse / chips discoloring toward blue / thick-thin irregularity in the yarn), each entered in its own of the three columns of the speed-holding page.
6. **Accept / rework / scrap criteria**: fluctuation within the tier and product passing — accept; brief overage (<1 min) already corrected and spot-checked product passing — record it, no rework; overage persisting >1 min or scrap appearing — that batch is reworked per its process (re-mill / re-turn / re-spin), and the command records are traced to find the slow-to-act link.
7. **Common failures and troubleshooting order**: uneven flour coarseness → (1) command not repeated back, gate acted late (check against the command records) → (2) load connected suddenly without a call (ask the workstation) → (3) opening table expired (check the re-calibration date).
8. **L1/L2/L3 evidence**: L1 one complete speed-holding page; L2 the local reference tables + 7 consecutive days of speed-holding pages; L3 records of the three tiers' allowed fluctuations calibrated against yield + complete duty records from two separate machine attendants (reproducible by a different person).

### 29.14 Detailed Rules for Power Redundancy and Mutual Backup

This section is third tier. The 29.7 downtime redundancy law (single-source base load ≤50%) only takes effect once the three systems below are all in place — "redundancy" without drills and maintenance exists only on paper.

1. **Two-source mutual-backup switching drill system**: once per quarter, switch between waterwheel and steam engine (in steamless periods, waterwheel ↔ animal-power set), executing all of the 29.10 five steps (shut down before shifting, speed synchronization, engagement, unloaded trial run, step-by-step loading); record the "switching duration" in the ledger, from the moment the order is given to the moment the base-load chain is running again. Targets: first drill ≤2 h, year-end average ≤1 h (empirical values; calibrate the local targets from quarter-by-quarter measurements); a single run >4 h judges the drill failed — hold one extra drill that quarter and record the cause of failure; the most common causes are a sticking clutch and an unoiled gate winch, precisely the two maintenance items most often skipped in ordinary times.
2. **Standby-equipment maintenance posts**: every mothballed unit (spare wheel set, spare boiler — Chapter 28 storage procedure) is assigned a maintenance post and a responsible person, and is **turned over once per ten-day period**: rotate the flywheel or paddle wheel by hand through exactly two full turns; the criterion is no point of sticking anywhere through the travel. If sticking is found, chalk-mark the rim and note the angle; if the same angle sticks for two consecutive periods → open the housing and inspect the bearing and seal there. While turning, also check oil level, dryness of the packing, and rust spots; enter the results on the standby-equipment page. **Missing the turning for two consecutive periods demotes that standby unit to "awaiting repair" and strikes it from the mutual-backup roster** — being struck off triggers a 29.7 recheck: while the roster has fewer than two sources, the next planned overhaul is frozen until it is restored.
3. **"One unit under overhaul, one unit covering" scheduling linkage**: when planning overhauls (the waterwheel's off-season annual inspection, the boiler's periodic inspection — Chapter 28), issue the overhaul window and the coverage window as one combined entry (scheduling carrier: the Chapter 41 roster): on the day the overhaul opens, the covering source is paralleled per 29.10 and takes up the base-load chain; only after the overhaul is finished and passes trial-run acceptance may the standby be taken offline back to its storage position. If hands conflict (overhaul crew and covering machine attendant both short), **postpone the overhaul** per the Chapter 41 conflict rules — canceling the overhaul or skipping acceptance is not allowed; moving an overhaul by a week is a small loss, running while unhealthy is an uncontrolled loss.

### 29.15 Power-Failure Emergency Response

This section is third tier: each of the three contingency plans has its first actions, criteria, and records; the night-shutdown rehearsal and the runaway command drill are folded into the 29.14 drills (at least one of each per year); the drill records are themselves promotion evidence.

**Main-source night-shutdown plan (blackout procedure)**: when the waterwheel stops for the night (ice lock, low water, overhaul) and steam has not been lit, the whole plant enters the blackout procedure. The lighting-priority table is written and posted in advance; it is not decided on the spot:

| No. | Lamp position | Reason |
|---|---|---|
| 1 | Boiler house / forge fire-watch position | Kept always lit (against a banked fire flaring up unnoticed) |
| 2 | Gatehouse + line-shaft passage | Prevent people walking into rotating parts (after shutdown, residual inertial rotation can last several minutes) |
| 3 | Pump-house water gauge | Against night-time overflow or the pump sucking air |
| — | All other workstations | No lamps, no exceptions |

Oil-lamp allowance: 2 always-lit + 1 inspection lamp; lamp oil 0.2–0.3 L per lamp per night (empirical value; calibration method: measure the actual consumption of one full night for the local lamp type and transcribe it into the ledger). Night-shutdown execution sequence: give the order 1 h before dark → unload in the reverse order of the 29.11 load-shedding table → close the gate or bank the fires → light the always-lit lamps → hang the tags (stating the morning gate-opening time + the responsible person's name) → the inspection lamp makes one round every 2 h. Operating Card 29-06 follows.

**Runaway emergency (three checks on the thrown load)**: the symptoms are the wheel's sound turning into a sharp scream and the white line blurring into a ring. Step one, **cut the source before seeking the cause** (red line; no watching while it spins): for the waterwheel, drop the gate (a gate-drop handle is kept beside the winch, with a marked tag position); for the steam engine, close the throttle valve + open the safety blow-off (Chapter 28). Step two, three checks on the thrown-load cause, in order of probability: (1) belt broken or thrown off — check the broken ends of the belt and the press-marks on the pulley face; (2) belt-shifting fork / clutch fork displaced out of engagement — check whether the fork-position marks line up; (3) tool collapse at the load end, a broken shaft, or a jam suddenly releasing — check the workstation's tools and transmission parts. Step three, restart: once the cause is identified and corrected, reload step by step per 29.10; **if the cause cannot be found, restarting is not allowed** — hand over to the corresponding Chapter 21/28 overhaul procedures and enter it in the failure table.

**Shutdown sequence under flood or high wind**: this interfaces with the Chapter 44 disaster plan; on the power side, execute the five fixed steps (the order must not be changed — first ensure people can get out, then that the equipment can be restored): (1) windmill: furl the sails first, then deflect the tail vane (the top tier of the 29.2.4 three-level wind defense); (2) waterwheel: drop the gate + open the bypass to spill the flood (so the gate is not overtopped and the channel does not overflow); (3) steam engine: bank the fires and seal the furnace (Chapter 28 furnace-sealing procedure); (4) put all belt-shifting forks into neutral and disconnect the whole line-shaft chain; (5) before the people withdraw, confirm the tags and broken chains item by item. After the flood recedes, restart by first turning over and inspecting per the 29.14 standby-maintenance-post procedure, then loading step by step; wheel sets soaked by silt-laden floodwater are treated as sediment abrasion (29.3 settling basin and blade inspection).

[Card 29-06 Main-Source Night-Shutdown Emergency] (eight fields)

1. **Input materials**: 3 oil lamps (2 always-lit + 1 inspection); the lamp-oil night allowance (0.2–0.3 L per lamp, locally calibrated); 2 tags (gate tag + furnace-position tag); the inspection sign-in book's "night-shutdown page."
2. **Tools required**: the gate winch, the throttle valve, and the fire-banking/furnace-sealing tools (Chapter 28); the lighting-priority table (posted on the wall); an hourglass for timing, or calls by night-watch. Calibration: once per quarter, alongside the drill, verify the lamp positions and allowances against the priority table.
3. **Operating sequence and control points**: (1) issue the "night-shutdown order" 1 h before dark; (2) unload in the reverse order of the load-shedding table; (3) close the gate or bank the fires; (4) light the always-lit lamps (boiler position, gatehouse); (5) **the tags must state the morning restart time + the responsible person's name (control point; a tag without a name counts as not hung)**; (6) the inspection lamp makes one round every 2 h, one sign-in per round.
4. **Empirical parameters and calibration method**: inspection interval 2 h; for a night of 10–12 h, 5–6 rounds (winter's longer nights, 6–7 rounds); lamp oil calibrated by measuring a full night; the inspection route is fixed (gatehouse → pump house → furnace position → gate), with the sign-ins as proof.
5. **In-process observation items**: sign-in per round, lamp-oil remaining, pump-house water-gauge readings, gate/furnace-position status — entered in the corresponding columns of the night-shutdown page.
6. **Accept / rework / scrap criteria**: a night without incident and an on-time, in-order morning start — accept; one missed sign-in — record the cause and add one full-route re-inspection in daytime (rework); ≥2 missed sign-ins, or the morning start finding the gate displaced or the pump house abnormal — rework, retrain the on-duty person, and review and revise the plan table.
7. **Common failures and troubleshooting order**: abnormal water level found at the morning start → (1) the pump-house always-lit lamp was not lit (check the lamp-position sign-ins — not being able to see the water gauge is the leading cause) → (2) missed inspection sign-ins (check the night-shutdown page) → (3) the tag lacked a time, delaying the morning start (check the tag).
8. **L1/L2/L3 evidence**: L1 one complete night-shutdown page from a single shutdown; L2 the lighting-priority table in writing + the lamp-oil night-consumption account; L3 a full quarter's night-shutdown records + one record of the "night shutdown → morning start" switching duration (folded into the 29.14 drill ledger).

### 29.16 Energy-Efficiency Improvement Archive

This section is third tier (it has a template, a decision line, and worked examples). The power ledger (29.5) answers only "is there a deficit"; the efficiency archive answers "where is it being lost, and did the fix help." Every transmission / friction / steam-path modification runs the three steps "measure before — modify — measure after," one page per item, transcribed into the ledger:

| Field | How to fill it in |
|---|---|
| Before-measurement | Measure power 3 times under the same conditions before the change (same water level day / same steam pressure / same load chain), take the median W_before |
| Modification content | One sentence + location and dimensions (e.g., "bearing No. 2 clearance re-scraped to half a sheet-of-paper thickness") |
| After-measurement | Re-measure 3 times under the same conditions after the change, take the median W_after |
| Verdict | Gain = (W_after − W_before)/W_before; **≥5% is recorded as "effective modification," <5% as "no significant improvement"** — no exaggeration allowed |
| Annual energy-saving rate | Σ(gain power of effective modifications × that chain's annual running hours) ÷ total annual power consumption; compiled year by year into the Chapter 42 account as a third path alongside "expand sources / shed load" |

**Where the 5% decision line comes from (order-of-magnitude sanity check)**: the Chapter 25 dynamometry method has a re-measurement scatter of about ±2–3%; an "improvement" below 5% cannot be told apart from measurement fluctuation; therefore change only one thing per round (single variable) — high gains measured with several changes bundled together are invalid.

**Three worked examples (empirical orders of magnitude, for expectation management; the actuals are governed by local before/after measurements)**:
- **Belts**: tensioning + pulley-face waxing (29.11), transmission loss down 3–5% — a base-load chain of 2 kW saves about 60–100 W, roughly the human power of half a windlass; completed in half a person-hour; usually ranked first priority;
- **Bearings**: re-scrape those with excessive clearance; friction at that point drops about 20% — example: a mill drawing 300 W saves about 60 W after the change, at the cost of half a day of scraping; after the modification, re-check journal temperature and waxing interval together (friction down means temperature down);
- **Steam path / piping**: straightening an atmospheric engine's exhaust pipe from 3 right-angle bends to 1 lowers back pressure and raises output about 1–2% (empirical value; calibration method: measure power 3 times before and after the change, take the medians). Piping modifications are the most easily overlooked: every additional right-angle bend in the steam path raises the exhaust back pressure another step, and the whole engine's output is discounted step by step — the worked example shows that even "an unremarkable pipe" deserves a page in the archive.

The efficiency archive and the 29.11 load-shedding checklist share the same power account. Once a round of easy modifications is finished (two consecutive rounds with no item crossing the 5% line), the remaining gap has only two paths left — expanding sources and shedding load (29.5–29.6); delaying the decision with "let's think of something else" is not allowed.

## Master Parameter Table

| Parameter | Value | Class |
|---|---|---|
| Hydrological annual ledger | Record month by month for a full year before installing | System |
| Flow measurement | Volumetric method as reference + float method (0.8 × surface speed) as cross-check | Method |
| Effective head | Total head − channel slope loss | Definition |
| Steam substitution trigger | Light the boiler only after a ledger shortfall >20% for three consecutive days | System |
| Undershot-wheel blade-angle trial settings | Best taken around 20°/35°/50° | Empirical |
| Rim speed / flow velocity ratio | ≈0.4–0.5 (undershot wheel) | Empirical |
| Sail wind-shedding | Press bars + elastic lashing; a corner self-opens beyond the rated wind | Empirical practice |
| Furling time limit | 1 person, 1 min | Criterion |
| Single-source base-load ceiling | ≤50% | Empirical |
| Ledger deficit line | Three consecutive months → expand sources or shed load | System |
| Waterwheel annual inspection | Planned overhaul in the off season | System |
| Allowed speed-holding fluctuation, three tiers | Milling ≤±15% / turning ≤±10% / spinning ≤±8% (10 s white-line count) | Empirical |
| Gate/throttle minimum action | Half a finger-width / half a turn (set by the local reference tables) | Empirical |
| Mutual-backup switching duration | First drill ≤2 h, year-end average ≤1 h, >4 h judged failed | Empirical |
| Standby turning-over period | Once per ten-day period; two missed → demoted to awaiting repair | System |
| Night-shutdown inspection interval | 2 h (5–6 rounds/night; winter 6–7) | Empirical |
| Night-shutdown lamp oil | 0.2–0.3 L per lamp per night (calibrated by local measurement) | Empirical |
| Modification effectiveness decision line | Power gain ≥5% (dynamometry re-measurement scatter ±2–3%) | Criterion |
| Command repeat-back | Repeat back before acting; single-person attendance degrades to the timed system (5 min) | System |

## Failure Modes and Diagnosis

| Symptom | Candidate causes (by probability) | Verification | Disposition |
|---|---|---|---|
| Pump will not start | Insufficient starting torque (mismatch) | Compare against the characteristic table | Open gate fully / add counterweight / increase reduction ratio |
| Hammer blows slowing | Flywheel insufficient; source is a constant-torque type | Peak dynamometry | Enlarge the flywheel / move it to a steam-engine post |
| Flour unevenly coarse | Constant-speed load on a fluctuating source | Observe the fluctuating source | Wind-pond-wheel smoothing / switch to a waterwheel |
| Belt slips frequently | Load peaks exceed transmission capacity | Section 21.6 chalk method | Check the peaks before tensioning |
| Waterwheel output declining month by month | Tailwater back-flooding / sediment / blade wear | Staff gauge + blade inspection | Clear the tailwater / settling basin / replace blades |
| Windmill storm damage | Wind-shedding mechanism failed / furling delayed | Wreckage inspection | Review the prototyping records; reaffirm the warning system |
| Resonant noise after paralleling | Mismatched speeds engaged hard | Shut-down shifting procedure | Engage while stopped; synchronize speeds first |
| Gritting through a ledger deficit | Expand/shed decision never executed | Monthly settlement | Shed load in priority order |
| Governing lag out of tolerance (constant-speed product intermittently good and bad) | Command not repeated back, gate late; opening table expired (water level changed, not re-calibrated); novice misreads the white line | Check against command records; check the re-calibration date; paired counting | Reaffirm the repeat-back system; re-calibrate at season change; ◎ no taking the post until the practice apprenticeship is complete |
| Standby turning-over missed (bearing seized when called into service) | No responsible person scheduled; storage spot out of the way and forgotten; the "won't need it anyway" mindset | Verify against the standby-page sign-ins | Enter it as a Chapter 41 roster item; two missed periods → demote to awaiting repair and strike from mutual backup |
| Night-shutdown lighting order wrong (furnace/pump abnormality found at morning start) | Priority table never posted; inspection lamp lit before the always-lit lamps; pump-house lamp position left out | Check the night-shutdown page's lamp-position sign-ins | Post the table + inspection sign-in system; missed sign-ins handled as Card 29-06 rework |

## Process Card Index

## Acceptance Criteria

- **L1**: measured data for the four local power types entered into the tables; the power ledger opened; one matching-diagnosis case (symptom → mismatch → correction → re-measurement).
- **L2**: at least two sources running in parallel (shut-down shifting procedure executed); base-load/interruptible-chain tiering in force; monthly full-cost accounting written up and having guided at least one load-shedding decision; waterwheel angle-of-attack trial records on file.
- **L3**: the power network's annual supply rate and downtime redundancy meeting target (a single-source fault does not stop everything); the hydrological/wind annual ledger driving next year's installation and overhaul plans; the windmill coming through one wind of force ≥8 (empirical magnitude) undamaged (or with an honest damage analysis). Evidence: annual ledger, power ledger, overhaul plans, storm records.

## Labor Hours, Personnel, and Consumption

| Item | Personnel | Labor hours (empirical values) |
|---|---|---|
| Hydrological annual ledger | 1 person (part-time) | Half a day per month |
| Angle-of-attack trial | 2 people | 1 day |
| Wind-shedding mechanism prototyping | 2 people | 2 days |
| Paralleling modification (clutches) | 3 people | 3–5 days |
| Power ledger | Machine attendant | 15 min daily |
| Consumption | 2 spare blade sets, clutch friction plates | Into the Chapter 38 ledger |

## Safety Boundaries

- **Paralleling requires shut-down shifting** (engaging a clutch while running = flywheel injuries); each source keeps an independent means of stopping.
- On storm warning, furl the sails — better to furl in vain than to gamble; test-actuate the wind-shedding mechanism quarterly.
- During consecutive ledger deficits, "grabbing output while running unhealthy" is strictly forbidden.
- For waterwheel overhaul, drop the gate, cut the water, and hang the tags first (Chapter 21).
- **For a runaway, cut the source before seeking the cause** (no watching while it spins); if the cause cannot be found, no restart.
- The always-lit lamp positions of the night-shutdown lighting (boiler position, gatehouse) must not be diverted to other uses; missed inspection sign-ins are reworked per Card 29-06.

## A. Existing Tools List

Waterwheel / windmill / line-shaft clutching (Chapter 21); atmospheric (Newcomen-type) steam engine (Chapter 28); dynamometry and the power reference (Chapter 25); resource ledger (Chapter 2).

## B. New Tools Added in This Chapter

**Three-class load classification and torque–speed matching diagnostic table**; **waterwheel angle-of-attack / speed-ratio optimization trial method**; **windmill three-level wind defense (spring wind-shedding, 1-minute furling, tail-vane deflection)**; power-selection decision questions; hydrological annual ledger system; wind-pond-wheel energy-storage combination; multi-source paralleling procedure; base-load/interruptible-chain tiering; power ledger and monthly surplus/deficit system; allocation priority order; load-shedding troubleshooting method; full-cost accounting table; downtime redundancy law; **speed-holding three-tier operation (command repeat-back + white-line counting + opening/turns reference tables)**; **centrifugal governor pre-research (two-step observation model)**; **two-source mutual-backup quarterly drills and switching-duration ledger**; **standby ten-day turning-over maintenance post**; **blackout procedure and lighting-priority table**; **runaway thrown-load three checks**; **five-step flood/high-wind shutdown sequence**; **energy-efficiency "measure before — modify — measure after" archive and the 5% decision line**.

## C. Unresolved Dependencies

High-pressure steam engine and greater output (Chapter 28's four conditions); grid connection of electricity (Chapters 31–32); precision governor (long-term: the mechanical centrifugal governor).

## Next-Step Dependencies

Chapters 30–31: stable mechanical work is the prime mover for electricity generation. Chapter 32: the electric motor upgrades power distribution from "shaft" to "wire." Part 10's four-environment edition: this chapter's framework is the master outline for each energy route (rainforest = water power first; desert = wind-pond combination; tundra = ice-season countermeasures; islands = wind + limited steam). Chapter 38: the power ledger merges into the master energy account.
