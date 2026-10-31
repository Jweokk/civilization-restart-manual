# Chapter 38 Material and Energy Ledgers

## Chapter Objectives

On completing this chapter, the settlement should establish and maintain four ledgers, one summary table, and one wall board:

| Deliverable | Content | Question it answers |
|---|---|---|
| Materials ledger (Card 38-01) | Four-column daily flow: receipts / consumption / stock / in-transit | How many more smelts will the material last? |
| Unit-consumption summary table (38.2.1) | Per-product main material, fuel, transport, wear-and-tear unit costs | What must be stocked for the next smelt? |
| Energy master ledger (Card 38-02) | All fuels converted to firewood-equivalents; human and animal power listed separately | Can the woodland sustain this? |
| Wear-and-spare-parts ledger (38.5) | Consumable life, amortization, reorder points | What will fail within six months? |
| Three-color warning board (38.6.3) | Months of reserve for key materials, updated monthly | Cut production now, or expand? |

## Capability Boundaries

**Can do:**

- After 3 full months of per-smelt records, calculate main-product unit consumption to ±20–30% and identify which factor drove the change.
- Use three-color lines to flag supply-cutoff risk 1–2 months ahead; use unit-consumption trends to catch process drift and ore-grade decline early.
- Convert fuel, transport, and wear into one unit (firewood-equivalent and person-days) to compute the "full cost per ton of main product," testing any new-furnace decision.

**Cannot do:**

- Predict when an ore vein will run out. Grade can only be monitored month by month; the inflection point is unpredictable.
- Replace the improvement duties of the process chapters. This chapter only keeps accounts, never cuts consumption; to reduce unit costs, go back to the relevant chapter and change the process.
- Smooth out fluctuations. Wet-wood seasons, new kilns, and ore-source changes swing unit costs ±20–30%; record them as they are — averaging for appearance is forbidden.
- Produce data from nothing. Without per-smelt weigh-ins, the ledger is an empty form; recording without weighing is recording imagination.

**External dependencies (entered in the C list):**

