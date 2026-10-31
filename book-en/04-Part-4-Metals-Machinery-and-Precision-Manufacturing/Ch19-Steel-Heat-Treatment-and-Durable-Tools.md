# Chapter 19: Steel, Heat Treatment, and Durable Tools

> Part 4: Metals, Machinery, and Precision Manufacturing. Chapter 18 delivered wrought iron stock; this chapter turns iron into steel and steel into durable edge tools, and establishes material grading, defect identification, and a regrind–requench regime. Two red lines run through the whole chapter: first, heat color and strike sound are **auxiliary means only**; second, of the three heat-treatment steps (carburizing—quenching—tempering), not one may be missing when a tool is delivered.

## Chapter Objectives

- Establish the "carbon content determines properties" discrimination system: four methods — fracture, bending, hardening, sparks — to grade iron stock.
- Walk through the solid carburizing process: converting the surface layer of wrought iron into high-carbon steel, with controllable, inspectable case depth.
- Walk through quenching and tempering: media graded by carbon content, the interrupted quenching (water-then-oil) method, and the tempering-color scale window.
- Design hardness–toughness ratios by use: chisels, saws, axes, and hammers each to their own table.
- Manufacture and accept the first batch of steel edge tools; establish recognition and prevention of the three quench-crack patterns.
- Establish a regrind–requench cycle regime and a material grading library, making the tool system "repairable and remanufacturable."
- Deliverables: ≥1 kg carburized steel stock, 2 qualified chisels and 2 qualified saws, the material grading library, and heat-treatment records.

## Capability Boundaries

**Can do:** carburized case depth controllable at 0.5–2.5 mm (±0.5 mm); quench hardness judged at three levels by "scratch sequence + file test"; tempering double-judged by color scale + test coupon; tool life accepted by functional testing.

**Explicitly cannot do:**
- Chemical quantification of carbon content (awaiting Chapters 23, 26) — grading relies on source control + the three live tests;
- Deep-hardenability alloy steels (manganese and chromium ore sources not surveyed; listed as a Class-C dependency);
- A stable spring-steel process (to be tackled when Chapter 21 needs it; this chapter does not pretend to solve it);
- Temperature-stable quench media and precise temperature control (no thermometer; glass thermometers come in Chapter 25).

**Upgrade criterion (unavailable now; enabled as soon as its prerequisite is built):** the spark carbon test requires a foot-treadle speed-up grinding wheel (rim speed on the order of 5–10 m/s, available after Chapter 20's cone pulleys + Chapter 21's belt speed-up). This section gives the full table (Section 19.2.2); when the time comes, train against known samples from the grading library before putting it into service.

## Pre-Start Verification (check item by item)

| # | Verification item | Criterion | Source |
|---|---|---|---|
| 1 | Graded iron-stock library | Every batch has a fracture record and bending samples; "suspected steel" batches marked separately | Chapter 18 |
| 2 | Forge | Can hold a steady bright orange (approx. 900–1100 °C, re-verified by the standard-coupon method) | Chapters 12, 18 |
| 3 | High-temperature furnace soak | Holds 900–1000 °C for ≥8 h (the carburizing box fits inside with clearance around it) | Chapter 12 |
| 4 | Carburizing box | **Refractory-clay saggar** (made from the Section 11.8 refractory base mix, wall ≥10 mm with lid; fireclay seal leaving only one pinhole); **first box empty-fired at the 1000 °C level × 2 h without cracking before it may be charged** — ordinary pottery softens at 900 °C and is forbidden | Chapter 11 |
| 5 | Three quench-medium tubs | Still-water tub (≥15 L), oil tank (animal fat/fish oil, with lid), brine tub; water and oil temperatures logged | Chapters 10, 15 |
| 6 | Hardness reference set | Three standard blocks — copper, wrought iron, hardened steel; a file or a sharp edge of hardened steel usable | Chapters 17, 18 |
| 7 | Test-coupon library | ≥3 companion coupons fired with the stock of each batch (every carburizing/quenching furnace run must have companion coupons; no companion, no firing) | This chapter's regime |

---

### 19.1 The Difference Between Iron and Steel

**One variable makes four materials: carbon.**

| Material | Carbon content | Fracture appearance | Forgeability | Quench response | Use at this stage |
|---|---|---|---|---|---|
| Wrought iron | <0.1% | Gray, fibrous, ragged | Excellent | **Will not harden** | Structural parts, forgings, carburizing feedstock |
| Mild steel (low-carbon steel) | 0.1%–0.3% | Gray fine grain, slightly bright | Good | Slightly hard | Parts needing toughness, riveted forgings |
| Hard steel (high-carbon steel) | 0.3%–1.5% | Bright white fine grain | Moderate (good when hot) | **Hardens markedly** | Edge tools, springs, punches |
| Cast iron (brittle iron) | >2% | Coarse bright white grains, shell-like | **Not forgeable** (shatters at a blow) | Hard and brittle | Treated at this stage as an "accident product"; log and quarantine (white cast iron reserved for the puddling conditional route, Section 19.8.2) |

**Principle: before you lay hands on any piece of stock, you must know whether it is iron or steel.** Tools made on guesses fail halfway through their work and cannot be reworked.

### 19.2 How Carbon Content Affects Properties

#### 19.2.1 Behavioral Grading Table (primary field criterion)

**Mechanism (one paragraph, for understanding not memorization):** carbon exists in iron as iron carbide (an extremely hard, brittle compound), forming a mixed structure with the iron. The more carbon, the more hard particles — the harder and more wear-resistant the material, but the lower its toughness reserve; past about 2% carbon the brittle compounds link into a network and the material loses forgeability entirely. **Quenching** "freezes" the carbon dissolved in the iron at high temperature into a supersaturated structure — extremely hard; **tempering** reheats moderately to relieve part of the internal stress, sacrificing a little hardness to buy toughness back.

| Carbon magnitude | Forgeability | Behavior after quench | Bending behavior (as-quenched) | Suitable uses |
|---|---|---|---|---|
| ≈0.1% (wrought iron) | Excellent | No hardening | Bends any way without breaking | Nails, chain, structural parts, carburizing blanks |
| ≈0.3% | Good | Light hardening | Bends 90°, springs back, does not break | Impact-tough tools: chisel bodies, axe bodies |
| ≈0.6% | Moderate | Clearly hardens | Breaks after about 30°–60° of bend | General edge tools: chisels, knives, axe edges |
| ≈0.8%–1.0% | Moderate-poor | Hardens strongly | Breaks with slight bending | Saws, drills, gravers, punches |
| >1.2% | Poor | Hardens strongly but extremely brittle | Shatters on any bend | File-blank stock, fine gravers (little used at this stage) |

**Edge-tool window conclusion:** chisels, knives, and axe edges take **0.5%–0.9%**; saws and drills take **0.8%–1.0%**; impact-loaded hammers and drill steels take **<0.3% or no quench at all**. At this stage there is no chemical analysis, so carbon content can only be controlled at the source: bloomery-smelting iron is naturally near-zero carbon (wrought iron); high-carbon stock comes from Chapter 18's "suspected steel" batches and from this chapter's carburizing — case depth is controllable (high-carbon surface, low-carbon core), so **the "wrought-iron body + carburized surface layer" route is the most controllable choice for edge tools**.

**Grading test method (run on every batch of iron stock entering the library):** draw 1 bar, forge it into a strip about 10×200 mm, heat one end to bright orange and quench it in water, then scratch the quenched end against the unquenched end:

- The quenched end clearly cannot scratch the unquenched end → steel stock (carbon on the order of ≥0.3%), mark "steel," enter the edge-tool candidates;
- The two ends scratch each other with no difference → wrought iron, mark "iron," use as structural stock or carburizing feedstock;
- The whole batch breaks on quenching → carbon too high or a brittle source (sulfur-phosphorus / burnt), mark "brittle source," quarantine, and trace back through Chapter 18's furnace-number records.

[Card 19-01 Iron-Stock Grading Test] (eight fields)

1. **Input materials**: 1 bar drawn from every batch of iron stock entering the library (forged into a standard strip about 10×200 mm); 1 companion coupon of the same source as the batch; a hardness reference set of three blocks — copper (soft), wrought iron (medium), hardened steel (hard).
2. **Tools required**: forge (able to hold bright orange), tongs, still-water tub, anvil and hand hammer, fracture bench; a standard steel coupon fired in the same heat (heat-color reference); scratch and grading record sheet. Calibration source: every heat-color call is checked against the standard steel coupon in the same fire — a grading made on color alone is never accepted.
3. **Sequence and control points**: ① forge the standard strip (10×200 mm) → ② heat one end to bright orange, **even along the whole section; local overheating causes misjudgment** → ③ **enter vertically into water, depth ≥100 mm, agitate at once** → ④ when cold, scratch the two ends against each other, then against all three reference blocks → ⑤ record and grade. Reading: the quenched end clearly cannot scratch the unquenched end = steel (≥0.3% order, enters the edge-tool candidates); no difference either way = wrought iron (structural stock or carburizing feedstock); the whole batch breaking on quenching = brittle source — quarantine it and trace the Chapter 18 furnace number.
4. **Empirical parameters and calibration**: standard strip 10×200 mm; entry depth ≥100 mm; bright orange about 900–1100 ℃ (verified by the standard-coupon method) — **empirical values, to be calibrated to local conditions**. Calibration method: fire the standard steel coupon together with the bar under test and compare both the heat color and the color of the hardened end; **insufficient entry temperature is the number-one cause of misjudging stock as "wrought iron,"** so only the coupon-verified conclusion counts.
5. **Observations to record**: batch and furnace number / pieces drawn / heat color (against the coupon) / entry posture and depth / scratch difference between the two ends / scratch results against the reference blocks / surface color of the hardened end (silvery bright = normal, blue-black = critical point not reached) / grading verdict and number of pieces quarantined.
6. **Pass / rework / scrap criteria**: pass = an unambiguous verdict with the end-to-end scratch difference on record; rework = coupon temperature doubtful — re-verify by the coupon method and redo once; scrap = the whole batch breaks on quenching (the batch is graded brittle source and quarantined; cherry-picking pieces out of it is forbidden).
7. **Common failures and diagnosis order**: (1) the whole batch grades "iron" → check first whether the heating reached temperature, then the entry depth and whether it was agitated; (2) the whole batch grades "steel" → mixed charge from the previous heat, check the furnace-number records; (3) the whole batch breaks on quenching → carbon too high, or a sulfur-phosphorus / burnt brittle source; quarantine and trace the Chapter 18 records; (4) scratch and fracture verdicts conflict → redo the scratch test first, then take a fracture from another spot; if they still conflict, go to the service-test arbitration of Section 19.12.2.
8. **L1 / L2 / L3 evidence**: L1 = one batch graded and on file; L2 = five consecutive batches whose grades agree with later service performance; L3 = the four-color grading library in operation, 20 blind tests with ≥16 correct, and a misgrade rate of zero (traced backward through service feedback).

