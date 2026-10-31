# Chapter 30 Experimental Foundations of Electromagnetism

## Chapter Goals

Building electricity from zero: static electricity and electric charge, **battery engineering (the three ailments of galvanic cells — polarization / internal resistance / capacity — and their treatment)**, magnetism and magnetization, the three effects of current, electromagnets, **self-induction and the spark coil**, and electrical measurement starting from the compass galvanometer. This chapter builds **understanding and repeatable experimental apparatus** (L1–L2 level); power generation and the grid come in the following two chapters.

**The first lesson of electricity is the same as for steam: safety.** Static electricity has high voltage but little energy — the Leyden jar is the exception (its shock can be lethal); battery current is mild, but "low voltage is harmless" is an illusion — every step-up in the chapters ahead brings new dangers with it.

## Capability Boundary

**Can do:** voltaic pile and Daniell two-solution cell (stable current source); measurement and logging of battery capacity/internal resistance/polarization; reference cell (the seed of a voltage standard); the three electromagnet devices (iron-lifting / electric bell / sound code); spark coil (low voltage to high-voltage pulses, reused directly by the Chapter 33 leak detector).

**Explicitly cannot do:** **charging** storage batteries (requires a generator — backfilled and enabled at 31.10 once Chapter 31 is built; this chapter only establishes the principle and plate preparation); absolute calibration (Chapter 31 electrolytic method); insulated copper wire in bulk (Chapter 31).

**External dependencies:** acids (the Chapter 23 three-acid line — dilute the sulfuric acid before it enters the cell); zinc (if no zinc, substitute iron and honestly log the halved capacity).

## Pre-Work Verification (Check Off Item by Item)

| # | Verification item | Criterion | Source |
|---|---|---|---|
| 1 | Copper plates/copper stock | Acid-pickled to remove oxides (Chapter 23 dilute acid or vinegar) | Chapter 17 |
| 2 | Zinc/iron sheets | Use iron sheet if no zinc; surface polished | Chapters 17, 18 |
| 3 | Acid | Vinegar (weak) or dilute sulfuric acid (**dilute acid into water**, about 1 part oil of vitriol + 9 parts water; empirical starting point, must be field-calibrated) | Chapter 23 |
| 4 | Lodestone | Clearly attracts iron in tests; ore site logged | Chapter 16 |
| 5 | Compass and angles | Homemade magnetic needle floating on water holds a steady bearing | Chapters 3, 25 |
| 6 | Record system | Five-element electrical log table in place | Chapter 25 |
| 7 | Clay pot and diaphragm | Unglazed clay pot for the Daniell cell (porous diaphragm) | Chapter 11 |

---

### 30.1 Static Electricity and Electric Charge

- **Triboelectric charging**: rub amber/sealing wax/dry rosin with fur, and a glass rod with silk — the rubbed objects attract light items;
- **Two kinds of charge**: a glass-silk rod repels a rod made the same way and attracts an amber-fur rod — like charges repel, unlike charges attract; name and log them;
- **Electroscope**: a metal rod through a glass bottle stopper, with two thin copper-leaf strips hung from its lower end — they spread apart when charged, and the opening angle roughly indicates strength;
- **Leyden jar**: metal foil stuck on the inner and outer walls of a glass bottle stores charge. **Safety red line: after charging it must be discharged with a discharger (insulated rod + wire); approaching it bare-handed means a shock; persons with heart conditions must not operate it**;
- The conductor/insulator dichotomy (metal foil conducts, glass does not) is the first map of all electrical science.

### 30.2 Current, Voltage, and Resistance

#### 30.2.1 Galvanic Cell Engineering: From the Voltaic Pile to the Daniell Cell

**Voltaic pile** (the first unit, quick and rough): copper plate / acid-soaked cloth / zinc plate (iron if no zinc, poor results) stacked into a tower; the two ends are the positive and negative terminals. **Its ailment becomes obvious within a few minutes of continuous supply: the current decays** — three causes (the three battery ailments, all to be measured and logged):

| Ailment | Symptom | Cause | Remedy |
|---|---|---|---|
| **Polarization** | Current gradually falls during continuous discharge; bubbles coat the electrodes | Electrolysis products (hydrogen bubbles) cling to the plates and block the way; internal resistance rises | **Depolarizer**: pack charcoal powder around the electrodes (absorbs hydrogen; an empirical practice — log it and verify); or switch to a two-solution cell |
| **Internal resistance** | Voltage under load clearly lower than open-circuit | Resistance of the electrolyte and electrodes | Raise the liquid temperature (slow), enlarge the plates, shorten the spacing |
| **Local action** | Leaking charge even when unused; plates whiten and waste away | Foreign-metal impurities / local micro-cells | Plate purity (select impurity-free faces); when not in use, lift the plates out of the liquid |

[Card 30-01 Daniell Two-Solution Cell] (eight fields)

