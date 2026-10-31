# Chapter 18 From Ore to Iron

> Part 4 · Metals, Machinery, and Precision Manufacturing. This chapter pushes the furnace–air–charcoal–forging system of Chapter 17 on to iron: iron ore is reduced in the solid state inside the furnace into bloom (bloomery smelting), densified into wrought iron stock by repeated forging that expels the slag, and finally forged into the first iron tools. The whole route starts with no machine tools and no iron tools — the first iron tools are forged entirely with a stone anvil, stone hammers, copper tooling, and human power, and iron is then used to bootstrap the iron anvil and iron hammer.

## Chapter Objectives

- Build a shaft-type bloomery furnace (a direct-reduction furnace) and run it per procedure: charge makeup, furnace loading, blasting, endpoint judgment, iron drawing.
- Master **slag-flow temperature reading** (slag color and thread-length method) and basicity adjustment.
- Master the technique of **hot forging the bloom to expel slag** and the heat schedule, producing dense wrought iron stock.
- Forge the first iron tools (hammer, anvil, chisel bootstrap first), accepted by the three tests: fracture, repeated bending, use testing.
- Distinguish "getting iron" from "getting steel," and prepare stock for Chapter 19.
- Deliverables: ≥3 kg dense iron stock, one set of basic ironwork tools, a per-run parameter archive.

## Capability Boundary

**Can do:** 1.5–3 kg dense wrought iron per run (stable after L2); passing the three tests; graded operation of the iron stock library.

**Explicitly cannot do:**
- Continuous production of liquid pig iron (needs greater air volume and coke; listed as a Class-C item, see Section 18.8) — when white cast iron occasionally forms in the hearth, register it as an "accidental product"; the recovery route is in Section 19.8.2;
- Detection and removal of sulfur and phosphorus (no means available; only ore sorting as the gate plus labeling of brittleness sources);
- Capacity beyond workshop scale: kg-level per run, batch operation.

**External dependency:** Charcoal production capacity must come first (the Chapter 6 charcoal-kiln expansion is an L3 prerequisite — fuel supply cutoff is the most common historical failure of this route; see the Chapter 38 energy ledger).

## Pre-Start Verification (check off item by item)

| # | Verification item | Criterion | Source |
|---|---|---|---|
| 1 | Iron concentrate | Grade ≥40% (verified by Section 16.6 panning/visual estimate), grain 5–20 mm, gangue composition recorded; hydrous ore sun-dried (grab a handful and press it to your cheek — no cool, damp feel) | Chapter 16 |
| 2 | High-temperature furnace experience | The full Chapter 17 copper-smelting process completed at least 3 runs; standard-sample method in place for judging furnace temperature | Chapters 12 and 17 |
| 3 | Bellows | Two operators can work continuously ≥1 h (20–40 full strokes per minute without rest) | Chapter 12 |
| 4 | Charcoal | Metallurgical grade ≥100 kg per run: hardwood, dense and jet black, crisp when struck, 20–50 mm grain, fines screened out (passes all Section 6.6 criteria) | Chapter 6 |
| 5 | Ceramic tuyere tubes | Inner diameter 25–40 mm, fired through with no cracks (crisp when struck), 2 spares | Chapter 11 |
| 6 | Dual flux reserve | Quartz sand (acidic) and lime (basic), each ≥2 kg | Chapters 16 and 13 |
| 7 | Forging tooling | Stone anvil half-buried and fixed, hard-stone hammer and copper hammer, wooden fork holder, carrying bars, leather apron and gloves | Chapters 5, 9, and 17 |
| 8 | Record system | Process cards, furnace-number archive, balance in place | Chapters 3 and 8 |

---

### 18.1 Iron Minerals and Usable Ores

| Mineral | Chemical formula | Theoretical iron | Streak | Field identification | Usability |
|---|---|---|---|---|---|
| Magnetite | Fe₃O₄ | 72% | Black | Extremely heavy, metallic luster, dense fracture | Excellent: high grade, reduces fast |
| Hematite | Fe₂O₃ | 70% | **Cherry red** | Streak is red no matter how black the specimen; botryoidal, massive, scaly habits | Excellent: most widespread, easiest to reduce |
| Limonite | Fe₂O₃·nH₂O | 37%–55% | Yellow-brown | Earthy, porous, loose; main body of gossans | Medium: easy to mine and reduce, but its water costs fuel |
| Siderite | FeCO₃ | 48% | Pale brown, fizzes in acid | In layered limestone; brown rust color on weathered faces | Medium: must be calcined before charging |
| Bog iron ore | Limonite variant | 30%–45% | Yellow-brown | Porous rust-colored nodules at lake/marsh margins and below springs | Excellent (a great boon if present): picked by hand, reduces with extreme ease |
| Pyrite | FeS₂ | — | Greenish black | Cubic crystals, golden yellow, hard | **Forbidden in the furnace**: high-sulfur iron is hot-short; register; uses await Chapters 6 and 23 |

**Charge gate**: grade ≥40%; lean ore is first crushed—hand-sorted—panned to concentrate (Section 16.4); **hydrous ore must be sun-dried or dried at the furnace mouth before charging** — water entering the furnace both eats heat and causes bursting and spitting charge.

### 18.2 How Iron Oxides Are Reduced

**Core reactions (indirect reduction dominant)**: carbon monoxide strips the oxygen —

- Fe₂O₃ + 3CO → 2Fe + 3CO₂
- Fe₃O₄ + 4CO → 3Fe + 4CO₂

Where the CO comes from: in the combustion zone C + O₂ → CO₂ releases heat; the CO₂ rises through the red-hot charcoal bed and is reduced to CO (C + CO₂ → 2CO); the CO rises on through the ore bed and strips oxygen. Three zones in the furnace, bottom to top: **combustion zone (bottom, hottest) → reduction zone (middle, CO most concentrated) → preheating zone (top)**.

**Temperature steps (empirical values, must be field-calibrated)**: at 600–700 ℃ reduction begins but is extremely slow; 800–900 ℃ significant; 1000–1200 ℃ fast and thorough. The essential difference from copper smelting: **reducing iron does not require the iron to melt**. Iron melts at 1538 ℃; the furnaces of this stage cannot reach that and need not — the ore is "hollowed out" of its oxygen by CO while solid, leaving a porous iron skeleton: the **bloom**. That is the physical essence of the "direct reduction (bloomery smelting)" route.

**Slag and basicity (the chemistry that decides success or failure)**: gangue (mainly SiO₂ — high melting point, viscous slag) and FeO form an iron-silicate slag. Slag basicity = CaO/SiO₂:

- **Acidic-slag strategy (the traditional mainstream)**: add no large flux charge; let FeO join the slagging to lower the slag's melting point; the viscous slag stays in the bloom's pores, **held until the forging stage to be squeezed out**. Iron loss runs high, but furnace-temperature demands are low and operation simple. For rich ores with gangue <20%.
- **Basic strategy (gangue 20%–40%)**: add lime or wood ash to drop the slag's melting point so it thins and flows out; the bloom comes out cleaner. Add 0.5–1.5 kg lime per 10 kg of ore (empirical starting point). **Excess calcium makes the slag viscous again** — lime is not "the more the better."
- Gangue >40%: go back to beneficiation first (Section 16.4); forcing a smelt without flux on such ore is a fuel black hole.

### 18.3 Charcoal, Furnace Temperature, Airflow, and the In-Furnace Environment