#### 19.2.2 Spark Carbon Test (upgrade criterion; full table for reference)

Conditions: a foot-treadle speed-up grinding wheel (Chapter 20 cone pulleys + belt speed-up; rim speed on the order of 5–10 m/s). Hold the stock in hand, press it lightly against the rim, and observe the spark stream (dark background, viewed from the side against the light):

| Carbon grade | Spark stream | Stream lines | Burst flowers | Reading mnemonic |
|---|---|---|---|---|
| Wrought iron/low carbon | Short, sparse | Coarse and few, bright yellow | Almost no forking | "One line straight through, never forking" |
| ≈0.3%–0.5% | Gradually longer and denser | Many and fine | Forking begins, single burst | "First bloom on the fork" |
| ≈0.6%–0.8% | Long, bright, dense | Fine and dense, in bundles | Multi-layer forking, **with pollen** (pinprick tiny bright stars) | "Pollen appears — tool steel" |
| ≈1.0%–1.3% | Brighter and denser still | Very fine | Bursts thick and dense, pollen in patches | "A tree full of silver blooms — high carbon" |
| Cast iron | Short, dull red | Fine and fragmented | Very few, dull | "Red, fragmented, dull fire — cast iron" |

◎Reading must use the **known-sample comparison method**: grind the four-grade library samples and the test piece one after another on the same wheel, with the same pressure and the same lighting, and compare the differences — do not memorize the table. Training method: 20 blind tests (someone else samples at random; the record is opened against the answers only after judging); at least 16 out of 20 qualifies you for stock-grading duty. Misjudgment fallback: whenever the sparks are doubtful, return to the scratch grading method (Card 19-01) as arbiter.

### 19.3 Basic Principles of Carburizing, Quenching, and Tempering

#### 19.3.1 Solid Carburizing (turning wrought iron into surface steel)

Principle: at 900–1000 °C carbon atoms diffuse into the iron's surface; depth grows with temperature and time. The carbon-monoxide atmosphere formed inside the sealed box is the porter that carries the carbon.

**Packing recipe (empirical starting point; must be field-calibrated):** crushed charcoal (2–5 mm) 70–80% + bone ash or leather ash 10–20% + potassium carbonate (evaporated from wood-ash lye, Chapter 8) 5–10%. Bone/leather ash supplies phosphorus and carbon and promotes carburizing; potassium carbonate raises the atmosphere's activity. All packing must be dry (wet packing = uneven case).

**Case-depth–time table (900–1000 °C range; empirical values; must be field-calibrated):**

| Soak time | Expected case depth |
|---|---|
| 4 h | 0.3–0.5 mm |
| 8 h | 0.5–1 mm |
| 16 h | 1–1.5 mm |
| 24 h | 1.5–2.5 mm |

Depth versus time is **not linear** (it grows roughly as √time) and is extremely sensitive to temperature: 50 °C low, and the same time may halve the case depth. **Calibration method: bury 3 coupons at different positions inside the box; after opening, fracture them one by one and measure the case depth** — a large positional spread = uneven temperature inside the box; fix the furnace before discussing the process.

[Card 19-02 Solid Carburizing] (eight fields)

1. **Input materials**: forged blanks with grinding allowance left on (single-side allowance by use: chisel edge 0.8–1.0 mm / axe edge 1.0–1.2 mm / punch and drill 1.3–1.5 mm; surface filed to fresh metal, free of scale and oil); packing (charcoal crushed to 2–5 mm 70%–80% + bone ash or leather ash 10%–20% + potassium carbonate 5%–10%, all dry — wet packing means an uneven case); fireclay sealing compound; 3 coupons forged with the same batch (T / W / C positions, wire-tied lettered tags); charcoal (for the furnace).

2. **Tools required**: carburizing box (pot + lid, box number recorded); high-temperature furnace (Chapter 12, standard coupon + box color double check); coupons and a fracture bench (hammer, anvil, rule); long-handled tongs; mortar and sieve (crushing charcoal, mixing); water for wet mixing and a mask (bone and leather ash are wetted to avoid inhaling dust); the carburizing ledger (box number, three-coupon depths, packing batch, reuse count). Calibration source: temperature by standard coupon (the Chapter 12 cone system) + box color (dark orange = at temperature); case depth measured on the fracture, never guessed from color.

3. **Sequence and control points** (prepare blanks → load the box → seal → soak → slow cool → open and judge the box): ① **Prepare the blanks** — file off scale and oil, leave the allowance from the use table. ② **Mix the packing** — dry-mix the three components, charcoal at 2–5 mm; wet-mix the bone/leather ash before blending it in. Control point: the packing must be dry. ③ **Bed the bottom** — 20 mm of packing on the box floor. ④ **Load** — workpiece centred, ≥15 mm of packed, tamped packing all round. Control point: workpieces must not touch one another and **must not touch the box wall** (touching the wall = short case on that face). ⑤ **Insert the coupons** — T (box centre) / W (mid-radius) / C (box corner), numbered at fixed positions. ⑥ **Seal the lid** — fireclay, **leaving exactly one pinhole** (it vents and verifies the seal: thin smoke early on; no smoke = sealed dead and the pressure will lift the lid; thick smoke = the seal leaks). ⑦ **Soak** — 900–1000 ℃ per the depth–time table (4 h 0.3–0.5 mm / 8 h 0.5–1 mm / 16 h 1–1.5 mm / 24 h 1.5–2.5 mm; depth grows roughly as √time, and 50 ℃ lower can halve it at the same time). ⑧ **Slow cool** — box and all buried in hot ash overnight; never open it to cool fast. ⑨ **Open and judge the box** — fracture the three coupons and measure: spread <0.5 mm = box passed; 0.5–1.0 mm = take the shallowest coupon; >1.0 mm = the whole box downgraded pending verification (fracture 1 piece in 5). ⑩ **Accept the batch** — only when it is up to spec does the whole batch of workpieces pass, with the basis for the depth taken and the box number entered in the ledger. Control point: pinhole smoke is the only on-line signal of the atmosphere; if the positional spread is large, fix the furnace before discussing the process.

4. **Empirical parameters and calibration**: carburizing temperature 900–1000 ℃ (window); depth–time 4 h 0.3–0.5 / 8 h 0.5–1 / 16 h 1–1.5 / 24 h 1.5–2.5 mm (empirical, √time growth, to be calibrated locally); packing charcoal 70%–80% + bone/leather ash 10%–20% + potassium carbonate 5%–10% (empirical starting point); three-coupon spread <0.5 mm pass / 0.5–1.0 take the shallowest / >1.0 pending verification; box admission — a box type with three consecutive boxes under 0.5 mm enters the "approved box list", and new or repaired boxes re-run the three-box verification; packing reuse topped up with 30% new charcoal (by volume) each time, at most 3 times, with a full recalibration before the 4th (reused packing shifts the whole depth–time relation shallower); post-carburizing single-side grinding allowance = case × 0.3 (uniform-band ratio ≈0.7, the coefficient replaced by the measured ratio after local calibration); one box takes 2 people in shifts, 16 h soak + 0.5 day loading and unloading.

5. **Observations to record**: box number / packing batch / reuse count; loading sketch (workpieces and the three coupons); pinhole smoke behaviour (thin and steady / none / thick); box exterior color with the time it appeared; soak start, end and total; the three coupon depths (one value each for T / W / C) and the maximum spread; which basis the workpiece depth was taken on (mean / shallowest); cooling method and duration; sampling results.

6. **Pass / rework / scrap criteria**: pass = three coupon depths on target with a spread <0.5 mm, workpiece depth taken as the mean; marginal (0.5–1.0 mm) = depth taken as the shallowest coupon and the box marked "skewed"; rework = depth short — return the box for more time, the workpieces are not reforged; downgraded pending verification = spread >1.0 mm — fracture 1 piece in 5 of that box, and if the sample fails the whole box goes back for more carburizing; scrap = a leaking seal left the depth near zero with oxidation (packing and workpieces repacked and recharged); also, any crack, any burning, decarburization deeper than 2/3 of the case, or more than 3 cumulative requenches goes back to the furnace.

7. **Common failures and diagnosis order** (by frequency): ① no case ring (most common) → check in order: leaking seal, temperature short, damp packing; ② case ring uneven in thickness → uneven temperature in the box (read the three-coupon spread) or workpieces touching the wall; ③ a decarburized soft shell outside the case ring → the box leaked during the slow cool; ④ depth uniformly shallow with the three coupons agreeing → soak too short, or the packing reuse limit exceeded; ⑤ all three coupons shallow → furnace temperature low overall: fix the furnace, **never mask a sick furnace with longer soaking**; ⑥ C position shallowest, T deepest → corner dead zone: move workpieces inward, pack 20 mm of fireclay block between box and furnace wall; ⑦ depth drifting >0.5 mm from the 5th box on the same recipe → packing activity or furnace condition has drifted: retire the old depth–time table and recalibrate.

8. **L1 / L2 / L3 evidence**: L1 = one box with three coupon fractures on file (positions, individual depths, box number complete); L2 = two consecutive boxes within 0.5 mm, with the ledger able to trace recipe and reuse count from the box number; L3 = the site's "packing recipe–soak time–case depth" calibration written up and transcribed into the ledger, the approved-box list running, and a second person reproducing a passing three-coupon spread on the same box type from this card.

[Card 19-04 Interrupted Quenching (Water → Oil)] (eight fields)