1. **Input materials**: copper plate (positive electrode); zinc rod/zinc plate (negative electrode; iron if no zinc, with the halved capacity logged honestly); **concentrated copper sulfate solution** (the blue liquid; copper-mining byproduct or Chapter 26 copper salts); dilute sulfuric acid (zinc-electrode side, about 1 part oil of vitriol + 9 parts water, acid into water); unglazed clay pot (porous diaphragm) + outer trough.
2. **Tools required**: clay pot and outer trough (Chapter 11); acid-pickling and polishing supplies for the plates (Chapter 23 dilute acid or vinegar); galvanometer (in series, reading loaded voltage and current); voltage log page. Calibration: log open-circuit and loaded voltage cell by cell (comparison method), never from a nameplate.
3. **Operating sequence and control points**: (1) acid-pickle and polish the plates to remove oxides; (2) the outer trough holds dilute sulfuric acid with the zinc electrode, the clay pot holds copper sulfate solution with the copper electrode and sits in the trough — **the porous clay wall lets ions through without letting the two liquids mix quickly**; (3) **keep the copper-salt level lower than the zinc-side level** (copper solution seeping to the zinc side grows dendrites through the diaphragm — dendrite puncture is the classic death of a Daniell cell; a salt bridge is steadier if you can manage one); (4) let it stand half a day before loading; (5) load for 30 min and read the voltage drop. **Control points: the level difference is never skipped; once cells are stacked in series and the voltage rises, apply the safety boundary "wire with the power off, never touch with wet hands" — ordinary materials cannot serve as high-voltage insulation, so terminals must stay out of human reach.**
4. **Empirical parameters and calibration method**: open-circuit voltage ≈1.1 V class per cell (empirical, calibrate cell by cell); loaded voltage drop <10% over 30 min as the stability criterion (empirical); sulfuric acid dilution 1 part oil of vitriol + 9 parts water (empirical starting point, acid into water); capacity measurement see Card 30-02; more than half the blue liquid seeping out of the pot means remaking the liquids (criterion).
5. **In-process observation items**: whether the zinc electrode whitens (local action); whether the blue liquid fades (copper exhausted — add copper sulfate crystals); copper dendrites on the pot wall; open-circuit and loaded voltage of each cell; level difference between the two sides; loaded hours and voltage drop.
6. **Accept / rework / scrap criteria**: accept = loaded voltage (galvanometer in series) drops <10% in 30 min; rework = replace and remake the liquids (change the diaphragm when the liquid is weak or the diaphragm clogged); scrap = zinc plate perforated (change the plate), copper dendrites on the pot wall (remake and correct the level difference); more than half the blue liquid seeped out counts as failure and a rematch.
7. **Common failures and troubleshooting order** (by frequency): (1) voltage insufficient → weak liquid / clogged diaphragm (check levels and colour first, then change the diaphragm); (2) current decays fast → polarization (check the charcoal-powder depolarizer, or move to the two-solution structure); (3) sudden short and dead → dendrites through the diaphragm (inspect the pot wall, remake and correct the level difference); (4) draining when idle → local action (select impurity-free faces, lift the plates out of the liquid when idle).
8. **L1/L2/L3 evidence**: L1 = one cell discharged with open-circuit and loaded voltage logged; L2 = three cells in series powering a galvanometer steadily for a whole day; L3 = the battery archive (per-cell voltage log + capacity/internal-resistance records) + the consumption ledger (zinc 5–20 g per operating day, etc., into Chapter 38).

#### 30.2.2 Capacity, Internal Resistance, and the "Reference Cell"

- **Capacity (rough measurement)**: discharge the cell through a fixed load (a resistance wire of known value); the hours **from the start until the voltage falls to 60–70% of its initial value (empirical criterion)** × the average current (galvanometer comparison method) = the amp-hour-class capacity. Log the capacity of every cell of a batch in the register — this is the "how long will it last" account (the basis of the Chapter 38 battery-consumption ledger);
- **Internal resistance (voltage-drop method)**: measure open-circuit voltage V₀ and loaded voltage V once each; internal resistance r＝(V₀−V)×R/V (R is the load resistance). r rising month over month = an early warning of plate aging / liquid depletion;
- **Reference cell**: set aside the most voltage-stable Daniell cell, sealed and unused, as the **local voltage standard** (all voltage readings are checked against it) — the seed of the standard-cell idea; recheck quarterly;
- Ohm-relation experiment: connect iron wires of different lengths/thicknesses to the cell and watch the galvanometer deflection — the qualitative laws that current ∝ voltage and ∝ 1/resistance, plus a local wire-gauge-to-resistance cross-reference table (the quantitative version awaits the better table in Chapter 31).

Verify the water-circuit analogy of the three concepts immediately with apparatus: voltage = water-tower height (doubles in series); current = flow rate (bubble rate / heat); resistance = narrow pipe (the long-thin-wire effect is weak).

[Card 30-02 Capacity and Internal Resistance Measurement] (eight fields)

1. **Input materials**: an assembled Daniell battery (Card 30-01 output, each cell already logged); resistance wire of known value (fixed load R); galvanometer; pendulum clock or hourglass; capacity/internal-resistance log page; reference cell (the most stable cell, sealed and set aside).
2. **Tools required**: galvanometer (current by the comparison method); resistance wire and the wire-gauge-to-resistance table; pendulum clock for timing; voltage readings checked against the reference cell. Calibration: recheck the reference cell quarterly; the quantitative version of the wire-gauge table awaits Chapter 31.
3. **Operating sequence and control points**: (1) capacity — discharge through the fixed load, noting the starting voltage and the start time; (2) time it by the pendulum clock until the voltage falls to 60–70% of the starting value; (3) hours × average current (galvanometer comparison) = amp-hour-class capacity; (4) internal resistance — measure open-circuit V₀ and loaded V once each, r＝(V₀−V)×R/V; (5) log cell by cell and batch into the register, then pick the steadiest cell and seal it as the reference cell. **Control point: capacity and internal resistance are taken in one and the same discharge run — no topping the numbers up after changing the liquids; wire stacked cells only with the power off — ordinary materials cannot serve as high-voltage insulation, so terminals stay out of human reach.**
4. **Empirical parameters and calibration method**: capacity criterion line = discharge to 60–70% of starting voltage (empirical); internal-resistance formula r＝(V₀−V)×R/V (a method, not an empirical value); Daniell ≈1.1 V/cell (empirical, calibrate cell by cell); r rising month over month = warning of plate aging / liquid depletion; reference cell rechecked quarterly; current by comparison of deflections, absolute calibration awaits the Chapter 31 electrolytic method.
5. **In-process observation items**: starting and end voltage, discharge duration, average current (deflection), computed capacity, V₀ / V / R and computed r, liquid colour and zinc whitening, air and liquid temperature (internal resistance moves with temperature).
6. **Accept / rework / scrap criteria**: accept = a smooth discharge curve, capacity read at the 60–70% line, and a loaded voltage drop <10% over 30 min; rework = self-contradictory readings (voltage not checked against the reference cell, timing not recorded) — rematch the liquids and re-measure; scrap = r clearly above the rest of the batch (plate aging) or capacity unable to carry the workstation — demote that cell to "demonstration only" and strike it from the reference-cell candidates.
7. **Common failures and troubleshooting order** (by frequency): (1) capacity varying wildly → timing start or end criterion not standardized (standardize on the 60–70% read); (2) internal resistance rising month by month → plate aging or liquid depletion (top up or change plates); (3) voltage far off the reference cell → galvanometer needle weakened or coil damp (re-magnetize / dry out, recheck against the reference cell); (4) two capacity runs on the same cell far apart → different liquid temperature, or the load resistance wire heating and changing value (retest at the same temperature and resistance).
8. **L1/L2/L3 evidence**: L1 = one complete capacity and internal-resistance record for a single cell; L2 = the capacity/internal-resistance register written up + the reference cell sealed with quarterly recheck records; L3 = one liquid top-up or plate-change decision taken on the r and capacity trend and filed, with the batch capacity register citable by the Chapter 38 battery-consumption ledger.

