# Chapter 32 From Wires to the Grid

## Chapter Goals

Grow "one generator" into "one system": mass production of conductors and insulators, switch and fuse protection, battery storage, the electric motor (the electrical extension of the power network), the transformer and the AC system, the engineering account of line loss and supply distance — and finally the assembly of a small power network with a maintenance regime built on top.

**Core idea: a power system is a complete engineering system, not merely generation equipment.**

## Minimum Prerequisites

| Capability | Source |
| --- | --- |
| Generator, wire drawing, enameled wire, moving-coil meters | Chapter 31 |
| Glazed pottery firing | Chapters 11–12 |
| Sulfuric acid (crude grade), lead | Chapter 26, Chapters 16–17 |
| Electric-bell contacts and sounder code | Chapter 30 |
| Instrument regime and record-keeping | Chapters 25, 27 |

## Capability Boundary

**Can do:** the three-wire-gauge production line; umbrella-skirt porcelain insulators and wet-state re-verification; fuse rating calibration; ampacity red-line management by temperature rise; lead-acid charge/discharge cycling; transformers and unified-frequency AC; single-wire telegraph circuits; the electric-shock first-aid protocol.

**Explicitly cannot do:** precise metering of electric energy (the electric meter is a long-term item); systematic insulation design for high-voltage engineering (stops at the "moderate step-up" tier); the induction AC motor (AC theory not yet mature — registered as a next step).

**External dependencies:** a stable supply of lead and sulfuric acid (Chapters 16–17, 23); glazed-pottery kiln capacity (Chapters 11–12).

## Pre-Work Verification (Check Off Item by Item)

| # | Verification item | Criterion | Source |
| --- | --- | --- | --- |
| 1 | Generator and the three meters | Chapter 31 L2 met; voltage/current meters cleared by release slip | Chapters 31, 27 |
| 2 | Three wire-gauge tiers | coarse/medium/fine each ≥100 m; wire-diameter micrometer registered | Chapters 22, 31 |
| 3 | Fuse blanks | tin wire/low-melting-alloy wire in three tiers or more, diameters registered | Chapter 17 |
| 4 | Porcelain insulators | glaze complete, no cracks (crisp ring when tapped); wet-state re-verification passed | Chapters 11–12 |
| 5 | Lead plates and dilute acid | lead grid plates cast; dilute sulfuric acid density registered | Chapters 17, 23 |
| 6 | Grounding electrode | iron rod + charcoal-salt backfill pit dug | This chapter |
| 7 | Meter-reading register | the electric-power page of the power ledger opened | Chapter 29 |
| 8 | First-aid protocol | electric-shock first aid posted at every household; quarterly drill plan in place | This chapter |

***

### 32.1 Copper Wire, Conductive Materials, and Conductor Manufacture

* Wire drawing becomes a production line (the Chapter 31 single die → continuous operation): multiple dies in tandem + capstan linkage (power from Chapter 21), inter-stage annealing furnace (dark red, Chapter 18); **wire-gauge standardization** (transplanting the institutional thinking of Chapter 22): three wire diameters cover everything — coarse (trunk lines/large currents), medium (indoor wiring), fine (coils/instruments);

* Conductor material selection table (measured locally): copper first; iron wire's resistance is on the order of six times copper's (empirical value, must be field-calibrated) but its strength is good — **iron wire suits long overhead spans where resistance is sacrificed; copper wire is reserved for equipment**;

* The boundary of aluminum (honest registration, knowledge kept as background): aluminum is lighter and cheaper, but smelting it requires enormous electrolytic power (molten-salt electrolysis of alumina in cryolite); not feasible today — placed on the "when to unlock" list (when the power surplus is a hundredfold);

* Joint workmanship: twisting + tin soldering (Chapter 17) + insulation wrapping; **joints are the number-one cause of line faults** — copy the process-card and spot-check regime of Chapter 22.

### 32.2 Sources and Performance of Insulating Materials

* **Porcelain insulators (the king of outdoor insulation)**: glazed pottery (Chapters 11–12) thrown into an umbrella-skirt shape — the skirt edge cuts off the rainwater film path; glazed after firing to seal the pores; fitted with a glued-in wood core or a through bolt (hole reserved at forming time); breakdown and creepage are reduced to two disciplines: **dry-state clearance starts at ten times the wire diameter; in the wet state, rely on the umbrella skirt** (empirical values, must be field-calibrated);

* Indoor insulation: porcelain cleats/porcelain knobs fastening bare wire (air insulation); oil-paper/waxed-cloth wrapping (Chapter 31) used at wall penetrations and crossings;

* Wood-trough wiring impregnated with an asphalt/rosin compound (the upgrade for humid environments);

* Insulation performance test: connect the piece under test in series with a galvanometer + battery; no deflection = pass; humidity test (re-test after a water-mist spray) — **wet-state insulation must be re-verified** (the lifeline of the rainforest/island editions).

### 32.3 Switches, Fuses, and Basic Protection

* **Knife switch**: hardened copper blade + copper clip jaws, spring-assisted fast opening (a slow opening draws an arc that burns the jaws); insulated handle (wax-soaked wood); the switch must sit in series on the "live" side, and breaking as a double-pole pair is preferred;