1. **Input materials**: graded or carburized steel parts (edge tools in the 0.6%–0.9% carbon band; thin parts at 0.8%–1.3% belong to the oil-quench grade and do not use this card); clear water (still-water tub ≥15 L); animal-fat / fish-oil tank (lidded). **The higher the carbon and the thinner the part, the less a full water quench is allowed.**
2. **Tools required**: forge (750–800 ℃ cherry-red window), long tongs, water tub, lidded oil tank (≥3 m from open flame, a bucket of dry sand at hand, **water never used on an oil fire**), timing (spoken seconds or the Chapter 3 drip clock), scrap lengths for practice, standard steel coupon.
3. **Sequence and control points**: ① heat to 750–800 ℃ (cherry red to bright cherry red; standard coupon plus heat color judged together; overheating past bright yellow coarsens the grain and invites cracking) → ② **edge down, enter vertically, depth ≥100 mm, then stroke up and down to break the vapor film** → ③ cool in water a few seconds; **the instant the shudder / hiss stops, transfer to oil** (too early and it will not harden, too late and it cracks) → ④ cool in oil all the way (lid on, never lifted mid-way to look) → ⑤ **temper immediately on leaving the oil; never set the part aside overnight**. Control points: the card has exactly one hand-skill point — the transfer instant; thin parts entering flat-face are forbidden (violent warping).
4. **Empirical parameters and calibration**: water-cooling time ≈1 s per 3 mm of thickness — **empirical value, to be calibrated to local conditions**; entry depth ≥100 mm; stop quenching when the oil smokes heavily. Calibration method: split scrap from the same batch into "water 1 s / 2 s / 3 s" groups, bend-break them, compare hardened-case depth against cracks, set the standard on the best, and transcribe the seconds into the tool record.
5. **Observations to record**: stock batch number / heat color (against the coupon) / entry posture and depth / seconds in water / the hiss and shudder at transfer / whether the part rings dull out of the oil (a dull-sounding part is set aside alone — **brittle parts are never tested by hammering**) / the moment tempering began.
6. **Pass / rework / scrap criteria**: pass = the three-level scratch test passed (the hardened block scratches it, wrought iron does not) plus a plastic bend at 30°–60° without breaking; rework = soft spots (requench, ≤2–3 times in total, with a full anneal before the third); scrap = any crack, any burning (cracks cannot be repaired — back to the furnace).
7. **Common failures and diagnosis order**: (1) longitudinal crack (long straight axial crack, often the full length) → a high-carbon part given a full water quench; switch to interrupted or oil; (2) transverse crack (section changes, hole edges, edge roots) → tensile stress in the transition zone of a part not through-hardened; oil-quench and plug holes with wet clay; (3) local soft spots → still water with no agitation, or oil carried in on the surface; (4) the whole part not hard → heating short of the critical point, or transferred to oil too early; (5) warping → a thin part entered flat-face, or no vertical agitation after entry.
8. **L1 / L2 / L3 evidence**: L1 = one interrupted-quenched part passing scratch and bend; L2 = two consecutive batches of the same part form with the water seconds and hardness results comparable and the tool records complete; L3 = a second person runs the card alone and reads the same hardness grades.

#### 19.3.3 Tempering (buying the toughness back)

Temperature window 150–340 °C; the criterion is **temper color** (reheat the polished-bright quenched steel surface; the oxide film shows the color):

| Temper color | Temperature (°C, empirical) | Hardness | Applies to |
|---|---|---|---|
| Pale straw | 200–220 | Highest | Files, drills, gravers (most wear-resistant) |
| Straw/hay yellow | 220–240 | ↓ | Saws |
| Gold/deep yellow | 240–255 | ↓ | Knife edges |
| Brown yellow | 255–265 | ↓ | Chisels |
| Purple-red/purple | 270–285 | ↓↓ | Punches, axe edges |
| Blue | 290–300 | ↓↓ | Hammer faces, springs, shovels |
| Blue-gray | 320–340 | ↓↓↓ | Not for edge tools (too soft; used only as an annealing indicator) |

Operating rules:
1. **Judge at "color just showing"** — at the same temperature, the longer the time the deeper the color; watch the color early rather than late, and cool immediately when it is reached;
2. Color is only the surface — **after reaching color, wait 1–2 min for the core to reach the same temperature** (shorter for thin parts, longer for thick), then quench in water or set in still air;
3. The surface must be polished bright first (old scale color will deceive you); use side light, not backlight;
4. **Oil-bath tempering** (more uniform; first choice for thin parts): heat the oil tank until the surface just smokes (about 200–250 °C) and immerse the workpiece 30–60 min. Oil-temperature anchors: a water drop into the oil crackles ≈300 °C level; faint smoke on the surface ≈200 °C level (auxiliary criteria; re-verify with a coupon).

**Whole-process mnemonic: forge to shape → carburize (wrought-iron blanks) → quench hard → temper tough → grind the edge → deliver tested parts.** Skip any step and everything after it is void.

[Card 19-05 Tempering by Color Step] (eight fields)

1. **Input materials**: quenched parts not yet left overnight (old scale ground off and the face polished to bright metal); animal fat / fish oil for the oil bath; hot ash (for the buried slow cool).
2. **Tools required**: furnace-mouth hot-draft position or oil-bath tank (surface just smoking, about 200–250 ℃), grinding stone and wiping cloth, side-light position (never backlight), tongs, timing (spoken seconds or drip clock), the seven-step color table of Section 19.3.3.
3. **Sequence and control points**: ① polish the face to be tempered immediately after quenching → ② into the furnace-mouth draft or the oil bath, **watch the color in side light, one glance every 10 s** → ③ **judge at "color just showing"** (at the same temperature the longer the time the deeper the color; early rather than late) → ④ after the color shows, wait 1–2 min for the core to reach the same temperature (short for thin parts, long for thick) → ⑤ quench in water or set in still air (oil-bath parts soak 30–60 min first) → ⑥ color name and time into the tool record. Control point: color is only the surface — the 1–2 min of step ④ is never skipped.
4. **Empirical parameters and calibration**: seven color steps — pale straw 200–220 ℃ (files, drills, gravers; most wear-resistant) / straw 220–240 (saws) / gold 240–255 (knife edges) / brown yellow 255–265 (chisels) / purple-red 270–285 (punches, axe edges) / blue 290–300 (hammer faces, springs, shovels) / blue-gray 320–340 (not for edge tools, an annealing indicator only); oil-temperature anchors — a water drop crackling in the oil ≈300 ℃ level, faint smoke on the surface ≈200 ℃ level. **All values are empirical, to be calibrated to local conditions and re-verified with a coupon.**
5. **Observations to record**: part number / time quenching finished / how bright the polish is / color progression (color name every 10 s) / dwell after the color showed / cooling method and oil-bath duration / final color name / who read it.
6. **Pass / rework / scrap criteria**: pass = color step matches the use table, file / scratch checks pass, and service testing shows no chipping or curling; rework = under-tempered (raise one color step and re-temper, unlimited times) / over-tempered (grind off the discolored layer, requench and re-temper, ≤2–3 requenches in total); scrap = blue-gray or softer still used as an edge tool (too soft), the requench limit exceeded, or any crack.
7. **Common failures and diagnosis order**: (1) hard but chips at a touch → under-tempered; raise a color step and re-temper (the most used fix); (2) not hard, dulls fast → over-tempered, or grinding-heat tempering (dip the edge often; stop the moment it turns blue); (3) colors uneven across a batch → temperature varies with position in the furnace; place parts by position and watch each one; (4) colors read too deep → backlight was used or the surface was not polished bright; switch to side light and re-polish.
8. **L1 / L2 / L3 evidence**: L1 = one part tempered to its color step and passing scratch / bend; L2 = one batch at each of three color steps with archived color names comparable to measured hardness; L3 = two people reading the same part's color to within one grade, with the batch's color-step values transcribed into the ledger.

### 19.4 The Hardness, Toughness, and Brittleness Trade-off

**There is no free lunch that is both hard and tough:** of the same steel, the harder it is quenched the less impact it takes; the tougher it is tempered the less it resists wear. Designing a tool means picking a point on this line.

**Field hardness tests (three-level method):**
1. **Scratch-sequence method**: reference set — copper (soft), wrought iron (medium), hardened steel (hard). The new part is scratched by each reference block in turn: scratched by wrought iron = too soft (under-quenched / decarburized); scratched only by the hardened block = qualified edge-tool grade; even the hardened block cannot scratch it = too hard (under-tempered, brittle risk).
2. **File test**: press a standard file on the new part — skids without biting = hard; bites and produces chips = soft. The file test is also the practical criterion for "will the file cut it" (edge-tool hardness slightly below that of a file).
3. **Impact trial-and-error method**: treat scrap lengths from the same batch identically, hammer them, and see whether chips fly or they bend — if they chip, raise the whole batch one temper-color step and re-temper.

**Toughness test:** for the repeated-bending method (Chapter 18), the targets after quench-and-temper: chisels show a plastic bend at 30°–60° rather than brittle fracture; saw blades bend about 30° around a 50 mm log and spring back without breaking (empirical criteria; must be field-calibrated).