### 30.3 Magnets and the Magnetic Field

- Natural lodestone (magnetite): attracts iron, points north–south; **magnetic poles**: strongest at the two ends, like poles repel and unlike attract; break a magnet bar and you get two new magnet bars (no monopoles);
- **Magnetizing steel needles (industrializing the compass)**: stroke the steel needle repeatedly along the lodestone in **one and the same direction** (one-way strokes, never back-rubbing; ◎ hand-feel: keep the pressure even, like grinding ink; practice method: magnetize ten needles and compare how much iron powder each picks up); or magnetize inside an energized solenoid (upgrade after 30.5); a magnetic needle floating on water (bowl + cork) is a compass;
- Visualizing the magnetic field: sprinkle iron filings on paper with a magnet bar beneath the paper — the pattern of lines of force;
- Geomagnetism: the compass points north–south and also dips — the cornerstone of navigation and surveying (Part 10 island edition). **Magnetic declination is corrected and logged against the local true-north line (Section 3.2.1 equal-shadow method)** — this is the step that turns the compass from a "toy" into an "instrument".

[Card 30-03 Magnetizing Steel Needles and Compass Correction] (eight fields)

1. **Input materials**: steel needles (high-carbon steel, pointed and straightened); natural lodestone (clearly attracts iron, ore site logged); cork and a bowl of water (floating-needle compass); true-north line mark (3.2.1 equal-shadow method); magnetic-declination log page; iron filings (for visualizing the lines of force).
2. **Tools required**: lodestone; protractor and angle reference (Chapters 3, 25); equal-shadow true-north line (3.2.1); iron-powder weighing (Chapter 3 balance, comparing pickup amounts). Calibration: the declination is logged against the local true-north line; needle strength is judged by comparing iron-powder pickup.
3. **Operating sequence and control points**: (1) stroke the needle repeatedly along the lodestone **in one and the same direction**, one-way and never back-rubbing (◎ hand-feel: even pressure, like grinding ink); (2) practice method — magnetize ten needles, compare iron-powder pickup needle by needle, and adopt the technique that picks up most; (3) thread the needle through a cork and float it; once still it points north; (4) measure the angle between the needle and the equal-shadow true-north line — that is the local magnetic declination; (5) log declination, date, observer, weather; (6) re-magnetize an under-magnetized needle; switch to high-carbon steel if the steel is too soft. **Control points: one-way strokes, never back-rubbing; a compass reading must be reported with the declination correction applied, never as "where the needle points".**
4. **Empirical parameters and calibration method**: magnetizing technique = one-way strokes, even pressure (◎ hand-feel, a parameter-table entry); declination logged against equal-shadow true north (system); iron-powder pickup as the magnetism criterion; magnetizing inside an energized solenoid is the upgrade route after 30.5; iron filings on paper show the lines of force (verify the poles — a broken magnet bar gives two new bars, no monopoles).
5. **In-process observation items**: iron-powder pickup per needle, still-pointing direction of the floating needle, angle to true north (declination), weather and observation time, whether the needle settles briskly (sluggish = weak magnetism), the field-line pattern and the breakage-test record.
6. **Accept / rework / scrap criteria**: accept = the floating needle holds a steady bearing, the declination is on the register, and two independent observations differ within the reading resolution; rework = the needle drifts or settles sluggishly — re-magnetize by the ten-needle comparison; scrap = pickup clearly below the batch after magnetizing (steel too soft) — remake from high-carbon steel; if the needle is sound but readings disagree with the season's declination register, re-measure the true-north line.
7. **Common failures and troubleshooting order** (by frequency): (1) needle magnetism fading → under-magnetized or soft steel (compare pickup → re-magnetize / switch to high-carbon steel); (2) unsteady bearing, swinging back and forth → off-centre float or wind on the water (re-thread the cork, shelter from wind); (3) compass systematically off by one angle → declination not corrected or the true-north line mis-measured (re-run the equal-shadow method); (4) galvanometer-style readings drifting → needle magnetism fading or coil damp (recheck against the reference cell, dry out).
8. **L1/L2/L3 evidence**: L1 = ten needles magnetized with one floating-needle bearing and true-north angle logged; L2 = the local declination register (with date and observer) + one actual orientation taken with the compass; L3 = a second person magnetizes from this card alone and measures the same declination (within reading resolution), and the compass is released for navigation and surveying (Part 10 island edition).

### 30.4 The Relation between Current and Magnetic Field

**Oersted's experiment**: lay a current-carrying wire parallel above the compass needle — it deflects; reverse the current and the deflection reverses. Conclusion: **a magnetic field exists around a current**.

Extensions:
1. The solenoid — magnetic effects add up; it behaves like a magnet bar (verify with the iron-filing pattern);
2. Log the right-hand rule (winding direction vs. polarity; the mistake-proofing basis for winding generators);
3. **The force of a magnet on a current-carrying wire**: a straight current-carrying wire placed between two poles feels a force and moves (the three-finger mnemonic). **Current + magnetic field → force** and **motion + magnetic field → current** (Chapter 31) are two faces of the same coin.

#### 30.4.1 Self-Induction and the Spark Coil (Mother of the Chapter 33 Leak Detector)

- **The self-induction phenomenon**: an energized coil produces a spark at **the instant of disconnection** — the faster the break, the bigger the spark (the sudden change of current in the coil induces high voltage. Experiment: when the electromagnet circuit is broken there is a clear spark at the contact point, while an ordinary resistive circuit shows almost none);
- **Making a spark coil**: on an iron core, one winding of thick wire with few turns (the primary, connected to the battery) + one winding of thin wire with many turns (the secondary, up to a thousand or more turns); put an **interrupter** in series with the primary (the electromagnet attracts the armature — power cut — armature springs back — attracts again, the same structure as the electric bell) — the primary current is switched on and off at high speed, a **thousands-fold voltage** (empirical order of magnitude) is induced in the secondary, and a spark jumps at the gap;
- **Applications land immediately**: ①ignition (gas/flammable-gas demonstration) ②**the Chapter 33 high-frequency spark leak detector uses it directly** — this is the key device this chapter plants for the vacuum line;
- Safety: the secondary spark is small but can still sting; when testing sparks, hold the gap electrodes with insulated handles.

[Card 30-04 Spark Coil] (eight fields)

