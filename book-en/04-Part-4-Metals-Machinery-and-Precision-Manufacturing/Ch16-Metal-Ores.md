# Chapter 16 Understanding Metal Ores

> Part 4: Metals, Machinery, and Precision Manufacturing. Part 4 solves the core problem of the whole book: manufacturing "the tool that can make other tools." The metals route has four steps: this chapter learns the ores → Chapter 17 takes the first metal → Chapter 18 goes from ore to iron → Chapter 19: steel and heat treatment. This chapter covers prospecting, identification, sorting, evaluation, and **shallow mining engineering** — smelting belongs to Chapters 17 and 18.

## Chapter Objectives

- Build the ability to distinguish "metal ore" from "metal" (Iron Law 3).
- Build a field identification criteria table for the four main ore types — copper, iron, tin, and lead (streak, density, cleavage, simple chemical tests).
- Build the crushing–screening–panning (heavy-mineral-concentrate method) beneficiation workflow and its tools.
- Build the ore-source evaluation method: grade estimation, mining cost accounting, rough reserve estimation, and **numerical exit criteria**.
- Build shallow mining engineering capability: **support, drainage, ventilation, and toxic-gas testing for open shallow pits and initial drifts** (added in 16.8).
- Deliverables: registration of metal ore occurrences, sample book and grade records, and the "metal-route selection for this region" conclusion.

## Capability Boundary

**Can do:** open shallow pits (no deeper than a person) and supported initial drifts (advance ≤ a few steps, dual exits or strong ventilation); hand-sorting + panning beneficiation; three-level visual grade estimation cross-checked against quantitative panning.

**Explicitly cannot do:** delineating deep ore bodies (no drilling); deep shaft sinking and long tunnels (limited by drainage and ventilation capability — **deep-mine drainage was precisely the first historical use of the Chapter 28 steam engine**; the route was long since drawn on the dependency graph); quantitative chemical composition (Chapters 23 and 26); zinc smelting (no condensation-collection means — abandoned).

## Pre-Start Verification (check off each item)

| # | Verification item | Criteria | Source |
|---|---|---|---|
| 1 | Identification tool kit | Streak plate, hardness reference set, ten-step identification card carried on the person | Chapter 2 |
| 2 | Measurement | Standard rod, balance weights, error record sheets | Chapter 3 |
| 3 | Stone and wood tools | Stone hammer set, full woodworking set, three grades of rope | Chapters 5 and 7 |
| 4 | Experiment system | Single-variable method, record sheet templates practiced to fluency | Chapter 8 |
| 5 | Screens and bags | Three grades of woven screens, numbered ore sample bags | Chapters 7 and 15 |
| 6 | Transport | Back frame and rollers in place (ore is heavy) | Chapters 7 and 10 |
| 7 | Mining engineering materials (before starting 16.8) | Support timber (hardwood posts/planks), 2 torches, water-lifting bucket, rope | Chapter 7 + this chapter |

---

### 16.1 Copper, Iron, Tin, Lead, and Other Common Metals

**First set up the master ledger: metal reactivity determines smelting difficulty.** Ordered by "restart difficulty":

| Metal | Main ores | Theoretical smelting temperature (carbon reduction) | Restart priority |
|---|---|---|---|
| Copper | Malachite, cuprite, native copper | ~700–1100 °C | **Highest**: oxidized copper ores are the easiest to smelt |
| Lead | Galena | ~700–900 °C | High: easy to smelt and cast, poor mechanical properties |
| Tin | Cassiterite | ~1100–1300 °C + flux | Extremely high if present (bronze); substitute if absent |
| Iron | Hematite, magnetite, limonite | Reduction at ~800–1200 °C (solid state) | High: fuel threshold higher than copper |
| Zinc | Smithsonite, zincite | >1000 °C, and zinc's boiling point is low | **Abandon**: vapor escapes and is toxic |
| Silver, gold | Native gold; silver-bearing galena | Gold obtainable by panning; silver requires cupellation | Register only, do not pursue |
| Arsenic | Arsenopyrite, arsenical copper ore | Occurs with copper ores | Substitute raw material; highly toxic (17.8) |

**Streak table (memorize all eight entries on top of the five from Chapter 2)**:

| Mineral | Massive appearance | Streak | Hardness | Density feel | Diagnostic criterion |
|---|---|---|---|---|---|
| Malachite | Bright green bands | Pale green | 3.5–4 | Heavy | Bubbles vigorously with a drop of acid |
| Azurite | Deep blue | Light blue | 3.5–4 | Heavy | Occurs together with malachite |
| Cuprite | Reddish brown to lead gray | **Brownish red** | 3.5–4 | Heavy | Commonly occurs with malachite |
| Chalcopyrite | Brass yellow | **Greenish black** | 3.5–4 | Heavy | Difference from gold: black streak, brittle |
| Magnetite | Iron black, metallic luster | Black | 5.5–6.5 | **Very heavy** | Attracted by natural lodestone; dense fracture surface |
| Hematite | Reddish brown to steel gray | **Cherry red** | 5–6 | Heavy | However black the massive form, the streak is always red |
| Cassiterite | Brown with golden-red luster | White to pale yellow | 6–7 | **Extremely heavy** | Same-volume piece weighs about 2.5x quartz; does not react with acids |
| Galena | Bright lead gray | Lead-gray black | 2.5 (soft) | **Extremely heavy** | **Cubic cleavage**: breaks into small cubes when struck |

### 16.2 How to Find Minerals from Surface Signs

**Six classes of prospecting indicators (ordered by reliability)**:
1. **Gossan, the iron cap (most important)**: the weathered limonite crust atop sulfide deposits — reddish brown, porous, honeycombed. Primary sulfide ore may lie beneath it;
2. **Oxidized-zone colors**: green (malachite), blue (azurite), and reddish brown (hematite) staining bands on bedrock outcrops — staining on fracture faces is more reliable than staining on loose soil;
3. **River-beach heavy-mineral concentrate**: ore minerals are dense and concentrate naturally in riverbed cracks and on the insides of river bends; upon picking up "unusually heavy dark grains," trace them upstream;
4. **Bedrock and artificial outcrops**: canyon walls, fresh landslide scarps, and spots where fallen trees have torn up the roots;
5. **Old pits and ancient slag heaps**: occurrences already verified by predecessors;
6. **Botanical anomalies**: leads only, never grounds — **must not serve alone as the basis for registration**.

**Tracing method**: after finding an indicator, chip and number one sample every 20–30 steps along the strike, until three consecutive points show no mineralization. Ore-occurrence boundaries are drawn with data; writing "it is everywhere" is not allowed.

### 16.3 The Difference Between Ore and Ordinary Rock

**Core concept: grade.** Three-level visual estimation:

| Level | Visual feature | Equivalent metal grade (empirical) | Disposition |
|---|---|---|---|
| Rich ore | Useful minerals contiguous over ≥1/2 of the fracture face to the naked eye | Cu ≥20%, Fe ≥50% | Direct furnace-feed candidate |
| Medium ore | Specks and bands over 1/5–1/2 | Cu 8–20%, Fe 30–50% | Crush + hand-sort / pan |
| Lean ore | Specks <1/5 | Cu <8%, Fe <30% | Registration deferred |

**Misjudgment cross-reference table**:

| You think it is | It may actually be | Discriminating criterion |
|---|---|---|
| Malachite | Chlorite, epidote | Bubbles with acid = malachite; silicates do not bubble |
| Magnetite | Hornblende, biotite | Heavy heft; hornblende has cleavage, biotite peels into thin flakes |
| Cassiterite | Rutile, garnet | Cassiterite is extremely heavy, greasy luster, conchoidal fracture |
| Galena | Stibnite | Cubic cleavage is unique to galena |
| Hematite | Red sandstone, laterite | Streak cherry red vs. white |
| Pyrite | Gold ("fool's gold") | Gold is soft (scratchable with a fingernail) with a golden-yellow streak; pyrite is hard with a greenish-black streak |

