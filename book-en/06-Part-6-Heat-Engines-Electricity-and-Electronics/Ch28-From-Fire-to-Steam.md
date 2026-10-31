# Chapter 28 From Fire to Steam

## Chapter Objectives

Build heat-engine capability: understand the heat–pressure–work conversion chain, master the key properties of water vapor, and build **the first low-risk atmospheric (Newcomen-type) steam engine** (the Newcomen route—it tolerates coarse tolerances and is the bootstrap entry point), while giving an upgrade route toward Watt-style improvements.

**The first lesson of this chapter is safety, not efficiency**: the energy stored in a steam system can kill instantly. Early experiments use only low-pressure demonstration devices; never perform high-pressure experiments with unverified homemade vessels.

## Capability Boundary

**Can do:** an atmospheric (Newcomen-type) steam engine (boiler at gauge pressure near zero) running self-sustained while driving a pump; riveted boilers released after a two-times hydrostatic test; quantitative safety-valve setting.

**Explicitly cannot do:** high-pressure steam (the four unlock conditions are in Section 28.8; until all four are met it remains "knowing ≠ being able to build"); the separate condenser and slide valve (Watt-style; depends on precision boring and valve-machining upgrades; preliminary study and unlock conditions in Section 28.14); locomotive and marine use and high-speed rotation (requires a governor).

**External dependency:** dedicated stokers (Iron Law 7: continuous-process watches are staffed by two people)—**without an established stoker corps, the steam engine must not be fired**.

## Pre-Start Verification (check off item by item)

| # | Verification item | Criterion | Source |
|---|---|---|---|
| 1 | Riveting and brazing | A vertical test shell (300 mm class) passes a 2-times hydrostatic test with no leakage | Chapters 17 and 20 |
| 2 | Cylinder boring | Trial-bored bore: three-point-method roundness ≤0.1 mm, taper ≤0.2 mm/300 mm | Chapter 20 |
| 3 | Thermometer/pressure gauge/water gauge | All three gauges carry the Chapter 27 release slip (with calibration records) | Chapters 25 and 27 |
| 4 | Sealing materials | Grease-soaked hemp rope, leather cups, and graphite grease stocked for ≥2 shifts | Chapters 15 and 23 |
| 5 | Crank, connecting rod, and bearings | Chapter 21 shafting passes no-load running with acceptable temperature rise (≤60 ℃) | Chapter 21 |
| 6 | Safety-valve setting calculation | Lifting-pressure formula and weight value written on the process card | Section 28.4 of this chapter |
| 7 | Stoker corps | 2 people pass the training assessment (start/stop, water-level red line, burn treatment) | Iron Law 7 |
| 8 | Pressure-relief and fire-withdrawal tools | Long-handled fire hook, relief valve, and wooden probe rod in place | This chapter |

---

### 28.1 Heat, Temperature, Pressure, and Work

- Heat (energy) → temperature (intensity) → pressure (the push of a confined gas when heated) → work (pressure driving a piston): the four-step heat-engine chain;
- **High temperature does not mean high energy** (a blazing furnace holds far more energy than a red-hot iron nail);
- Quantifying work (continuing from Chapter 25): pressure × area = force; force × displacement = work. On a 30 cm cylinder diameter (area about 700 cm²), a pressure difference of just one atmosphere produces roughly 700 kg of thrust—**low pressure does not mean small force**; this is the physical reason the atmospheric route is viable, and also the other face of its danger;
- Efficiency concept: atmospheric engines are on the order of <1% (empirical value). This chapter first targets the milestone of "stable mechanical power output," not efficiency.

### 28.2 Boiling of Water and the Properties of Steam

Experimental sequence (demonstration level, open and semi-open vessels):
1. Heating an open pot: bubbles form at the bottom, rise, and burst—the atmospheric-pressure boiling point is the thermometer's 100-degree point (reusing the Chapter 25 calibration);
2. Cover with a ceramic lid leaving a small hole: the escaping steam can spin a pinwheel—steam carries kinetic energy;
3. Condensing steam back into water collapses its volume—**steam occupies on the order of a thousand times the volume of the same mass of water**; condensation is "volume collapse," and this is the driving principle of the atmospheric engine;
4. Closed-vessel demonstration (dedicated thick-walled small vessel + relief valve; **for the demonstration rig only, do not scale up**): the pressure gauge rises on heating, and the temperature–pressure relationship is recorded as a table;
5. Steam-burn demonstration (safety lesson): steam condenses instantly on cool skin and releases heat—**a steam burn is worse than a burn from hot water at the same temperature**; operating procedures are set accordingly.

### 28.3 Why Steam Can Drive Machinery

Two routes for extracting work, with entirely different safety levels:
- **High-pressure route** (steam pushes the piston directly): efficient, but demands pressure vessels and precise control—**not done in this chapter**;
- **Atmospheric route** (the Newcomen idea): after the cylinder fills with steam, cold water is sprayed in to condense it, leaving a near vacuum in the cylinder—**it is the pressure of the atmosphere that pushes the piston down**. The boiler only needs to produce steam slightly above atmospheric, minimizing vessel risk. History shows this route runs even with cylinder tolerances at the millimeter level.

### 28.4 Basic Structure and Risks of Pressure Vessels

#### 28.4.1 Structural and Material Discipline

- **Three structural elements**: cylindrical shell (best load-bearing shape), torispherical/flat heads (a flat head must be much thicker + stays), riveted seams in double staggered rows + caulking (**pressure sealing relies on riveting and caulking; tin brazing serves only as auxiliary external anti-rust protection, never as a pressure seal**—tin solder has a low melting point and low strength);
- **Material discipline**: copper/bronze preferred (good ductility, controllable corrosion); iron plate forged and joined is usable but joint-seam inspection is strict; **cast iron is never used for pressure shells** (brittle; shatters without warning).

#### 28.4.2 Riveted-Seam Caulking (the key leak-prevention technique, ◎)

Whether a riveted seam leaks is decided not by a layer of brazing but by **caulking**: after riveting, use a round-nose caulking chisel at about a 45° angle along the outer edge of the lap seam, tapping and working the metal lightly—one set, one advance, force even and slow—working the lapped edges into a tight, continuous line. Key points:
- The chisel edge is rounded and blunt (working, not cutting); hammer blows are light (listen for a "dull thud," not a "sharp ring"—a sharp ring means you are cutting metal, which is wrong);
- Work along the seam twice: the first pass at 45° working the outer edge, the second pass vertical to lightly close the seam; finish by smoothing with an oilstone;
- **Do not caulk the inner seam** (caulking the outer edge already presses the lap faces together);
- Practice method: practice a 500 mm seam on scrap plate, then run a hydrostatic test and compare leak-point counts—when leaks go from "a line of beads" to "isolated spots," you have graduated.

[Card 28-05 Riveted-Seam Caulking] (eight fields)