* **The fuse (the system's sacrificial part)**: fine tin wire/low-melting-alloy wire (Sn-Pb-Bi ratios registered per the Chapter 17 alloy experience) in series in the main run — it melts and opens on overcurrent; **the fuse rating table**: wire diameter mapped to fusing current (measured calibration); substituting copper wire for a fuse is strictly forbidden (the source of historical accidents — a red line);

* **Grounding**: a wet-soil pit + charcoal-salt backfill + an iron-rod electrode; metal enclosures (e.g., motor frames) bonded to earth — under a leakage fault the current flows through the ground wire, and a person touching the enclosure does not become the circuit;

* **The protection action chain**: fault → fuse blows → inspect → replace with a same-rated fuse → if it blows again, shut down and trace the line (repeated blowing = a line or load fault; thickening the fuse to force power through is forbidden — the second red line).

#### 32.3.1 Ampacity and the Temperature-Rise Red Line (Wire Selection Table)

How large a current a wire can carry is decided by **heating**, not by "whether it conducts". **Acceptance criterion: full-load running for 1 h, the back of the hand can rest on it (**≤50 ℃ class**) = pass; 60 ℃ is allowed only for a momentary touch; sustained scalding that makes the hand recoil = overload; move up one wire size.**

| Wire tier | Empirical ampacity (starting values, must be field-calibrated) | Use |
| --- | --- | --- |
| Fine wire (instrument/coil class) | 1–2 A | meters, signaling |
| Medium wire (indoor-wiring class) | 5–10 A | lamp groups, small motors |
| Coarse wire (trunk class) | 15–30 A | trunk lines, electrolysis |
| Iron wire (overhead class) | derated to 1/2 of same-diameter copper (resistance ≈6×) | long-span overhead |

**Calibration method**: take 2 m of each wire, wire it in series with an ammeter and an adjustable load (water resistor), raise the current step by step until the wire reaches the "back-of-hand can-rest-on-it" upper limit, and record that current as the local ampacity — once entered in the meter-reading register it becomes the basis of wire selection. **For conduit/bundled runs, apply six to seven tenths of the bare-wire ampacity** (poor heat dissipation; empirical value).

[Card 32-02 Ampacity Calibration] (eight fields)

1. **Input materials**: a 2 m sample of each wire tier (fine / medium / coarse / iron); water resistor (adjustable load); joints and clamps.
2. **Tools required**: ammeter (Chapter 31 moving-coil meter, cleared by the Chapter 27 release slip); micrometer (diameter registration, Chapter 22); the back of the hand (the temperature criterion — a calculated value never substitutes for it); meter-reading register. Pre-use calibration: meter zero and range cleared; measure the diameter with the micrometer — never trust the nominal gauge number.
3. **Operating sequence and control points**: (1) cut 2 m of each tier; (2) wire it in series with the ammeter and the adjustable water resistor; (3) raise the current step by step; (4) raise it until the wire reaches the "back of the hand can rest on it" limit (≤50 ℃ class; 60 ℃ momentary touch only); (5) record that current as the local ampacity; (6) for conduit / bundled runs apply six to seven tenths of the bare-wire figure; (7) enter it in the meter-reading register as the basis of wire selection. Control points: only temperature counts, not "whether it conducts"; calibrate each tier on its own, never across tiers; the clamps must be tight (contact-resistance heating fakes an overload).
4. **Empirical parameters and calibration**: starting values — fine 1–2 A / medium 5–10 A / coarse 15–30 A; iron wire at 1/2 of same-diameter copper (resistance ≈6×); conduit and bundled runs at six to seven tenths; the temperature-rise red line = full load 1 h, restable on the back of the hand (≤50 ℃ class; 60 ℃ momentary only). All are empirical starting values, to be calibrated to local conditions and re-checked batch by batch.
5. **Process observation and recording items**: tier / batch / measured diameter; the current steps against the hand verdict (cool / warm / hot); the set-value current; ambient temperature and whether bundled; any discoloration or smoking of the sample.
6. **Pass / rework / scrap criteria**: pass = full load 1 h, restable on the back of the hand, no smoking, no discoloration. Rework = judged hot or the hand recoils (overload) → move up one size, or shed load and recalibrate. Scrap = the sample has discolored, softened, or scorched its insulation (that batch is not for trunk lines; if it happens batch-wide, recalibrate the whole batch before assigning any duty).
7. **Common failures and troubleshooting order**: (1) the wire scalds the hand (overload or too fine a wire); (2) large scatter when the same tier is retested (contact resistance at the clamps, ambient temperature differences); (3) overheating once bundled (the six-to-seven-tenths derating was not applied; if it is still hot, drop another size); (4) iron wire used at copper ampacity (same diameter must be derated to 1/2).
8. **L1 / L2 / L3 evidence**: L1 = one set value for each of the three gauge tiers, plus one for iron wire (checked against the 1/2 derating for same-diameter copper); L2 = the value table on the electric-power page of the meter-reading register, serving as the basis of wire selection; L3 = recalibration on batch change or annually, with consecutive recalibration records on file.

#### 32.3.2 Fuse Fusing-Current Calibration

[Card 32-01 Fuse Calibration] (eight fields)

1. **Input materials**: several diameter tiers of tin wire / low-melting-alloy wire (Sn-Pb-Bi ratios registered per the Chapter 17 alloy experience); water-resistor box (adjustable load); leads and clamps.
2. **Tools required**: micrometer (measuring wire diameter, Chapter 22); water-resistor box; ammeter (cleared by the Chapter 27 release slip); timing means (reading 5 min and 10 s, the Chapter 25 counting method); clamps (uniform wire length). Pre-use calibration: ammeter zero and range cleared; every tier's diameter measured with the micrometer and registered.
3. **Operating sequence and control points**: (1) measure the wire diameter (micrometer) and register it; (2) wire into the circuit and raise the current step by step; (3) **record two currents: the largest carried for 5 min without blowing, and the smallest that blows within 10 s** (between them lies that wire's fusing band); (4) tabulate tier by tier: wire diameter → fusing band. Control points: fuse length uniform (about 5 cm); clamping contact good (contact-resistance heating causes false blowing).
4. **Empirical parameters and calibration**: fuse length ≈5 cm, uniform (empirical — too long dissipates heat and will not blow, too short blows falsely); fusing band = 5-min no-blow maximum to 10-s must-blow minimum (calibration method; a theoretical calculation never replaces the measurement); in use, the upper limit of the fuse's fusing band ≈ the line's ampacity (wire-protection matching, 32.3.1). Calibrate to local conditions and recalibrate every wire batch.
5. **Process observation and recording items**: wire number / diameter / alloy ratio registered; wire length; current steps; the 5-min no-blow maximum; the 10-s must-blow minimum; clamping condition; retest agreement.
6. **Pass / rework / scrap criteria**: pass = every tier has a clear band and retests agree. Rework = retests disagree (re-clamp, unify the length, and recalibrate). Scrap = mixed batches or missing diameter records (recalibrate the batch whole; any batch with copper wire mixed in is rejected outright — **red line: copper wire must never substitute for a fuse**).
7. **Common failures and troubleshooting order**: (1) false blowing (first check the clamping → then whether the wire is too short); (2) fails to blow when it should (check for copper wire mixed in — a red line; reject the batch); (3) the band drifting on retest (non-uniform wire length or changed heat dissipation).
8. **L1 / L2 / L3 evidence**: L1 = one tier's fusing band measured and registered; L2 = the rating table (diameter → fusing band) on file; L3 = a recalibration record for every wire batch, consecutively on file.

#### 32.3.3 Rough Ground-Resistance Measurement (Three-Electrode Method, Field-Expedient)

Good grounding is decided not by "it is buried" but by "the resistance is small enough". In an age without an earth-resistance tester, use the **three-electrode voltage method for a rough value**:

1. Drive three identical iron rods into the soil: the electrode under test E, auxiliary electrode A (about 20 paces from E), auxiliary electrode B (about 40 paces from E; the three roughly in one line);
2. Battery current forms a loop via E→earth→A; an ammeter in series reads I;
3. A voltmeter (high-resistance comparison method) measures the voltage U between E–B (B sits far from the current path and serves as an approximately zero-potential reference);
4. Rough ground resistance R≈U/I.
   **Criterion (empirical value, must be calibrated)**: R at the ≤20 Ω class = pass. Over the limit, three remedies: deepen and thicken the electrode, charcoal-salt backfill (more contact), multiple electrodes in parallel (spacing ≥10 paces). Re-test after the rainy season (soil resistance changes with moisture).

[Card 32-03 Three-Electrode Rough Ground Test] (eight fields)

1. **Input materials**: 3 identical iron rods (electrode under test E, auxiliary A, auxiliary B); connecting wire (long enough for 40 paces); battery bank; charcoal-salt backfill (used when over the limit).
2. **Tools required**: hammer (driving the rods); pace counting (20 / 40 pace spacing, the Chapter 25 counting method); ammeter and moving-coil voltmeter (Section 31.6, cleared); meter-reading register. Pre-use calibration: meter zero and range cleared; all three rods identical and driven the same way; spacing verified by pacing.
3. **Operating sequence and control points**: (1) drive three identical iron rods — E; A about 20 paces from E; B about 40 paces from E, the three roughly in one line; (2) battery current loops E→earth→A, with an ammeter in series reading I; (3) a voltmeter reads the voltage U between E and B (B sits far from the current path and serves as an approximately zero-potential reference); (4) R≈U/I. Control points: the three rods must be identical and the spacings may never be shortened (too close = a low reading and a false pass); B must stay clear of the current path; re-test after every rainy season.
4. **Empirical parameters and calibration**: A about 20 paces and B about 40 paces from E; pass criterion R at the ≤20 Ω class (empirical values, to be calibrated to local conditions); dedicated lightning ground ≤10 Ω class; parallel electrodes spaced ≥10 paces. Soil resistance changes with moisture, so the before-and-after pair of rainy-season tests governs.
5. **Process observation and recording items**: test-point location and soil state (dry / wet / days since rain); the three spacings; the I and U readings; the computed R; comparison with the previous test; the remedy applied (deepen and thicken / charcoal-salt backfill / parallel electrodes).
6. **Pass / rework / scrap criteria**: pass = R at the ≤20 Ω class (lightning ground ≤10 Ω class). Rework = over the limit: the three remedies in order — deepen and thicken the electrode → charcoal-salt backfill → parallel electrodes (spacing ≥10 paces) — then retest. Scrap = the electrode is rusted through or cannot be pulled out (re-drive at a new spot nearby and register the old rod as abandoned).
7. **Common failures and troubleshooting order**: (1) R too high (dry soil or a shallow rod → backfill charcoal-salt, deepen); (2) retest values swinging (spacing too short, or B sitting on the current path → pull out to the 20 / 40 pace spacing and retest); (3) parallel electrodes bringing no improvement (spacing under 10 paces — the two fight over the same patch of soil); (4) back over the limit after the rains (the post-rain re-test was skipped — add it to the checklist).
8. **L1 / L2 / L3 evidence**: L1 = one three-electrode test record; L2 = the quarterly and post-rain re-test table; L3 = ground resistance and remedies entered in the inspection checklist, with the lightning ground registered separately and rust-inspected annually.

### 32.4 Batteries and Electrochemical Energy Storage

* The lead-acid battery (engineering description; the route depends on the Chapter 26 sulfuric acid scale-up): two lead plates in dilute sulfuric acid — when charged (from an external source) the anode turns brown (lead oxide) and the cathode becomes sponge lead; on discharge it converts back reversibly and delivers current; **charge/discharge cycling** = surplus waterwheel power charges it by day, lighting discharges it by night — the water-power plant's "daily-regulation battery";

* Fabrication points: lead grid plates (Chapter 17 casting/forging); many plates in parallel to enlarge capacity; separators (acid-soaked wood/fiberglass) against shorts; electrolyte concentration registered by density (the Chapter 26 density method) as a state-of-charge table;

* Maintenance: storage in a discharged state causes sulfation (plates whitening and hardening) — the number-one killer; **fully charge before taking out of service, top up monthly**;

* Honest boundary: lead-acid needs a stable supply of lead and sulfuric acid; the other route of bulk storage = elevated reservoir + waterwheel (Chapter 29); run both routes together as backups for each other.

### 32.5 The Basic Principle of the Electric Motor

* **The reversibility experiment**: wire the Chapter 31 generator to a battery as a motor — it spins (one machine, two identities; a fact recorded doubly in history and physics);

* The practical DC motor: field magnet (permanent or self-excited electromagnet) + rotor coil + commutator + carbon brushes (the whole Chapter 31 part family reused);

* **The starting-current problem**: a stationary rotor is nearly a short circuit; direct full-voltage starting draws several times the rated current (empirical value) — remove the starting resistor (water-resistor box or resistor-wire sections) step by step;

* Rough speed control: series-resistance speed regulation / field regulation (direction registered); application ranking: **water pumps and blowers (they tolerate fluctuation), machine tools (the electrification of the Chapter 20 line shaft begins: motor–belt–machine tool), lighting** — the power network extends from "shafts" to "wires," and the corners the line shaft cannot reach now have power (the Chapter 29 promise redeemed).

### 32.6 The Transformer and the AC Power System

* **The law of mutual induction, turned into a device**: one iron core (laminated, the Chapter 31 process) wound with two coils — the primary carries a **changing** current (AC), and a voltage is induced in the secondary; turns ratio = voltage ratio; **no moving parts, no sparks, isolation**;

* DC cannot use a transformer (constant flux induces nothing — the direct corollary of the Chapter 31 principles) → **the balance of long-distance transmission tips toward AC**;

* The AC generator: slip rings (two full rings, not a commutator) lead out the AC (a small modification of the Chapter 31 mechanism); the concept of frequency (cycles per second) registered from the waterwheel speed — **one unified frequency for the whole grid** is the Iron Law of interconnection (the first edition fixes one number, say the 50-cycle class, and the whole settlement obeys it);

* The route resolution (this settlement's engineering choice; the two systems coexist): electrolysis/electroplating/battery charging run on a dedicated DC line (the Chapter 31 DC machine); lighting and transmission run on AC + transformers — **this is the engineering resolution of the historical AC/DC war, not an ideological one**.

### 32.7 Voltage Drop, Line Loss, and Supply Distance

* The line-loss account (two lines of arithmetic): line resistance R=ρ×length/cross-section (ρ from the Chapter 30 reference table); loss power=I²R — **at the same delivered power, double the voltage, halve the current, and line loss falls to one quarter**;

* The voltage-drop check: the difference between voltmeter readings at the two ends of the line — when the end-of-line drop indoors exceeds one tenth, the lamps dim (empirical value, must be calibrated);

* The distance strategy table (engineering-handbook form):

| Distance | Plan |
| --- | --- |
| Same courtyard (within a hundred paces) | low-voltage DC/AC direct supply |
| Neighborhood (li class) | AC + overhead iron wire + moderate step-up |
| Across settlements (several li or more) | transformer step-up transmission, step-down at the receiving end (small current → fine wire also works; insulation strengthened for high voltage) |

* **The safety cost of stepping up**: the higher the voltage, the harsher the insulation demands (more skirts on the porcelain, larger clearances, taller poles); the work rules for jobs beneath high-voltage poles and near the lines are put in writing (the quantified version of the safety boundary).

### 32.8 From a Single Generator to a Small Power Network

The network-building checklist (execute in order):

1. Sources: one waterwheel-AC machine + one DC machine (or one dual-output unit); charge the lead-acid by day, discharge for lighting by night;
2. Trunk line: overhead iron wire + porcelain insulators; pole spacing registered so the sag touches no obstacle (pole erection, Chapter 13 water-and-wood work);
3. Distribution board: main switch + branch fuses + voltmeter and ammeter (the Chapter 27 instrument family goes on the wall);
4. Indoors: porcelain-cleat wiring + lamp sockets (carbon-filament lamps, from the Chapter 31 dim-everlasting-flame trial → this chapter's lighting installation) + switches that break the live wire;
5. The telegraph line (the engineering of the Chapter 30 sounder code): a single-wire earth-return circuit between settlements (grounding electrodes, Chapter 21) — **information and energy share the pole but not the wires**, and any interference declares itself at once;
6. The meter-reading regime: daily voltage/current/charge-discharge quantities entered into the Chapter 29 power ledger — electricity becomes an auditable resource.

[Card 32-04 Network-Building Checklist Execution] (eight fields)

1. **Input materials**: one waterwheel-AC machine + one DC machine (or a dual-output unit); overhead iron wire and umbrella-skirt porcelain insulators (wet-state re-verified); distribution board (main switch + branch fuses + voltmeter and ammeter); porcelain cleats, lamp sockets, carbon-filament lamps, switches (breaking the live wire); grounding electrode and charcoal-salt; single-wire telegraph gear; meter-reading register (the electric-power page of the power ledger).
2. **Tools required**: pole-erection and stringing tools (Chapter 13 water-and-wood work); the three-piece test kit (continuity tester, comparison voltmeter, spark test — for dry open wiring only); the three-electrode ground kit (Card 32-03); the three-check wiring acceptance sheet. Pre-use calibration: re-verify the porcelain's wet-state insulation by water-mist spray (the Section 32.2 galvanometer-in-series method); the fuse rating table on file (Card 32-01).
3. **Operating sequence and control points** (six steps, the order not to be reversed): (1) sources: one waterwheel-AC machine + one DC machine, charging the lead-acid by day and discharging for lighting by night; (2) trunk line: overhead iron wire + porcelain insulators, pole spacing registered pole by pole so the sag touches no obstacle; (3) distribution board: main switch + branch fuses + voltmeter and ammeter on the wall; (4) indoors: porcelain-cleat wiring + lamp sockets + switches breaking the live wire; (5) telegraph line: a single-wire earth-return circuit between settlements (information and energy share the pole, not the wires); (6) the meter-reading regime: daily voltage / current / charge-discharge quantities into the power ledger. Control points: no step begins before the previous one has passed acceptance; **an indoor line without a three-check acceptance sheet must not be switched on**.
4. **Empirical parameters and calibration**: pole spacing has no universal figure — register it pole by pole against "the sag touches no obstacle"; cleat spacing on straight runs ≤1.5 m; lamp to timber ≥300 mm and to flammables ≥500 mm; end-of-line drop ≤ one tenth; one unified frequency for the whole grid (the number fixed in the first edition); grounding per Card 32-03 and lightning protection per Card 32-07. These are empirical values, to be calibrated to local conditions.
5. **Process observation and recording items**: completion date and acceptor for each of the six steps; pole numbers and sag; the porcelain wet-state re-verification result; each branch's full-load current and the distribution board's temperature rise; end-of-line voltage drop; the telegraph test exchange; the daily meter readings.
6. **Pass / rework / scrap criteria**: pass = all six steps passed + end-of-line drop ≤ one tenth + every indoor line holding a three-check acceptance sheet + one week of complete meter readings. Rework = a step fails acceptance: rework that step on the spot; never carry a fault into the next step. Scrap = the trunk route is not viable (pole spacing and tree obstacles admit no answer) → reroute the whole run and register the old poles for removal.
7. **Common failures and troubleshooting order**: (1) lamps dim at the end of the line (drop over one tenth: wire too fine or distance too long → thicker wire or step up); (2) trips or tingling leakage on rainy days (wet-state insulation failure → change the insulators, add skirts); (3) fuses blowing repeatedly (line or load fault → drop loads section by section and trace; thickening the fuse to force power through is forbidden); (4) heavy telegraph noise (too near the power lines on the same pole → separate poles or change the wire position); (5) ground failure, tingling when touching an enclosure (three-electrode re-test → remove rust / backfill charcoal-salt / add electrodes).
8. **L1 / L2 / L3 evidence**: L1 = the three items in place: transformer step-up lighting a lamp, a motor driving a pump, the fuse table initially calibrated; L2 = one week of continuous operation with complete meter readings + telegraph exchanged between two settlements + end-of-line drop within standard; L3 = stock rotation of the four spares + weekly patrol and quarterly inspection executed + every indoor line holding a three-check acceptance sheet.

### 32.9 How to Repair and Test the Power System

* **The three-piece test kit**: a continuity tester (battery + galvanometer; finds broken wires), a comparison voltmeter (two meters read against each other; finds voltage drop), the spark test (strictly forbidden in damp or flammable-gas surroundings — only for rough checks of dry open wiring);

* The line-patrol regime: weekly patrol (porcelain cracks, wire sag, tree obstacles), quarterly inspection (joint resistance — the voltage-drop comparison method), special patrol after thunderstorms;

* **The electric-shock first-aid protocol (posted at every household)**: open the main switch or flick the wire away with a dry stick — never pull the person with bare hands; if breathing has stopped, give continuous artificial respiration (do not give up within the hour) — **knowing how to rescue ranks as high as knowing how to use electricity**;

* Spare-parts stock: fuses in every rating, porcelain insulators, lamps, carbon brushes, insulation wrapping tape — the power system's "medicine cabinet".

[Card 32-05 Electric-Shock First Aid] (eight fields)

1. **Input materials**: one dry wooden or bamboo pole (to flick the wire away); one dry wooden board (to stand on and to lay the casualty on); dry leather gloves (the low-voltage-tier substitute in an age without rubber); insulating wrapping tape; a door panel or stretcher; dry cloth. This card, together with the pole and the board, is posted and kept at every household and beside the distribution board.
2. **Tools required**: the main-switch handle with its two-sided "RUNNING / MAINTENANCE" tag; a voltage tester (numbered and entered in the register); a dry wooden standing board; a clean cloth (over the mouth for mouth-to-mouth). Pre-use calibration: **test the voltage tester once at a known live point before every use** — "the tester tests itself first"; a broken tester harms more than no tester.
3. **Operating sequence and control points**: **switch off or break contact with the source before touching the casualty; never pull the person directly.** (1) call for help and open the main switch (de-energizing: branch switches first, then the main switch; if the main switch is out of reach, flick the wire away with the dry wooden pole); (2) still verify dead after flicking it away (the tester having first been proved at a known live point); (3) drag the casualty clear of wet ground and lay the body flat on the dry board; (4) check consciousness and breathing: the moment breathing is judged absent, start mouth-to-mouth and keep it going without a break, not giving up within the hour; (5) one person rescues while another calls for help — resuscitation and transport run in parallel; (6) hang the "MAINTENANCE" tag and post someone to watch, so no one closes the switch. Control points: the first act before touching a casualty is always to switch off or break contact with the source; the rescuer stands on the dry board and wears dry leather gloves (low-voltage tier only); **outdoor work stops entirely during thunderstorms** and turns into the after-rain special patrol.
4. **Empirical parameters and calibration**: this card has no calibratable numeric parameter, only two time disciplines: start mouth-to-mouth the moment breathing is judged absent, and keep it up until breathing returns or a physician takes over, not giving up within the hour; post it at every household and drill it once a quarter. Dry leather gloves plus a dry wooden board are a substitute permitted only at the low-voltage tier; at the step-up tier the work insists on two people present and no one below the pole.
5. **Process observation and recording items**: date, time, and place of the incident; the means of de-energizing (main switch / pole); the tester result; the time consciousness and breathing returned; the start and stop times of artificial respiration and who gave it; where the casualty was sent. For drills, the participants, the timing, and the step-by-step check.
6. **Pass / rework / scrap criteria** (each item an executable action): pass = all four hold at once: (1) the main switch was opened, or the wire flicked away with the dry pole, before anyone touched the casualty; (2) after flicking it away the tester was proved at a known live point and then showed the casualty clear; (3) mouth-to-mouth began the moment breathing was judged absent and continued until breathing returned or a physician took over; (4) the "MAINTENANCE" tag is hung, someone is posted to watch, and no one closes the switch. Rework = any one of the four failed: do it on the spot at once and register it in the accident record — a verbal promise is not a remedy. Scrap = none. There is no "scrap" in rescue, only "not executed"; non-execution goes into the Chapter 25 accident record and is reviewed.
7. **Common failures and troubleshooting order**: (1) pulling the person bare-handed and shocking a second rescuer (the first prohibition — switch off first); (2) opening the switch but not testing for dead, so residual charge or backfeed strikes (test for dead right after breaking contact); (3) moving the casualty before resuscitating (resuscitate first, transport while resuscitating); (4) giving up partway (do not give up within the hour); (5) a bystander closing the switch (hang the "MAINTENANCE" tag and post a watcher); (6) attempting rescue outdoors during a thunderstorm (stop work; after-rain special patrol).
8. **L1 / L2 / L3 evidence**: L1 = the card posted at every household plus the dry pole and board kept beside the distribution board; L2 = the quarterly drill record (participants, timing, every action checked off); L3 = shock-incident records and reviews entered in the Chapter 25 accident regime, with four consecutive quarters of drill records on file.

***

### 32.10 The Distribution Board in Detail: Assembling Switches and Meters into One Board

The "distribution board" of the 32.8 checklist is refined here into a buildable drawing. The distribution board is the grid's "face and throat": who loses power first, who is supplying, how large the current is — one board shows it all.

* **Backboard and skeleton**: dry thick plank (thickness ≥25 mm, tung-oil or wax impregnated against damp — the Chapter 18 drying and impregnation methods), two horizontal battens added on the back against warping; board width set by the number of branches: reserve a vertical column about 150 mm wide per branch (empirical value; a 6-branch board comes out about 900 mm wide), with margins ≥100 mm top and bottom;

* **The bus bar (copper strip)**: incoming lines must not fly wildly onto the main switch's output terminals; first mount one copper-strip bus bar — **bus-bar cross-section ≥1.5× the trunk-line cross-section** (empirical value: the bus bar must carry the summed currents of all branches and dissipates heat poorly, so err thick rather than thin); drill the bus bar and clamp with bolts, at most two wire ends per bolt (copper washer + spring washer against loosening — loosened contact resistance is the top cause of distribution-board heating); with no copper strip available, twist a bundle of thick stranded copper wire as a substitute (same cross-section; the performance cost = messy routing and a temperature rise that must be watched even harder);

* **Branch layout**: every branch, top to bottom, in a fixed order "fuse holder → branch switch → output terminal"; leave ≥50 mm of air gap between adjacent branches (empirical value; on damp days, after re-verifying the insulation between branches with the 32.2 mist-spray method, this may be narrowed); the main switch holds one end of the bus bar alone, with ≥100 mm to the nearest branch;

* **Instrument face layout**: the master voltmeter and master ammeter sit side by side at the top center of the board face (read at a glance; the meter-reading sight line is never blocked — the "reading first" principle of the Chapter 27 instrument regime); an ammeter on every branch is too expensive and unnecessary — keep one portable ammeter and rotate it, and pre-install a pair of "measurement terminals" at every branch output: normally a copper strip shorts them and the board feeds normally; loosen it, insert the ammeter in series, and read (each measurement terminal carries a branch-number tag on both ends, so circuits cannot be crossed by mistake);

* **The three-level operating order (discipline)**: incoming line → main switch → bus bar → branch fuses → branch switches → loads. **Energizing: close the main switch first, then the branch switches; de-energizing: open the branch switches first, then the main switch** — opening the main switch under load is forbidden (a slow opening draws an arc and burns the knife; settled in 32.3); the main-switch handle wears a two-sided "RUNNING/MAINTENANCE" tag; during maintenance it must be flipped to the "MAINTENANCE" face;

* **Behind-board wiring and marking**: wiring behind the board runs square and true, fixed by a porcelain knob about every 200 mm (empirical value); every wire carries a branch-number tag at both ends (scribed or painted); one wiring diagram is mounted on the back of the board, **diagram and object identical** — the Chapter 22 "diagram and object share one number" regime copied over; joints behind the board are forbidden (joints live only on terminals).

[Card 32-06 Distribution Board Fabrication] (eight fields)

1. **Input materials**: dry plank ≥25 mm (width by branch count: a vertical column about 150 mm wide reserved per branch, so a 6-branch board comes out about 900 mm wide, with margins ≥100 mm top and bottom); copper-strip bus bar ×1; one main knife switch, one branch switch per branch; one fuse holder per branch; porcelain knobs ≥20; bolts, copper washers, and spring washers as needed; paint or scriber (marking). Prepare for one 6-branch standard board per run.
2. **Tools required**: hand-crank drill; micrometer (verify the bus bar and wire diameters, Chapter 22); moving-coil voltmeter/ammeter (Chapter 31; re-verify zero and cross-reading per the Chapter 27 release slips before mounting); plane and saw (board and battens). Pre-use calibration: both meters' zero and cross-reading re-verified; the bus-bar cross-section checked at 1.5× the trunk before cutting.
3. **Operating sequence and control points**: (1) lay out and scribe (three-level order in place: incoming line → main switch → bus bar → branch fuses → branch switches → loads); (2) mount the bus bar and switch holders (bus bar ≥1.5× the trunk cross-section); (3) run the behind-board wiring (square and true, a porcelain knob about every 200 mm); (4) clamp the connections (**≤2 wire ends per bolt; after tightening, a hand pull must not move them**); (5) mount the meters and measurement terminals (the master meters side by side at the top of the board face); (6) hang the branch-number tags (one at each end); (7) mount the wiring diagram on the back of the board. Control points: clamping torque and marking verified at every step; **no joints behind the board** (joints live only on terminals); the main-switch handle wears the two-sided "RUNNING / MAINTENANCE" tag.
4. **Empirical parameters and calibration**: bus-bar cross-section ≥1.5× the trunk cross-section (calibration: full load 1 h and the back-of-hand temperature test, the 32.3.1 red-line method); adjacent-branch gap ≥50 mm and the main switch ≥100 mm from the nearest branch (calibration: re-verify branch-to-branch insulation after misting); porcelain-knob spacing about 200 mm. These are empirical values, to be calibrated to local conditions (plank and load differences set the figures).
5. **Process observation and recording items**: each branch's full-load current; the temperature rise of the bus bar and of every joint (back-of-hand recorded in three grades "cool / warm / hot"); the count of sticky switch operations — entered on the electric-power page of the meter-reading register.
6. **Pass / rework / scrap criteria**: pass = full load 1 h with the bus bar and joints restable on the back of the hand + main and branch switches each worked five times with no sticking + a spot-check of three branches against the diagram all correct. Rework = one point running hot (open it and re-clamp; de-oxidize the wire ends, grease, and re-clamp). Scrap = the plank cracked, or still swelling with damp after wax impregnation (new board, start over).
7. **Common failures and troubleshooting order**: (1) one branch hot (first check loose clamping → then wire-end oxidation → finally that branch's wire diameter); (2) the whole board hot (first check the bus-bar cross-section → then a master overload); (3) a branch's meter reads nothing (first check that the measurement-terminal shorting strip was not left loose → then the meter's range).
8. **L1 / L2 / L3 evidence**: L1 = successful energization + one wiring diagram; L2 = full-load temperature-rise records; L3 = a record of one bolt re-tightening pass after a quarter of operation (re-tightening is a regime, not a feeling).

### 32.11 The Indoor Wiring Code

* **Porcelain-cleat wiring**: bare wire or waxed-cloth-covered wire fastened with two-hole porcelain cleats; cleat spacing on straight runs ≤1.5 m (empirical value: too sparse and the wire sags and sways, grinding its insulation against the wall); **corner practice**: at right-angle bends the wire turns through an arc (bend radius ≥10× wire diameter, so a hard kink never injures the conductor), and within 100 mm on both sides of every bend a cleat is mandatory (bends are stress-concentration points); where wires cross, wrap waxed cloth ≥50 mm overlapping on both sides of the crossing (the Chapter 31 taping method), or lift one wire on porcelain knobs so the two layers pass clear of each other;

* **Wall-penetration sleeves**: every wall penetration uses one whole porcelain tube, protruding ≥20 mm past the wall face at both ends; **no joints inside the wall hole or within the wall** — joints live forever in the open, where they can be inspected; outdoors the tube mouth bends downward about 20 mm, or the tube is mounted with its mouth sloping down (so rain cannot crawl along the tube and down the wall into the house — a mandatory clause for the rainforest/island editions);

* **Lamp hanging and heat clearance**: the lamp socket hangs on two suspension cords, the load carried by the hanging knot (the knot takes the load, never the terminal — a loaded terminal always loosens); **lamp-to-ceiling/timber distance ≥300 mm** (empirical value); calibration method: after 1 h lit at full voltage, the back of the hand can rest at 100 mm from the shade = pass; if it cannot, widen the distance or add an asbestos/ceramic shield (ceramic parts, Chapter 12); flammables such as mosquito nets and curtains keep ≥500 mm from lamps (a discipline value, not subject to calibration — fire does not rely on luck);

* **Switch-location discipline**: the switch sits on the door side, at about the 1 m level (register the local adult's elbow height); it must be wired in series on the "live" side (the 32.3 Iron Law); in two-wire systems enforce the "one color/number for the switch-side wire" regime; in wet zones (the splash range of the water vat and the stove) switches all move out of the wet zone, and wet-zone wiring gains porcelain-knob standoffs and reinforced waxed-cloth wrapping;

* **The wiring acceptance sheet (three checks; all must pass before energizing)**: first check, pull — every kind of fixing point (cleat, hanging knot, terminal) is hand-pulled for 30 s without coming off or shifting; second check, insulation — de-energized, the whole run is tested by the 32.2 galvanometer-in-series method, with a mist-spray re-verification on wet-zone segments; third check, points — lamp positions, switch positions, socket positions (if any) and numbering are checked point by point against the wiring diagram, diagram and object identical. The acceptance sheet is signed by two people and filed (the Chapter 29 archive section); **a line without an acceptance sheet must not be switched on**.

### 32.12 The Electrical Safety System: Grounding Grid, Lightning Protection, Tools, and Work Tickets

* **The grounding grid in detail**: the single-electrode ground (32.3.3) is only the starting point; a grid is a system — iron-rod electrodes **two or more in parallel, spacing ≥10 paces** (the 32.3.3 experience again: too close and the two electrodes "fight" over the same patch of soil, voiding the parallel gain); the parallel trunk uses copper wire, **cross-section ≥2× a single equipment grounding branch** (the trunk must carry the summed leakage current of several pieces of equipment at once); every metal-enclosed equipment item runs its **own** grounding wire to the trunk (daisy-chaining from end to end is forbidden — one break in mid-chain and every device downstream becomes "fake grounded", more deceptive than no ground at all); the grounding trunk runs exposed along the wall at about the 300 mm level, painted with wax-crayon color rings along its whole length as a marker, and rust-inspected and re-tested (three-electrode method) once before each rainy season;

* **The lightning rod**: an iron rod forged to a point at its tip, erected at the highest point diagonal to the protected object, **≥1.5 m above the protected object's top** (empirical value); **the empirical protection-angle rule**: the rotating cone with the rod tip as apex and a 45° angle to the vertical is treated as the protected zone (empirical value; to be re-assessed against real thunderstorm seasons); the down conductor uses trunk-grade iron wire, on the straightest path, clamped every 2 m, and **is strictly forbidden to share a pole or a trough with power or telegraph lines** (a lightning pulse will couple in and strike indoors — see the failure-mode table); where the down conductor enters the earth it bonds to the grounding grid, **its connection point ≥10 paces from the equipment grounding connection point** (so a strike's ground-potential surge cannot back-charge into the equipment ground);

* **The electrician-tool insulation regime**: every electrician's pliers and screwdriver wooden handle is wax-impregnated (the Chapter 31 wax-impregnation method) and re-impregnated once before each rainy season; voltage testers (the Chapter 30 testing tools or the neon-lamp class) are numbered and entered in the register, and **tested once at a known live point before every use** — "the tester tests itself first"; a broken tester harms more than no tester; in an age without rubber, insulating gloves are compensated by dry leather gloves + a dry wooden standing board, permitted only at the low-voltage tier (at the step-up tier the work insists on two people present + no one below the pole — see the safety boundary);

* **The emergency-repair work ticket (two-person system)**: any repair (even "only changing a fuse") is worked by a pair: one operates, one supervises; the ticket has five columns — "which branch is opened (branch number), voltage-tested or not, maintenance tag hung or not, what is repaired, restoration order"; the supervisor enforces **call-and-repeat**: the operator speaks each step aloud ("open branch 3's main switch"), the supervisor checks and answers ("correct, open branch 3") before hands may move; when the ticket is closed, both sign and it is filed. **All outdoor repair stops during thunderstorms** and turns into the after-rain special patrol (the 32.9 regime).

[Card 32-07 Lightning Rod Installation] (eight fields)

1. **Input materials**: iron rod ×1 (length ≥2 m, diameter ≥20 mm class, chosen to bear standing and hammering; a copper rod resists rust better but is expensive — follow the inventory); trunk-grade iron wire ≥10 m; clamps and insulators ≥6; charcoal-salt backfill (the same mix as 32.3.3).
2. **Tools required**: forge and hammer (Chapter 18, forging the tip); hand-crank drill; ladder or scaffolding + safety rope; the full three-electrode kit (Card 32-03). Pre-use calibration: after forging, the tip must be "pointed but not barbed" on sight; the three-electrode kit calibrated per Card 32-03.
3. **Operating sequence and control points**: (1) choose the spot (the highest point diagonal to the protected object, solid footing); (2) erect and fix the rod (guy lines tensioned in three directions); (3) forge the rod tip (**pointed but not barbed** — burrs cause corona loss and rust fast); (4) run the down conductor (the straightest path, a clamp every 2 m, spacing ≥1.5 m class from power and telegraph lines; sharing a pole or a trough is strictly forbidden); (5) backfill charcoal-salt at the ground, with the connection point ≥10 paces from the equipment grounding connection point; (6) re-test by the three-electrode method. Control points: **the down conductor continuous to the eye along its entire run, with no joints**; the tip ≥1.5 m above the top of the protected object.
4. **Empirical parameters and calibration**: ≥1.5 m above the top of the protected object; protection angle 45° cone (calibration: tally lightning-strike and damage points thunderstorm season by season — if damage turns up inside the cone for two consecutive seasons, narrow it to the 30° class, redraw the protected zone, and add rods); lightning ground ≤10 Ω class (twice as strict as the equipment ground's 20 Ω class). These are empirical values, to be calibrated to local conditions (re-assessed against thunderstorm experience).
5. **Process observation and recording items**: erection date; the ground re-test value; whether the protected-zone drawing is posted; a visual inspection after every thunderstorm (loose down-conductor clamps, rust points, a leaning rod) — entered in the "lightning-protection column" of the electric-power page of the meter-reading register.
6. **Pass / rework / scrap criteria**: pass = the down conductor continuous along its whole run + the ground re-test at the ≤10 Ω class + the protected-zone drawing posted in place. Rework = ground over the limit (deepen the electrode / add electrodes in parallel / re-drive at a damper soil spot). Scrap = a suspected hidden break in the down conductor that cannot be cleared clamp by clamp (re-run the whole conductor; patching a section is not allowed).
7. **Common failures and troubleshooting order**: (1) indoor equipment damaged after a storm (first check whether the down conductor runs alongside the signal lines → then whether its ground connection sits too near the equipment ground → finally whether the ground has rusted over the limit); (2) an abnormal hiss or glow halo at the tip (a burr → shut down and re-forge the point); (3) the down conductor heating and discoloring mid-run (induction from power lines too near → reroute).
8. **L1 / L2 / L3 evidence**: L1 = rod erected + the ground value record; L2 = a ledger of zero losses for one thunderstorm season; L3 = annual rust inspection + ground re-test on file three years running.

### 32.13 Metering Electric Quantity: The Electrolytic Coulometer and the "Electricity Account"

* **The principle (a direct extension of Chapter 26 electroplating)**: the mass deposited by electrolysis is proportional to the electric charge passed — connect **one "copper coulometer" in series in each household's indoor main** (a small electrolytic cell, two pure copper plates in copper sulfate solution); however much electricity flows through, the cathode gains exactly that much weight; it has no moving parts, does not wear, and when it fails it simply "stops with its reading in hand" — the electric-quantity meter best matched to this chapter's level;

* **The household adaptation**: a small cell at the ≤0.5 L class (empirical value: too large and the liquid resistance eats power, too small and it fills within a month); register the cathode plate's initial weight and wire it in; at each month's end, cut power and take out the plate → wash in clean water → air-dry → weigh on the balance (the Chapter 3 balance); **the grams gained are that month's electricity reading**; the reading is transcribed into the register, and the original plate goes back into service (a roughened plate surface does not affect the weighing, only the efficiency — see below);

* **Conversion calibration**: converting gained mass m (g) into electric quantity uses a local calibration — pass a known steady current I (meter reading) for a timed interval t, weigh the gain, and register \*\*"how many ampere-hours one gram of copper is worth in this cell"\*\* (copper has a theoretical electrochemical equivalent, but liquid temperature, concentration, and current density all eat efficiency; **the measured value governs**); re-check the efficiency once a month: a deposited copper surface gone dark, rough, or noduled = efficiency down and readings running high; change the solution or lower the current density and re-calibrate;

* **The maintenance discipline**: top up the electrolyte concentration monthly (copper sulfate + a little sulfuric acid, the Chapter 26 materials procedure); when the cathode blackens, swap in the spare plate (two plate sets rotate: one in the cell, one on the scale); guard the cell liquid against freezing in winter — if it freezes, metering stops; for the stopped interval, enter that electricity at the previous month's average and **honestly mark it "converted"** (silent estimation is forbidden — the Chapter 29 account discipline);

* **The "electricity account" enters Chapter 38**: each month, every household's weight-gain reading is transcribed onto the electric-power page of the power ledger (Chapter 29) and reconciled against the generation-side readings, forming a three-line "electricity account" — **generation, line loss (the generation reading minus the sum of the household readings), and household use**; line loss gains a number every month, and the theoretical account of 32.7 becomes an actual account; the accounting regime, billing, and quota rules are written up together in the Chapter 38 materials-and-energy ledger; this chapter delivers only one prerequisite: **the readings are trustworthy and re-testable**.

## Master Parameter Table

| Parameter | Value | Class |
| --- | --- | --- |
| Three wire-gauge tiers | fine 1–2 A / medium 5–10 A / coarse 15–30 A | empirical, field-calibrated |
| Iron-wire ampacity | about 1/2 of same-diameter copper | empirical |
| Conduit derating | six to seven tenths of bare wire | empirical |
| Temperature-rise red line | full load 1 h, restable on the back of the hand (≤50 ℃ class; 60 ℃ momentary touch only) | criterion |
| Fuse length | ≈5 cm, uniform | empirical |
| Fusing band | 5-min no-blow maximum ~ 10-s must-blow minimum | calibration method |
| Ground resistance | ≤20 Ω class; rough-measured by the three-electrode method | empirical criterion |
| Dry-state clearance | from ≥10× wire diameter | empirical |
| End-of-line voltage drop | ≤ one tenth | empirical criterion |
| Unified frequency | one number for the whole grid (tier fixed in the first edition) | Iron Law |
| Pole spacing and sag | touches no obstacle; registered pole by pole | regime |
| Bus-bar cross-section | ≥1.5× the trunk cross-section; ≤2 wire ends per bolt | empirical + discipline |
| Branch clearance | adjacent branches ≥50 mm; main switch ≥100 mm from the nearest branch | empirical |
| Cleat spacing | straight runs ≤1.5 m; one cleat within 100 mm on each side of bends | empirical |
| Lamp heat clearance | lamp to timber ≥300 mm; flammables ≥500 mm | empirical + discipline |
| Wall sleeves | whole tube, no joints; both ends ≥20 mm past the wall face; outdoor mouth sloping down | regime |
| Grounding grid | electrodes parallel at ≥10 paces; trunk cross-section ≥2× branch; a separate lead per equipment item | empirical + discipline |
| Protection angle | 45° cone (re-assessed each thunderstorm season; may narrow to the 30° class) | empirical, calibrated |
| Lightning ground | ≤10 Ω class; connection point ≥10 paces from the equipment ground | empirical criterion |
| Electric-quantity conversion | ampere-hours per gram of copper = local measured calibration; monthly efficiency re-check | calibration method |
| Monthly line-loss account | generation reading − sum of household readings, registered month by month | regime |

## Failure Modes and Diagnosis

| Symptom | Candidate causes (by probability) | Verification | Disposition |
| --- | --- | --- | --- |
| Fuse blows repeatedly | line short/load fault; fuse too fine | trace the line (drop loads section by section) | repair the fault; **thickening the fuse to force power through is forbidden** |
| Lamps dim at line end | drop over one tenth (wire too fine/distance too long) | read voltmeters at both ends | thicker wire/step up the voltage |
| Wire scalds the hand | overloaded beyond ampacity | check against the ampacity table | shed load or change to thicker wire |
| Trips/tingling leakage on rainy days | wet-state insulation failure | mist-spray re-test of the porcelain | change the insulator/add skirts |
| Lead-acid plates whiten | sulfation from storage in a discharged state | visual inspection | attempt rescue with a long low-current charge; regime: fully charge before taking out of service |
| Motor start blows the fuse | direct full-voltage starting | starting current several times rated | remove the starting resistor step by step |
| Heavy telegraph noise | interference from running too near the power lines | separate poles/change wire position | information and energy do not share a pole |
| Ground failure (tingle on touching the enclosure) | electrode rusted/soil dry | three-electrode re-test | remove rust/backfill charcoal-salt/add electrodes |
| Transformer secondary dead | the primary is carrying DC | check the nature of the source | AC only (a principle red line) |
| One point on the distribution board stays hot | bus bar/terminal bolt loosened; contact-resistance heating | de-energize and feel point by point; re-check temperature after re-tightening | re-clamp; de-oxidize and grease; make quarterly re-tightening a regime |
| Telegraph/instruments damaged in batches after storms | the lightning down conductor runs alongside signal lines, or its connection point sits too near the equipment ground | check the routing and the connection-point spacing | reroute the down conductor independently; separate the two connection points by ≥10 paces |
| Coulometer reading jumps between months | electrolyte concentration sagged/cathode roughened and noduled, efficiency down | compare against a standard cell in series; inspect the plate | change the solution, change the plate, and re-calibrate "ampere-hours per gram of copper" |

## Process Card Index

## Work Hours, Manpower, and Consumption

| Item | Manpower | Work hours (empirical) |
| --- | --- | --- |
| Three-tier fuse calibration | 2 people | 1 day |
| One round of ampacity calibration | 2 people | 1 day |
| 100 paces of overhead trunk (pole erection + stringing) | 4 people | 3–5 days |
| One lead-acid set (charge/discharge commissioning) | 2 people | 2 days |
| Three-electrode ground re-test | 2 people | half day |
| One distribution board (6-branch standard) | 2 people | 2–3 days |
| One lightning-rod set (grounding included) | 3 people | 2 days |
| Indoor wiring, one household (three-check acceptance included) | 2 people | 1–2 days |
| One copper coulometer (build + initial calibration) | 1 person | 1 day |
| Monthly metering and weighing, whole settlement | 2 people | half day/month |
| Weekly patrol | 2 people | half day/week |
| Consumption | fuses, porcelain, carbon brushes, lamps, wrapping tape | entered in the Chapter 38 ledger |

***

## A. Tools Already in Hand (partial)

Generator with DC/AC output (Chapter 31); wire drawing and enameled wire (Chapter 31); glazed pottery (Chapters 11–12); sulfuric acid and electroplating (Chapter 26); electric-bell contacts (Chapter 30); the instrument regime (Chapters 25, 27).

## B. New Tools Added in This Chapter

Three-wire-gauge standardization and the iron-wire overhead strategy; umbrella-skirt porcelain insulators and the wet-state re-verification method; knife switches/fuse rating tables/grounding electrodes; the lead-acid battery and the charge/discharge density table; the practical electric motor (starting resistor, rough speed control); the laminated transformer and the turns-ratio relation; AC slip rings and the unified-frequency Iron Law; the two-line line-loss arithmetic and the distance strategy table; the distribution board in detail (bus bar, three-level order, behind-board marking); the indoor wiring code and the three-check acceptance sheet; the grounding-grid parallel detail, the lightning-protection system (protection angle + down conductor + dedicated ground), the electrician-tool insulation regime and the emergency-repair work ticket; the copper-coulometer electric-quantity meter and the "electricity account" reading regime; the line-patrol regime and the electric-shock first-aid protocol.

## C. Unresolved Dependencies

* Precise metering of electric energy and mechanical work (the electric meter, long term);

* Systematic insulation design for high-voltage engineering (currently stops at the "moderate step-up" tier);

* The AC motor (the induction type — needs a more mature AC theory; registered as a next step).

## Safety Boundary

* Two red lines: copper wire must never substitute for a fuse; a fuse must never be thickened to force power through;

* High-voltage (step-up tier) lines: test for voltage before climbing, two people present, no one below the pole;

* Never touch switches with wet hands; wet-zone wiring in bathrooms/kitchens gains leakage clearance or an isolation transformer;

* The electric-shock first-aid protocol is drilled once every quarter.

## Acceptance Criteria

* **L1**: a transformer steps up and lights a secondary lamp (the registered turns ratio matches the measurement); a motor drives a pump; the fuse rating table's initial calibration complete.

* **L2**: the waterwheel-AC machine + lead-acid charge/discharge running continuously for one week with meter reading complete; telegraph short messages exchanged between two settlements; end-of-line voltage drop within standard.

* **L3**: stock rotation of the four spares — fuses/porcelain/carbon brushes/lamps; the line-patrol and quarterly-inspection regimes executed; electric-shock first-aid drill records on file; the grid entered into the power ledger as auditable infrastructure; every indoor line holds a three-check acceptance sheet, distribution-board quarterly re-tightening and monthly coulometer readings on file for three consecutive months, and the three lines of the "electricity account" (generation/line loss/household use) closed monthly and handed over to the Chapter 38 ledger regime.

## Next-Step Dependencies

* Chapter 33: stable power supply + vacuum + filament — the three prerequisites of the electro-vacuum device are in place as of this chapter;

* Chapter 36: the grid + batteries are the operating foundation of the electronics industry;

* The environment editions of Part 10: island salt-fog insulation re-verification, rainforest wet-state code, desert day-night charge/discharge cycling, permafrost low-temperature battery maintenance — the four editions each cite the matching clauses of this chapter.
