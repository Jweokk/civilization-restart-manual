# Chapter 12: From the Pottery Kiln to the High-Temperature Furnace

> Part 3 · Agriculture, Pottery, and Basic Industry. The Chapter 11 shaft kiln can already stably reach 800–1000 °C, but burning lime through, melting glass, and reducing iron all demand higher, more concentrated, and more controllable temperatures. This chapter answers four questions: why the temperature won't rise (air), how to make it rise (blast and furnace type), how to know how high it has actually gotten (comparative temperature measurement), and **when it won't rise, which link to check first (the diagnostic tree)**. This chapter is the final prerequisite before Part 4's metallurgy.

## Chapter Objectives

- Establish the air-first view of combustion: a furnace's power ceiling is usually set by the air supply, not the fuel.
- Master the five means of raising and stabilizing furnace temperature (fuel, air matching, preheating, heat concentration, insulation).
- Complete the design rules for flue–firebox–chimney and empirical cross-section ratios; establish the **blast pipe diameter–air flow–air velocity conversion**.
- Build the leather bag bellows and the piston bellows (including the leather one-way valve design) to achieve continuous manual blast.
- Establish the three-layer furnace lining (refractory face–insulation layer–structural layer) and the cold-repair and hot-repair procedures; master **firing-shrinkage measurement and the mold enlargement method**.
- Establish the three-tier comparative thermometry regime of "slump-cone set + melting-point reference materials + fire-color table" (fire color is auxiliary only, not quantitative).
- Establish the **"furnace temperature won't rise" diagnostic tree** (four causes and one symptom, verified item by item) and the furnace-and-kiln life ledger.

## Capability Boundaries

**Can do:** about 1000–1100 °C on natural draft; about 1200–1400 °C on continuous manual blast (comparative; the local slump-cone set is the authority); furnace and kiln life managed through the ledger.

**Explicitly cannot do:** quantitative temperature measurement (the glass thermometer comes after Chapters 14+25); air flow and pressure metering (air matching is closed-loop by fire color and heating rhythm); bauxite- and graphite-grade refractories (the grog mix's limit is the furnace-temperature ceiling; to be upgraded after Part 4's mineral-source survey).

**External dependency:** charcoal production capacity (Chapter 6 charcoal-kiln expansion) — once blast capacity goes up, charcoal is the first supply to run short.

## Pre-Work Verification (check off item by item)

| # | Verification item | Criterion | Source |
|---|---|---|---|
| 1 | Refractory base mix | Grog 50%–70% + refractory clay 30%–50%; bricks already through at least one kiln firing with no spalling | Chapter 11 |
| 2 | Charcoal batch | Metallurgy-grade charcoal ≥100 kg (crisp knock, jet-black and dense, passes all Section 6.6 criteria) | Chapter 6 |
| 3 | Leather and sealing materials | 2 whole hides or large hide pieces (no big holes); animal fat, hemp tow, and tar glue all on hand | Chapters 7, 8 |
| 4 | Woodworking capability | Able to plane a flat 60×30 cm plank box (diagonal difference <2 mm) | Chapters 7, 9 |
| 5 | Measurement and timing | Standard rod, angle board, Type-A level frame, water-clock timing | Chapter 3 |
| 6 | Test-piece regime | Standard test-piece method in practiced use (at least 5 firings of records) | Chapter 6 |
| 7 | Firing archive | Chapter 11 archive system in operation | Chapter 11 |
| 8 | Manpower | 2 for furnace building; blast shifts of ≥2 each (Iron Law Seven: continuous single-person blast ≤30 min) | — |

---

### 12.1 Why Combustion Needs Air

**Qualitative chemistry:** The main constituents of charcoal and firewood are carbon and volatiles. Combustion is carbon combining with oxygen and releasing heat: with ample oxygen, carbon becomes carbon dioxide and releases its full heat; with insufficient oxygen, carbon becomes only carbon monoxide — releasing roughly half the heat, and carbon monoxide is toxic (Section 6.8). "A yellow, soft, sluggish flame" is the sign of CO still hunting for oxygen in the flue.

**Order-of-magnitude concept:** Burning 1 kg of charcoal through takes about 8–9 kg of air, roughly 7 m³ (empirical order of magnitude). **What the furnace eats every minute is mostly air; fuel is the minority.** From this follows the chapter's first law:

> **When the furnace temperature won't rise, check the air first, the fuel second.** Pile up fuel as you please; without a matching air flow, the surplus fuel not only releases no heat, it absorbs heat (warming up, devolatilizing) and crowds out combustion space.

**The physical ceiling of natural draft:** An open fire and a kiln draw air by the buoyancy of hot gas — the draft grows with chimney height and the temperature difference inside the furnace, but cold air entering the firebox absorbs heat and cools the flame. Under natural draft, the heat carried off by excess air and unburned gas pins the flame temperature near about 1000 °C (shaft kiln + charcoal about 1000–1100 °C, empirical, must be field-calibrated). The only ways past it are "make the wind something you deliver yourself" (Section 12.4) and "don't let heat escape for nothing" (Sections 12.2, 12.6).

**Engineering implications table:**

| Phenomenon | Air-side explanation |
|---|---|
| Flame yellow, soft, long, trailing black smoke | Oxygen short; heavy CO and soot generation |
| Flame glaring white and short, furnace temperature falls instead | Too much air; cold air dilutes the flame |
| Temperature dips then rises after adding wood | New wood absorbs heat to dry out and crowds combustion space |
| Kiln temperature stuck at a value, no longer climbing | Natural draft maxed out; needs blast, or a smaller heat-concentrating chamber |

### 12.2 How to Raise and Stabilize Combustion Temperature

The flame's heat has only three destinations: stay in the furnace (useful), leave with the flue gas, or leak through the furnace walls. The five means each block one escape route:

| Means | Principle | Operation |
|---|---|---|
| ① Fuel upgrade | Charcoal has no moisture and no volatiles; its flame is hotter than wood's | Charcoal only for the temperature-pushing stage |
| ② Air matching | The less excess air, the hotter the flame | Adjust the air port to "a flame bright white and forceful but not glaring" |
| ③ Air preheating | Use flue waste heat to heat the incoming air | Put the air port beside a long flue; the air travels the hot path into the furnace |
| ④ Heat concentration | The higher the heat intensity per unit volume, the higher the temperature | Shrink the firebox and concentrate the fuel — "small and fierce" beats "big and mild" |
| ⑤ Insulation | Cut wall heat loss and heat-storage loss | Three-layer furnace lining (Section 12.6) |

**Temperature ladder table (target temperature bands per process, comparative):**

| Process | Target band | Reliable means combination |
|---|---|---|
| Drying, smoking | <150 °C | Charcoal bed, low fire |
| Pottery | 700–1000 °C | Shaft kiln on natural draft (Chapter 11) |
| Lime decomposition | 900–1000 °C | Shaft kiln + continuous wood feeding |
| Glass melting | 1100–1300 °C | High-temperature furnace + blast (Chapter 14) |
| Bloomery reduction of iron | about 1200–1400 °C | High-temperature furnace + strong blast + charcoal (Chapter 18) |

"Stable" matters as much as "higher": temperature swings are more harmful than a slightly lower steady temperature (thermal-shock cracking, incomplete reactions). What stable operation looks like: predictable hold times for each fire-color stage, a fixed feeding rhythm, and slump-cone set readings that match firing after firing.

### 12.3 Flues, Firebox, and Heat-Flow Organization

**Three design principles:**
1. **Low in, high out**: air inlet low, smoke outlet high; the greater the height difference, the stronger the draft.
2. **Continuous cross-section**: passages must never shrink or swell abruptly. Every point of the flue must have a cross-section ≥1.5 times the total air-port area (empirical value), or the front forces air in while the back chokes on pressure.
3. **The flow must wrap the workpiece**: the flame must pass around the workpiece before leaving. The baffle wall forces the smoke to take the long way around; only then is heat exchange thorough. Straight in, straight out = heat leaves with the smoke.