1. Chapter 37 per-capita annual baselines (ration grain, household fuelwood) — the base of the household account.
2. Measured unit consumption from every furnace and kiln (Chapters 6, 11–14, 16–19, 28; from each chapter's L3 acceptance ledgers); uncalibrated items may only use this chapter's ranges.
3. Settlement-wide unified weights and measures (Chapters 3, 22) and the ledger-archival institution.

## Pre-Start Verification

Checklist form. Any item unmet demotes the corresponding account to "provisional," not usable for furnace-start or production-planning decisions.

| # | Verification item | Criterion (confirm you have ××, standard is ××) |
|---|---|---|
| 1 | Weights and measures | One scale and one volume measure each; bookkeeper and workshops cross-check on site: mass error ≤2%, volume ≤5%; fix before recording |
| 2 | Per-capita baselines | Chapter 37 grain and fuelwood medians calibrated and copied into the ledger; uncalibrated items marked "provisional" throughout |
| 3 | Furnace/kiln register | Every active furnace registered with five items: name, source chapter, monthly output, unit-cost status (measured / uncalibrated), staffing establishment |
| 4 | Bookkeeping office | ≥1 person at Level 2 (passed the Chapter 37 bookkeeper assessment: cross-checking, recording, monthly stocktake — all evidenced) |
| 5 | Ledger books | Printed from Card 38-01, one set per workshop; requisition-stub numbers continuous, no gaps |
| 6 | Warehouses | Two-person two-lock system in place (37.6.1); fuel, ore, finished goods, and consumables stored in four separate zones, each with a stock placard |
| 7 | Production plan | Next 3 months' furnace schedule and output targets in writing; the bookkeeper computes the "monthly consumption baseline" from them |
| 8 | Opening stocktake | All stock weighed or counted, error ≤10%, recorded as the opening account; every later entry measured from this origin |

## 38.1 Why the Ledger Decides Survival

### 38.1.1 The Death Chain of Product-Only Accounting

Project a settlement that records products but never consumption, over 5–10 years (each step an empirical value; the generic shape of a historical failure mode):

| Stage | Books (products only) | What actually happens off-book | True system state |
|---|---|---|---|
| Year 1 | 300 kg iron produced; only "output" and "grain trades" recorded | Firewood cut and charred within 1 km; wood treated as free, never entered | Healthy |
| Years 2–3 | Output raised to 1 t/yr; books look better | Cutting radius expands to 3–5 km; wood-hauling hours already 20–30% of total fuel-acquisition labor (37.6.4 yellow line) | Hidden overdraft |
| Years 4–5 | Output barely maintained | Radius 8–10 km; acquisition hours per kg of charcoal exceed forging hours per kg of iron; furnaces forced to intermittent operation | Inverted returns |
| Years 6–8 | Iron-for-grain exchange rate worsens quarter by quarter | Forest line retreats to the watershed; erosion hits fields (37.6.4 chain); farthest kiln abandoned, smiths drift back to farming | Eve of supply cutoff |
| Years 8–10 | Bookkeeping ends with the workshop | Metallurgical supply cut off; timber and stone repairs substitute for iron; technology drops two tiers (cf. 37.3.2) | Collapse |

Reading point: every link looked "normal" in its own year. The fuel forest isn't eaten in a year — it's eaten one extra li of walking per day over three years, and only the ledger can see that extra li. The two signals that should have raised the alarm in Years 2–3 (hauling-hours share, acquisition hours per kg of charcoal) are buried precisely where nothing is recorded.

**Interception points of the various ledgers on this same chain:**

| Stage | Ledger signal readable at that stage | Intercepting action |
|---|---|---|
| Year 1 | Opening stocktake has no "firewood" page — fuel was never entered | Open Card 38-01; start wood and charcoal pages immediately |
| Years 2–3 | Transport master ledger: wood-hauling person-days rise to 20–30% | Cap the cutting radius; plan fuelwood rotation (37.2.2) |
| Years 4–5 | Energy master ledger: acquisition hours per kg charcoal > forging hours per kg iron | Freeze expansion; fuel-saving furnace retrofits back in the relevant chapter |
| Years 6–8 | Monthly energy ledger over woodland budget >20% for consecutive months | Recompute N₂; seal furnaces and cut output per 37.6.4 |

All four interception points fall two to six years before "iron-for-grain deterioration." **The earlier the ledger opens its pages, the more reversible the collapse.**

### 38.1.2 The Ledger's Three Questions

Materials bookkeeping has one discipline: **every product entry must simultaneously answer three questions.**

| Question | Corresponding ledger | Line item | Unit |
|---|---|---|---|
| What was **burned** for it | Energy ledger (38.3) | Wood, charcoal, lamp oil, as firewood-equivalent | kg firewood-equiv. |
| What was **hauled** for it | Transport ledger (38.4) | Movement of ore, charcoal, wood, products | t·km and person-days |
| What tool **wore out** for it | Wear ledger (38.5) | Amortization of crucibles, furnace lining, files, bellows leather | piece-uses and hours |

Plus the first question, "how much main material did it use" (materials ledger, 38.2). Four questions together = the four ledgers of 38.2–38.5.

**Three-question worked example (a 1.5 kg iron hoe, mid-range values from this chapter):**

| Question | Reading | Source |
|---|---|---|
| Main material used | Iron ore 30 kg; iron-material consumption already inside the 25–40% yield factor | 38.2.1 |
| What was burned | Charcoal 27 kg ≈ 110–160 firewood-equiv. (production basis) | 38.2.1, 38.3.2 |
| What was hauled | Ore 30 kg × 5 km + charcoal 27 kg × 3 km ≈ 0.2–0.5 person-days | 38.4.2 |
| What wore out | Furnace-lining and forging-tool amortization 0.02–0.05 person-hours + refractory clay 0.1–0.7 kg | 38.5.2 |

Reading: the full cost of a new hoe ≈ 0.5–1.2 person-days (smelting labor computed separately in 38.3.4); regrinding an old hoe costs only 0.05–0.15 person-days. **The book-keeping case for maintenance before replacement sits in that one line** — the same entry goes into the wear ledger (38.5) and the maintenance plan (see Next Dependencies); it counts only when the two agree.

The ledger's second identity: **a diagnostic instrument.** Month-over-month unit-cost rise is the earliest signal of process drift or ore-grade decline — earlier and cheaper than fracture inspection or the scrap pile (38.6.2, third check). Using the ledger only as a record spends half its value.

### 38.1.3 The Ledger's Place in the Acceptance System

| System requirement (source) | Which card here delivers it | Consequence if missing |
|---|---|---|
| Iron Law 6: acceptance must store evidence into ledgers (Ch. 1) | Card 38-01 daily flow + Card 38-03 monthly stocktake | Passes without proof; the reader repeats the same failed smelt and blames luck |
| L3's "material reserves and resupply routes" element (Ch. 1 §5) | Card 38-01 in-transit column and reorder points | Every chapter's L3 "materials" line idles; single-piece success never becomes a system |
| Sustainable fuel-consumption rate (Ch. 1 §5) | Card 38-02 conversion table and monthly energy ledger | N₂ (37.2.2) overloaded unnoticed until the forest line visibly retreats |
| Change control dual signatures and verification records (37.6.3) | Card 38-01 summary column + monthly unit-cost trend | Process drift untraceable; bad batches have no identifiable starting change |
| Resource red-line patrol (37.6.4) | Readings of the 38.4.2 transport master ledger | Red lines have no data to read — decoration |

## 38.2 Materials Ledger

### 38.2.1 Unit-Consumption Summary Table

This table collects empirical values from earlier chapters; **all are empirical values requiring field calibration**; before calibration they may serve magnitude judgment only, never production scheduling (same rule as Chapter 37). Each row's calibration method is directly executable.

| Product (unit) | Main-material unit cost | Fuel unit cost | Consumables amortization | Source chapter | Field calibration method |
|---|---|---|---|---|---|
| Dense iron (kg) | Iron ore 20–40 kg | Charcoal 20–35 kg | Furnace-lining clay 70–500 g; forging losses inside the yield factor | Ch. 18 | Calibrate in two stages: ① in-furnace fuel ratio — record charged charcoal, ore, and bloom per smelt (4–8:1 by bloom weight, 37.1.2); ② yield — bloom weight ÷ ingot weight (25–40%); full-chain unit cost = the quotient, cross-checked against the 20–35 range; if outside, check grade or furnace condition |
| Pottery (kg) | Clay 1.1–1.3 kg (incl. drying shrinkage and waster loss) | Wood 0.2–1.2 kg/kg pottery (0.3–0.8 t per firing, charge 0.5–2 t) | Saggar and kiln supports, amortized over 5–20 firings | Ch. 11–12 | Weigh the whole kiln's wood charge + weigh each piece loaded; median of 3 firings |
| Brick and tile (kg) | Clay 1.1–1.3 kg | Wood 0.15–0.5 kg/kg (separate kilns, separate accounts from pottery) | Kiln lining amortized 1–3 years | Ch. 11–13 | Same; brick/tile and pottery kept in separate accounts — merging forbidden |
| Lime (kg) | Stone 1.7–2.2 kg (loss on ignition 40–45%) | Wood 0.3–0.5 kg/kg | Kiln lining amortized 1–3 years | Ch. 13 | Weigh-in/weigh-out over 3 continuous firings; loss-on-ignition = 1 − ash weight/stone weight; replace 1.7–2.2 with measured values |
| Glass (kg) | Sand 0.55–0.7 kg; soda or plant ash 0.2–0.4 kg | Firewood-equiv. 4–10 kg/kg | Crucible amortized over 10–30 melts | Ch. 14 | Record charge batch and output weight per melt; fuel allocated per firing by total weigh-in |
| Copper (kg) | Copper ore 20–60 kg (grade 2–5%) | Charcoal 10–30 kg | Crucible amortized over 5–15 melts | Ch. 17 | Record ore and charcoal charged and copper output per smelt; grade sampled per batch per Ch. 16 |
| Roasted ore (kg) | Iron ore 1.0–1.1 kg (roasting drives off water and sulfur) | Wood 0.05–0.15 kg/kg | Roasting-basket and rake wear | Ch. 16 | Weigh-in/weigh-out over 3 continuous batches |
| Steam-engine work (kWh) | Boiler feedwater 20–80 kg (large spread with/without condensing) | Firewood-equiv. 6–10 kg/kWh | Firebox refractory accounted separately per Ch. 28 | Ch. 28 | Log running hours and wood consumption daily; convert to output |
| Paper (sheets or reams) | (reserved column) | (reserved column) | (reserved column) | (reserved; to be added) | (reserved column) |

Three table-reading rules: ① for workshops with multiple furnaces/kilns, keep unit costs per furnace per kiln as separate rows — workshop-wide averages mask differences, and the hungriest furnace is the one the account must catch; ② production planning and reserves use the upper bound of the range; efficiency testing uses the lower bound — write the two uses separately; ③ the replacement moment is "the day 3 continuous furnace measurements are complete"; replacement goes through 37.6.3 dual signatures.

**Settlement materials opening-page list (minimum pages at account opening):**

| Category | Materials requiring pages | Pages (reference) |
|---|---|---|
| Household | Grain, salt, household firewood, lamp oil | 4 |
| Fuel | Dry wood, green wood (separate pages), charcoal | 3 |
| Ores | Iron ore, copper ore, roasted ore, limestone | 3–4 |
| Auxiliaries | Refractory clay, sand, soda or plant ash | 3 |
| Products | Iron ingots, pottery, brick, lime, glassware | per active product |
| Consumables | Crucibles, files, saggars, rope | 4 |
| External purchases & relics | Salt (if bought), relic metals and medicines | 2 |

Criterion: any material a furnace needs to start must have a page first — **no page, no furnace start**; record opening quantities the day pages are opened. Open pages top-down: the household account first — bookkeeping on an empty stomach doesn't work.

◎ Estimating charcoal-pile and wood-stack weight (visual volume → kg) is a hand-feel step. Practice: compare against 5 pre-weighed charcoal piles, 20 trials. Misjudgment compensation: weigh a 10% random sample of piles; if error >15%, switch that month entirely to scale weighing.

### 38.2.2 The Unit-Cost Formula: Where the Ranges Come From

Unit cost is not a memorized number — it is the reciprocal product of stage factors:

> **Ore consumption = 1 ÷ (grade × beneficiation recovery × smelting recovery × yield factor)**

Worked example: grade 0.20 × beneficiation recovery 0.75 × yield 0.32 → ore consumption = 1 ÷ 0.048 ≈ 20.8 kg/kg, at the low end of the 20–40 range. Two uses: first, when unit costs worsen, check factors in order — grade from Ch. 16 batch sampling records, recoveries and yield from this chapter's per-smelt ledger; whoever changed, fix that. Second, before switching ore sources, pre-compute unit cost with the new grade and decide.

### 38.2.3 The Four-Column Ledger Format

One page per material, daily flow, four fixed columns:

| Date | Summary (workshop / furnace no. / batch) | Receipts (kg/L/pieces) | Consumption (kg/L/pieces) | Stock | In transit | Dual signatures |
|---|---|---|---|---|---|---|
| (ex.) Mar 2 | Charcoal kiln No. 3 output | Charcoal +420 | — | 640 | — | A / B |
| (ex.) Mar 4 | Smelter No. 1, 7th smelt, draws stock | — | Ore −260, charcoal −180 | 460 | — | C / A |

Hard bookkeeping rules:

| # | Rule | Criterion |
|---|---|---|
| 1 | Stock = yesterday's stock + receipts − consumption | In-transit **never enters stock**; a negative stock column is a recording error — same-day investigation |
| 2 | Units only kg, L, pieces | "One shoulder-load, one cart, one pile" forbidden; convert before entry |
| 3 | Dual signature per entry | Handler and custodian each sign one cell; single-signed pages are invalid |
| 4 | Requisition stub numbers continuous | Gaps reported to the bookkeeper same day; replacements marked "replacement"; no alterations — errors crossed out and re-signed |
| 5 | All receipts weighed or counted | Estimated entries treated as scrapped (Card 38-01 field 6) |
| 6 | Month-end reconciliation with physical stock | Process and shortage three-check per 38.6 |

Three-way reconciliation (ledger↔ledger, ledger↔goods, ledger↔voucher):

| Comparison | Frequency | Tolerance | Over-tolerance action |
|---|---|---|---|
| Workshop sub-ledger ↔ bookkeeper master | Every 10 days | 0 (only transcription errors allowed) | Reconcile same day; hunt gaps and omissions |
| Ledger stock ↔ physical stock | Monthly (Card 38-03) | ≤5% | Three checks (38.6.2) |
| This chapter's unit costs ↔ chapter acceptance ledgers | Quarterly | ±20% | Any deviation: check definitions and batches — never let both sides adjust independently |

In-transit column definition: quantities ordered or shipped but **not yet received into stock**. Criterion: the three-color warning (38.6.3) reads only the stock column; in-transit is for scheduling receiving labor only — never treated as available for furnace starts.

**Full-month example (charcoal page; figures illustrative):**

| Date | Summary (workshop / furnace / batch) | Receipts | Consumption | Stock | In transit | Dual signatures |
|---|---|---|---|---|---|---|
| Mar 1 | Opening carry-forward | — | — | 950 | — | A / B |
| Mar 4 | Kiln No. 3 output | +420 | — | 1370 | — | A / B |
| Mar 6 | Smelter No. 1, 7th smelt draws | — | −180 | 1190 | — | C / A |
| Mar 9 | Forge draws charcoal | — | −60 | 1130 | — | D / A |
| Mar 12 | Kiln No. 3 ignited (in transit) | — | — | 1130 | +400 | A / B |
| Mar 15 | Smelter No. 1, 8th smelt draws | — | −180 | 950 | 400 | C / A |
| Mar 22 | Kiln No. 3 output received into stock | +400 | — | 1350 | 0 | A / B |
| Mar 26 | Forge and glass shop draw | — | −270 | 1080 | 0 | D / B |
| Mar 31 | Month-end carry (receipts +820, consumption −690) | — | — | 1080 | 0 | stocktake dual signature |

Mid-month reading (example): by the 15th, 420 kg consumed; month-end projection 840 kg vs. the 750 kg monthly plan — 12% over. No color line tripped yet, but per criterion **projected monthly deviation >10% goes into the ten-day report; >20% launches a cause hunt** (38.6.2 third check: change register → ore grade → lining wall thickness). Don't wait for the month-end stocktake to react.

### 38.2.4 The Reorder-Point System

General formula:

> **Reorder point = consumption during replenishment lead time + 2 furnace (kiln/batch) safety reserves**

| Key material | Replenishment lead time (empirical, calibrate) | Lead-time calibration | Reorder-point example |
|---|---|---|---|
| Charcoal | 7–14 days (cut, load, burn, cool) | Time 3 full cycles, take the longest | Daily charcoal use × 14 + 2 kiln charges |
| Refractory clay | 3–10 days (dig, haul; aging adds 7–20 days) | Same | Monthly use ÷ 30 × cycle + 2 relines |
| Crucibles | 20–40 days (form, dry, fire) | Same | Monthly crucible use ÷ 30 × 40 × 1.5 |
| Iron ore | 3–7 days (mine, beneficiate, deliver) | Same | Daily ore use × 7 + 2 furnace charges |
| Soda / plant ash | 10–30 days (collect, sieve, dry-store) | Same | Monthly use ÷ 30 × 30 × 1.5 |

Stop-line criterion (linking to Chapter 18's L3 raw-material reserve clause): **if charcoal, ore, or refractory stock falls below 2 furnace-charges, stop the line and replenish**. "Scrounging while running" is forbidden — a half-smelt that runs dry costs more than no smelt: furnace-temperature collapse, a frozen hearth; restart costs per 37.4.2.

Worked example (illustrative): daily charcoal use 200 kg; measured longest lead time 10 days; one furnace charge = 180 kg → charcoal reorder point = 200 × 10 + 2 × 180 = **2,360 kg**. The day book stock falls below 2,360 kg, the bookkeeper issues a replenishment order to the kiln crew and marks a yellow dot on the ledger header; below 2 × 180 = 360 kg (hard 2-charge line) → stop line and replenish.

### 38.2.5 Volume-to-Weight Conversion Table

Where per-entry weighing is impossible (whole stacks, whole kiln charges), entry by volume-to-weight conversion is allowed using the coefficients below; **re-weigh 10% monthly as a spot check — error >10% reverts that material to full weighing.**

| Material | Bulk density (empirical, calibrate) | Measuring convention |
|---|---|---|
| Loose charcoal pile | 180–250 kg/m³ | measured pile height × base area |
| Loose wood stack | 300–450 kg/m³ (stacked volume) | stack length × width × height |
| Iron ore (loose) | 1.5–2.5 t/m³ | depends on lump size and clay content; re-standard after washing |
| Clay (loose measure) | 1.3–1.6 t/m³ | — |
| Lime (powder, out of kiln) | 0.9–1.2 t/m³ | — |

Calibration: pick 3 typical piles per material, measure volume then weigh the whole pile for a local coefficient; re-standard after any ore-source or kiln change. Converted entries must carry the marker "converted" in the summary column; month-end stocktakes spot-check converted batches first.

[Card 38-01 Materials Ledger Card] (eight fields)

1. **Input materials**: ledger pages (Ch. 4 recording materials: bound book or waxed board), requisition stubs, ink and charcoal pencil, opening-stocktake record (verification item 8).
2. **Required tools**: scale (Ch. 3/22; check zero and full scale against a standard weight before use, >2% error = out of service), volume measures (≤5% error), three-color board (painted plank). No higher-precision instruments needed.
3. **Operating sequence and control points**: ① opening stocktake by weight establishes the account, marked "data origin date"; **② every receipt and issue entered same day, dual-signed, stock balance computed same day**; **③ in-transit listed separately, never in stock**; ④ missing requisition stubs reported same day; ⑤ Card 38-03 stocktake executed every month-end; ⑥ calibrated unit costs copied into the summary table immediately with date.
4. **Empirical parameters and calibration**: unit-cost ranges from table 38.2.1; replaced after per-smelt measurement (four-point weighing: charge, output, bloom, ingot); reorder points computed per material per 38.2.4 and written on each ledger page header.
5. **Process observation and recording items**: the summary column must state "which furnace, which batch"; anomalies (wet wood, fines fraction, returned material) go in remarks; daily stock balance checked against the previous row.
6. **Pass / rework / scrap criteria**: pass = daily closure, monthly closure, stocktake gap ≤5%, continuous vouchers; rework = gap 5–10% resolved within the month, replacement stubs marked, originals retained with strikethrough; scrap = reconstructing entries from memory or entering estimates (page voided, physical stock recounted and rebuilt).
7. **Common failures and troubleshooting order**: books≠goods → check omissions first (missing stubs, unentered returns) → check scales (calibration) → check pilferage (38.6.2); negative stock → check receipt/issue direction reversal → check unit mixing (kg vs. loads, pieces vs. kg); erratic unit costs → check whether the summary column mixes furnaces/batches.
8. **L1 / L2 / L3 evidence**: L1 = one month of original four-column flow records; L2 = 3 months of stocktake records with gap ≤5% + at least one product's measured unit cost; L3 = one genuine three-color trigger with disposition record + books≠goods holds after a change of bookkeeper + all calibrated values copied into the archive.

**Blank ledger page (copy from card):**

| Date | Summary (workshop / furnace / batch) | Receipts | Consumption | Stock | In transit | Dual signatures |
|---|---|---|---|---|---|---|
| | | | | | | |
| | | | | | | |
| | | | | | | |

Ledger binding rules: one page per material, one book per workshop, master ledger at the bookkeeping office; sub-ledgers go to the office every ten days for reconciliation.

## 38.3 Energy Ledger

### 38.3.1 The Firewood-Equivalent: An Accounting Unit, Not a Physical Constant

Definition: **1 firewood-equivalent (FWE) = the heat content of 1 kg of air-dried pine wood (15–25% moisture), roughly 3,500–4,000 kcal (1 kcal ≈ 4.19 kJ; ≈ 14.6–16.7 MJ).**

Field calibration (no calorimeter — use the **comparison method**; stove efficiency cancels out in same-condition tests): same stove, same pot, same damper setting — boil the same quantity of water (suggest 5 kg, from 15 ℃) separately with the test fuel and with reference pine wood; 3 trials each, take the median. **Conversion coefficient = reference-pine consumption ÷ test-fuel consumption.** Example: to boil the same pot, pine costs 0.90 kg, a hardwood costs 0.75 kg → coefficient = 0.90 ÷ 0.75 = 1.2 FWE/kg. Auxiliary method (stove-efficiency estimate): keep boiling after the roll and weigh the evaporated water; heat delivered = evaporated water × 539 kcal/kg; divide by theoretical heat content for efficiency — useful when improving stoves. Local variation ±15% is allowed, but **the whole settlement must use one conversion table**, copied onto the energy ledger's flyleaf with a version date.

Two hard rules:

| # | Rule | Reason |
|---|---|---|
| 1 | Heat-equivalent and production-equivalent are used separately: charcoal yields 1.7–2.1 FWE/kg as fuel, but costs 4–6 kg of wood to make | Heat-equivalent tests the furnace's heat balance; production-equivalent tests woodland pressure — charcoal is not gathered for free |
| 2 | Green wood must be converted: wood at 40–60% moisture enters the books at 0.5–0.7 FWE/kg | Unconverted, the books inflate 30–50% and the fuel ceiling N₂ (37.2.2) is overstated |

◎ Judging wood dryness (heft and knock: dry wood rings crisp, green wood thuds) is a hand-feel step. Practice: 20 trials on batches of known moisture. Misjudgment compensation: weigh 3 sticks, oven-dry at the stove for 24 h, weigh again — the loss is the moisture content; any batch with >10% error is booked as green wood.

### 38.3.2 Energy Conversion Table

All empirical values requiring field calibration; the calibration method is uniform: weigh-in/weigh-out for fuels, daily records for humans and animals.

| Energy source | Unit | Heat (kcal) | Heat FWE | Production/keeping cost | Use boundary |
|---|---|---|---|---|---|
| Pine wood (air-dry) | kg | 3,500–4,000 | 1.0 | Felling, splitting, drying 0.7–1.5 person-hr/10 kg | Reference unit; all furnaces and cooking |
| Hardwood | kg | 4,000–4,500 | 1.1–1.2 | Same; splitting +30–50% labor | All furnaces |
| Green wood (40–60% moisture) | kg | 1,800–2,600 | 0.5–0.7 | 2–6 months drying | Must convert on entry; direct use in smelting furnaces forbidden (Ch. 18) |
| Charcoal | kg | 6,800–7,500 | 1.7–2.1 | Production costs 4–6 kg wood (Ch. 6) | Metallurgy, glass, forging only; must not be diverted to household use when short |
| Straw and leaves | kg | 3,000–3,500 | 0.8–0.9 | Farm by-product | Cooking and drying; bulky — never mixed into kiln-fuel accounting |
| Peat (if sourced) | kg | 3,000–4,000 | 0.9–1.1 | Digging + 1–3 months drying | Sulfur-bearing; use cautiously in metallurgy |
| Lamp oil (plant oil, fat) | kg | 8,500–9,500 | 2.2–2.5 | Pressing 0.2–0.4 person-days/kg | Lighting only; burning in furnaces forbidden |
| Pine resin, pitch (if any) | kg | 8,000–9,000 | 2.2–2.5 | Collection 0.1–0.2 person-days/kg | Kindling, waterproofing, preservation only; no bulk furnace use |
| Human labor | person-day | Effective mechanical work 0.15–0.3 kWh (130–260 kcal) | **not converted** | Ration 1–1.5 kg grain; +20–30% for heavy work (37.1.1) | Mechanical work and heat are not interchangeable, see below |
| Animal power | head-day | Effective mechanical work 2–3 kWh | **not converted** | Hay 8–12 kg/head-day (37.1.3) | Separate line in the transport ledger (38.4) |

Why human and animal power are not converted into FWE: one person-day of effective mechanical work equals only 0.04–0.07 FWE of heat — but the reverse fails: burning 100 kg of wood produces no 1-person-day of hauling. Before the steam engine (Ch. 28), mechanical work has only four sources: humans, animals, water, wind. **Mechanical work and heat are two separate budgets**; mixing them simultaneously overstates fuel and understates human labor (Ch. 37: person-hours are the balancing variable).

### 38.3.3 The Monthly Energy Master Ledger

Convert the whole settlement's monthly fuel movements into firewood-equivalents and compare with the woodland budget of 37.2.2. Table form (illustrative figures):

| Line item | Physical quantity | Conversion factor | Firewood-equiv. (kg) | Notes |
|---|---|---|---|---|
| Pine wood (air-dry) into store | 12 t | 1.0 | 12,000 | Felling crew weighed in |
| Green wood into store (~50% moisture) | 3 t | 0.6 | 1,800 | Converted after measured moisture |
| Charcoal into store | 2.5 t | 5.0 (production equiv.) | 12,500 | Woodland-pressure basis |
| Lamp oil drawn | 40 kg | 2.3 | 92 | Lighting only |
| **Total monthly outlay** | — | — | **26,392** | = 26.4 t |

Reading: against the 750 t annual available wood of the 37.2.5 example settlement (monthly average 62.5 t), this month used 42% — within budget; but charcoal alone is 47% of the 26.4 t — woodland pressure is driven by metallurgy, cross-checking the 38.3.4 computation. **The two bases must never share a column**: this table uses production-equivalent for woodland pressure; for in-furnace heat balance, charcoal switches to heat-equivalent (2.5 t × 1.9 = 4,750 FWE) in a separate column. Hard criterion: **monthly energy ledger over woodland budget >20% for two consecutive months → mandatory recompute of N₂ (37.2.2).**

### 38.3.4 Worked Example: The Full Energy Cost of One Ton of Iron

Teaching computation; figures are mid-range assumptions to be replaced by local ledgers. Assumptions: ore grade 20%, beneficiation recovery 0.75, in-furnace fuel ratio 6:1 (by bloom weight), yield 0.32, ore carted 5 km by wheelbarrow, charcoal kiln on site (wood not hauled), charcoal hauled 3 km.

Physical quantities first: bloom = 1,000 ÷ 0.32 ≈ 3.1 t; ore consumption = 1 ÷ (0.20 × 0.75 × 0.32) ≈ 20.8 t; charcoal = 3.1 t × 6 = 18.8 t (in-furnace) + 15% screening loss 2.8 t + forging heating 1.4 t = **23 t**; wood = 23 t × 5 kg-wood/kg-charcoal = **115 t**.

| Stage | Physical quantity | Firewood-equiv. (t) | Person-days (range) | Basis and calibration |
|---|---|---|---|---|
| ① Mining | Ore 20.8 t | — | 21–42 | Hand-pick mining 0.5–1 t/person-day (Ch. 16; calibrate: 3 days of real production) |
| ② Crushing and beneficiation | Ore 20.8 t | — | 7–21 | Crush and sort 1–3 t/person-day |
| ③ Woodcutting | Wood 115 t | 115 | 77–164 | 0.7–1.5 t/person-day incl. splitting, drying, stacking (calibrate: 5 person-days of real output) |
| ④ Charcoal burning | Charcoal 23 t | counted in ③ | 29–77 | 0.3–0.8 t charcoal/person-day (Ch. 6 kiln records) |
| ⑤ Ore haul 5 km | 10.4 t·10 km | — | 69–130 | Wheelbarrow 80–150 kg/person-day·10 km (38.4.1) |
| ⑥ Charcoal haul 3 km | 6.9 t·10 km | — | 46–86 | Same |
| ⑦ Furnace floor | Bloom 3.1 t | charcoal counted | 43–109 | 0.2–0.5 t/furnace-day × 7-person crew (37.4.2) |
| ⑧ Forging densification | Ingots 1 t | charcoal counted | 20–50 | 20–50 kg/person-day (Ch. 19) |
| ⑨ Lining relining amortized | 1/10–1/30 per lining generation | 0.1–0.5 | 0.7–4 | One lining generation yields 10–30 t iron; relining 20–40 person-days + refractory clay 2–5 t + drying wood 2–5 t |
| **Total** | — | **≈115 (92–139 when charcoal yield swings 4–6)** | **314–684** | — |

Order-of-magnitude self-check (per file G02 §5): charcoal 23 t ÷ bloom 3.1 t ≈ 7.4:1, upper edge of the 4–8:1 range (incl. screening loss and forging heat) — pass. Wood 115 t ÷ (temperate forest growth 2.5 t/ha × 0.75 harvestable share, 37.2.2) ≈ **61 ha of woodland's sustainable annual yield** — that is the true price of one ton of iron. With back-hauling instead of carts, or the kiln off-site, person-days climb past 1,000.

Three immediate conclusions:

| Conclusion | Basis | Decision implication |
|---|---|---|
| The ironworks must sit where ore, charcoal, and water meet | ⑤⑥⑦ are 50–60% of total person-days | Site-selection procedure per Chapters 16, 18 |
| Doubling output = doubling woodland pressure | 61 ha·yr/t | Recompute N₂ (37.2.2) before any new furnace; against the 37.2.5 example settlement (400 ha woodland, 750 t/yr), 1 t/yr of iron already consumes 15% of annual yield |
| Fuel is the largest single cost item in iron | First in both FWE and person-days | Fuel-saving technology (furnace insulation, waste-heat preheating of blast) pays better than mining more ore |

[Card 38-02 Energy Ledger Conversion and Computation Card] (eight fields)

1. **Input materials**: conversion table (38.3.2 copied onto the flyleaf), monthly materials ledger (Card 38-01), per-furnace unit-cost records, weighing water and a measure (for approximate heat-value calibration).
2. **Required tools**: scale (calibrated per Card 38-01), graduated measure and water-boiling stove (boiling method), ledger book; no higher-precision instruments needed.
3. **Operating sequence and control points**: ① calibrate the local firewood-equivalent first (boiling method, median of 3); **② the conversion table is settlement-wide and unique — copy onto the flyleaf with version date**; **③ all green-wood batches converted before entry**; ④ fill physical quantity / FWE / person-days per stage in the blank table; ⑤ attach computation basis per stage; ⑥ compare results against next month's actual consumption; deviation >30% → re-examine stage factors.
4. **Empirical parameters and calibration**: every stage factor from the right-hand calibration column of the 38.3.4 table; filling from impression is forbidden.
5. **Process observation and recording items**: wood moisture batch number, charcoal kiln firing number, assumption row (grade, recovery, yield) listed separately; changed assumptions → recompute.
6. **Pass / rework / scrap criteria**: pass = three columns complete, every row justified, order-of-magnitude check passed; rework = any stage substituted a range default for measurement (measure and recompute within a month); scrap = green wood unconverted, or human/animal power mixed into FWE (whole card recomputed).
7. **Common failures and troubleshooting order**: result clearly too small → check screening loss and auxiliary consumption → check yield numerator/denominator; too large → check whether the wrong grade batch was used → check whether woodcutting hours double-count hauling (hauling is ⑤⑥); FWE doesn't match materials ledger → check whether both ledgers use the same conversion-table version.
8. **L1 / L2 / L3 evidence**: L1 = one completed computation sheet (range values allowed); L2 = computation sheet + one month of actual-consumption back-check (deviation ≤30%); L3 = two consecutive seasons back-checked + conversion table under version control (changes via 37.6.3 dual signature).

**Blank computation sheet (copy from card; target product: __ t):**

| Stage | Physical quantity | Firewood-equiv. | Person-days | Basis |
|---|---|---|---|---|
| Mining | | | | |
| Crushing/beneficiation | | | | |
| Woodcutting | | | | |
| Charcoal burning | | | | |
| Ore haul | | | | |
| Charcoal haul | | | | |
| Furnace floor | | | | |
| Forging | | | | |
| Lining amortization | | | | |
| **Total** | | | | |

## 38.4 Transport Ledger

### 38.4.1 Hauling-Capacity Table

All empirical values requiring field calibration; uniform calibration: three real loaded trips per mode, recording load, one-way distance, round-trip time — take the median.

| Mode | One-way load | Daily range | Capacity (kg/person-day·10 km) | Boundary | Notes |
|---|---|---|---|---|---|
| Human back-carry | 25–40 kg | 20–25 km round trip | 25–40 | Roadless hills, emergencies | Long-term back-hauling = a siting error |
| Shoulder poles | 40–60 kg | 15–20 km | 40–60 | Paths | Shoulder gear is a woodworking product (Ch. 7–9) |
| Wheelbarrow | 80–150 kg | 15–20 km | 80–150 | Graded dirt roads; out of use in mud season | Vehicle wear into the 38.5 ledger |
| Pack animal | 60–100 kg/head | 20–30 km | 60–100 (per head incl. drover) | Mountain trails | Feed cost listed separately (38.3.2) |
| Animal cart | 300–600 kg | 15–25 km | 300–600 (per cart crew: one person, one animal) | Dry roads | Vehicle maintenance in its own account |
| Water (if navigable) | 0.5–5 t/boat | 30–60 km | calibrate per boat crew | Downstream and flat stretches | Where navigable, water precedes all land transport |

Road-condition derating factors (multiply table capacity):

| Condition | Factor | Criterion |
|---|---|---|
| Grade >10% or gravel surface | ×0.5–0.7 | rests required on grades >200 m |
| Mud season | ×0.4–0.6 | wheelbarrow out of service when ruts hold >50 mm of water |
| Snow and freeze | ×0.6–0.8 | snow >100 mm → switch to sled; capacity re-calibrated |

Derating entry rule: the transport master ledger's "mode" column notes the month's road condition; condition changes never rewrite history — they change next month's budget.

### 38.4.2 Entering Transport Costs

Two line items: **t·km (displacement) and person-days (consumption)**. Formula for the transport column of any product's unit cost:

> Transport person-days = unit physical quantity (kg) × distance (km) ÷ 10 ÷ capacity (kg/person-day·10 km)

Ore, charcoal, wood, and finished goods are carried in four separate accounts — merging them into "misc haulage" is forbidden: distances and capacities differ, and merging destroys diagnostic power (failure-modes table, row 5). Table capacities already include the return trip (empty return counted at half); one-way carriers (downstream rafts) account recovery costs separately — table values do not apply.

**Monthly transport master ledger form (illustrative; capacities from 38.4.1):**

| Category | Monthly tonnage | Mean distance (km) | t·km | Person-days (or cart-crew days) | Mode |
|---|---|---|---|---|---|
| Ore → smelter | 18 | 5 | 90 | 60–113 | wheelbarrow |
| Charcoal → forge | 6 | 3 | 18 | 12–23 | wheelbarrow |
| Wood → settlement (household + workshop) | 14 | 2 | 28 | 5–9 cart-crew days | animal cart |
| Iron ingots → market | 0.6 | 10 | 6 | 4–8 | wheelbarrow |

Two readings: first, the wood-hauling share = (5–9) ÷ (felling 9–20 + hauling 5–9) ≈ 20–50% — the range straddles 37.6.4's 40% red line, so this month's **measured** hours set the reading; above 40%, or rising >10 points in a year, the forest is sealed and output cut. Second, ore haul at 60–113 person-days is ~50% of all transport, confirming that step ③ of 38.4.3 ("move the furnace to the ore") deserves priority evaluation. Also links to the 37.2.3 building-material criterion: any material whose round-trip sourcing exceeds 1/3 of the working day is re-assessed as unsustainable.

### 38.4.3 Transport-Radius Criterion: When Does a Mine Stop Paying

Three-step estimate (for 1 kg of iron):

| Step | Computation | Criterion and outcome |
|---|---|---|
| ① Ore-haul person-days | Ore consumption (20–40 kg) × distance ÷ 10 ÷ capacity | — |
| ② Compare with mining person-days | Against 38.3.3 ①② (≈0.7–3 person-days/t ore, converted per kg) | Hauling > mining → haul roasted concentrate instead (roasting per Ch. 16), cutting tonnage 30–60% |
| ③ Compare with furnace-moving cost | On-site primary smelting increment (build furnace, haul charcoal to ore) vs. raw-ore haul increment | Ore haul + charcoal haul person-days > on-site increment → move the furnace to the ore |

Empirical thresholds (calibrate to local capacity): for lean ore (>20 kg ore/kg iron), economic ore haul distances — back-carry 3–5 km, wheelbarrow 8–15 km, animal cart 20–40 km. Beyond threshold, evaluate in order: haul roasted bloom only → move furnace to ore → abandon the site (back to Ch. 16 site evaluation).

Another standing red line (37.6.4; executed through this chapter's transport ledger): **wood-hauling hours ÷ total fuel-acquisition hours > 40% → seal the forest and cut output** — this red line's reading comes precisely from the four-way transport accounts of this section.

## 38.5 Tool Wear Ledger

### 38.5.1 Consumable Life Table

All empirical values requiring field calibration. Master method: **tag every item with an item-history card, record its start date and each use; at scrap, record cause and cumulative output**. After 3 months of operation, replace this whole table with settlement-measured values, copied into the archive.

| Consumable | Life (empirical) | Counting basis | Scrap criterion (observable) | Charged to | Source chapter |
|---|---|---|---|---|---|
| File | 50–200 filing hours | hours log | teeth glide without biting; still glides after re-cutting | standards, tools | Ch. 19–20 |
| Potter's scraper, bamboo knife | 0.5–2 months | piece-months | edge curled or worn into the grip section | pottery | Ch. 11 |
| Clay crucible (copper) | 5–15 melts | numbered per crucible | hairline crack, wall erosion >1/3 thick, weeps on water test | copper | Ch. 17 |
| Crucible (glass) | 10–30 melts | numbered per crucible | same | glass | Ch. 14 |
| Smelting-furnace lining | 10–50 smelts or 1–2 seasons | per-smelt check | remaining wall <1/3 (probe-rod measured) | iron | Ch. 18 |
| Bellows leather face | 0.5–2 years | bellows log | air leak hiss within stroke; >3 patches | all air-blast furnaces | Ch. 12, 18 |
| Drive belt | 200–1,000 running hours | run log | speed drop >20% under load; visible transverse cracks | machine tools, waterwheel output | Ch. 20–22, 29 |
| Saggar, kiln supports | 5–20 firings | numbered per piece | cracks, warping that jams ware | pottery, brick | Ch. 12 |
| Rope, sling | 20–80 hoists | tag counter | fuzz >1/3 strands, ≥1 broken strand | all hoisting | — |
| Wood bearings (potter's wheel, waterwheel) | 3–12 months | start date | play >2 mm (measured by slip of thin blade) | pottery, power | Ch. 11, 29 |
| Steel drills, chisels | 5–15 regrinds, 5–10% shorter each | regrind count | length exhausted or shaft bent | mining, stonework | Ch. 16 |
| Lamp wick | 10–30 h | burn timing | charred black, dim | lighting (household ledger) | — |
| Whetstone | 0.5–2 years | start date | middle groove >10 mm (straightedge test) | all edged tools | Ch. 5, 19 |
| Potter's wheel head and cup | 1–3 years | start date | visible wobble; >30% speed drop at same effort | pottery | Ch. 11 |
| Blast tuyere (clay or wood tube) | 0.5–2 years | start date | joint leaks (flame-deflection test) | air-blast furnaces | Ch. 12 |
| Charcoal kiln door and sealing mud | 3–10 firings | count | door frame burnt and warped; sealing mud cracked and leaking | charcoal | Ch. 6 |

### 38.5.2 Wear Amortization

Formula:

> **Amortization per unit product = (replacement labor + replacement material) ÷ lifetime output**

Example: a copper-smelting crucible's replacement = 6–10 person-hours of making + 15–25 kg clay and sand; life 10 melts × 8–15 kg copper per melt → per melt, 0.6–1 person-hour + 1.5–2.5 kg clay/sand → **per kg of copper, 0.04–0.13 person-hours and 0.1–0.3 kg clay/sand**. This figure enters the 38.2.1 summary's "consumables amortization" column.

Three amortization rules:

| # | Rule | Reason |
|---|---|---|
| 1 | Amortize by measured life, not by this table's ranges indefinitely | the table is a starting point; after 3 months without measurement the item counts as uncalibrated |
| 2 | Spare-parts stock = daily consumption × replenishment lead × 1.5 | same structure as 38.2.4 reorder points; execution belongs to the maintenance system (Next Dependencies) |
| 3 | Scrapped items retained until the monthly stocktake | stocktake-gap evidence; disputed scrap criteria are settled by the physical item (Iron Law 6: a pass without evidence is not a pass) |

**Item-history card (tag) format:**

| Number | Item name | Batch no. | Start date | Use record (date / conditions) | Scrap date | Scrap criterion | Cumulative output |
|---|---|---|---|---|---|---|---|
| | | | | | | | |

Registration rules: one tag per item, the tag travels with the item; at scrap the tag is torn off and pasted into that month's stocktake sheet; items of one batch (crucibles from one kiln load) share a batch number so whole-batch life can be compared — a uniformly short batch points to workmanship; individually short items point to service conditions.

Disposition priority before scrapping (executing Iron Law 4: "tool damage must state whether it is repairable"):

| # | Disposition | Example |
|---|---|---|
| 1 | Repair | file re-cut; drill regrind (counted per 38.5.1) |
| 2 | Downgrade | fine file → coarse file; cracked-but-not-leaking crucible → preheat crucible; old lining brick → kiln supports |
| 3 | Material recovery | scrapped iron back to the forge (Ch. 18); broken belt → sling (recounted) |
| 4 | Scrap with sample retained | history card pasted to the stocktake sheet; item into the retention basket |

Criterion: skipping 1–3 straight to scrap requires a written reason in the history card's "scrap criterion" field.

## 38.6 Monthly Stocktake and Supply-Cutoff Warning

### 38.6.1 Stocktake Procedure

| Step | Action | Criterion |
|---|---|---|
| 1 | Open the stocktake after month-end books close; two-person count (custodian + bookkeeper) | single-person counts invalid; rushing the count before close = scrapped (Card 38-03 field 6) |
| 2 | Weigh or count everything | 10% re-weigh sample; re-weigh discrepancy >2% → re-weigh the whole batch |
| 3 | Gap rate = |physical − book| ÷ book | >5% investigated within the month (37.6.1 warehouse rules) |
| 4 | Shortage three-check (38.6.2) | in order: records first, physical evidence second, people last |
| 5 | Update the three-color board (38.6.3) | color changes posted at the mess hall and workshops |
| 6 | Stocktake sheet dual-signed and archived | copied into the ledger with counter and date |

**Yellow-tier ten-day mini-sheet (one row per ten days during yellow tier; key materials only):**

| Ten days | Material | Physical count | Ten-day use | Monthly projection | Reserve months | Color | Signature |
|---|---|---|---|---|---|---|---|
| | | | | | | | |

Rule: ten-day use × 3 is for early warning only and never replaces the monthly stocktake; two consecutive ten-day periods darkening the color triggers a red-tier assessment early — do not wait for month-end.

### 38.6.2 The Shortage Three-Check

| Check | Criterion (what counts as a hit) | Disposition |
|---|---|---|
| 1. Missing records | requisition stub gaps, unentered returns, proxy signatures, vague summaries that don't match batches | replacement marked "replacement"; the handler does bookkeeping practice that month and later pages are re-checked |
| 2. Pilferage | shortages concentrated in concealable small items (salt, lamp oil, iron nails, copper, finished tools) with patterned timing | audit the two-person two-lock records; personnel handled separately; fix the warehouse system first, accountability second |
| 3. Process drift | books complete but unit costs rise month over month — nothing stolen; the process is eating more | check 37.6.3 change register (unsigned changes?) → per-batch grade records (Ch. 16) → lining wall thickness (38.5.1) |

The check order is fixed: records first, physical evidence second, people last. Inverting the order turns process drift into a theft case — after which nobody records honestly again; that kills the ledger institution faster than any fuel cutoff.

### 38.6.3 Three-Color Warning Lines

Reserve months = physical stock ÷ trailing 3-month average monthly consumption (rolling update; last season's stale average is forbidden).

| Color | Reserve months | Action (fixed on the board; no on-the-spot debate) |
|---|---|---|
| Green | ≥2.0 months | normal production; meet reorder points (38.2.4); bookkeeper's monthly stocktake |
| Yellow | 1.0–2.0 months | no new orders; increase cutting and purchasing; non-critical furnaces limited; key materials move to **ten-day counts** |
| Red | <0.5 month (~2 weeks) | **cut production to survive**: seal non-essential furnaces (per each chapter's shutdown procedure; metallurgy per Ch. 18); protect household fuel and critical maintenance only; draw reserves per the pre-agreed plan; the recovery order is pre-written on the board's reverse |

Dual criterion for key furnace materials: charcoal, ore, and refractory carry, besides the months line, a **hard furnace-charge line — stock < 2 furnace-charges = stop line and replenish** (38.2.4, linking to Ch. 18 L3). The months line governs slow variables (household wood, salt, grain); the charge line governs fast variables (furnace materials); each triggers independently, neither substitutes for the other.

**Color-change record sheet (pasted on the board's reverse):**

| Date | Material | Color change (→) | Reserve months at trigger | Action | Responsible | Back-to-green date |
|---|---|---|---|---|---|---|
| | | | | | | |

Rule: a color change without a record = an unhandled event (L3 veto item); returning from red to green requires dual signature from the bookkeeper and the works supervisor — preventing "paper green" by borrowing against in-transit quantities.

**Red-tier shutdown order (agreed in advance; on a red day, execute in order — no debate):**

| # | Seal first | Reason |
|---|---|---|
| 1 | Glass furnace, non-ferrous smelting | most fuel-intensive; product can wait |
| 2 | Brick and tile kilns | construction can defer; use stocked brick |
| 3 | Lime kiln (retain one) | agricultural and sanitary lime must not stop |
| 4 | Iron smelting furnace | seal and hold warm per Ch. 18 shutdown procedure; preserve the furnace body |
| 5 | Cooking and heating | never sealed — household fuel is the last reserve (37.6.4) |

Recovery runs in reverse order; the shutdown order is written on the board's reverse and archived with the color-change records.

[Card 38-03 Monthly Stocktake Card] (eight fields)

1. **Input materials**: current month's sub-ledgers from every workshop, full requisition stub book, last month's stocktake sheet, three-color board, scrap-retention basket, standard weights for spot re-weighing.
2. **Required tools**: scale (cross-checked once before starting, >2% error = out of service), board chalk or colored earth. No higher-precision instruments needed.
3. **Operating sequence and control points**: ① stocktake only after month-end close; **② two-person count + 10% re-weigh sample**; ③ compute gap rate; >5% triggers the three-check this month; **④ three-check order fixed: missing records → pilferage → process drift**; ⑤ update and post the three colors; ⑥ dual-sign and archive, copies to the works supervisor and the council.
4. **Empirical parameters and calibration**: gap line 5% (37.6.1); sample share 10%; three-color thresholds 2.0/1.0/0.5 months — after one year of operation, re-validated against local cutoff and color-change history; revision via 37.6.3 dual signature.
5. **Process observation and recording items**: gap rate per warehouse, three-check hits, color changes with trigger dates, whether the board-reverse recovery order still matches physical reality.
6. **Pass / rework / scrap criteria**: pass = every warehouse counted, gap ≤5% or three-check concluded, board updated and posted; rework = gap 5–10% unresolved within the month (due by the 10th of next month, else escalated to scrap); scrap = rushing the count before close, or a single-person count (that month's books re-counted).
7. **Common failures and troubleshooting order**: same warehouse gap >5% two months running → check the scale → check two-person two-lock execution → check handler rotation; color change with no action → check whether actions are truly fixed on the board → check whether the council overrode the lines; yellow accelerating to red → check whether the consumption baseline misuses a slack-season average.
8. **L1 / L2 / L3 evidence**: L1 = one completed monthly stocktake sheet; L2 = 3 months gap ≤5% + one complete three-check record; L3 = one genuine color change with full plan-based disposition + threshold revision dual-signature slip + archived ledger.

**Blank monthly stocktake sheet (copy from card):**

| Warehouse / material | Book | Physical | Gap rate | Three-check result | Color this month | Disposition | Dual signature |
|---|---|---|---|---|---|---|---|
| | | | | | | | |
| | | | | | | | |

Stocktake sheets are transcribed per warehouse, one page per warehouse, bound and archived at year-end.

## Parameter Master Table

| Parameter | Empirical value | Calibration | Section |
|---|---|---|---|
| Firewood-equivalent heat | 3,500–4,000 kcal/kg | boiling method, median of 3 | 38.3.1 |
| Charcoal heat-equivalent | 1.7–2.1 FWE/kg | from heat values | 38.3.2 |
| Charcoal production-equivalent | 4–6 kg wood/kg charcoal | whole-kiln weigh-in/out (Ch. 6) | 38.3.2 |
| Green-wood conversion | 0.5–0.7 FWE/kg | sample dry-down weighing | 38.3.1 |
| Human effective mechanical work | 0.15–0.3 kWh/person-day | not converted to FWE; transport capacity measured live | 38.3.2 |
| Animal effective mechanical work | 2–3 kWh/head-day | same; hay 8–12 kg/head-day | 38.3.2 |
| Iron full-chain charcoal cost | 20–35 kg/kg dense iron | furnace ratio 4–8:1 ÷ yield 25–40% cross-check | 38.2.1 |
| Iron full-chain ore cost | 20–40 kg/kg | reciprocal of grade × recovery × yield | 38.2.2 |
| FWE per ton iron (worked example) | 92–139 t | Card 38-02 staged computation + back-check | 38.3.4 |
| Limestone consumption | 1.7–2.2 kg/kg | weigh-in/out over 3 firings | 38.2.1 |
| Copper crucible life | 5–15 melts | item-history cards per crucible | 38.5.1 |
| Furnace lining generation | 10–50 smelts or 1–2 seasons | probe-rod wall measurement | 38.5.1 |
| Back-carry capacity | 25–40 kg/person-day·10 km | median of 3 loaded trips | 38.4.1 |
| Wheelbarrow capacity | 80–150 kg/person-day·10 km | same | 38.4.1 |
| Lean-ore economic distance | back 3–5 / barrow 8–15 / cart 20–40 km | three-step method + local capacity | 38.4.3 |
| Reorder point | lead-time consumption + 2 charges | longest of 3 measured cycles | 38.2.4 |
| Spare-parts stock | daily use × lead × 1.5 | measured daily use from history cards | 38.5.2 |
| Stocktake gap line | 5% | 37.6.1 warehouse rules | 38.6.1 |
| Three-color lines | green ≥2 / yellow 1–2 / red <0.5 months | local cutoff and color-change history | 38.6.3 |
| Computation back-check line | ≤30% | actual monthly consumption vs. computation | Card 38-02 |
| Energy ledger deviation line | >20% for 2 months → recompute N₂ | vs. 37.2.2 woodland budget | 38.3.3 |
| Ten-day report line | >10% projected → report; >20% → investigate | mid-month rate extrapolation | 38.2.3 |
| Wood-haul red line | hauling person-days ÷ total fuel hours >40% | 37.6.4; monthly transport ledger reading | 38.4.2 |
| Volume-conversion audit line | >10% → full weighing | 10% of converted batches monthly | 38.2.5 |
| Road-condition derating | grade ×0.5–0.7; mud ×0.4–0.6 | 3 loaded comparisons on the same stretch | 38.4.1 |
| Red-tier shutdown order | glass → brick → lime (retain one) → iron; cooking never sealed | pre-agreed, posted on board reverse | 38.6.3 |

## Failure Modes and Diagnosis

Ordered by "hardest to detect" — most failures this chapter handles are silent: mute in year one, visible in year two.

| Symptom | Candidate causes | Verification | Disposition | Prevention |
|---|---|---|---|---|
| Unit costs rising month over month (books complete) | process drift (uncontrolled change) or falling ore grade — must be separated | check 37.6.3 change register → per-batch grade records (Ch. 16): grade down while mix steady = ore; grade steady while charcoal up = furnace | ore: switch source or add beneficiation; furnace: check lining and blast, then back to the chapter | change dual-sign + per-batch grade records |
| Charcoal use spikes, iron output doesn't | lining degraded (thin walls leak heat); insufficient blast; charcoal under-burned | probe rod for wall thickness → bellows log → break charcoal (under-burned shows a brown core) | stop and reline (38.5.1); repair bellows; return charcoal to the kiln | per-smelt wall check; charcoal break-sample acceptance |
| Books ≠ goods (gap >5%) | missing records / pilferage / scale drift | three-check in fixed order (38.6.2); scale first, books second | per three-check results; scale over-tolerance flags the month's books "questionable" | dual signature, stub numbers, monthly scale cross-check |
| Stock "looks enough" then sudden cutoff | in-transit counted as stock; stale baseline (slack-season average) | audit in-transit documents; recompute trailing 3-month average | warning reads only the stock column; baseline switched to rolling 3 months | 38.2.3 in-transit rule |
| Transport person-days exploding | ore/wood sources receding; road damage; mud-season shutdown | check which of the four transport accounts is rising (38.4.2) | past 38.4.3 thresholds: roasted bloom only / move furnace / abandon site; roads into the maintenance plan | site at ore-charcoal-water junction; pre-season road repair |
| Monthly energy ledger over woodland budget for months | expanding cutting radius hidden by "free wood"; green wood unconverted | audit felling-zone register and round-trip hours (37.6.4); check moisture conversion records | recompute N₂ (37.2.2); cut workshop wood before household wood | monthly energy ledger + quarterly red-line patrol |
| Consumables failing in batches | bad batch; use beyond duty | history-card scrap-cause distribution | halt the batch, back to the chapter; overuse via 37.6.3 change control | item-history cards + scrap samples |
| Three-color never changes — then jumps to red | key materials never entered on the board; stocktake interval too long | does the board list charcoal, ore, refractory, crucibles? | complete the list; key materials to ten-day counts | stocktake card step 5 |
| Household items mixed into workshop accounts (salt, lamp oil, cooking wood) | undefined boundary | check summary-column usage field | re-enter in separate accounts; household back to Ch. 37 | summary column must name "workshop/furnace/batch" |
| Books≠goods after a change of bookkeeper | newcomer unfamiliar with conventions (in-transit, conversion, summary format) | check conversion notes and summaries on newcomer pages | old bookkeeper mentors for a month; conventions written on the ledger page header | dual signatures + ten-day reconciliation |

## Process Card Index

| Card no. | Name | Purpose | Copy to |
|---|---|---|---|
| 38-01 | Materials ledger card | four-column flow recording + blank pages | workshops / warehouse |
| 38-02 | Energy conversion and computation card | conversion table and full-cost staged computation | bookkeeping office / council hall |
| 38-03 | Monthly stocktake card | stocktake procedure, shortage three-check, three-color update | bookkeeping office / warehouse / mess-hall board |

## Acceptance Criteria L1/L2/L3

| Level | Criterion | Test conditions | Evidence retained |
|---|---|---|---|
| L1 | Four-column ledger running 1 month; opening stocktake done; unit-cost summary copied and calibration started | verification items may have gaps but must be marked "provisional account" | original ledger, stocktake record |
| L2 | 3 months gap ≤5%; at least one product with measured unit cost; one full energy computation back-checked against reality, deviation ≤30% | dual-person stocktake; computation and back-check same basis | 3 stocktake sheets, calibration records, computation-back-check comparison |
| L3 | Three-color or furnace-charge line genuinely triggered once and handled per plan; no unplanned line stops from material shortage during reorder-point operation; books≠goods holds after a change of bookkeeper; calibrated values and threshold revisions copied into the archive with dual signature | reproduced through staff changes and season changes | full color-change disposition record, ledger transcriptions, dual-signature change slips |

## Labor Hours and Consumption

| Item | Crew and duration (empirical) | Notes |
|---|---|---|
| First-time account opening (stocktake + books) | 30–60 person-hours + counting labor per warehouse | up to 8 warehouses |
| Daily recording | 5–15 min/day per workshop | record at issue, never defer |
| Unit-cost calibration | 10–20 min per smelt (four-point weighing) | replaces all ranges within 3 months |
| Monthly stocktake | 2 people × half-day per warehouse | dual-person rule; yellow-tier key materials add ten-day counts |
| Energy computation | 20–40 person-hours per run | quarterly, or before any new furnace |
| Bookkeeping office | 0.5–1 dedicated person | same person as the Ch. 37 bookkeeper post |
| Yellow-tier ten-day counts | 0.3–0.5 person-hour/material·ten days | board key materials only |
| Volume-conversion spot checks | 0.5–1 person-hour/month | converted batches first |
| This chapter's own consumption | ledger paper, charcoal pencils, chalk, lamp oil | entered monthly — the ledger itself is on the books |

## Safety Boundaries

No high-temperature or high-pressure operations in this chapter, but the following four items are part of the procedure — failing to execute them equals failing the chapter:

1. **Charcoal-store fire prevention**: fresh charcoal air-cooled 24–48 h before storage; charcoal store ventilated, no open flame, ≥20 m from dwellings; daily patrol (smoke, scorched smell). A charcoal-shed fire burns more than charcoal — it burns the data origin of the entire fuel account.
2. **Stocktake yard safety**: piles no taller than a person, nobody stands on pile tops; two-person carries; ladder holder required for high retrieval.
3. **Custody/bookkeeping separation**: the custodian and the bookkeeper must not be the same person (two-person two-lock, 37.6.1); violations rework that month's books.
4. **Red-tier actions put people first**: red-tier furnace sealing follows the Ch. 18 shutdown procedure; "rescuing stock" through rule-breaking rush-smelting is forbidden; when fuel runs short, household wood is protected first (37.6.4) — cold, hunger, and smoke dust kill the workforce faster than supply cutoffs (Iron Law 7).

## A/B/C Lists

**A list (executable with this chapter):**

| Item | Criterion |
|---|---|
| Four-column ledger bound and running daily | Card 38-01 eight fields complete; daily and monthly closure |
| Opening stocktake | error ≤10%, data origin date stated |
| Unit-cost summary copied, calibration started | 38.2.1 table + per-smelt four-point weighing records |
| Item-history cards tagged | full 38.5.1 table numbered and registered |
| Three-color board established | list includes charcoal, ore, refractory, crucibles; actions fixed on the board |
| First monthly stocktake and three-check executed | Card 38-03 |
| Reorder points computed per material | written on each ledger page header |

**B list (requires prior chapters):**

| Item | Prerequisite |
|---|---|
| Measured unit costs per furnace | Ch. 6, 11–14, 16–19, 28 L3 ledgers |
| Per-capita household baselines | Ch. 37 calibrated values |
| Weights-and-measures cross-check | Ch. 3, 22 standards |
| Furnace shutdown procedure (red-tier actions) | Ch. 18 |
| Roasted-concentrate haul reduction | Ch. 16 |
| Recording materials and ledger books | Ch. 4 |

**C list (external dependencies and irreducibles):**

| Item | Note |
|---|---|
| Uncalibrated unit costs | this chapter's ranges only; magnitude judgment |
| Ore-vein exhaustion timing | unpredictable; only monthly grade-trend monitoring |
| Seasonal and batch swings | ±20–30%, recorded as they are — no averaging away |
| Continuous scale/measure calibration | depends on not losing the Ch. 3, 22 standards |
| Paper raw-material unit cost | (reserved column, to be added) |

## Next Dependencies

- **Chapter 39 Maintenance and spares**: the execution end of this chapter's wear ledger — item-history cards roll up into spare-part making and regrinding plans; the spare-stock formula (38.5.2) becomes work orders and inspection points there.
- **Chapter 40 Redundancy and resilience**: the reserve categories and quantities behind "draw reserves per the pre-agreed plan" are defined in Ch. 40; this chapter's job is only to shout red two months early.
- **Chapter 43 Archives**: all calibrated values, stocktake sheets, and color-change records are copied into the archive with retention periods; a lost ledger demotes every unit cost to uncalibrated (file G02 §5).
- **Reverse dependency (whole book)**: the "materials, records" columns of every chapter's L3 acceptance, Chapters 1–40, are executed uniformly through Cards 38-01 and 38-03 — without this chapter, every earlier chapter's L3 is only half-accepted; and Ch. 37's carrying capacity would remain a once-a-year snapshot — with this chapter it becomes a daily-auditable living account.