**Charcoal specification**: hardwood charcoal (oak, locust types); grain 20–50 mm (roughly finger-joint to egg size) — too fine chokes the air paths, too coarse burns incompletely; **screen out the fines** and store them separately (briquetting awaits Chapter 23).

**Air volume**: two operators alternating, 20–40 full strokes per minute (empirical, must be field-calibrated). Judge not by numbers but by furnace behavior: an orange-yellow CO flame at the furnace top, continuous and steady, with the burden sinking evenly — air is sufficient; intermittent black smoke and a dull, motionless burden surface — air short or the charge too fine. **If blasting stops more than 5–10 min, the reduction zone cools and this run's iron yield drops visibly** — shift changes must hand over the air without a pause in blowing.

**Layer ratio (ore-to-charcoal ratio, the core parameter)**: one layer of charcoal, one layer of ore; empirical mass-ratio starting point **ore 1 : charcoal 1.5–2**. Calibration path: little iron and black slag → insufficient air/temperature, add air first; plenty of iron but the furnace hangs (burden fuses solid and will not sink) → charcoal excess or ore too fine. **Change only one parameter per run** (the Chapter 8 single-variable Iron Law).

**The fuel account (honest numbers)**: one run (1.5–3 kg of dense iron) burns 80–120 kg of charcoal in total — about 1/3 of that is furnace-body heat storage and losses; steady-state net consumption is about **20–35 kg charcoal per kg of dense iron** (empirical range, must be field-calibrated; higher still if charcoal for drying, furnace curing, and forging is counted). **This account decides how big the Chapter 6 charcoal kilns must be expanded and how the Chapter 38 energy ledger is kept** — expanding production without keeping accounts is where the "eat through the fuel forest in three years" failure mode begins.

**Reducing-atmosphere criteria**: orange-yellow flame at the top, light smoke = normal; weak blue flame, much white smoke = excess air (check for tuyere leaks and too-loose a burden); thick black smoke = charcoal excess or air shortage. **All of these are auxiliary criteria**, used together with the standard-sample method (Chapter 12).

### 18.4 How the Simple Direct-Reduction Furnace Works

**Furnace type: shaft-type bloomery.** Empirical dimensions (starting values, all to be field-calibrated iteratively):

| Parameter | Empirical value | Notes |
|---|---|---|
| Hearth inner diameter | 200–300 mm | A larger bore sends air demand up steeply; do not overreach |
| Total shaft height | 800–1200 mm | Provides the preheating-reduction travel |
| Hearth depth | 150–250 mm | The bloom pancake grows here |
| Tuyere | 1, ceramic tube, 25–40 mm bore | 100–150 mm above the hearth floor, angled down 10°–15° toward the center |
| Tuyere height above furnace bottom | about 1/4 of furnace height | The combustion zone lies around the tuyere plane |
| Wall thickness | 80–120 mm | Inner layer refractory clay (Chapter 12 recipe), outer layer ordinary clay mixed with straw |

**Seven steps of furnace building**: ① siting (open air or a ventilated shed, dry ground, ≥5 m from wood, with room in the radius for 2 blowers + 1 furnace keeper + one forging setup) → ② base (flat stones or a rammed-earth platform, laid with refractory clay brick) → ③ formwork (a wooden cylindrical inner mold, outer planks forming an annular cavity) → ④ wall filling (refractory clay rammed in layers, with the ceramic tuyere tube embedded) → ⑤ drawing the mold and trimming the mouth (leave a furnace mouth of about 100 mm at the top; the tuyere connects outside to the air duct, sealed with wet clay) → ⑥ drying (shade-dry ≥3 days, then one day of low-fire drying; a fast first burn will crack it) → ⑦ preheating and curing the furnace (before the first run, burn half a shaft of charcoal empty, raising temperature slowly over 2–3 h; check for cracks and patch with clay slip).

**Full sequence of one run**:

1. **Ignition and base charcoal**: fill the hearth with charcoal to 200 mm above the tuyere, add the fire starter, gentle blast.
2. **Heat-up**: once the charcoal is fully lit and the tuyere plane glows bright red (15–30 min), shift to strong blast.
3. **Layered charging**: alternate charcoal layers 80–100 mm with ore layers 40–60 mm up to the mouth; top up as the burden sinks, **keeping the charge line steady**.
4. **Running and tending**: every 10–15 min probe the burden with a long refractory-tipped rod for looseness and crusting; watch for slag seeping from the slag notch / below the tuyere lip (viscous slag hanging on the wall is normal — the bloomery runs mainly on "holding the slag in"); keep adding charcoal. **Take one slag sample every 30 min** (dip an iron rod into the hearth and lift) into the slag-sample register.
5. **Judging the endpoint**: after the final charge, run 30–60 min more; the top flame weakens and the burden surface stops sinking.
6. **Stop blast and draw the iron**: open the furnace mouth (with the reserved clay-charcoal plug section), and while hot draw out the **bloom pancake** with wooden tongs / carrying bars (800–1000 ℃, yellow-red to orange-red). Slag hangs all around it — do not grip it bare-handed for long.
7. **Clean out and reset**: dig out leftover charcoal and slag, inspect the lining for erosion, patch with clay. Lining life is about 3–8 runs (empirical); keep a furnace-body archive.

[Card 18-01 One Bloomery Furnace Run] (eight fields)

1. **Input materials**: concentrate 20–40 kg (**grade ≥40%, 5–20 mm, dry**); metallurgical charcoal 80–120 kg (including heat losses); limestone 0–4 kg depending on the basicity strategy. Wet or badly graded ore wastes everything downstream.
2. **Tools required**: the bloomery, bellows (**two-person rotation**), furnace hook and rake, slag rod, carrying pole, tongs, full leather protection (apron, gloves, face shield). Calibration source: temperature read from fire color and furnace behavior, not from a pyrometer.
3. **Sequence and control points**: (1) **ignite and charge the bottom charcoal** — fill to 200 mm above the tuyere, insert fire, gentle blast; (2) **heat up** — once the charcoal is fully alight and the tuyere plane is bright red (15–30 min), switch to strong blast; (3) **charge in layers** — charcoal layers 80–100 mm, ore layers 40–60 mm alternating to the top, making up layers as the burden sinks; **keep the burden line steady**; (4) **run and maintain** — every 10–15 min rake the burden loose with the long rod where it has crusted; watch slag seep from the slag notch or below the tuyere; (5) **judge the end point** — after the last charge run another 30–60 min; the top flame weakens and the burden stops sinking; (6) **stop the blast and tap** — open the tap hole, take out the **bloom at 800–1000 °C (yellow-red to orange-red)** with tongs and pole; (7) **clean and reset** — clear charcoal and slag, inspect lining erosion and patch. Control points: **steady burden line** and **end-point criteria** (weakening flame plus no further sinking) — tap early and the iron is raw, tap late and it sticks.
4. **Empirical parameters and calibration**: ore:charcoal 1:1.5–2; charcoal per run 80–120 kg; steady-state consumption **20–35 kg charcoal per kg of dense iron** (empirical band, calibrate to local ore and charcoal); yield **1.5–3 kg per run** (L2 criterion); run 6–9 h with 3–4 people in rotation; tuyere bore 25–40 mm, angled down 10°–15°; lining life 3–8 runs.
5. **Observations to record**: per run — ore grade and sizing / total ore and charcoal / layer ratio / time from ignition to full blast / number of layer top-ups / slag flow / end-point time / yield / lining erosion.
6. **Pass / rework / scrap criteria**: pass = 1.5–3 kg of dense, forgeable bloom with free slag flow; rework = low yield (unsteady burden line or low grade), review the record and adjust charging; scrap = lining burned through and charge lost (shut down and rebuild; log the run in the furnace file).
7. **Common failures and diagnosis order**: (1) will not light or heats slowly → damp charcoal, too little bottom charcoal, insufficient blast; (2) burden crusts and blocks → raking interval over 15 min; (3) little iron, much slag → low grade or too little charcoal in the ratio; (4) bloom black and slag-laden → limestone short or tapped late; (5) lining cracks in one run → insufficient drying at build (Card 18-03).
8. **L1 / L2 / L3 evidence**: L1 = one complete run producing iron; L2 = three consecutive runs with comparable yield and charcoal consumption, steady within 1.5–3 kg; L3 = a second person runs one from this card alone and meets the standard.