**Density-feel calibration method**: carry a fist-sized quartzite reference block (density about 2.6) at all times. Heft pieces of equal visual size, one in each hand: 1.5x the heft → "heavy" (3.5–5); 2x or more → "extremely heavy". Quantitative check: immerse the ore in a water-filled leather bag; the overflow volume = the volume, and weight ÷ volume = density.

### 16.4 Crushing, Screening, Panning, and Sorting

**Workflow: run-of-mine ore → hand sorting → crushing → screening → (panning) → concentrate.**

- **Hand sorting**: the standard-sample method — nail a "qualified for the furnace" specimen beside the sorting bench and pick out everything inferior. After hand sorting, the rich-ore fraction of a basket of medium ore often doubles (empirical value);
- **Crushing**: stone anvil + stone hammer (500–800 g for coarse crushing / 300–500 g for medium crushing); surround the anvil on three sides with wooden guards against splashing; **furnace feed is 5–20 mm — do not crush finer** (fines clog the furnace gas passages); crush panning check samples below 2 mm;
- **Screening**: three grades of woven screens (coarse 15 / medium 8 / fine 3 mm; verify the mesh openings with the standard rod by sampling 10 holes and measuring the extreme spread). +15 mm goes back for re-crushing, 8–15 mm is the main furnace feed, −3 mm serves as the panning sample.

[Card 16-01 Heavy-Mineral Panning] (eight fields)

