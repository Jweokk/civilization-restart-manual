# Chapter 33: The First Electronic Devices

## Chapter Objectives

Establish the **experimental and conceptual foundation** for electronic devices, and give an honest manufacturing route: the component language of resistors, capacitors, and inductors; relays toward automatic control; thermionic emission and the vacuum diode and triode; crystal (ore) detection with a **rectification-ratio comparison registry**; and the first electronics laboratory. **We do not assume the reader can immediately build a sealable, long-life vacuum tube** — that depends on seal materials, the vacuum ladder, and degassing processes; this chapter stands up these three physical preconditions one by one, and explicitly downgrades the parts that cannot be done to demo grade + external dependency.

## Capability Boundary

**Can do:**

* R/L/C component manufacture and field calibration (comparison method);

* Relay logic and automatic control;

* **Continuous-pump demo-grade vacuum tubes** (the tube stays permanently connected to the exhaust station under continuous pumping — the true form of the first vacuum tubes in history): thermionic emission, one-way conduction, and grid-control phenomena measured;

* Practical crystal (cat's-whisker) detectors + a rectification-ratio comparison archive.

**Explicitly cannot do (the real status of the three physical preconditions)**:

1. **Sealed long-life tubes**: requires seal wire whose expansion matches glass (platinum or Dumet-type). Platinum has no local sourcing route (listed as a Class-C dependency); transitional iron-wire seals have high slow-leak rates — **in this chapter a sealed tube can only be a trial piece, not a capability item**;
2. **Convenient attainment of 0.01 Pa-class vacuum**: the piston pump cannot get there; a mercury-pump stage is needed (slow — several hours per tube by experience);
3. **High-frequency sources and precision AC measurement** (RF behavior registered as a challenge item).

**Exclusions** (Master Plan G01 table): the tungsten-filament incandescent-lamp route is not pursued — all filaments in this chapter are carbon filaments (carbonized bamboo/plant fiber, the route contemporary with Edison).

## Pre-Work Verification (check off one by one)

| # | Verification item | Criteria | Source |
| - | --------- | -------------------------------------- | ------------------ |
| 1 | Stable power supply | Battery bank or rectified supply, voltage fluctuation on record | Chapters 31–32 |
| 2 | Moving-coil meters and comparison-method bridge | Meters cleared by release slip; field-calibration records on file | Chapters 27, 31 |
| 3 | Glass lampworking | Tube pulling successful (Chapter 14 challenge item resolved); rod-to-tube fusion qualified after ≥50 practice runs | Chapters 14, 26 |
| 4 | Glass tubing and bulb blanks | Same-batch glass, annealed and qualified (thermal-shock test passed) | Chapter 14 |
| 5 | Two vacuum-pump stages | Water-jet aspirator outflow normal; piston pump leather-cup seal intact | This chapter + Chapter 21 |
| 6 | **Mercury source** | Mercury ≥0.5 kg (**only legitimate source: Section 16.12 mercury unlock protocol; this item is frozen until that protocol is built**) or legacy mercury (Starting Point B) | Chapters 12, 16 + Chapter 49 red line |
| 7 | McLeod vacuum gauge | One glass compression-type vacuum gauge, capillary volume ratio field-calibrated | This chapter + Chapter 25 |
| 8 | Ore | Galena ≥3 pieces (**different origins or different vugs of the same ore — needed for the Section 33.5 comparison registry**) | Chapter 16 |
| 9 | Chemical glassware and safety | Exhaust station ventilated; mercury tray (splash-containment tray) in place | Chapter 26 |

***

### 33.1 Resistors, Capacitors, and Inductors

#### 33.1.1 Resistors

* **Wire-wound resistors (reference grade)**: resistance wire (iron wire/copper-alloy wire, Chapter 31) wound on a ceramic tube (Chapter 11), given two coats of insulating varnish against moisture and abrasion. **The three-part basis for resistance values**: ① the same wire diameter and same length give equal resistance (paired by the comparison method); ② halving the wire diameter at the same length roughly quadruples the resistance (resistance ∝ length ÷ cross-sectional area — measure the local coefficient with two wires of known size); ③ register each unit individually with the Wheatstone comparison bridge (the Chapter 30 comparison-table system).

* **Power and temperature rise**: the rated power is registered by the "temperature rise stays under the red line (about 60 °C hand-feel)" test — raise the current through the same resistor until the too-hot-to-hold line; 0.7 times that current is the long-term allowable value (empirical value, must be field-calibrated).

* **Winding method**: plain close winding suffices for DC and low frequencies; **high-value wire-wound resistors in series in galvanometer circuits must be bifilar-wound (non-inductive winding)** — fold the wire into two strands and wind them together; adjacent turns carry current in opposite directions and the residual inductance cancels (otherwise self-inductance disturbs fast-changing measurements).

* **Carbon resistors** (molded rods of carbon black + wax/resin): high resistance values but poor noise and stability; register them for high-resistance situations, not as references.

#### 33.1.2 Capacitors

* **The Leyden jar** is the ancestral form (Chapter 30); **engineering it = the wax-paper rolled-foil capacitor**: two sheets of metal foil (Chapter 17 hammered foil) separated by waxed paper (Chapter 10 paper dipped in wax) and rolled tight. Capacitance grows with **area and layer count** and falls with **paper thickness** — make three capacitors from one roll by varying its length, measure relative capacitance by the comparison method, and you have the local "area–capacitance" coefficient;

* Behavior verification: DC is blocked (after charging, a series galvanometer gives only one swing), AC passes (in series in the AC-generator loop the lamp dims but does not go out — register this in comparison with the resistor);

* **Withstand-voltage test**: step the voltage up under water-resistor current-limiting protection; breakdown = scrap — sample two per batch for withstand voltage, and use the rest derated to 0.7× the batch's registered value (empirical protocol).

#### 33.1.3 Inductors

* A coil is an inductor (Chapter 30); **iron-core boost** (inserting an iron core at unchanged turns makes the lamp dimmer — register the phenomenon); doubling the turns roughly quadruples the self-inductance (unlike resistance: a squared flux-linkage effect; measure and register the local relationship);

* The three-component behavior table (responses to DC/AC) is page one of the language of circuits — **this table must be written from memory by every person, and each person must also measure it once by hand**.

[Card 33-01 Wire-Wound Resistor and Power Rating] (eight fields)

1. **Input materials**: resistance wire (iron or copper alloy, Chapter 31 drawing process); ceramic tube former (Chapter 11); two coats of insulating varnish for moisture and wear protection.
2. **Tools required**: winding jig, calipers (Chapter 22), supply and ammeter for the power test, hand for the temperature check. Calibration source: resistance set by **wire length and diameter** (measure resistance per unit length once per batch); power set by **temperature rise**, not by calculation.
3. **Sequence and control points**: choose wire for the target resistance, wind onto the tube (**turns must not touch** — touching shorts several turns), fix the leads, **two varnish coats each fully dry**, then power test: **raise current until the "too hot to hold" line (about 60 °C)** and record that current as the rating. Control points: turn-to-turn insulation and both coats dry.
4. **Empirical parameters and calibration**: rated power registered by the "rise does not cross the red line (about 60 °C by hand)" test — raise current to the too-hot line, that is the limit; resistance from length and diameter, with per-unit-length resistance measured first for the batch.
5. **Observations to record**: per unit — wire batch / length and diameter / measured resistance / varnish coats and drying days / test current and hand-temperature verdict.
6. **Pass / rework / scrap criteria**: pass = resistance in tolerance, no smoking or discoloration; rework = out of tolerance (change length); scrap = varnish breakdown or cracked tube (rewind).
7. **Common failures and diagnosis order**: (1) resistance lower than calculated — turns touching; (2) smokes when powered — rating too high or wire too thin; (3) drifts when damp — only one coat; (4) tube cracks — winding tension too high.
8. **L1 / L2 / L3 evidence**: L1 = one resistor with resistance and power registered; L2 = three of the same spec with comparable figures; L3 = a second person makes the same spec from this card alone.

### 33.2 From Electromagnetic Relays to Automatic Control

* **Relay** (Chapter 30 electromagnet + armature contacts): small current controls large current — a weak signal switches on local strong power; silver/copper contact pairs; a self-oscillating reed makes a buzzer;

* **Prototype logic gates**: relays in series = "AND"; in parallel = "OR"; normally-closed contacts = "NOT" — **relay logic is the first language of electronic computing** [Background/Outlook: the seed of the far-future computer lies here; not developed in this chapter];

* First case of automatic control: the automatic water-level pump (float–lever–relay–pump) — a rehearsal of the sense–judge–act three-stage pattern.

### 33.3 Why Mechanical Control Has Limits

* Contact sparking and erosion (a lifetime ceiling); response speed limited by mechanical inertia (an order of counts per second, empirical value);

* Logic scale: the wiring complexity of a room-sized relay installation far exceeds what hands can maintain [Background/Outlook];

* Conclusion: a current-control element that is **contactless and inertia-free** is needed — the vacuum tube (this chapter) and the crystal (Chapter 34) are the answers in the two directions.

### 33.4 Vacuum Electronic Devices I: The Cathode and Thermionic Emission

**Thermionic emission (the Edison effect)**: when the filament is incandescent its surface emits charged particles — add a positive electrode (plate) inside the tube and the emitted stream flows to the plate as a current (visible with a series galvanometer).

**Cathode material route (this chapter uses carbon filament throughout)**:

* **Carbon filament preparation**: shave bamboo slivers (or tough plant fiber) into uniform fine filaments (cross-section about 0.2–0.5 mm square, checked with a gauge plate), carbonize at high temperature in a sealed crucible (Chapter 12 furnace, above red heat for 1–2 h, empirical value) — out of the furnace they must be jet black, conductive (measure resistance with a battery), and springy rather than brittle to pass; under-carbonized turns brown, over-burned turns brittle (snaps when bent);

* **The carbon filament's fate**: at incandescent operating temperature it slowly evaporates and thins, and residual-gas oxidation burns it through — **a demo-grade tube lifetime of tens of hours is the design expectation** (empirical value, must be field-calibrated), not a failure; oxide cathodes and tungsten filaments are listed as Class-C dependencies (Master Plan exclusion table);

* First experiment (no vacuum needed): compare a carbon filament sealed into a bulb with a little air vs. one under rough vacuum — it burns out quickly in air and its lifetime rises sharply in low vacuum; **this is the lesson that "vacuum is the precondition of filament life."**

### 33.5 Vacuum Electronic Devices II: The Vacuum Ladder and Its Criteria (this chapter's key challenge; one of the three review gates)

#### 33.5.1 Pressure Ladder Table (orders of magnitude first; all criteria are checked against this table)

| Level | Pressure | Means of attainment | The tube's fate in it |
| --- | -------------------------- | --------------- | --------------- |
| Rough vacuum | \~10⁴–10³ Pa (about 10–20 mmHg) | Water-jet aspirator (limited by water temperature and water column) | Filament dies at once: too much gas |
| Low vacuum | \~10²–10 Pa | Grease-sealed piston pump (single stage) | Filament lights briefly, then oxidizes |
| Medium vacuum | \~1–0.1 Pa | Piston pump run long + degassing | Diode works marginally (glow discharge still present) |
| High vacuum | ≤0.1–0.01 Pa | **+ mercury displacement pump stage** | **Stable operating region of the triode** |

\*\*Key fact: stable triode operation needs ≤0.01–0.1 Pa, and the single-stage piston pump stalls at 1–10 Pa — a stage is missing in between.\*\* The first generation of practical triodes in history relied precisely on the mercury pump (mercury displacement pump / mercury diffusion pump), not the piston pump.

#### 33.5.2 Three-Stage Pump Sequence

1. **Water-jet aspirator** (rough pumping): high-speed water flow carries the gas away; cheap, no moving parts; stalls at the 10³ Pa level;
2. **Grease-sealed piston pump** (fine pumping): leather/rope seals + eccentric (the Chapter 21 mechanism family); twin cylinders alternating approximate continuous running; stalls at 1–10 Pa (limited by the seals and dead volume);
3. **Mercury displacement pump (the new stage established this chapter; slow but sure)**: structure — a mercury pool at the bottom + a gas-storage glass bulb whose lower opening is immersed in the mercury + a lifting mechanism (pulley or lever; the mercury container is raised and lowered by hand or waterwheel). **Cycle**: lower the mercury → the pressure in the bulb falls and the gas to be pumped is drawn through the valve into the bulb chamber; raise the mercury → the gas is compressed, pushes open the exhaust valve, and is expelled; each up–down cycle removes one charge of gas; repeat tens to hundreds of times (1–4 h per tube, empirical value, must be field-calibrated) and the tube can be pumped down to the 0.1–0.01 Pa level. **Every part is glass + mercury + levers — unlike the piston pump, it has no "seal dead volume" order-of-magnitude ceiling.** [Upgrade path: the mercury vapor diffusion pump (boiler + jet + condenser), more continuous and faster; listed as the challenge after this level]

#### 33.5.3 The Criteria Chain: McLeod Gauge Primary, Glow Secondary (declaration abolishing the old criterion)

**Old criterion abolished**: the previous edition used "the appearance/disappearance of glow discharge" as the vacuum criterion — **this is a wrong criterion**: glow discharge exists across the wide range of about 1–10³ Pa (varying with gas, gap, and voltage); "seeing a glow" proves only rough vacuum, 2–4 orders of magnitude short of the triode's need; "glow gone" corresponds to about the 10 Pa order, still 1–2 orders short. **From this edition on, glow serves only as a supplementary observation, not as an acceptance criterion.**

**Primary criterion: the McLeod gauge (compression type; self-buildable; the principle is not complicated)**:

* Structure: a glass tee with a large glass bulb at its lower end (volume V₀, known) joined to capillary C₁ (bore known), with a reference capillary C₂ standing alongside (same bore, compensating the capillary pressure difference); at the bottom, a mercury pool with a raising/lowering mechanism;

* Operation: after pumping to equilibrium, **raise the mercury** — once the mercury surface passes the tee, the gas in the bulb is cut off and compressed into capillary C₁, compressed until a small gas column remains at the top; **read the height difference h between the mercury levels in the two capillaries**;

* Principle and reading: the trapped gas originally filled V₀ (pressure = the unknown pressure P); after compression its volume = capillary cross-section × column length, and its pressure = h (in mmHg) — P = h × (compressed volume/V₀). The compression ratio reaches the 10⁴ level, so pressures down to 10⁻²–10⁻³ mmHg (≈ the 1–0.1 Pa level) can be measured;

* **Field-calibration method**: V₀ is measured by the water-fill weighing method (the Chapter 3/25 balance); the capillary bore is measured by filling with mercury and weighing a measured length; both values go into the instrument dossier, and readings thereafter give absolute pressure;

* Caution: the McLeod gauge **is distorted by condensable gases (water vapor)** (the vapor condenses during compression and shows no pressure) — bake the tube system to drive off water vapor before reading; after reading, **lower the mercury back to the pool** before pumping again.

**Supplementary criterion: high-frequency spark leak detection** (spark coil: interrupter + step-up winding, a Chapter 30 component) — move the probe along the outer glass wall, and the residual gas inside glows by induction: the color changes with pressure (violet-red → pink-white → pale blue → glow gone); use it together with a **field-calibrated color–pressure reference table** (calibrate the local reference table with simultaneous McLeod readings), for quick leak scanning (at the leak point bright spots gather into a "bright-spot cluster"). **Color judgments without a reference table behind them do not count.**

#### 33.5.4 Distinguishing Leaks from Outgassing (the pressure rise-rate method)

Close the valve to isolate the pump, and read the McLeod gauge at 5 min, 15 min, and 60 min:

* Pressure rises fast, then levels off → **outgassing** dominates (gas slowly released by the inner walls and electrodes) → remedy: bake-out (33.6);

* Pressure rises linearly → **leak** dominates → remedy: spark scanning + sectional clamping of the rubber line to localize (clamp near the pump end and the pressure still rises = the tube leaks; it does not rise = the leak is on the pump side).

[Card 33-02 Evacuation and Pressure Reading] (eight fields)

1. **Input materials**: sealed envelope (per 33-03); pumping train (water-jet aspirator, piston pump, mercury diffusion pump).
2. **Tools required**: vacuum gauge (McLeod or glow observation), pumps, sealing grease. Calibration source: **every criterion is read against the pressure ladder table**, never by feel.
3. **Sequence and control points (step down one grade at a time, never skip)**: rough vacuum (~10⁴–10³ Pa, aspirator), low vacuum (~10²–10 Pa, grease-sealed single-stage piston pump), medium vacuum (~1–0.1 Pa, piston pump at length plus outgassing), high vacuum (≤0.1–0.01 Pa, **plus one mercury diffusion stage**). Control points: hold and measure at each grade — the filament dies at rough vacuum, lights briefly then oxidizes at low, a diode barely works at medium, and **high vacuum is the triode's stable region**.
4. **Empirical parameters and calibration**: aspirator limit ~10³ Pa; piston pump 1–10 Pa; **diffusion pump 0.1–0.01 Pa, 1–4 h per tube** (empirical, calibrate); diode floor ~1 Pa; triode stable region ≤0.1–0.01 Pa; the glow range ~1–10³ Pa is **auxiliary only, never a criterion**.
5. **Observations to record**: per tube — time to each grade / pump hours / measured pressure / glow appearance (auxiliary) / internal discoloration.
6. **Pass / rework / scrap criteria**: pass = the grade that tube type requires, reached and held; rework = will not reach grade (check leaks, change grease, pump longer); scrap = repeated leakage (micro-crack at a seal, redo 33-03).
7. **Common failures and diagnosis order**: (1) never comes down — slow leak at a seal (water-drop or dust test, 14.9); (2) stalls at one grade — pump limit reached, add the diffusion stage; (3) pressure fluctuates — grease dried or oil contaminated; (4) filament flashes and dies — still at rough vacuum, too much gas.
8. **L1 / L2 / L3 evidence**: L1 = one tube through four grades with records; L2 = three consecutive tubes reaching triode grade; L3 = a second person runs the train and reads the same grade from this card alone.

### 33.6 Vacuum Electronic Devices III: Seals, Degassing, and Seal-Off (review gates two and three)

**Figure 33-1 Lead-seal structure (schematic cross-section)**

```
      ┌─────────────┐ Glass bulb (α≈9)
      │ Vacuum region│
      │  ◇Plate      │
      │ ╱           │
      │ filament~~~  │
      │  ╲           │
      └──╪═══════╪───┘ ← Seal point: fine platinum wire / fine iron wire (≤0.5mm)
         ║       ║      Glass–metal α difference <10% = matched; cooling-shrink mismatch = microcracks, slow leak
      ──╨───────╨── External leads → circuit
   Leak check: drip water at the seal / ash-powder suction method (14.9)
```


#### 33.6.1 Seal Material Routes (applying the expansion-coefficient table)

| Seal pair | α difference | Assessment |
| ---------------------------- | ---- | ------------------------------------------------------ |
| This chapter's soda-lime/lead glass + **fine platinum wire** (α≈9×10⁻⁶/K) | Matched | **First choice, but platinum has no local route — listed as a Class-C dependency** (if legacy platinum wire exists, Starting Point B uses it directly) |
| Lead glass + **very fine iron wire** (≤0.5 mm) | Off by 30% | Fine-wire flexibility gives tolerance — usable as a transitional seal, **high slow-leak risk**, trial pieces only |
| Glass + copper wire (α≈17) | Off by nearly double | **Forbidden** (will certainly crack or slow-leak) |
| Glass + glass + **pressed-in carbon electrode** | No metal interface | Carbon neither melts nor cracks the glass — **the conductive-seal problem shifts to "mechanical crimping of the carbon to its lead wire"**; gas tightness relies on a long channel and sealing paste (substitute route, trial grade) |

**The dual-track system this chapter adopts**:

* **Demo track (capability item)**: the tube is **permanently connected to the exhaust station** (pump never stopped) — all teaching, measurement, and phenomenon registration is done on this track. The earliest vacuum-tube experiments in history ran exactly this way;

* **Sealed track (trial item, L3 target)**: lead glass + fine platinum wire (external dependency), or lead glass + very fine iron wire transitional seal (local, low success rate; register the success rate honestly); **until matched materials exist, "making a sealed vacuum tube" is not a capability commitment — it is a Class-C dependency**.

#### 33.6.2 Degassing (bake-out; a mandatory step missing from the previous edition)

The number-one cause of vacuum-tube failure is not incomplete pumping but **continued outgassing from the electrodes and glass walls after seal-off** — water vapor and organics adsorbed at room temperature are released within hours once the filament heats, ruining the vacuum. Protocol:

1. **Bulb bake-out**: while pumping, bake the bulb evenly with a soft flame or furnace-mouth hot air to the "too hot to touch" level (about 150–250 °C order, empirical value; never overheat one spot until it softens and deforms) for 15–30 min while the pump keeps drawing — the released gas is pumped away;
2. **Electrode degassing by current**: raise the filament voltage in steps (rated → 1.2×), 10 min each — the plate can be heated to dull red by an external supply (if the structure allows); **watch the McLeod gauge while baking**: pressure first rises (outgassing) then falls (pumped away) — when the curve turns downward, degassing is nearly complete;
3. Degassing-complete criterion: the McLeod reading returns to its pre-bake level and the **pressure rise-rate method** shows outgassing is exhausted (pressure trending steady).

#### 33.6.3 The Getter: the Correct Activation Procedure (correcting the previous edition's operational error)

* **Previous edition's error**: "burn white phosphorus / a magnesium strip inside the tube" — after seal-off the tube **is sealed; nothing can be burned inside it afterward**. The correct procedure is **post-seal-off activation by external heating**;

* Correct process: the getter (red phosphorus powder or magnesium powder, mixed with glue into a paste and pre-coated on a small metal dish/ring on the electrode support inside the tube) — after seal-off, aim a sharp fine flame **through the glass at the metal dish** and heat it locally to red; the getter evaporates/burns into activation, the evaporant deposits as a mirror film, and it keeps absorbing the residual gas. Seeing a brief flash inside the tube + a metallic mirror deposit somewhere on the glass means success (the classic criterion);

* White phosphorus falls under the Chapter 26 red line (do not handle it without dedicated protection) — **red phosphorus / magnesium powder is the default choice**; tubes without a getter are honestly labeled "tens of hours" lifetime.

#### 33.6.4 Seal-Off

At the soft-glass narrow neck of the exhaust-station line, seal with a soft flame and pull apart (◎ hand technique: heat the neck evenly with the flame until soft, draw it thin first, then part it, and immediately fire-polish the break round) — after seal-off, **recheck the tube at 24 h** (leave a test port where the McLeod gauge can stay attached, or substitute spark-glow + behavior testing): pass if the one-way conduction characteristic has not degraded.

[Card 33-03 Sealing, Outgassing, and Tip-Off] (eight fields)

1. **Input materials**: glass envelope (α ≈ 9×10⁻⁶/K, soda-lime or lead glass); leads (**fine platinum wire is the matched first choice but has no local route — carried as an open item**; **very fine iron wire ≤0.5 mm works as a transitional seal with high slow-leak risk**); carbon electrode pressed in, which moves the conduction problem to the carbon-lead interface. **Glass with copper wire (α ≈ 17) is forbidden** — nearly a factor of two apart, it cracks or leaks.
2. **Tools required**: torch or small furnace, jigs, leak agents (water drop, dust), baking rig. Calibration source: **expansion mismatch under 10% counts as matched** — read the table, do not experiment.
3. **Sequence and control points**: seal (fuse glass to lead; **differential contraction on cooling is the root of micro-cracks and slow leaks**), leak test at the seal, **bake out about 150–250 °C for 15–30 min**, fit getter if used, evacuate, **tip off**. Control points: the **α difference of the sealing pair** and **bake temperature and time** — neither may be adjusted by feel.
4. **Empirical parameters and calibration**: pair α difference <10%; iron wire limit ≤0.5 mm; bake 150–250 °C for 15–30 min; **the 24 h post-tip-off check is the acceptance test**.
5. **Observations to record**: per tube — sealing materials and α difference / leak result / bake temperature and duration / tip-off time / characteristics at 0 h and 24 h.
6. **Pass / rework / scrap criteria**: pass = leak clean, bake on target, **unchanged at 24 h**; rework = seep found (re-seal); scrap = clear degradation at 24 h (slow leak — wrong material pair or process, change route).
7. **Common failures and diagnosis order**: (1) micro-cracks after cooling — α difference over 10%, change the pair; (2) fades a day after tip-off — insufficient outgassing or an active leak; (3) white haze inside — water vapour, extend baking; (4) getter darkens early — oxidized during evacuation, check the grade.
8. **L1 / L2 / L3 evidence**: L1 = one tube through seal, leak test, bake, tip-off; L2 = three consecutive tubes unchanged at 24 h; L3 = a second person completes one from this card alone and passes the 24 h re-check.

### 33.7 Vacuum Electronic Devices IV: Diode and Triode (demo-track experiment procedure)

**Vacuum diode**: carbon-filament filament + plate (a rolled cylinder of tin foil/copper sheet) sealed into a bulb (Chapter 26 lampworking) → pumped on the exhaust station to ≥1 Pa (Section 33.5 criteria) → degassed → experiments:

* **One-way conduction**: plate through an ammeter to the battery positive — current flows; reversed — near zero (record the volt-ampere characteristic point by point into a curve table: voltage 0 / half a cell / 1 cell… read the current);

* Immediate use: AC to DC (rectification) is quieter and spark-free next to the commutator — demonstrated directly on the demo track.

**Vacuum triode**: add a **grid** (a sparse spiral wire or mesh) between plate and filament → pump to ≤0.1 Pa (**must pass through the mercury-pump stage**) → degas → experiments:

* **Grid-control phenomenon (the L2 criterion is this phenomenon, not a gain value)**: with filament and plate voltage fixed, adjust the grid voltage from zero toward negative, recording plate current point by point — **a small grid-voltage change producing a clear plate-current change** establishes grid control;

* Amplification demo: feed a weak signal into the grid circuit (e.g., the brush fluctuation of a hand-cranked generator) and watch the amplified fluctuation on a meter in series in the plate circuit — **gain figures are not an acceptance item** (in medium vacuum gain appears sporadically and irreproducibly; the previous edition's "at least 5×" is void; reasons under Capability Boundary);

* \*\*[Background/Outlook]\*\* amplifiers and oscillators lead from here to the beginning of electronics — stable gain awaits mature sealed tubes and purer materials.

### 33.8 Crystal Detection and the Rectification-Ratio Comparison Registry (pre-planting the motivation for Chapter 34)

**Crystal (cat's-whisker) detector**: touch a galena/pyrite crystal face lightly with a fine spring wire (the "cat's whisker", Chapter 31 fine wire) — the contact conducts one way; the contact position is sensitive (every point of the crystal face differs), so use an adjustable contact mechanism (spring + fine-adjustment screw, Chapter 27).

**Detector-making essentials (material identification filled in — it is not "any galena will do")**:

* Choose a **fresh cleavage face**: crack the ore open and take the bright face (exposed faces have thick oxide layers and rectify poorly); the face must be flat (uniform reflection when viewed against the light); wipe off the oxide film lightly with a fine whetstone (◎ hand-feel: light enough to remove only the film, not scratch the face);

* Try-touch point by point: **test point by point** on the same crystal face (press the spring wire lightly at different spots), and choose the point that gives "large forward current, small reverse current, and a stable reading after you let go" — good points often sit at the edges of small steps on the crystal face;

* Locking: once chosen, lock it with the fine-adjustment screw and record a position sketch into the component register.

**Rectification-ratio comparison registry (a new institution this chapter, setting the problem for Chapter 34)**:

* Definition: at the same voltage (e.g., one battery cell), forward current ÷ reverse current = the **rectification ratio**;

* **Registry table**: measure contacts of galena, pyrite, and magnetite across different origins / different vugs / fresh face vs. oxidized face — ratios range from near 1 (no rectification) to tens of times (empirical range; your team's own measurements govern);

* **This table is page one of Chapter 34**: different purity and crystal quality → different rectification behavior → the motivation for "why purify semiconductor materials" is no longer preaching; it is your own data.

**Interference elimination for negative-resistance registration (correcting the previous edition)**: the old edition registered "current decreases as voltage in some direction increases" directly as possible negative resistance — poor contact, measurement error, and true negative resistance get mixed together. **New protocol**: on observing the phenomenon, first run two elimination steps — ① tap and re-seat the contact and retest (rules out poor contact); ② swap meter and leads and retest (rules out measurement error); only what still reproduces stably after both eliminations is entered in the negative-resistance observation register (the mechanism explanation belongs to Chapter 34; do not speculate).

[Card 33-05 Crystal Detector: Point Selection and Rectification Ratio] (eight fields)

1. **Input materials**: mineral (galena, chalcopyrite and other natural semiconductors, surveyed in Chapter 16); cat's whisker (fine metal wire); adjustable holder.
2. **Tools required**: meter or simple galvanometer, adjustable contact rig, signal source (spark gap or resonant circuit). Calibration source: **the rectification ratio is the only criterion** — forward/reverse resistance ratio, not "it sounds louder".
3. **Sequence and control points**: break a fresh cleavage face, mount, probe point by point, **measure forward and reverse resistance at each point and compute the ratio**, fix the best point, connect and try reception. Control points: **probe and measure every point** (one mineral varies enormously between points); light contact pressure — press hard and it becomes an ohmic contact and rectification vanishes.
4. **Empirical parameters and calibration**: ratio = reverse / forward resistance, higher is better; resonant demonstration point L ≈ 2.5 H with C ≈ 1 µF gives f₀ ≈ 100 Hz (buzzer band, empirical, measure it); contact pressure limited to "signal received without the ratio collapsing".
5. **Observations to record**: per mineral — type and origin / points probed / forward and reverse resistance and ratio at each / chosen point / reception result.
6. **Pass / rework / scrap criteria**: pass = a usable ratio that receives stably; rework = low ratio (fresh face or another point); scrap = no rectification anywhere (not a semiconductor, or fully oxidized).
7. **Common failures and diagnosis order**: (1) nothing at all — pressure too high (shorted) or surface oxidized; (2) works intermittently — unstable contact; (3) ratio changes with pressure — pressing too hard, lighten and remeasure; (4) good yesterday, dead today — face oxidized, break a new one.
8. **L1 / L2 / L3 evidence**: L1 = one mineral with point-by-point ratios and a chosen point; L2 = three minerals with comparable ratios; L3 = a second person finds a usable point from this card alone.

### 33.9 Semiconductors versus Metals (qualitative observation checklist)

Distinguish materials with three tests — temperature difference, light, and contact (an observation institution paving the road for Chapter 34):

1. **Thermoelectric EMF**: join two metals into a loop with the two junctions at different temperatures → the galvanometer deflects (a thermocouple — register this new route for temperature measurement in passing; Chapter 25 alternate route); some ore contacts show pronounced thermal effects [Background/Outlook: the seed of thermoelectric generation];
2. **Light effect**: the current through an ore contact changes under illumination — record the photosensitive phenomenon (the far-term seed of illuminance meters and optical communication);
3. **Temperature rise**: metal resistance rises; some ores' resistance falls instead — register the negative-temperature-coefficient observation (one hallmark of semiconductors).

### 33.10 From Material Properties to Electronic Devices

**Capability ladder table (honest version)**:

| Level | Capability | Status in this chapter |
| - | --------------- | ------------------------ |
| 1 | R/L/C components and measurement | **Established (L2 verifiable)** |
| 2 | Relays and automatic control | **Established (L2 verifiable)** |
| 3 | Three-stage vacuum ladder + McLeod gauge criteria | **Established (L2 verifiable)** |
| 4 | Practical crystal detection + rectification-ratio archive | **Established (L2 verifiable)** |
| 5 | Vacuum diode (demo track) | **Established (L2 verifiable)** |
| 6 | Vacuum triode (demo track: grid-control phenomenon) | **Phenomenon-level established (L2 verifies the "phenomenon", not gain)** |
| 7 | Sealed long-life tube | **Class-C dependency (external dependency for seal materials; fine-iron-wire trial track)** |
| 8 | Transistor (point contact) | Chapter 34 (after material purification matures) |
| 9 | Integrated circuits | Chapter 35 (the ultimate challenge) |

### 33.11 How to Establish the First Electronics Laboratory

* **Instrument release slips** (Chapter 27 electrical edition): voltmeters, ammeters, and continuity testers calibrated and tagged first; the McLeod gauge carries its field-calibration dossier;

* **Component register**: every homemade component (resistor/capacitor/tube/ore) gets a number + parameter card + lifetime record — vacuum-tube lifetimes and ore-contact drift tracked item by item; **the rectification-ratio archive and the negative-resistance observation register are managed in the same book**;

* **Test protocols**: new circuits run no-load → half-load → full-load; power off before changing wiring; discharge high-voltage capacitors before touching them;

* **A separate room from the chemistry laboratory** (vapors and corrosive atmospheres ruin contacts); guard against moisture, dust, and vibration; static discipline (in dry climates, touch the grounded bench first);

* **Mercury discipline (new this chapter, red-line level)**: all mercury work is done in shallow trays (splash containment); spilled mercury is covered with sulfur powder and collected (the Chapter 49 disposal line); the McLeod raising/lowering mechanism moves slowly to prevent mercury hammer; wash hands after work; **no food, no drink, no smoking in mercury work areas**.

***

### 33.12 Deeper R/L/C Measurement: Prototype AC Impedance and a Resonance Demo

**Same-component AC/DC behavior comparison table** (AC source = the Chapter 32 hand-cranked AC generator; DC source = battery bank; the same indicator lamp in series to show brightness; measure and register item by item):

| Component | On battery (DC) | On AC generator (low frequency) | Registered conclusion |
| ---- | --------- | -------- | ------------ |
| Wire-wound resistor | Brightness set by resistance, steady | Essentially as bright as the DC case | Resistance does not distinguish AC from DC (low frequency) |
| Wax-paper capacitor | One swing while charging, then current stops | Lamp dim but not out | Blocks DC, passes AC |
| Air-core coil | As bright as an equal-resistance resistor | Slightly dimmer than the DC case | Small inductive reactance |
| Iron-core coil | As bright as an equal-resistance resistor | Markedly dimmer | Iron-core boost = more "AC resistance" |

* **Frequency dependence (crank speed is frequency)**: double the crank speed — the capacitor loop brightens, the iron-core loop dims: capacitive reactance falls with frequency, inductive reactance rises. **Crank-speed-to-frequency conversion**: a two-pole machine gives one cycle per revolution, f = revolutions/second; time 60 revolutions with a seconds pendulum or pendulum clock (the Chapters 3, 25 time base) to obtain the local conversion value, registered in the instrument book; thereafter the "crank-speed setting" doubles as a coarse frequency setting;

* **Resonance demo (LC frequency selection; register the lamp-brightness peak)**: switch the AC source to the 33.2 buzzer (self-oscillating reed, tens to hundreds of Hz — the hand-cranked machine cannot reach the resonance band; see the calculation below). Series-connect the iron-core inductor and the capacitor bank with an indicator lamp, to the buzzer output; sweep frequency by turning the reed-tension screw: **at one screw turn count the lamp is brightest (current peak); off it, it dims** — this is series resonance. Register: peak turn count, bright-zone width in turns, L (turn count and core depth), C (number of roll turns);

* **Reachability calculation (number discipline)**: f₀ = 1/(2π√(LC)). Take L ≈ 2.5 H (iron core, 2000-turn class, measured and registered) + C ≈ 1 µF (a dedicated roll-wound batch: about 6 m² of 0.1 mm waxed paper rolled with foil gives 1 µF, empirical estimate) → f₀ ≈ 100 Hz, inside the buzzer band — reachable; if the capacitor bank only manages 0.1 µF, then L ≈ 25 H is needed (several times the turns, still hard to reach) — **conclusion: the 1 µF capacitor bank is dedicated material for this demo; without it, downgrade to the "crank-speed-doubling monotonicity" demo, and register the resonance peak as a challenge item**;

* **◎ Peak-point reading**: visual judgment of the lamp peak has a subjective component. Practice method: sweep the same loop 10 times, with each person reading the peak turn count; dispersion ≤ half a turn passes. Misjudgment compensation: parallel a small-value shunt with the lamp into a moving-coil meter (Chapter 31) and take the peak at maximum needle deflection;

* **Coarse Q comparison (compare rank only, no numeric measurement)**: with the same capacitor, sweep two coils of different core-insertion depth once each — **the narrower bright-zone turn width has the higher Q** (the sharper peak). The concept Q = f₀/Δf lands intuitively as "peak width"; the comparison conclusion goes into the component register. Absolute reed-frequency measurement (an improvised stroboscope: hand-cranked through speed-up gears driving a multi-hole spinning disk to freeze the reed's image visually; the disk speed is known, so it can be computed) is registered as a challenge item and does not affect the comparison method. [Background/Outlook: the frequency-selective loop is the first cornerstone of radio reception]

[Card 33-06 McLeod Gauge: Making and Calibration] (eight fields)

1. **Input materials**: glass tubes and two capillaries **of identical bore**, mercury, scale plate. **The two capillaries must match** — mismatch biases every reading.
2. **Tools required**: mercury, rule, level reference, connection to the vacuum system. Calibration source: **compression ratio sets the range** (~10⁴); the scale is computed from geometry, not drawn by rule of thumb.
3. **Sequence and control points**: form the U and capillaries, fill with mercury, fit the scale, **zero both columns**, connect to the system, compress and read, convert to pressure. Control points: **matched bores** and **zero correction**; read both the column difference and the compressed height.
4. **Empirical parameters and calibration**: compression ratio ~10⁴; reads to the **0.1 Pa level**; scale graduated in segments from the geometry; self-calibrate each instrument once against a known pressure.
5. **Observations to record**: per instrument — measured bores / scale segments / zero correction / deviation at known points.
6. **Pass / rework / scrap criteria**: pass = agrees with a standard point within tolerance at the 0.1 Pa level; rework = zero off (re-zero); scrap = mismatched bores (remake — no scale can compensate).
7. **Common failures and diagnosis order**: (1) constant offset — zero never set; (2) chaotic readings at high vacuum — mismatched bores; (3) column breaks — air admitted too fast, bleed slowly; (4) two readings differ at one point — temperature change or dirty mercury surface.
8. **L1 / L2 / L3 evidence**: L1 = one gauge graduated and zeroed; L2 = readings at three known pressures with deviations recorded; L3 = a second person makes and calibrates one from this card alone.

### 33.13 Cathode Process Extension: Measured Carbon-Filament Aging and Two Registry-Only Directions

**Carbon-filament lifetime–voltage measurement table (new institution this chapter)**: same filament batch, same vacuum grade (≥1 Pa, demo track), burn at each voltage step until failure, ≥3 filaments per step, take the median:

| Voltage step (rated = 1.0) | Visual brightness | Lifetime (empirical range) | Notes |
| ----------- | ---- | ------------- | -------------- |
| 0.9 | Dim red | Several times the rated step | Emission drops in step; unsuitable for amplification experiments |
| 1.0 (rated) | Dull red tending orange | Tens of hours | The rating is calibrated to this visual step |
| 1.1 | Orange-yellow | About 1/3–1/2 of the rated step | For short use when brightness comes first |
| 1.2 | Bright yellow-white | Around ten hours | Degassing overvoltage step only, not a working step |

* **Rated-voltage field calibration**: raise a new tube's voltage in steps from low; "dull red tending orange, not glaring to the eye" defines the 1.0 step (same-batch filaments paired by equal length-resistance, the Chapter 31 comparison method); transcribe the calibrated value into that tube's dossier, and record lifetime in the lifetime column of the component register;

* **Aging indicator (end-of-life precursor)**: at constant voltage the carbon filament evaporates and thins → resistance rises → current slowly falls; **register an end-of-life precursor when the working current falls to 0.85 of its initial value**; thereafter record every 2 h until burnout, keeping the current trace and the burnout time on the same page;

* **Oxide-cathode pre-research boundary (listed Class-C, not implemented)**: the only registrable item is coating preparation — an alkaline-earth carbonate slurry (starting from lime slurry) applied to the carbon filament and dried, with control tubes built to compare emission; **the activation mechanism (how the coating becomes an active emitting surface) and the required temperature are unknown** — coating without confidence only adds an outgassing source, so the whole direction is listed Class-C (consistent with the Class-C list); this chapter keeps a single page, the "coating-preparation register", its data reserved for the metallurgy line's far-term use;

* **Thoriated-tungsten substitution direction (register only, do not start)**: thoriated cathodes could lower emission temperature and extend life — the tungsten-filament route is already excluded under the Master Plan exclusion table; there is no local thorium source and no starting point; keep a one-line catalog entry and spend no labor hours on it.

[Card 33-04 Carbon Filament: Making and Life-Grade Registration] (eight fields)

1. **Input materials**: organic precursor yarn (cotton thread, hemp fibre, Chapter 15); carbonizing setup (sealed crucible plus furnace, Chapter 12).
2. **Tools required**: crucible, furnace, calipers for the section, supply with voltage steps, brightness reference. Calibration source: section by calipers; life registered as **hours burned to failure**.
3. **Sequence and control points**: select the yarn, carbonize sealed (oxygen excluded, heat with the furnace), retrieve the filament, check section (**0.2–0.5 mm square**), mount, burn at each voltage step and record life. Control points: **carbonizing must be oxygen-free** (with air it burns to ash); section drift sets the life grade directly.
4. **Empirical parameters and calibration**: section **0.2–0.5 mm square**; life in the tens of hours; **voltage steps (rated = 1.0)**: 0.9 dull red, several times rated life, emission falls with it and it is unusable for amplification; 1.0 rated, tens of hours; 1.1 orange-yellow, about 1/3–1/2 of rated; **1.2 yellow-white, ten-hour class, outgassing over-voltage only, never a working point**.
5. **Observations to record**: per batch — yarn type / carbonizing temperature and time / measured section / brightness and burn-out time per voltage step.
6. **Pass / rework / scrap criteria**: pass = section in band and rated-step life in the tens of hours; rework = section off (redraw); scrap = under-carbonized (brittle, snaps on contact).
7. **Common failures and diagnosis order**: (1) snaps on mounting — over-carbonized or too thin; (2) burns out in hours at rated — thin section or poor vacuum; (3) uneven brightness — uneven section; (4) life far below grade — residual gas (back to 33-02).
8. **L1 / L2 / L3 evidence**: L1 = one filament with section and rated-step life; L2 = a four-step life table from one batch at one vacuum grade; L3 = a second person makes the same grade from this card alone.

### 33.14 Tube Sockets and Pin Standardization (aligned with the thinking of the Chapter 22 thread standard)

**Why standardize**: the demo track's "tube–station interface" and the trial track's "tube–circuit interface" both involve repeated connecting and disconnecting of wiring; without a standard, every tube needs its own fixture and every tube swap costs half a day of rewiring. The tube socket is the electronic device's first serialized standard part — **the thinking matches the Chapter 22 thread standard: define the series first, then the tolerances, and register go-gauge checks on mated pairs.**

* **Pin diameter series**: three steps, 1.0 / 1.5 / 2.0 mm (the same wire-drawing process as Chapter 31 resistance wire): demo-tube leads uniformly 1.5 mm; 1.0 reserved for grid leads; 2.0 for filament leads (large current, low voltage drop);

* **Pitch circle and pin count**: the four-pin socket (diode) has a 20 mm pitch circle with pins at 90°; the five-pin socket (triode, one extra grid pin) has a 30 mm pitch circle with pins at 72°. Transcribe the series table into the ledger; tubes and sockets are made to the same table, and **cross-batch interchangeability** is the L3 criterion;

* **Anti-reverse-insertion keying**: with equally spaced pins, one reversed insertion destroys the tube (plate–grid reversal always ruins it). Specify **adjacent arc lengths as one wide and three narrow** (four-pin socket arc lengths at the 45/30/30/30 mm level; on the five-pin socket the wide arc faces the filament pin), with an asymmetric keyway cut in the socket — **"cannot be inserted reversed" is the pass criterion**;

* **Socket material**: porcelain first (turned from a ceramic blank, Chapter 11; heat- and voltage-resistant, non-hygroscopic); Bakelite chemistry is not yet mature, so substitutes are varnished-cloth laminate board (cloth soaked in varnish and hot-pressed) or hard wax board — **permitted only at the cold end, far from the filament's heat**, with the surface branded "COLD" to prevent misuse;

* **Contact springs and insertion-cycle lifetime registration**: contacts are spring copper strips (Chapter 31 copper alloy) with two-point contact, pre-bent with overtravel; **lifetime criterion: after 200 insertion cycles, contact resistance ≤ 1.5× the initial value** (voltage-drop method: pass a known current and read the contact voltage drop, Chapter 27 meters); measure once every 50 cycles into the ledger.

[Card 33-07 Socket Making and Pin Standardization] (eight fields)

1. **Input materials**: pin wire (1.0 / 1.5 / 2.0 mm, same Chapter 31 drawing route as resistance wire); insulating body (ceramic, varnished hardwood, or a phenolic substitute); spring contacts.
2. **Tools required**: drill and reamer, pitch-circle layout (Chapter 3 angle plate and dividers), contact-resistance measurement. Calibration source: **pitch circle and pin spacing laid out to the standard value**, not fitted to whatever envelope is at hand.
3. **Sequence and control points**: lay out pitch circle and pin positions, drill, fit pins and springs, trial insertion, **measure contact resistance**, number and log. Control points: **pitch circle and spacing** (off and the tube will not insert or the pins land wrong); spring pressure firm but not excessive.
4. **Empirical parameters and calibration**: pin diameters **1.0 / 1.5 / 2.0 mm** (demonstration tubes all 1.5 mm; 1.0 for small-signal tubes); **four-pin socket pitch circle 20 mm, pins at 90°**; **five-pin socket (triode, one extra grid pin) 30 mm at 72°**; **after 200 insertions contact resistance ≤ 1.5× initial** (criterion).
5. **Observations to record**: per socket — pin count / measured pitch circle and spacing / pin diameter / initial resistance / after 200 insertions.
6. **Pass / rework / scrap criteria**: pass = positions correct and **≤1.5× initial after 200 insertions**; rework = resistance high (adjust spring or change pins); scrap = body cracked or positions wrong (remake).
7. **Common failures and diagnosis order**: (1) tube will not go in — pitch circle or spacing off; (2) poor contact — low spring pressure or oxidized pins; (3) loose after a few insertions — spring fatigue; (4) sockets not interchangeable — not built to standard (one jig per tube equals failed standardization).
8. **L1 / L2 / L3 evidence**: L1 = one socket through the insertion test; L2 = one four-pin and one five-pin both within resistance after 200 insertions; L3 = a second person makes the same spec from this card alone with matching readings.

### 33.15 Voltage Indicator: Glow Steps and a Prototype Voltage-Test Pen

**No neon bulb — what then**: neon depends on air fractionation (far-term chemical industry; no local route) — but glow discharge (the supplementary observation established in 33.5.3) is itself a physical voltage indicator: **the tube strikes = the voltage has crossed that tube's striking step**. A row of discharge tubes with different striking voltages forms a "voltage scale" — the forerunner of the glow indicator tube [Background/Outlook: seeds of glow regulation and numeric display tubes; this chapter registers the phenomenon only].

* **Improvised tube making**: seal "needle-point-to-plane" electrodes inside the tube; the demo track connects to the exhaust station at fixed pressure (backfill dry air to the target pressure: crack the valve to admit gas + McLeod spot checks); the trial track seals off at fixed pressure (pressure registered in the dossier);

* **How to choose pressure and gap (registering the Paschen minimum; counterintuitive first)**: at fixed pressure, **striking voltage first falls, then rises as the gap grows** — striking voltage against "pressure × gap" is U-shaped (the Paschen minimum; the air minimum sits at several hundred volts). The improvised step series takes **the left branch on the low-pressure side**: fixed pressure at the 10 Pa level, gaps in four steps of 0.5/1/2/4 mm, striking voltage rising as the gap shrinks (counterintuitive; register honestly);

* **Calibration table (example values; must be re-calibrated locally)**: striking voltage is calibrated by the **atmospheric sphere-gap method** — connect the same high-voltage source to an adjustable sphere gap in open air; a breakdown distance of d mm corresponds to about 3×d kV (atmospheric air \~3 kV/mm, empirical value); re-verify the local coefficient at three breakdown points of 1/2/3 mm, then read each tube's lit/unlit threshold (raise the voltage 3 times, take the median):

| Tube | Gap (fixed pressure, 10 Pa level) | Striking-voltage step (example; re-calibrate locally) |
| -- | -------------- | -------------- |
| G4 | 4 mm | \~1 kV class (lights first) |
| G3 | 2 mm | \~2 kV class |
| G2 | 1 mm | \~4 kV class |
| G1 | 0.5 mm | \~7 kV class (lights last) |

* **Use and limits**: connect the tubes, each through a current-limiting carbon resistor (1–5 MΩ, Chapter 31), in parallel across the high voltage under test; "G(k) lit while G(k+1) is not" places the voltage at step k — **coarse-step (±30% class) indication, not a substitute for measurement**; pressure drift shifts the steps: spot-check the exhaust line once daily with the McLeod gauge. The glow remains continuously visible (unlike an atmospheric spark, which flashes and dies), so it serves better as an indicator than the spark gap — the spark gap is reserved as the calibration reference;

* **Prototype voltage-test pen**: a G4-step tube + current-limiting resistor inside an insulated tube, a probe at one end and a metal cap for the hand at the other: it lights = "live and above the striking step". **The lower limit is bounded by the physics of the Paschen minimum (several hundred volts class); below that it does not light** — for low-voltage live testing, substitute the series-lamp method (the Chapters 31–32 line-repair practice). Current limiting is set by criterion, not a fixed value: working voltage ÷ resistance ≤0.5 mA (order-of-magnitude sanity check: 220 V ÷ 470 kΩ ≈ 0.5 mA, below the human perception threshold of about 1 mA, empirical value; when only hundred-kΩ-class resistors are available, temporary use under the two-person rule only); two-way check before use: it must light on a known-live point and must not light on a confirmed-dead point; high-voltage testing under the two-person rule (this chapter's safety boundary).

[Card 33-08 Glow-Discharge Voltage Calibration] (eight fields)

1. **Input materials**: glow tube, adjustable high-voltage source, sphere gap for calibration, fixed-pressure gas supply at 10 Pa.
2. **Tools required**: sphere gap (**~3 kV/mm calibration**), voltmeter or gap-distance reading, gas supply and pressure gauge. Calibration source: **gap distance is the voltage** (3 kV/mm), not a hard-read meter.
3. **Sequence and control points**: connect the tube, fix pressure at 10 Pa, raise voltage step by step, record the start and end of each glow region, **check the same points with the sphere gap**, log the voltage scale. Control points: **pressure must be fixed** (glow voltage differs completely at other pressures); the gap check is not optional.
4. **Empirical parameters and calibration**: sphere gap ~3 kV/mm; **G1–G4 roughly 7–1 kV at 10 Pa fixed pressure** (empirical, re-calibrate); **glow is auxiliary observation only and since 33.5 is explicitly not an acceptance criterion** — this card gives glow a reproducible voltage scale, it does not make glow a criterion.
5. **Observations to record**: per tube — fixed pressure / gap distance and converted voltage per glow region / re-calibration date / deviation from the previous calibration.
6. **Pass / rework / scrap criteria**: pass = glow voltages agree with the gap check and deviation is within limit; rework = large deviation (impure gas or aged tube); scrap = glow regions chaotic.
7. **Common failures and diagnosis order**: (1) two calibrations far apart — pressure not held at 10 Pa; (2) no glow — wrong pressure or voltage (check the ladder table); (3) disagrees with the gap — gap spacing wrong or meter uncalibrated; (4) wrong glow colour — residual gas (back to 33-02).
8. **L1 / L2 / L3 evidence**: L1 = one tube with a glow voltage scale at 10 Pa; L2 = calibrated against a sphere gap with deviations logged; L3 = a second person re-calibrates the same tube from this card alone with matching readings.

## Master Parameter Table

| Parameter | Value | Category |
| ------------ | ------------------------------------------ | ------ |
| Water-jet aspirator limit | \~10³ Pa | Physical limit |
| Piston pump limit | 1–10 Pa | Empirical |
| Mercury displacement pump reach | 0.1–0.01 Pa; 1–4 h per tube | Empirical, needs calibration |
| Diode working lower bound | \~1 Pa | Empirical |
| Triode stable region | ≤0.1–0.01 Pa | Empirical |
| Glow range | \~1–10³ Pa (supplementary observation, not a criterion) | Fact |
| McLeod gauge compression ratio | \~10⁴; measures down to the 0.1 Pa level | Design |
| Bake-out temperature band | About 150–250 °C, 15–30 min | Empirical |
| Carbon filament cross-section | 0.2–0.5 mm square; lifetime tens of hours | Empirical |
| Demo tube vacuum recheck | No characteristic degradation at 24 h after seal-off | Criterion |
| Seal α matching | Difference <10% = matched; iron wire limited to ≤0.5 mm | Design rule |
| Pin diameter series | 1.0 / 1.5 / 2.0 mm; four-pin pitch circle 20 mm, five-pin 30 mm | Design standard |
| Socket insertion lifetime | Contact resistance ≤ 1.5× initial after 200 cycles | Criterion |
| Carbon filament 1.2-step lifetime | Around ten hours (below about 1/5 of the rated step) | Empirical, needs calibration |
| Resonance demo operating point | L≈2.5 H + C≈1 µF → f₀≈100 Hz (buzzer band) | Empirical, needs measurement |
| Glow voltage steps | Sphere gap \~3 kV/mm calibration; G1–G4 about 7–1 kV class (10 Pa fixed pressure) | Empirical, needs re-calibration |

## Failure Modes and Diagnostics

| Symptom | Candidate causes (by probability) | Verification | Disposition |
| ---------- | --------------------------- | -------------------------- | ------------------------- |
| Filament burns out as soon as it enters the tube | Rough vacuum (residual oxygen); under-carbonized and brittle | McLeod reading; carbon-filament bend test | Back to the rough pump and repump; new filament, re-carbonize |
| Pressure stops falling at some level | That pump stage's limit reached | Check the ladder table | Connect the next pump stage |
| Characteristics degrade hours after seal-off | Insufficient degassing; no getter; seal slow leak | Rise-rate method (those with a test port); spark scan | Demo track: back to pump, re-degas; sealed track: reject and re-seal |
| Diode passes current in reverse too | Vacuum insufficient (residual gas ionizing); grid/plate short | McLeod recheck; ohmmeter check with power off | Back to the mercury-pump stage; rebuild the electrodes |
| Triode grid control comes and goes | Vacuum at the critical point; poor grid contact | McLeod gauge; grid-circuit continuity | Pump longer; secure the grid wire |
| Detection point drifts | Contact oxidized / vibration displacement | Retest the rectification ratio | Reselect and lock the point; record the drift period |
| Rectification ratios all ≈1 | An old oxidized face was used; poor ore variety | Crack a fresh face and retest | Switch to a fresh cleavage face; switch ore sample |
| McLeod reads abnormally low | Condensable water-vapor interference; wrong calibration value | Retest after baking; check the calibration dossier | Re-bake; re-calibrate V₀ |
| Ring crack at the seal | α mismatch (copper wire / thick iron wire) | Magnified visual inspection + water-tank bubble method | Change materials per the seal table |
| Pin oxidation, poor contact | Insufficient contact pressure; oxide film on pin surface; insertion wear | Voltage-drop contact-resistance test; visual check of pin surface finish | Sand the pin surface + reshape contacts; replace out-of-spec contacts |
| Glow step drift | In-tube outgassing / slow leak shifting pressure; electrode sputtering changing the gap | Daily McLeod spot check; rise-rate method to distinguish leak/outgassing | Demo track: back to pump, reset pressure; trial track: reject |
| No LC resonance peak | Crank speed / reed frequency short of f₀; capacitor broken down shorted; inductor turn-to-turn short | Calculate f₀ against the reachable band; disconnect the capacitor and watch the lamp; swap parts and retest | Increase L or C to move f₀ down into the reachable band; replace bad parts |

## Process Card Index

## Acceptance Criteria

* **L1**: R/L/C three-component behavior tests reproduced; ore detection audible/readable; three-state relay-logic demo; carbon-filament air/vacuum comparison experiment completed.

* **L2**: three-stage vacuum ladder built and the **McLeod gauge criteria** passed (diode ≥1 Pa, triode ≤0.1 Pa, once each); degassing curve (rise–fall) on file; **diode volt-ampere characteristic curve archived; triode grid-control phenomenon on record (gain not an acceptance item)**; rectification-ratio comparison table ≥6 data sets; component register in operation.

* **L3**: demo-track diodes/triodes rebuildable (filament/exhaust/degas whole process locally closed-loop, lifetimes recorded item by item); the automatic pump serving one month at a real post; **fine-iron-wire transitional-seal trial-track success rate registered honestly (no target set, data only)**; laboratory three protections + mercury discipline up to standard. Evidence: exhaust dossiers, characteristic curves, rectification-ratio tables, lifetime ledgers.

## Work Hours, Personnel, and Consumables

| Item | Personnel | Hours (empirical value) |
| ---------------- | -------------------------- | ------------- |
| One batch of 10 wire-wound resistors | 1 person | 2 days |
| One batch of wax-paper capacitors | 1 person | 1 day |
| One batch of carbon filaments (carbonizing included) | 1 person | 1 day |
| McLeod gauge making and calibration | 2 people (1 lampworking, 1 calibrating) | 3–5 days |
| Mercury displacement pump build | 2 people | 5–8 days |
| One demo tube, whole process (exhaust, degas, experiment) | 2 people | 1–2 days (the mercury-pump stage takes most of it) |
| Consumables | Per tube: glass stock, carbon filaments, mercury loss 5–20 g (into the poison ledger) | Entered in the Chapter 42/53 ledgers |

## Safety Boundary

* **Vacuum tube shattering/implosion**: goggles during heating and sealing + face turned aside; wrap test tubes in cloth mesh;

* **Mercury red line (Iron Law Seven)**: mercury work confined to shallow-tray zones; spilled mercury covered immediately with sulfur powder and collected; mercury vapor is odorless and imperceptible — ventilation and sealed storage are institution, not suggestion; long-term mercury workers follow the Chapter 49 occupational-exposure registration and medical checks;

* High-voltage capacitors hold charge after power-off — discharge with a discharge rod first; spark-coil tests with two people present;

* Red phosphorus / magnesium-powder getters stored away from open flame; white phosphorus not implemented (Chapter 26 red line);

* RF and high-voltage tests under the two-person rule; no food, drink, or smoking in the electronics laboratory.

## A. Existing Tool Inventory

Power supplies and meters (Chapters 31–32); glass lampworking and tube pulling (Chapters 14, 26); annealed glass tubing and bulb blanks (Chapter 14); carbonization furnace (Chapters 6, 12); ore identification (Chapter 16); mechanisms and fine adjustment (Chapters 21, 27); chemical glassware (Chapter 26); mercury barometer technique (Chapter 25).

## B. New Tools This Chapter

Three-stage vacuum ladder (water-jet aspirator + piston pump + **mercury displacement pump**); **McLeod vacuum gauge and criteria institution** (glow demoted to supplementary); spark leak detector and local color–pressure reference table; pressure rise-rate leak/outgassing discrimination method; **carbon-filament cathode preparation**; **seal dual-track system** (demo track, pump never stopped + fine-iron-wire transitional-seal trial track); **degassing (bake-out) protocol**; **getter external-activation method**; diode volt-ampere characteristic recording; triode grid-control phenomenon recording (no gain acceptance); **ore-detector point-selection protocol and rectification-ratio comparison registry table**; negative-resistance observation interference-elimination protocol; **R/L/C AC behavior comparison table and LC resonance demo**; **carbon-filament lifetime–voltage measurement table and end-of-life precursor criterion**; **tube socket and pin series standard (four-pin/five-pin, anti-reverse-insertion keying, insertion-cycle lifetime ledger)**; **glow voltage step calibration table and prototype voltage-test pen**; electronics laboratory (three protections + mercury discipline + component register + rectification-ratio archive).

## C. Unresolved Dependencies

**Matched seal wire (platinum or Dumet type) — the first external dependency for sealed long-life tubes**; mercury vapor diffusion pump (faster high vacuum; challenge item); high-purity semiconductor materials (Chapter 34); AC and high-frequency measurement (RF challenge); oxide cathodes and better filaments (metallurgy line, far term); tungsten filament (Master Plan exclusion table).

## Next-Step Dependencies

Chapter 34: the rectification-ratio archive and the negative-resistance observation register are the firsthand motivation for "why purify"; the McLeod gauge and mercury pump directly serve zone refining and vacuum sintering. Chapter 35: the vacuum ladder is the foundation for sputtering/evaporation coating and sealing processes. Chapter 36: production-lining = this chapter's laboratory × institution. The Part 10 environment editions: radio/detection communication is the shared base for liaison and rescue. Chapter 49: toxic-substance registration and occupational-exposure dossiers for mercury work.