[Card 18-03 Building the Furnace in Seven Steps] (eight fields)

1. **Input materials**: refractory clay (Chapter 12 mix: 50–70% grog plus 30–50% refractory clay); ordinary clay with straw (outer layer); tuyere clay pipe; wooden cylindrical inner form and outer ring boards; flat stone or rammed earth.
2. **Tools required**: wooden form, rammer, trowel, blast pipe, slip bucket. Calibration source: furnace dimensions per the table (hearth depth 150–250 mm, wall 80–120 mm, tuyere about a quarter of furnace height above the base).
3. **Sequence and control points (seven steps, none skippable)**: (1) **siting** — open air or a ventilated shed, dry ground, **at least 5 m from timber**, with room within reach for 2 on the bellows, 1 stoker, and a forge; (2) **base** — flat stone bedding or a rammed-earth platform, laid with refractory bricks; (3) **set the form** — wooden cylindrical inner form with outer boards forming an annular cavity; (4) **fill the wall** — ram refractory clay in layers, **embedding the tuyere pipe**; (5) **withdraw the form and dress the mouth** — leave about a 100 mm mouth, connect the blast pipe and seal with wet clay; (6) **dry** — **shade-dry at least 3 days, then gentle heat for 1 day; firing wet cracks it**; (7) **preheat** — before the first run, burn half a charge of charcoal empty and raise heat over 2–3 h, inspect for cracks and patch with slip. Control points: **the drying time in step 6** (skip it and the furnace cracks in one run) and tuyere position and angle.
4. **Empirical parameters and calibration**: hearth depth 150–250 mm; one tuyere, 25–40 mm bore clay pipe, 100–150 mm above the hearth floor, angled down 10°–15° toward the center; tuyere about a quarter of furnace height above the base; wall 80–120 mm (refractory inner, straw-clay outer); lining life 3–8 runs.
5. **Observations to record**: per furnace — build date / completion of each step / shade-drying days / drying heat hours / crack locations at first preheat and patching / subsequent runs and lining life (a furnace file).
6. **Pass / rework / scrap criteria**: pass = no through-crack at first preheat and a normal first run; rework = surface hairline cracks, patch with slip and dry again; scrap = through-crack at hearth or tuyere (take it down and rebuild; it cannot be patched).
7. **Common failures and diagnosis order**: (1) cracks at first preheat → shade-dried under 3 days, heated too fast; (2) clay falls away near the tuyere → under-rammed, or the pipe was not bedded firmly; (3) hearth distorts → form withdrawn too late or clay too wet; (4) collapses in one run → base not solid, or the outer layer had no straw.
8. **L1 / L2 / L3 evidence**: L1 = one furnace built, preheated, and run; L2 = three furnaces with comparable life records (≥3 runs); L3 = a second person builds one from this card alone and passes the preheat acceptance.

### 18.5 Slag, the Iron Mass, and Residual Impurities

#### 18.5.1 Slag-Sample Reading Table (mandatory every run, mandatory archive)

| Slag appearance | Meaning | Countermeasure |
|---|---|---|
| Deep black glassy, dense and glossy | Slag high in FeO — reduction insufficient or iron loss high | Raise air / lengthen the run; verify the layer ratio |
| Gray-green to pale blue, lighter and porous | Low iron loss, basicity right | Hold the parameters; record as baseline |
| Extremely viscous, thread hangs on the rod without dropping | Basicity too acidic (SiO₂ high), temperature short | Add lime (trial from 0.5 kg per 10 kg of ore); raise air |
| Thin as water, heavy loss | Basicity too high or temperature too high | Cut the lime; blooms from such runs tend to come out fine and friable |

#### 18.5.2 Slag-Rod Temperature Reading (thread length)

Temperature cannot be seen directly; slag fluidity is its spokesperson. **Dip the slag rod, lift, and read the thread** (◎ technique, requires practice):

| Thread behavior | Slag temperature order | Furnace reading |
|---|---|---|
| No thread; drops as droplets; slag on the rod tip darkens | <1100 ℃ class, slag stiff | Temperature short: raise air; check charcoal dryness |
| Short thread (breaks below 30 mm) | about 1100–1200 ℃ | Near usable; keep watching |
| Long thread (50–100 mm continuous fine filament, bright yellow) | about 1200–1300 ℃ | **Reduction zone working well** (target band) |
| Extremely long thread (>150 mm) with slag running thin as water | >1300 ℃ | Overheat risk: the pancake may locally fuse into white iron (cast-iron conversion); cut air and watch |

Calibration method: cross-check within the same furnace against the standard samples (Chapter 12) — drop a temperature-test coupon whenever a slag sample is taken, pair "thread length ↔ coupon state" run by run in the slag register, and build a local-site cross-reference table. **Thread length is an empirical criterion; its legitimacy comes from the paired coupon records, not from this table itself.**

**What the bloom is made of**: iron skeleton + slag held in the pores + unreduced gray-black ore cores + a thin carburized skin near the charcoal (carbon up to 0.1%–0.5%, empirical). **The bloom is not a product** — loose as a slag cake, it shatters at a blow if used as is; it must be forged dense.

**Impurity awareness**: sulfur makes iron **hot-short** (cracks on the first forging blow; troubleshooting in Section 18.9); phosphorus makes it **cold-short**. Nothing at this stage can test for either — only ore sorting as the gate, plus reading back from forging behavior; "brittleness-source" ore sites get flagged on the resource map (the Chapter 16 backfill system).

[Card 18-04 Slag-Rod Temperature Reading] (eight fields)

1. **Input materials**: molten slag in a running bloomery; a slag rod (long iron or copper rod). **The slag is the furnace's thermometer** — you cannot see the iron, but you can see the slag.
2. **Tools required**: slag rod with a polished tip, heat-resistant gloves, a viewing position at the side, never in line with the slag notch. Calibration source: the criteria are **drawing length and fluidity**, not color alone.
3. **Sequence and control points**: draw slag from the notch or from below the tuyere → fling and draw it out on the rod → read the thread. Control points: **sample from a fixed position** (slag at the notch and slag under the tuyere are not equivalent — record which); draw the thread immediately after taking it (it will not draw once cool).
4. **Empirical parameters and calibration**: **a continuous fine thread 50–100 mm long is the normal band** (empirical, calibrated against test pieces). Too short = temperature low or basicity low; long and syrupy = temperature too high or basicity high (thin slag carries iron away). Viscous slag clinging to the walls is normal (a bloomery runs "smothered"), but **no slag at the notch while slag hangs heavily under the tuyere = wrong hearth slope or notch position**.
5. **Observations to record**: every 10–15 min — sampling position / thread length / slag color (black, green-black, gray) / fluidity / slag volume.
6. **Pass / rework / scrap criteria**: pass = 50–100 mm thread and slag running clear; rework = short thread, add charcoal for heat or limestone for basicity; scrap = slag set like stone and blocked the notch (stop the blast, clear it, the run is written off).
7. **Common failures and diagnosis order**: (1) slag will not draw a thread → temperature short (check blast and charcoal first), then basicity; (2) slag too thin and carrying iron → excess limestone, reduce basicity; (3) notch blocked → notch below the highest point of the hearth floor or slope insufficient (see 18.11); (4) slag green-black and sticky on the rod → reduction incomplete, burden layers too thick or too little charcoal.
8. **L1 / L2 / L3 evidence**: L1 = one run's slag readings including thread lengths; L2 = three runs comparable, with the relation between thread and yield explained; L3 = a second person reads the same run from this card alone and agrees on the band.