1. **Input materials**: soft iron core; primary of thick wire, few turns; secondary of thin wire, a thousand-plus turns; interrupter (electromagnet + armature + contacts, same structure as the bell); battery pack (Daniell, 3-cell class); waxed cloth / oil-soaked paper insulation; gap electrodes (held with insulated handles).
2. **Tools required**: winding frame and hand-crank drill; waxed cloth (interlayer insulation); galvanometer (to check primary continuity); insulated-handle clamp; adjustable discharge gap (2/4/6/8/10 mm steps, set with thick paper slips). Calibration: spark length is graded fresh the same day (humidity changes daily; re-grade every other day).
3. **Operating sequence and control points**: (1) wind the primary on the core (thick wire, few turns, wired to the battery); (2) waxed cloth between layers, wind the secondary (thin wire, many turns, up to a thousand or more); (3) put the interrupter in series with the primary (attracts the armature — breaks — springs back — attracts again); (4) energize, listen to the interrupter and watch the gap for sparks; (5) open the gap from small to large and record the largest sparking gap; (6) if there is no spark, polish the contacts first. **Control points: test sparks only with gap electrodes held in insulated handles; the secondary is the step-up part and must stay out of human reach — ordinary materials cannot serve as high-voltage insulation, so use it only as "untouchable + insulated handles + wire with the power off".**
4. **Empirical parameters and calibration method**: primary thick wire with few turns / secondary thin wire with a thousand-plus turns (empirical); the secondary induces a thousands-fold voltage (empirical order of magnitude); the faster the break, the bigger the spark (self-induction); sparks are read against the range table — recording the "largest gap that does not discharge" beats recording an "occasional jump" (the 30.9 spark-grading method).
5. **In-process observation items**: whether the interrupter buzzes continuously, contact spark size and blackening, largest sparking gap (mm), number of cells and voltage, winding layers, scorch marks from secondary breakdown, humidity and date.
6. **Accept / rework / scrap criteria**: accept = continuous interrupter buzz and a steady spark at the gap, with two same-condition largest-gap readings within one grade; rework = no spark or intermittent spark — polish the contacts, adjust spring tension, check primary connections for oxide; scrap = secondary winding breakdown (interlayer scorch, spark migrating inside the winding) or an interlayer short in the core — rewind / change the core; once voltage is stepped up, carbonized insulation judges the unit scrap.
7. **Common failures and troubleshooting order** (by frequency): (1) no spark → interrupter contacts oxidized (polish, adjust spring tension); (2) weak, intermittent spark → weak battery or poor primary contact (add cells, check the connections); (3) spark migrating into the winding → insufficient secondary insulation (rewind, add waxed-cloth layers); (4) interrupter not buzzing → armature gap too large or spring blade too stiff (adjust per the four elements of 30.12).
8. **L1/L2/L3 evidence**: L1 = a steady spark with one largest-gap reading; L2 = spark-grade records + the coil parameter table (turns, wire diameter, layers); L3 = the device entered in the register with a handover record, for direct reuse by the Chapter 33 high-frequency spark leak detector.

### 30.5 Coils, Iron Cores, and Electromagnets

- **Iron core concentrates the field**: insert a soft iron rod (annealed state) into the solenoid and the magnetic field strengthens several-fold; **soft iron becomes magnetic when energized and loses its magnetism when the current stops**; hard steel retains magnetism (permanent magnets — a difference in carbon content and heat treatment; knowledge transferred from Chapter 19);
- **Electromagnet**: wind tens to hundreds of turns of insulated copper wire (waxed cloth / oil-soaked paper insulation in this chapter; enameled-wire upgrade in Chapter 31) on a soft iron horseshoe core; step up the lifting load grade by grade and record "turns × current vs. pull";
- Three application devices: electromagnetic iron-lifting, the **electric bell** (self-sustained oscillation), the **telegraph sound code** (on/off is a click; combinations of long and short are information).

### 30.6 How to Make Basic Electrical Measurements

- **Galvanometer (mother of all meters)**: a compass needle mounted inside a large coil; with no current flowing, the coil is aligned north–south; when energized, the deflection ∝ current (approximately linear in the weak region). To increase sensitivity: double the turns / a stronger needle / add a soft iron core;
- **Comparison measurement**: use a "standard deflection" as the reference; the ratio of two readings is the ratio of the currents. Absolute calibration (electrolytic method) waits for Chapter 31;
- Rough voltage measurement: wire a known resistance line in series and compare the difference in deflection. Copy the Chapter 25 five-element record system as-is.

### 30.7 From Experimental Phenomena to Repeatable Electromagnetic Devices

The three questions of device-ization (the substance of acceptance): ①disconnect and reconnect — does the phenomenon reproduce? ②does another person get the same result? ③when parameters change, does the direction of the effect match the pre-registered prediction? Pass all three and the device enters the register for later chapters to cite.

### 30.8 Converting between Electrical, Mechanical, and Thermal Energy

Three directions to log (laying track for Chapters 31–32):
1. **Chemical → electrical** (discharge) and **electrical → chemical** (electrolyzing water, depositing copper) — the seed of reversibility (**storage battery foreshadowed**: two lead plates in dilute sulfuric acid can be "charged" by passing current and "discharged" to deliver it — log the principle; the charging current source awaits the Chapter 31 generator, backfilled at 31.10);
2. **Electrical → heat** (wires warming, carbon rods glowing red-hot);
3. **Electrical → magnetic → mechanical** and the converse proposition (Chapter 31).

Energy-ledger awareness: the cell consuming zinc and acid = what is paid out; heat, magnetic, and mechanical work = what is gained — every new device must answer "where does the energy come from and where does it go" (the physics version of the Chapter 38 battery-consumption ledger).

---

### 30.9 Electrostatic Metrology: Making the Leaf Angle and the Spark Speak

Static electricity experiments degenerate most easily into "finger tricks" — lift a few paper bits, crackle once, and no number survives. This section promotes the electroscope and the Leyden jar from demonstration props to **measuring instruments**: all readings land on three tables (range card, spark range table, shock-sensation grading); the tables travel with the apparatus, and whoever operates it reads off them the same way.

**Electroscope leaf-angle graduation (the range-card system)**

