# Chapter 55: Wire Telegraph and Early Radio

## Chapter Objectives

Grow the component capabilities of Chapters 31–33 into the system capability of "getting information out the door": the **wire telegraph** (encoding, long-line driving, relay repeating, pole routes) lets settlements exchange confirmed messages same-day; **spark-gap radio telegraphy** (transmission, crystal-detector reception, antenna and ground system) provides the guaranteed floor for wireless-only stretches, the far banks of waterways, and line-broken disaster zones. This chapter delivers on the first edition's Chapter 33 promise — "the radio station is the common backbone of liaison and rescue in every environment edition" — and fills the missing communications hand-off layer between Chapter 33 (components) and Chapter 36 (the electronics industry).

Core idea: **the first bottleneck of communication is not the circuit, it is the procedure** — the code table, call signs, and the acknowledgment and verification systems decide the error rate first; the machine is only responsible for shaving a bit more off the errors beyond "human copying mistakes". The line-resistance account decides relay-station spacing; insulation leakage decides wet-season error rates; both accounts are laid open and computed in full in this chapter.

## Minimum Prerequisites

| Capability | Source |
|---|---|
| Electromagnets, bells and audible code reading, relays (pull-in/release registration) | Chapter 30 |
| Drawn iron and copper wire, enameled wire, moving-coil meter, hand-cranked generator | Chapter 31 |
| Umbrella-skirt porcelain insulators, three-pole method for ground electrodes, lightning protection system, line-patrol system | Chapter 32 |
| Crystal detector point selection and rectification ratio, LC resonance method, waxed-paper capacitors | Chapter 33 |
| Tin soldering, pole erection, ledger system | Chapters 17, 13, 43 |

## Capability Boundaries

**Can do:** the Morse code table and transmit/receive procedures (including local character-set trimming and Chinese numeric telecode transcription); 3.0 mm-class iron-wire single-wire earth-return trunk lines with relay stations placed by current budget (tens of kilometers scale); porcelain-insulator pole routes with wet-season leakage re-checks; spark-gap transmitters (a registered-grade band at working wavelengths of several hundred to 3000 m, frequency re-verified daily in wavelength terms); crystal detector receivers and homemade magnetic headphones; resonant wavemeters (LC + detector indication) — the verification tool for multi-station frequency fingerprints; station establishment (site, watch-keeping copy, time-window conventions, emergency power).

**Explicitly cannot do:** wireless voice and continuous-wave transmission (requires vacuum-tube amplification and oscillation; after Chapter 36); precise fault location on telegraph lines (only the sectional search method); prediction of radio propagation range (only measured "distance-condition" ledgers, no theoretical promises); long-term frequency stability (spark transmission frequency drifts with antenna sway and ground-system humidity — it can only be re-verified and registered day by day).

**External dependencies:** stable supply of iron/copper wire and enameled wire (Chapters 31–32); porcelain-insulator production capacity (Chapters 11–12); battery materials (zinc, copper, sulfuric acid, or lead-acid; Chapters 30, 32) — all three count as Class-C dependencies.

## Pre-Work Verification (check off one by one)

| # | Verification item | Criterion | Source |
|---|---|---|---|
| 1 | 2 sensitive relays | Registered on file per Card 30-06: pull-in current ≤20 mA, release ≥60% of pull-in, coil resistance measured and filed | Chapter 30 |
| 2 | Iron wire in three gauges | 2.5 / 3.0 / 4.0 mm diameter, each ≥3 km; per-kilometer resistance measured and registered (reference-table system) | Chapters 31–32 |
| 3 | A batch of porcelain insulators | Glaze intact (rings clear when tapped), wet-state re-inspection passed | Chapter 32 |
| 4 | ≥30 Daniell cells | Each cell's EMF and internal resistance registered per Card 30-02; series output ≥25 mA sustained for 30 min | Chapter 30 |
| 5 | 2 crystal detectors | Per Card 33-05, contacts with rectification ratio ≥10× class selected and locked; position sketches on file | Chapter 33 |
| 6 | Waxed-paper capacitors, 5 steps | Capacities registered by the comparison method; two units drawn at sample pass voltage withstand | Chapter 33 |
| 7 | Moving-coil meter and continuity tester | Release slips in date | Chapters 27, 31 |
| 8 | Copying logbook and master call-sign register | Logbook pages printed; master register opened and numbered | This chapter |

***

### 55.1 Codes and Procedures: Rules First, Then Wires

#### 55.1.1 The Timing Unit and the Full Morse Code Table

**Timing (settlement-wide standard, Iron Law)**: the "dot" is 1 time unit, dash = 3 units, pause within a character = 1 unit, gap between characters within a word = 3 units, gap between words = 7 units. Sending speed scales with "dot length" — shorten the dot and everything speeds up proportionally. **Whether dot length is stable directly decides the error rate**: if dots run long and short, the receiver swaps dots and dashes and characters go wrong. Criterion: any 10 consecutive dots must sound equal in length (◎ hand-feel; misjudgment compensation: re-verified by having a certified operator copy and cross-check — see the 55.1.4 assessment).

**Letter code table (the full international table, 26 letters)**:

| Letter | Code | Letter | Code | Letter | Code |
|---|---|---|---|---|---|
| A | ·− | B | −··· | C | −·−· |
| D | −·· | E | · | F | ··−· |
| G | −−· | H | ···· | I | ·· |
| J | ·−−− | K | −·− | L | ·−·· |
| M | −− | N | −· | O | −−− |
| P | ·−−· | Q | −−·− | R | ·−· |
| S | ··· | T | − | U | ··− |
| V | ···− | W | ·−− | X | −··− |
| Y | −·−− | Z | −−·· |  |  |

**Digit code table (10 digits — the foundation of the Chinese telecode book; these must be drilled first)**:

| Digit | Code | Digit | Code |
|---|---|---|---|
| 1 | ·−−−− | 6 | −···· |
| 2 | ··−−− | 7 | −−··· |
| 3 | ···−− | 8 | −−−·· |
| 4 | ····− | 9 | −−−−· |
| 5 | ····· | 0 | −−−−− |

**Local character-set trimming declaration**: all punctuation and Q-abbreviations of the international table are excluded. Only 6 procedural signs are adopted locally, identical at every station; private additions are not allowed:

| Sign | Meaning | Sending method |
|---|---|---|
| SOS | Rescue sign (highest priority) | ···−−−··· sent three times in a row, pause 1 min, send again, until a station answers |
| AR | End of this message | ·−·−· |
| AS | Please wait | ·−··· |
| RPT | Please repeat | letters R, P, T sent in sequence (·−· ·−−· −) + the group numbers of the range to repeat |
| Eight dots | Preceding transmission void | ········ then resend the correct content |
| AA | Word-group separator / decimal point | ·−·− |