### 18.6 Repeated Forging and Densification of the Iron Mass

**Goal**: hammer the porous, slag-laden bloom into dense, uniform wrought iron stock. Principle: hot iron is soft and slag is brittle — hammer blows weld the iron skeleton together while the slag is crushed and worked out of the seams along the deformation direction. **Each heating–forging cycle counts as one "heat."**

**The reality of forging tools (starting with no iron tools)**:

| Tool | Stage solution |
|---|---|
| Anvil | A large, flat, hard rock (basalt, granodiorite), half-buried in the ground and fixed, face ground flat |
| Hammer | Hard-stone hammer (800–1500 g) worked with the copper hammer; **the first iron stock goes first to bootstrapping an iron hammer** (Section 18.7) |
| Holding | A hardwood stick with a fork (an iron-sheet sheath on the fork mouth makes it last long) + carrying bar; short, small pieces get a "forge handle" forged on for gripping |

**The hot-forging slag-extrusion technique (this chapter's core technique, ◎ must be practiced)**:

1. **Catch the heat**: the drawn pancake or the stock is buried in red-hot charcoal and raised to **bright orange–bright yellow** (about 1000–1200 ℃; yellow-bright forges, glaring white near melting is danger). The **useful forging window of one heat is about 1–3 min** — from pickup to dark red (below about 700 ℃ plasticity falls off). **Rather another heat than a cold hammering** (cold hammering cracks it).
2. **The four-character formula: fast, light, even, turn** —
   - **Fast**: 60–100 light blows per minute, never letting the stock sit and cool;
   - **Light**: light blows, no heavy swings (a heavy blow crushes slag into the iron; a light blow lets the iron weld and the slag surface);
   - **Even**: work the hammer over the whole face, center first then edges (densify the center first; close the edges after);
   - **Turn**: every 2–3 rounds rotate 90°, alternating face blows and edge blows.
3. **Watch the slag sweat**: slag seeping from the edge seams like black sweat, and sparks flying with slag in them, are normal; scrape the slag skin off with a wood slat as you go. **No sweat = temperature short or slag exhausted** (a smooth face and a crisper hammer note are the sign of slag exhausted — auxiliary criteria).
4. **Fold forging**: flatten the piece, fold it double, and forge it shut — folding cuts the internal slag layers, spreads them thin, and works them out, over and over. **One fold per heat, 3–6 folds in total** (empirical, must be field-calibrated); turn the fold direction 90° each time, crossing over. **This is the step that turns "iron wrapping slag" into "iron carrying fine slag streaks"; skip the folding and the product delaminates and cracks.**
5. **Judging density**: the hammer note turns from dull to crisp (auxiliary); fracture spot-check shows fine, tight fiber and no continuous black slag line; **the water-quench test: a dense piece enters water with no stream of bubbles** (bubbles rising out of pores = not dense, directly countable).
6. **Burning-through warning**: sparks bursting like fireworks, edges whitening and fuzzing = local burning; cut that section off and scrap it — better short than bad.

[Card 18-02 Folding, Forging, and Slag Squeezing] (eight fields)

1. **Input materials**: the bloom (from 18-01, taken at 800–1000 °C and worked hot); flux (river sand or a borax substitute); charcoal. The goal is to turn porous, slag-laden bloom into dense, uniform wrought iron.
2. **Tools required**: **a large flat hard rock as anvil** (basalt, granodiorite — half-buried and fixed, face ground flat); hard stone hammer 800–1500 g used together with a copper hammer (**the first iron is used to make an iron hammer**); forked hardwood stick for holding (iron-shod fork lasts) plus a carrying pole. Calibration source: temperature by fire color (bright orange to bright yellow, 1000–1200 °C).
3. **Sequence and control points**: onto the anvil hot → **light rapid blows to squeeze slag** (slag is brittle, iron is soft; hammering welds the iron skeleton while slag breaks and runs out of the seams) → turn and work the other face → fold → reheat → repeat. Control points: **1–3 min per heat** (cool it and it cracks under the hammer); **fold 3–6 times, once per heat, alternating direction** (folding one way only laminates the slag).
4. **Empirical parameters and calibration**: forging window **bright orange to bright yellow (1000–1200 °C)**, 1–3 min per heat; folding **3–6 times**, once per heat, direction alternating; slag thread target 50–100 mm continuous (calibrated with test pieces, see Card 18-04).
5. **Observations to record**: per piece — number of heats / duration of each / fold count and direction / slag squeezed out and its color / density of the finished section (any laminated slag).
6. **Pass / rework / scrap criteria**: pass = dense section with no laminations, no delamination after folding, workable into a tool; rework = slag still present, add folds (but not beyond 6 — over-folding decarburizes); scrap = extensive internal slag or folding cracks (downgrade to small items or remelt).
7. **Common failures and diagnosis order**: (1) cracks at the first blow → below the window, back to the fire; (2) delamination → folding in one direction, switch to alternating; (3) gets harder and the hammer will not bite → decarburization from too many heats or too fierce a fire; reduce folds; (4) slag will not come out → blows too heavy or heat too short; use light rapid blows and lengthen the heat.
8. **L1 / L2 / L3 evidence**: L1 = one densified wrought iron billet plus record; L2 = three billets with fold counts and section quality comparable; L3 = a second person forges one billet to the section standard from this card alone.

### 18.7 From Bloom to Usable Iron Tools

**Managing the intermediate form**: dense iron stock is uniformly forged into **standard bar stock** (cross-section 20×20 mm, length measured against the standard rod and registered) and enters the graded iron stock library — every later tool is made from this bar stock (the starting point of "copy one dimension" in metal — Iron Law Two).

**The bootstrap order of the first iron tools (fixed, do not shuffle)**:

| # | Item | Reason | Specification |
|---|---|---|---|
| 1 | Iron hammer | Immediately lifts all forging and breaking efficiency | Head 800–1500 g, forged solid throughout, hafting per Section 9.1 |
| 2 | Iron anvil | Stabilizes the forging reference face | A block ≥10 kg, face ground flat (grinding table + quartz sand, slow work) |
| 3 | Fire tongs | Makes holding safe | Two forged bars + riveted/wrapped joint |
| 4 | Iron chisel | Upgrades mining and wood/stone work | Cross-section 16×16 mm, edge angle 40°–50° |
| 5 | Iron adze / iron axe | Heavy chopping and cutting handed over to iron | Edge width 70–100 mm |

**Forging-to-shape essentials**: wrought iron forges superbly — in the bright orange band it draws out, spreads, and bends freely, **and unlike copper it does not need frequent annealing**. Order: draw out → spread → bend and close up → dress; local thickness transitions ≤2:1 (this rule doubles as the Chapter 19 design rule against quench cracking). **Softening annealing (for dressing)**: bury the piece in hot ash at the furnace edge and let it cool slowly overnight (slow cooling from about 600–700 ℃, empirical).

**The boundary with copper tools**: an iron chisel cuts hard rock, an iron axe chops hard wood — the items "forbidden" to the Chapter 17 copper tools are handed over to iron one by one; stone tools drop to backup (keep the Section 9.6 toolbox).

### 18.8 Why Getting Iron Is Not the Same as Getting Steel

**Only one variable separates iron from steel: carbon.** Wrought iron (<0.1% C) is soft and tough and **does not harden in the quench**. The inhomogeneity of bloomery product demonstrates exactly this: within one bloom pancake, the side near the charcoal may be locally carburized to 0.3%–0.6% (harder, bright-white fracture) while the center is still wrought iron (soft, gray fibrous fracture) — **one furnace of iron mixes "wrought iron + scattered low-carbon steel," unpredictable by position**. Quenching it directly as steel is guaranteed scrap. The two Chapter 19 methods: fracture-based stock selection + artificial carburizing.

**The essential difference between the bloomery and the modern blast furnace (must be understood as it is)**:

| Item | Bloomery (this chapter) | Blast furnace (modern, long-term) |
|---|---|---|
| Product | Solid-state bloom → forged into wrought iron | Liquid pig iron (C >2%), then refined into steel |
| Furnace temperature | About 1200–1400 ℃ peak at the tuyere zone; iron does not melt | Hearth >1500 ℃; slag and iron fully molten |
| Continuity | Batch: one run, one pancake, furnace opened to draw iron | Continuous charging, continuous tapping of iron and slag |
| Scale | kg-level per run | Hundreds of tons per day |
| Dependencies | Chapter 12 bellows + refractory clay + charcoal | Strong blast, coke, large refractory structures, slag-iron separation systems |

**Why this stage does not chase liquid pig iron**: molten iron requires the hearth to hold >1400 ℃ for a long time — the charcoal-and-bellows system can only manage that occasionally; and liquid pig iron is high in carbon and badly brittle, with limited refining means at this stage (stir-refining (puddling) is a conditional route, Section 19.8.2). **The correct order: first obtain forgeable iron stock reliably through direct reduction (this chapter's L2), then chase capacity and the liquid route (long-term, pending greater air volume and coke).** Stated honestly: this chapter's route caps iron output at a few kg per run — enough to support tool bootstrapping and workshop production, not enough to support a machine industry at scale.

### 18.9 How to Check Basic Quality of Iron Tools

**Three tests in parallel; not one may be skipped**:

**One, fracture inspection (spot-check 1 bar per batch)**: clamp the bar (rope-loop clamp), strike it or bend it back and forth until it breaks —

| Fracture appearance | Verdict | Disposition |
|---|---|---|
| Gray fibrous, torn-fiber texture | Quality wrought iron | Into stock as Grade A |
| Bright white coarse grains | High carbon, or overheated coarse grain | Label separately as "suspected steel stock," sample for Chapter 19 |
| Continuous black slag lines, layered peeling | Slag inclusions not removed | Reforge (add 1–2 folds) |
| Smooth bright conchoidal face | Burned through **or converted to white cast iron** | Cut off the burned part; register white iron as Grade D (recover per Section 19.8.2) |
| Sulfur smell / yellow slag spots | Suspected high sulfur | Flag the whole batch as a brittleness source; trace the ore origin |

**Two, the repeated bending test**: take a section of about 10×200 mm; a bend of 90° and back 180° counts as one cycle. **Soft, tough wrought iron holds ≥8–10 cycles without breaking**; breaking within 3 cycles is judged brittle (slag inclusion / high sulfur / burned through). Keep a bend sample from each batch in the archive.

**Three, the functional test**: the iron chisel cuts granite for 10 min — the edge neither chips nor curls; the iron axe chops hard wood 50 times — no cracks, no dents; the iron hammer strikes iron stock 100 times — no sinking or spalling of the face. **The functional test is the final acceptance**; a piece that passes the first two but fails function is returned just the same.

**Auxiliary means (limits stated)**: strike-listening (crisp long ring ↔ dull thud) helps judge density and cracks but is strongly affected by the piece's shape and clamping and **may not stand alone as the basis of acceptance**; the same holds throughout for judging temperature by fire color.

**Quick product identification (which iron came out)**:

| Means | Wrought iron | Steel stock | White cast iron |
|---|---|---|---|
| Fracture | Gray fibrous, torn | Bright white fine grains | Conchoidal, bright white, coarse |
| Hammer blow | Bends without breaking | Breaks after bending | Shatters at one blow |
| File feel (files in Chapter 19) | Bites in and cuts chips | Barely bites | Slips without biting (extremely hard, extremely brittle) |

**Archives**: every batch of iron stock gets a furnace number + batch number, with ore source, layer ratio, flux, air conditions, slag samples, iron yield, and the three inspections recorded. **Iron stock without an archive may not enter the quenching process** (item 1 of the Chapter 19 pre-start verification).

---

### 18.10 Furnace Iteration: Double Tuyeres, Tuyere Preheating, and the Furnace-Height Account

The single-tuyere, flat-bottom furnace is a starting point, not an endpoint. This section gives three directions of iteration — tuyere count, air temperature, shaft height. Iron Law: **change one thing at a time** (the Chapter 8 single-variable Iron Law); after each changed run, put three numbers — charcoal consumption, iron yield, run duration — into the ledger against the pre-change baseline furnace; a change that fails to move the three numbers may not be called an improvement.

#### 18.10.1 The Double-Tuyere Furnace (Opposed Tuyeres)

**Rule source**: the Chapter 12 multi-tuyere rule — with two or more tuyeres, each tuyere's axis must converge at the center of the hearth, and the convergence point is the combustion core; the two air streams collide and stir at the heart of the bed, and the combustion zone spreads from "a point" into "a sheet."

**Layout (empirical starting point, calibrated run by run)**:

| Item | Value | Notes |
|---|---|---|
| Tuyere count × bore | 2 × 20–30 mm ceramic tubes | The two tubes' combined cross-section matches the original single 25–40 mm tuyere, or runs 10%–20% larger |
| Arrangement | Horizontally opposed (180° apart), on one level | Height above the furnace floor unchanged (about 1/4 of furnace height) |
| Downward angle | 10°–15° each, same as the single tuyere | Convergence point pressed into the bed-center burden |
| Installation tolerance | Height difference between tuyeres ≤10 mm; axis convergence deviation ≤15 mm | Verified on the cold furnace; see below |

**Cold-furnace verification (mandatory before sealing with clay)**: pass a straight rod (length ≥2× the hearth diameter) through both tuyeres — the rod tips should meet at the furnace center; check the two tube mouths for equal height against the stilled surface of a water bowl (the connected-vessel leveling method, Chapter 3). After ignition, **equal brightness at the two tuyeres** is the sign of a sound run; one bright and one dark means uneven air paths — check the duct joints for leaks and the tubes for charcoal blockage first, then the installation tolerances.

**Benefit**: the hearth heats evenly and the bloom pancake grows round and centered (in single-tuyere furnaces the pancake habitually skews toward the side opposite the tuyere, with local overheating on the air side); the dead column of charge at the center shrinks; at the same layer ratio the slag thread settles into the target band more easily.

**The cost account (computed before the change)**: budget air demand at roughly 1.5–2× the original (empirical; calibration: watch the double-tuyere brightness and slag thread during the first trial run, converging by ±10% per run) — the two-operator rotation floor rises from 20 full strokes per minute to 35–40; shift-change intervals shrink from 30 min to 15–20 min; add the labor bill to the shift schedule first. **If the bellows cannot feed a double tuyere, stay with a single tuyere — a half-alive double-tuyere furnace is worse than a single one** (the air short-circuits; see the failure-mode table).

[Card 18-05 Converting to Twin Tuyeres] (eight fields)

1. **Input materials**: an existing furnace (built per 18-03); two tuyere clay pipes (20–30 mm bore); blast pipe and tee; refractory clay. Purpose: a single tuyere starves the center and over-blows the edges; twin tuyeres stretch the combustion zone into a line.
2. **Tools required**: scored rule, straight rod for cold-furnace checking, angle gauge, slip. Calibration source: **height difference and intersection offset between the two tuyeres are measured with a straight rod in the cold furnace**, never by eye.
3. **Sequence and control points**: mark the two tuyere positions (opposed or at 90° depending on furnace type) → bed the pipes → **cold check with the straight rod: height difference ≤10 mm, intersection offset ≤15 mm** → connect the tee → seal with clay → dry. Control point: **height difference and intersection offset** — misaligned tuyeres over-blow one side and starve the other, worse than a single tuyere.
4. **Empirical parameters and calibration**: each tuyere bore 20–30 mm; height difference **≤10 mm**, intersection offset **≤15 mm** (empirical tolerances, verified with the rod in the cold furnace); hot-blast passage length 250–350 mm (judged by the charcoal-consumption ledger, calibrated against a reference furnace).
5. **Observations to record**: before and after the change — charcoal per kg of iron / yield / density difference between bloom at center and at the edge / slag condition.
6. **Pass / rework / scrap criteria**: pass = charcoal consumption falls or yield rises, and the center-edge density gap narrows; rework = tolerances exceeded (pull the pipes and rebed); scrap = the wall cracks from the two openings (reinforce or revert to a single tuyere).
7. **Common failures and diagnosis order**: (1) worse after the change → height difference or offset out of tolerance, recheck cold; (2) one tuyere backfires smoke → insufficient blast pressure or uneven tee split; (3) clay falls away around a tuyere → not rammed when bedded; (4) consumption unaffected → the furnace was not the bottleneck (do the heat balance first, 12.7).
8. **L1 / L2 / L3 evidence**: L1 = one furnace converted with check data recorded; L2 = three runs before and after with an explicable difference; L3 = a second person converts one from this card alone and passes the cold check.

### 18.11 Slag-Iron Separation Tooling: The Sloped Hearth, the Slag Notch, and Notch-Plug Clay

The flat-bottom furnace runs mainly on "holding the slag in" (the acidic-slag strategy, Section 18.2), and leaving all the slag to be squeezed out at forging costs iron and labor. This section's direction: **let more slag leave inside the furnace and less enter the pancake**. Note that this is an iteration item, not a threshold item — the flat-bottom, slag-holding furnace still produces qualified iron.

- **Hearth slope**: the hearth floor slopes down 5°–8° toward the slag-notch side (empirical; when padding and truing the surface with refractory clay, measure with a wooden slope template; templates are marked and entered into the tooling library under the Chapter 9 template system).
- **Slag notch**: open it on the same side as the tuyere, 30–50 mm above the highest point of the hearth floor — slag floats on top of the pancake, so a high notch position does not lose iron. At this stage iron does not melt (Section 18.8), **so no iron notch is cut**: the pancake rests in the hearth semi-solid and is raked out at shutdown.
- **Notch-plug clay**: refractory clay mixed with charcoal powder, 2:1 by volume (empirical starting point), wet-kneaded into a ball and pressed into the slag notch, dusted outside with dry charcoal powder against sticking. During the run the notch stays closed and slag is released in concentrated batches — a small notch left permanently open will only freeze itself shut.
- **Reading the tapping moment (linked to the Section 18.5.2 slag-rod method)**: dip the slag rod and read the thread — 50–100 mm = the slag can flow; open the notch and it runs down the slope in a rope; <30 mm and the slag is stiff — forced tapping only plugs the notch; raise air and temperature first, then try; >150 mm and the slag runs thin as water — **keep the notch closed and tap little**: thin slag carries iron away with it. Compare slag color at tapping against Section 18.5.1 and log the iron loss (glossy black slag = heavy iron loss; re-verify that run's parameters).
- **Tapping-quantity criterion**: slag released through the run should make up about 1/3–1/2 of the furnace's total slag (empirical; calibration: weigh the tapped slag against the slag raked out at teardown) — that achieves the goal of "holding less slag in"; spot-check fractures from the same batch for comparison: pancake slag-line density from the sloped-hearth furnace should be visibly sparser than from the flat-bottom furnace.
- **Safety**: opening the notch sprays flame carrying slag grains — stand to the side; full leather protection (the Chapter 6 procedures apply in full).

### 18.12 Forge-Welding: Detailed Rules and Fluxes

Forge welding is the common underlying process of fold forging (step 4 of Section 18.6) and of every joined part (Section 18.13 chain links, iron bands, iron sheathing), and it deserves rules of its own. **The first enemy of forge welding is the false weld — it looks welded, is not welded, and breaks only in use**; that is a silent failure, so inspection is established first and technique written second. **Joint inspection (universal for all forge-welded work)**: after cooling, bend 90° with the weld on the tension side — no delamination and no cracking passes; additionally break one piece per batch: the fracture should lie in the parent metal — a break at the weld is a false weld, and that batch is then inspected piece by piece in full.

**The forge-welding temperature window**: bright yellow to near-white (about 1250–1350 ℃, empirical, must be field-calibrated). The window's sign is the iron face **sweating** — the surface just begins to melt into a bright film; strike the two faces together at that moment and they weld. **Spark warning**: sparks spraying off the iron face like a sieve = burned through (the iron is boiling and spitting); stop welding at once, cut off the burned end and scrap it — better short than bad (as in step 6 of Section 18.6). ◎ Reading the fire by sweating is hand-feel work. Practice: make stepped trial welds on the ends of scrap bar, ≥10 of them — weld each at a different fire color, cool, break, and examine the welded area. Misjudgment compensation: make a "fire color ↔ weld fraction" comparison card and hang it by the forging hearth; read the card before welding, break and verify after welding, and revise it run by run into the ledger.

**Three steps of weld-face cleaning (mandatory before welding; miss one and you have a false-weld candidate)**:

1. **Dress the faces**: forge both weld faces flat; mate them dry against the light with no gap;
2. **Strip the scale**: after heating, tap lightly or use a scraping bar to remove the oxide scale, exposing fresh iron color;
3. **Dust the flux and return to the fire**: sprinkle flux on the weld faces and put the piece back; the flux melts into a glassy film that covers the face and shuts out air; weld the moment it is drawn — **no pausing midway to flip and inspect**: every flip breaks the film once, and you start over.

**Fluxes**:

- **Quartz sand (standing stock)**: clean, dry sand. Action: with FeO it forms a low-melting iron-silicate slag film that both shuts out air and "pushes" the weld-line impurities out. Dose: until the weld face carries a white frost. **Wet sand and clay-bearing sand are forbidden** (explosive spatter + slag inclusions).
- **Borax (if registered; long-term item)**: lower melting point, better fluidity — an upgraded replacement for quartz sand; register acquisition channels for the Chapter 16 resource-map backfill; until it is in hand it stays out of the process.

[Card 18-06 Chain-Link Forge Welding] (eight fields)

1. **Input materials**: wrought iron bar (from 18-02, section sized to the ring); flux (river sand or borax); charcoal. Chain welding is the first practical "iron made with iron" joint, and the best practice piece for fire-color control.
2. **Tools required**: anvil, hammer, tongs, **a tapered mandrel that fits inside the ring** (sets the internal diameter), flux pot. Calibration source: **fire color** — bright yellow to near white (about 1250–1350 °C), "a sweat means weld."
3. **Sequence and control points**: heat the bar to bright yellow → bend into a U → pass it through the previous ring → heat both ends to near white → **apply flux** → bring together and hammer (**weld at the sweat**: the instant fine droplets appear on the surface, strike) → true the ring on the mandrel → cool and check. Control points: **flux goes on only at near-white** (earlier and it burns off, later and the oxide layer is too thick to weld); **the first blow after closing must be fast**.
4. **Empirical parameters and calibration**: welding window **bright yellow to near white (about 1250–1350 °C)**, weld at the sweat; flux applied at near-white; ring diameter set by mandrel; calibrate with three trial welds to fix this shop's color and hammer rhythm.
5. **Observations to record**: per link — heats / fire color / flux quantity / whether it sweated / hammer rhythm / ring note after cooling (clear = welded through, dull = a false weld).
6. **Pass / rework / scrap criteria**: pass = no visible seam, clear ring, holds in a pull test; rework = false weld (dull note), reheat and re-weld (at most twice — repeated heating decarburizes); scrap = joint cracked or ring deformed out of round (use as a hook or other non-load part).
7. **Common failures and diagnosis order**: (1) will not weld → color short of near-white, or flux applied too early and burned off; (2) oxide inclusions in the joint → heated too long and the scale was not cleaned; (3) opens under load → contact area too small, or the first blow came too late and the temperature dropped; (4) ring out of round → mandrel not used.
8. **L1 / L2 / L3 evidence**: L1 = a three-link chain passing a pull test; L2 = ten chains with a false-weld rate below twenty percent; L3 = a second person welds an acceptable chain from this card alone, both judging "the sweat" at the same instant.

### 18.13 Expanding the Wrought Iron Application List

Once the hammer, anvil, chisel, and axe are bootstrapped (Section 18.7), the second wave of applications is sequenced "joined parts first, structural parts after." Every item below passes the Section 18.9 three tests, plus this section's item-specific inspection.

**Chains (welded link by link)**: hoisting, wellhead protection, and waterwheel drive (Chapter 21) all need it. Process per Card 18-06: cut stock → flatten the ends → hot-bend the ring closed with a lap → add flux at the welding heat → strike over the lap to weld through → dress round. Two iron rules: **the lap weld always sits on the inside of the ring** (the least-bent position); **hoisting chains are inspected link by link, non-hoisting chains by spot-check**. **Tensile spot-check**: take 1 link in every 10, plus each chain's first and last link — thread a bar through the link, two people lift and hold a suspended load of ≈20 kg for 1 min: no deformation, no cracking (empirical starting point; quantitative calibration to be added once the Chapter 8 lever-weighing method is in place). A chain that fails is downgraded whole to non-hoisting use and tagged.

**Rivets (the hot-riveting process)**: for fire-tong handle joints, iron-band joints, and hull-plank positioning. Hole diameter ≤1 mm larger than the rivet's cold diameter; heat the shank to bright orange, drive it in, and upset the second head on a cupping anvil (a washer plate). ◎ Hot-rivet hand feel: practice — trial-rivet ≥5 pieces on scrap plate before touching real work; misjudgment compensation: wobble it and listen (a solid note, no looseness) + inspect both heads complete and uncracked. **The principle of why hot riveting beats cold riveting is one line: the hot shank is fat and shrinks as it cools — the hole is swelled full and the plates are drawn tight**; cold riveting has only the first half of that. Rivet cracking is mostly from upsetting at too low a temperature or from brittle rivet stock (see the failure-mode table). Rivet pitch 3–6× the plate thickness, edge distance ≥2× the plate thickness (empirical starting point).

**Iron bands shrunk hot (hot shrink-fitting onto shafts)**: for wheel rims and locking shaft ends — the formal specification for wheels and shaft systems is given in Chapter 21; this chapter delivers only the "hot-shrink" technique. Steps: make the band's inner diameter 1‰–2‰ smaller than the shaft diameter (empirical shrink allowance — about 0.05–0.10 mm small on a 50 mm shaft; **make one sample ring first and calibrate by a cold trial fit before cutting formal stock**) → heat the whole band to bright orange → slip it over the shaft end in one motion while red → it grips tight as it cools and shrinks. **If it jams midway, never hammer it on hard** — drive it back off, reheat, and fit again; hard hammering ruins the journal. Criteria: when cool, the band rings solid under a hammer tap; no movement at the seam under a chisel-pry.

**Ship nails**: square-section faceted nails, hot-forged to a point. Awl the wooden hole first (driving straight in is forbidden — a split plank means a wasted hole); once the nail is in ≥2/3 (empirical criterion), clinch the exposed point to lock it. Criteria: the clinched point uncracked, the head tight to the surface.

**Iron sheathing for tool handles**: iron-sheet wrapping on the loaded ends — hammer handle butt, shovel handle mouth — fixed with two or more rivets. Purpose: stop the wooden handle from splitting lengthwise and extend handle life. Criteria: the sheathing sits tight to the wood; no shake under the hand.

## Master Parameter Table

| Parameter | Value | Class |
|---|---|---|
| Charge grade | ≥40%, grain 5–20 mm, dry | Threshold |
| Layer ratio (ore : charcoal) | 1 : 1.5–2 | Empirical starting point |
| Total charcoal per run | 80–120 kg (including heat storage and losses) | Empirical |
| Steady-state charcoal consumption | 20–35 kg charcoal / kg dense iron | Empirical range, must be calibrated |
| Iron per run | 1.5–3 kg dense stock | L2 criterion |
| Run duration | 6–9 h, 3–4 people in shifts | Empirical |
| Tuyere bore | 25–40 mm, angled down 10°–15° | Empirical |
| Slag thread target | 50–100 mm continuous fine filament | Empirical, calibrated against coupons |
| Forging heat window | Bright orange–bright yellow (1000–1200 ℃), 1–3 min per heat | Window |
| Fold count | 3–6 total, 1 per heat, directions crossed | Empirical |
| Lining life | 3–8 runs | Empirical |
| Double-tuyere bore and tolerances | 20–30 mm each; height difference ≤10 mm, convergence deviation ≤15 mm | Empirical tolerances, verified with the straight rod on the cold furnace |
| Air-superheating duct length | 250–350 mm, judged by the charcoal account | Empirical, calibrated against a comparison furnace |
| Slag notch position (sloped hearth) | 30–50 mm above the highest point of the hearth floor, floor slope 5°–8° | Empirical |
| Forge-welding fire-color window | Bright yellow–near-white (about 1250–1350 ℃), weld at sweating | Window, calibrated by stepped trial welds |
| Hot-shrink allowance | Band inner diameter 1‰–2‰ smaller than the shaft | Empirical, calibrated by cold trial of the sample ring |
| Rivet hole clearance | ≤1 mm larger than the shank's cold diameter; pitch 3–6× plate thickness | Empirical starting point |

## Failure Modes and Diagnosis

| Symptom | Candidate causes (by probability) | Verification | Disposition |
|---|---|---|---|
| The whole run yields no iron (pancake all slag) | ① air short (dark flame, sluggish burden) ② ore not dry ③ grade overstated | One by one: watch the flame, grab ore and test for dampness, re-test the grade | Add air first next run; dry the ore; back to beneficiation |
| Little iron, glossy black slag | Reduction short / iron lost into slag | Slag-sample reading (Section 18.5.1, black glassy) | Lengthen the run; verify the layer ratio |
| Pancake locally converted to white cast iron | Hearth overheated (slag thread >150 mm) | Recheck by the slag-rod method; conchoidal fracture | Register the white iron as Grade D into the stir-refining line; cut air next run |
| Furnace hang-up (burden will not sink) | Charcoal excess / ore too fine / early crusting not broken up | Probe-rod records | Break it loose; adjust the layer ratio next run |
| Cracks at the first forging blow | ① hammered too cold ② high-sulfur hot shortness ③ white cast iron mixed in | Read the fracture (slag line vs yellow slag spots vs conchoidal) | Reheat and return to the forge; flag the brittleness-source ore site; divert the white iron |
| Finished piece peels in layers | Folding short / directions not crossed | Slag-line direction on the fracture | Add 1–2 folds and reforge |
| Falls apart the more it is hit | Forging continued on overcooled stock | Read the color (below dark red) | Back to the furnace at once; cold hammering forbidden |
| Bar bubbles in streams in the water quench | Not dense | Count the bubbles | Add heats |
| Lining burned through | Tuyere locally too close / poor mix | Campaign archive | Patch with clay and repair; thicken next campaign |
| Double-tuyere air short-circuit | ① tuyeres mismatched in height or angle — air races along the wall straight to the mouth ② one tube blocked with charcoal, all air through the other ③ air volume short, the air "cannot move" | Symptoms: top flame overly fierce while the tuyere-plane temperature does not rise; burden sinks fast but iron yield low; re-verify convergence with the straight rod, pull the tubes to check for blockage | Shut down and re-verify (height difference ≤10 mm, convergence deviation ≤15 mm), then seal again; clear the tubes; resume running above the air-volume floor — if the air cannot be supplied, fall back to a single tuyere |
| Forge-weld false weld | ① fire color short (welded before sweating; most common) ② scale not stripped from the weld faces ③ slag trapped in the lap gap | Spot-break: a break at the weld is a false weld; a 90° bend delaminates | Cut it out and reweld once (a second false weld is scrap); enforce the Section 18.12 three cleaning steps to the letter |
| Rivets crack on riveting | ① upset at too low a temperature ② rivet stock slaggy / brittleness source ③ hole too small, upsetting allowance too large | Read the crack pattern: radial head cracks point to rivet temperature and hole diameter; a crack crossing the shank section points to the rivet stock — check its fracture | Rivet at bright orange or above; switch to Grade A stock rivets; re-verify hole diameters |

## Process Card Index

## Acceptance Criteria

- **L1**: The bloomery is built and run through one complete cycle, yielding a bloom pancake containing metallic iron in the hearth (a metallic-luster iron skeleton visible in the fracture); one heat of forging completed (densification visible).
- **L2**: Three consecutive runs yield ≥1.5 kg of dense iron per run; every run's slag samples, parameters, and three inspections complete on file; bar stock bends ≥8 times without breaking; the iron hammer + iron chisel pass the functional test and complete the bootstrap replacement.
- **L3**: The three classes of consumables — ore, charcoal, lining — are supplied on account with ≥2 runs in reserve; lining repair and campaign management executed across ≥3 campaigns; the graded iron stock library in operation; 2 or more people independently pass the full-run assessment; monthly iron output and charcoal-rate data continuously registered and used for tuning (entered in the Chapter 38 ledger). Evidence: campaign archives, inventory ledger, assessment records.

## Labor, Manpower, and Consumption

| Item | Manpower | Labor hours (empirical) |
|---|---|---|
| Furnace build (including drying wait) | 2 people | 3 days net work + 3 days shade-drying + 1 day furnace curing |
| One run | 3–4 people in shifts | 6–9 h (including charging and drawing) |
| Densifying one pancake | 2 people (1 hammer, 1 holder) | 4–8 h (5–10 heats) |
| One iron hammer | 1 person | 0.5–1 day |
| Consumption per run | Charcoal 80–120 kg, ore 20–40 kg, lime 0–4 kg | Entered in the Chapter 38 ledger |

## Safety Boundary

- **CO poisoning**: runs last 6–9 h; blasting in shifts, ≤30 min per person; the furnace area in the open or in a shed open on all four sides; the keeper's station upwind; withdraw immediately at headache, nausea, or dizziness (the Chapter 6 iron rules apply in full — Iron Law Seven).
- **Burns and molten slag**: the drawn bloom runs 800–1000 ℃; fire tongs / carrying bars throughout; leather apron + leggings + gloves complete before anyone enters the drawing area; forging sparks carrying slag are the main injury source — sleeves tied tight, neck covered.
- **The forging-hammer zone**: no standing within 2 m of the anvil; a call before every swing; the holder stands at 45° behind the striker's side.
- **Burned-through stock**: a piece throwing bursting sparks goes at once to the cooling area; continuing to hold and forge it is forbidden.
- **The quench bucket**: ≥1 m from the furnace mouth; pieces enter the water facing away from people.
- The first run and the curing period are led by someone with Chapter 17 copper-smelting experience; novices serve only as assistants.

## A. Existing Tools List

Chapter 16 iron-ore evaluation, crushing table, panning pan; Chapter 17 crucible master processes, carrying-bar pouring, copper hammer and chisel, smelting archives, leather protection; Chapter 12 high-temperature furnace, bellows, refractory clay, standard samples, furnace-and-kiln repair procedures; Chapter 11 refractory clay, ceramic tubes, brick, kilns; Chapter 6 metallurgical charcoal, fire management, CO procedures; Chapter 9 grinding table, templates, rope-loop clamps; Chapter 13 lime.

## B. New Tools Added in This Chapter

Shaft-type bloomery furnace (with ceramic tuyere and drawing mouth); slag-sample register and slag rod (slag-rod temperature reading); forging hearth (heating pit / furnace-mouth position); stone-anvil forging station → iron anvil (bootstrap replacement); hard-stone hammer → iron hammer; wooden-fork fire tongs → iron fire tongs; standard iron bar stock and the graded iron stock library; iron chisel, iron adze, iron axe; furnace-number iron stock archives (including the bend-sample library); double-tuyere verification straight rod and water bowl, air-superheating duct extended ceramic tubes; sloped-hearth slope template, notch-plug clay; flux jar (quartz sand); ring-bending mandrel, cupping anvil (for riveting), hot-shrink sample ring.

## C. Unresolved Dependencies

No thermometer (Chapter 25; until then all thermal work is managed by "calibration + windows"); no carbon/sulfur/phosphorus testing (Chapters 23 and 26); capacity ceiling at the kg level (liquid ironmaking + refining await a full upgrade in air volume, coke, and refractories — long term); forging entirely on human power (the water-powered forge hammer awaits Chapter 21); slow grinding (hard abrasives registered and waiting; abrasives formalized in Chapter 19).

## Next-Step Dependencies

Chapter 19: this level's iron stock and "suspected steel stock" go straight into carburizing and heat treatment; the iron anvil and iron hammer are the workholding base for quenching and edge-tool making. Chapter 20: all machine-tool structural stock is taken from this chapter's standard bar stock. Chapter 21: waterwheel shafts, gears, and bearing blanks are supplied by this chapter; mechanical power feeds back into crushing and blasting. Chapter 16 upgrade: iron hammers and iron drills push mining into shallow-pit extraction. Chapter 38: steady-state charcoal consumption and iron output enter the energy-and-materials ledger.