1. **Input materials**: fine ore sand (crushed below **2 mm**; the −3 mm grade serves as the panning sample); still water.
2. **Tools required**: wooden panning pan (**mouth 40–50 cm, depth 8–10 cm, inner wall scraped smooth**), still-water trough, drying yard, balance (dry-weight cross-check). Calibration source: concentrate quantity is read from **the pan's heft**, compensated by weighing after drying; the round-count endpoint is judged by eye — the concentrate layer on the pan bottom "stops thickening".
3. **Sequence and control points**: (1) load the sample (**pan bottom ≤1 cm thick**); (2) soak through; (3) rub apart into a slurry underwater; (4) **horizontal circular swirling + light jiggling** (the heavy sinks); (5) tip the pan outward to pour off 1/3 of the water, floating away light sand; (6) repeat **10–20 rounds**; (7) tilt to drain, sun-dry, collect the concentrate. Control points: do not load too thick (the pan rides heavy); do not swirl too violently (all the sand floats away).
4. **Empirical parameters and calibration**: the endpoint is when the concentrate layer "stops thickening" (◎ hand-feel: the change in the pan's heft; compensation: weigh dry and compare); recovery acceptance — **the second pass over the tailings yields <10% of the first** (criterion).
5. **Observations to record**: concentrate color (deep black / tin white / golden yellow registered separately), round count, dry concentrate weight, tailings re-pan result, tailings-pile location.
6. **Pass / rework / scrap criteria**: pass = the second tailings pass yields <10% of the first; rework = the second pass still yields much (technique unstable) — keep practicing on the same batch; scrap = the pan is judged unrecoverable — tailings go to the tailings pile, **location registered, water sources protected**.
7. **Common failures and diagnosis order**: (1) all the sand floats away → swirling too violent; (2) heavy and light not separated → density difference insufficient (gravity separation unsuited to this ore; switch to hand sorting); (3) the pan rides heavy → sample loaded too much; (4) concentrate yield falling pan by pan → go back to the sampling point and the ore's grain size.
8. **L1 / L2 / L3 evidence**: L1 = one pan meeting standard (tailings re-pan <10%); L2 = tailings re-pan records on file and sampling reproducible; L3 = a second person pans the same sample from this card alone, matching color and order of magnitude, tailings re-pan likewise <10%.

### 16.5 Why Different Ores Need Different Processing Methods

| Mineral class | Representatives | Processing route | Reason |
|---|---|---|---|
| Oxide ores | Malachite, hematite, magnetite, cassiterite | (roasting) → direct carbon reduction | Carbon takes the oxygen in a single step |
| Carbonate ores | Azurite, siderite | Calcine to decompose first → then reduce | Fed to the furnace directly they absorb heat and burst apart, and CO₂ dilutes the reducing atmosphere |
| Sulfide ores | Chalcopyrite, galena | **Roast to desulfurize first** → then reduce | Sulfur in the metal means hot shortness; sulfides cannot be reduced directly by carbon |

[Card 16-02 Roasting for Desulfurization] (eight fields)

1. **Input materials**: sulfide ore (chalcopyrite, galena and the like) crushed to 10–30 mm; firewood and kindling; hand-sorted medium ore (the template method: anything worse than the "fit for the furnace" specimen is picked out); wet grass bundles (to read the fume direction). **Arsenic-bearing ore (garlic odor when hammered) must never enter this firing** — Section 17.8 freezes that whole route (dedicated site, closed kiln, alkaline wash, respiratory protection, urinary-arsenic monitoring; all five before any roasting), and the batch is sealed and registered separately.

2. **Tools required**: stone-slab roasting bed (flat slabs, edges slightly raised); long-handled raking tool (hardwood or iron head on a wooden handle); shovel; sieves (15 / 8 / 3 mm, for sizing after roasting); balance or scale (weight-loss record, Chapter 3); wet grass bundles and a cloth wind vane; batch tags and a roasting record sheet; an upwind working position. Calibration source: the degree of desulfurization cannot be measured with instruments — it is estimated from weight loss, color and looseness together; temperature is not measured but read from whether the bed glows and from flame color.

3. **Sequence and control points** (hand-sort → crush → spread → firewood on top → turn → judge → discharge): ① **Hand-sort** — pick out gangue and intergrown rock with the template method. ② **Crush** — to 10–30 mm; not fine. Control point: fines block the gas path, and too fine a crush sinters easily. ③ **Spread the bed** — 5–10 cm thick on the stone slabs, even throughout. Control point: **never exceed the spread** — a thick bed starves the bottom of air and only distils, it does not desulfurize. ④ **Firewood on top** — lay the firewood over the ore and light from the windward end so the fumes carry the sulfur away. ⑤ **Leave the vents open** — openings along the bed sides and at the four corners; without air it only distils and gives up no sulfur. ⑥ **Turn 1–2 times** — once a crust forms, turn the top to the bottom so unreacted ore meets flame. ⑦ **Time it 2–4 h** — governed by how long the bed stays glowing and by the number of turns. ⑧ **Judge** — color darkened, surface loose and porous, obvious weight loss: done. ⑨ **Discharge** — cool, then sieve; lumps go to smelting, fines are handled separately. ⑩ **Record** — weight loss, time, turns, color. Control point: **work upwind, stand crosswind**; fumes must not drift into the dwelling area.

4. **Empirical parameters and calibration**: roast size 10–30 mm, bed 5–10 cm, 2–4 h (empirical); 1–2 turns; furnace-feed size after roasting 5–20 mm; sieve classes 15 / 8 / 3 mm; for every 10% less gangue the slag is 10% less and 10% of the fuel is saved (empirical). The spread-to-time relation is **empirical and must be calibrated locally**: split the same ore into 2 h / 3 h / 4 h piles, compare color and weight loss, fix the site's "spread–time" class and keep to it. Safety red line: SO₂ is acrid and choking — work upwind, stand crosswind; arsenic-bearing ore (garlic odor) gives highly toxic fumes, the site must lie ≥100 steps downwind of the dwelling area, disposal per Section 17.8.

5. **Observations to record**: batch number and ore type; feed size and bed thickness; firewood quantity; lighting and discharge times (measured within the 2–4 h band); number and times of turning; weight loss (in-weight / out-weight); color and looseness described; fume color and drift (wind vane); lump-to-fines ratio after sieving; operator and standing position (wind).

6. **Pass / rework / scrap criteria**: pass = color darkened, surface loose and porous, obvious weight loss, and the lumps still whole (not crumbling) over the 15 mm sieve; rework = under-roasted (metallic sheen still in the core, color unchanged, little weight loss) — burn again with more frequent turning; scrap = over-roasted and sintered into lumps (surface fused, will not break) — crush them and reuse as return charge, and cut firewood and time on the next batch.

7. **Common failures and diagnosis order** (by frequency): ① under-roasted (most common: bed too thick, too few vents, too little firewood) → thin the bed, open more vents, add firewood; ② surface fused while the core is unchanged (fire too concentrated, too little turning) → turn earlier, spread the firewood; ③ heavy crumbling after roasting (over-roasted or a brittle ore) → less firewood and time, smaller lumps; ④ fumes backing up (wind misjudged, bed downwind of a building) → move the bed to a steady upwind position; ⑤ the operator coughing and weeping (high SO₂, standing downwind) → withdraw upwind at once and wait for the fume to clear; ⑥ roasting on after a garlic odor on hammering (arsenic) → stop at once, seal and register, handle per Section 17.8; ⑦ no metal from the smelt afterwards (insufficient desulfurization or a misjudged ore type) → acid-drop / streak recheck, retry after roasting, and if it still fails apply the Section 16.7 exit criteria.

8. **L1 / L2 / L3 evidence**: L1 = one batch of sulfide ore roasted with a weight-loss record kept, lump color and looseness up to standard; L2 = three consecutive batches whose weight loss and time can be compared, and a smelt that yields a metal bead which forges without hot shortness; L3 = the site's "spread–time–weight-loss" class written up and in the ledger, a second person running the card independently to the same result, and no arsenic-bearing batch left unsealed or unregistered.

**Associated minerals and contaminants**: cassiterite must be concentrated by panning before going to the furnace; arsenopyrite gives a garlic odor when hammered, i.e., it contains arsenic (17.8); pyrite is **forbidden for direct iron smelting** (high sulfur, hot shortness); its proper uses are fire-making (Chapter 6) and, in the long term, acid-making (Chapter 23); **for every 10% less gangue, the slag drops 10% and the fuel saved is 10%** (empirical value) — beneficiation is the first process step of smelting.

### 16.6 From a Handful of Samples to a Sustainable Ore Source

**Four-step evaluation method**:
1. **Grab sampling**: rope-frame grid (1 step square); chip a fist-sized sample (weigh and record 100–300 g) at the center of each cell, ≥9 pieces (3×3); for small outcrops, ≥5 pieces along the strike. Number uniformly and bag;
2. **Two-method grade estimation with cross-checking**: the visual polished-face method (area fraction × coefficient: Cu 0.8, Fe 0.65–0.7, conservative discount) + the quantitative panning method (heavy-mineral fraction; cassiterite fraction ≥20% qualifies as a smelting candidate, empirical value). If the two methods differ by >1x, the panning result is authoritative — go back and examine the visual-estimation bias;
3. **Small smelting trial (decisive)**: 10–20 kg of medium ore → hand-sort and crush into 1–2 kg of concentrate → one crucible trial smelt per Chapter 17. **A grade table is paper evidence; only a smelted metal bead is physical evidence** (Iron Law 4). Enter the yield and fuel consumption into the accounts;
4. **Rough reserve estimate**: outcrop length × width × inferred depth (count only the downward 1/3 of the outcrop, no extrapolation) × density (massive oxide ore 3–3.5; with gangue 2.7–3) × grade. Record as the kg order of magnitude of contained metal (low <50 / medium 50–500 / high >500). Backfill the resource map.

[Card 16-05 Two-Method Grade Estimation] (eight fields)

1. **Input materials**: grab samples — rope-frame grid (1 step square), a fist-sized sample chipped at each cell center, **100–300 g, weighed and recorded**, **≥9 pieces (3×3)**; ≥5 pieces along the strike for small outcrops; all numbered and bagged uniformly (three-tag system, Section 16.10).
2. **Tools required**: balance and weights (Chapter 3, weighing samples), panning pan and still-water trough (16-01), polished face / broken face for inspection, density reference block (fist-sized quartzite, density about 2.6, Section 16.3), record sheet (Chapter 8). Calibration source: the visual estimate rests on area fraction × coefficient; the quantitative figure on the heavy-mineral fraction from panning.
3. **Sequence and control points**: (1) **sample** (grid method, numbered and bagged); (2) **visual polished-face method** — area fraction × coefficient (copper 0.8, iron 0.65–0.7, conservative discount); (3) **quantitative panning method** — heavy-mineral fraction; a cassiterite fraction ≥20% qualifies as a smelting candidate; (4) **cross-check the two** — a difference >1x makes panning authoritative, and the visual bias is examined; (5) small smelting trial (10–20 kg medium ore → hand-sorted and crushed to 1–2 kg concentrate → one crucible trial per Chapter 17); (6) rough reserve estimate (outcrop length × width × inferred depth, counting only the downward 1/3, × density × grade). Control points: both methods are mandatory — one alone gives no conclusion; **a grade table is paper evidence; only a smelted metal bead is physical evidence** (Iron Law 4).
4. **Empirical parameters and calibration**: coefficients copper 0.8 / iron 0.65–0.7 (area-fraction conversion); three visual grades — ore minerals continuous over ≥1/2 of the face is rich (Cu ≥20%, Fe ≥50%), 1/5–1/2 is medium (Cu 8–20%, Fe 30–50%), <1/5 is lean (Cu <8%, Fe <30%); minimum smeltable grade Cu 8% / Fe 30% / cassiterite fraction 10%; density 3–3.5 for massive oxide ore, 2.7–3 with gangue; trial-smelt yield ≥30%; reserve classes low <50 / medium 50–500 / high >500 kg of metal.
5. **Observations to record**: per sample — number / location description / sample weight / visual grade and area fraction / coefficient used / heavy-mineral fraction from panning / difference between the two methods and which was taken / trial-smelt yield and fuel consumption.
6. **Pass / rework / scrap criteria**: pass = the two methods within 1x and grade at or above the minimum smeltable line (otherwise register it under the exit criteria); rework = difference >1x — panning is authoritative, examine the visual bias and revise the personal coefficient before re-estimating; scrap = the average grade of two consecutive sampling days below the minimum smeltable grade (Cu 8% / Fe 30% / cassiterite 10%) — stop or downgrade the registration (exit criterion one).
7. **Common failures and diagnosis order**: (1) the two methods differ by >1x → visual bias or finely disseminated minerals; take panning and re-examine the records; (2) the visual estimate runs high → the conservative discount was not applied; (3) heavy and light not separated in panning → density difference insufficient or sand too coarse (switch this ore to hand sorting); (4) the trial smelt yields no metal → inflated grade or a misjudged mineral class (sulfide not roasted): re-check with acid drop and streak, roast and retry; if it still fails, apply the exit criteria.
8. **L1 / L2 / L3 evidence**: L1 = a 3×3 grid sampled at one occurrence with one grade record from each method; L2 = **≥2 occurrences through the full "sample → two-method grade → register and backfill" cycle, reproducible by a second person (deviation <1 visual grade)**, plus trial-smelt data from 1 occurrence on the books; L3 = the metal-route decision written up (with ≥1 exit-criterion enforcement record) and the sample book, cost ledger, and resource map updated for ≥1 quarter.

### 16.7 How to Judge Whether an Ore Route Is Worth Continuing

**Answer with the cost ledger, not with hope.**

**Unit cost table (per kg of metal, person-hours, empirical values, must be field-calibrated and replaced)**:

| Item | Copper | Iron | Tin |
|---|---|---|---|
| Mining and transport | 5–15 | 8–20 | 10–25 (including panning) |
| Beneficiation | 2–5 | 3–6 | 8–15 |
| Charcoal | 3–6 kg | 6–12 kg | 4–8 kg + flux |
| Smelting and forging | 2–4 | 4–10 | 2–4 |

**Three exit criteria (if any one holds, stop or downgrade the registration)**:
1. **Grade criterion**: the average grade of two consecutive sampling days falls below the minimum smeltable grade (Cu 8%, Fe 30%, cassiterite fraction 10%);
2. **Cost criterion**: the measured total person-hours per kg of metal exceed 3x those of "a stone tool of the same function," and the lifespan advantage cannot amortize the difference within 10 pieces;
3. **Scale criterion**: the visible reserve is "low" class with no sign of extension.

**Continuation criteria (all three required)**: grade on target + trial-smelt yield ≥30% + occurrence within half a day's walk of the worksite.

**Alternative-route boundary (Iron Law 5)**: with no copper, go iron (higher fuel threshold; Chapter 12 must reach L2 first); with no tin, go arsenical copper (highly toxic, small scale only); with no metal ores at all — the stone-and-wood tool system is already a sustainable baseline, and metal comes by long-distance transport and exchange. **This does not count as failure; it counts as honest reporting.**

### 16.8 Mining Engineering: Shallow Pits, Support, Drainage, Ventilation, and Gases (new in v2)

After shallow hand-picking, the vein extends deeper and mining turns from "picking" to "digging." **Digging is the most dangerous production activity at this book's stage** — the four classes of death (collapse, water accumulation, toxic gas, oxygen deficiency) are all more insidious than smelting accidents. The procedures established in this section remain in force throughout Part 4; the unlock conditions for deep mines (shafts and long tunnels) are at the end of this section.

#### 16.8.1 Choosing the Excavation Method (choose the right one before discussing how to dig)

| Method | Applicable to | Limit |
|---|---|---|
| Surface picking and open shallow pits | Outcrop ore, shallow inclined ore | Depth no more than a person (about 1.5–2 m); beyond that, the support procedures apply |
| Open-slope stripping along hillsides | Hillside outcrops | Leave a bench ≥0.5 m wide for every 1 m of slope deepening (against collapse), empirical value |
| Following the ore by drift (horizontal tunnel) | Layered ore entered from flat ground or hillsides | **Initial advance ≤5–8 steps** (limit of natural ventilation); beyond that, dual exits or mechanical ventilation is mandatory |

**Discipline: do not work beneath overhanging rock; do not keep digging deeper inside old workings (tunnels abandoned by predecessors)** — the age of their support is unknown.

#### 16.8.2 Support (timber support, supplied directly by Chapter 7 woodworking)

**Portal frame sets (standard drift support)**:
1. Two posts (hardwood, diameter ≥1 fist, empirical value) stand in post sockets in the two walls of the drift (chiseled half a fist deep);
2. The crossbeam (cap piece) is set on the posts, **beam diameter ≥ post diameter**, and wedged tight against the roof rock face with wooden wedges — drive the wedges at the beam's two ends near the posts, never in the middle (driven in the middle, the beam bends);
3. Set spacing: in sound strata one set every 1–1.5 steps; in fractured zones **close spacing** (beams and posts touching); in extremely fractured zones erect the close-spaced sets before digging (the advance-support concept);
4. **Lagging**: in fractured zones, lay boards / half-round timbers horizontally between beam and roof rock to spread the load; never let the beam bear only on a single loose block;
5. **The sounding-the-walls-and-roof system (mandatory at the start of every shift; ◎ listen to the sound)**: strike the roof and both walls with a hammer — **a crisp ring = intact rock; a dull thud = already delaminated and hanging; it must be pried down or supported first**. Practice method: new and veteran miners strike and judge together, checking their answers against what actually falls; when prying loose rock, stand to the side of and above the block's **fall trajectory**, using a long-handled pry bar.

**Timber cribs (filling mined-out areas)**: stack waste-wood cribs as support in mined-out areas to prevent large-scale collapse — backfilling with waste rock is better still (solving waste-rock storage in passing).

[Card 16-04 Portal Frame Erection] (eight fields)

1. **Input materials**: hardwood posts (**diameter ≥1 fist**); crossbeam (**beam diameter ≥ post diameter**); wooden wedges; lagging (boards / half-round timbers, for fractured zones); waste timber (cribs for mined-out areas).
2. **Tools required**: chisel (post sockets, **half a fist deep**), hammer, saw (Chapter 7 woodworking), pry bar, sounding hammer. Calibration source: post and beam diameters measured in fists, socket depth checked by chisel depth; no instrument — the criteria are "wedged tight, not skewed, no hollow roof".
3. **Sequence and control points**: (1) chisel post sockets in both walls (half a fist deep); (2) stand the posts (hardwood, ≥1 fist) in the sockets; (3) set the crossbeam (beam ≥ post), wedged tight against the roof rock — **drive wedges at the beam's two ends near the posts, never in the middle (driven in the middle, the beam bends)**; (4) in fractured zones add **lagging**, laying boards / half-rounds between beam and roof rock to spread the load — **never let the beam bear on a single loose block**; (5) set spacing by rock character — one set every 1–1.5 steps in sound strata, close-spaced (beams and posts touching) in fractured zones, **close-spaced sets erected before digging in extremely fractured zones**; (6) sound the roof and walls at the start of every shift. Control points: wedges at the ends; advance support is only ever added, never removed.
4. **Empirical parameters and calibration**: post diameter ≥1 fist, beam ≥ post (empirical); socket depth half a fist; spacing 1–1.5 steps in sound rock / close-spaced in fractured rock (master table); the lagging count is judged by "the beam no longer rests directly on loose rock".
5. **Observations to record**: per set — position (advance in steps) / post and beam diameter (fist measurements) / spacing / wedge position (ends or middle) / lagging count / rock class (sound, fractured, extremely fractured) / sounding result.
6. **Pass / rework / scrap criteria**: pass = sockets properly seated, beam ≥ post, wedges at the ends, lagging spreading the load, spacing matching the rock; rework = wedge driven in the middle (beam bending) — **move it to the ends**; spacing too wide — add sets; scrap = beam cracking or post buckling (overload) — evacuate, add sets, re-erect.
7. **Common failures and diagnosis order**: (1) the beam cracks and creaks → overload; check next whether the wedge sits mid-beam (evacuate, add sets, move wedges to the ends); (2) roof rock falling → lagging missing, or the beam bearing on one loose block; (3) posts settling → sockets too shallow or posts too thin; (4) sets skewing → the two wall sockets are not paired, or not cut into solid rock.
8. **L1 / L2 / L3 evidence**: L1 = one portal frame erected to this card and passing sounding; L2 = sets erected continuously at 1–1.5 step spacing along a shallow drift with no collapse for three months (records on file); L3 = the support-material consumption vs. rock-character table in the ledger, and a second person erecting one set from this card alone with spacing and wedge position passing inspection.

#### 16.8.3 Drainage (water is the drift's number-one killer)

1. **Gradient**: leave the drift a slight downhill slope toward the portal (the proportional rule "raise one finger-width per step," Chapter 3) so the water flows out on its own;
2. **Ditch**: dig a drainage ditch along one side of the drift (1 palm deep and 1 palm wide), with the ditch bottom sloped like the drift; clear the sediment once a week;
3. **Water-lifting bucket chain**: lift ponded water from the downhill stretch of the drift by hand with a bucket chain — **the labor of draining 1 bucket of water equals digging 10 baskets of ore** (empirical value); if the inflow rate exceeds the drainage capacity, stop digging (continuing = flooding and collapse);
4. **Water-inrush warnings**: wall seepage turning into a flow, or the water turning turbid (turbid water = carrying sediment = the rock mass is loosening) — evacuate and reinforce immediately;
5. [Long-term hookup] **When deep-mine drainage exceeds human power, that is precisely the first use of the Chapter 28 atmospheric (Newcomen-type) steam engine** (mine drainage pump) — this line on the dependency graph really existed in history.

#### 16.8.4 Ventilation and Toxic Gases (the invisible causes of death)

**The three gas enemies and their criteria (in the era without instruments, rely on the flame and the body)**:

| Gas | Source | Danger | Detection criterion |
|---|---|---|---|
| Oxygen deficiency (insufficient O₂) | Deep drifts, old workings, consumption by decay | Fainting without warning | **Safety lamp / torch method: withdraw as soon as the flame weakens or turns blue** (a flame needs roughly 15% oxygen or more; the flame warns before a person faints — this is the single most important criterion in this chapter) |
| CO | Blasting / fire sources / adjacent burning coal seams | Odorless, causes unconsciousness | Flame normal but people feel headache, dizziness, nausea = CO (Chapter 6 procedures) — at the first headache, everyone withdraws |
| CO₂ (heavier than air) | Low spots in drifts, old workings | Suffocation at high concentration | Lower a torch **into the low spot** to test (if it will not burn when lowered low, gas has accumulated); before entering old workings, lower a torch tied to a rope to probe the bottom first |

**Ventilation procedures**:
1. **Dual exits first**: any drift advanced more than 5 steps must open a second exit (an air shaft); the greater the elevation difference, the stronger the natural ventilation (chimney effect; same principle as 12.1);
2. **Single-exit drifts**: blow air to the working face with a bellows (Chapter 12) through ceramic or leather pipe — keep the pipe outlet behind and to the side of the worker; **deliver the fresh air to the person's nose, not to the fire**;
3. **No blasting before the gunpowder era** — every rock at this stage that "cannot be blasted" is broken by the fire-heat water-quench method: heat the rock face with a firewood fire (about 1–2 h), then splash water on it for a sudden quench; the thermal expansion and contraction cracks the rock for prying (the fire needs ventilation support; after the fire, always wait until the smoke has fully cleared before entering);
4. **The first thing on entering the drift each shift**: torch in front, people following 2 steps behind; work only once the flame is steady.

[Card 16-03 Drift Excavation Safety Procedures] (eight fields)

1. **Input materials**: support materials (posts / beams / wedges / lagging stocked for **≥3 sets**), 2 torches, water-lifting bucket and bucket chain, pry bar, rope; for single-exit drifts, also a bellows with ceramic or leather pipe.
2. **Tools required**: torch (the gas criterion), sounding hammer, long-handled pry bar, chisel (post sockets), bellows (air supply), record sheet. Calibration source: **ventilation has one acceptance criterion only — normal torch flame color at the working face**; set spacing is set by rock character; no instrument.
3. **Sequence and control points**: (1) **enter with the torch leading** — torch in front, people 2 steps behind, in only once the flame is steady; (2) **sound the roof and walls** — at a dull thud, pry and support first, standing to the side of and above the block's fall trajectory; (3) **support before digging** (erect close-spaced sets first in fractured zones); (4) keep the ditch clear (1 palm deep and wide, sediment cleared weekly); (5) **erect one set per set-interval advanced; never advance two set-intervals without support**; (6) mucking synchronized with supporting. Control points: single-exit advance **≤5–8 steps**, beyond which a second exit or mechanical ventilation is mandatory; **stop digging the moment the inflow exceeds drainage capacity**.
4. **Empirical parameters and calibration**: set spacing 1–1.5 steps in sound rock / close-spaced in fractured; post diameter ≥1 fist, beam diameter ≥ post; natural-ventilation limit for drifts ≤5–8 steps; drainage labor ratio **1 bucket of water ≈ 10 baskets of ore**; open-pit bench ≥0.5 m wide per 1 m of depth; fire-heat water-quench 1–2 h, then splash to crack before prying.
5. **Observations to record**: roof seepage and water color (turbid = the rock mass is moving), orientation of wall cracks, torch flame color, personnel sensations (**withdraw at the first headache**), location of dull-sounding zones and their treatment, number of sets erected per shift.
6. **Pass / rework / scrap criteria**: pass = steady flame color all shift, no untreated dull-sounding zone; rework = support lagging — erect sets at once; scrap = the drift itself — **evacuate, seal the opening, register; no forced rescue**.
7. **Common failures and diagnosis order**: (1) the flame weakens and turns blue → oxygen deficiency (everyone out; open a second exit or blow air); (2) water turning turbid → rock mass loosening (withdraw, reinforce, resume after assessment); (3) headache and nausea → CO (stop work, withdraw, ventilate fully and retest before re-entry); (4) beams cracking and creaking → overload or a wedge in the wrong place (evacuate, add sets, move wedges to the ends); (5) a dull-sounding zone spreading → strata delamination (pry loose rock / add sets, support before digging).
8. **L1 / L2 / L3 evidence**: L1 = one supported shallow drift dug to completion with a basket of ore removed safely; L2 = **three months of drift work with no collapse and no gas incident** (records on file); L3 = the support-material consumption vs. rock-character table in the ledger (Chapter 38), and two or more miners passing the blind listening test on sounding.

**Deep-mine unlock conditions (register; forbidden at this stage)**: deep shaft sinking and long tunnels require — (1) mechanical drainage (water-wheel pumps / steam pumps, Chapters 21/28); (2) mechanical ventilation (Chapter 21 fans); (3) hoisting machinery (winches and pulleys, Chapter 21); (4) mature mine lamps and underground fire management. Until all four conditions are in place, **mining stops at this section's boundary**.

---

### 16.9 Panning-Pan Improvement and the Sluice: from Pan-by-Pan Panning to Continuous Concentration

The panning pan is fine beneficiation: one tray of fine sand takes about 1 h. When the throughput is large (river-beach heavy-mineral sand, sheet-like low-grade cassiterite sand), the labor is eaten up first by "hauling water and dumping sand." A sluice = a panning pan stretched to 3–4 steps long, fed continuously and discharging tailings continuously — the heavy-mineral concentrate sinks into the matting gaps by density difference while the light sand is carried away by the water flow. Division of labor: **the sluice does rough concentration (10–30x); the panning pan does final cleaning**.

**Sluice selection and construction**:
- **Box**: pine / fir boards assembled into a trough, 3–4 steps long, 1.5 palms inner width, half a palm deep; caulk the seams with hemp fiber against leakage; widen the feed end slightly into a flare, and fit a movable board at the tail discharge to adjust the water depth;
- **Slope 3–5° (empirical value)**: in erection, raise 2–3 finger-widths (about 4–7 cm) per step of box length, or measure 10 steps of horizontal distance and raise 40–70 cm. Field calibration corrects in both directions according to the symptom: **heavy concentrate running to the tailings (black sand / tin-white grains seen in the tailings) → lower the slope or reduce the water; light sand failing to discharge, sediment building up in the box → raise the slope or reduce the feed**. The two symptoms never appear together; treat concentrate loss first — running to tailings loses values, a silted box only stops work;
- **Matting**: lay one layer of felt or two layers of coarse burlap on the box bottom; the fiber gaps trap the heavy-mineral concentrate. On top of the matting, press a transverse stone or wooden bar every step (bar half a finger high); the eddy zone behind each bar holds concentrate. Without felt, substitute fuzzy dry-grass matting (performance loss: fine-particle recovery drops; compensate by doubling the wash frequency);
- **Water-flow control (diversion weir)**: build a stone weir across the river upstream; leave a notch in the weir crest with a board to lead water into a wooden flume (shallow delivery trough) joined to the box head; **the notch width is the flow knob** — the baseline water depth covers the matting by about one finger-width. Shut down during flood season (flows uncontrolled; safety boundary same as panning).

**Two-stage concentration workflow**: feed −3 mm fine sand at even speed into the box head → the sluice traps the heavy concentrate in the matting and behind the bars → every 2–3 h stop the water once, lift the bars, and wash the matting into a basin to obtain "sluice concentrate" → take the sluice concentrate to the panning pan for final cleaning → sun-dry, weigh, and enter into the ledger. **Before every tailings discard, grab a handful and re-pan it as a spot check** (concentrate-loss check; criteria see card).

**Recovery comparison calibration (Chapter 8 single-variable method)**: weigh one homogenized batch of sample and split it into two equal parts: part A is panned to completion pan by pan; part B goes through the two stages "sluice + panning pan". Sun-dry and weigh the heavy-mineral concentrate from each: **if part B ≥ 90% of part A (empirical acceptance line), the two-stage workflow stands**; if not, troubleshoot and re-measure single-variable in the order slope → water volume → matting. Transcribe the calibrated slope, water depth, and wash cycle into this occurrence's ledger; the next crew may not work from memory.

[Card 16-06 Sluice Construction and Two-Stage Concentration] (eight fields)

1. **Input materials**: pine / fir boards (3–4 steps long, 1.5 palms inner width, half a palm deep, **no through knots**), one layer of felt or two of coarse burlap (fuzzy dry-grass matting where there is no felt), transverse stone or wooden bars (half a finger high), hemp fiber (caulking), wooden flume for the feed; homogenized fine sand **≤3 mm, 20–40 kg per batch**.
2. **Tools required**: saw and chisel (Chapter 7), level line and standard rod (Chapter 3, pulled taut and checked for sag before use), feed shovel, washing basin, panning pan (final cleaning). Calibration source: slope set by "2–3 finger-widths per step" or by measuring 10 steps of horizontal distance and raising 40–70 cm; feed rhythm by the shovel's feel.
3. **Sequence and control points**: (1) **assemble and caulk the box** — water-test it, the bottom must not seep; (2) lay and nail the matting, **one transverse bar pressed every step**; (3) **erect and set the slope** — raise 2–3 finger-widths (about 4–7 cm) per step; (4) **lead in water and set the depth** — the notch width is the flow knob, baseline depth covers the matting by about 1 finger; (5) **drop test grains at the box head** — scatter a pinch of known concentrate; **feeding may begin only once they are held within the first 1/3 of the box**; (6) feed at an even rate (the sand stream unbroken, no dam building); (7) **stop the water once every 2–3 h**, lift the bars, wash the matting into a basin for sluice concentrate; (8) take the sluice concentrate to the panning pan for final cleaning, sun-dry, weigh, enter the ledger. Control points: no feeding while the test grains run through; **grab and re-pan a handful before every tailings discard**.
4. **Empirical parameters and calibration**: slope **3–5°** (concentrate running to tailings: lower the slope; silted box: raise it; **the two symptoms never appear together — treat concentrate loss first**, since running to tailings loses values while silting only stops work); depth about 1 finger over the matting; wash interval 2–3 h; **sluice rough concentration 10–30x**; two-stage acceptance **part B ≥ 90% of part A** (A panned directly, B through both stages); tailings re-pan **<5% of that day's concentrate** (empirical line).
5. **Observations to record**: turbidity of the tail water, color change of the material held behind the bars, how loaded the matting is, where the test grains were caught, each wash time and concentrate weight, tailings spot-check results — into the panning ledger.
6. **Pass / rework / scrap criteria**: pass = test grains held in the first 1/3 of the box and two-stage recovery ≥90% of direct panning; rework = grains not held (lower slope → reduce water → coarser matting, one variable at a time) or a silted box (raise slope / reduce feed); scrap = the box leaks or deforms, or the matting is packed and glazed — **change the matting**.
7. **Common failures and diagnosis order**: (1) concentrate running to the tailings → check slope, then water, then matting, in that order; (2) light sand silting the box → slope too gentle or feed too fast; (3) far less concentrate than on previous days → check whether coarse sand has entered the feed; (4) the box seeps → the hemp caulking has failed, open the seam and re-caulk.
8. **L1 / L2 / L3 evidence**: L1 = one two-stage run completed with a concentrate sample kept; L2 = the recovery comparison record and the calibrated parameters entered in the occurrence ledger; L3 = **three consecutive working days of tailings spot checks (re-pan yield <5% of that day's concentrate) on file**.

### 16.10 Ore-Sample Preservation and Handoff Standards: three tags, dry sealing, and blind-sample rechecks

Every conclusion of an occurrence evaluation hangs on the sample-bag numbers. **One number lost or two bags' batches mixed contaminates the grade ledger and the exit criteria themselves** — a mis-numbered grade can make you shut down a real occurrence or keep a fake one alive. From collection to panning, samples pass through many hands over many days; the system must guarantee that "no link trusts a person, only a number."

**The three-tag system for sample bags**:

| Tag | Location | Content | Medium |
|---|---|---|---|
| Inner tag | Inside the bag | Full number, location, date, sampler | Oiled-paper / birch-bark tag, written in charcoal ink, writing face folded inward against abrasion |
| Outer tag | Hung by cord on the bag mouth | Same as the inner tag | Wooden plaque, scribed marks + charcoal ink, recorded twice |
| Ledger | Camp sample book | Five columns: number + **location description** + date + sampler + visual grade | Transcribed the same day as sampling; may not sit overnight |

- **Three-part numbering: occurrence number - year - serial number** (e.g., "Fe2-Year3-14"); each occurrence keeps its own serial-number book, and they must not be mixed;
- **Moisture-proof dry sealing**: bag the samples only after sun-drying (wet samples mold inside the bag, sulfides reabsorb moisture and oxidize, and the inner tag's writing smears); in the rainy season, spread them on the roasting stone-slab bed to dry with its residual heat, then seal;
- **Anti-mixing compartment boxes**: one numbered box per occurrence, large characters on the box face + compartments inside; **samples move in and out as whole bags** — opening a bag for use requires a deduction column in the ledger, and the remainder returns to the bag with all three tags renewed;
- **Cross-season retained samples (the duplicate-sample system)**: keep ≥1/3 of each sample as a duplicate, dry-sealed separately into the duplicate box. Three uses: rechecking disputed grades; letting newcomers practice on reference samples at seasonal handovers; checking for drift in panning technique;
- **Blind-sample recheck system (≥1 time per quarter)**: draw ≥3 bags from the retained samples, erase their numbers, and hand them to **someone who took no part in the original sampling** to re-pan and re-estimate the grades; then reveal the tags and check against the ledger. Pass = deviation ≤1 visual-estimation grade; if out of tolerance, troubleshoot in the order "mixed samples → technique drift → ledger error"; **until the cause is found, all grade data for that occurrence are suspended** — exit criteria must not be built on suspect data.

[Card 16-07 Sample Three-Tag System and Blind-Sample Recheck] (eight fields)

1. **Input materials**: woven sample bags (Chapter 15), two oil-paper / birch-bark tags plus one wooden tag, charcoal ink, number box and duplicate box.
2. **Tools required**: knife, pen, sample book (Chapter 8 record template), residual heat of the roasting stone-slab bed (for drying in the rainy season). Calibration source: the recheck pass line is the larger of **the team's own technique-noise baseline** and 1 visual grade.
3. **Sequence and control points**: (1) at the sampling site write the **inner tag** and put it in the bag (full number, location, date, sampler; writing face folded inward against abrasion); (2) close the bag and attach the **outer tag** (wooden tag carrying both a cut notch and charcoal ink); (3) **copy the five ledger columns the same day** (number + location description + date + sampler + estimated grade — never left overnight); (4) sun-dry, bag, dry-seal and place in the number box (**bags in and out whole**; record any opening in the deduction column and re-tag what is left); (5) keep **≥1/3 as a duplicate** in the duplicate box; (6) **each quarter draw ≥3 blind bags** — strip the numbers, hand them to someone who did not do the original sampling to re-pan and re-estimate, then break the tags and compare with the ledger. Control points: the three-part number (occurrence-year-serial), one serial book per occurrence, never mixed; one box per occurrence, no loose bags mixed together.
4. **Empirical parameters and calibration**: three-part numbering; duplicate ≥1/3; ≥3 blind bags per quarter; recheck pass line **deviation ≤1 visual grade**; calibration method — two experienced hands pan the same sample three times each, their spread is the team's technique-noise baseline, and the recheck line is the larger of that baseline and 1 visual grade.
5. **Observations to record**: the five ledger columns, the duplicate-box inventory, the quarterly recheck comparison table, the deduction column, the wet/dry state of the bags.
6. **Pass / rework / scrap criteria**: pass = the three tags agree + all five ledger columns present + **the location description walks you back to the sampling point**; rework = a missing tag or column made good the same day (a column that cannot be recovered is marked "missing" honestly); scrap = the number is illegible with no ledger entry — the sample is void, re-take it from the ledger description; when a recheck is out of tolerance and the cause is not yet found, **all grade data for that occurrence is suspended**.
7. **Common failures and diagnosis order**: (1) writing blurred → check whether dry sealing was done (damp bags grow mold, sulfides re-absorb moisture, the inner tag smears); (2) two bags with the same number → check whether two people each kept their own serial book; (3) recheck out of tolerance → work through sample mix-up → technique drift → ledger error, in that order; (4) a lost tag causing a batch mix-up → walk back to the sampling point using the ledger description, check rock character and piece count, void the batch and re-take it.
8. **L1 / L2 / L3 evidence**: L1 = **9 consecutive bags (one complete 3×3 grid set) with all three tags in order**; L2 = one complete blind-sample recheck record on file; L3 = the cross-season duplicate handover list and the new-hand sample-comparison practice records on file.

### 16.11 Open-Pit Bench Design Details: classing, advance direction, post-rain inspection, and slope reduction with reclamation

The 16.8 rule "leave a 0.5 m wide bench for every 1 m dug deeper" is a single rule; once a mining block is worked as a contiguous area, benches must be designed by rock class — otherwise the design is either overly conservative (excess benches at every step) or reckless, courting landslides.

**Bench class table (empirical values. A new block always starts one class higher; the class may be lowered only after 3 consecutive operating days of sounding with no dull sounds and no spalling on the slope face)**:

| Rock character | Single bench height | Bench width (doubles as the working platform) | Remarks |
|---|---|---|---|
| Hard massive rock (must be broken by fire-heat water-quench) | ≤2 m | ≥1.5 m | A near-vertical slope face can be held short-term |
| Semihard layered oxidized ore zone | ≤1.5 m | ≥2 m | The domain where the single 16.8 rule applies |
| Soft rock and thick overburden (laterite / residual-slope deposits) | ≤1 m | ≥3 m | Slope angle ≤45°; bringing soft soil down to 35° is more stable |

**Working-face advance direction (along the bedding, never across it)**: before breaking ground, measure the strike of the bedding — stretch a cord straight along the bedding plane, plant stakes at both ends, and take the direction with the standard rod (Chapter 3 method). **Keep the bench slope face's strike as parallel to the bedding strike as possible (advance along the bedding)**; a slope face "lying" on a full rock bed is most stable. When the slope face cuts across the bedding's end faces (advance across the bedding), the rock mass is like a slant-stacked pile of stone slabs with an edge pulled away — the probability of bedding-plane sliding collapse rises sharply. Disposition: in cross-bedding sections, drop the bench one class and widen it by half a step. Mnemonic: **slope and seam parallel means along the bedding; slope and seam crossing means drop a class first**.

**Post-rain slope inspection checklist (when the rain stops, inspect first and resume work second; no resumption without an inspection — discipline at the same level as 16.8's "the first thing on entering the drift each shift")**:
1. **Tension cracks at the slope crest**: before the rain, drive two stakes across each crack at the crest, tie a crossbar between them, and mark with scribed lines; at inspection, measure the crack width — **if it has grown >1 finger-width (about 2 cm) versus before the rain, close the slope and evacuate**;
2. **Seepage at the slope toe and on the bench faces**: slow, clear seepage may be kept under observation; **seepage turning turbid (carrying sediment = the slope mass is moving inside) means withdraw immediately**;
3. Bench-face subsidence and offset: a new offset >half a fist closes that bench;
4. The toe of old waste-rock piles: bulging or fresh slip marks means setting an exclusion zone at the toe (3 m);
5. The inspection's five columns (date / crack-width reading / seepage clear or turbid / spalling amount / inspector) enter the ledger.

**Bench slope reduction and reclamation registration (Chapter 49 interface)**: when a block is worked out, no vertical walls are left — cut the slope down into a stair-stepped profile from the top, bringing the slope angle to around 35° in soft-soil sections; the topsoil stockpiled separately during stripping is spread back over the slope and bench faces (**spread-back thickness ≥2 finger-widths**, empirical value), willow cuttings are planted and local grass seed scattered to protect the slope; ponded depressions on the pit floor are registered as water sources or backfilled with waste rock. **Reclamation is engineering, not virtue**: a vertical wall plus a loose waste-rock pile will not survive one rainy season; landslide injuries and the silting-over of downstream water sources are bills that come due later. Register four items per block: the slope-reduction completion date, the measured slope angle, the topsoil spread-back thickness, and the vegetation measures — entered into the Chapter 49 site and occupational health ledger.

### 16.12 Mercury: Cinnabar Identification and Unlock Procedures (the sole legitimate source for the mercury line of Chapters 33/27)

Chapter 33 (mercury displacement pump / McLeod gauge) and Part B of Chapter 27 (mercury barometer) use mercury as a raw material — **the mercury line is unlocked by this section; the "no mercury" wording in all other chapters means "forbidden until this section's procedures have been completed."**

- **Cinnabar identification**: scarlet red, scarlet streak, high specific gravity (heavy heft in the hand), powder extremely heavy — distinguish it from hematite (cherry-red streak);
- **Roasting distillation**: mix crushed cinnabar grains with charcoal powder in a sealed ceramic retort (refractory base mix) and heat it in an external furnace to dull red — the mercury vapor passes down the outlet tube and condenses underwater into the receiving bottle (the bottle sits in cold water); **entirely outdoors, crosswind, two people**;
- **Sealed storage**: thick-walled ceramic bottles with double lids sealed in clay, red lettering on the body, a dedicated cabinet with a dedicated lock; dispense only using a shallow tray (Chapter 33 discipline);
- **Spill disposal**: cover and collect with sulfur powder (Chapters 33/53 cards);
- **Monitoring**: operators register the three signs — gums / tremor / personality — monthly (Chapter 53 observation-items table);
- **Red line**: until this section's procedures are fully built, the Chapter 25 thermometers, the Chapter 26 reagents, and the Chapter 33 vacuum parts all keep the "no mercury" wording.

## Master Parameter Table

| Parameter | Value | Class |
|---|---|---|
| Furnace-feed ore size | 5–20 mm | Specification |
| Screen grades | 15 / 8 / 3 mm | Specification |
| Tailings re-pan acceptance | Second pass <10% of the first | Criterion |
| Grade coefficients | Cu 0.8 / Fe 0.65–0.7 (converted from area fraction) | Empirical |
| Minimum smeltable grade | Cu 8% / Fe 30% / cassiterite fraction 10% | Empirical criterion |
| Mining-depth benches | 0.5 m wide left per 1 m dug deeper | Empirical |
| Support set spacing | Sound 1–1.5 steps / fractured close-spaced | Empirical |
| Post/beam diameter | Post ≥1 fist, beam ≥ post | Empirical |
| Drift natural-ventilation limit | Advance ≤5–8 steps | Empirical |
| Drainage labor ratio | 1 bucket of water ≈ the labor of 10 baskets of ore | Empirical |
| Roasting | 10–30 mm spread 5–10 cm, 2–4 h | Empirical |
| Sluice slope | 3–5° (raise 2–3 finger-widths per step, or 40–70 cm per 10 steps) | Empirical |
| Sluice water depth and wash cycle | Depth covers the matting by about 1 finger-width; wash once every 2–3 h | Empirical |
| Two-stage concentration acceptance | Sluice recovery ≥90% of direct panning; tailings re-pan <5% of the concentrate | Empirical criterion |
| Blind-sample recheck | ≥3 bags per quarter, deviation ≤1 visual-estimation grade; out of tolerance suspends that occurrence's grade data | System criterion |
| Bench classes (height/width) | Hard rock 2 m/1.5 m; semihard 1.5 m/2 m; soft soil 1 m/3 m | Empirical |
| Post-rain resumption | Inspect first, resume second; crest crack growth >1 finger-width closes the slope | Criterion |
| Reduced slope angle | Soft-soil sections brought to around 35°; topsoil spread back ≥2 finger-widths | Empirical |

## Failure Modes and Diagnosis

| Symptom | Candidate causes (by probability) | Verification | Disposition |
|---|---|---|---|
| Panning fails to separate heavy from light | Density difference insufficient / sand too coarse | Re-check by heft; re-screen and re-measure | Gravity separation unsuited to this ore; switch to hand sorting |
| Visual grade and panning differ by >1x | Visual-estimation bias / minerals finely disseminated | The panning method is authoritative | Re-examine the visual-estimation records; revise the personal coefficient |
| Small smelting trial yields no metal | Grade overestimated / mineral class misjudged (sulfide not roasted) | Re-check by acid drop / streak | Roast and retry; if it still fails, execute the exit criteria |
| Flame weakens in the drift | Oxygen deficiency | Torch method (the sole criterion) | Everyone withdraws; open a second exit / blow air |
| Personnel headache and nausea | CO | Stop work and withdraw | Ventilate until clear, re-test, then re-enter |
| Dull-sounding roof zone expanding | Bed delamination | Sound the walls and roof | Pry loose rock / add sets; support before digging |
| Support beam cracks and creaks | Overload / wedge placement error (driven at mid-beam) | Inspect the wedge positions visually | Evacuate and add sets; move the wedges to the two ends |
| Water turns turbid | Rock mass loosening, carrying sediment | Observation records | Withdraw and reinforce; resume after assessment |
| Roasted ore sinters into lumps | Over-roasting | Visual inspection | Break up and reuse; reduce firewood and time next batch |
| Sluice matting compacts and fails | Heavy concentrate left full beyond 2–3 h without washing / matting compressed to a glossy surface | Drop test grains at the box head; see whether they are trapped in the head 1/3 | Stop the water and wash the matting; a glossy fabric surface means replace it and shorten the wash interval |
| Lost sample tags cause batch mixing | Inner tag damp, writing smeared / transfer without compartment boxes, loose bags mixed together | Return to the sampling point per the ledger's location description and verify rock character and piece counts | Void and retake that batch; switch to dry sealing + numbered boxes with whole-bag movement |
| Bench over-excavation landslide | Greed — dug a full two classes of height in one go / resumed after rain without inspection | Measure bench height and width against the class table; check the crest cross-crack marker readings | Withdraw, cut the slope back to unload, rebuild per the class table; crack growth >1 finger-width closes the slope |

## Process Card Index

Cards 16-01 to 16-07 are all full eight-field cards, each copyable onto a single page.

## Acceptance Standards

- **L1**: field discrimination of all eight ores against the streak table (≥1 physical specimen each); one pan of heavy-mineral panning meeting standard (tailings re-pan <10%); one supported shallow drift dug to completion with one basket of ore removed safely.
- **L2**: ≥2 occurrences complete the full "sampling → two-method grade → registration and backfill" workflow, reproducible by a second person (deviation <1 visual-estimation grade); 1 occurrence completes a small smelting trial with the data entered into the accounts; three consecutive months of drift work with no collapse and no gas incidents (sounding and torch records on file).
- **L3**: the metal-route selection conclusion in writing (including ≥1 record of an executed exit criterion); the sample book, cost account, and resource map updated in sync for ≥1 quarter; support material and crushing hammer wear on the books; two or more miners pass the blind-listening sounding assessment. Evidence: the three tables and one book, incident (or zero-incident) records, and assessment records.

## Labor Hours, Manpower, and Consumption

| Item | Manpower | Labor hours (empirical values) |
|---|---|---|
| One day of prospecting and tracing | 2 people | 1 day |
| Crushing one basket of medium ore (20 kg) | 1 person | 0.5 day |
| Panning one tray | 1 person | 1 h |
| Full evaluation of one occurrence | 2 people | 2–4 days (small smelting trial excluded) |
| Shallow drift advance (including support) | 2–3 people | about 1–2 days per 1 step advanced (depends on rock character; needs calibration) |
| Consumption | Support timber, firewood, torches | entered into the Chapter 38 ledger |

## Safety Boundary

- Sampling forbidden beneath cliffs and landslide masses and in the depths of old workings; pit sampling always 2 people together; withdraw the moment the pit wall becomes unstable.
- Crushing splash: keep everyone out of the 3 m fan around the anvil bench; crush quartz-bearing ore **wet** (spray water against silica dust — silicosis is the number-one chronic killer of miners on a twenty-year scale, Iron Law 7; the protection system is in Chapter 49).
- SO₂ from sulfide-ore roasting and arsenic-bearing fumes: operate upwind, stand crosswind; arsenic-bearing sites ≥100 steps downwind of dwelling areas.
- Keep lead ore dust out of the mouth and away from food; wash hands after handling.
- Panning never touches flood-season rapids.
- **Drift red lines**: support before digging; torch in front, people behind; a dull sound means pry first; a headache means withdraw; an inrush or turbid water means withdraw. **No ore is worth a life.**

## A. Existing Tools List

Chapter 2 resource map and identification cards; Chapter 3 standard rod, balance, and error records; Chapters 5–7 stone tools, woodworking, and rope; Chapter 8 experiment and marking system; Chapter 9 workbench, grinding bench, and templates; Chapters 10 and 15 transport and weaving.

## B. New Tools Added in This Chapter

Wooden panning pan; three grades of woven screens; crushing bench (stone anvil + guards + stone hammer set); rope-frame sampling grid; density reference block and water-bag displacement cylinder; ore sample bags and sample book; occurrence evaluation ledger (three tables: grade / cost / reserves); roasting stone-slab bed; **portal frames, lagging and wooden wedges, pry bar**; **drift drainage ditch and water-lifting bucket chain**; **ventilation ducting and the torch inspection procedure**; **the sounding-the-walls-and-roof system and the blind-listening assessment**; the fire-heat water-quench breaking method; the deep-mine unlock conditions registration sheet; **the full sluice set (box + felt/coarse-cloth matting + cross-bars + delivery flume and diversion weir)**; **the three-piece sample tag set (inner tag / outer tag / ledger five columns), the numbered box and the duplicate box**; **slope cross-crack marker stakes (two stakes, crossbar, scribed lines) and the post-rain inspection checklist**; the four-item slope-reduction and reclamation registration (Chapter 49 interface).

## C. Unresolved Dependencies

Quantitative chemical composition (Chapters 23 and 26); deep prospecting and deep-mine mining (the four unlock conditions, see the end of 16.8); hydraulic ore crushing (Chapter 21); discriminating and using the tungsten and tantalum associated with cassiterite (long term).

## Next-Step Dependencies

Chapter 17: concentrate enters crucible smelting. Chapter 18: iron-ore evaluation feeds bloomery furnace charging. Chapters 20 and 21: iron hammers and iron drills, together with mechanical drainage, push mining toward the depths. Chapter 28: the steam drainage pump = the first puzzle piece of the deep-mine unlock (the historically true order). Chapter 38: support timber and miners' labor hours enter the accounts. Chapter 49: occupational exposure registration and medical examination systems for silica dust, arsenic, and lead.