- Calibration source: glass rod + silk is the only standard friction pair (if you switch to amber or sealing wax, regrade everything that same day). Standardize the rubbing stroke: one pass of 300 mm, one pass per second, 10 passes total recorded as "10 rubs". ◎ hand-feel: pressure such that the rod body does not bend; practice method — one person does a full 1/3/6/10-rub calibration round on 10 different days, and the differences in leaf angle are logged as "daily corrections";
- Range table (empirical starting point; calibrate each instrument individually): 1 rub → barely open (<10°); 3 rubs → small opening (15–25°); 6 rubs → medium opening (30–40°); 10 rubs → wide opening (>45°). Paste a handwritten range card on the body of each electroscope bottle, noting the calibration date and the weather;
- Criterion: repeat the same rub count three times; a spread in leaf angle <10° counts as pass; the whole table drifting by more than one grade = dampness or fatigued copper foil (verify: check against that day's freshly graded card); rework = bake the bottle + re-stick the foil;
- Humidity correction: grade one round on a rainy day and one round after consecutive clear days; the difference between the two rounds is logged as the "seasonal correction" — on humid days readings generally run one grade low; report the weather before reading the table.

**Rough estimation of Leyden jar charge (spark grades + shock-sensation grading)**

- Spark range table (discharger ball gap; same charging source, same number of charging strokes): no spark / only a faint glow inside the jar = empty grade; spark <2 mm = micro charge; 2–5 mm = small charge; 5–10 mm = medium charge; >10 mm = large charge. Method: ground one end of the discharger first, then bring the other end closer in steps of 2/4/6/8/10 mm, stopping at the first spark — **recording the "largest gap that does not discharge" is more reliable than recording an "occasional jump"**;
- Shock-sensation grading log (corroborating evidence only, never the primary criterion): grade 1 = tingling fingertips; grade 2 = a blow at the wrist; grade 3 = a numbing blow down the whole arm. **Red line: stop testing at grade 3**; the day's "largest grade" goes into the register; persons with heart conditions must not touch any grade (same safety clause as 30.1);
- Criterion: pass = two spark tests at the same charge count agree, or differ by within one grade; leakage suspected = after charging, let it stand 5 min and the spark drops two grades or more (verify: wipe the dry band clean, dry it, and retest).

**Electrostatic shielding and point discharge (two mandatory comparison demonstrations)**

- Shielding: cover the electroscope with a wire mesh (mesh ≤10 mm) and bring a charged Leyden jar close from outside the bottle — the leaf angle does not move; remove the mesh and it opens. Conclusion for the register: **inside the cage and outside it are two different worlds** (the intellectual root of protecting instruments from electrostatic interference);
- Point discharge: stick the tail of a sewing needle into the top ball of a Leyden jar, needle tip 10–15 mm from a candle flame; once charged, the flame is steadily blown aside — "the point puts out the candle". The comparison piece is the same jar fitted with a round-headed ball electrode: at the same distance the flame only wavers and does not go out. The record must state the contrasting point: **both are metal; the pointed one leaks charge, the round one stores it**;
- Applications logged: the collecting comb of the electrostatic generator and the lightning rod both grow out of this one needle.

[Card 30-05 Leyden Jar Fabrication and Discharge] (eight fields)

1. **Input materials**: glass bottle (uniform wall, no cracks, mouth 60–80 mm); tin foil (aluminum foil if tin is lacking, pressed flat, same performance), inner and outer walls each to 2/3 of the bottle height, about two palms of foil per application; cork stopper + copper rod and chain + top ball; discharger (dry wooden handle + thin metal rod with a small ball at the end).
2. **Tools required**: scissors; paste or shellac (let dry a full day after sticking); feeler gauge or thick paper slips (to set the ball gap; check with a 2 mm slip before use); electrostatic generator or rubbing rod (charging). Calibration: the charge-count-vs-spark-length curve is graded fresh the same day and re-graded every other day.
3. **Operating sequence and control points**: (1) bake the bottle by the stove for 1 h until thoroughly dry; (2) stick foil on the inner wall to 2/3 height (a hand can reach inside to work); (3) stick foil on the outer wall to the same height as the inner wall — **control point: leave a dry band ≥30 mm between the two foils, and the foil edges must not curl over across it (surface tracking across the band means leakage)**; (4) seal the stopper with the rod through, the chain hanging to touch the inner foil; (5) charge repeatedly with the generator or a rubbing rod; (6) always discharge with the discharger, **grounded end first and only then approach the bottle**. Also: **ordinary materials cannot serve as high-voltage insulation** — the jar interior is the step-up, energy-storing part and must stay out of human reach; approaching it bare-handed means a shock, and persons with heart conditions must not operate it.
4. **Empirical parameters and calibration method**: dry band ≥30 mm (procedure); spark grades micro <2 / small 2–5 / medium 5–10 / large >10 mm (empirical); two spark tests at the same charge count differing <20%, and a grade drop <2 after standing 5 min, as pass (empirical); shock grades 1 = tingling fingertips, 2 = a blow at the wrist, 3 = numbing blow down the whole arm, stop testing at grade 3 (red line).
5. **In-process observation items**: whether foil edges curl or wrinkle (discharge travels along the edges), faint purple glow on the dry band (leakage), spark length grade, shock-sensation grade, number of charging strokes, grade after standing 5 min, humidity and date.
6. **Accept / rework / scrap criteria**: accept = two spark tests at the same charge count within <20% and a grade drop <2 after standing 5 min; rework = bake the bottle, press the foil edges down, wipe the dry band clean, then retest; scrap = wall crack or white puncture traces (change the bottle); a drop of two grades or more after 5 min standing is treated as suspected leakage (wipe and dry the band, retest).
7. **Common failures and troubleshooting order** (by frequency): (1) will not hold charge → dirty or damp dry band (wipe with alcohol, bake again); (2) sparks smaller → foil edges lifting (press flat, re-stick); (3) no charge at all → chain desoldered or stopper damp (pull the stopper, check the chain); (4) the whole grade table drifting → rising humidity or fatigued copper foil (compare with that day's freshly graded card, re-grade).
8. **L1/L2/L3 evidence**: L1 = a steady 2 mm spark; L2 = the spark range table + records of the shielding and point-discharge demonstrations entered in the register; L3 = the electrostatic metrology ledger (including range-drift corrections) with complete discharger-use records.

### 30.10 Standardizing Quantitative Demonstrations of the Three Effects of Current: Three Tables

Sections 30.2–30.8 have shown the "phenomena" of the magnetic, chemical, and thermal effects; this section raises each of the three by one level — **each effect delivers one table that a different person can re-measure**; records follow the Chapter 25 five elements. The acceptance questions are unchanged: does disconnect-and-reconnect reproduce? Does another person get consistent results?

**Magnetic effect: deflection-vs-turns table**

- Apparatus: when winding the galvanometer coil, leave taps in reserve — one terminal each brought out at 10/20/40 turns (same winding direction, same needle); the power source is fixed as one Daniell cell + the same load iron wire;
- Readings: record the equilibrium deflection at each of the three turn grades, three repetitions each, take the median;
- Criterion: a difference between the deflection ratio and the turns ratio <15% (empirical value, weak linear region) counts as pass; beyond that = already out of the linear region — log the "saturation angle" (the critical reading beyond which the deflection no longer grows with the turns); from then on, always take readings below half the saturation angle;
- Calibration method: recheck the turn grades once a quarter against the reference cell (30.2.2); if the deflection has drifted >10%, recalibrate or rewind.

**Chemical effect: comparing deposit amounts at equal charge (copper/hydrogen baths in series)**

- Apparatus: a copper bath (dilute copper sulfate solution + two copper plates, electrode spacing 30 mm) and a hydrogen bath (1:9 dilute sulfuric acid + two carbon rods) connected **in series** to the same battery pack — series connection guarantees both baths carry **the same current for the same time**, timed with a pendulum clock for 10 min;
- Readings: weigh the copper bath's cathode (record the gain to 0.1 g; gram-scale balance see the Chapter 3 measuring tools); over the hydrogen bath's cathode, collect the gas in an inverted graduated test tube and read the gas column volume (mL);
- Criterion: two rounds under the same conditions with copper weight-gain difference <10% and hydrogen volume difference <15% counts as pass; if the copper gain is zero, first check for oxidized connections; if the hydrogen is zero, first check whether the carbon rods were wax-boiled (gas trapped in the carbon pores will deceive you — boil new carbon rods in wax first to expel the air);
- Conclusion to log: **at the same charge, the amount deposited in each bath is its own constant** — this is the idea of electrolytic equivalence (the absolute calibration method awaits Chapter 31).

**Thermal effect: heating comparison with the same current and different wire diameters**

- Apparatus: connect 0.5/0.8/1.2 mm iron wires, each 200 mm long, one at a time into the same battery-pack circuit; **hang one wax bead of the same size at the midpoint of each wire** (drip-formed with a fine needle dipped in molten wax, 4–5 mm in diameter), with a porcelain dish beneath to catch the dripping wax;
- Readings: start timing when the current flows; record the time (s) for the wax bead to melt off; randomize the order in which the three wires take their turns, so "the battery weakening as it discharges" does not contaminate the comparison;
- Criterion (empirical starting point; calibrate against the local battery pack): the bead falls within 60 s on the 0.5 mm wire and does not fall within 5 min on the 1.2 mm wire — the comparison stands; the bead fails to fall on all three wires = the battery is weak; add cells up to 3 in series and retest;
- Safety: keep the heating wires away from acids and flammables; never leave the current unattended; change wires only after cutting the power.

With all three tables complete, the "three effects of current" turn from a noun into three re-measurable measuring instruments.

---

### 30.11 Earth Return and First Grounding

The old telegraph trick for saving copper is to use the earth as half a wire: one overhead line + a ground electrode at each end. This section builds the prototype — **prove the earth conducts, make a ground electrode that passes, and log the seasonal account of soil conductivity**. The formal grounding standard is established in Chapter 32; here we build only the minimal usable version.

**Demonstration: the earth as a conductor**

- Apparatus: two ground electrodes 10–30 m apart, each brought indoors by a lead wire; wire the electric bell (30.5 device) and 3 Daniell cells in series into the circuit — the bell rings, so the current is crossing through the earth;
- Criterion: the ringing is clearly audible; break either electrode's lead wire and the bell stops at once (proving the current really goes through the earth, not through wire touching wire);
- Extension to log: swap the battery polarity and the bell is unchanged — the earth does not distinguish polarity (contrast: put an electrolysis bath in series in a metallic circuit and it does, see 30.10).

**Making a ground electrode (prototype version)**

- Materials: one iron rod ≥16 mm in diameter and 1–1.2 m long (drill the top and crimp or lead-solder the lead wire); backfill of charcoal powder and coarse salt pre-mixed 2:1 by volume, about 2 L;
- Driving method: choose soil that stays moist year-round; drive the rod in until its top stands 300 mm above ground; pull it out halfway, sprinkle in backfill, and drive it in again — do this twice; **a backfill ring hugging the rod closely is the key to lowering resistance**;
- Criterion: retest with bell + cells in series; wiggle the lead wire and gently rock the rod — if the ringing is unchanged, contact is good; weak ring = pour in 5 L of salt water until soaked and retest; still weak = drive 300 mm deeper or add backfill;
- Silent failure first: a failed ground electrode makes no sound — **pick one fixed day each month to retest with the bell in series**; log the ring in three grades, strong/medium/weak; two consecutive weak months means repair — do not wait for it to fail on you.

**Logging the seasonal variation of soil conductivity**

- Method: fix one pair of ground electrodes + a fixed number of cells; read the deflection with a galvanometer in series; measure one round on the first clear day after the first of each month, and one round on the day after a rain;
- Table format: Month | deflection after rain | deflection on clear day | soil grade (strong/medium/weak) | remarks (frozen/drought/waterlogged);
- Expectation (empirical): deflections are high after rain and during the humid summer; in winter freeze and prolonged drought they can fall by half or more — **for any line that depends on the earth, check this table first before blaming the apparatus**;
- System: once this table covers a full year, transcribe it into the ledger (Chapter 43 system); the formal Chapter 32 grounding standard uses it as its local basis.

### 30.12 Electric Bell and Relay: Detail-Drawings-Level Fabrication

The bell (30.5) demonstrated self-sustained oscillation; this section takes it apart to the level of adjustable, measurable, repairable — and along the way grows the **relay**: the same electromagnet + armature + contacts, with the bell replaced by a silent signal contact — a switch that "uses a small current to throw a large current". The Chapter 32 telegraph relay depends entirely on it.

**Four elements, each individually adjustable**

1. **Armature gap**: cold starting point 2 mm (measured with a feeler gauge), approach the optimum in 0.5 mm steps. Too large = will not pull in, or the strike is feeble; too small = will not break open, sticking tendency rises. Pass criterion: the bell rings continuously and crisply, and stops the instant power is cut;
2. **Contact material and pressure**: silver strip is best (it oxidizes reluctantly); use copper strip if no silver (grind once a week: fold fine sandpaper with the grit inward, clamp the contact, and draw it through 3–5 times). Pressure is not measured directly; compensate with **overtravel** — after the armature pulls fully in, the moving contact must push the stationary blade along with it for 0.3–0.5 mm (the film-wiping action). ◎ hand-feel: pre-bend the spring blade to "about to snap but not yet"; practice method — bend 20 pieces from scrap spring blades, and for each piece use the pull-in current as the objective criterion to check the hand-feel in reverse, until the hand-feel and the criterion agree;
3. **Self-sustained oscillation frequency**: determined by the spring blade's stiffness, the armature's mass, and the gap; of the three, the gap is the most sensitive. How to log: count the strikes in 10 s and divide by 10; record "strikes/second" (slow grade 2–4; fast grade rings in a continuous blur, beyond counting);
4. **Pull-in and drop-out currents**: measurement method see Card 30-06. Return coefficient = drop-out current / pull-in current, empirically 60–80%; a coefficient too low = gap too large or spring blade too stiff.

[Card 30-06 Relay Fabrication and Pull-In Measurement] (eight fields)

1. **Input materials**: electromagnet on a soft iron core (finished 30.5 unit or freshly wound, 200–400 turns, waxed-cloth insulation); armature of thin iron sheet 0.5–1 mm thick; spring blade of watch-mainspring steel or brass sheet 0.3–0.5 mm thick (bamboo strip backed with copper foil if no mainspring steel — shorter life, must be logged honestly); silver or copper contacts 2×3 mm; one wooden baseboard.
2. **Tools required**: hand-crank drill, needle files, feeler gauge (0.5–3 mm grades), galvanometer (deflection converted to current), a lamp for first-test current limiting. Calibration: gap approached from a 2 mm starting point in 0.5 mm steps; pull-in current judged as "the smallest battery grade at which the armature just moves".
3. **Operating sequence and control points**: (1) wind the core, waxed cloth between layers; (2) mount the armature and spring blade, **cold gap 2 mm** (feeler gauge); (3) align the contacts, **control point: overtravel 0.3–0.5 mm** (still pushing the stationary blade after pulling fully in, guaranteeing self-wiping of the oxide film); (4) wire a lamp in series for the first test; (5) measure pull-in/drop-out currents grade by grade and log them; (6) return coefficient = drop-out / pull-in, empirically 60–80%. Once voltage is stepped up the contacts and coil are live parts: **ordinary materials cannot serve as high-voltage insulation** — keep them out of human reach and disconnect the power before wiring.
4. **Empirical parameters and calibration method**: cold gap 2 mm starting point, 0.5 mm steps; overtravel 0.3–0.5 mm (procedure); return coefficient 60–80% (empirical); pull-in/drop-out measured three times within <20% counts as accurate; copper contacts without silver ground once a week (fine sandpaper folded, 3–5 draws); oscillation frequency logged as "strikes/second" (slow grade 2–4).
5. **In-process observation items**: whether the pull-in sound is crisp or dull, contact spark size, whether the spring blade snaps back cleanly, contact blackening after 100 continuous operations, pull-in/drop-out currents and the return coefficient, gap readings.
6. **Accept / rework / scrap criteria**: accept = pull-in/drop-out three times within <20% and 100 continuous operations without sticking; rework = grind the contacts, add pre-bend, adjust the gap; scrap = fatigue fracture of the spring blade or an interlayer short in the core (replace the part); an armature that will not release after power-off and sticks when pushed = contact sticking, handled per the failure table.
7. **Common failures and troubleshooting order** (by frequency): (1) no pull-in → check in order: too few cells → too few turns → gap too large → spring blade too stiff; (2) no drop-out → gap too small → contacts fused → spring blade too soft (remedies in that order: enlarge the gap, grind the contacts and add overtravel, change the spring); (3) jittery rapid-fire action → insufficient contact pressure (add pre-bend); (4) contacts blackening fast → insufficient overtravel or unsuitable contact material (switch to silver, add overtravel).
8. **L1/L2/L3 evidence**: L1 = pull-in action visible to the naked eye and repeatable; L2 = the pull-in/drop-out current log written up + a 100-operation continuous record; L3 = the relay entered in the register with contact material and life records, for direct citation by the Chapter 32 telegraph relay.

---

## Master Parameter Table

| Parameter | Value | Class |
|---|---|---|
| Daniell voltage | ≈1.1 V/cell (open circuit) | Empirical; calibrate cell by cell |
| Loaded stability criterion | Voltage drop <10% in 30 min | Empirical |
| Sulfuric acid dilution | 1 part oil of vitriol + 9 parts water (acid into water) | Empirical starting point |
| Capacity criterion line | Discharge until 60–70% of starting voltage | Empirical |
| Internal resistance formula | r＝(V₀−V)×R/V | Method |
| Dendrite prevention | Copper-salt level **lower than** zinc-side level | Procedure |
| Spark coil turns ratio | Primary thick wire, few turns / secondary thin wire, a thousand-plus turns | Empirical |
| Magnetizing technique | One-way strokes, even pressure | ◎ hand-feel |
| Compass correction | Log the local magnetic declination against equal-shadow-method true north | System |
| Electroscope grades | 1/3/6/10 rubs → barely/small/medium/wide open (calibrate each unit, paste the card) | Empirical; calibration into ledger |
| Leyden jar spark grades | micro <2 / small 2–5 / medium 5–10 / large >10 mm | Empirical |
| Dry band width | ≥30 mm between the inner- and outer-wall foils | Procedure |
| Linear region criterion | Difference between deflection ratio and turns ratio <15% | Empirical |
| Equal-charge criterion | Copper weight-gain difference <10%, hydrogen volume difference <15% across two rounds | Empirical |
| Ground electrode backfill | Charcoal powder : coarse salt = 2:1 by volume, about 2 L per electrode | Empirical starting point |
| Armature cold gap | 2 mm starting point, approach in 0.5 mm steps | Empirical |
| Contact overtravel | 0.3–0.5 mm | Procedure |
| Relay return coefficient | Drop-out ≈ 60–80% of pull-in | Empirical |

## Failure Modes and Diagnosis

| Symptom | Candidate causes (by probability) | Verification | Action |
|---|---|---|---|
| Cell current decays within minutes | Polarization (hydrogen bubbles coating the plates) | Look at the bubbles on the plates | Add charcoal powder depolarizer / switch to Daniell |
| Voltage collapses under any load | High internal resistance | Measure r by the voltage-drop method | Enlarge the plates / shorten the spacing |
| Draining even when unused | Local action (impurity micro-cells) | Plates whitening | Select pure faces; lift the plates out when idle |
| Daniell cell suddenly shorted and dead | Dendrites through the diaphragm | Copper dendrites visible on the pot wall | Remake the liquids + correct the level difference |
| Blue liquid fading | Copper ions exhausted | Visual color comparison | Add copper sulfate crystals |
| Spark coil gives no spark | Interrupter contacts oxidized | Polish the contacts | Adjust the spring tension / grind the contacts |
| Needle magnetism fading | Under-magnetized / steel too soft | Compare iron-powder pickup amounts | Re-magnetize; switch to high-carbon steel |
| Galvanometer readings drifting | Needle magnetism fading / coil damp | Recheck against the reference cell | Re-magnetize; dry out |
| Static grades drifting (leaf angle shrinks at the same rub count) | Rising humidity / fatigued, deformed copper foil | Compare against that day's freshly graded range card | Bake the bottle and the foil; re-stick the foil; re-grade the range table |
| Relay contacts sticking (armature does not release when power is cut) | Insufficient contact pressure + spark welding / oxide film | With power off, push the armature and see whether the contacts stick | Grind the contacts; increase the overtravel; switch to silver contacts |
| Earth circuit intermittently open | Ground electrode contact resistance changing with soil moisture / lead wires rusting | Wiggle the lead wire and see if the bell recovers; re-measure the deflection after rain | Pour in salt water + top up the charcoal-salt backfill; switch the lead wires to lead-soldering for rust protection |

## Process Card Index

## Acceptance Criteria

- **L1**: Oersted's experiment reproduced with reverse-current verification; voltaic pile demonstrating two effects (bubbling / heating); magnetic-needle compass holding a steady bearing with the true-north correction logged.
- **L2**: three Daniell cells in series powering a galvanometer steadily for a whole day (drop <10% in 30 min); one measurement record each for capacity and internal resistance; the electromagnet "turns × current vs. pull" table written up; spark coil jumping a spark successfully; galvanometer repeatability (two deflections differ by <half a division); electroscope range card and Leyden jar spark range table each written up; each of the three tables of the three effects (deflection-vs-turns, copper/hydrogen equal-charge, wax-bead melt time) with one re-measurement record by a different person; relay pull-in/drop-out current measurement entered in the register.
- **L3**: supply lines for the three consumables zinc/iron, acid, and copper salts entered in the ledger (Chapter 38); reference-cell system in operation (quarterly recheck); device register complete for direct citation by Chapter 31; storage-battery plate pre-fabrication ready (awaiting the Chapter 31 charging backfill). Evidence: battery archive, reference-cell recheck records, consumption ledger, electrostatic metrology ledger, soil seasonal conductivity log.

## Work Hours, Manpower, and Consumption

| Item | Manpower | Work hours (empirical values) |
|---|---|---|
| One set of three Daniell cells | 1 person | 1 day (including mixing solutions) |
| One spark coil | 2 people | 2–3 days (mostly winding) |
| One round of capacity/internal resistance measurement | 1 person | Half a day |
| Magnetizing ten steel needles | 1 person | 1 h |
| Electroscope grade calibration (including one daily-correction round) | 1 person | Half a day |
| One pair of ground electrodes (including driving and backfill) | 2 people | Half a day |
| Monthly soil conductivity recheck (two electrodes, one line) | 1 person | 0.5 h |
| One relay (including pull-in measurement) | 2 people | 2 days |
| Consumption | Per operating day: zinc 5–20 g, acid, copper sulfate | Entered in the Chapter 38 ledger |

## Safety Boundary

- Leyden jars are always discharged with the discharger after charging; shock "games" are strictly forbidden;
- Water electrolysis tests: no open flame where hydrogen collects;
- Acid rules as in Chapters 23/26 (ventilation, **acid into water**, 15 min of clean water if splashed in the eyes);
- The spark coil secondary is sting-level — operate with insulated handles; once battery packs are wired in series and voltage rises, enforce "wire only with power off, never touch with wet hands";
- Circuit discipline is established from the very first device: **disconnect the power before wiring** — the habit will save lives when the high-voltage era arrives.

## A. Tools Already in Hand

Copper/zinc/iron stock (Chapters 17, 18); lodestone (Chapter 16); vinegar and the three acids (Chapter 23); distilled water (Chapter 26); compass and angles (Chapters 3, 25); record system (Chapter 25); clay-pot diaphragm (Chapter 11).

## B. New Tools Added in This Chapter

Electroscope, Leyden jar, and discharger; **the Daniell two-solution cell (depolarized two-solution structure) and treatment of the three battery ailments**; **capacity/internal resistance measurement methods and the reference-cell system**; conductor-insulator grading table; wire-gauge-to-resistance cross-reference table; magnetized steel needles and the **true-north-corrected compass**; iron-filing visualization; Oersted and the three-finger mnemonic; **self-induction and the spark coil (with interrupter)**; the solenoid and the three electromagnet devices; the galvanometer and the comparison method; **electroscope range cards and the spark range table (electrostatic metrology)**; **copper/hydrogen baths in series and the wax-bead heating comparison (the three quantitative tables of the three effects)**; **ground electrodes and the soil seasonal conductivity log**; **the relay and pull-in/drop-out current measurement methods**; the storage-battery principle logged and plates pre-fabricated.

## C. Unresolved Dependencies

Charging current source for storage batteries (backfilled at 31.10 of Chapter 31); absolute calibration (Chapter 31 electrolytic method); insulated copper wire in bulk (Chapter 31); strong-permanent-magnet bootstrap (Chapter 31 magnet bootstrap chain); vacuum and thermionics (Chapter 33).

## Next-Step Dependencies

Chapter 31: the electromagnet and the galvanometer are the two cornerstones of the generator; electrolytic calibration; storage-battery backfill. Chapter 32: the bell contacts and the sound code grow into the telegraph; the relay (30.12) serves as the relay mother machine; the formal grounding standard uses the 30.11 prototype and the seasonal conductivity table as its local basis. Chapter 33: the spark coil = the high-frequency leak detector; the thermal-effect route extends into the lamp filament. Chapter 35: chemical power sources take this chapter's cell as their prototype. Chapter 38: the battery-consumption ledger.