#### 55.1.2 Handling Chinese Traffic: the Local Numeric Telecode Book

A telegraph key cannot send Chinese characters; the historically proven route is the **four-digit telecode book**: each Chinese character is encoded as four digits, and the digits then go out on Morse code. Our team compiles its own *Local Telecode Book*:

* 2000–3000 characters collected, ordered by their actual frequency of use in local documents; each character takes 4 mutually distinct digits (homophones must get different codes);
* three coding disciplines: (1) common characters get "handy codes" (dot-heavy codes are kept away from rare combinations); (2) no two characters' codes may be transpositions of each other (guards against swapped characters); (3) the telecode book is issued in numbered editions; a revision must be swapped network-wide in step, with the effective date announced;
* traffic drafting procedure: the drafter first writes the **numeric draft** from the telecode book, and the operator sends the digits — the operator need not read characters and is answerable only for the digits; the receiving side restores the text with the same edition of the telecode book. The numeric draft and the restored text are archived with the message.

#### 55.1.3 Transmit/Receive Procedure: Call Signs, Acknowledgment, Verification, Priority

* **Call signs**: two letters per station (the pinyin initials of the two characters of the station's name), registered in the *Master Call-Sign Register*; no duplicates anywhere in the network roll call; a call-sign change must be announced network-wide.
* **Calling format**: `BB BB BB DE AA K` — call the other party three times; after DE ("this is") send your own call sign; K (−·−) invites an answer. The receiving side answers: `AA DE BB AR`, and the message then follows.
* **Three header elements**: message number (this station's running serial, incremented by one per message), group count (every 5 characters = 1 group), priority (1 = rescue, 2 = urgent dispatch, 3 = routine). Example: `NR 7 · groups 20 · P1`.
* **Acknowledgment system**: on completing reception the receiver sends `R R R` (·−· three times) + message number + group count read back; only when the read-back matches the original may the sender strike the number. **Until R is received, the sender keeps the original and re-calls every 10 min.**
* **Verification system**: the receiver counts group by group; if the group count does not match, or three consecutive groups cannot be copied clearly, it sends `RPT + group-number range` to request a repeat of that range; **guessing characters or words is strictly forbidden** — a one-character difference is an accident in dispatching and rescue. Uncopyable characters are written down as "□"; leaving them blank is not allowed.
* **Priority (Iron Law)**: the P1 rescue sign may interrupt any traffic at any time — on hearing SOS every station immediately stops transmitting, keeps a listening watch throughout, copies word by word, and logs the times; the station nearest the incident responds per the emergency plan, and all other stations yield the channel. P2 urgent traffic may cut in after the current group finishes (before AR); P3 routine traffic queues by reserved time window.

#### 55.1.4 Operator Training: the Graded Words-per-Minute Assessment

Counting 5 characters as 1 word (consistent with the code-table convention), the pass criterion at every grade is the same: **copy 100 groups with ≤2 group errors** (accuracy ≥98%) to pass:

| Grade | Target speed | Content | Positioning |
|---|---|---|---|
| One | 5 words/min | digits 0–9 alone | trainee entry |
| Two | 10 words/min | digits + the 100 highest-frequency characters of the telecode book | journeyman for Chinese traffic |
| Three | 15 words/min | mixed letter+digit continuous traffic | **qualified operator (L2 operator criterion)** |
| Four | 20 words/min | copying under interference (adjacent station transmitting at the same time) | backbone / instructor |

Four training rules: (1) **write from the sound, no silent decoding** — write the sign the moment the sounder is heard, without looking up the code table in your head (30–60 min daily; instructor sends, trainee copies); (2) senders train in step, with even rhythm judged against the copier's accuracy; (3) assessment papers are composed and sent fresh by the instructor, and the paper is archived after the test; (4) **retraining system**: anyone who has been away from operating duty for 30 days is re-tested, and those who miss the grade go back to the bench — operating is a craft, and rust voids it. A station may only be commissioned with ≥2 certified operators on its roster (solo manning of a station is not allowed).

[Card 55-01 Morse Key and Sounder] (eight fields)

1. **Input materials**: contact blanks (cut from brass rod or old copper coins; contact face ≥5 mm diameter; silver points preferred if silver stock exists, roughly a tenfold-life class — register); spring steel strip (annealed and reshaped from old saw blades, 0.8–1.2 mm thick); 2 electromagnets (reuse the Chapter 30 bell component family; enameled wire 0.3–0.5 mm, each wound ≥800 turns); hardwood base ≥30 mm thick (tung-oil soaked, Chapter 18); pivot bolts and stop pins; waxed-cloth covered wire. One run produces a pair: one key + one sounder.
2. **Tools required**: bench vise and fine files (Chapter 20), tin-soldering kit (Chapter 17), feeler gauge, moving-coil meter (Chapter 31 — a >10% difference between the two coils' resistances in mutual comparison means suspected inter-turn shorting).
3. **Sequence and control points**: (1) anneal, shape, and harden the spring strip (Chapter 18; press 3 mm by hand and it must snap back crisply to pass); (2) mount the key lever on its pivot, turning freely with no play; **set the key-stroke travel at the 8–12 mm class** (too long slows the hand, too short sticks dots and dashes together); (3) solder the contacts on aligned, **gap 0.8–1.2 mm**; (4) electromagnet-to-armature gap adjustable at 1–2 mm; (5) fit the sounder's diaphragm and wooden cavity to fix the tone; (6) terminals and waxed-cloth wiring runs. Control points: contact alignment and gap, and stroke — verify at every step.
4. **Empirical parameters and calibration**: contact gap 0.8–1.2 mm (calibration: 100 dots in a row with no sticking and no tailing; compensate by listening on the sounder for whether "the dots are clean"); pull-in current registered by the same method as Card 30-06; sounder pitch auditioned at three armature-gap steps of 0.5/1/2 mm; adopt the step that "does not grate during long copying sessions" and **standardize it settlement-wide**.
5. **Observations to record**: contact-face color after 100 consecutive dots (slightly bright = good; blackened = oxidized, lap the points); the spring's snap-back sound; whether the armature picks up and drops crisply — into the component register.
6. **Pass / rework / scrap criteria**: pass = 1,000 key presses with no sticking + the sounder holds its pitch and does not heat through 30 min of continuous copying-listening; rework = contacts blackened (disassemble, lap, re-set the gap); scrap = spring cracked in quenching or base cracked.
7. **Common failures and diagnosis order**: dots sticking (spring pressure too high → gap too small → burrs on contact faces); dot tailing (armature gap too large → spring too soft); no sound or weak sound (inter-turn coil short → weak battery → gap too large).
8. **L1 / L2 / L3 evidence**: L1 keying produces sound that can be copied; L2 the thousand-press record and the 30 min continuous-listening record; L3 two pairs used interchangeably + cross-month life records filed in the register.

### 55.2 Wire Telegraph Engineering: the Resistance Account, Relaying, Pole Routes

#### 55.2.1 The Line-Resistance Account: Two Lines of Arithmetic for Relay Spacing

A telegraph line is not a power line: **the contest is not power, it is current**. Relay pull-in needs only a few tens of milliamperes, but the resistance of a long line eats it. The budget in three lines (all values defer to local measurement; table values are empirical starting points):

1. Line resistance R_line = ohms per km × km (3.0 mm iron wire ≈17 Ω/km, 4.0 mm ≈10 Ω/km, 2.5 mm ≈24 Ω/km — every batch of iron wire is measured and registered, method as in the Chapter 32 reference table);
2. Loop resistance R_loop = R_line + ground electrodes at both ends (each ≤20 Ω, three-pole method) + the relay coil (about 400 Ω in the sensitive winding, measured);
3. Current I = N·E ÷ (R_loop + N·r) — **battery internal resistance must not be ignored**: each Daniell cell has EMF E≈1.1 V and internal resistance r≈5 Ω (Card 30-02 registered values), so N cells in series have internal resistance N·r.

**Worked example (this chapter's standard trunk section)**: 30 km of 3.0 mm iron wire: R_line = 510 Ω; grounding 2×15 = 30 Ω; coil 400 Ω; R_loop = 940 Ω. Take N = 30 cells: I = 33 ÷ (940 + 150) = **30 mA**. If the relay pulls in at ≤20 mA, the margin is 1.5× — **design criterion: operating current ≥ 1.5× the pull-in current** (empirical margin factor; calibration method: measure with a meter in series along the whole line and read it directly with the key pressed).

**Quick cell-count estimate**: N ≈ R_loop ÷ 32 (an empirical coefficient derived from E−I·r≈0.95 V and I = 30 mA; re-verify and recompute with the registered E and r whenever the battery batch changes).

**Relay spacing table** (budget values for N = 30 cells and a sensitive relay of 400 Ω / 20 mA pull-in; **measured current on the actual line governs — table values are for scheduling only**):

| Wire gauge | Resistance per km (empirical) | Single-section limit without a relay | Recommended relay spacing (0.8× margin) |
|---|---|---|---|
| 4.0 mm iron wire | ≈10 Ω/km | ≈52 km | 40 km |
| 3.0 mm iron wire | ≈17 Ω/km | ≈30 km | 24 km |
| 2.5 mm iron wire | ≈24 Ω/km | ≈21 km | 16 km |

The purpose of the 0.8× margin: wet-season leakage and joint aging both eat current (next subsection) — a line budgeted right to the limit drops below the pull-in line as soon as the rains come.

#### 55.2.2 The Relay Repeater Station: Relaying Weak Current

The principle is Chapter 30's "a small current throwing a large one": **one relay per direction** — the A-side line feeds the coil of relay A (pull-in), and A's contacts switch the local battery through to drive the B-side line; B→A is symmetric. Watch monitoring: a sounder is bridged into the relay contact circuit so the station can hear what it forwards. **Manual bypass**: two hand keys run straight through to both lines — when automatic relay forwarding fails, the watch operator keys it through by hand (the one-beat keying delay is automatically tolerated by the receiving procedure: a wait between words is handled as AS). The station stands on two knife switches side by side: the **line knife switch** (puts the relay in or out of circuit) and the **grounding knife switch** (shorts both lines to ground during thunderstorms); a mechanical interlock is arranged; the thunderstorm procedure is in 55.2.5.

#### 55.2.3 Insulation and Leakage: the Telegraph Line's Real Enemy

Telegraph line voltage is only tens of volts; breakdown is not the danger — **leakage is**. Insulator leakage, trees touching the wire, damp pole bodies: all of them shunt signal current. Criteria and calibration:

* **Leakage-current criterion**: with the far end of the line open, read the leakage current on a meter in series at the near end; **< 1/10 of operating current** passes (empirical criterion; measure once after rain and once in the dry season, into the ledger);
* the small umbrella-skirt insulators of Chapter 32 are enough (low voltage, one grade down in spec), but the **wet-state re-inspection is carried out all the same** — leakage does not care how high the voltage is, only what the resistance is;
* pole route: thin wire, light insulators, pole spacing 40–60 paces, sag criteria as Chapter 32 (no touching obstacles; register pole by pole); with several pairs on one pole, **inter-pair spacing ≥300 mm class** (against wire contact and crosstalk); every 10 poles get a "test clamp" (a joint that can be opened) — the handle for sectional fault-finding;
* joint workmanship copies Chapter 32 (twisting + tin soldering + sheathing); the standing rule that joints are the leading cause of line faults does not change.

#### 55.2.4 Earth Return vs. Two-Wire: the Trade-Off

A single-wire earth return saves half the wire and half the insulators (the Chapter 32 networking list already fixed this system), at two costs: (1) ground resistance rises with dry season/frozen ground and the current drops a step; (2) where the corridor shares a right-of-way with power lines, stray currents intrude as noise. **Trade-off rule (apply in order)**: trunk lines default to single wire + earth return; if measured ground resistance exceeds the 30 Ω class (three-pole method), or the route runs parallel to power lines for more than 1 li, that section changes to two-wire; if dry-season ground re-measurement exceeds the limit, slow the sending temporarily (double the dot length) and register it, restoring on wet-season re-measurement.

#### 55.2.5 Lightning Protection: a Long Line Is a Lightning Rod

Tens of kilometers of overhead wire are the settlement's biggest collector of induced lightning; a pulse entering the station along the line will destroy relay coils and headphones and hurt people. The procedures follow the Chapter 32 lightning-protection system in full; this chapter adds three items:

* **Lightning spark gap**: where the line enters the station, ahead of the relay, a pair of brass points to ground, gap 0.3–0.5 mm (working voltage of the 30 V class is far below the breakdown value of about 1 kV — the 3 kV/mm empirical value reuses the Chapter 33 ball-gap calibration; a kilovolt-class lightning pulse jumps straight across the gap to ground). Disassemble and inspect after every thunderstorm: lightning-splashed metal lodged in the gap will conduct permanently and short the signal — clean out the spatter and re-set the distance;
* **grounding-knife-switch system**: before a thunderstorm arrives, open the line knife switches on both sides and close the grounding knife switches (lines shorted to ground); restore only after the rain stops and the line has been patrolled;
* telegraph lines are **strictly forbidden to run on the same poles as lightning down-conductors** (≥1.5 m spacing; Chapter 32 clause cited directly); every 5-km-class pole route must include one lightning rod with independent grounding, its connection point ≥10 paces from the station equipment ground point (same clause as Chapter 32).

[Card 55-02 Repeater Station] (eight fields)

1. **Input materials**: 2 sensitive relays (Card 30-06); ≥20 local Daniell cells (cell count per the 55.2.1 budget formula); 1 sounder; 2 line knife switches + 2 grounding knife switches (Chapter 32 knife-switch family); 1 lightning spark gap (brass point pair, disassemblable for spatter cleaning); small porcelain insulators and wall-entry porcelain tubes; one dry wooden-box station hut (waxed-cloth wiring runs). One run's quantity, stocked for one station.
2. **Tools required**: moving-coil meter and continuity tester (Chapters 27, 31), feeler gauge, the full three-pole method kit (Chapter 32, for ground re-measurement).
3. **Sequence and control points**: (1) entry order fixed, never reversed: **line → lightning gap → grounding knife switch → line knife switch → relay coil → ground**; (2) forwarding circuits: relay A contacts → local battery → B-side line; relay B contacts → the same battery set → A-side line; (3) sounder bridged in; (4) manual-bypass double keys; (5) measure both ground electrodes by the three-pole method and separate them by ≥10 paces. Control points: entry order, interlock arrangement, ground re-measurement.
4. **Empirical parameters and calibration**: end-to-end current margin ≥1.5× pull-in (measured over the full line: main-station key pressed, meter read in series at the repeater); leakage current < 1/10 of operating current (open-far-end method); lightning gap 0.3–0.5 mm (calibration: set the gap with a feeler gauge + re-measure after each thunderstorm season). Repeater spacing by wire gauge: 40/24/16 km for 4.0/3.0/2.5 mm wire (the 8/10 derated column); measured line current governs.
5. **Observations to record**: forwarding delay by ear (station sounder and forwarded signal nearly simultaneous = normal); contact spark size; post-rain margin re-measurement values — into the engineering column of the copying logbook.
6. **Pass / rework / scrap criteria**: pass = 100 groups forwarded in both directions with zero errors + margin still present after rain; rework = contact oxidation (lap the points, re-set the spring); scrap = relay coil burned open (rewind).
7. **Common failures and diagnosis order**: receives but does not send (local battery weak → contacts oxidized → spring pressure); two stations cross into each other (degraded grounds, common-ground crosstalk — separate the two stations' ground electrodes and re-measure).
8. **L1 / L2 / L3 evidence**: L1 one-way forwarding works; L2 ledger of 100 groups both ways with zero errors; L3 before/after-wet-season margin comparison + a 30-day unattended error logbook.

### 55.3 Spark-Gap Radio Telegraphy (Transmission): Throwing Current into the Air

> **Downgrade declaration**: the construction workmanship of this section is written at the third tier (reproducible by other hands with other materials); **propagation range and the antenna-wavelength relation are registration-grade data** — local terrain, ground-system humidity, day/night and season all eat range; they can only be accumulated in a "distance-condition" ledger, and the upgrade condition is measured tables across two consecutive seasons.

#### 55.3.1 Circuit and Construction: Spark Coil + Resonant Circuit + Antenna

The transmit chain has four stages, from low voltage to high:

1. **Power stage**: one lead-acid battery set (Chapter 32; a parallel Daniell bank may substitute — the performance cost is higher internal resistance, weaker spark, shorter range; measure and register). **The key keys only this low-voltage side** — the key opens and closes the primary in the low-voltage circuit, so the key contacts do not erode and the operator never touches high voltage; this is an Iron Law (a 0.1 µF-class waxed-paper capacitor + a hundred-ohm-class resistor wired across the key contacts as a spark-quenching circuit; the capacity is wound and registered per the Chapter 33 workmanship volume).
2. **Step-up stage**: one spark coil (Chapter 30 Card 30-04: primary of coarse wire with few turns + secondary of fine wire with thousands of turns + interrupter); the interrupter's vibration frequency is registered (tens of hertz class).
3. **Oscillation stage**: a Leyden jar bank of 2–4 jars in parallel (about 2–4 nF class, Chapter 30; per-jar capacity registered) ∥ an adjustable ball gap (brass balls ≥15 mm diameter, gap adjustable 0.5–1.5 mm), then in series the transmitting coil (air-core; enameled wire 1.5–2.0 mm, 60–120 turns, diameter 150–200 mm, 6 taps), connected to the antenna and ground system. **The secondary voltage charges the jars up to the ball-gap breakdown voltage (about 1.5–4.5 kV for a 0.5–1.5 mm gap, the 3 kV/mm empirical value); the moment the gap breaks down, jars + coil + antenna capacitance become one loop of damped oscillation — each break rings off a burst, the interrupter fires a few dozen times a second, and the energy is thrown onto the antenna one packet at a time.**
4. **Radiation stage**: electromagnetic waves radiate between the antenna (flat-top 20–60 m + down-lead) and the ground system.

**Order-of-magnitude sanity check (numeric discipline)**: energy per break ≈ ½CV² = ½ × 2 nF × (3 kV)² ≈ 9 mJ; at an interrupter rate of 30 Hz the RF power is about the 0.3 W class — the same order as the early historical spark stations; with a good antenna and a quiet receiver, the 3 km class is reachable (registration-grade; see 55.3.3). Counting on "tens of kilometers" is a dishonest target — file the station at 3 km first.

#### 55.3.2 Antenna, Ground System, and Wavelength: Field Rules (registration-grade)

* **Antenna capacitance**: a long-wire antenna's capacitance to ground is about 5–8 pF/m (empirical, registration-grade) — a 40 m flat-top with its down-lead is about the 300 pF class; the longer the flat-top, the bigger the capacitance.
* **Wavelength-component relation**: λ(m) = 1885 × √(L(H) × C(F)). Example: L = 0.5 mH, C = 2 nF → λ ≈ 1885 m (about 160 kHz). **Field mnemonic**: coil tap moved up (more inductance) lengthens the wavelength; flat-top lengthened (more capacitance) lengthens the wavelength; one more Leyden jar in parallel lengthens the wavelength. All three are registration-grade relations — **the same antenna loosened by today's wind, the ground system soaked by tomorrow's rain, and the wavelength drifts**; hence re-verify daily with the wavemeter (next item).
* **Wavemeter (this chapter's key verification tool)**: a waxed-paper capacitor of known capacity (registered value) + a tapped coil + a crystal detector + a moving-coil meter, wired into a resonance indicator; couple it inductively 1–2 m from the transmitting coil and try the taps one step at a time — **the step with the biggest meter deflection is the transmitted wavelength** — read it off the local L-C-wavelength reference table. Keep one at the transmit end and one at the receive end; the "frequency fingerprints" of multiple stations are arbitrated entirely by this instrument.
* **Ground system**: 2–3 iron-rod ground electrodes in parallel (electrode spacing ≥10 paces, Chapter 32) + one buried ring of bare iron wire (radius 2–3 m, buried 0.3–0.5 m deep); ≤20 Ω class by the three-pole method. The RF ground and the power ground are two different things: **drive the transmitting ground system separately; do not share an access point with the station's power ground** (it keeps keying pulses out of the station equipment).
* An honest account of antenna materials: iron wire loses heavily at high frequency (registration-grade); **for transmit and receive antennas, copper wire first when copper is available**; estimate the reachable range on iron wire at 0.6–0.7× and note it in the ledger.
* Antenna masts: 6–10 m tall, two to three masts (Chapter 13 pole erection); **every guy wire carries an insulator spliced into its middle as an insulated section (≥0.5 m)** — a closed guy loop eats radiation and invites lightning; the flat-top and down-lead enter the building fixed on insulators.

#### 55.3.3 Keying and Operating Procedure

* Power-on sequence: connect the antenna → set the ball gap with the feeler gauge → close the low-voltage switch → **short-key test fire** (one dot; listen to the interrupter, watch the gap fire) → wavemeter verifies the wavelength falls inside this station's agreed band → begin sending. Power-off is the reverse; **after cutting power, discharge the Leyden jars with the discharge rod before touching anything** (Chapter 33 safety clauses apply directly).
* Ball-gap adjustment is only allowed with power off: a bigger gap means higher breakdown voltage, more energy per break, a "heavier" sound — but it strains the jars and the coil. **Within 0.5–1.5 mm, register the copyable range at each step**, and choose the margin step, not the limit step.
* Range-trial procedure: two stations open up stepwise at 0.5/1/2/3/5 km; at each step, copy 20 groups each by day and by night, in rain and in clear weather, recording errors. The **"copyable range" table goes into the ledger** — this is how L2 "3-km-class reception" is evidenced, and it is the chapter's most honest promise: **the 3 km class is an empirical value governed by the local ledger; no universal guarantee is made.**

[Card 55-03 Spark-Gap Transmitter] (eight fields)

1. **Input materials**: lead-acid battery set (Chapter 32) or a parallel Daniell bank; 1 spark coil (Card 30-04); 2–4 Leyden jars (per-jar capacity registered); 2 brass balls (≥15 mm diameter, turned or cast then filed smooth); enameled wire 1.5–2.0 mm, about 50–80 m in total (transmitting coil); copper tap strips, porcelain supports, wooden baseboard (wax-soaked), hand key (Card 55-01), spark-quench capacitor and resistor. One run's quantity, stocked for one transmitter.
2. **Tools required**: feeler gauge (ball gap), discharge rod (insulated handle + ground hook, homemade), one wavemeter (55.3.2), moving-coil meter (inter-turn check of the coil — stepwise resistance comparison between taps).
3. **Sequence and control points**: (1) baseboard laid out in four separated zones (power / step-up / oscillation / antenna terminals — high-voltage and low-voltage zones ≥200 mm apart); (2) wind the transmitting coil without overlapping turns, leads brought out as each tap is wound; (3) mount the ball gap on porcelain supports, gap faces parallel and aligned; (4) **keying only on the low-voltage side**, with the spark-quench circuit in parallel across the contacts; (5) hang the discharge rod on the wall; (6) test-fire and register step by step. Control points: **adjust the gap with power off, discharge before touching, verify with the wavemeter**.
4. **Empirical parameters and calibration**: ball gap 0.5–1.5 mm (feeler gauge sets the gap; calibration: test-fire at each step, read the wavelength on the wavemeter + 20 groups of errors at the receive end, register as a three-column "gap-wavelength-range" table); the number of Leyden jars in parallel is back-derived from the wavelength (adjusted by wavemeter measurement); interrupter vibration frequency registered (count the breakings per 10 s by ear). The transmit band is the 500–3000 m class, re-checked daily with the wavemeter; energy per spark ≈9 mJ, RF power ≈0.3 W (order-of-magnitude check only, no range promise).
5. **Observations to record**: gap-fire color and length (a short orange-white beam is normal; violet-red scattering = jars damp or gap faces oxidized); no noise inside the jars; the delay from key press to start of oscillation — into the transmission log.
6. **Pass / rework / scrap criteria**: pass = wavemeter confirms the agreed band + 20 groups at 3-km-class between two stations with errors ≤10% + 100 keyings with no contact sticking; rework = wavelength drifted out of band (adjust the taps and re-verify); scrap = Leyden jar punctured with white tracks or coil inter-turn short (replace the part and rewind).
7. **Common failures and diagnosis order**: no spark (primary circuit open → interrupter not vibrating — listen → secondary open); spark but nothing received (ball gap too big: fires but does not oscillate → jar punctured, capacity lost → coil inter-turn short); wavelength drift (antenna swaying → ground-system humidity → jars heating).
8. **L1 / L2 / L3 evidence**: L1 spark produced + wavemeter reads; L2 the three-column calibration table + the 3-km-class trial record; L3 a cross-season distance-condition ledger + jar/gap maintenance-cycle records.

### 55.4 Crystal Detector Receiver: the Unplugged Ear

#### 55.4.1 The Detector: Reusing the Section 33.8 Point-Selection Workmanship Outright

The crystal detector **starts no new workmanship** — the point-selection flow of Chapter 33's Card 33-05 is reused whole: knock a fresh cleavage face, fine-grind off the oxide film, touch-test point by point with the spring wire, select a point that is "big forward, small reverse, steady reading", lock it with the fine-pitch screw, and file the position sketch into the component register. This chapter adds three station-post disciplines:

1. **Vibration protection**: mount the detector on a cork-padded stand (table vibration shifts the point at once); no elbows on the table during watch;
2. **Backup points**: every detector gets at least two spare points selected and sketched — if the point drifts during watch, switch points and resume the listening watch within 30 seconds;
3. **Life registration**: re-measure the rectification ratio once a week; when it falls to half the initial value, re-select the point or change the mineral sample (same method as Card 33-05).

#### 55.4.2 The Tuning Circuit: Coarse Taps + Fine Capacitor Steps

* **Tuning coil**: wind enameled wire 0.5–0.8 mm, 150–300 turns in total, on a ceramic tube or wax-soaked paper tube (diameter 80–120 mm), with 8–10 taps (brought out at 20–30-turn increments from the grounded end); connection: antenna to the tap, coil bottom to ground — **the antenna capacitance plus the inductance of the turns in use is the resonant circuit**; tap up = more inductance, longer wavelength (the same mnemonic as 55.3.2).
* **Capacitor bank**: 5 steps of waxed-paper capacitors (about the 0.1/0.2/0.5/1/2 nF class; each unit's capacity registered), switched with small knife switches, wired in parallel between the detector input and ground for fine tuning.
* **Tuning operation**: first turn the tap (near the step where the signal jumps sharply), then step the capacitors to find the peak — **selectivity criterion: one capacitor step off, the signal weakens noticeably**. If stepping off does not weaken it, the peak is too broad; reduce the tap turns or reduce the parallel capacitance to improve it (registration-grade).
* Circuit order: antenna → tap → detector → headphones → ground. The detector contact position also gets fine adjustment (changing which tap it hangs on) — a crystal set's "tuning" is the cooperation of tap, capacitor, and contact, all of it field-method registration-grade.

#### 55.4.3 Homemade Magnetic Headphones: Permanent-Magnet Bias + Fine-Wire Coils

* **Structure**: two coils wound on soft-iron pole shoes (shoe faces curved into an arc); a thin arc-shaped iron diaphragm (0.3–0.5 mm thick, about 40 mm diameter, arc domed at the center) suspended **0.5–1 mm** in front of the shoes; **one permanent magnet fixed to the back of the pole shoes as bias** — made by the Chapter 30 magnetizing workmanship (steel-needle magnetizing method). Bias is the key to sensitivity: once the diaphragm is pulled bent toward the permanent magnet, tiny changes in the signal current can push it into vibration; without bias it is nearly silent (usable as a registered controlled experiment).
* **Coil specification**: enameled wire 0.10–0.15 mm, ≥5,000 turns per coil, the two coils in series, DC resistance ≥800 Ω class in total (turns counted on the winding machine, Chapter 20; resistance measured and registered) — more turns, more sensitivity, but take the grade that fits the enameled-wire labor budget.
* **Ear shells**: turned hardwood or ceramic (Chapter 11), leaving a resonance cavity about 10 mm deep behind the diaphragm; two shells, one per ear, joined by a headband of wax-soaked leather.
* **Acceptance criteria**: touch the headphone leads intermittently across a battery — the click is clear and identical in both ears; on the crystal set, the weak induced signal of the local buzzer through one wall is audible (sensitivity compensation test).

#### 55.4.4 Antenna-Ground Installation and Receive-End Discipline

* The receive antenna may be shorter than the transmit antenna: flat-top 20–40 m, height 6–10 m; all other rules as in 55.3.2 (insulator spliced into the guys, down-lead entering the house on insulators); ground system the same design (three-pole method ≤20 Ω).
* Three receive-end disciplines: (1) **keep your distance from the transmit antenna** (same pole or same courtyard means certain crosstalk — while the transmitter sends, the receiver goes deaf; keep the two antenna sets ≥30 m class apart and run their directions perpendicular wherever possible); (2) before a thunderstorm, close the antenna grounding knife switch (as in 55.2.5); (3) the antenna lead-in passes through the wall in one unbroken porcelain tube (the Chapter 32 wall-penetration clause applies).

[Card 55-04 Crystal Receiver] (eight fields)

1. **Input materials**: 2 pieces of galena (point selection passed per Card 33-05); tuning-coil stock (ceramic tube + enameled wire 0.5–0.8 mm, about 60–100 m); 5 steps of waxed-paper capacitors (capacities registered); 5 small knife switches; spring wire (fine phosphor bronze / steel wire) and fine-pitch screw (Chapter 27); one pair of headphones (55.4.3 specification); porcelain insulators, grounding materials (iron rods + charcoal and salt, Chapter 32). One run's quantity, stocked for one receiver and one pair of headphones. Receiving antenna: top wire 20–40 m, height 6–10 m (55.4.4), with an insulator in the middle of each guy.
2. **Tools required**: winding machine (Chapter 20), moving-coil meter (registered re-measurement of coils and capacitors), feeler gauge (diaphragm distance), three-pole method (ground system).
3. **Sequence and control points**: (1) wind the coil with taps brought out as wound, register the resistance steps; (2) select and lock the detector point per Card 33-05 + anti-vibration pad; (3) wind the headphones — **no overlapping turns, waxed-paper insulation between layers**, diaphragm distance set with the feeler gauge; (4) after wiring the set, test-listen first with the local buzzer behind an induction coil as the "demonstration signal source"; (5) calibrate and register the three-way tuning cooperation (tap / capacitor / contact). Control points: point-selection lock and vibration protection, diaphragm distance, inter-turn insulation.
4. **Empirical parameters and calibration**: rectification ratio ≥10× class (weekly re-measurement by the Card 33-05 method); diaphragm distance 0.5–1 mm (calibration: touch across the battery and take the setting with the loudest click); a tap-capacitor-step vs. wavemeter-reading reference table registered for every set (this is the set's "frequency fingerprint").
5. **Observations to record**: point-stability duration (first lock to first drift); peak width (off-step attenuation by ear, three grades: sharp / gradual / flat); headphone left-right symmetry — into the component register.
6. **Pass / rework / scrap criteria**: pass = demonstration signal copyable + selectivity criterion passed + headphones worn 30 min without heating; rework = point drift (switch to a backup point and re-select); scrap = coil inter-turn short (rewind) or deformed diaphragm (replace it).
7. **Common failures and diagnosis order**: the whole set is silent (antenna/ground continuity → detector point lost → headphone coil open — check in order with the continuity tester); receives but stations bleed together (peak too broad → too many tap turns → capacitor step too large); sound comes and goes (contact vibrating → oxidizing → mineral degrading).
8. **L1 / L2 / L3 evidence**: L1 local demonstration signal audible; L2 tuning reference table + selectivity record + one long-range reception registered; L3 cross-season reception ledger + detector weekly-inspection records.

### 55.5 Station Establishment: Site, People, Time Windows

* **Four site-selection rules**: (1) high, dry, flood-free (ground-system efficiency and equipment life); (2) far from power lines and iron workshops (stray current and vibration noise), ≥100 paces class; (3) no tall trees or unsafe poles around a wireless antenna (wind-throw crushing the line); transmit and receive antennas ≥30 m class apart and cross-perpendicular in orientation; (4) near the office watch post and reachable by road (emergency repair and message delivery).
* **Watch and copying system**: two-person watch (one copies, one verifies and registers); the *Copying Logbook* has fixed columns: date / time window / call sign / message number / group count / errors and RPT records / dual operator signatures; every message is archived (original + numeric draft + restored text in the same dossier; Chapter 43 ledger system); **three checks at equipment handover** (continuity-test the lines, test the key and listen to the sounder, match the frequency fingerprints on the wavemeter).
* **Frequency / time-window conventions (so multiple stations do not interfere)**: (1) **frequency fingerprint** — every station's tap step + capacitor step + antenna geometry registered into the master register; adjacent stations offset by at least one step; changing any one item requires a network-wide announcement and re-registration; (2) **time-window system** — three windows daily (morning/noon/evening, 15 min each; local time set by the Chapter 25 time standard) for a network-wide centralized roll call: within a window each station, in master-register order, sends 2 min of roll call and urgent items; other routine traffic goes point-to-point by appointment at staggered times; (3) **wavemeter arbitration** — when two stations interfere, measure each with the wavemeter; whoever drifted, changes; (4) rescue signals are not bound by time windows (the 55.1.3 Iron Law).
* **Emergency power**: the wire-traffic batteries (Daniell) are fully independent of the grid — a grid outage does not touch the telegraph (Chapter 31/32 hand-cranked generators and lead-acid serve as charging backup and transmit power); the wireless transmitter battery is a dedicated set; transmission hours and battery electrolyte consumption are entered in the Chapter 38 accounts; **every station always keeps one battery set of spares on hand**, and voltage is checked at shift handover (comparison method, Chapter 27).

## Master Parameter Table

| Parameter | Value | Class |
|---|---|---|
| Line resistance (iron wire) | 4.0/3.0/2.5 mm ≈10/17/24 Ω/km | empirical; measured and registered per batch |
| Current margin criterion | operating current ≥ 1.5× pull-in current | design criterion |
| Sensitive relay | pull-in ≤20 mA, coil ≈400 Ω, release ≥60% of pull-in | empirical (Card 30-06) |
| Daniell cell | E≈1.1 V, r≈5 Ω per cell; quick cell count N ≈ R_loop ÷ 32 | empirical; re-verified per Card 30-02 |
| Relay spacing | 4.0/3.0/2.5 mm wire: 40/24/16 km (0.8× step) | budget values; measured line current governs |
| Leakage-current criterion | < 1/10 of operating current (open-far-end method; measured in wet and dry seasons) | empirical criterion |
| Inter-pair wire spacing | ≥300 mm class on shared poles; one test clamp per 10 poles | procedure |
| Lightning spark gap | 0.3–0.5 mm, ahead of the station-entry relay; clean spatter and re-set after thunderstorms | empirical + procedure |
| Grounding | ≤20–30 Ω at each end (three-pole method); stations' ground electrodes ≥10 paces apart | criterion |
| Ball gap (transmit) | 0.5–1.5 mm (about 1.5–4.5 kV; 3 kV/mm) | empirical; registered per step |
| Leyden jar bank | 2–4 jars in parallel ≈2–4 nF; energy per break ≈9 mJ class | empirical; registered |
| RF power order | ≈0.3 W class (estimated at 30 Hz interrupter rate) | order-of-magnitude check |
| Wavelength formula | λ(m) = 1885 × √(L·C); antenna capacitance ≈5–8 pF/m | registration-grade |
| Transmit wavelength band | 500–3000 m class; re-verified daily with the wavemeter | convention |
| Antenna | flat-top 20–60 m, height 6–10 m; insulator ≥0.5 m spliced mid-guy | procedure |
| Iron-wire antenna derating | estimate reachable range at 0.6–0.7× | registration-grade |
| Tuning coil | 150–300 turns, 8–10 taps; 5 capacitor steps for fine tuning | design |
| Headphones | 0.10–0.15 mm wire, ≥5,000 turns per coil, two in series ≥800 Ω; diaphragm distance 0.5–1 mm | empirical; registered |
| Rectification ratio | select points at ≥10× class; weekly check — re-select at half value | criterion (Card 33-05) |
| Timing | dot 1, dash 3, intra-character pause 1, inter-character 3, inter-word 7 | Iron Law |
| Operator grading | 15 words/min, 100 groups with ≤2 group errors = qualified operator | criterion |
| Time windows | three daily windows of 15 min each, 2 min roll call apiece; SOS unrestricted | convention |
| TX/RX antenna separation | ≥30 m class, orientations perpendicular | empirical |

## Failure Modes and Diagnosis

| Symptom | Candidate causes (by probability) | Verification | Action |
|---|---|---|---|
| Whole line silent (wire) | broken wire; oxidized joints; battery exhausted; key contacts oxidized | sectional current tests with a series meter at the test clamps | repair section by section; lap the points; change battery |
| Error rate surges in wet weather | insulators leaking when wet; damp pole bodies shunting; degraded grounding | open-far-end leakage-current test | replace insulators / add skirts; re-measure grounding; slow the sending and register |
| Repeater not forwarding / half forwarding | local battery weak; contacts oxidized and sticking; spring loose | series meter on the forwarding current; flick the armature by hand | change battery; lap points and re-set spring |
| Crosstalk from the adjacent line (another line's code dots mixed into the message) | pairs too close on shared poles; running parallel to power lines | open this line and measure induced current | open inter-pair spacing ≥300 mm; reroute or switch to two-wire |
| Transmitter gives no spark | primary circuit open; interrupter not vibrating; secondary wire broken | listen to the interrupter; sectional continuity checks | repair the primary; lap the interrupter contacts; re-solder the secondary |
| Spark but nothing received | ball gap too big — fires but does not oscillate; Leyden jar punctured, capacity lost; coil inter-turn short | wavemeter sweep shows no peak; compare with jars disconnected | adjust the gap; change the jars; change the coil |
| No tuning peak at the receiver | antenna broken; ground system rusted; taps oxidized | sectional continuity checks | reconnect antenna; replace ground electrodes; sand taps bright |
| Sound comes and goes | detector point drifting (vibration / oxidation / degrading mineral) | re-measure rectification ratio | switch to backup point; anti-vibration pad; change mineral sample |
| Two stations interfere | frequency fingerprints too close; time windows overlapping | wavemeter measurement of both stations | widen the tap-step separation; stagger the time windows; re-register in the master register |
| Headphones weak | diaphragm too far; permanent magnet demagnetized; coil inter-turn short; poor detector point | compare with another headphone; tap the magnet and test its pull | adjust diaphragm distance; re-magnetize; rewind; re-select the point |
| Key sticking / burning | spring pressure too low; no spark-quench capacitor | inspect contact faces; check the capacitor is present | lap points and adjust spring; add the spark-quench circuit |
| Whole station dead after lightning | lightning gap bridged by spatter, permanently conducting (signal shorted); relay coil burned open | disassemble and inspect the gap; coil continuity test | clean spatter and re-set distance; rewind coil; full-line retest before restoring |

## Process Card Index

## Acceptance Criteria

* **L1**: key and sounder usable as a pair; full dictation correct on the 36-character code table; a single station's key controls relay pull-in and release; the transmitter gives spark and the wavemeter reads; the crystal set is audible and copyable on the local demonstration signal.

* **L2**: **two-point wire traffic (including 1 repeater station), 100 groups with an error rate <2%**; full-line current margin measured ≥1.5×, and leakage current < 1/10 of operating current, both on file; **wireless 3-km-class reception achieved and registered (an empirical value — range floats with day/night, weather, and season; the local "distance-condition" ledger governs; no universal promise)**; the transmit wavelength verified by wavemeter to fall in the agreed band; ≥2 operators passing the "15 words/min, errors ≤2%" grade; one post-rain re-measurement of pole-route leakage current on file.

* **L3**: a 30-day continuous unattended error logbook from the repeater station on file; the wireless "distance-condition" table accumulated across two seasons; spare-parts rotation (contact blanks, detector mineral, Leyden jars, spark gaps, fuse-grade wire lengths); telecode book, master call-sign register, and copying logbook archived and handed over to the ledger system (Chapter 43); the training system producing the next batch of ≥2 operators (succession criterion); the before/after-wet-season comparison report on margin and leakage completed.

## Labor Hours, Manpower, and Consumption

| Item | Manpower | Hours (empirical) |
|---|---|---|
| One key-and-sounder pair | 2 people | 2 days |
| Sensitive relay installation and registration | 1 person | 1 day per unit |
| Main-station installation (key, sounder, lightning protection, double knife switches, wiring) | 2 people | 2 days |
| One repeater station (including simple hut) | 3 people | 3–4 days |
| Pole route per 100 paces (erect poles + string wire + insulators + grounding) | 4 people | 3–4 days (lighter than power lines) |
| 5 km trunk line, total | 4 people | about 40–50 days |
| One spark transmitter | 2 people | 4–5 days |
| One crystal receiver (including one pair of headphones) | 2 people | 4 days (mostly winding) |
| One wavemeter | 1 person | 1–2 days |
| Antenna masting (one end, transmit or receive) | 3 people | 2–3 days |
| Operator training (to 15 words/min) | 1 h per person per day | 60–90 days |
| Consumption | zinc, copper, sulfuric acid (Daniell); enameled wire; tin solder; porcelain insulators; iron wire | entered in the Chapter 38 accounts |

## Safety Boundaries

* **High voltage (spark-coil secondary, thousands of volts class)**: keying only on the low-voltage side (Iron Law); power off before adjusting the ball gap, and the Leyden jars discharged with the discharge rod first; two people present for every test — the Chapter 33 safety clauses apply in full.
* **Falling antenna**: mast guys tensioned in three directions; no watch position directly under the antenna; check guys and insulators pole by pole before wind season; when a broken antenna end falls, cut power before gathering the wire.
* **No sending, no receiving in thunderstorms**: before the storm, open the line knife switches and close the grounding knife switches (wire); close the antenna grounding knife switch (wireless); after the thunderstorm, patrol the line and inspect the lightning gaps before restoring traffic — emergency repair never races the storm.
* Electric-shock first aid follows the Chapter 32 procedure; posted at every station and drilled quarterly.
* Antenna-mast work at height runs on the two-person rule with no one below (Chapter 13 pole-erection safety clauses apply).

## A. Existing Tool List (partial)

Telegraph-key-grade audible code reading and the bell component family, spark coil, relays (Chapter 30); wire drawing, enameled wire, moving-coil meter, hand-cranked generator (Chapter 31); porcelain insulators, three-pole grounding method, lightning protection system, knife switches (Chapter 32); crystal detector point selection, waxed-paper capacitors, resonance method, magnetizing workmanship (Chapter 33); pole erection and water/carpentry works (Chapter 13); tin soldering (Chapter 17); ledger system (Chapter 43).

## B. New Tools Added in This Chapter

The full Morse code table and local character-set trimming (6 procedural signs); the Chinese four-digit telecode book system; the call sign / acknowledgment / verification / priority transmit-receive procedures; graded words-per-minute assessment and the retraining system; the three-line line-current budget arithmetic and the quick cell-count estimate, with the relay spacing table; the leakage-current criterion and sectional fault-finding with test clamps; the dual-relay bridged repeater station with manual bypass; the lightning spark gap and grounding-knife-switch system; the earth-return/two-wire trade-off rule; the spark transmitter of Leyden jar bank + adjustable ball gap + transmitting coil (low-voltage-side keying, spark-quench circuit); the wavelength formula and field antenna-capacitance accounting, with the resonant wavemeter; the tap + capacitor-step crystal receiver; the permanent-magnet-biased homemade headphones; the distance-condition registration ledger system; station establishment (four site-selection rules, copying logbook, frequency fingerprints, three-window roll call, independent emergency power).

## C. Unresolved Dependencies

* Continued supply of iron/copper wire and enameled wire (Chapters 31–32 capacity, counted into the accounts);
* Porcelain-insulator production capacity (Chapters 11–12) — pole routes and antenna-guy insulation both consume insulators;
* Battery materials (zinc, copper, sulfuric acid; or lead-acid grid materials) — the materials account for the traffic batteries and the transmission battery;
* Long-term frequency stability, and voice/continuous wave (requires vacuum-tube oscillation and amplification; to be registered after the Chapter 36 electronics industry);
* A local quantitative model of radio propagation (currently only the distance-condition ledger, no theoretical prediction — kept on file for future work).

## Next-Step Dependencies

* **Chapter 36**: station traffic records (error rates, life, spare-part consumption) are the raw data behind the electronics industry's production-line demand; once vacuum tubes can be sealed for long life, amplification arrives at the receive end first and the transmit end moves to continuous wave — this chapter's spark-gap keying, antennas, ground systems, and time-window system all carry straight over;
* **The Part 10 environment editions**: island edition (salt fog doubles insulator leakage — wet-state re-inspection tightened to weekly), rainforest edition (high thunderstorm frequency — the grounding-knife-switch system upgraded to standing practice), desert edition (dry-season ground-resistance re-checks and windblown-sand abrasion of antennas), frozen-ground edition (winter freeze blockage of ground electrodes — deepen the electrodes or switch to two-wire): each cites this chapter's corresponding clauses;
* **Chapter 43 ledger**: handover and succession of the four archives — telecode book editions, the master call-sign register, copying logbooks, and the distance-condition table;
* **Chapter 49**: occupational-safety registration for work at height and thunderstorm watch duty.