1. **Input materials**: a riveted lap seam (double row, staggered, 28.4.1); plate stock (copper/bronze preferred, wrought iron acceptable); **no filler** — the pressure-tight seal comes from riveting plus caulking, while tin brazing serves only as external anti-corrosion, never as the pressure seal.
2. **Tools required**: round-nose caulking chisel (blunt, rounded edge — working, not cutting); light hammer; oilstone (finish smoothing); chalk (circling leak points); the hydrostatic-test set (28-01); scrap plate practice piece (500 mm seam).
3. **Operation sequence and control points**: (1) start working at 45° along the outer edge of the lap seam, one set and one advance, force even and slow → (2) first pass at 45° working the outer edge along the whole seam → (3) second pass vertical, lightly closing the seam → (4) smooth with the oilstone → (5) hydrostatic test for leaks (full 28-01 procedure). Control points: **never caulk the inner seam** (working the outer edge already presses the lap faces together; caulking inside pries the seam open); judge the force by sound — a "dull thud" is right, a "sharp ring" means you are cutting metal, so stop and ease off at once.
4. **Empirical parameters and calibration**: working angle about 45°; two passes (45° outer working + vertical closing); the practice baseline is a 500 mm scrap seam (1 person, 1 day); the graduation criterion is leak points falling from "a line of beads" to "isolated spots" (empirical, calibrate to local plate stock and rivet pitch).
5. **In-process observation items**: for each seam record plate thickness / rivet pitch / hand-feel of the working angle / number of passes / smoothing result / leak-point positions and counts from the hydrostatic test (mid-seam = caulking failed; around rivets = rivet holes stretched; concentrated in one spot = plate defect).
6. **Pass / rework / scrap criteria**: pass = 2× pressure for 30 min with no leakage; rework = ≤3 leak points → after caulking repair, **repeat the entire procedure** (a partial re-test of only the patched spot is forbidden); scrap = leaks forming a line, visible plate deformation, or a dull sound when tapped — repairs forbidden, scrap it outright.
7. **Common failures and troubleshooting order**: (1) a line of leaks along mid-seam → working angle too shallow or blows too light (work the whole seam again, correcting by sound); (2) leaks around rivets → rivets not expanded tight (re-rivet; caulking does not substitute for riveting); (3) the more you caulk the more it leaks → the chisel edge has gone blunt and is cutting metal (round the edge, ease the force); (4) still leaking after repair → a defect in the plate itself (replace the plate; no repeated caulking).
8. **L1 / L2 / L3 evidence**: L1 = a 500 mm practice seam brought from "a line of beads" to "isolated spots"; L2 = one vessel's full seam caulked and passing the 2× hydrostatic test; L3 = the caulking parameters (angle / passes / hammer weight) on file and reproducible by a second person from this card.

#### 28.4.3 Safety Valve: Quantitative Setting (the worked example is mandatory—no guesswork)

**Simplest form (recommended for the first generation): the direct-weight valve**. The weight presses directly on top of the valve stem—structure is transparent, nothing can be fudged, and the calculation is one line:

> Lifting pressure (gauge) = (weight + self-weight of valve plug and stem) ÷ valve-seat area—verify by measurement after assembly and lead-seal

Worked example: valve seat diameter 20 mm → area = π×1² = 3.14 cm²; target lifting gauge pressure 0.5 kgf/cm² (about half an atmosphere) → weight = 0.5×3.14 ≈ **1.6 kg**. Check: a 1.6 kg weight holds the plug down; when the vessel's gauge pressure reaches 0.5 it just lifts open—there is not a bit of safety margin to spare, so **the weight gets a lead seal, is kept by a designated person, and no one may ever add weight to the valve** (adding weight to a valve turns a safety valve into a bomb—the first direct cause of boiler explosions in history).

**Lever type (for later use)**: lifting pressure = W×L₂÷(L₁×A) (W = weight force, L₂ = weight arm, L₁ = valve arm, A = valve-seat area). Every time the weight position is moved, recalculate and log it.

**Action test**: after each valve is set, perform a live popping test—raise pressure slowly to the set value; the valve should pop open automatically to vent steam, and reseat automatically as pressure falls. Lift the valve manually once a week to test popping (to prevent the plug from sticking).

[Card 28-04 Safety-Valve Setting and Live Popping] (eight fields)