**Furnace anatomy (this chapter's standard furnace: separated-firebox shaft furnace):**

```
      ┌─ smoke port (top, total area = 1.5–2× the air ports)
   ┌──┴──┐
   │ working chamber │ ← workpiece/crucible/kiln load here
   ├─ baffle wall ─┤ ← forces the flame to detour, not roast the workpiece directly
   │ combustion chamber │ ← fuel bed; grate (clay-rod bars) below
   ├──────┤
   │ ash pit / air │ ← air ports angled 30°–45° up toward the bed center
   └─ air inlet ─┘
```

- **Air ports**: 1–2, placed below or at the lower side of the fuel bed, blowing in at a slant; with manual blast the air port is the clay pipe's outlet.
- **Grate**: refractory clay bars laid side by side, gaps half a finger wide; ash pit below (cleaned before every firing).
- **Baffle wall**: a passage left between combustion chamber and working chamber, height about 1/3 of firebox height (empirical value) — the workpiece receives swept-flow heat, not direct flame.
- **Chimney**: adobe/brick, 1.5–3 m tall (empirical value); every extra meter adds draft but also adds heat-storage loss — an intermittent furnace need not be built tall.

**Trial-firing method (no guessing)**: after loading, light a small fire; set wet grass bundles at each smoke port and passage point in turn and watch the smoke's path and strength; wherever no smoke comes out is a dead zone — adjust the loading layout or add smoke ports, then begin the formal heat-up.

### 12.4 From Natural Draft to Manual Blast

#### 12.4.1 Blast Capacity and Pipe-Diameter Conversion

The essence of forced blast: push air into the fuel bed under pressure, so the combustion rate is no longer limited by natural buoyancy. But **the air must reach the bed center at a reasonable velocity** — pipe diameter decides all of it:

**Bellows output estimate**: box 60×30×30 cm = 54 L volume; effective piston displacement about 30–40 L/stroke; 30 strokes/min → **about 1–1.2 m³/min** (empirical value, must be field-calibrated: bag metering — at the bellows outlet, time how long it takes to fill and empty an inflated leather bag and convert).

**Flow–diameter–velocity table** (velocity = flow ÷ pipe cross-section, engineering approximation):

| Air flow | 25 mm inner diameter | 40 mm inner diameter | 60 mm inner diameter |
|---|---|---|---|
| 0.5 m³/min | ≈17 m/s | ≈6.6 m/s | ≈2.9 m/s |
| 1.0 m³/min | ≈34 m/s | ≈13 m/s | ≈5.9 m/s |
| 2.0 m³/min (twin boxes) | ≈68 m/s (too fierce) | ≈27 m/s | ≈12 m/s |

**Target velocity 10–25 m/s (empirical window)**:
- Velocity too low (pipe too fat) → the air disperses as soon as it enters the furnace, cannot penetrate the fuel bed, and the bed center goes oxygen-starved;
- Velocity too high (pipe too thin) → resistance grows with the square of velocity, human effort is wasted on pipe-wall friction, and the air port goes locally too cold and over-oxidized; the pipe also heats up and buzzes (verification: feel the pipe wall temperature, listen to the wind's note — a sharp whistle = too fast).
- Conversion self-check (order-of-magnitude check): 1 m³/min ≈ 17 L/s; a 25 mm pipe's cross-section is about 4.9 cm²; 17 L/s ÷ 4.9 cm² ≈ 34 m/s — outside the window; switch to a 40 mm pipe.

**Air port position and angle**: air enters from below or the lower side of the fuel bed, angled 30°–45° upward toward the bed center — the air must **pass through** the fuel layer, not skim its surface. No straight-through hole opposite the air port (the air would short-circuit and blow straight out). Multiple air ports are placed symmetrically so the flows meet at the bed center.

**Feedback control (instrument-free operation)**: close the loop on three observables — ① flame state (the 12.1 phenomenon table); ② standard test pieces (Section 6.7: place known pieces in the same furnace and watch their progress); ③ heating rhythm ("how many feeding intervals per cone level"). All three go into the firing archive; the next firing executes from the archive.

#### 12.4.2 The "Furnace Temperature Won't Rise" Diagnostic Tree (four causes and one symptom; easiest first)

There is only one symptom (the slump-cone set is slow to advance a level) but five cause classes. **Ordered by "most common + easiest to verify"; go through item by item; skipping checks is not allowed**:

```
Furnace temperature won't rise
├─ ① Fuel problem? (most common; checkable in 5 minutes)
│    Verify: pull charcoal and knock (dull = damp/underfired); break it open and look at the core (black core = not burned through); weigh equal volumes (damp charcoal 20%+ heavier)
│    Action: switch to dry charcoal; check the Chapter 6 charcoal-kiln firing criteria
├─ ② Air not getting in?
│    Verify: hold the back of your hand at the bellows outlet to feel the air; standard-fire comparison method (Section 12.5) against the historical "wind-strength levels"; check the valve flaps (ash-stuck and cocked up is most common)
│    Action: clean flaps / replace the piston seal ring; re-verify pipe diameter per Section 12.4.1
├─ ③ Charge loaded wrong?
│    Verify: compare charge volume and packing tightness against the baseline firing (photos/records); is the charge packed too tight (probe rod will not pass) or too full and covering the smoke ports
│    Action: reload, keeping charge line and tightness identical to the baseline
├─ ④ Lining stealing heat?
│    Verify: back of hand against the outer wall (bearable = pass; too hot to touch = large heat loss); check the first-bake record — a lining never dried through holds high moisture and absorbs heat every single firing
│    Action: a thorough slow bake; thicken the insulation layer (Section 12.6)
└─ ⑤ Flue blocked / air port wrong?
     Verify: wet grass bundles to test draft at each smoke port (the 12.3 trial-firing method); check whether the air ports are half-blocked with slag/ash; check whether the air-port angle has been changed to skim across the bed surface
     Action: clear the flue ash; reset the air-port bricks
```

**Discipline: after each cause class is checked, log it in the firing archive. Skipping items to guess is the number-one cause of drawn-out commissioning.**

[Card 12-05 Furnace Temperature Won't Rise: Troubleshooting] (eight fields)

1. **Input materials**: the firing in which the cone set is slow to advance; charcoal samples (knock sound, core, equal-volume weight); bellows and valve flaps; the charge record of this firing and of the baseline firing (volume, tightness, charge line); the first-bake record; wet grass bundles.

2. **Tools required**: back of a hand (to feel air at the port, heat at the outer wall); probe rod (charge tightness); equal-volume weighing (damp charcoal comparison); wet grass bundles (port draft test); scribed rod (erosion depth); firing archive. Calibration source: air strength by the standard-fire comparison against historical levels; heat loss by "3 s of hand" on the outer wall; every verdict rests on the historical record, not on how it feels now.

3. **Sequence and control points (four causes, one symptom; ordered most common + easiest to verify; item by item, no skipping)**: (1) Fuel problem? (most common, checkable in 5 minutes: a dull knock = damp or underfired, a black core = not burned through, equal volume 20%+ heavier = damp) → switch to dry charcoal, check the Chapter 6 charcoal-kiln criteria; (2) Air not getting in? (hand at the port to feel the air, standard-fire comparison against the historical wind-strength level, check valve flaps for ash-stuck cocking) → clean the flaps / replace the piston seal ring, re-verify pipe diameter per 12.4.1; (3) Charge loaded wrong? (compare volume and tightness with the baseline, a probe rod that will not pass = too tight, too full and covering the smoke ports) → reload with the charge line and tightness as at baseline; (4) Lining stealing heat? (back of hand on the outer wall, check the first-bake record) → one thorough slow bake, thicken the insulation; (5) Flue blocked or air port wrong? (wet grass bundles at each port, ports half-blocked with slag or ash, port angle changed to skim the bed) → clear the flue ash, reset the air-port bricks. Control points: log each cause class as it is checked; guessing across skipped items is the number-one cause of drawn-out commissioning.

4. **Empirical parameters and calibration**: damp charcoal 20%+ heavier at equal volume; fuel tiers — damp wood under half a share of dry wood / dry wood / charcoal about 1.5–2× the same weight of dry wood; target pipe velocity 10–25 m/s; outer wall "3 s of hand" ≈ 60–70 °C; flue cross-section ≥1.5× total port area; actual use 20% over budget triggers this tree — grinding on regardless is not allowed.

5. **Observations to record**: cone advance rhythm; flame color and shape (yellow, soft, long, black smoke = short of air / piercing white and short = too much air); outer-wall hand-feel; charcoal knock sound, core, equal-volume weight; charge-line height and tightness; grass-bundle draft at each port.

6. **Pass / rework / scrap criteria**: pass = the tree walked item by item, a single main cause identified and fixed, and the cone set advancing again; rework = still not advancing — go back and retest (2) and (4) (air and lining); scrap = a through crack or erosion beyond 1/3 of the lining, requiring shutdown and major repair (never run a sick furnace).

7. **Common failures and diagnosis order (by frequency)**: (1) damp or underfired fuel (most common, a 5-minute check); (2) valve flaps ash-stuck and cocked, piston seal ring worn (air feels weak, the rod pulls light); (3) charge too tight or too full, blocking the smoke ports; (4) lining never dried through, absorbing heat every firing; (5) flue ash and ports half-blocked with slag; (6) pipe too small, velocity too high (pipe hot and trembling, sharp whistling); (7) a through hole opposite the port short-circuiting the air.

8. **L1 / L2 / L3 evidence**: L1 = one record of locating and solving a single case by the tree; L2 = three consecutive firings with consistent cone readings after tree-based fixes and actual use within ±20% of budget; L3 = the diagnosis record in the firing archive, and a second person locating the same main cause independently from this card.

### 12.5 Building the Simple Blast Devices

**The leather bag bellows (skin-bag air bladder)** — the simplest air blower: sew a whole hide into a bag, or make a flat cavity of wooden boards + leather faces (seams sealed with tar glue); an outlet pipe lashed to a clay pipe (the near-fire end must be clay pipe); squeeze with both hands to expel air, release to draw air in — **no valves, pulsing air**, two people alternating. Role: ignition, small furnaces, pit-kiln temperature pushes; the training device that precedes the piston bellows.

**The piston bellows (this chapter's core engineering)**, single-acting; dimensions are empirical starting values:

| Part | Specification | Construction |
|---|---|---|
| Box | plank-built square box about 60×30×30 cm | planed planks + tar-glued joints + rope hoops; inner walls planed smooth |
| Piston | a single board slightly smaller than the inner cross-section, 2–3 mm clearance all around | felt/hemp tow/leather ring nailed to the board edge, lubricated with animal fat |
| Pull rod | hardwood rod through a center hole in the front board | hemp tow wound around the hole for sealing, greased |
| Intake valves | 2–3 holes in the rear board, each covered by a leather flap (nailed down on one side, liftable) | leather flap + wooden-nail hinge: opens outward, closes inward |
| Exhaust valve | hole in the piston board center covered by a leather flap: opens on the push, closes on the pull | installed reversed |
| Outlet pipe | opening on the lower front side, lashed to a clay pipe | pipe diameter chosen from the Section 12.4.1 table |

**Working cycle**: pull out — the piston-hole valve closes, the rear-board intake valves are sucked open by the negative pressure, air enters the box; push forward — the intake valves close, the piston-hole valve is pushed open by pressure, air passes through the piston and into the furnace via the outlet pipe. **Two people, two boxes, in parallel, alternating** (push and pull rhythms offset) approximates continuous air; four people in two shifts can burn day and night.

**The valves are the soul of this device**: the leather flaps must be supple, flat, and well seated; the nailed-down side is the "hinge", the other three edges free to seat against the valve mouth. Failure signs: the air feel weakens, the pull rod goes lighter, the furnace-mouth flame no longer pulses with the push-rod beat. Troubleshooting order: flap stuck with ash and cocked up → valve mouth worn uneven → piston seal ring worn thin → box leaking at the seams. Inspect the flaps once per work shift; grease the piston with animal fat.

**Comparative air-flow calibration (no instruments)**: with the same standard fire (equal charcoal, equal air port), blow in turn with the leather bag bellows / one box / two boxes; record the number of wood charges needed for the standard test piece to reach the same change level — this becomes the team's "wind-strength comparison table"; from then on, speak only reproducible language like "single box, level three".

[Card 12-01 Piston Bellows Manufacture and Maintenance] (eight fields)

1. **Input materials**: planed boards (for a plank-built box about 60×30×30 cm; the inner walls must be planed smooth); 2 hides of leather (valve flaps and piston seal ring — take supple, flat, scar-free sections); felt or hemp tow (piston-edge packing, rod-hole wrapping); animal fat (piston and rod lubrication, 0.2 kg per high-temperature firing); tar glue (joint sealing); an outlet clay pipe (diameter from the Section 12.4.1 table); one hardwood pull rod.

2. **Tools required**: the full Chapter 7 / 9 woodworking kit (plane, chisel, saw, drill, rope hoops); a leather awl and thread; a standard fire (equal charcoal, equal ports) for the air-strength comparison; a leather bag for displacement measurement; wet grass bundles and the back of a hand (air and heat checks); the firing archive and the crew's air-strength comparison chart. Calibration source: displacement by the leather-bag method — hold the outlet against a fully inflated bag and time how long it takes to collapse, then convert; air strength by the standard-fire comparison against the historical "strength level"; "the air feels strong" is never a conclusion.

3. **Sequence and control points** (build → test the air → put into service; each stage signed off, no stage skipped): ① **Build the box** — plane the boards, glue the joints with tar, add rope hoops, plane the inner walls and wipe the glue ridges off with a damp cloth. Control point: inner-wall smoothness (◎ hand-feel: the piston drags evenly over the whole stroke with no dead point; a dead point means a ridge or a warped board). ② **Fit the piston** — a single board slightly smaller than the inner cross-section, 2–3 mm clearance all round, a felt / hemp-tow / leather ring nailed to the edge, greased with animal fat. Control point: the clearance must be even — too tight and the rod pulls hard and wears the ring, too loose and it leaks. ③ **Fit the pull rod** — a hardwood rod through the centre hole of the front board, hemp tow wound round the hole and greased. Control point: the rod axis square to the piston face, so the piston does not skew and scrape the wall. ④ **Cut the intake valves** — 2–3 holes in the rear board, each covered by a leather flap nailed down along one edge as a hinge (opens outward, closes inward). Control point: the flaps supple, flat and well seated — hold them to the light and check that no gap shows round the valve mouth. ⑤ **Fit the exhaust valve** — a hole in the centre of the piston board covered by a leather flap, installed reversed (opens on the push, closes on the pull). Control point: the two valve sets work in opposite directions; installed the same way the bellows blows on neither stroke. ⑥ **Attach the outlet pipe** — an opening on the lower front side lashed to a clay pipe, diameter from the Section 12.4.1 table (target pipe velocity 10–25 m/s). Control point: **the near-fire end must be clay pipe** — bamboo or wood burns through next to the fire and starts a furnace-front fire. ⑦ **Accept the joint seal** — water test: fill the box and let it stand; no seepage at the outer joints. Control point: do this before the leather parts go on — a leaking joint is cheapest to fix with glue now. ⑧ **Calibrate the air output** — on one and the same standard fire, blow with the leather bag / single box / double box and record the number of fuel charges each needs to bring a standard coupon to the same stage of change; that gives the crew's "air-strength comparison chart". Then measure single-box displacement by the leather-bag method (30–40 L per stroke, 30 strokes/min ≈ 1 m³/min as starting points, replaced by the measured values). Control point: displacement and air strength are entered together, in the same batch; after this the crew speaks only in reproducible terms such as "single box, third notch". ⑨ **Put into service** — two people, two boxes in parallel, alternating (push and pull rhythms offset) approximates continuous air; four people in two shifts can burn day and night. Control point: one shared rhythm call; **nobody stands at the rod end** (a slipped pin throws the rod back).

4. **Empirical parameters and calibration**: box about 60×30×30 cm, piston clearance 2–3 mm, 2–3 intake valves (structural starting values); displacement 30–40 L per stroke, 30 strokes/min ≈ 1 m³/min — empirical values, to be calibrated to local conditions (leather-bag method); target pipe velocity 10–25 m/s (empirical window); air port angled up 30°–45° at the bed centre; one box takes 1–2 people 3–4 days (half of it leather sewing); 0.2 kg of lubricating fat per high-temperature firing. The seal-ring wear period has no fixed number of days: it is logged at every "the rod has gone light" event until the crew's replacement interval emerges.

5. **Observations to record**: synchrony between the push-rod beat and the furnace-mouth flame pulse (loss of synchrony = valve leak); fuel charges needed by single box / double box to bring a standard coupon to the same stage; how heavy the rod feels (against the previous entry); flap condition (ash-stuck, cocked, edge curled); seal-ring wear and replacement dates; whether the joints seep; pipe wall temperature and whether it whistles (a sharp whistle = overspeed); the per-shift flap check.

6. **Pass / rework / scrap criteria**: pass = 100 consecutive strokes with no loss of air, and the standard-fire comparison at the historical level; part rework = replace the flaps or the piston seal ring (leather parts recovered and re-cut); box rework = leaking joints re-glued and retested; scrap = the box has cracked or warped (rebuild the box, recover the leather parts and rod); pipe scrap = the clay pipe has cracked (replace it; bamboo or wood is not an option).

7. **Common failures and diagnosis order** (by frequency): ① flaps ash-stuck and cocked (most common: air weakens, the rod pulls light, the flame no longer pulses with the beat) → clean them and reseat, once per work shift; ② piston seal ring worn thin (air fades, a hiss at the piston) → replace and grease; ③ valve mouth worn uneven (a new flap will not seat either) → true the mouth or renew the seat; ④ box joints leaking (visible seep in the water test) → re-glue and re-hoop; ⑤ rod-hole seal failed (air escapes round the hole, fat on the hand) → rewind hemp tow and grease; ⑥ outlet pipe too small (wall hot, trembling, sharp whistle, velocity above 25 m/s) → step up one pipe size per the Section 12.4.1 table; ⑦ a through hole opposite the air port (air short-circuits straight out of the furnace, the bed centre still starved) → plug it and reset the port to 30°–45° upward; ⑧ the two boxes out of rhythm (air surging) → one call, push and pull offset.

8. **L1 / L2 / L3 evidence**: L1 = a newly built box runs 100 consecutive strokes with no loss of air and reaches the historical level in the standard-fire comparison, recorded in the firing archive; L2 = two boxes run 20 consecutive firings on routine maintenance only (flap changes, greasing), with the cone advance rhythm matching the baseline firings; L3 = flap and seal-ring lives logged event by event (handing on to Chapter 39), the ledger able to answer "which flap is due next", and a second person building a box alone from this card and passing L1.

### 12.6 Furnace Lining, Refractory Materials, and Insulation Structure

#### 12.6.1 Firing Shrinkage and the Mold Enlargement Method

Refractory bricks and lining parts shrink after firing. **Without measuring the shrinkage, molding straight to target dimensions, every finished piece comes out undersized**. Measurement card (one run per batch of clay/mix):

1. Make test bars: press the mix into 100×20×20 mm bars; scribe two 100 mm datum lines on the surface;
2. Measure the datum lines after drying → gives the **drying shrinkage** (commonly 2–5%, empirical value);
3. Fire in the kiln to this mix's service temperature band (judged with the slump-cone set); measure the datum lines cold → gives the **firing shrinkage** (commonly 5–10%, empirical value);
4. **Mold enlargement**: mold length = target length ÷ (1 − total shrinkage). Example: target 200 mm brick, 8% total shrinkage → mold length 200÷0.92 ≈ 217 mm;
5. The test bars also check distortion (a mix warping >2% gets its grog share raised and a retest) and cracks (crazing = drying too fast or too much plastic clay).

**What grog does**: once-fired crushed material (Chapter 11) no longer shrinks; blending in 50%–70% pushes shrinkage and cracking down at the same time — that is why the grog share in the refractory base mix is so high, not merely for heat resistance.

**Local judgment for the alumina–silica rule of thumb**: refractoriness rises with alumina content. Rough field test for local clays: light color (white, gray-white) and greasy texture usually mean higher refractoriness; deep red = high iron, refractoriness drops and melt staining is easy. Take material from different strata of the same deposit and run test bars against each other (the Chapter 11 panning regime); **build a local "material color–shrinkage–refractoriness" triple archive for each site**.

[Card 12-02 Firing-Shrinkage Test Bars] (eight fields)

1. **Input materials**: the mix of this batch (refractory base mix: grog 50%–70% + refractory clay 30%–50%); water; identification marks (batch number, stratum). One run per batch of clay or mix.

2. **Tools required**: test-bar mold (100×20×20 mm); scribing knife (two 100 mm datum lines); rule (zeroed against the standard rod, Chapter 3); slump-cone set (to judge the temperature band); kiln. Calibration source: dimensions against the standard rod; the band reached is judged by the cone set, never by fire color.

3. **Sequence and control points**: (1) make bars — press the mix into 100×20×20 mm bars and scribe two 100 mm datum lines; (2) measure the datum lines after drying → **drying shrinkage** (commonly 2%–5%); (3) fire to this mix's service band (judged with the cone set), measure cold → **firing shrinkage** (commonly 5%–10%); (4) **mold enlargement** — mold length = target length ÷ (1 − total shrinkage); example: a 200 mm brick at 8% total shrinkage → 200÷0.92 ≈ 217 mm; (5) the same bar checks distortion (a mix warping >2% gets its grog share raised and is retested) and cracks (crazing = drying too fast or too much plastic clay). Control point: mold straight to target dimensions without measuring and every finished piece comes out undersized.

4. **Empirical parameters and calibration**: drying 2%–5%, firing 5%–10% (experience values, measured per batch, never carried over); grog 50%–70%; warping >2% means more grog and a retest; rough color test — light (white, gray-white) and greasy clay usually fires more refractory; deep red carries iron, drops refractoriness, and easily stains the melt.

5. **Observations to record**: both datum lengths (after drying, after firing); warping amount; crack pattern (crazing / straight crack); kiln position and stratum of the bar; batch number and clay color.

6. **Pass / rework / scrap criteria**: pass = datum readable, warping ≤2%, no crazing, both shrinkages and the enlargement factor computed; rework = warping >2% or crazing — raise the grog share, remake the bars and retest; scrap = the bar breaks up and no datum can be measured (too much plastic clay or drying too fast) — remix the whole batch.

7. **Common failures and diagnosis order**: (1) bricks firing smaller and smaller with joints opening → the shrinkage was never measured: remake by the mold-enlargement method; (2) crazing → drying too fast or too much plastic clay: add grog and lengthen shade-drying; (3) warping >2% → too little grog, add grog and retest; (4) bar data disagree with the product → datum lines not scribed or the rule not zeroed against the standard rod; (5) the batch fires deep red → high iron, low refractoriness: take material from another stratum and retest.

8. **L1 / L2 / L3 evidence**: L1 = one batch's two shrinkage readings plus one mold-enlargement calculation; L2 = the shrinkage archive on file by batch number (remeasured with every new clay batch); L3 = the local "material color — shrinkage — refractoriness" triple archive in the ledger, with brick and lining sizes reproducible.

#### 12.6.2 The Three-Layer Furnace Lining

| Layer | Function | Material | Thickness (empirical value) |
|---|---|---|---|
| Refractory face | takes the fire and the slag | refractory base mix, precast brick or monolithic ramming | 5–10 cm |
| Insulation layer | blocks heat escaping outward | wood ash mixed with clay, chopped-grass mud, (if available) crushed pumice | 5–10 cm |
| Structural layer | carries load and protects | ordinary adobe or coarse ceramic brick | per structure |

**The value of the insulation layer is chronically underestimated**: with the same fuel and air, a well-insulated firebox runs one to two cone levels hotter — **insulation is temperature**. Rough thermal-resistance arithmetic: resistance ∝ thickness ÷ conducting ability; the ash mix conducts about 1/3–1/5 as well as dense refractory mud (empirical value), so a 5 cm ash insulation layer matches the resistance of 15–25 cm of solid refractory mud — **ash is far better value than brick**. Acceptance criterion (◎ hand-feel + compensation): after 2 h of running, the outer wall "bearable against the back of the hand for 3 s" ≈ within 60–70 °C = pass; too hot to touch = large heat loss; shut down and thicken the insulation. Ash is free; collect it from the ash pit after every firing.

**Rammed lining and the bake-out curve**: fill refractory mud between formwork and furnace shell in layers, ramming each layer tight with a wooden mallet (each layer ≤3 cm, rammed until it stops compressing), shade-dry for several days, then **slow-bake** — first-bake curve: low fire (hand-feel "warm" tier) for 2–4 h to drive off free water (**white steam at the chimney; no temperature rise until the steam runs clean**) → 100–300 °C for 1–2 h → 300–600 °C until every trace of water vapor is gone → up to red heat. **Rush the first bake and the steam blows cracks straight into the lining — the number-one cause of failed furnace builds.** During the first bake, no one stands in front of the furnace.

**Wear points and countermeasures**: around the air ports (fiercest oxidation and erosion) use **independent air-port bricks** (precast, extractable for replacement); the furnace floor (slagged and loaded) uses replaceable floor plates; baffle-wall top and furnace roof get periodic visual checks.

**Repair procedures**:
- **Cold repair** (standard): shut down and cool completely → chisel away the friable layer down to sound material (solid knock sound) → brush on slip → fill with refractory mud, compacting in layers → shade-dry → slow bake. Erosion beyond 1/3 of lining thickness means a full overhaul.
- **Hot patching of holes** (emergency): press a ball of refractory mud (the less water, the safer) into the hole — **stand to the side, face away**; the vaporizing water will spatter.

**Inspection system**: a cold walk-around after every firing (visual check + tap-sounding for hollow spots; a hollow spot sounds dull); every 10 firings, erosion depth measured with the fixed scribed rod; seasonal maintenance (roof repaired and drainage cleared before the rainy season). The data goes into the ledger (the furnace-and-kiln page of the Chapter 39 inspection system starts here).

[Card 12-03 Rammed Lining and First-Bake Curve] (eight fields)

1. **Input materials**: refractory face material (refractory base mix: grog 50%–70% + refractory clay 30%–50%, precast brick or monolithic ramming); insulation material (wood ash mixed with clay, chopped-grass mud, crushed pumice if available); structural material (ordinary adobe or coarse ceramic brick); water; formwork and furnace shell.

2. **Tools required**: formwork and shell; wooden mallet (layer-by-layer ramming); scribed rod (erosion depth); drip clock (first-bake timing, Chapter 3); the back of a hand (outer-wall temperature criterion); record sheet. Calibration source: outer-wall temperature is substituted by "bearable against the back of the hand for 3 s" ≈ 60–70 °C; first-bake stages by hand-feel grade plus white steam.

3. **Sequence and control points**: build or ram three layers — refractory face 5–10 cm, insulation 5–10 cm, structural per structure → fill refractory mud between formwork and shell, ramming each layer with the mallet (each layer ≤3 cm, rammed until it stops compressing) → shade-dry several days → **slow first bake**: low fire (hand-feel "warm" tier) 2–4 h to drive off free water (white steam at the chimney; **no temperature rise until the steam runs clean**) → 100–300 °C 1–2 h → 300–600 °C until every trace of vapor is gone → up to red heat. Control points: a rushed first bake lets steam blow cracks into the lining — the number-one cause of failed builds; nobody stands in front of the furnace during the first bake.

4. **Empirical parameters and calibration**: refractory face 5–10 cm, insulation 5–10 cm; ramming ≤3 cm per layer; low fire 2–4 h, 100–300 °C 1–2 h, 300–600 °C until vapor is gone; outer wall "3 s by hand" ≈ within 60–70 °C; the ash mix conducts about 1/3–1/5 as well as dense refractory mud, so 5 cm of ash insulation equals 15–25 cm of solid refractory mud (empirical value).

5. **Observations to record**: volume of white steam and when it stops; time spent in each band; outer-wall hand-feel after 2 h of running; cracks by eye (hairline / through); hollow sound on tapping; scribed-rod erosion readings (every 10 firings).

6. **Pass / rework / scrap criteria**: pass = no through crack after the first bake + outer wall bearable for 3 s after 2 h of running; rework = hairline cracks (narrower than a fingernail) marked and watched, not treated (heating expansion often closes them), and local hollow spots cut out, patched, and re-baked; scrap = a through crack (light or smoke passes) still leaking after patching, a fallen arch block, or erosion beyond 1/3 of lining thickness — full rebuild.

7. **Common failures and diagnosis order**: (1) lining blown apart on the first bake (most common) → heating too fast or lining too wet: cut out and patch, re-bake, and lengthen the low-temperature stage for the next build; (2) outer wall too hot to touch → insulation thin or damp: shut down and thicken the ash layer; (3) dull hollow sound on tapping → ramming not tight (a layer over 3 cm or not rammed to refusal): cut out and re-ram; (4) furnace temperature won't rise and the first-bake record is incomplete → the lining never dried through and absorbs heat every firing: a thorough slow bake; (5) rapid erosion around the air ports → the most severe oxidizing scour is there: fit replaceable air-port bricks.

8. **L1 / L2 / L3 evidence**: L1 = one lining through its first bake with no through crack and a 3 s outer wall; L2 = the three-layer lining's first-bake curve on file, with cold and hot repairs following the procedure; L3 = scribed erosion readings and the repair cycle in the Chapter 39 inspection ledger, with the life account used for scheduling.

### 12.7 How to Measure and Compare High-Temperature Processes

There is no thermometer (the glass thermometer waits for Chapters 14+25). The general principle reverts to Chapter 3: **replace absolute measurement with comparative measurement** — one criterion sequence such that anyone, following the record, reproduces the same conclusion.

**Tier 1: the fire-color table (auxiliary empirical method, not quantitative)** — its limits must be stated: affected by ambient light, smoke, and viewing angle; error on the order of ±100 °C; for coarse grading only, **never to be treated as quantitative measurement**.

| Fire color | Approximate temperature band (empirical value) |
|---|---|
| Dark red first visible | about 500–600 °C (needs a dark background) |
| Dark red to bright red | about 600–800 °C |
| Bright red turning orange | about 800–950 °C (lime burn-through stage) |
| Orange-yellow | about 950–1100 °C |
| Bright yellow to yellow-white | about 1100 °C and above (glass and reduction stages) |

**Tier 2: the standard test-piece method (Section 6.7 made formal)**: place in the same furnace small pieces of known behavior — a clay chip (sinters hard and changes color), a limestone chip (a burned-through layer appears on the fracture), a glass bead (melts round) — and grade by state on unloading.

**Tier 3: the slump-cone set method (established this chapter; the locally calibrated "temperature scale")**:

1. Make small cones from reference materials of known melting/softening point: table salt (melting point about 801 °C, pure grade; coarse salt reads lower); potassium carbonate (about 891 °C, Chapter 8 ash-alkali purification); homemade glass (softening range about 700–900 °C); quartz sand grains (>1400 °C, does not melt; serves as the high-end "unmelted" marker).
2. Method: press each material into a half-finger-tall small cone and set it in a numbered clay-tile stand.
3. Use: place the cone set at representative positions in the furnace (center/edge/top/bottom); read the temperature band on unloading by the "bent over / melted down / unchanged" sequence.
4. **Calibration regime**: each reference material is calibrated once against a known stable kiln temperature; from then on the cone set's readings are the team's temperature language. Cone numbers and readings go into the firing archive.

**Handling spatial non-uniformity**: four cone sets in one firing map this furnace's temperature distribution — the map decides where the glass crucible goes and where the ore goes (Chapter 18). The distribution maps of successive firings should agree; disagreement = furnace-condition drift; check the lining and the flues.

[Card 12-04 Slump-Cone Thermometry] (eight fields)

1. **Input materials**: reference materials of known melting/softening point — table salt (melting about 801 °C, pure grade; coarse salt reads lower), potassium carbonate (about 891 °C, Chapter 8 ash-alkali purification), homemade glass (softening range about 700–900 °C), quartz sand grains (>1400 °C, does not melt; the high-end "unmelted" marker); numbered clay-tile stands.

2. **Tools required**: small cones (each material pressed half a finger tall); clay-tile stands and numbers; long rod (to place and retrieve cones at representative positions); firing archive. Calibration source: each reference material is first calibrated once against a known stable kiln temperature, after which cone readings are the team's temperature language; the fire-color table is auxiliary only (±100 °C order, never quantitative).

3. **Sequence and control points**: (1) make small cones from the reference materials, press each half a finger tall, set them in numbered clay-tile stands; (2) place the cone sets at representative positions (center / edge / top / bottom); (3) on unloading read the temperature band by the "bent over / melted down / unchanged" sequence; (4) four sets in one firing map the furnace's temperature distribution. Control points: numbers and readings go into the firing archive; successive distribution maps must agree — disagreement = furnace-condition drift, check the lining and the flues.

4. **Empirical parameters and calibration**: salt ≈801 °C, potassium carbonate ≈891 °C, homemade glass softening 700–900 °C, quartz sand >1400 °C unmelted; cone height half a finger; fire-color table ±100 °C order (auxiliary, not quantitative); natural draft tops out around 1000–1100 °C and forced draft reaches about 1200–1400 °C, with cone readings deciding (empirical values, calibrate locally).

5. **Observations to record**: "bent over / melted down / unchanged" for every cone in every set; the positions of the four sets; fire and smoke color in the same firing; time for the cones to advance a level (heating rhythm); differences from the previous firing's map.

6. **Pass / rework / scrap criteria**: pass = the same position reads the same level reproducibly (three consecutive firings agreeing); rework = one set reads oddly — check whether that spot sees a direct flame or a cold-air short circuit, then re-place that set; scrap = a reference material has absorbed moisture or been contaminated so its melting point drifts (salt deliquesced, ash alkali impure) — discard that batch of cones and remake.

7. **Common failures and diagnosis order**: (1) cones slow to advance → walk the 12.4.2 tree first (fuel → air → charge → lining → flue), never blame the cones first; (2) the same position drifts firing by firing → local lining erosion or flue ash; (3) the edge set reads a full level below the center → uneven distribution: adjust charging, baffle wall, and smoke ports; (4) cone reading contradicts fire color → trust the cone; fire color is skewed by ambient light and smoke; (5) cones of unequal height → readings not comparable: remake to a uniform half-finger height.

8. **L1 / L2 / L3 evidence**: L1 = one four-set reading plus this furnace's distribution map; L2 = three consecutive firings reading the same level at the same position, with band judgments and shrinkage runs both using the cones; L3 = cone numbers and calibration records in the firing archive, and a second person reading independently to the same result from this card.

### 12.8 Furnace Maintenance and Life Management

**Inspection cycle table**:

| Cycle | Items |
|---|---|
| Every firing | cold walk-around: cracks, hollow spots, visual erosion depth; clean air-port bricks, grate, ash pit |
| Every 10 firings | erosion depth measured (scribed rod); rotate or replace air-port bricks; clean flue ash |
| Quarterly | furnace roof waterproofing, surrounding drainage; tighten timber-frame lashings; spare-parts inventory |

**Crack classification and handling**: hairline cracks (narrower than a fingernail is thick) — mark and observe, no action; thermal expansion on heat-up often closes them by itself; through cracks (light/smoke passes through) — cold repair with a dug-out patch; vault spalling — local rebuild; merely smearing the surface is forbidden.

**The life account**: under frequent high temperature (cone levels above 1100 °C) the lining overhaul cycle is about 20–50 firings; at medium temperature about 100 firings (empirical values, must be field-calibrated). **Overhaul labor and materials go into that process's cost account** (Chapter 38): better to run one temperature level lower than to burn until the lining is destroyed.

**Spare-parts stock (a floor triggers restocking)**: precast air-port bricks ×4, floor plates ×2, grate clay bars ×6, half a basket of dry refractory mud mix, sealing hemp tow and animal fat, clay air pipes ×2. When stock falls below the floor, shut down and restock; never run ailing.

**Kiln care regime**: before laying a kiln up, fire it through to drive out moisture and seal the openings against rain; on return to service, slow-bake the first firing per the first-bake curve — a kiln is an asset that can be "starved" and "rain-ruined".

---

### 12.9 Crucible Specialization: A Vessel That Takes Heat, Shock, and Corrosion at Once

Glass melting (Chapter 14) and the metallurgy that follows both demand a vessel that "holds its charge while being fired." It carries three requirements beyond a furnace lining: thermal-shock resistance (cold charges alternate with hot), no reaction with the charge, and a rim that can be gripped for carrying. Ordinary pottery cracks within three firings; crucibles must be made as a dedicated line and booked separately.

**Mix (a high-grog variant of the refractory base mix)**: the crucible does not fear shrinkage, it fears cracking, so grog goes to the upper limit. The blend tier is picked among three tiers by live testing, never by hand-feel:

| Variant | Refractory clay | Grog (coarse:fine = 2:1) | Use |
|---|---|---|---|
| A baseline | 40% | 60% | medium-temperature charges, trial firings |
| B standard | 35% | 65% | default for glass melting |
| C extreme | 30% | 70% | high-temperature trials; insufficient plasticity, prone to delamination; verify with test bars batch by batch |

Coarse grog grains at rice-grain size (a skeleton against cracking), fine powder fills the gaps. Press test bars for all three variants in the same batch (the 12.6.1 method) and choose the highest grog tier that "fires without cracks and warps ≤2%" — **re-select with every new batch of clay**; the tier and the batch number go into the ledger.

**Forming (coil building, thick-walled)**: thick-walled large pieces exceed Chapter 11's wheel-throwing capability, so coil-build: clay coils thumb-thick, one ring pressed onto the next, seams scored and compressed. Wall 15–20 mm, floor 25–30 mm (empirical starting point: wall ≈ 1/10 of mouth diameter; revise in the field by working back from where the first piece cracked); thicken the rim with a turned flange (the load point for carrying, and also the most crack-prone spot). Shade-dry ≥7 days, covered with hemp cloth against drying cracks. Criteria: the wall-thickness shadow uniform under raking light; the tapping sound identical everywhere (a dull spot = delamination; cut up a scrapped piece to inspect the ring seams).

**Pre-firing curve (empty firing in stages; hard protocol)**: a new crucible must be pre-fired empty once before it may take a charge: ① bake beside the stove 1–2 days (hand-feel "warm" tier) → ② into another kiln at the low-fire stage for 2–3 h, holding at first visible dark red → ③ raise to the bright-red band (about 800 °C, aligned with this kiln's cone level) and hold 1 h → ④ cool naturally with the kiln. Criteria: knock sound crisp throughout with no dull spots; **filled with water overnight, the outer wall shows no damp patches** = pass. Skipping stages and firing fast = explosive cracking and scrap; there is no rework path.

**Life ledger and scrap criteria**: each piece numbered; after every firing, measure wall thickness cold at three points with calipers (below the rim, mid-body, near the floor) and log the weight. Three-way criteria:

- **Pass**: thinnest wall of the three points ≥2/3 of original wall, no through cracks, interior growths removable by scraping;
- **Reworkable**: small rim chips, hairline cracks on non-slag-facing surfaces — patch with refractory mud, shade-dry, then repeat the pre-firing curve;
- **Scrap**: wall eroded beyond **1/3 of original wall** at any point, leaked through, or floor cracked. The 1/3 erosion line is a dead line — a thin-walled crucible is not "still usable", it is next firing's melt-through accident.

Precursors of through-leakage (a silent failure; first, record how to detect it): glaze beads on the outer wall, a bright-lined fire color in a local patch of the wall, ledger weights falling faster firing by firing — on any one of the three, downgrade to watch status: fire only medium- and low-temperature charges and tighten the inspection interval.

**Fitting the crucible tongs**: the jaw curve is matched to the crucible's outer-wall curve — **bend them using a scrapped crucible as the template**; wrap the jaws with three layers of wet hemp rope (heat insulation + grip + prevents pinch-cracking). Acceptance (cold): a crucible full of sand carried 10 steps without slipping or pinch-cracking. Fit compensation criterion: a sheet of paper between jaw and wall — the paper can be drawn out but the crucible cannot be lifted = too loose; the paper cannot be drawn and the wet rope's imprint dents the wall = too tight. ◎ hand-feel: grip force — practice: carry a cold crucible full of sand 20 times, then two different crucibles 20 more; misjudgment compensation: replace hand-feel with the paper criterion and the depth of the wet-rope imprint.

[Card 12-06 Crucible Manufacture and Pre-Firing] (eight fields)

1. **Input materials**: refractory clay (a batch whose 12.6.1 test bars passed); grog 60%–70% (coarse:fine = 2:1, coarse grains at rice-grain size); hemp cloth (cover for shade-drying); substitute: if grog runs short, drop to variant A (clay 40% / grog 60%) and thicken the wall by 2 mm, with the life penalty booked. Three variants: A 40/60 medium-temperature charges and trial firings, B 35/65 the glass-melting default, C 30/70 high-temperature trials (insufficient plasticity, prone to delamination — verify with test bars batch by batch).

2. **Tools required**: calipers (zeroed against the standard rod); a scrapped crucible as template (for the jaw curve); clay-compacting board; another kiln's low-fire stage (for pre-firing); wet hemp rope (three wraps on the jaws). Calibration source: three-point wall thickness with calipers against the standard rod; the pre-firing end point aligned with this kiln's cone level; jaw fit by the paper-sheet criterion in place of hand-feel.

3. **Sequence and control points**: press test bars for all three variants (the 12.6.1 method) → choose the highest grog tier that "fires without cracks and warps ≤2%", re-selected with every new clay batch, tier and batch number into the ledger → coil-build the form (coils thumb-thick, one ring pressed onto the next, seams scored and compressed; wall 15–20 mm, floor 25–30 mm; rim thickened with a turned flange) → shade-dry ≥7 days under hemp cloth against drying cracks → **pre-firing (empty firing in stages; hard protocol)**: (1) bake beside the stove 1–2 days (hand-feel "warm" tier) → (2) into another kiln's low-fire stage for 2–3 h, holding at first visible dark red → (3) raise to the bright-red band (about 800 °C, aligned with this kiln's cone level) and hold 1 h → (4) cool naturally with the kiln. Control point: no skipping stages — a rushed, skipped pre-fire cracks the piece and there is no rework path.

4. **Empirical parameters and calibration**: grog 60%–70% (coarse:fine 2:1); wall 15–20 mm / floor 25–30 mm (empirical starting point: wall ≈ 1/10 of mouth diameter, revised by working back from where the first piece cracked); shade-dry ≥7 days; pre-fire (1) 1–2 days (2) 2–3 h (3) about 800 °C held 1 h; scrap deadline: erosion beyond 1/3 of the original wall at any point.

5. **Observations to record**: shade-drying cracks; knock sound (uniform everywhere; a dull spot = delamination); **outer wall free of damp patches after a night full of water**; three-point wall thickness each firing (below the rim, mid-body, near the floor) plus weight; the three through-leak precursors — glaze beads on the outer wall, a bright-lined fire color in a local patch, weight falling faster firing by firing.

6. **Pass / rework / scrap criteria**: pass = no damp patch after a night of water + crisp knock sound throughout with no dull spot + thinnest of the three points ≥2/3 of the original wall; rework = small rim chips or hairline cracks on non-slag faces — patch with refractory mud, shade-dry, and repeat the pre-firing curve; scrap = wall eroded beyond 1/3 of the original at any point, a through leak, or a floor crack (a dead line: a thin-walled crucible is not "still usable", it is next firing's melt-through accident).

7. **Common failures and diagnosis order**: (1) explosive cracking → check whether the pre-fire skipped stages and whether the clay was too wet; (2) dull spots (delamination) → check coil-seam compaction, seams not scored and pressed; (3) erosion too fast → check whether ash alkali got into the mix (Chapter 8, alkali attacks crucibles) and whether flame plays directly on the wall (baffle wall failed); (4) through leak → re-measure the three points in the ledger; wall erosion past 1/3 not scrapped is the most common cause; (5) the rim cracks first → the rim was not thickened with a flange (the carrying load point, and the most crack-prone spot).

8. **L1 / L2 / L3 evidence**: L1 = the first piece passes its empty pre-firing (seepage test passed + wall ≥2/3); L2 = the ledger continuous across three firings (three-point thickness + weight); L3 = every piece numbered and the ledger continuing into the Chapter 39 inspection system, with life and scrap criteria traceable.

### 12.10 Rough Furnace Heat Balance: Where a Kiln's Fuel Actually Goes

The aim is not accuracy but **priority ranking**: know which path the biggest share of heat escapes by and you know what to modify first. Throughout, use "shares" (heat input = 100 shares) as the comparative unit, not absolute calorific values.

**Fuel tiers**: for the ranking see Chapter 23 (equal weights: wood < peat < lignite < charcoal < bituminous coal ≈ anthracite); in the field only three tiers are used — damp wood (less than half a share of dry wood), dry wood, charcoal (about 1.5–2× the same weight of dry wood). Calibration without a calorimeter — **boiling-water timing comparison**: burn equal weights of fuel under the same pot of the same amount of water, record the minutes to boil, and derive the team's "fuel tier table"; damp-wood criterion: two sticks struck together sound dull = damp; charge it at the damp tier.

**Rough four-path heat-loss table (comparative, empirical values pending ledger correction)**:

| Path | Rough share | Field evidence | How to plug it |
|---|---|---|---|
| Carried off by flue gas (incl. excess air) | natural-draft furnace 40–60 shares, the largest | scalding, copious smoke at the ports; yellow smoke = losing even more | shrink the chamber to concentrate heat; match the air; preheat the intake |
| Wall losses | bare furnace 20–30 shares; well insulated 10–15 shares | back of hand on the wall (the 12.6.2 criterion) | thicken the ash insulation layer |
| Heat-storage loss (a cold furnace absorbs heat) | intermittent furnace, first firing 15–25 shares; diluted by continuous burning | a cold furnace heats slower than a hot one on the same fuel | run the kiln cluster back-to-back, staggered; avoid cold furnaces |
| Incomplete combustion (CO + soot) | 10–30 shares with poor air matching | yellow soft flame; black soot in the flue | adjust the air per 12.1/12.4 |

Order-of-magnitude self-check: the four paths should sum to roughly 100 shares; if the "useful heat" you compute exceeds 30 shares, this table has been misapplied — a firing kiln's useful heat is usually only 5–20 shares; the rest is lost along the way.

**"Firewood per firing" budget worked example**: one pottery firing (50 pieces loaded) has a baseline actual of 200 kg dry wood (take the median of 5 consecutive firings from the ledger as the baseline, never the best one). Budget formula:

> Budget = baseline × (1 + cold furnace 0.2 + rainy-season damp fuel 0.1 − insulation retrofit 0.15)

In this example, a cold furnace plus a rainy-season first firing: 200×1.3 = 260 kg — stock up to the budget; actual use 20% over budget triggers the 12.4.2 diagnostic tree; grinding on regardless is not allowed.

**Payoff ranking of insulation retrofits (plug the biggest, cheapest path first)**: ① seal air-leaking joints (slurry the seams, half a day; directly cuts excess air); ② thicken the ash insulation layer (ash is free, one day); ③ lengthen the flue to preheat the intake air (two to three days); ④ thicken the lining and rebuild (several days, smallest payoff, comes last). Criterion: record 3 baseline firings' firewood before and after each retrofit; a drop of ≥10% counts as effective; an ineffective retrofit is undone and logged.

[Card 12-07 Rough Heat Balance] (eight fields)

1. **Input materials**: the firewood ledger for 5 consecutive firings (the median taken as baseline, never the best one); the fuel tier table; this furnace's temperature distribution map (four cone sets); time to each cone level and smoke-color records.

2. **Tools required**: lever balance (checked against the standard weights); drip clock (Chapter 3); boiling-water timing comparison (fuel tiers calibrated by burning equal weights under the same pot of the same amount of water and recording minutes to boil). Calibration source: throughout, "shares" (heat input = 100 shares) are the comparative unit, never absolute calorific values; two sticks struck together sounding dull = damp, charged at the damp tier.

3. **Sequence and control points**: (1) fix the fuel tier (damp wood under half a share of dry wood / dry wood / charcoal about 1.5–2× the same weight of dry wood) → (2) estimate shares along the four paths — carried off by flue gas incl. excess air (natural draft 40–60 shares, the largest), wall losses (bare furnace 20–30, well insulated 10–15), heat storage (intermittent furnace, first firing 15–25), incomplete combustion (poor air matching 10–30) → (3) **closure check**: the four paths should sum to roughly 100 shares; if the computed "useful heat" exceeds 30 shares the table has been misapplied (a firing kiln's useful heat is usually only 5–20 shares) → (4) firewood budget per firing: budget = baseline × (1 + cold furnace 0.2 + rainy-season damp fuel 0.1 − insulation retrofit 0.15), e.g. 200×1.3 = 260 kg, and stock to the budget → (5) retrofit payoff order: seal air-leaking joints → thicken the ash insulation → lengthen the flue to preheat the intake air → thicken and rebuild the lining. Control points: the closure check is mandatory; the baseline is the median, never the best firing.

4. **Empirical parameters and calibration**: four-path shares flue 40–60 / wall 20–30 (10–15 when insulated) / storage 15–25 / incomplete 10–30 (comparative; empirical values, corrected from the ledger); useful heat 5–20 shares; budget coefficients cold furnace 0.2, rainy-season damp fuel 0.1, insulation retrofit −0.15; actual use 20% over budget triggers the 12.4.2 tree; a retrofit counts as effective at a drop of ≥10%, measured against 3 baseline firings before and after.

5. **Observations to record**: firewood per firing; time to each cone level; smoke color (yellow smoke = losing even more); outer-wall hand-feel; the heating difference between a cold and a hot furnace on the same fuel; 3 baseline firings before and after each retrofit.

6. **Pass / rework / scrap criteria**: pass = the four paths closing to ≈100 shares + the budget holding (actual within ±20% of budget); rework = the paths will not balance — look for a forgotten path (open-door radiation, water evaporating from damp charge) and recompute; scrap = two consecutive firings over budget — go back to the fuel tier and the air matching (12.4.2), undo the ineffective retrofit and log it.

7. **Common failures and diagnosis order**: (1) the four paths will not balance → a path was left out (open-door radiation, water from damp charge); (2) actual use 20% over budget two firings running → the fuel tier was mis-booked (damp wood counted as dry) or air matching has worsened; (3) no drop after a retrofit → the wrong path was plugged: plug the biggest, cheapest one first, the leaking seams; (4) "useful heat" comes out too high → the table is misapplied, flue sensible heat counted as staying in the furnace; (5) a cold furnace heats slower than a hot one on the same fuel → the storage term is underestimated.

8. **L1 / L2 / L3 evidence**: L1 = one closed four-path share sheet; L2 = 10 consecutive firings with actual use within ±20% of budget; L3 = the retrofit payoff account in the Chapter 38 materials-and-energy ledger, with stocking scheduled to budget.

### 12.11 Fuel Store and Kiln-Side Logistics: the Heat-Balance Account Starts in the Storehouse

**Dry-wood shed capacity design**: stock floor = 3 high-temperature firings' worth + 1 month of stove cooking and heating (empirical starting point; correct to your team's output). Worked example: a high-temperature firing takes 100 kg charcoal, daily stove cooking takes 20 kg/day dry wood → shed floor: dry wood ≥1 t, charcoal ≥0.5 t. Three components, none optional: **moisture-proof racks** (stone footings, timber frame, rack surface about 30 cm off the ground — two palms high; rising ground moisture is the top cause of damp bottom-layer wood); **roof** (eaves overhang the stack; eave drip must not land on the stack top); **ventilation** (shed open at both ends; a fist-wide air channel between stacks). Acceptance: two sticks drawn from the stack core and struck together sound crisp = dry; no white mold on the rack surfaces, no termite tunnels (insect and fire prevention per the Chapter 13 building discipline).

**Woodstack discipline**: height limited to one person (fermentation heat inside tall stacks is the starting point of smoldering); 3 paces between stacks; first in, first out; a tag on the stack side records the month of intake.

**Kiln-side fuel-stack safety distance** (cites the Chapter 13 fire spacings: fire work 15 paces, fuel stacks 8 paces, doubled in windy areas): only **one firing's single charge** (≤half a basket) sits at the kiln side; the main fuel stacks stand back ≥15 paces from fire work and ≥8 paces apart; within one pace of the kiln a full water vat + 2 wet hemp sacks are kept at all times. Observable criterion: from any ignition point, a fuel stack is beyond one arm's reach.

**Charcoal store management (two lines: moisture and spontaneous combustion)**: moisture — damp charcoal drops a fuel tier and crumbles to powder after re-drying; rack storage, covered; spontaneous combustion — **hot charcoal fresh from the kiln must never enter the store; cooled through overnight is a hard rule**; stacks height-limited, with a hand-probe hole left in each stack; probe by hand before each shift; any warmth means turn the stack and spread it to cool. Three store-entry criteria: cool (back of hand against the stack core feels no warmth), dry, crisp knock (Chapter 6 criteria).

**Material flow and handling person-hours per firing**: the flow runs one way, no doubling back — shed → kiln side → ash pit → ash store; the charcoal path and the ash path are separate (keeps ash out of the charcoal). Worked example: a high-temperature firing needs 100 kg charcoal + 40 kg slag clearance, shed 30 paces from the kiln (about 20 m): a basket carries 20 kg/trip, so 5 charcoal trips + 3 slag trips, 2 min handling + 1 min round trip per trip → about 25 min ≈ 0.5 person-hours/firing. This account is not small change: every 30 paces farther the kiln sits, a firing costs about 0.2 extra person-hours; multiply by the year's firing count and enter it in the Chapter 38 ledger — moving the fuel shed 30 paces closer on the site map is a worker gained for free.

### 12.12 Multi-Furnace Workshop Layout: the Kiln Cluster, the Water Channel, and the Watch House

One furnace can burn; only a cluster is a workshop. Three costs of a bad layout: fire riding the wind from furnace to furnace (fire safety), the downwind furnace eating the upwind furnace's smoke (mutual smoke fouling), and materials hauled back and forth (labor hours wasted). The three constraint sets, laid out in one pass:

**Fire-work spacing and wind direction** (spacing base cites Chapter 13: 15 paces between fire works, doubled in windy areas):

| Furnace | Wind position | Adjacent constraint |
|---|---|---|
| Glass furnace | most upstream | far from dust sources (sand yard, ash pit) — ash falling into the melt means bubbles and scrap |
| High-temperature furnace (iron/crucibles) | upwind side, ≥15 paces downwind of the glass furnace | crucible shed and spares room set beside the furnace but not shared with it |
| Forge | midstream, ≥15 paces from the woodworking shop | nothing combustible within one arm's reach of the spark zone |
| Lime kiln | downwind end | heaviest smoke and dust; beside the stone pile and the slaking pools |

Adjacent chimney mouths staggered ≥1 m in height, so one kiln's smoke cannot pour into another's air ports; **the downwind furnace's air inlet must not face the upwind furnace's smoke port** — criterion: test the draft at the downwind furnace's air port with a wet grass bundle; smoke pouring sideways across = violation; widen the spacing or stagger the firing times. The prevailing wind is taken from a full season measured with wind flags (cloth-strip poles), never by feel; after a seasonal wind shift, revise the site map to the new direction.

**Shared water channel and ash pit**: the channel runs one way, upstream → downstream, positions ranked by decreasing water cleanliness — glass furnace (cleanest) → forming-shed panning pool → lime slaking pool → ash-pit drain. The shared main ash pit sits at the site's downwind end, ≥15 paces from every fire work, dug deep and covered against rain; ash entering the pit must pass the Section 6.8 extinguishing acceptance; the ash pit is also the year-round source of insulation material (12.6.2) and mortar admixture; keep an ash-collection walkway beside the pit so taking ash never disturbs the stacks.

**Watch house siting**: side-rear of the site, upwind; one window must see the fire color at both the high-temperature furnace mouth and the lime kiln mouth (the watch's core task is spotting fire-color anomalies); ≥15 paces from the nearest fire work, 8 paces from the fuel shed; no firewood stored inside — only that night's hearthside quantity. Night watch is two people; shift changes sign off against the firing archive.

**Site map system**: one map pins down five elements — wind vane, every furnace position, one-way material-flow arrows, water-channel direction, fire points and water vat locations; the 15-pace/8-pace spacing stakes planted in the ground; one map-based inspection per quarter; every map revision saved to the ledger as it happens.

## Master Parameter Table

| Parameter | Value | Class |
|---|---|---|
| Air needed to burn 1 kg charcoal | about 8–9 kg (≈7 m³) | order of magnitude |
| Natural-draft ceiling | about 1000–1100 °C | empirical |
| Reachable with manual blast | about 1200–1400 °C | empirical (cone readings are the authority) |
| Flue cross-section | ≥1.5× total air-port area | empirical |
| Bellows output | 30–40 L/stroke; 30 strokes/min ≈1 m³/min | empirical, bag-method calibrated |
| Target in-pipe air velocity | 10–25 m/s | empirical window |
| Baffle-wall passage height | about 1/3 of firebox height | empirical |
| Drying/firing shrinkage | 2–5% / 5–10% | empirical, measured per batch with test bars |
| Grog blend share | 50%–70% | empirical |
| Insulation acceptance | outer wall ≤60–70 °C (back of hand 3 s) | criterion |
| First-bake white-steam rule | no temperature rise while the steam runs dirty | hard protocol |
| Lining overhaul cycle | high temperature 20–50 firings / medium about 100 | empirical |
| Crucible grog share | 60%–70% (coarse:fine = 2:1), tier picked by three-tier live testing | empirical |
| Crucible wall/floor thickness | 15–20 / 25–30 mm | empirical, worked back from the first crack location |
| Crucible scrap dead line | any point eroded beyond 1/3 of the original wall | hard protocol |
| Heat-balance four-path shares | flue 40–60 / wall 10–30 / storage 15–25 / incomplete 10–30 shares | comparative, ledger-corrected |
| Kiln-cluster spacing | ≥15 paces between fire works, chimney mouths staggered ≥1 m | discipline |
| Kiln-side fuel distances | fire work 15 paces, between fuel stacks 8 paces (doubled in strong wind) | discipline (Chapter 13) |
| Handling person-hours per firing | ≈0.5 person-hours (30-pace shed-to-kiln example) | worked example, entered in the Chapter 38 account |

## Failure Modes and Diagnostics

(The full diagnostic tree is in 12.4.2; this table adds structural failures)

| Symptom | Candidate causes (by probability) | Verification | Action |
|---|---|---|---|
| Slump-cone set slow to advance a level | four causes and one symptom — run the 12.4.2 tree | item by item per the tree | handle per the tree |
| First bake blows the lining | heat-up too fast; lining material too wet | white-steam record | dig out, patch, re-bake; lengthen the low-temperature stage next batch |
| Outer wall too hot to touch | insulation layer thin / damp | back-of-hand method | thicken the ash insulation layer |
| Bricks shrink firing after firing, joints open | shrinkage never measured | re-run test bars | remake per the mold enlargement method |
| Flame doesn't pulse with the push rod | bellows valve leak (12.5 troubleshooting) | feel the air against your hand | clean/replace flaps |
| Air pipe hot, buzzing, whistling | pipe too small, velocity too high | the 12.4.1 table | go up one pipe diameter |
| Temperature distribution map drifts firing to firing | local lining erosion / flue ash buildup | scribed rod + grass-bundle draft test | patch / clean the ash |
| Charge fuses solid and will not settle | ash-pit buildup jacking up the grate | inspect through the clean-out | make per-firing ash clearing a rule |
| Crucible leaks through | wall eroded past 1/3 without scrapping (most common); pre-fire stages skipped; flame striking the wall directly | ledger three-point wall re-measurement; tap for dull spots; check whether the baffle wall has failed and the flame hits the wall | scrap immediately; reset the baffle wall; next crucible one wall grade thicker |
| Woodshed damp, calorific value down | roof leaking; rising damp at the rack surface; fermentation heat inside stacks | strike two sticks and listen; boiling-water timing against the fuel tier table | send damp wood to the stove first; repair the shed, turn the stacks; raise the per-firing fuel budget by 10% |
| Downwind kilns foul each other with smoke | spacing too small; chimneys at equal height; wind shifted without a map revision | wet grass bundle draft test at the downwind air ports; watch whether smoke pours across | widen spacing / stagger chimney heights; revise the site map; stagger firing times |

## Process Card Index

Cards 12-01 to 12-07 are all full eight-field cards, each copyable onto a single page.

## Acceptance Standards

- **L1**: one controlled experiment — same furnace, same charge, natural draft vs. leather bag bellows, half a firing each, with a recordable level difference in the cone readings; the piston bellows survives 100 consecutive strokes without failure.
- **L2**: the separated-firebox shaft furnace is built; cone readings consistent across 3 consecutive firings (same position, same level); twin-box continuous blast takes the cone set stably to the glass-softening level and above (about 900 °C+); valves and piston need only routine maintenance after 20 firings; the three-layer lining's first bake shows no through cracks; the shrinkage archive and the temperature distribution map are on file.
- **L3**: spare-parts stock never below the floor; the lining life account runs continuously and feeds scheduling (able to answer "how many firings does this furnace have left"); charcoal supply matched to the firing plan (Chapter 6 capacity account + Chapter 38 energy account); two or more members pass the full build–blast–measure–repair assessment independently. Evidence: firing archive, life ledger, assessment records.

## Labor, Manpower, and Consumption

| Item | Manpower | Labor hours (empirical values) |
|---|---|---|
| Furnace build (incl. drying waits) | 2 people | 4–6 net working days + 3–5 days shade-drying + 1 day first bake |
| One piston bellows | 1–2 people | 3–4 days (leather sewing takes half) |
| One firing (blast shifts) | 4 on blast in two shifts + 1 stoker | 6–9 h |
| One batch of shrinkage test bars | 1 person | 0.5 day (including firing) |
| Consumption / high-temperature firing | metallurgy charcoal 80–120 kg, animal fat 0.2 kg (lubrication) | into the Chapter 38 ledger |

## Safety Boundaries

- The furnace room follows Section 6.8's four CO iron rules: indoor furnaces must have a low air inlet and a high smoke vent; open the door to feed fuel; no one sleeps at its upwind head (Iron Law Seven).
- The near-fire end of the air pipe must be clay pipe; bamboo near fire = burn-through + a hearthside fire.
- Slow first-bake heat-up is a hard protocol: fast baking blows the lining; fragments and steam injure; during the first bake, no one stands in front of the furnace.
- When hot-patching holes, stand to the side, face away; carry crucibles and hot pieces with long tools and wet-rope-wrapped handles.
- Furnace ash is dumped only after passing the Section 6.8 extinguishing acceptance; hot ash into wooden boxes is strictly forbidden.
- No one stands at the end of the bellows pull rod (it can slip loose and spring back); unified rhythm calls for the two-person twin-box setup, to prevent collision injuries.
- Chronic smoke and CO exposure from long hearthside work is logged under Iron Law Seven; the protection system is in Chapter 49.

## A. Existing Tool List

Chapter 11: shaft kiln, refractory base mix, fired bricks, clay pipes, firing archive; Chapter 6: charcoal, smoke-color criteria, test-piece method; Chapter 7: lashed woodworking; Chapter 8: tar glue, animal fat, ash alkali; Chapter 9: workbench, templates, standard parts; Chapter 3: measurement and leveling datum.

## B. New Tools in This Chapter

Separated-firebox shaft furnace (baffle wall + grate + ash pit + chimney); replaceable air-port bricks, floor plates, grate clay bars; leather bag bellows; piston bellows (2 leather one-way valves, felt piston, two-person twin-box system); clay air pipes (selected per the pipe-diameter table); slump-cone thermometry set (salt/potassium carbonate/glass/quartz cones + numbered stands); air flow–pipe diameter–velocity conversion table; shrinkage test-bar regime and the mold enlargement method; rammed-lining tool set (formwork, rammer, scribed rod); the furnace-temperature diagnostic tree; the furnace-and-kiln ledger; crucible set (three-tier mix variants, fitted tongs, scrapped-crucible template); the fuel tier table and boiling-water timing comparison; the heat-balance share sheet; the kiln-cluster site map and spacing stakes; dry-wood shed and charcoal store (moisture-proof racks, stack-spacing stakes, temperature-probe holes).

## C. Unsolved Dependencies

Quantitative temperature measurement (glass thermometer Chapters 14+25; thermocouples long-term); continuous mechanical blast (waterwheel-driven automatic bellows awaits Chapter 21; for now manpower shifts tie directly to capacity); higher-refractoriness materials (bauxite and graphite await Part 4's mineral-source survey); slag-corrosion standards (backfilled after Chapter 18's real service conditions); air flow and pressure metering (no differential-pressure gauge; the comparative method closes the loop).

## Next-Step Dependencies

Chapter 13's lime kiln adopts the separated-firebox structure directly; Chapter 14's glass furnace = this chapter's furnace type + strong blast + glass-grade temperatures, with the slump-cone set as the temperature yardstick for glass recipes; Chapters 16–18's ore roasting and bloomery reduction are all designed inside this chapter's blast capacity ceiling, with slag-corrosion data backfilled into 12.6; after the Chapter 25 thermometer arrives, the cone set retires to coarse measurement; Chapters 38–39's furnace life account and inspection sheets upgrade directly from this chapter's ledger.