**Use-based selection master table (this chapter's design baseline):**

| Tool | Surface carbon / treatment | Quench medium | Temper color | Taboos |
|---|---|---|---|---|
| Chisel | Carburize 0.8–1 mm | Interrupted (water → oil) | Brown yellow—purple | Through-quenching the whole part in water (a hardened core means brittle fracture) |
| Axe | Carburize the edge 1–1.5 mm, rest wrought iron | Interrupted, edge only | Yellow—brown yellow | Hardening the whole axe |
| Saw | Carburize the whole blade, thin case (≈8 h) | Oil | Pale yellow—straw | Water quench (distortion and cracking) |
| Hammer | Wrought iron, not carburized; working face lightly hardened locally or not at all | Clear water, local only | Blue | Any through-hardening |
| Drill / punch | High-carbon stock or deep carburizing | Interrupted | Brown yellow | Over-fine tips (quench-crack source) |
| Knife | Single-face carburizing | Interrupted | Yellow | Burning the thin edge |

### 19.5 How to Make Chisels, Saws, and Edge Tools

[Card 19-03 Steel Chisel Full Process] (eight fields)

1. **Input materials**: Chapter 18 Grade-A wrought iron bar 20×20×200 mm (bends ≥8 times, fibrous fracture); one box of carburizing packing (recipe in Card 19-02); clear water in a still tub ≥15 L and a lidded oil tank; handle wood and wedges (for fitting); abrasives (grindstone, dipping basin).

2. **Tools required**: forge (750–800 ℃ cherry-red window for judging heat), anvil, hammer, tongs; angle plate (Chapter 3, to check the edge angle); carburizing box with three coupons, fracture bench; grinding bench; hardness reference set (copper / wrought iron / hardened steel); bend-test bench (fixed vise + angle reference); tool record card. Calibration source: temperature by standard steel coupon + heat color judged together; the quench seconds from a three-group comparison on scrap from the same batch (water 1 s / 2 s / 3 s); the edge angle measured with the angle plate, not by eye.

3. **Sequence and control points** (forge → carburize → quench → temper → grind → test → handle; the order may not be reversed): ① **Finish all hot forging first** — draw the taper, forge the edge (1 mm grinding allowance), forge the handle step. Control point: forging after the quench means scrap. ② **Normalize / anneal to shape**, file to fresh metal. ③ **Carburize** — the 60–80 mm edge-end section into the box at the 16 h level (case 1–1.5 mm; chisel edge target effective case 0.8 mm, carburizing target 1.1–1.2 mm); load, pinhole, ash-bury and slow-cool per Card 19-02, and accept only when the three coupon fractures pass. ④ **Grind the allowance** — 0.3–0.4 mm off each face (case × 0.3). Control point: check with a same-box coupon ground by the same amount — the remaining ring must be ≥0.8 mm before release. ⑤ **Heat and quench** — 750–800 ℃ (cherry red to bright cherry red), **quench only the 40 mm edge end**, enter vertically, depth ≥100 mm, stroke up and down to break the vapor film. Control point: the whole part into water through-hardens the handle too = a brittle handle. ⑥ **Transfer to oil** — water ≈1 s per 3 mm of thickness (empirical, to be calibrated locally); the instant the shudder / hiss stops, transfer, cool right through in oil with the lid on and no lifting to look. ⑦ **Temper** — **temper immediately on leaving the water**: polish the edge face bright, watch the color in side light to brown yellow–purple (the chisel step, 255–285 ℃), wait 1 min at color so the core catches up, then quench. ⑧ **Grind the edge** — 40°–50° (50° for hard rock), dip in water often. Control point: grinding until it burns the hand and turns blue = grinding heat re-tempering, soft edge. ⑨ **Three live tests** — three-level scratch, a plastic bend at 30°–60°, and 10 min chiselling granite with no chipping or curling. ⑩ **Handle and record** — Chapter 9.1 four-way attachment, numbered into the tool record. Control point: the card has exactly two hand-skill points — the oil-transfer instant and the 1 min hold at color; everything else runs on the numbers.

4. **Empirical parameters and calibration**: quench temperature 750–800 ℃ (cherry-red window); interrupted-quench water ≈1 s per 3 mm of thickness — empirical, to be calibrated locally (three scrap groups fix the seconds); temper colors brown yellow 255–265 ℃ / purple 270–285 ℃ (chisel step, empirical, verified on a coupon); edge-tool carbon window chisel and axe 0.5%–0.9%; carburizing 16 h ≈ 1–1.5 mm; chisel edge target effective case 0.8 mm, carburizing target 1.1–1.2 mm, single-side removal 0.3–0.4 mm, total single-side forging allowance 0.8–1.0 mm; edge angle 40°–50° (50° for hard rock); bend acceptance 30°–60° plastic bend without breaking; entry depth ≥100 mm; one piece takes 1 skilled worker 1–1.5 days; per quench day 10–20 kg charcoal, 0.5–1 kg oil, 30 L water.

5. **Observations to record**: stock batch number (→ Chapter 18 furnace number); carburizing box number and three coupon depths; measured remaining ring after grinding; heat color (against the coupon); entry posture and depth; seconds in water; the hiss and shudder at transfer; temper color name and hold time; edge angle (angle-plate reading); the three live tests; regrind / requench count and reasons. **A tool with no record is downgraded to "unverified"** and may not be used for critical work.

6. **Pass / rework / scrap criteria**: pass = three-level scratch passed (the hardened block scratches it, wrought iron does not) + a plastic bend at 30°–60° without breaking + 10 min chiselling granite with no chipping or curling; rework = under-tempered (hard but chips at a blow: raise one color step and re-temper, unlimited times) / soft spots (requench, ≤2–3 times in total, with a full anneal before the third); scrap = any crack (unrepairable, back to the furnace), any burning, decarburization deeper than 2/3 of the case, more than 3 cumulative requenches.

7. **Common failures and diagnosis order** (by frequency): ① hard but chips at a blow → under-tempered, raise a color step and re-temper (the commonest fix); ② edge dulls fast, local hollows after grinding → soft spots (still water, no agitation, oil on the surface at entry) or the case ground through (allowance < case ×0.3, depth taken as the three-coupon mean instead of the shallowest) — requench or return to the box; ③ transverse crack at the edge root → sharp section change not rounded, water quench used on a stepped part — oil-quench, plug holes with wet clay; ④ longitudinal crack (straight down the axis, full length) → a high-carbon part given a full water quench — switch to interrupted, temper on leaving the water; ⑤ warping after the quench → wrong entry posture, or a thin section entered flat — straighten hot at about 200 ℃ after tempering; ⑥ blue color while grinding, edge goes soft → grinding heat re-tempering — dip often, stop at the first blue; ⑦ handle snaps → the whole part was quenched through — quench only the 40 mm edge end; ⑧ fine surface cracking days later → stress in the decarburized layer or over-grinding — prevent decarburization next batch, grind light and dip often.

8. **L1 / L2 / L3 evidence**: L1 = one chisel passes the scratch, bend and granite tests with the record complete; L2 = two pieces from independent batches pass, and at least one case of each Section 19.6 defect has been identified and handled on file; L3 = the regrind–requench ledger running continuously for ≥1 month, and a second person completing the same part form from this card and reading the same hardness grade.

### 19.6 How to Recognize Common Heat-Treatment Defects

#### 19.6.1 Three Quench-Crack Patterns (special topic — the pattern is the diagnosis)

| Pattern | Appearance | Conditions of occurrence | Prevention |
|---|---|---|---|
| **Longitudinal crack** | Long straight crack along the axis, often running the whole length | Fully through-hardened high-carbon part + violent water/brine quench; surface scratches are crack starters | Forbid full-length water quenching of high-carbon parts (switch to oil or the interrupted quench); **immediately** temper after quenching; file off surface scratches before the quench |
| **Transverse (arc) crack** | Crack perpendicular to the axis or arced, mostly at section changes, hole edges, and edge roots | Tensile stress in the transition zone between the hardened case and the soft core of a part that is not through-hardened; stress concentration at sharp corners and abrupt thick-thin changes | Design rounded transitions and avoid thickness ratios >2:1; plug holes with wet clay to slow the cooling of the hole wall; parts with abrupt section changes are always oil-quenched |
| **Network cracking (crazing)** | Fine, dense, turtle-shell cracks at the surface, often appearing after grinding or days later | Tensile stress in a thin decarburized surface layer; grain-boundary oxidation; over-pickling | Prevent decarburization (fast heating, a sound carburizing box); light grinding with frequent water dips; halve the pickling time (links to Chapter 23) |

**Cracked parts are scrapped back to the furnace, every one** — cracks cannot be repaired, and any "try quenching it once more" is wasted fuel. The diagnostic value lies in **working backward to which step of the process went wrong**, and fixing the next batch.

#### 19.6.2 Defect Master Table (symptom → cause → countermeasure → reworkability)

| Defect | Symptom | Cause | Countermeasure | Reworkable |
|---|---|---|---|---|
| Burning | Sparks burst off while heating, the surface fuzzes; oxidized patches on the fracture | Local temperature near melting | Cut the section off | **Not reworkable** |
| Quench crack | Dull sound on leaving the bath, surface crack lines; breaks at a hammer strike | See the three patterns in Section 19.6.1 for graded handling | Cracked = scrap to the furnace | No |
| Distortion | Bends or warps after quenching | Wrong entry posture, thin parts entered flat-face, uneven cooling | Vertical entry + agitation; oil for thin parts | Straighten hot at about 200 °C after tempering |
| Soft spots | Local softness; local fast dishing after grinding | Vapor film not broken (still water, no agitation); surface oil carried into the bath | Agitate on entry; degrease and dust off before entry | Requench (yes) |
| Decarburization | Surface soft as wrought iron; a soft shell outside the case ring on carburized parts | Long high-temperature exposure in an oxidizing flame | Heat fast, flame slightly reducing, seal the carburizing box | Usable if grinding off the soft shell still leaves enough case; otherwise re-carburize |
| Under-tempering | Hard but chips at a touch | Temper temperature too low / time too short | Raise a color step and re-temper | **Repeatedly repairable (the most used fix)** |
| Over-tempering | Not hard; dulls quickly | Temperature too high; grinding-heat tempering | Grind off the discolored layer, requench, re-temper | Yes (count limited by Section 19.7) |

**Diagnosis sequence:** classify the symptom → check that furnace batch's heat-treatment record → localize along the four variables "temperature—medium—posture—time," one variable at a time (the Chapter 8 method) → reproduce and verify on a coupon from the same batch → revise the process card version.

**Explicit limits on the auxiliary means:** heat color, temper color, and strike sound are all auxiliary grading — affected by ambient light, surface condition, part shape, and grip, their error can reach a full grade or more; every conclusion defers to the three live tests of **scratch + bend + use**.

### 19.7 Tool Regrinding and Repeated Heat Treatment

**Regrind procedure (daily):** wipe clean and grease after use; grind as soon as the edge dulls, the angle checked unchanged against the angle plate — **grinding marks parallel to the edge are the evidence that the angle is unchanged**. Grinding-heat alert: stop as soon as it burns the hand or shows blue. Edge chipping <2 mm: grind it shorter and re-form the edge; >2 mm: hot-forging repair (anneal → forge closed → requench and temper).

**Repeated heat-treatment regime:**
- **Re-tempering:** unlimited;
- **Requenching:** ≤2–3 times per part; before the 3rd time it must be fully annealed (cherry-red upper limit, 1 h soak, buried in ash for an extremely slow cool) to refine the structure before quenching again;
- **Scrap criteria:** cumulative requenches >3, any crack, burning, or decarburization deeper than 2/3 of the case → back to the furnace (iron-stock account, recovery column).

**Tool record** (one file per edge tool): number, stock batch number (→ Chapter 18 furnace number), carburizing time, quench medium and interrupted-quench seconds, temper color, three-live-test results, regrind/requench counts and reasons. **Tools with missing records are downgraded to "unverified parts" and may not be used for critical work.**

### 19.8 How to Build a Stable Tool-Material System

#### 19.8.1 Material Grading Library (four colors)

| Grade | Contents | Marking | Use |
|---|---|---|---|
| Iron Grade A | Wrought iron, ≥8 bends, fibrous fracture | White stripe | Structural parts, forge-welding bodies, carburizing blanks |
| Steel Grade B | Natural steel batches / forge-welded steel sections, hardening qualified | Black stripe | Direct stock for edge tools |
| Carburized Grade C | Carburized semi-finished parts (shelved by case depth) | Black-and-white twin stripes | Edge-tool blanks |
| Brittle-source Grade D | High sulfur-phosphorus / burnt / cast iron | Red stripe | **Quarantine**; white cast iron logged separately (next section) |

Every grade keeps fracture samples and bend samples in the library — this is the only way to turn "properties" into transferable information (Lineage 6).

#### 19.8.2 Puddling Decarburization of Pig Iron (conditional route, honest boundary)

When the bloomery furnace hearth overheats it occasionally produces **white cast iron** (bright white shell-like fracture; unforgeable). If ≥3 kg of white cast iron accumulates in the Grade-D library, a small **puddling** trial furnace line may be opened:

1. A shallow, flat hearth (built of fireclay, strong blast); the white cast iron blocks go in and melt to a semi-molten mush (it need not melt fully);
2. **Oxidizing flame** operation (blast biased high) — the opposite of reducing iron-smelting: at this stage you want oxygen to remove carbon;
3. **Stir and turn over** repeatedly with a wooden or iron rod (◎technique: as if stir-frying, so the mush surface meets the flame evenly); the carbon oxidizes and burns in the flame — **sparks turning from dense to sparse and the flame turning from bright white to orange** are auxiliary readings of the decarburization progress (empirical values; must be field-calibrated; the coupon fracture is the authority);
4. After about 30–60 min of stirring (empirical value), ball it up and draw it out; proceed to the fold forging of Section 18.6;
5. Every heat must have a coupon fractured and graded — puddled steel varies widely in composition; **grade each ball of stock separately**; never blend grades across a heat.

**Honest boundary:** without a thermometer or composition analysis, puddling is a process with an "extremely narrow empirical window" — this section is positioned as a **recovery route** for white cast iron, not as the main line of steel supply. The main line remains "wrought iron + carburizing."

[Card 19-06 Puddling Route (White-Cast-Iron Recovery)] (eight fields)

1. **Input materials**: white cast iron from the Grade-D library, ≥3 kg (bright white shell-like fracture, unforgeable, logged separately); charcoal; fireclay (to build the shallow flat hearth); coupon stock from the same source. **This card is a recovery route for white cast iron, not a main-line steel source** — the main line remains "wrought iron + carburizing."
2. **Tools required**: shallow flat hearth (fireclay, strong blast), bellows (able to bias the blast high), wooden or iron stirring rod, tongs, anvil and hammer (for the Section 18.6 fold forging), fracture bench.
3. **Sequence and control points**: ① charge the white cast iron and melt it to a semi-molten mush (it need not melt fully) → ② **operate with an oxidizing flame (blast biased high)** — the opposite of reducing smelting; here oxygen is wanted to burn the carbon out → ③ stir and turn repeatedly with the rod (◎ as if stir-frying, so the mush surface meets the flame evenly) → ④ after about 30–60 min of stirring, ball it up and draw it out → ⑤ proceed to the Section 18.6 fold forging → ⑥ **fracture and grade a coupon every heat; grade each ball separately and never blend grades across a heat**. Control points: semi-molten but not running, an oxidizing flame, and constant turning — miss any one and decarburization stops halfway.
4. **Empirical parameters and calibration**: opening threshold white cast iron ≥3 kg; stirring 30–60 min — **empirical, to be calibrated to local conditions**; progress anchors — **sparks turning from dense to sparse and the flame from bright white to orange** (empirical, to be calibrated; the coupon fracture is the authority). Calibration method: on the first heat draw 2–3 balls at different moments and fracture each, establishing this furnace's time-versus-fracture relation before fixing the draw moment.
5. **Observations to record**: charge weight / blast setting / stirring start and end / spark density and flame color (every 10 min) / the moment each ball is drawn / fracture grade of each ball / final grade after fold forging.
6. **Pass / rework / scrap criteria**: pass = the ball is forgeable and the fracture has gone from bright white shell-like to gray fine grain or fibrous, graded Steel B or Iron A; rework = decarburized too little (one more heat, timing re-recorded); scrap = burnt (sparks bursting, surface fuzzed, oxidized patches on the fracture) or still unforgeable (back to the Grade-D library and re-logged).
7. **Common failures and diagnosis order**: (1) still unforgeable after the heat → first check whether the blast really reached an oxidizing flame, then whether the stirring turned the whole mass; (2) decarburized past the target into "wrought iron" → stirring too long or blast too high; shorten the time; (3) composition swinging from ball to ball → per-ball grading was skipped; add coupons and grade each ball; (4) the ball crumbles instead of forming → furnace temperature too low (the mush never balled up); raise the blast and the heat.
8. **L1 / L2 / L3 evidence**: L1 = one heat producing a forgeable ball with a fracture grade; L2 = three consecutive heats where each ball's grade agrees with its performance after fold forging; L3 = one complete puddling–fold-forging–edge-tool-trial loop closed (that tool in the tool record), with this furnace's time-versus-fracture calibration transcribed into the ledger.

#### 19.8.3 The Bootstrap Loop

> Steel chisels and saws → faster quarrying, felling, and woodworking → more ore and charcoal → more iron and steel → better forges, bellows, anvils and hammers → better tools...

Tool wear rates, iron-stock turnover, and carburizing batches are entered monthly in the accounts (the Chapter 38 ledger system); ≥2 spares for every critical edge tool (the Chapter 9 regime).

---

### 19.9 Case-Depth Control Process

The depth–time table of Section 19.3.1 gives expectations for "a normal box"; this section turns it into a regime that is **inspectable and re-verifiable**. Failure of case control is a silent failure — a shallow-cased chisel exposes its iron core after a couple of grinds, and it is only discovered on site — so all the controls are moved up front, into the box and onto the ledger.

#### 19.9.1 Coupon-Gradient Method (acceptance of in-box temperature uniformity)

The 3 coupons per box are not "buried and done" — their positions are fixed and numbered:

| Coupon position | Location | What it represents |
|---|---|---|
| T position | Geometric center of the box | Hottest zone |
| W position | Midway between wall and center | Average-temperature zone |
| C position | Box corner | Dead corner (weakest atmosphere convection) |

The coupons are forged in the same batch as the workpieces and wired with lettered tags (T/W/C); after the box is opened, each is fractured and its case depth measured, then judged per this table:

| Max spread among the three coupons | Verdict | Disposition |
|---|---|---|
| <0.5 mm | Box qualified | Workpiece depth taken as the three-coupon average; box number logged "qualified" |
| 0.5–1.0 mm | Marginal pass | Workpiece depth taken **as the shallowest coupon** (conservative principle); box number logged "skewed" |
| >1.0 mm | Temperature non-uniformity exceeds the limit | This box's workpieces downgraded pending inspection: fracture-sample 1 in every 5; if any sampled piece fails, the whole box goes back in for more carburizing |

**Box qualification regime:** only after 3 consecutive boxes of the same box type show a three-coupon spread <0.5 mm is the type entered on the "qualified box list"; new boxes, repaired boxes, and boxes moved to a different furnace position all re-run the 3-box validation. Gradient localization (for diagnosis): C shallowest and T deepest → corner dead zone — when charging, move the workpieces toward the center and pack 20 mm fireclay blocks between the box and the furnace wall; all three coupons shallow → the furnace temperature is low overall (check the furnace per the Section 19.3.1 temperature criteria) — nothing to do with the box, and using a longer soak to mask a sick furnace is not allowed.

#### 19.9.2 Post-Carburizing Machining Allowance

The carburized case divides into three zones from outside in: scale and decarburized soft shell (0.05–0.15 mm) → high-carbon plateau zone → declining transition zone. **The cutting edge must land in the plateau zone** — an edge quenched with the soft shell still on drops into the transition zone at its first regrind and goes soft. So the forging/grinding allowance of a carburized blank follows this formula:

**Single-face grinding allowance = case depth × 0.3** (empirical. Calibration: measure on the coupon fracture the fraction of the total case depth occupied by the "uniform ring," typically ≈0.7; after one local calibration of the packing, replace the 0.3 coefficient with the measured ratio — i.e., allowance = total depth × (1 − uniform-zone fraction)).

| Use | Target effective case | Carburizing target depth (÷0.7) | Single-face removal | Total single-face blank allowance (incl. forging tolerance ±0.5 mm) |
|---|---|---|---|---|
| Chisel edge | 0.8 mm | 1.1–1.2 mm | 0.3–0.4 mm | 0.8–1.0 mm |
| Axe edge | 1.2 mm | 1.7–1.8 mm | 0.5 mm | 1.0–1.2 mm |
| Punch / drill | 2.0 mm | 2.8–3.0 mm | 0.8 mm | 1.3–1.5 mm |

Acceptance of "ground enough or not" uses the **same-box coupon, same-removal comparison method**: grind the T-position coupon and the workpieces by the same single-face amount, fracture, and check that the remaining ring ≥ the target effective case; then release the whole batch. When coupons run short, sample the pieces near the box corner (C position) at double rate — if the shallowest passes, the deeper ones surely do.

#### 19.9.3 Case-Depth Re-Verification Cycle

- **Per-box acceptance:** 3 coupons per box (the regime tabled above); no companion, no firing (pre-start verification item 7);
- **Batch-drift re-verification:** every 5 boxes on the same recipe, add 1 "ledger coupon" (placed at the W position of a qualified box); if its depth differs from the ledger archive value by >0.5 mm → the packing activity or the furnace condition has drifted; the old depth–time table is suspended and recalibrated;
- **Packing reuse rule:** carburizing packing is reusable; each reuse tops up 30% new charcoal (by volume), mixed evenly; reuse is capped at 3 times; before the 4th charge, the whole depth–time table must be recalibrated with coupons (for reused packing the depth–time relation shifts left as a whole — shallower depth for the same time; empirical value);
- Record fields: box number, the three coupon positions and their depths, recipe batch, reuse count, average depth. **Carburized parts lacking a box number in the ledger are downgraded to "unverified parts"** (the same rule as the Section 19.7 records).

### 19.10 Spring Making (entry level)

**Tier declaration: this section is the second tier** — it delivers low-duty entry-level springs (bow-drill hold-down leaf, box-lock leaf springs, bellows valve flaps, pawl returns), repeatable in manufacture and passing a unified compression test; the stable process for high-duty power springs (energy storage, high-frequency reciprocation) is unsolved and is listed in this chapter's Class-C list — what is missing is compositionally uniform spring steel stock and quantitative temperature control. Entry-level parts may not be passed off as power parts.

#### 19.10.1 Spring Steel Stock Selection (upper part of the high-carbon window)

What a spring needs is not hardness but a **high elastic limit**: no permanent deformation even as loading approaches the limit. Take the stock from the upper part of the high-carbon window of the Section 19.2.1 behavioral grading table (≈0.8%–1.0%) + the blue temper step (the "blue 290–300 °C" row of the Section 19.3.3 color scale already lists springs) — hard but not over-brittle, springy without sagging.

| Route | Stock | Applies to | Limits |
|---|---|---|---|
| Direct | Steel Grade B natural steel batch (Section 19.8.1) | Coil springs, thick leaf springs | Batch composition must be uniform (grading test on ≥3 bars of the same batch with consistent conclusions) |
| Thin-sheet full carburizing | Grade-A iron thin sheet, carburized whole, about 8 h (same route as saw blades) | Leaf springs ≤1.5 mm thick | If the case is shallower than half the sheet thickness the core is soft; large-travel bending cracks the core — thin sheet only |
| **Forbidden** | Carburized blanks for thick coil springs | — | A 1 mm-level case coiled into a φ20 mm ring: the bending strain far exceeds what the case can bear; it will crack |

#### 19.10.2 Coil Springs (mandrel winding, tempered set)

1. **Cutting and annealing:** developed length = π×mean diameter×turns +15% (gripping and end-dressing allowance; empirical value); the blank is fully annealed (the Section 19.7 regime: cherry-red upper limit, 1 h soak, buried in ash for an extremely slow cool) — soft-state winding neither cracks nor leaves large residual stress;
2. **Mandrel:** mandrel diameter = target inner diameter ÷ 0.85 (springback correction; empirical value. Calibration: trial-wind 1 length of annealed scrap, slip it off the mandrel, measure the free inner diameter; springback ratio = free inner diameter ÷ mandrel diameter; replace 0.85 with the measured value);
3. **Winding** (◎technique): insert the blank end into the positioning hole in the mandrel, press it tight against the mandrel and wind 2–3 turns (entry-level turn count); turns not seating against one another = scrambled pitch. Practice: wind 5 lengths of annealed scrap, measure the pitch turn by turn with equal-thickness gauge strips (Chapter 3 feeler gauges); only when the pitch spread is <20% do you touch good stock; misjudgment fallback: replace hand-feel with a count — "the number of hammer taps / wrench turns needed per turn wound on is the same";
4. **Oil quench on the mandrel:** the whole coil, mandrel and all, into the oil (the thin high-carbon oil-quench grade of Section 19.3.2), vertical entry, agitated; **never strip the mandrel before quenching** — quench distortion after stripping ruins the shape outright;
5. **Temper to set (the critical step; skip it and the coil relaxes in service):** temper the whole coil on the mandrel to the blue step (290–300 °C), soak 30 min, cool slowly buried in ash, then strip the mandrel. Winding stress and quench stress are released together in the setting, and the shape is locked by the mandrel; oil-bath setting is more uniform (oil-surface bluish-smoke level ≈250–300 °C, cross-checked against the water-drop crackle anchor), 60 min immersion;
6. Strip-and-check: pitch spread <20%, no surface cracks (wipe and inspect against the light), end faces flat.

#### 19.10.3 Leaf Springs (forged plate + quench-temper + camber set)

1. Forge the plate to target thickness (entry level 1.5–2.0 mm), 0.3 mm single-face grinding allowance; the edges must be filed smooth — **scratches and forge marks are the number-one source of leaf-spring fracture**;
2. Anneal and flatten → scribe and cut to shape → end treatment: drill the fixed end (chamfer the hole edges; holes are crack starters) or hot-forge curl eyes (must be completed before tempering);
3. Oil quench (the thin-part rule) → out of the oil, immediately oil-bath temper at the blue step for 30 min;
4. **Camber set:** after quench-and-temper the elastic springback "opens up" the curve, so when setting the camber **over-bend by 10%–15%** (empirical value. Calibration: make the first spring at +15%, measure the free camber against the target, correct the over-bend coefficient, and transcribe it to the ledger); set the camber hot at 200–250 °C (tempering-temperature level; does not harm the properties); heavy cold setting = brittle-fracture risk, forbidden; after setting, the whole part re-enters the oil bath for 30 min to relieve the setting stress.

#### 19.10.4 Spring Acceptance (three full-stroke compressions method)

Spring failure is a silent failure — you find out only when it collapses inside a machine, so **inspect every spring, no sampling**:

1. Measure the free length L0 (calipers or gauge; read to 0.5 mm);
2. Compress to the full design stroke, hold 10 s, release — do this **3 times**. Compression-test fixture: threaded press screw + pressure plate (made in this chapter); the stroke is fixed by a limit sleeve — setting the stroke by hand-feel is not allowed;
3. Measure L1 after release: **decay = (L0−L1)/L0 <5% passes**;
4. Take 1 more spring per batch and bend-break it: bright fine grain = the stock grade is correct; gray fibrous = insufficient carbon (wrong grade; stop the whole batch and back-trace the grading records);
5. L0/L1/stroke/compression counts go into the record (the same system as the Section 19.7 tool records).

[Card 19-07 Spring Making] (eight fields)

1. **Input materials**: Steel Grade B bar (entry section 2×3 mm or φ3 mm, annealed, same-batch grading on ≥3 bars in agreement); acceptable substitute: Grade-A iron thin sheet, fully carburized (leaf springs ≤1.5 mm thick only; performance cost: breaks first where the case is uneven, shorter life); per-piece stock by developed length = π×mean diameter×turns +15%. **Carburized blanks are forbidden for thick coil springs** (a 1 mm-level case coiled into a φ20 mm ring will crack).
2. **Tools required**: mandrel (forged per Chapter 18; diameter = target inner diameter ÷ 0.85), forge, oil tank, oil-bath tank, compression-test fixture (threaded press screw + pressure plate + stroke limit sleeve), equal-thickness gauge strips (Chapter 3 feeler gauges), calipers or gauge.
3. **Sequence and control points**: anneal (cherry-red upper limit, 1 h soak, buried in ash for an extremely slow cool) → cut → wind on the mandrel (or forge the plate and set the camber) → **oil quench with the mandrel on; never strip it before quenching** → blue-step temper to set, 30 min → cool slowly in ash → strip the mandrel → 100% compression test. **This chapter treats springs only in summary form (Section 19.10); the full procedures are set out in 19.10.2 for coil springs and 19.10.3 for leaf springs, and this card invents no process beyond them.** Control points: the turns must seat tight against one another, and the setting step is never skipped.
4. **Empirical parameters and calibration**: springback correction — mandrel diameter = target inner diameter ÷ 0.85 (trial-wind one annealed scrap length, measure the free inner diameter, replace the coefficient with the measured ratio); blue-step temper 290–300 ℃ for 30 min (oil bath 60 min); leaf-spring over-bend +10%–15% (first article at +15%, measure the error, correct the coefficient and transcribe it); decay (L0−L1)/L0 <5%. **All empirical values, to be calibrated to local conditions.**
5. **Observations to record**: stock batch / annealing time / winding heat color (bright yellow = overheating, stop) / turn count / sound and posture on oil entry / temper-color progression / L0 and L1 readings / fracture grain (bright fine grain or gray fibrous).
6. **Pass / rework / scrap criteria**: pass = decay <5% after three full-stroke compressions + bright fine-grain fracture + pitch spread <20% + no surface cracks; rework = decay 5%–10% (raise half a color step, re-temper to set 30 min, retest); scrap = any crack, pitch spread >20%, decay >10%, or a gray fibrous fracture (wrong stock grade — stop the batch and back-trace the grading records).
7. **Common failures and diagnosis order**: (1) relaxes as soon as it is fitted → setting temperature too low or the step was skipped; (2) breaks in service → check first whether edge scratches and forge marks were filed smooth, then for overheated coarse grain, then the stock grade; (3) weak spring → insufficient carbon (wrong grade) or over-tempered past blue-gray; (4) scrambled pitch → the turns were not pressed tight against one another while winding.
8. **L1 / L2 / L3 evidence**: L1 = one spring through the compression test and on file; L2 = one spring from each of three independent batches through the test with complete records; L3 = the compression fixture finalized and springs in the spares library (≥2 per type) with a continuous decay record.

### 19.11 File Making

The file is a bootstrap-critical part: hardness verification relies on the file test (Section 19.4); the file test needs files; and files themselves must be made from steel and by chisel work — the loop starts from "the first hand-cut file," and once files work well the tooth cutting is mechanized and files come out in batches.

#### 19.11.1 Mechanizing the Tooth Cutting (jump-chisel fixture: guide groove + equal-spacing strike)

Hand tooth cutting relies on eye-estimated pitch; past 20 teeth it always turns to chaos. The jump-chisel fixture replaces "estimating" with "blocking":

- **Guide groove:** cut a locating V-groove in hardwood or a wrought-iron bar (groove width = blank thickness + 0.5 mm); scribe equidistant tooth-position lines along the groove side; the line spacing is the pitch (scribed with templates, Chapter 3 marking gauges);
- **Equal-spacing strike:** the chisel gets a stop block — for each tooth the chisel seats against the block, and after each strike the blank is advanced (or the chisel advanced along its slide) one pitch to the next line; the advance is guaranteed by the stop block's dead point, not by the eye;
- **Equal-force strike** (◎technique): the same person, the same fixed-weight hammer, the same swing arc, every strike. Practice: cut 20 teeth in an annealed scrap bar, measure the tooth depth tooth by tooth with soft-lead impressions; target tooth-depth spread <0.3 mm; practice to standard before touching good stock; misjudgment fallback: replace hand-feel with lead-impression measurement of tooth-depth uniformity.

**Sequence red line: cut the teeth first, quench second** — tooth cutting must be done in the annealed state (on hardened stock the chisel cannot bite and the blank chips at the edges); after cutting, trim the edges and straighten, then oil quench and temper to pale straw (200–220 °C, the most wear-resistant step of Section 19.3.3). Skipped teeth cannot be added after the quench: re-cutting means a full anneal and starting over, so every tooth must be counted and verified before quenching.

#### 19.11.2 Single-Cut / Double-Cut, and Coarse-Medium-Fine: Three Sizes

| Cut | Tooth form | Use |
|---|---|---|
| Single cut | One-direction parallel teeth | Filing soft material: lead, tin, wrought iron, wood, horn; putting the first edge on new files |
| Double cut | Crossing two-direction teeth: undercut first, overcut second, the overcut teeth chiseled between the undercut teeth | Filing steel and hard material: the main working file |

Double-cut angles: undercut 45°, overcut 60° (empirical values. Calibration: trial-chisel a short length of scrap blank at each angle, test-file on soft material and watch whether the chip flow is continuous, and enter the pair that chips most smoothly into the card).

| Size | Pitch | Tooth depth (≈pitch×0.3) | Use |
|---|---|---|---|
| Coarse | 2.0 mm | 0.6 mm | Roughing, heavy stock removal |
| Medium | 1.2 mm | 0.36 mm | Shaping |
| Fine | 0.8 mm | 0.24 mm | Finishing; putting edges on other tools |

A set of three goes into the spares library (the Chapter 9 regime), each with a leather sleeve (wood slats inside to keep the teeth from knocking each other); file faces touching = mutual destruction of tooth tips — a storage Iron Law.

#### 19.11.3 Handle Fitting and Rules of Use

- **Handle fitting:** forge a tapered tang (taper from 1:10 up) and press it into a bored tapered wooden handle; after fitting, three blows on the butt end while suspended, without loosening, passes, plus a pull-off check (tang down, dropped against a soft-padded floor; it must not come off). **Never use a file without a handle** — the tang injures the hand;
- **Break in a new file on soft material first (rule No. 1):** run a new file 10–20 strokes on wrought iron or lead; the burrs from tooth cutting and the micro-chipped teeth get rounded in that first use on soft material; file hard material straight away and the first stroke knocks off the tooth tips;
- Press on the forward stroke and lift on the return (pressing on the return dulls the backs of the teeth); do not file material harder than the file itself (hardened parts skid and dull the teeth — this is exactly the principle of the file test, Section 19.4); every 20 strokes clean the teeth once with a brass-wire brush (brass does not hurt the teeth; iron wire only in emergencies); chips packed into the gullets with filing going on anyway = intermittent chip flow and rising tooth temperature;
- After use, clean the chips, grease, and sleeve (executed the same way as the Section 19.7 regrind procedure).

#### 19.11.4 Tooth Dulling and Refurbishment

Dull-tooth signals: the file skids, chip flow is intermittent, chips pack into the gullets. Quantified criterion: measure the tooth depth with soft-lead impressions; **wear of ≥1/3 of the tooth depth means refurbish** (continuing with dull teeth = slide-press-hardening the blank face, after which it is harder to chisel). Refurbishment route: anneal (the Section 19.7 regime) → re-chisel the overcut (the undercut may stay if still good) → oil quench → pale-straw temper → break in on soft material. **Refurbishment is capped at 2 times:** each refurbishment thins the blank face by 0.3–0.5 mm; below 3 mm blank thickness, scrap to the iron-stock account recovery column.

[Card 19-08 File Tooth Cutting] (eight fields)

1. **Input materials**: Steel Grade B or high-carbon blank (annealed; entry size 200×25×4 mm, thickness ≥4 mm); acceptable substitute: carburized blank (case ≥1 mm so the tooth tips land inside the case; performance cost: one refurbishment grinds through the case and the file is scrapped). **Cut the teeth first, quench second** — on hardened stock the chisel cannot bite and the blank chips at the edges.
2. **Tools required**: jump-chisel fixture (guide groove = blank thickness + 0.5 mm, stop block, pitch scribe template), 3 matched chisels, fixed-weight hammer, annealing pot, soft-lead impression plate, fine file and oilstone, brass-wire brush.
3. **Sequence and control points**: anneal → file the blank faces smooth → scribe the tooth lines → clamp in the groove → chisel the undercut (45°) → chisel the overcut (60°) → **count and verify every tooth** → trim edges and straighten → oil quench → pale-straw temper at 200–220 ℃ → fit the handle → break in on soft material for 10–20 strokes. **This chapter treats file tooth cutting only in summary form (Section 19.11); the full procedures are in 19.11.1–19.11.4, and this card invents no process beyond them.** Control points: the advance comes from the stop block's dead point, not the eye; a skipped tooth cannot be added after the quench (re-cutting means a full anneal and starting over).
4. **Empirical parameters and calibration**: pitch coarse 2.0 / medium 1.2 / fine 0.8 mm; tooth depth ≈ pitch×0.3 (0.6 / 0.36 / 0.24 mm); double-cut angles undercut 45°, overcut 60° (trial-chisel a short scrap length at each angle and enter the pair that chips most smoothly on soft material); temper pale straw 200–220 ℃; strike force accepted by "tooth-depth spread <0.3 mm" measured tooth by tooth with lead impressions; refurbish at ≥1/3 tooth-depth wear, capped at 2 refurbishments. **All empirical values, to be calibrated to local conditions.**
5. **Observations to record**: blank batch / annealing time / pitch line alignment / strike sound (a dull note at the same tooth position = a double strike, logged for inspection) / burr form at the tooth mouths / lead-impression tooth depths / oil-entry posture and hiss / temper color / break-in record.
6. **Pass / rework / scrap criteria**: pass = pitch spread <0.2 mm + tooth-depth spread <0.3 mm + continuous chip flow over 20 strokes on soft material + handle still tight after three blows on the butt; rework = locally skipped or shallow teeth (re-chisel in the annealed state before quenching); scrap = chiseled through the blank face, any crack, tooth tips chipping in patches after the quench.
7. **Common failures and diagnosis order**: (1) pitch drifting progressively → loose stop block or misread lines (stop, realign, verify the teeth already cut); (2) tooth depth getting shallower → strike force decaying (change operator or rest, then continue); (3) chipping after the quench → under-tempering or burrs left on the cut teeth (check the temper-color and break-in records); (4) skidding within a few dozen strokes → the decarburized shell was not ground off before break-in, or the temper went too far.
8. **L1 / L2 / L3 evidence**: L1 = one file passing 20 test strokes on soft material; L2 = one file of each of the three sizes + break-in records + lead-impression depth records; L3 = the file-test gauge of Section 19.4 switched to a self-made file, with the refurbishment ledger running continuously.

### 19.12 Tool-Steel Judgment Extension Training Card

The grading methods of Sections 19.1–19.2 are executed by people; this section turns "being able to judge" into a regime that can be examined and arbitrated.

#### 19.12.1 Three-Method Comparison Practice Regime: Fracture—Sparks—Scratch

| Method | Destructive | What it judges | Position |
|---|---|---|---|
| Scratch (Process Card 19-01) | None | Hardenability (= carbon grade) | **Primary field judgment**, mandatory every batch |
| Fracture (the Section 19.1 grading table) | Destructive (coupons and scrap lengths only) | Grain and fiber (iron/steel/brittle source) | Intake aid |
| Sparks (Section 19.2.2) | None (grinding dust) | Carbon grade | Upgrade criterion (enabled once that section's grinding-wheel conditions exist) |

**Grading blind-test regime:** each round has two people examining each other, drawing 10 numbered blind samples from the four-color grading library (Section 19.8.1) (covering iron A / steel B / carburized C / brittle-source D, including at least 2 confusable samples: decarburized steel, burnt-borderline stock); the trainee grades by scratch + fracture, and the record is opened against the answers afterward; **a cumulative ≥16 correct out of 20 blind tests earns the "stock-grader" qualification** (the same standard as spark qualification in Section 19.2.2). Each misjudged piece gets its cause explained and entered into the record; ≥4 errors across 2 consecutive rounds means standing down for retraining. Once the spark method's grinding-wheel conditions exist, the blind-sample library expands to all three methods tested together — a blind sample may leave the library graded only when all three methods agree; conflicting samples go to arbitration per Section 19.12.2.

#### 19.12.2 Judgment-Dispute Arbitration Procedure (the service test has final say)

When two methods conflict (e.g., a bright fine-grain fracture judging "steel" while the scratch test does not mark it at all, judging "iron" — typical of decarburized-surface stock or underheating misjudgments):

1. **Redo:** first redo the scratch test (the "underheating misjudged as wrought iron" of Card 19-01 is the prime suspect; re-verify the heating by that card's coupon method); then take a supplementary fracture from a different spot (to rule out a local defect misleading);
2. Still conflicting after the redo → **the service test has final say:** forge a 10 mm miniature test chisel from the stock, quench and temper it by the standard chisel process (Process Card 19-03), and drive it into hardwood 100 times — an edge that neither chips nor curls = "Steel Grade B"; a curling edge = "Iron Grade A / mild steel"; a chipping edge = "brittle-source Grade D." **The final definition of a material is "what it can do"**: the entire purpose of grading is choosing the right use, and the service test measures the use directly;
3. Write the final verdict back into the ledger, and charge the method that judged wrong one misjudgment — misjudgment rates go into the grading-library archive (Section 19.8.1); if a method repeatedly misjudges on a class of stock, suspend that method for that class and trust only the others.

Arbitration cost note: the service test costs about 1 day of labor plus one heat treatment amortized, and is used only for disputed pieces; routine grading may not skip the first two methods and jump straight to a service test.

## Parameter Master Table

| Parameter | Value | Category |
|---|---|---|
| Carburizing temperature | 900–1000 °C (standard coupon + box color, double-checked) | Window |
| Carburizing depth–time | 8 h≈0.5–1 / 16 h≈1–1.5 / 24 h≈1.5–2.5 mm | Empirical, grows as √time |
| Carburizing packing | Charcoal 70–80% + bone/leather ash 10–20% + potassium carbonate 5–10% | Empirical starting point |
| Quench temperature | 750–800 °C (cherry red) | Window |
| Interrupted-quench water-cooling time | ≈1 s / 3 mm thickness | Empirical, set by the shudder feel |
| Temper color scale | Pale straw 200–220 ... blue 290–300 °C | Empirical, re-verified by coupon |
| Edge-tool carbon window | Chisel/axe 0.5–0.9% / saw/drill 0.8–1.0% | Design baseline |
| Bend acceptance | Chisel 30°–60° plastic bend without breaking | Criterion |
| Coupon position spread (gradient method) | Three-coupon spread <0.5 mm qualified / >1.0 mm whole box pending | Criterion, Section 19.9.1 |
| Post-carburizing grinding allowance | Case ×0.3 (single face; uniform-zone ratio ≈0.7, locally calibrated) | Empirical, Section 19.9.2 |
| Packing reuse | +30% new charcoal per reuse, capped at 3, full recalibration before the 4th | Regime, Section 19.9.3 |
| Coil-spring mandrel diameter | Target inner diameter ÷ 0.85 (springback correction, calibrated by trial winding) | Empirical, Section 19.10.2 |
| Spring setting temper | Blue step 290–300 °C, 30 min soak (oil bath 60 min) | Window, Section 19.10.2 |
| Spring compression test | Full stroke 3 times, free-length decay <5%, 100% inspection | Criterion, Section 19.10.4 |
| Leaf-spring over-bend | +10%–15% (first-article calibrated correction) | Empirical, Section 19.10.3 |
| File tooth pitch | Coarse 2.0 / medium 1.2 / fine 0.8 mm, tooth depth ≈ pitch×0.3 | Empirical starting point, Section 19.11.2 |
| File tempering | Pale straw 200–220 °C | Window, Section 19.11.1 |
| Stock-grader qualification line | ≥16 correct out of 20 cumulative blind tests | Criterion, Section 19.12.1 |

## Failure Modes and Diagnosis

| Symptom | Candidate causes (by likelihood) | Verification | Disposition |
|---|---|---|---|
| Self-cracking hours after quenching (longitudinal) | High carbon + full-length water quench; no timely temper after quenching | Compare the crack pattern against Section 19.6.1 | Scrap; next batch switch to interrupted/oil quench and temper immediately out of the bath |
| Transverse crack at the edge root | Section change not filleted; an abrupt-section part water-quenched | Check the drawings and the medium grading table | Scrap; redesign with fillets + oil quench |
| Surface crazing days later | Decarburized-layer stress; over-grinding | Pickle and inspect the crazing distribution | Scrap; prevent decarburization in the next batch |
| Uneven hardness (soft spots) | Still water not agitated; oil on the surface entering the bath | File test section by section | Requench |
| Not hard anywhere | Insufficient heating (critical point not reached); wrong quench-medium grade; carburizing failed | Check the coupon fracture for a case ring | Re-carburize / requench; fix the furnace-temperature criteria |
| Hard but chips at a touch | Under-tempering | Raise a color step and re-temper one piece as a trial | Re-temper the whole batch |
| Saw blade warped | Thin part water-quenched | Check the medium grading | Scrap or hot-straighten; oil quench in the next batch |
| File test skids but it chips in use | Surface and core both hard (over-through-hardened) | Fracture: measure the hardened-case depth | Raise the temper step |
| Case depth below spec | Leaking seal / low temperature / short time | Coupon fracture + the pinhole smoke record | Return the box for more time; fix the seal |
| Spring free-length decay >5% | Setting temper insufficient; stock low in carbon (wrong grade); wrong over-bend coefficient | Compression-test L0/L1 comparison + bend-break fracture grain | Raise half a color step, re-temper to set, retest; gray fibrous fracture = stop the whole batch; recalibrate the over-bend coefficient (Section 19.10.4) |
| File teeth dulling early (skids after a few dozen strokes) | Decarburized shell not ground off before break-in; over-tempering; filed hard material before break-in | Soft-lead impression tooth depth + check the temper-color and break-in records | Grind off the surface layer and re-break in; if dulled in patches, refurbish and re-chisel the whole file (Section 19.11.4); retrain on the rules |
| Case ground through (soft spots exposing the iron core after grinding) | Grinding allowance insufficient (< case ×0.3); depth taken as the three-coupon average instead of the shallowest coupon | File-test the soft spot + re-measure with a same-box coupon at the same removal | Mild: return the box for more carburizing; severe: scrap; put the allowance formula and the "shallowest-coupon principle" into the card (Section 19.9.2) |

## Process Card Index

All eight, 19-01 to 19-08, are full eight-field cards, each copyable onto a single page.

## Acceptance Standards

- **L1**: one carburizing run (case ring measured on a coupon); one hardening quench (markedly harder by scratch); one temper (color step reached, toughness restored).
- **L2**: 2 consecutive carburizing batches with depth deviation <0.5 mm; 2 chisels and 1 saw made, all passing functional tests; at least 1 instance of each Section 19.6 defect identified and handled (on record); the three live tests documented.
- **L3**: the four-color grading library + sample library in operation; the regrind–requench ledger running ≥1 month; ≥2 batches of quench media and packing in reserve; 2 or more people passing the independent full-process examination; ≥2 spares per critical edge tool. Evidence: ledgers, examination records, inventory accounts.

## Labor, Personnel, and Consumption

| Item | Personnel | Work-hours (empirical values) |
|---|---|---|
| Grading test, one batch | 1 person | 0.5 day |
| One carburizing box (incl. firing the furnace) | 2 people rotating | 16 h soak + 0.5 day loading/unloading (furnace firing counted separately, coordinated with the Chapter 18 furnace campaign) |
| One steel chisel (incl. carburizing amortization, quench, temper, grind) | 1 skilled worker | 1–1.5 days |
| One frame saw | 1 person | 2 days |
| One coil spring (incl. amortized annealing and setting furnace time) | 1 person | 0.5 day |
| One leaf spring (incl. camber set and compression test) | 1 person | 0.5 day |
| One file (incl. jump-chisel fixture amortization and refurbishment reserve) | 1 person | 1 day |
| One blind-test round (10 pieces, two examiners) | 2 people | 0.5 day |
| One puddling trial heat | 3 people | half a day (plus one day preparing stock) |
| Consumption | Per quenching day: charcoal 10–20 kg, oil 0.5–1 kg, water 30 L | Entered in the Chapter 38 ledger |

## Safety Boundaries

- **Quench-oil-tank fire**: the oil tank must have a lid (a cover plate extinguishes the fire); stop quenching when the oil smokes thickly; ≥3 m from open flame; keep a bucket of dry sand on hand; **water on an oil fire is forbidden**.
- **Quench-crack shrapnel**: observe from the side before handling parts by hand out of the bath; set dull-sounding parts aside alone; **hammer-testing brittle parts is forbidden**.
- **CO**: the ventilation and ≤30 min shift rules for long soaks at the furnace apply in full (Iron Law 7).
- Brine and hot-oil splashes: keep the liquid surface turned away from the face; long-handle tongs; leather apron and gloves complete.
- Grinding dust and forging sparks: dip the edge in water while grinding; no standing within 2 m of the anvil; call out before swinging the hammer.
- Carburizing packing contains bone and leather ash: mix wet to prevent inhalation; potassium carbonate is strongly alkaline — wash hands after handling (Chapter 8 rules).
- Burn procedure: cold-water rinse ≥15 min; tempered parts and hot-ash beds are always handled with tongs.

## A. Existing Tools List

Chapter 18 graded iron stock, anvil and hammers, forge, furnace-number records; Chapter 17 carrying regime, leather protection; Chapter 12 high-temperature furnace (capable of soaking), bellows, standard coupons; Chapter 11 pottery; Chapter 9 grinding bench, templates, angle plate, rope-lash clamps; Chapters 8 and 3 lye, testing and version regimes; Chapters 10 and 15 oils and fats, leather goods.

## B. New Tools List (this chapter)

Carburizing box and packing recipe; three quench tubs (water / brine / covered oil); tempering hot-ash bed and oil-bath tank; hardness reference set and file-test gauge; test-coupon library regime and the T/W/C gradient ledger; steel chisel, steel saw (frame saw), axe edge, knife, forge-welded composite edge; the four-color grading library and the heat-treatment ledger; the puddling conditional route (shallow flat furnace); coil-spring mandrel and spring compression-test fixture, a batch of entry-level springs; the jump-chisel fixture (guide groove + stop block) and one set of coarse-medium-fine files; stock-grading blind-test tags and the arbitration archive.

## C. Unsolved Dependencies

Chemical quantification of carbon content (Chapters 23, 26); the speed-up grinding wheel needed for the spark carbon test (Chapters 20, 21; the full table is ready); thermometer (Chapter 25; the tempering oil bath will be upgraded to quantitative); alloy-steel ore sources (manganese, chromium unsurveyed); spring steel and deep-hardening parts (forced through by Chapters 21, 28); protective atmosphere against decarburization (long-term furnace upgrade).

## Next-Step Dependencies

Chapter 20: steel chisels, scraping tools, and scribing needles are direct tools for machine-tool building; iron–steel structural stock supplies bed-guideway blanks. Chapter 21: the gear-shaft spring blank system; the water-powered forging hammer lifts the manpower ceiling on forging. Chapter 22: dimensional stability of measuring-tool steel (this chapter's annealing regime is the start). Chapter 23: backfill of carbon-content analysis, pickling descaling, rust-proof coatings. Chapters 25, 27: thermometers and hardness testers upgrade the auxiliary criteria to quantitative. From Chapter 28 on: pressure-vessel-grade steel depends on a long chain of later upgrades.