1. **Input materials**: safety valve (direct-weight type for the first generation, lever type later); weight sized by the formula, cast iron or lead, drillable for the lead seal; valve plug and stem; valve seat of known diameter, measured and entered in the register.
2. **Tools required**: calipers or bore gauge (seat diameter); balance or weights (to verify the weight's actual mass — the weight counts as weighed, not as marked); pressure gauge (Chapter 27-calibrated, range covering the set pressure); hand pump (the 28-01 set); lead-seal press and pellets; white paint and scriber; the register.
3. **Operation sequence and control points**: (1) measure the seat diameter → compute the area → solve lifting pressure = (weight + self-weight of plug and stem) ÷ seat area for the weight → (2) weigh the weight on the balance (plug and stem self-weight included) → (3) assemble → (4) **first verification (measured check)**: raise pressure slowly to the lift point and read the actual popping pressure → (5) compare against the formula; if they agree, lead-seal, assign a custodian, register → (6) **second verification (live popping test)**: raise pressure to the set value; the valve must pop open on its own to vent steam and reseat itself as pressure falls, with both popping and reseating pressures read and recorded → (7) lift the valve by hand once a week to test popping (prevents the plug sticking) and register it. Control points: **calculated but never popped means not set** (a correct formula alone does not pass); once lead-sealed the weight is untouchable, and nobody may ever add weight to the valve.
4. **Empirical parameters and calibration**: worked example — 20 mm seat → area 3.14 cm²; gauge pressure 0.5 kgf/cm² → weight 1.6 kg (a worked example of the formula, not a recommended setting; the set value comes from the boiler design pressure, per 28.10.1 "design pressure = safety-valve setting"); lever type: lifting pressure = W×L₂÷(L₁×A), recalculated and registered every time the weight position moves; the allowed deviation of the measured check is limited to the smallest division of the gauge in use (the gauge must be within its Chapter 27 release slip); calibration method = formula — weighing — measurement — lead seal, the measured value entered in that vessel's file, recalibrated on any valve or weight change.
5. **In-process observation items**: measured seat diameter, weighed mass of the weight (plug and stem included), formula result, measured popping pressure, reseating pressure, whether the gauge needle rose in one sweep without trembling, lead-seal number, date of the next weekly test.
6. **Pass / rework / scrap criteria (two steps; neither alone passes)**: step one, "setting passed" = formula on file + weighed mass on file + measured popping pressure agreeing with the calculated value (deviation within the gauge's smallest division); step two, "live popping passed" = pressure raised to the set value, the valve pops open on its own to vent, reseats itself as pressure falls, and both readings agree with the set value. Rework = measurement off → re-weight, recompute, re-pop (no "close enough, use it"); no reseat after popping or a stuck plug → strip, inspect and lap plug and seat, then repeat the whole setting-and-popping procedure; scrap = pitting on the seat or plug cone, a bent guide stem, or a deliberately broken lead seal → replace the valve and trace who broke the seal.
7. **Common failures and troubleshooting order**: (1) leaking before reaching the set pressure (poor plug-seat lapping or weight too light) → re-lap and verify the weight; (2) no pop at the set pressure (stuck plug, binding guide, something loaded on the weight) → lift by hand, strip and inspect; (3) no reseat after popping (scale on the seat, bent guide stem) → clean, straighten or replace; (4) popping pressure falling week by week (weight moved, seal broken) → check the seal and the custodian's records.
8. **L1 / L2 / L3 evidence**: L1 = one valve with formula + measured check + one live pop, all three on file; L2 = setting cards complete for every valve in service and continuous weekly-test records; L3 = a quarter of weekly tests with no gaps and no seal broken, and the boiler design pressure matching the setting (28.10.1).

#### 28.4.4 Complete Hydrostatic Test Procedure (release ceremony; one vessel, one file)

[Card 28-01 Hydrostatic Test] (eight fields)

1. **Input materials**: vessel awaiting release (riveting + caulking + brazing complete); working pressure value (in writing); test pressure = 2 times working pressure
2. **Tools required**: hand pump (lever-actuated piston pump + check valve, Chapters 12/20 technique); pressure gauge (range ≥ test pressure, calibrated); chalk (for marking leak points); wooden mallet
3. **Operation sequence and control points**: ① fill the vessel with water and **purge all air** (vent at the top until water shows, then close)—trapped air is a stored-energy bomb; the test is invalid and dangerous → ② raise pressure in stages: 1/2 → 1 → 1.5 → 2 times working pressure, **hold 10 min at each stage** (pump idle during the hold; any pressure drop means a leak) → ③ inspect at each stage: watch for leak beads section by section along the riveted seams, caulked seams, brazed seams, and valve seats; circle them with chalk → ④ hold at the 2-times stage for 30 min: no leakage, no visible deformation, no pressure drop; **no hammering or tightening of any kind during the hold** → ⑤ after venting to below working pressure, tap lightly along the seam zones with a soft-faced hammer (keep personnel out of the tapping direction; set up an exclusion zone) → ⑥ depressurize and drain (open the relief slowly; fast opening forbidden) → ⑦ fill out the release record (test date / stage pressures / leak-point count / corrective action / conclusion), **stamp the lead-seal mark**
4. **Empirical parameters and calibration**: pressure gauge calibrated by the Chapter 27 deadweight method; water at ambient temperature (warm water accelerates leak appearance, optional)
5. **In-process observation items**: distribution of leak beads (mid-seam = caulking failed; around rivets = rivet holes stretched; concentrated in one spot = plate defect)
6. **Pass / rework / scrap criteria**: pass = 2-times pressure for 30 min with no leakage and no deformation. Rework = ≤3 leak points → after caulking repair, **repeat the entire procedure** (a partial re-test of only the patched spot is forbidden). Scrap = leaks forming a line, visible deformation, or a dull sound when tapped—repairs forbidden, scrap it outright
7. **Common failures and troubleshooting order**: (1) pressure will not rise = pump check valve leaking or a large vessel leak (check the pump first); (2) fast pressure drop = large leak (depressurize at once and investigate); (3) gauge needle trembling = residual air not fully purged; (4) a dull sound when tapped = plate defect (no repairs, scrap outright per item 6)
8. **L1 / L2 / L3 evidence**: L1 one test shell passes; L2 release files complete for every vessel; L3 the release system and lead-seal system in operation

**After every repair (rivet replacement, caulking touch-up, valve replacement) the entire procedure must be repeated.**

### 28.5 Piston, Cylinder, and Crank Mechanism

- **Cylinder**: bronze or cast-iron cylinder body blank (hole pre-formed on a clay core, leaving 3–5 mm boring allowance), bored (Chapter 20 boring-bar route) until roundness/taper meet targets (checked by the three-point method); typical bore 25–40 cm, stroke 60–100 cm class (empirical values).

#### 28.5.1 Cylinder-Wall Honing (mandatory after boring, ◎ hand-feel)

The tool marks left by boring are longitudinal grooves; seals leak steam and water along them. **Honing = applying a "rotation + reciprocation" compound motion to the cylinder wall with honing stones, replacing the tool marks with a uniform cross-hatch pattern**:

- Tools: honing bar (converted from a boring bar)—the bar carries 2–4 oilstones (fine grade from Chapter 9, expanded tight against the wall with wooden wedges); the bar rotates (hand crank or bow string) + reciprocates (one person pushing and pulling);
- **Cross-hatch angle criterion**: the crossing marks form 30°–60° with the cylinder axis (target about 45°)—determined by the ratio of rotation speed to reciprocation speed: fast reciprocation makes the pattern steep, fast rotation makes it flat. ◎ Hand-feel practice: hone a section of scrap cylinder and look at the pattern—"a clear diamond grid, a fine gritty drag under the fingertip but it does not catch the fingernail" means it is right;
- What the pattern does: the crossing grooves hold oil and grease so the piston seals bed in and conform—**a cylinder without cross-hatch either polishes bright and seizes, or leaks steam past the piston and has no power**;
- Final inspection: the wall shows a uniform fine cross pattern to the eye, no bright patches (a bright patch = honing missed that spot; it will surely leak), no deep scratches; roundness re-checked by the three-point method unchanged.

[Card 28-02 Cylinder Boring and Honing] (eight fields)

1. **Input materials**: cylinder body with the hole pre-formed on a clay core (leaving 3–5 mm boring allowance); saponified oil-water coolant; rubbing paper and charcoal stick.
2. **Tools required**: boring bar with dual supports (Chapter 20), bore gauge (for the three-point method); honing bar (converted boring bar) + 2–4 oilstones (Chapter 9 fine grade) + wooden wedges to expand them; hand crank or bow string (rotation), one person to push and pull; calipers.
3. **Operation sequence and control points**: bore — dual supports synchronized, measure after every pass, until roundness/taper are met → hone — rotation + reciprocation compound motion, converting the longitudinal tool marks into a uniform cross-hatch → final inspection (visual pattern + three-point re-measurement). Control points: **coolant throughout honing (saponified oil-water)** — dry honing embeds grit in the wall and heat-distorts it; the pattern is judged visually against the 45° crossing criterion.
4. **Empirical parameters and calibration**: bore 25–40 cm, stroke 60–100 cm class (empirical); boring allowance 3–5 mm; pattern angle 30°–60°, target about 45° (empirical, calibrated by the ratio of rotation speed to reciprocation speed: fast reciprocation makes the pattern steep, fast rotation makes it flat); hand-feel calibration = hone one section of scrap cylinder — "a clear diamond grid, a fine gritty drag under the fingertip that does not catch the fingernail" is right; roundness ≤0.1 mm, taper ≤0.2 mm/300 mm.
5. **In-process observation items**: chip form (boring); pattern direction and brightness (honing); location of bright patches; three-point roundness/taper readings; coolant concentration and flow.
6. **Pass / rework / scrap criteria**: pass = roundness ≤0.1 mm, taper ≤0.2 mm/300 mm, uniform cross-hatch with no bright patches; rework = re-hone localized bright patches; scrap = bore misaligned (axis tilted — rescue by scraping the bearing seats, or scrap).
7. **Common failures and troubleshooting order**: (1) bright patches (honing missed that spot; it will surely leak) → re-hone; (2) gouges and scuffing → grit not washed off or dry honing (change the coolant, rewash); (3) taper out of limit → boring-bar supports not synchronized (realign the supports and rebore); (4) roundness out of limit → bore misaligned (check per the 20.6 boring card; scrape or scrap).
8. **L1 / L2 / L3 evidence**: L1 = three-point records for one cylinder body; L2 = three-point records + wall rubbing on file; L3 = three consecutive cylinders comparable on roundness / taper / pattern, and a second person reading the pattern angle from this card alone reaches the same conclusion (rubbings are awkward to compare in the archive, so the pattern angle is recorded as a written visual conclusion).

- **Piston**: cast-iron or hardwood piston body, turned on its outer circle 3–5 mm smaller than the bore; **the gap is filled by sealing** (Section 28.6); the piston rod is forged steel, connecting to the beam (atmospheric engine) or to a crosshead and connecting rod (upgraded engine).
- **Steam distribution**: minimal on the atmospheric engine—the steam inlet valve and the water-injection valve are actuated automatically in sequence by the **valve-gear rod linkage** (the piston rod, through levers, opens and closes them); no slide valve.

### 28.6 Sealing, Lubrication, and Friction Control

- **Piston sealing**: grease-soaked hemp rope or leather cups packed into the piston grooves, pressed outward against the wall by compression rings (wedges or spring-steel rings)—seals are consumables; keep spares on hand;
- **Valve sealing**: conical valves (the plug cone lapped to its seat, Chapter 20 lapping); leak check: with the valve closed, the pressure gauge must not keep falling;
- **Rod sealing**: a stuffing box (a gland compressing grease-soaked hemp rope around the piston rod)—tightness is set to "slight seepage for lubrication, no dripping loss" (◎: a seepage rate of a few drops per minute is the standard; calibration method: compare stroke efficiency against rod temperature);
- Lubrication: the cylinder wall self-lubricates, kept slightly wet by the injection water; main bearings follow the Chapter 21 regime; high-temperature points use graphite grease (Chapter 23)—**grease washing away under heat** is the biggest difference between steam-engine lubrication and that of ordinary machinery.

### 28.7 Working Principle of the Early Steam Engine (complete atmospheric engine)

**Figure 28-1 Atmospheric (Newcomen-type) steam engine (schematic section)**

```
        Chimney                Beam (lever)
         │                ┌────△────┐
      ┌──┴───┐            │         │
      │ Boiler│≈≈ steam pipe ═══╡ Cylinder │      Pump rod
      │ ▓▓▓▓ │   steam valve→  │ ┆Piston┆  │       │
      │ ▓Fire▓│  water valve→  │ ↓spray-condense↑ │      ▼
      └──────┘            │(vacuum pulls down)│    [well/pump]
       Firebox             └─────────┘
  Cycle: steam fill (piston up) → water-spray condensation (vacuum in cylinder) → atmospheric pressure pushes the piston down, doing work → exhaust
```


Building and verifying the work cycle step by step:
1. The boiler makes steam (low pressure; gauge pressure near zero suffices) → open the steam valve; steam fills the cylinder and the piston rises (assisted by its own weight and the counterweight);
2. When the steam has filled, close the valve and **open the water-injection valve**: cold water sprays in, the steam collapses instantly, near vacuum forms in the cylinder—atmospheric pressure pushes the piston down: the power stroke;
3. The rod linkage completes the valve switching for the next cycle—self-sustained running;
4. Power output: the piston rod connects to one end of the beam (lever), the other end to the pump rod—**naturally suited to pumping water** (mine drainage was its first historical use).

[Card 28-03 First Start-Up and Loading] (eight fields)

1. **Input materials**: boiler and cylinder that passed the 2× hydrostatic test (release files on record); safety valve set and live-popped; all three gauges present (thermometer / pressure gauge / water-level gauge, Chapter 27 release slip).
2. **Tools required**: the Chapter 25 flow-method measuring gear and record sheets; long fire hook, relief valve, wooden probe rod (pre-work check item 8); shutdown tag-out kit; listening rod (for steam blow-by and knocking in the cylinder).
3. **Operation sequence and control points**: (1) trial-run unloaded, no load connected → (2) after several dozen cycles, stop and inspect: seal temperature rise, packing seepage rate, sweating of the riveted seams (any sweating = stop, recheck the caulking) → (3) load gradually (half pump stroke first, then full pump stroke) → (4) record parameters. Control points: **hold boiler gauge pressure near zero (≈0–0.2 kgf/cm²)** — the urge to "stoke it a bit harder" already belongs to the high-pressure route, which is out of bounds; raise the load one step at a time, checking the three items of step (2) before every step up.
4. **Empirical parameters and calibration**: injection quantity is the first lever of efficiency — too much condenses thoroughly but leaves the cylinder too cold, too little leaves steam uncondensed and the stroke weak; adjust the injection-valve opening against the twin indicators of stroke count and water output, **15 min per setting**; the accepted setting holds stroke-count fluctuation <±10% (empirical, enter in the machine's file after calibration); running consumption on the order of 2–4 m³ of injection water per shift (empirical order of magnitude).
5. **In-process observation items**: strokes per minute, stroke length, pumped water output (Chapter 25 flow method), coal/wood consumption, injection-water quantity; speed uniformity through the whole stroke (weak mid-stroke = incomplete condensation); color of the steam at the exhaust port; packing seepage rate (drops per minute).
6. **Pass / rework / scrap criteria**: pass = self-sustained running for a full consecutive shift with stroke-count fluctuation <±10%; rework = handle per the Section 28.9 table and re-run step (1) of this card; scrap = any riveted-seam leakage after the hydrostatic test (retire the unit, re-release it).
7. **Common failures and troubleshooting order**: (1) weak stroke → adjust the injection quantity first (gradient trial), then check piston-seal wear; (2) stroke stops mid-way → valve-gear phasing off, then water in the cylinder; (3) knocking at the first start-up → water hammer (water not drained from the cylinder; put the drain procedure first); (4) seam sweating or beading → caulking failed (stop and repeat the hydrostatic test).
8. **L1 / L2 / L3 evidence**: L1 = ≥50 unloaded cycles; L2 = a full-shift log with the pump running; L3 = a quarter's service records under real load.

### 28.8 From Low-Efficiency Prototype to Stable Power Source

- Main causes of low efficiency and their fixes (ordered by impact): ① the cylinder is chilled by injection water every cycle and reheated by steam—the **separate condenser** (Watt's improvement) is the fundamental fix: move condensation outside the cylinder and keep the cylinder hot; ② throttling loss at the steam inlet; ③ friction (add knife-edge bearings to the beam pin shafts);
- Route to more power: enlarging the stroke is more stable than enlarging the bore (force area grows quadratically and boiler demands climb steeply); evaluate multi-cylinder paralleling together with boiler upsizing—**every scale-up step must first clear the hydrostatic test and the instrument release slip** (Chapter 27);
- **High-pressure route unlock conditions (registered; not implemented in this chapter)**: ① uniformly repeatable plate stock; ② safety valves reliable in continuous operation; ③ pressure-gauge accuracy and range; ④ a dedicated stoker system. Until all four conditions are met, high-pressure steam remains "knowing ≠ being able to build" (a living example of the Chapter 1 three levels).

### 28.9 Steam-Engine Maintenance, Troubleshooting, and Safety

**Daily inspection sheet**: water level (communicating-vessel water gauge) twice per shift; pressure-gauge readings and safety-valve status; packing seepage rate; bearing temperature (hand-touch limit as in Chapter 21, compensated with wax strips).

**Troubleshooting table**:

| Symptom | First check | Second check |
|---|---|---|
| Weak stroke | Insufficient injection water (incomplete condensation) | Piston seal wear |
| Stroke stops midway | Valve-gear timing out of position | Water accumulated in the cylinder (drain valve blocked) |
| Boiler pressure rising too fast | Fire too fierce (withdraw the fire) | Steam-consuming side has shut off (open the relief immediately) |
| Abnormal knocking | Water hammer (water in the cylinder) | Bearing clearance |
| Cylinder wall sweating / leak beads | Riveted-seam caulking failure | Stop the engine and redo the hydrostatic test |

**Safety Iron Laws**: ① before any maintenance—withdraw the fire, vent pressure to gauge zero, and tag out; ② never tighten pressure-bearing parts while running; ③ trace steam leaks with a wooden probe rod (hands never enter the steam flow); ④ stokers are trained full-time and watch in pairs; ⑤ lift the safety valve manually once a week to test popping.

### 28.10 Boiler Detailed Design: Wall Thickness, Stays, Access Openings, and Blowdown Valve

Section 28.4 covered vessel discipline and test release; this section covers the four things still missing to turn that into "a boiler that can serve": how to set wall thickness, how to stay a flat head, how people get inside for inspection, and how scale is drained out. Missing any one of them, a demonstration boiler never becomes a service boiler.

#### 28.10.1 Empirical Shell Wall-Thickness Formula (the worked example is mandatory)

> Circumferential wall thickness (cm) = design gauge pressure × shell inner diameter ÷ (2 × allowable stress × riveted-seam efficiency e). **[σ] is already an allowable value (safety margin included); do not multiply by another safety factor**; take riveted-seam efficiency e as 0.5–0.7. Worked example: 0.5×60÷(2×200×0.6) ≈ 0.13 cm → **take 6 mm per the riveting process floor**; if diameter or pressure doubles, recalculate with the formula

Three disciplines on value selection—miss one and the formula becomes guesswork:

- **Take design pressure as the safety-valve set value, not the normal operating value**—if it runs at 0.2 and the valve is set at 0.5, calculate with 0.5. Reason: wall thickness must match the protective valve; when overpressure occurs the valve pops first, so the vessel is designed for "the instant before the valve fails";
- Take allowable stress as 1/8–1/10 of the material's tensile strength: annealed copper plate at **200 kgf/cm²**, wrought-iron plate at **300 kgf/cm²** (conservative empirical values; when possible, verify with tensile tests on test bars per Chapters 19/18);
- **The safety factor of 8 is already folded into the riveted-seam reduction** (single-riveted lap-seam efficiency 0.5–0.7, empirical)—do not divide by seam efficiency a second time; double-counting is forbidden.

Worked example (60 cm inner-diameter copper boiler): design pressure 0.5 × inner diameter 60 × safety factor 8 ÷ allowable 200 = 1.2 cm, i.e. **12 mm**. Order-of-magnitude check: drilling and cold-riveting 12 mm copper plate is feasible (rivets ≤16 mm are the hand-process ceiling, Chapter 17)—passes. Same parameters in wrought-iron plate: 0.5×60×8÷300 ≈ **8 mm**. **Process floor: no matter how small the formula result, a riveted shell is never thinner than 6 mm**—too thin and it deforms as you drill and will not hold a caulked seam; the heads and the manhole/handhole opening-frame zones take 50% more again.

#### 28.10.2 Flat-Head Staying (stay-bolt arrangement)

A flat head bulges most easily under pressure. Two options: thicken the whole plate (≥2.5 times shell wall thickness; wasteful and hard to rivet) or **flat head + stay bolts (recommended)**:

- Stay bolts: wrought iron, diameter **≥22 mm**, threaded at both ends; after passing through the head, clamped with double nuts inside and out plus washers; the annular gap between bolt and head hole is packed with a lead ring or grease-soaked hemp, doubling as the seal;
- Layout criterion: **bolt spacing in a grid ≤30 cm** (with too much spacing, the middle of the plate bulges and blisters during operation—visible); the outermost ring sits 8–10 cm from the shell wall;
- Quantity worked example: a 60 cm flat head has an area of about 2830 cm²; at ≤500 cm² carried per bolt → **6 bolts** (1 center + 5 inner ring). Load check: at 0.5 gauge pressure the total thrust on the head is about 1400 kgf, about 235 kgf per bolt; the net section at the thread root of a 22 mm bolt is about 2.8 cm², stress about 84 kgf/cm²; against the 400 kgf/cm² allowable for wrought iron that is a margin of over 4 times—passes;
- Observable criterion: **paint a white index line across each outer nut face**—if the line misaligns during operation, a stay bolt has loosened or the head plate has deformed; stop immediately and inspect (this is the staying's "instrument," at no cost).

#### 28.10.3 Manholes and Handholes (access openings + gaskets + covers)

Scale inspection, descaling, and internal inspection of the riveted seams all require a hand to fit inside (Section 28.11 depends on this item):

- **Manhole** (elliptical 400×300 mm): fitted only on boilers with shell inner diameter ≥800 mm—a manhole on a small boiler is just a big weak point; the opening frame is a riveted raised pad with frame plate 1.5 times the shell thickness; the cover plate is 1.5 times the shell thickness, clamped by two bridge bars and four stud bolts;
- **Handhole** (80×60 mm rounded-rectangle opening): at least 1 per 1 m² of heating surface, placed in the sediment zone at the lower shell and at the head center, one each; the cover is pressed by four single-end bolts;
- **Gaskets**: on the steam side use only asbestos rope / grease-soaked asbestos sheet (soft lead sheet gaskets cost more but seal more reliably, and may be substituted); **ordinary rubber gaskets are allowed only on the cold-water side**—above 80 ℃ they age, harden, and fail (empirical value);
- Criterion: during the hydrostatic test (28-01), the manhole and handhole gasket seats show no leak beads, checked together with the riveted seams; every opening and closing of an access opening is **logged into that vessel's file**—"opened but not re-tightened" is one of the most common dumb errors in boiler accidents, and logging is what blocks it.

#### 28.10.4 Blowdown Valve (bottom blowdown against scale)

- Location: the lowest point of the shell, outlet about 5 mm below the bottom plate with a shallow scale-settling pocket; bore **≥25 mm** (scale sludge must be able to leave with the water; anything narrower clogs);
- **Two valves in series**: the valve near the boiler is the master valve (usually open, rarely operated, to prevent erosion failure); the far valve is the operating valve (the only one used for every opening and closing)—erosion wear concentrates on the far valve, which can be replaced any time the unit is stopped, while the master valve moves only during maintenance;
- The blowdown line runs from after the operating valve straight to the drain ditch, **with no steam or water branch connections permitted anywhere along it** (to prevent mis-connection and mistaken opening); the outlet is routed to an unoccupied area, pipe mouth fixed pointing down—the discharged steam-water mixture exceeds 100 ℃, and the pipe mouth is exactly where scald accidents happen;
- Tight-shutoff criterion: after closing, the blowdown pipe mouth is silent—no steam sound, no water sound—and still dry after 1 min. The blowdown regime (how much, when) is in Section 28.11.4.

### 28.11 Feedwater and Water Treatment (silent-failure zone—detection comes first)

#### 28.11.1 The Harm of Scale (wrong actions are not immediately visible)

Hard water entering the boiler leaves calcium and magnesium salts forming a dense scale layer on the heating surface. Two chains of harm:

- **Heat-transfer degradation**: scale conducts heat only 1/30–1/50 as well as copper (empirical order)—at the same fire, a 1 mm scale layer raises wall temperature by tens of degrees and pushes coal consumption up by at least 20% (empirical value);
- **Local overheating**: the scale layer separates the heated wall from the boiler water; local wall temperature climbs → riveted seams leak and the plate bulges and blisters, **and when a blister bursts, scale fragments and steam-water burst outward**—even at the atmospheric engine's low pressure, blisters still wreck boilers and injure people;
- **How to detect (the first question of this section)**: scale is completely invisible during operation. Only three detection means exist: open the handholes periodically to measure scale thickness (the reason Section 28.10.3 exists); evaporate blowdown water in a porcelain dish and examine the residue quantity, comparing trends shift by shift; compare pressure-rise rate / coal consumption shift by shift under the same fire—a gradual decline means scale is growing.

#### 28.11.2 Saponification Softening Method (lime + soda precipitates calcium and magnesium, Chapter 23)

The principle in one sentence: **lime precipitates magnesium (treating temporary hardness), soda precipitates calcium (also treating permanent hardness)**—reagents go into the reaction pool, calcium and magnesium settle as mud on the bottom, and the clear supernatant goes to the boiler. Lime and soda production and identification follow the Chapter 23 route; this section gives the at-the-boiler quantities:

- Rough hardness judgment (soap-solution method, Chapter 23): add soap solution drop by drop to a 100 mL water sample with shaking; record the number of drops needed for **persistent foam ≥1 cm that holds for 5 min without dissipating**—more drops = harder;
- Dosing starting point (empirical value, must be field-calibrated): per 1000 L of feedwater, slaked lime 300–500 g + soda 200–400 g;
- Calibration method: **500 mL bench test**—dose at the same ratio, let stand 2 h, then retest with soap solution; if the drop count falls to within ±2 drops of the reference soft water (rainwater, prepare a separate sample), the recipe holds; if it falls short, increase the dose proportionally and retry;
- Retest discipline: **softened water that fails the retest never enters the boiler**—better to halt the boiler and wait for water. Scale is a debt that grows by the month and wrecks boilers by the quarter; it costs more than downtime.

#### 28.11.3 Feedwater Settling and Filtration

- Turbid water sources settle ≥12 h first (two pools used in rotation) before entering the softening pool;
- Sand filter tank: sand grain size 0.5–2 mm, sand bed ≥400 mm deep, filtration rate ≤0.5 m/h (a 0.5 m² filter area yields about 6 m³ per day—order-of-magnitude check: atmospheric-engine boiler feedwater is on the order of ≤1 m³ per shift, so a single tank suffices with rotation margin for tank washing);
- Filter-sand maintenance: backwash as soon as the outflow turns turbid (flush upward from below with clean water until the outflow runs clear), at least once every ten days; backwash water drains to the settling pond for sediment reuse.

#### 28.11.4 Daily Blowdown Regime (logged system)

- Feedwater metering: hang a measuring staff on the feedwater tank, read once before and once after each shift; the difference is that shift's feedwater quantity (L);
- Frequency and quantity: blow down once per shift before taking the boiler off line, quantity = **5–10% of that shift's feedwater** (empirical starting point, needs calibration);
- Calibration method: open the handhole weekly to measure scale thickness—scale layer <0.5 mm keeps the current ratio; 0.5–1 mm doubles the blowdown quantity or strengthens softening; ≥1 mm takes the boiler off line for mechanical descaling plus a review of the softening regime (the criterion shares its origin with Card 28-06);
- Operating order: **open the master valve first, then the operating valve; when done, close the operating valve first, then the master valve**; tight-shutoff criterion as in Section 28.10.4 (listen + watch the pipe mouth);
- Logging: each shift records three columns—"feedwater quantity / blowdown quantity / operator"—signed by two people; forgetting to close the blowdown goes into the failure-mode table (first class of human-error accident).

[Card 28-06 Feedwater Softening] (eight fields)

1. **Input materials**: raw feedwater (hardness roughly judged by the soap method, drop count on file); slaked lime (freshly slaked, Chapter 23); soda (Chapter 23); reference soft water (rainwater, a separate sample of the same batch kept for comparison).
2. **Tools required**: soap-solution bottle and dropper; 100 mL graduated cylinder (for the soap-method sample); 500 mL beaker and stirring rod (bench test); two-compartment reaction–settling pool (used in rotation); sand filter tank (sand 0.5–2 mm, bed ≥400 mm); measuring staff on the feedwater tank (read before and after each shift); porcelain dish (to evaporate blowdown water and see the residue); handhole wrench (weekly scale-thickness check, Section 28.10.3).
3. **Operating sequence and control points**: ① rough hardness judgment — add soap solution drop by drop to a 100 mL sample with shaking, recording the drops needed for **persistent foam ≥1 cm that holds 5 min** → ② 500 mL bench test — dose at the same ratio, stand 2 h, retest with soap solution → ③ once the bench test passes, dose the whole pool and stir 10 min → ④ stand ≥2 h for reaction and ≥12 h for settling → ⑤ run the supernatant through the sand filter (turbid sources settle ≥12 h first, two pools in rotation) → ⑥ **only water that passes the retest enters the feedwater tank**. Control points: **softened water that fails the retest never enters the boiler** (better to halt the boiler and wait for water — scale is a debt that grows by the month and wrecks boilers by the quarter, so it costs more than downtime); backwash the sand filter as soon as the outflow turns turbid, and never send turbid water to the boiler.
4. **Empirical parameters and calibration**: dosing starting point per 1000 L of feedwater: slaked lime 300–500 g + soda 200–400 g; bench-test criterion = retest drop count within ±2 drops of the reference soft water; sand filter: sand 0.5–2 mm, bed ≥400 mm, filtration rate ≤0.5 m/h (0.5 m² yields about 6 m³/day, matching feedwater on the order of ≤1 m³ per shift); blowdown 5–10% of the shift's feedwater (Section 28.11.4). Calibration = bench test → whole pool → retest as one closed loop, then back-calibrate dose and blowdown ratio from the weekly handhole scale measurement (scale <0.5 mm hold the current ratio, 0.5–1 mm double it, ≥1 mm take the boiler off line for descaling). All of these are **empirical values that must be calibrated to local conditions**.
5. **Observations to record**: sediment depth in the settling pool (a sudden rise = the source changed); residue from evaporated blowdown water (trend compared shift by shift); scale on the gauge-glass; weekly handhole scale thickness; the three columns "feedwater / blowdown / operator" every shift, signed by two people.
6. **Pass / rework / scrap criteria**: pass = retest drop count within ±2 drops of the reference soft water and weekly scale <0.5 mm; rework = retest short → top up the dose proportionally, settle a second time and retest (no "close enough, send it to the boiler"); regime-level scrap = scale ≥1 mm for two consecutive months → review the softening system and take the boiler off line for mechanical descaling (the criterion shares its origin with Section 28.11.4).
7. **Common failures and troubleshooting order** (by frequency): (1) still hard on retest → dose too low (double it in a bench test); (2) cold water giving a false foam reading → warm the sample back to 20–25 ℃ and retest; (3) soap solution spent → check the reference sample's drop count first; if abnormal, change the soap solution; (4) filter outflow turning turbid → backwash or change the sand (backwash as soon as it turns turbid, at least once every ten days); (5) scale climbing month after month although the dose is right → blowdown ratio too low or the source hardness jumped (check sediment depth and residue, redo the bench test).
8. **L1 / L2 / L3 evidence**: L1 = one 500 mL bench test plus one whole-pool record (dose, drop count and retest all three on file); L2 = the three-column log run for a full month with weekly scale <0.5 mm on file; L3 = a full quarter of monthly handhole scale records, zero retest violations released to the boiler, and a second person dosing and retesting independently from this card alone, reaching the same verdict.

### 28.12 Valve-Gear Linkage Detailed Design and Adjustment (the atmospheric engine's "nervous system")

#### 28.12.1 Linkage Structure and Stroke Allocation

- Transmission chain: piston rod → beam → two valve rods (steam-admission valve rod, water-injection valve rod) → the valves. The atmospheric engine has no slide valve; "when to open and how far" for the two valves depends entirely on the linkage geometry—**the linkage is this machine's program**;
- **Stroke allocation is set by attachment-point positions**: the displacement of each point on the beam is proportional to its distance from the fulcrum. With the cylinder-side attachment 2.0 m from the fulcrum and full stroke 80 cm, placing the valve-rod attachment 150 mm from the fulcrum gives a valve travel of about 60 mm—the valves actually need 30–50 mm (empirical value), with the remainder left for adjustment;
- **Fine-adjustment structure**: the middle of each valve rod carries a **right-and-left-thread adjusting sleeve** (right-hand thread on one end, left-hand on the other, 3 mm pitch)—one full turn changes the rod length by 3 mm, advancing or delaying the valve's opening/closing moment; the sleeve's outer circle is graduated into 10 divisions (0.3 mm each), and **every one-division adjustment is logged as a scale position** (transcribed into that machine's file ledger);
- Locking: locknuts at both ends of the sleeve; after adjustment the two nuts are jammed against each other—vibration backing-off is the first cause of phase drift; the white-paint line recheck follows the Section 28.10.2 technique.

#### 28.12.2 Target Phasing (empirical values; calibrated by stepped trials)

- Steam admission valve: opens when the piston rises to **about 5% of stroke before top dead center**, closes 5–8% of stroke past the top;
- Water injection valve: opens **immediately after admission closes**, closes when the piston reaches **about 10% of stroke before bottom dead center** (leaving a residual steam cushion to buffer the return);
- Calibration method: as in 28-03—run unloaded 15 min per setting and pick the best by the twin indicators of stroke count and water output; **the optimal scale position is transcribed into that machine's file**. Every engine's linkage proportions differ; copying another engine's scale readings is forbidden.

#### 28.12.3 Linkage Troubleshooting for "Stroke Count Won't Rise / No Return Stroke" (linkage first, thermodynamics second)

Symptom one: stroke count will not rise—check in order:
1. Use the **white-powder method** to see the two valves' actual opening/closing points (coat the valve-rod tops with white powder and watch the opening/closing lines through a full barring-over)—if the attachment point has slid along the beam → valve travel shrinks and admission is insufficient;
2. Check the sleeve locknuts and index lines—misalignment means back-off drift; **reset to the filed scale position** and retry;
3. Check the play at each pin—**cumulative pin play >3 mm eats nearly half the valve travel** (three pins at 1 mm each add in series; do not take the maximum); replace the pins or bushings, and **never use the adjusting sleeve to compensate for play**—the play keeps growing, and the more you adjust the messier it gets;
4. Rule out thermal factors (injection-water temperature, steam pressure, sealing)—checked only after the linkage is cleared; then continue with the Section 28.9 table.

Symptom two: the piston stops at bottom dead center and does not return (the return relies on the steam fill lifting the piston against its weight and the counterweight)—check in order:
1. Check whether the admission valve is actually open (white-powder line unmoved = linkage jammed or attachment fallen off);
2. Check whether the injection valve is fully closed—**with injection water always on, the cylinder never warms up; the fill steam condenses instantly and the piston can never be lifted** (this is the most common cause of "no return stroke");
3. Valve plug seized—disassemble, inspect, and lap (Chapter 20 lapping route), then re-run after reassembly.

[Card 28-07 Valve-Gear Adjustment] (eight fields)

1. **Input materials**: fully assembled linkage (Section 28.12.1); the machine's filed optimal scale values
2. **Tools required**: sleeve wrench; white powder; calipers (to measure actual valve travel); shutdown and tag-out kit (Section 28.9 Iron Law is a precondition)
3. **Operation sequence and control points**: ① shut down, withdraw fire, vent to gauge zero, tag out → ② bar the engine through the full stroke and mark both valves' open/close points in white powder → ③ compare against the target phasing (Section 28.12.2) → ④ **turn ≤1 division per adjustment; run unloaded 15 min and record the stroke count** → ⑤ pick the best, lock the locknuts, redraw the lines → ⑥ log the scale position
4. **Empirical parameters and calibration**: 3 mm pitch, 10 divisions, 0.3 mm each; calibration = take the peak of the scale-position vs. stroke-count gradient curve
5. **In-process observation items**: stroke count and water output per setting; white-powder line positions of both valves' open/close points; sleeve scale position
6. **Pass / rework / scrap criteria**: pass = stroke count reaches the filed peak ±5% with running fluctuation <±10%; rework = back off one division and run another round; component-level scrap = pin play >3 mm (replace the pin/bushing and readjust; forcing compensation with the sleeve is forbidden)
7. **Common failures and troubleshooting order**: adjusted but no gain → check pin play first, then phasing; no return stroke → admission valve travel insufficient / injection valve not fully closed
8. **L1 / L2 / L3 evidence**: L1 one complete gradient curve; L2 the scale-vs-stroke curve entered in the machine's file; L3 a quarter's ledger of scale positions before and after adjustment

### 28.13 Two Atmospheric-Engine Variants: the Water-Lifting Machine and the Air-Blasting Machine

The same boiler–cylinder–beam body, with the power end swapped, yields two dedicated machines. Their transmission arrangements and acceptance criteria follow.

#### 28.13.1 Water-Lifting Machine (direct pump-rod connection; for mines and wells)

- **Transmission arrangement**: one end of the beam connects to the cylinder's piston rod, the other end **connects directly to the pump rod**—no crank, no flywheel; the beam is the transmission. The pump rod is a long tension member: wooden rod ≥150×150 mm, or wrought-iron rod φ40 mm. Tension worked example: pump cylinder φ200 mm, lift head 20 m → rod tension ≈630 kgf; a φ40 iron rod has a cross-section of 12.6 cm², stress about 50 kgf/cm²—ample margin. Order-of-magnitude check: the atmospheric suction-lift ceiling is about 10 m—**single-stage suction lift ≤8 m** (empirical, with margin kept); deep wells use two stages in relay, with both pump rods linked to act at the same frequency;
- **Guides**: a pair of guide plates clamps the pump rod every 2–3 m (guarding against buckling under compression and side sway); guide clearance **≤5 mm**—too much play and the rod swings and strikes the guides; knock-noise locating as in Section 28.9;
- **Acceptance**: theoretical lift quantity = strokes per minute × pump-cylinder area × effective stroke × filling coefficient 0.8–0.9 (empirical; filling-coefficient calibration: measure actual values and average over three consecutive shifts). Measure the actual lift quantity with the Chapter 25 flow method—**a deviation ≤15% from the calculated value passes**; over a continuous full shift, check guide-plate temperature rise (hand touch / wax strip, same method as Chapter 21) and re-measure the clearance. Mine scenes add two items: a falling-object shelter over the rod passage at the shaft mouth, and a **broken-rod guard fork** (catches the rod the moment it snaps, preventing it from falling down the shaft—people are below; this is a safety component, not an accessory).

#### 28.13.2 Air-Blasting Machine (with bellows, Chapter 12)

- **Transmission arrangement**: the beam's power end, through a short lever (may reduce the stroke 2:1 to gain force), connects to the Chapter 12 wooden box-bellows / leather-bag route. The atmospheric engine delivers intermittent strokes, so the bellows outlet must add two items: a **check valve** (prevents back-suction on the return stroke—back-suction can pull the fire at the furnace mouth back along the air flow) and an **air receiver** (volume ≥3–5 times the bellows' single-stroke air output, empirical value) to smooth the flow into continuous blast;
- **Value account**: Chapter 12 human blowing (leather bag 8–15 L per stroke, 15–25 strokes per minute) cannot be sustained by one person through a full watch—one blowing machine replaces 2–3 dedicated blowers, and the blast volume is stable and adjustable with stroke count;
- **Acceptance**: connect a U-tube water-column differential gauge at the air-receiver outlet; reading fluctuation over a full shift **≤±30%** (empirical value; calibration method: first take human-blowing readings as the control group, then compare against machine power); return to the Chapter 12 furnace-temperature criterion—under machine blast, the forge / smelting furnace must reach the temperature class specified in that chapter to pass; the stroke-count vs. blast-pressure comparison table enters the machine's file.

### 28.14 Separate Condenser Preliminary Study (Watt-style upgrade route) [background/outlook]

> This section is a study registration, not a construction permit: **implementation is forbidden until the unlock conditions are complete** (an expansion of the "explicitly cannot do" item in the Capability Boundary).

- **Principle and benefit (why it is worth queueing for)**: the current engine chills the cylinder every cycle and then reheats it, **with steam spent on reheating on the order of more than half** (empirical estimate). Move condensation out of the cylinder into a dedicated condensing shell; the cylinder stays hot, and fuel savings are expected on the order of **30% or more** (a conservative, verifiable lower bound; historical Watt engines saved more—this book commits to the lower bound and lets measurement speak);
- **Sketch-level description (for registration; not elaborated)**: one vertical condensing shell with volume ≥**1.5 times** the cylinder's stroke volume (empirical); an exhaust pipe from the cylinder top leads into the shell's upper part; a water-injection ring pipe is set in the shell's upper section (the original injection valve's function moves here); a condensate sump at the shell bottom connects to an air pump (a small piston pump, driven by an extension of the original linkage), and the condensate drains into the feedwater tank—hot water reused, feeding back into the Section 28.11 feedwater temperature rise; the original two-valve linkage expands to four paths—admission, exhaust, injection (into the shell), and vacuum valve—with the phase-linkage principles as in Section 28.12;
- **Unlock conditions (registered; forbidden until all four are met)**: ① cylinder boring upgrade—roundness ≤0.05 mm class (now 0.1 mm), sealing rising from "packing makes do" to "precision fit"; ② slide-valve / box-valve tooling—valve-body bore boring + plug-lapping tooling (an extension of the Chapter 20 lapping route); ③ vacuum measurement always on hand—a mercury U-tube gauge (an extension of the Chapter 27 pressure-gauge route) able to read the cylinder's vacuum directly; ④ the condensing shell and air-pump barrel themselves pass the hydrostatic test (28-01 procedure) + a vacuum hold test—after evacuation, the mercury gauge falls back ≤5 mmHg in 10 min (empirical value);
- **Verification route (first step after unlocking)**: connect the old engine's exhaust port to a test condensing shell for a **controlled comparison**—at equal coal consumption, compare stroke count and per-shift water output between the "injection in cylinder" and "condensation in shell" modes; only when the data is complete do you decide on converting the whole engine. Skipping the comparison and converting outright "because history did it" is forbidden.

---

## Parameter Summary Table

| Parameter | Value | Class |
|---|---|---|
| Atmospheric-engine boiler gauge pressure | Near zero (≈0–0.2 kgf/cm²) | Design |
| Safety-valve setting | Lifting pressure = weight ÷ valve-seat area; e.g. 20 mm seat, 0.5 gauge → weight 1.6 kg | Formula |
| Hydrostatic test | 2 times working pressure, 30 min hold, one vessel one file | Hard rule |
| Bore/stroke | 25–40 / 60–100 cm class | Empirical |
| Boring precision | Roundness ≤0.1 mm, taper ≤0.2 mm/300 mm | L2 criterion |
| Honing cross-hatch angle | 30°–60° (target 45°) | Empirical |
| Piston clearance | 3–5 mm smaller than the bore (filled by sealing) | Empirical |
| Packing seepage rate | A few drops per minute | ◎ empirical |
| Stroke-count fluctuation | Within ±10% over a continuous full shift | L2 criterion |
| Efficiency | <1% order | Empirical |
| Boiler wall-thickness formula | t = design gauge pressure × inner diameter × safety factor 8 ÷ allowable stress (copper 200 / iron 300 kgf/cm²); riveting floor 6 mm | Formula |
| Flat-head staying | Bolts ≥22 mm, spacing ≤30 cm, ≤500 cm² carried per bolt; white-paint line observation on the nuts | Empirical |
| Manhole/handhole | Manhole 400×300 mm (only when shell diameter ≥800 mm); handhole 80×60 mm, ≥1 per 1 m² of heating surface | Empirical |
| Softening dose starting point | Per 1000 L feedwater: lime 300–500 g + soda 200–400 g (bench-test calibrated) | Empirical |
| Blowdown ratio | 5–10% of per-shift feedwater, calibrated by the weekly scale-thickness check; scale red line ≥1 mm → off line and descale | Empirical |
| Valve-gear fine adjustment | Right-and-left-thread sleeve, 3 mm pitch, 10 divisions (0.3 mm each); cumulative pin-play ceiling 3 mm | Empirical |
| Pump-rod acceptance | Measured lift vs. calculated value deviation ≤15%; single-stage suction lift ≤8 m; guide clearance ≤5 mm | L2 criterion |
| Blast acceptance | Blast pressure at the air-receiver outlet, full-shift fluctuation ≤±30% (U-tube water-column gauge) | Empirical |
| Separate condenser (preliminary study) | Shell volume ≥1.5 times stroke volume; benefit verified at fuel savings ≥30% order | Outlook |

## Failure Modes and Diagnostics

| Symptom | Candidate causes (by probability) | Verification | Disposition |
|---|---|---|---|
| Weak stroke | Wrong injection quantity; seal wear | Stepped injection-valve trials; listen for steam bypassing in the cylinder (◎ hiss at mid-stroke) | Adjust valve / replace seals |
| Stroke stops midway | Valve timing out of position; water in the cylinder | Observe the linkage action phasing; open the drain valve | Adjust the linkage; clear the drain |
| Sweat beads on the cylinder wall | Caulking failure | Stop and redo the 2-times hydrostatic test | Caulking repair + repeat the full procedure |
| Pressure-gauge drop (hold stage) | Leakage (seam/valve) | Circle the leak points with chalk | As above / lap the valve |
| Knocking at first start | Water hammer (un-drained water in the cylinder) | Probe the flow at the drain valve | Move the drain step to the front of the procedure |
| Bright patches biting the seals | Not honed / incompletely honed | Visual + rubbing impression | Re-hone |
| Bearing overtemperature | Clearance, oil passage, off-center load | The Chapter 21 three checks | Scrape / clear the oil groove / realign |
| After dry-firing | —— | **Adding water immediately is strictly forbidden** | Withdraw the fire and cool through (sudden addition explodes) |
| Heating-surface blister / burst scale fragments | Local overheating under the scale layer (long without softening, without blowdown) | Open the handhole and measure the scale thickness; a hollow sound when tapping the heating surface = blister | Take the boiler off line for mechanical descaling; rebuild the softening and blowdown regimes (28-06) |
| Blowdown valve left open (water level keeps falling) | Not confirmed tight after blowdown; plug eroded so it cannot seal | Sudden water-gauge drop + warm blowdown pipe mouth, sound of escaping steam | Close the operating valve immediately, feed water, take the boiler off line and inspect the valve; retrain the two-person sign-off system (Section 28.11.4) |
| Valve phasing reversed (injection before admission; the stroke cannot develop) | Linkage installed reversed; no unloaded trial after a large sleeve adjustment | White-powder method to view both valves' open/close order (admission must precede injection) | Swap or re-hang the linkage; readjust starting from the filed scale positions (28-07) |
| Condensate back-suction after shutdown (water hammer at restart) | Exhaust/blowdown line below the water level siphons back; no check valve | Open the drain valve to probe the flow before starting; bar the engine and listen for water in the cylinder | Mount the exhaust line high + check valve; add a "bar and drain" preliminary step to the start-up procedure |

## Process Card Index

[28-01] Hydrostatic test (28.4.4) | [28-02] Cylinder boring and honing (28.5.1) | [28-03] First start-up and loading (28.7) | [28-04] Safety-valve setting and live popping (28.4.3) | [28-05] Riveted-seam caulking (28.4.2) | [28-06] Feedwater softening (28.11) | [28-07] Valve-gear adjustment (28.12)

28-01 to 28-07 are full eight-field cards (items 1–8 complete). **28-04 carries two-step criteria: setting (formula + measured check after assembly) and live popping (rise to the set pressure, pop, fall back, reseat) — neither alone passes: calculated but never popped means not set.**

## Acceptance Criteria

- **L1**: the four steam-property experiments are on file; the demonstration small vessel with the weight-loaded safety valve passes its popping test; unloaded self-sustained running ≥50 cycles.
- **L2**: continuous full-shift running with pump connected, stroke-count / water-output records tabulated with fluctuation <±10%; the two-times hydrostatic test and the weekly safety-valve test regimes executed without gaps; the honed cylinder-wall cross-hatch records on file.
- **L3**: wear parts—seals, valve plugs, packing, rivets—are locally manufacturable and replaceable (mother-machine closed loop); the two-person stoker system and the maintenance tag-out system in operation; stable service for a quarter under real load (drainage). Evidence: release files, operating logs, spares ledger.

## Work Hours, Manpower, and Consumption

| Item | Manpower | Work hours (empirical) |
|---|---|---|
| Caulking practice (500 mm seam) | 1 person | 1 day |
| Boiler fabrication (rivet + caulk + braze, 1 m class shell) | 4 people | 15–25 days |
| Hydrostatic test, one vessel | 3 people | Half a day |
| Cylinder boring and honing | 3 people | 10–15 days |
| Linkage and beam assembly | 4 people | 10 days |
| Whole-engine first start-up commissioning | 4 people + 2 stokers | 3–5 days |
| Softening–settling–filtration system build (pools + tank + piping) | 2 people | 10 days |
| Linkage first phasing commissioning (incl. stepped trials) | 3 people + 2 stokers | 2–3 days |
| Operating consumption | Coal/wood per shift per the Chapter 38 ledger; injection cold water 2–4 m³/shift | — |

## Safety Boundary

- Vessels that have not passed the 2-times hydrostatic test are forbidden from receiving steam; cast iron is forbidden as a pressure shell; **no one may ever add weight to a safety valve** (lead seal kept by a designated person).
- After dry-firing, adding water immediately is strictly forbidden—withdraw the fire and cool through first (sudden water addition explodes).
- High-pressure experiments are outside the settlement's capability boundary and are never done (the four conditions of Section 28.8).
- Steam burn treatment: flush with cold water ≥15 min; do not peel away clothing stuck to the skin (links to Chapter 44 first aid).
- During hydrostatic-test tapping inspection, personnel stay out of the tapping direction; fast opening when relieving pressure is forbidden.
- Stokers' long-term heat-radiation and noise exposure goes into the Chapter 49 occupational health account.

## A. Existing Tool List

Riveting, brazing, and casting (Chapters 17 and 20); boring (Chapter 20); crank, connecting rod, and bearings (Chapter 21); leather, hemp rope, grease, and graphite grease (Chapters 15 and 23); thermometer / pressure gauge / water gauge / flow method (Chapters 25 and 27); the instrument release-slip system (Chapter 27).

## B. New Tools Added in This Chapter

The full atmospheric (Newcomen-type) steam engine set (boiler–cylinder–piston–spray condensation–beam–pump); the round-nose caulking chisel and the caulking technique; the direct-weight safety valve (with setting formula and lead seal); the hydrostatic test procedure (2-times pressure, staged, hold, one vessel one file); the honing bar and cross-hatch regime; the conical-valve and stuffing-box sealing system; the valve-gear rod linkage; the right-and-left-thread adjusting sleeve and scale-position system; the boiler wall-thickness formula and stay arrangement method; manhole/handhole cover assemblies and the asbestos gasket set; the blowdown double valves; the feedwater softening–settling–sand-filtration system and the soap-solution hardness method; the water-lifting machine's broken-rod guard fork and guides; the blower's air receiver and U-tube water-column differential gauge; the daily-inspection / weekly-inspection / troubleshooting three sheets; the two-person stoker watch system; the "high-pressure unlock four conditions" registration system.

## C. Unresolved Dependencies

Separate condenser and slide-valve steam distribution (Watt-style improvement; study description, benefit estimate, and the four unlock conditions in Section 28.14—implementation forbidden before unlocking); high-pressure boilers and high-pressure engines (four conditions unmet, explicitly forbidden); locomotive and marine engines (need a governor and rotational speed); the rotary factory line shaft (needs the crank-flywheel + governor combination).

## Next-Step Dependencies

Chapter 29: selection comparison among heat engines and water/wind power. Chapters 31–32: stable mechanical work is the prime-mover prerequisite for power generation. Chapter 33: heat sources serving vacuum work and lampworking. Chapters 50–53: power candidates for cold and arid regions. Chapters 38–39: operating consumption and wear-part cycles enter the ledger and the inspection sheets.
