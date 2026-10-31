# Chapter 40: Alternative Routes, Degraded Operation, and Disaster Redundancy

## Chapter Objectives

After reading this chapter, the settlement should produce four documents:

| Document | Content | Use |
|---|---|---|
| Alternative route register | Four-column registration for every alternative route (performance loss / resource cost / applicability boundary / final bottleneck) + trial-production evidence | When a main resource is missing, know what to switch to, how much is lost, how long it can run, and where it counts as safe |
| Degraded-operation plan set | Trigger criteria for every critical line (linked to the Chapter 38 three-color lines) and switchover action lists | In a crisis, switch by the book, not by improvisation |
| Annual degraded-operation drill record | Once a year, actually stop one line for 24 h per the plan: five-column record plus rectification and closure | Proves the plan is not a paper exercise |
| Six-disaster recovery cards and stand-in boards | Reserves, bypasses, and recovery order for drought / flood / fire / epidemic / mine disaster / critical equipment failure; stand-in arrangements for critical posts | Recover by the card after disaster: save people first, then food and fuel, machines last |

## Capability Boundaries

**Can do:**

- Build a substitution matrix for the five classes of critical resources — fuel, ore, power, materials, processes — registering every alternative in four columns, with temperature, lifespan, precision, and hazard boundaries stated item by item (Section 40.2).
- Write a "drop one tier and still run" plan for every critical production line: trigger criteria, switchover time limit ≤48 h, exit conditions (Section 40.3).
- Establish reserve lists, bypasses, and post-disaster recovery priorities for the six disasters, and test them with annual drills (Sections 40.3.3, 40.4, 40.5).

**Cannot do:**

- Cannot declare a nonexistent alternative feasible. If the territory holds no peat, no coal, no copper ore, the corresponding matrix cell can only say "no route" — "theoretically obtainable in trade from afar" does not fill the cell. Iron Law 5: never claim complete substitution on the grounds that a thing exists in theory.
- Cannot predict when a disaster arrives. Every reserve and plan in this chapter only shortens "minimum post-disaster downtime"; redundancy is not immunity.
- Cannot replace the Chapter 39 maintenance system or the safety procedures of the process chapters. This chapter governs "after it breaks, in what order to switch and into what"; it does not govern "how to keep it from breaking."
- Cannot guarantee an undrilled plan works. Any plan that has not been through one drill is treated as a draft and does not count toward acceptance.

**External dependencies (counted on the Class-C list):**

1. Chapter 38 ledgers with ≥1 quarter of continuous stock flows — the sole data source for the three-color lines.
2. Chapter 39 spare-parts ledger and inspection records — the basis for the "critical equipment failure" disaster entry.
3. Chapter 37 skills matrix and work schedules — proof that every degraded route "has someone who can run it."
4. Chapter 2 resource survey records of grade, reserves, and round-trip haul distances for substitute resources.

**Four-column format (the only core table format in this chapter, applied uniformly to all alternative routes throughout the book):**

| Column | Must answer | Passing standard (adjectives alone are not allowed) |
|---|---|---|
| Performance loss | How much is lost after substitution | Give numbers: furnace temperature down how many °C, precision down how many grades, lifespan down how many tenths, labor up how many times |
| Resource cost | What extra it costs | Give unit consumption and labor: extra fuel, manpower, and haul distance per ton of product |
| Applicability boundary | Where it counts as safe | Give upper limits: temperature, load, lifespan limit, contact media, hazard properties (sulfur, CO, brittle fracture) |
| Final bottleneck | What the downgrade ultimately is | Name the level "below which there is no substitution," and which chapter the whole technical chain falls back to when it is lost |

## Pre-Work Verification

Checklist style. If any item fails, the corresponding plan can only be marked "draft" and may not enter drills or acceptance.

| # | Verification item | Criterion (confirm you hold ××; the standard is ××) |
|---|---|---|
| 1 | Ledgers running | The Chapter 38 ledgers show ≥1 quarter of continuous flows for hardwood charcoal, iron ore, refractory clay, grain, and water; the three-color thresholds are agreed and posted |
| 2 | Substitute resources on record | The Chapter 2 resource maps can answer whether the territory holds softwood stands, coal, peat, lean ore, or substitute clays, with grades and round-trip labor hours; where a check finds none, fill "no route" in the matrix |
| 3 | Critical-line list | Every line annotated with "consequences of 7 days stopped"; any line whose 7-day stoppage harms drinking water, food, or fuel, or ruins a furnace body, falls within plan scope |
| 4 | Skills matrix valid | Card 37-03 quarterly review unexpired; ≥2 operators at Level 2 for every degraded route intended for use |
| 5 | Spare parts and plan boxes | Chapter 39 spare-parts ledger checkable; each plan's box sealed intact, most recent inspection within 90 days |
| 6 | Disaster history and terrain | Records on paper of drought, flood, fire, epidemic, and mine disasters over the past 10 years (oral accounts acceptable); written criteria for the relation between flood level and settlement elevation |
| 7 | Decision authority posted | Who may declare degradation (workshop supervisor + accountant, dual sign-off) and who may lift it (adding the three-item re-verification set) is posted; three names in succession on the disaster-time chain of command |
| 8 | Drill budget | The annual production schedule has reserved the capacity and rations for drill stoppages (Section 37.3), not squeezed them out of the busy farming season or overdrafted them from grain stores |

## 40.1 Institutionalizing Alternative Routes

### 40.1.1 Iron Law 5 at the Operating Level: Register First, Use Second

Iron Law 5 requires every alternative route to state its performance loss, resource cost, applicability boundary, and final bottleneck. This chapter turns that into a hard process step:

1. **Unregistered substitutions must not enter production.** Any substitute material or substitute process entering production for the first time must first pass the Card 40-01 four-column registration plus trial production. Unregistered substitution is handled as an out-of-control change per Section 37.6.3 — that batch's output is treated as unfinished process work and may not be accepted (Iron Law 6).
2. **Registration requires dual sign-off and a time limit.** Dual signatures of the baseline process card holder (Level 3) and the workshop supervisor; the approval field must state the boundary of use and the time limit (in months). An approval without a time limit counts as no approval.
3. **Substitute batches must be marked.** Substitute batches are stamped on the blank or tagged, and stored in a dedicated warehouse zone; the accounting office's requisition form gains a "substitute" column. A substitute batch with missing marks is handled as a material-mixing incident.
4. **A column that cannot be filled = unverified.** Any column lacking measured figures is written "unverified"; such a substitution may be trial-produced but not put into production.

Why raise the bar this high: the danger of alternative routes lies precisely in their "seeming to work." Registration is not meant to block substitution but to make every substitution happen inside known boundaries — **substitution buys time in the crisis; boundaries keep people alive.**

### 40.1.2 "Substitution ≠ Equivalence": Three Historical Counterexamples

What the three counterexamples share: none of the mismatches exploded on the spot; they surfaced late — classic silent failures (Iron Law 6).

**Counterexample 1: common clay passed off as fire clay → furnace burn-through.** Common clays withstand about 1150–1300°C; refractory clay ≥1580°C; the slag-line interface in bloomery and blast furnaces runs 1350–1500°C. The first heat often "looks like a success" — the new lining is still in its sinter-hardening period, outwardly unremarkable. By heats 2–5 the inner wall vitrifies and spalls in sheets; at heats 3–8 the slag line punches through, molten iron and slag pour through the furnace bottom, burn out the blast pipes, the wooden frame, and the nearby sheds, and injure people directly. Before-use criterion: the side-by-side test-bar bend-over method (Section 40.2.4). In-service criterion: after each heat cools, check the slag-line area; at the first bright glaze flow marks, take that lining out of service immediately. **Boundary: common-clay-plus-grog substitute mixes are permitted only for outer layers, flues, and interfaces below 1200°C.**

**Counterexample 2: pig iron passed off as wrought iron → brittle fracture.** Pig iron carries >2% carbon, under one-fifth the impact toughness of wrought iron. The two look nearly identical, and under static load pig iron even works — so it gets made into hooks, axles, and chains, load-bearing parts subject to impact and bending. Weeks to months later they snap without warning, and falling loads injure people. Before-use criterion: load-bearing parts are accepted only by test-bar fracture and a 90° hammer bend without cracking (fracture criteria of Chapters 18–19: pig iron fractures with coarse bright crystalline grains; wrought iron shows a fibrous dull-gray surface); the ◎ strike-and-listen test (pig iron sounds dull, wrought iron rings clear) is for initial screening only. Practice method: 20 strikes each on bars of known type. Misjudgment compensation: always rule on the fracture of a broken test bar; never conclude from sound alone. **Boundary: pig iron is permitted only for static-load parts, counterweights, and pots and cauldrons (the cast-iron boundary of Chapter 18); every load-bearing and impact-bearing use is forbidden.**

**Counterexample 3: softwood charcoal passed off as hardwood charcoal → furnace temperature collapse.** Softwood charcoal holds 60–75% fixed carbon (hardwood 75–85%), 30–40% lower bulk density, and burns fast. The same dou of charcoal gives a softer fire and drops furnace temperature 50–150°C; the bloomery furnace falls below the lower limit of reduction temperature, slag inclusions in the bloom multiply, and the fuel ratio worsens 20–40%. The most insidious part is on the books: the wood is still burning and charcoal still coming out, but the iron yield falls heat after heat — the fuel ledger shows nothing wrong; only the furnace-condition ledger can. Before-use criterion: the ◎ heft-and-ring test (softwood charcoal is light with a dull knock). Practice method: 30 hefts each on known samples of both. Misjudgment compensation: fill a 1 L graduated cylinder with charcoal and weigh it; <200 g/L rules it softwood charcoal, to be used within the softwood-charcoal boundary. **Boundary: softwood charcoal is approved for forging, annealing, pottery kilns, and heating; shaft furnaces must first pass a co-firing test and enter the register (Section 40.2.1).**

Read all three counterexamples the same way: **each substitution's "equivalence" holds only inside the boundary written in the register; one step past it, the substitution turns from a life-saving fallback into a delayed-action bomb.**

### 40.1.3 Maintaining the Register

- **Annual re-verification**: each year, draw ≥1 registered substitution and redo its comparative trial production; whenever ore sources, forest stands, or water flows change (especially drastic in the Chapter 50–53 environments), rewrite the matrix immediately.
- **Archival custody**: the register, trial pieces, and records fall under the Chapter 43 archive system; the register and the Chapter 38 ledgers cross-check each other — any requisition for an unregistered substitute appearing in the ledger is a violation event, pursued under Section 37.6.3.
- **Delisting condition**: an alternative route uncited for two consecutive years (in a drill or a real activation) drops to "historical record" and must be trial-produced anew before reuse.

[Card 40-01 Alternative Route Registration Card] (eight fields)

1. **Input materials**: the baseline route's process card and parameter sheet; substitute resource samples (fuel ≥20 kg; ore and clay ≥50 kg); ledger pages and batch markers (stamping punch or hang tags).
2. **Required tools**: scales (Chapter 3; cross-check zero point and full scale against standard weights); a test furnace or trial workstation; test bars and fracture criteria (Chapters 18–19). Those using flame-color temperature judgment (◎) must hold certification per the Chapter 12 practice records.
3. **Operating sequence and control points**: ① state the baseline and the intended substitution (which process step, which temperature/load interface); **② fill the four columns item by item; any column lacking measured data is written "unverified," and that substitution may not enter production**; ③ trial-produce ≥3 pieces, recording parameters and rejections; **④ dual sign-off on the boundary of use and the time limit (in months); no time limit counts as no approval**; ⑤ assign a number, enter the register, and send a copy to the accounting office to open the "substitute" requisition column.
4. **Empirical parameters and calibration methods**: performance loss is measured by comparative trial production (substitute batch and baseline batch judged by the same criteria and the same referee); sulfur risk by the three-bar 90° bend method (Section 40.2.1); refractoriness by the side-by-side test-bar bend-over method (Section 40.2.4); bulk density by weighing a 1 L graduated-cylinder fill, ×3, taking the median.
5. **In-process observation records**: trial piece numbers, boundary violations (must be zero), actual material consumed, pieces rejected, and the handler of each column's data.
6. **Pass / rework / scrap criteria**: pass = all four columns carry measured data and ≥3 trial pieces conform; rework = the boundary column says "as circumstances allow" or the time limit is missing (refill, then re-trial); scrap = approved for use without trial production, or put into production despite rejected trial pieces.
7. **Common failures and troubleshooting order**: substitute mixed into the main product → first check batch marks → check warehouse zoning → check the requisition form's "substitute" column; performance column contradicts measurements → first check whether another settlement's numbers were copied → redo the comparative trial production.
8. **L1 / L2 / L3 evidence**: L1 = registration page with all four columns filled; L2 = registration page + 3 trial pieces or their rejection records; L3 = annual re-verification record + citation records from drills or real activations (which degradation used it, and the function retention rate).

**Blank register page (for copying the card):**

| Route name / number | Baseline | Performance loss | Resource cost | Applicability boundary | Final bottleneck | Approval dual sign-off / time limit | Annual check date |
|---|---|---|---|---|---|---|---|
| | | | | | | | |

## 40.2 Substitution Matrix for Critical Resources

The matrices in this section are the master templates of the register: each settlement prunes them to the territory's actual resources and copies each line into Card 40-01 for registration. The values in the tables are empirical and must be field-calibrated by the calibration methods and filled back in; a column whose calibration is unfinished is written "unverified".

### 40.2.1 Fuel Matrix

| Tier | Key indicators (empirical; sample and calibrate) | Performance loss | Resource cost | Applicability boundary | Final bottleneck |
|---|---|---|---|---|---|
| Baseline: hardwood charcoal | Heating value 29–32 MJ/kg; fixed carbon 75–85%; bulk density 250–400 kg/m³ | — | Coppice rotation 30+ years; 1 kg charcoal costs 4–6 kg wood (Chapter 6) | All high-temperature processes | Forest standing stock (Section 37.2.2) |
| Softwood charcoal | Heating value 26–30 MJ/kg; fixed carbon 60–75%; bulk density 150–250 kg/m³ | Shaft furnace temperature down 50–150°C; heat per unit volume down 30–40%; fuel ratio worsens 20–40% | Rotation period 10–20 years; recovers fast | Forging, annealing, pottery kilns, heating; shaft furnaces require a co-firing test and registration | Temperature ceiling — metallurgy still viable, large glass furnaces marginal; below this, no charcoal-class substitute remains |
| Bituminous coal | Heating value 20–30 MJ/kg; sulfur 0.5–3%; volatiles 20–40% | Sulfur in iron above 0.1% means hot shortness; cracks under the hammer | Haul distance from the pit head; ironmaking requires prior pile coking (yield 50–70%) | Lime kilns, brick and pottery kilns, boilers (flue required); for ironmaking, low-sulfur coke only | Iron smelted from high-sulfur coal cannot be forged — the bottleneck is the feed, not the furnace |
| Peat (air-dried) | Heating value 8–14 MJ/kg; moisture 30–50%; ash 5–15% | Fire temperature ceiling about 1100°C | Drainage and sun-drying take an entire summer, 2–3 person-days/t | Heating, cooking, drying green ware; lime kilns require pre-drying to <25% moisture | Temperature ceiling — no metallurgy or glass continues past it |
| Direct-fired firewood | Heating value 13–16 MJ/kg (air-dried) | Kiln temperatures reach 950–1100°C; tar and moisture disturb the reduction zone in shaft furnaces | Saves the charcoaling step, but consumes 4–6 times the wood volume | Pottery kilns, brick kilns, heating | Shaft furnaces still need charcoal — direct firing cannot replace iron smelting |

**Sulfur test-iron calibration (mandatory for every new coal pit)**: sample 20–30 kg, coke it, smelt a batch of test iron per the Chapter 18 process, forge 3 test bars and bend them 90°: all cracked → that coal is banned from ironmaking for life; hairline cracks → castings only; no cracks → admitted and entered in the register. Never judge sulfur by smell — most sulfides are odorless; hot shortness does not recognize noses, only test bars.

### 40.2.2 Ore Matrix

| Grade | Pre-treatment | Fuel ratio (charcoal:iron, empirical) | Added labor hours | Boundary and final bottleneck |
|---|---|---|---|---|
| Rich ore ≥50% | Hand-pick waste rock, then charge directly | 4–6:1 | — | Baseline tier |
| Medium ore 40–50% | Hand sorting (0.5–1 t/person-day) | 5–8:1 | Sorting counts as 1–2 person-days/t iron | May be charged only with waste rock under 10% |
| Lean ore 30–40% | Crush to 10–25 mm (0.2–0.5 t/person-day) + panning to raise grade 5–15 percentage points, recovery 70–85% | 6–12:1 | Sorting counts as 3–8 person-days/t iron | Slag volume rises steeply and lining wear roughly doubles — must be computed together with the Section 40.2.4 refractory account |
| Grade <20% | — | — | — | **Bloomery economics collapse**: fuel and labor invert. The answer at this tier is a new ore source or a beneficiation process built first, not stubborn smelting |

Calibration: take 3 samples of 5 kg each per ore point, crush and homogenize, trial-smelt in a small furnace; iron yield = iron weight ÷ ore weight; if the three samples deviate by >20%, sample more densely. Lean-ore decision criterion: open the bed only if iron output converted into labor hours exceeds fuel labor + sorting labor, times a 1.2 safety factor; otherwise do not open — better an idle furnace than a collapsed ledger.

### 40.2.3 Power Matrix

| Tier | Sustained power (empirical) | Seasonality | Performance loss | Resource cost | Final bottleneck |
|---|---|---|---|---|---|
| Water wheel (baseline) | Overshot 2–5 kW; undershot 0.5–2 kW | Stops for freezing, floods, and spring drought; annual availability 70–90% | — | Annual repair of weir and wheel (Chapter 29) | Flow — the first casualty of a dry year |
| Windmill | Rated 2–4 kW (wind 7–9 m/s) | Stops when the wind stops; annual availability 20–40% | Carries interruptible loads only (milling, grinding, water lifting) | High capital cost; sails must be furled in strong wind | Wind regime — continuous blast and machine tools do not connect to this tier |
| Animal power | Horse 0.5–0.7 kW × 4–6 h/day; ox 0.3–0.5 kW × 5–7 h/day | Available year-round; recalled during the busy farming season (Section 37.3.3) | Power drops 5–10×; low speed requires reworking to direct drive | Hay 8–12 kg per ox per day, competing with people for land (Section 37.1.3) | Fodder land and draft-animal headcount |
| Human power | Sustained 0.06–0.08 kW; peak 0.3–0.4 kW for ≤15 min | Follows the shift schedule | Down another order of magnitude; bellows bag 8–15 L per stroke — one person can sustain it briefly, not across a full shift (Chapter 2 worked example) | Rations ×1.25 (heavy labor, Section 37.1.1); scheduling per Section 37.4 | Human hours (Section 37.1.3) |

Degradation chain example (mine hoisting, 50 m lift, empirical, needs calibration): water-wheel winch 10–20 t/day → animal-powered capstan 3–8 t/day → human windlass 1–3 t/day. Note the tier gap: every drop in power tier cuts output by more than half — **scheduling during degradation must be done at the degraded tier, never on the momentum of the tier above; otherwise the fuel, ore, and ration ledgers all go wrong at once.**

### 40.2.4 Materials Matrix

| Baseline | Substitute | Performance loss | Resource cost | Applicability boundary | Final bottleneck |
|---|---|---|---|---|---|
| Refractory clay (refractoriness ≥1580°C) | Common clay + 40–60% grog (crushed scrap pottery, 5–15 mm) | Refractoriness falls to 1250–1380°C; slag-corrosion life falls to 1/3–1/2 | Grog comes from self-produced scrap pottery; crushing 0.1–0.2 t/person-day | Kiln outer layers, flues, pottery-kiln linings, interfaces <1200°C | No substitute at molten-iron and molten-glass interfaces; if lost, metallurgy falls back to intermittent small furnaces |
| Copper conductor (resistivity 0.017 Ω·mm²/m) | Iron conductor (about 0.10 Ω·mm²/m) | Roughly 6× the resistance: equal resistance over equal length needs 6× the cross-section and 2.4× the wire diameter; rusts easily | High wire-drawing labor; joints need clean-face crimping and grease against rust | Short, thick trunk runs, grounding, battery electrode rods | Motor windings, fine wire, and everything relying on low resistance and flexibility do not continue |
| Leather (drive belts, sealing cups) | Oil-soaked canvas belts; felt or oiled-hemp seals | Belts stretch and fear moisture, life falls to 1/3–1/2; felt pressure rating ≤2 atm | Canvas must be finely woven and oil-soaked, with its own ledger of work | Low-speed drives in dry, room-temperature settings; low-pressure plunger pump seals | High-pressure steam valve-stem seals — require soft metal or graphite (Chapter 28) |

**Side-by-side test-bar bend-over method (admission test for substitute refractories)**: roll bars 8 mm × 8 mm × 60 mm from a known refractory clay and from the material under test; shade-dry 3 days, stand them side by side on the same crucible rim, fire to visual white-bright (about 1300°C; flame-color temperature judgment ◎ per the Chapter 12 practice records), and after cooling compare the bend-over: if the tested bar's bent tip exceeds the known bar's by ≥10 mm, consistent across three parallel sets, rule "banned from high-temperature interfaces."

### 40.2.5 Process Matrix (Precision Loss Table)

| Baseline process | Downgraded process | Precision / performance loss | Labor multiple | Non-continuing items (final bottleneck) |
|---|---|---|---|---|
| Sand casting | Free forging + cutting | Dimensional tolerance ±1–2 mm/100 mm → blanks ±3–6 mm/100 mm; internal cavities cannot be formed | ×2–5 | Complex-cavity parts, large-bore pipes, pots and cauldrons — fall back to cast iron (Chapter 18) |
| Glassblowing | Core-formed / mold-formed | Wall-thickness uniformity ±30% → ±50–60%; thin-walled vessels over 3 L hard to form; mouth consistency actually improves | ×3–5 | Transparent thin flat sheet, narrow-neck deep-vessel ware |
| Turning / boring | Hand scraping + hand reaming | Flatness: turning 0.02–0.05 mm/300 mm, scraping reaches 0.005–0.02 mm/300 mm — flat surfaces get flatter, but planes only; roundness 0.01–0.03 mm → hand reaming 0.03–0.08 mm | Scraping a 300×400 mm plate takes 40–120 h (turning 1–2 h) | Long cylindrical guide rails, long lead screws — precision screw threads are the bottleneck of machine-tool bootstrapping (Chapter 20) |

Read the scraping row twice: **handwork does not mean crude.** Scraping loses nothing to machine tools on flatness; it loses on the range of shapes (cylinders, cones, long threads) and on time. A settlement that treats "downgrade = precision collapse" as a law will stand paralyzed even where scraping plainly works; conversely, a settlement that believes scraping can do anything will die on the lead screw. The whole point of the matrix is to nail both illusions into their columns.

## 40.3 Degraded Operation Design

### 40.3.1 What "Drop One Tier and Still Run" Means

Degradation is not on-the-spot improvisation; it is a **state prepared in peacetime**. The test is the "three on-register" checks — missing any one, the plan is just paper:

1. **Equipment on the register**: degraded-route facilities are neither dismantled nor sold. The bloomery furnace, animal capstan, human windlass, oil lamps, and pottery capacity stay serviceable; matched blast pipes, tongs, and hammers are sealed into the plan box and inspected quarterly.
2. **Materials on the register**: the softwood-charcoal kiln is fired at least once a year, maintaining both stock and skill; grog for substitute refractories has a standing pile.
3. **Personnel on the register**: ≥2 people at Level 2 for every degraded route (recorded in the skills matrix), with operating card copies inside the plan box, so a literate operator can walk a novice through it by the card.

An example of degradation when all three are on the register:

| Main line | After degradation | Function retention (empirical; must be measured in a drill) | What was not saved |
|---|---|---|---|
| Blast furnace (blower or water wheel broken, charcoal at the red line) | Bank the furnace (per Chapter 18 procedure) → bloomery resumes | Iron output 10–25% (blast furnace 0.5–1.5 t/day, bloomery 50–150 kg/day) | Volume; but the tool-iron supply never breaks |
| Generator down | Storage batteries reserve for the accounting office and medical only; lighting drops to oil lamps; mill and water lifting switch to windmill or animal power | Depending on stored charge, lighting coverage <20% | All power-electric loads |
| Glass line down | Containers covered by pottery (Chapter 11 registered capacity); windows drop to wooden boards and oil paper | Containers 100% (pottery), transparent items 0 | Light-transmitting windows, chemical glassware |

Degradation's **exit** matters as much as its entry; it is not "the stock is back, relight the furnace." All three exit conditions (step ⑤ of Card 40-02) must hold or you wait: stock back above the yellow line; main equipment repaired and passing that chapter's acceptance; the degraded line's first three batches conforming — the last proves with product that the substitution period accumulated no hidden damage. Historical failure mode: the charcoal price falls back, the furnace is relit overnight, and the lining — already thinned by corrosion during the substitute-fuel period and uninspected — burns through on the third day after restart. The half-day saved by skipping the exit review cost an entire furnace. Exits, like entries, are dual-signed and archived.

### 40.3.2 Degradation Trigger Criteria: Linked to the Chapter 38 Three-Color Lines

The Chapter 38 ledgers set three color lines for every key stock: blue (ample), yellow (warning), red (crisis). This chapter rules: **yellow-line actions and red-line actions are hard-written into the plan cards in advance; touching a line triggers execution — no ad-hoc meeting to debate "whether to hold on a little longer."**

| Monitored item | Yellow line (example) | Red line (example) | Yellow-line action | Red-line action |
|---|---|---|---|---|
| Hardwood charcoal stock | ≤40 days of use | ≤20 days of use | Restrict forging charcoal; run the softwood co-firing test into the register | Start the banking procedure; bloomery stocked and on standby |
| Iron ore stock | ≤60 days of use | ≤30 days of use | Trial run of lean-ore beneficiation | Bloomery to reduced shifts; remaining ore reserved for tool iron only |
| Water source (dry-season flow) | Down to 60% of the multi-year mean | 40% | Cut non-essential uses (washing, part of cooling) | Water wheel stops, power degrades; start cistern rationing |
| Refractory clay stock | ≤2 major repairs' worth | ≤1 major repair's worth | Substitute mixes only for outer layers; send out a prospecting team | Metallurgy line schedules the "last heat" sequence |

Red-line calibration (in days of use): **red-line days ≥ (1 day trigger decision + switchover time + 3 days restart first-output verification) × 1.2; yellow line ≈ 2 × red line.** Example: a standing bloomery switches in 2–3 days → hardwood charcoal red line ≥8–10 days of use. The table's example values of 20–40 days are the "comfortable tier," for settlements with long haul distances. If the degraded facility is not standing, the red line must additionally carry reconstruction time (lining drying 20–40 days) — this formula is itself the economic argument for the "three on-register" checks: **nothing prepared in peacetime leaves no tier to drop to in disaster; the red line gets forced out beyond tens of days, and the ledger stays stretched taut forever.**

### 40.3.3 Degradation Drill System

- **Frequency and rotation**: at least once a year; subjects rotate over six years: ① fuel line (softwood-charcoal day / peat day) ② power line (water wheel down 24 h) ③ materials line (one kiln firing on a substitute lining) ④ process line (one casting delivered as a forging) ⑤ water-and-epidemic understaffing (minimum schedule with 30% of hands absent) ⑥ mine-hoisting degradation.
- **Rules**: the month is announced in advance, never the date; once the drill order is given, Card 40-02 is executed for real — really stop the line, really count the stock, really schedule at the degraded tier.
- **Five-column record**: time / line stopped and subject / plan version number / switchover time and function retention / problems exposed with rectification deadlines and responsible persons.
- **Three prohibitions**: no drilling only the subjects you are confident about (every drill must include one "main-resource cutoff" subject); no fake data (stoppages must truly stop, stock must be actually counted); no skipping review (review meeting within 7 days of the drill, every problem given a deadline; next year's drill first checks prior-year closure).
- **Cost booked**: the drill day's output loss is accrued at one day's capacity of that line and charged into the annual schedule (Section 37.3); settlements that begrudge this cost will pay for it later with a whole farming season.

[Card 40-02 Degraded-Mode Plan Card (One per Line)] (eight fields)

1. **Input materials**: the line's main process card; the degraded-route registration page (Card 40-01); the three-color line values for this line's monitored items from Chapter 38; the work schedule (Card 37-02).
2. **Required tools**: the plan box (sealed copies of degraded operating cards, dedicated tools, seals, and inspection sheets); the ledgers; the gong/bell signal convention (degradation signal = three short, one long, posted settlement-wide).
3. **Operating sequence and control points**: ① trigger confirmation: accountant and workshop supervisor verify the books jointly against the yellow/red action lines; **② declaration: issued under dual signatures, announced by gong, plan version number stated**; **③ switchover: first shut down per the original chapter's procedure (furnace banking, pressure release, and cooling curves must not be altered), then start the degraded line; during switchover reschedule shifts per Section 37.4 — safety lines not lowered by an inch**; ④ daily report: function retention, stock, injuries and illness; ⑤ exit review: only when all three conditions hold (stock back above the yellow line / main equipment repaired past acceptance / degraded line's first three batches conforming) may the main route resume; lifting requires dual signatures and archiving.
4. **Empirical parameters and calibration methods**: switchover time-limit target ≤48 h (empirical), corrected by drill measurements; three-color thresholds backfilled into the ledgers year by year per the Section 40.3.2 calibration.
5. **In-process observation records**: trigger time, declaration time, switchover completion time, function retention (degraded line output ÷ main line daily average), boundary-violation event count, injury and illness records.
6. **Pass / rework / scrap criteria**: pass = switched per the card, core functions restored within ≤48 h, complete records; rework = overtime (identify which of the "three on-register" checks is missing, fix it, re-drill); scrap = undocumented degradation or skipping the shutdown procedure (that period's output treated as unfinished process work, Iron Law 6).
7. **Common failures and troubleshooting order**: won't switch → first check the plan box physically exists → check the operators are there (≥2 people at Level 2) → check the degraded-material stock; degraded output far below the register → check whether it was forced outside the applicability boundary → check whether substitute batches were run at substitute parameters.
8. **L1 / L2 / L3 evidence**: L1 = the written plan and plan-box inventory; L2 = one drill's five-column record; L3 = the full file of one real activation, or two consecutive years of drill records + sign-off notes on prior-year closure.

## 40.4 Disaster List and Redundancy

### 40.4.1 Six-Disaster Master Table

| Disaster | Main impact surface | Reserves and bypasses beforehand | Recovery essentials (overall order in Section 40.5) |
|---|---|---|---|
| Drought | Water source, water-wheel power, irrigation → next year's grain (N₁ and N₃ of Section 37.2 tighten together) | Cisterns ≥30 days of water for people and livestock; short-season dryland crop seed; the banking plan (Section 40.3.2) | Secure drinking water first; decide firmly to save the crop or abandon the field — dragging until both are lost is not allowed |
| Flood | Low-lying stores, kilns taking on water, bridges and roads | Stratified storage (grain and critical items on upper floors); high-ground backup grain 10–15%; rafts and high-ground assembly points | After drainage, slow-dry the kiln bodies (Section 40.4.2); inspect bridges and culverts before crossing |
| Fire | Dense building zones, stores, dry-season woodland | Firebreak lanes ≥8 m between workshops; ≥2 sand boxes plus ≥1 200 L water vat per workshop; fire hooks and axes at fixed points | Rescue people → tear down houses to cut the fire's path → guard the ashes against reignition for 24 h |
| Epidemic | Labor — the only non-renewable asset (Iron Law 7) | Downwind isolation huts + separate water vessels; 40–60-day ration buffer; lime reserves (for disinfection, Chapter 13) | Isolation and separate dining first (details in Chapter 49); all lines run one tier down; return to work one further incubation period after symptoms clear |
| Mine disaster | Lives underground, tunnels, hoisting, and morale | Two-person rule and support (Chapter 16); second exit; hand windlass as backup hoisting | Rescuer safety first; seal the disaster zone → drainage and repair → the three incident steps of Section 37.6.2 |
| Critical equipment failure | Single-point equipment: water-wheel shafts, blowers, millstones, measurement standards | Chapter 39 spare-parts ledger; duplicate sets of small parts; the bypass is the degraded route (Section 40.2) | Bypass first to hold function, repair in parallel to hold capacity; after part replacement, acceptance per the Chapter 39 procedure |

**Six-disaster reserve quota baseline (empirical, scaled to a 300-person settlement; must be calibrated to population and disaster history):**

| Reserve | Quota | Storage rules |
|---|---|---|
| Drinking water | 20 L per person × 30 days (about 180 m³, cisterns and household vats combined) | Stored dispersed; each cistern fully rotated once a month |
| High-ground backup grain | 10–15% of the year-round ration (about 7.5–11 t unmilled grain) | Dedicated store above flood level, two-person two-lock, quarterly stocktake |
| Emergency fuel | 7 days of domestic firewood + household kindling | High-ground wood shed, sited apart from the main wood yard |
| Isolation and rescue | 2–3 isolation huts (about 5% of population capacity); lime 200–400 kg; 2 first-aid kits | Downwind, separate water vessels; lime kept off the ground against damp |
| Fire prevention | ≥2 sand boxes plus ≥1 200 L water vat per workshop; firebreak lanes ≥8 m kept clear year-round | Vats checked full daily in winter and the dry season |
| Hoisting backup | 1 hand windlass + 2 spare ropes | Fixed point in the shaft-head house, monthly inspection |

Reserve quotas must not be conjured out of thin air; derive them backward from the recovery criteria: **quota = days needed to meet the Card 40-03 Sequence 1–3 criteria × daily demand × 1.3–1.5 redundancy.** Three storage rules: first, emergency reserves and production stock are kept in **separate stores under separate ledgers** — one shared store will inevitably be diverted to daily use, which is exactly the root cause of row 3 of the failure-modes table; second, water, grain, and fuel rotate with daily first-in, first-out use — the ledger need only hold the floor quantity — while lime and medicines are replaced on a schedule back-calculated from shelf life; third, each quarter inspect on the same day as the plan boxes — one inspection covers both ledgers and saves one muster.

### 40.4.2 The Three Recovery Details Most Often Got Wrong

**First, post-flood kiln drying.** Water vapor trapped inside a fully soaked brick structure will crack and burst the kiln if the temperature rises too fast (>80–100°C/h). Procedure: open every fire-viewing port; hold a gentle fire (dark red) for 1–2 days, until the kiln wall's surface color returns to dry with no damp patches; then shift to the normal curve. Criterion: a dry-hay bundle placed inside for 30 min without taking up moisture means fully dry; a ◎ palm pressed to the inner wall feeling no cool dampness is a supplementary check — hand-feel is initial screening only; the hay bundle governs.

**Second, running during an epidemic.** With 30% of hands lost, crew processes cannot field their full complement — the blast furnace cannot field its 7 — so bank the furnace straight away per the plan and switch to intermittent processes one or two people can sustain: bloomery, small kilns. The medic post and the accounting office are non-reducible posts; every schedule during understaffing re-passes the Card 37-02 three-line check. Whether to halt production during an epidemic is not a moral question but arithmetic: the scrap and the lives lost running the big furnace through sickness exceed the cost of banking and restarting.

**Third, the equipment-bypass account.** A bypass is not an equivalent swap: with the blower dead, two large bellows bags worked in rotation by two people deliver 30–60% of the blower's air volume, and furnace output drops 30–50% accordingly (empirical; must be measured in a drill). Record the function retention in the register and immediately reschedule the fuel and ore ledgers at the degraded tier — the most common error is equipment downgraded while the books still record full capacity, and a month later the stock hits bottom in silence.

### 40.4.3 Single Points of Failure Among Critical People

On the institutional side, the redundancy iron rule of Section 37.5.1 (≥2 people at Level 2 for every critical post) and the Chapter 43 master–apprentice registry provide the backstop; this chapter adds one physical, operating-layer object — the **stand-in board**. One wooden board per critical post, hung at the workshop door, updated in step with the quarterly review and the skills matrix, five columns:

| Column | Content |
|---|---|
| Post | e.g., blast-furnace head / accounting-office metrology / medic |
| First stand-in | Name, skill level (must be ≥Level 2) |
| Tier the line drops to while they stand in | e.g., blast furnace banked, bloomery opened in its place |
| Processes stopped immediately after the downgrade | e.g., continuous blast, night-shift iron tapping |
| Who is responsible for sealing up and record-keeping after the stop | A specific name |

Precedent: the settlement's only accountant falls ill → no one to cross-check the weights and measures → all acceptance grinds to a halt (the Iron Law 6 evidence chain breaks). Pre-work verification item 8 requires the weights-and-measures cross-calibration to be done by two people each quarter — prepared for exactly this moment. **The terror of a single point of failure is not the post itself but that it freezes everyone else's acceptance along with it.**

## 40.5 Recovery Priority

### 40.5.1 Order and Criteria Table

When post-disaster resources and manpower are enough for only one thing, do it in this order. The guiding principle is Iron Law 7: equipment and stock can be remade, the dead cannot — **every dispute over order is settled by "which one kills people first."**

| Seq | Recovery item | Criterion (check it off before entering the next sequence) | Basis |
|---|---|---|---|
| 1 | Drinking water and shelter | ≥20 L/day per person of boiled water, unbroken for 7 consecutive days; every person has a dry bunk and a room that can be heated (warm enough that no hypothermia injuries occur) | A person dies in 3 days without water; hypothermia removes people by the batch in a single night |
| 2 | Food line | Two hot meals daily, rationed to individuals and recorded; grain stores fully counted, ration schedule laid out ≥14 days | Stores are the buffer; if ration order is not restored within 3 days, scramble-looting begins |
| 3 | Fuel line | Domestic firewood ≥7 days of use; cooking and heating unrestricted | Sequence 2's hot meals and Sequence 1's heating run on it; kilns are not in this sequence |
| 4 | Tool line | Line-by-line checklist per Section 40.5.2, tick by tick | One day stopped kills no one; one month stopped breaks the technical chain (furnaces cracked by frost, tools rusted, skills gone stale) |
| 5 | The rest | Glass, precision work, long-cycle projects | Taken up after the first four sequences are stable |

### 40.5.2 Internal Ordering of the Tool Line, and a Counterexample

Order within the tool line: first repair the tools that "protect the first three sequences" — water-pipe fittings, water buckets, axes and saws, cookware, water-lifting gear; then power (water wheels, winches); then the metallurgy small furnaces and pottery kilns; last, everything else. **The tool line itself must be screened by recovery priority, not by price or difficulty.**

Counterexample walkthrough (empirical walkthrough; copy the numbers onto the recovery card cover): a 300-person settlement is flooded; if the mill and machine tools are repaired before drinking water — the flood contaminates the wells, dysentery rises on days 4–10, losses run 15–25% (about 45–75 people — precisely all the full-time artisans plus two-tenths of the labor force, Section 37.3); the repaired machines have no one to run them, and recovery stretches from one season to a year. **The settlement that repairs machines before water ends up with neither machines nor people.**

[Card 40-03 Disaster Recovery Card (Common to the Six Disasters)] (eight fields)

1. **Input materials**: headcount results (alive / injured / dead in three columns, including the missing); the Section 40.5.1 order table; reserve ledgers and the substitution matrix (Section 40.2); the per-disaster recovery essentials (Section 40.4.1).
2. **Required tools**: the check-off checklist (copied from Section 40.5.1); gong/whistle; stretchers and first-aid kits (medic post); dry-hay bundles (for the kiln-dryness criterion).
3. **Operating sequence and control points**: ① count people and account for the missing; rescue the injured first, then the trapped; **② restore through the five sequences in order, entering the next only after each sequence's criteria are checked off; skipping a sequence requires the disaster commander's signature and a stated reason**; ③ one report every 12 h: five columns — headcount, water, grain, fuel, epidemic signs; **④ before resuming production, pass the change inspection (Section 37.6.3): flooded kilns, jolted furnaces, replaced parts — all inspected before use**; ⑤ archive the full recovery file under Chapter 43; register deaths, injuries, and causes of illness for Chapter 49 post-disaster sanitation.
4. **Empirical parameters and calibration methods**: the per-sequence time limits (drinking water achieved within 72 h; hot meals cooking within 72 h; 7 days of firewood within 5 days) are empirical values, corrected year by year against drill and real-event records.
5. **In-process observation records**: achievement time and gaps per sequence; sequence-skip signatures; first epidemic-sign time and headcount.
6. **Pass / rework / scrap criteria**: pass = five sequences never inverted, check-off evidence for every sequence's criteria, 12-h reports archived; rework = a discovered skip (stop, backfill the prior sequence, chase the signature); scrap = recovery without a checklist — no basis for after-action review and unclear accountability, treated as not recovered.
7. **Common failures and troubleshooting order**: stuck at a sequence past its time limit → check whether the lack is resources or hands: resources go to the substitution matrix (Section 40.2), hands go to the stand-in board and the reduced-output plan (Section 37.3); epidemic signs appear in camp → switch at once to the epidemic procedure (isolation, Chapter 49); the order table never overrides isolation priority.
8. **L1 / L2 / L3 evidence**: L1 = the written card and checklist; L2 = one tabletop exercise or drill record; L3 = the full file of one real activation, or six-disaster rotation drill records + annual revision sign-off.

## Master Parameter Table

| Parameter | Empirical value | Calibration method | Section |
|---|---|---|---|
| Softwood charcoal bulk-density threshold | <200 g/L rules softwood charcoal (hardwood 250–400 kg/m³) | Weigh a 1 L graduated-cylinder fill, ×3 | 40.1.2 |
| Shaft furnace temperature drop (softwood charcoal) | 50–150°C | Compare iron output and flame color against a co-firing control heat | 40.2.1 |
| Coal sulfur threshold | Sulfur in iron above 0.1% means hot shortness | Three-bar 90° bend method | 40.2.1 |
| Peat fire-temperature ceiling | About 1100°C | Lime-decomposition test firing | 40.2.1 |
| Lean-ore fuel ratio | Charcoal:iron = 6–12:1 | Booked heat by heat | 40.2.2 |
| Ore economic floor | Grade <20% uneconomic for bloomery smelting | Iron yield × fuel labor × sorting labor computed together | 40.2.2 |
| Crushing productivity | 10–25 mm, 0.2–0.5 t/person-day | Recorded labor, trial calculation | 40.2.2 |
| Water wheel power | Overshot 2–5 kW; undershot 0.5–2 kW | Back-calculated from water lifted or flour ground | 40.2.3 |
| Animal power | Horse 0.5–0.7 kW × 4–6 h; ox 0.3–0.5 kW × 5–7 h | Capstan lift, weighed and timed | 40.2.3 |
| Human sustained power | 0.06–0.08 kW (peak 0.3–0.4 kW for ≤15 min) | Timed by blast volume or water lifted | 40.2.3 |
| Substitute refractory refractoriness | 1250–1380°C | Side-by-side test-bar bend-over method | 40.2.4 |
| Iron conductor resistance | About 6× copper | Same-length, same-diameter wires lighting a lamp, compared | 40.2.4 |
| Plate scraping labor | 40–120 h per plate (300×400 mm) | Measured, recorded labor | 40.2.5 |
| Degradation switchover time limit | ≤48 h | Measured in a drill | 40.3 |
| Three-color red-line calibration | ≥ (1 + switchover + 3 days verification) × 1.2 days of use | Backfilled year by year | 40.3.2 |
| Drill frequency | ≥1 per year, six subjects over six years | Drill records | 40.3.3 |
| Post-flood kiln drying | Gentle fire 1–2 days until the surface returns to dry | Dry-hay bundle stays dry 30 min | 40.4.2 |
| Drinking water recovery criterion | ≥20 L/day per person of boiled water × 7 days | Water supply records | 40.5.1 |

## Failure Modes and Diagnosis

Ordered by "most common, hardest to detect." Every failure in this chapter is an institutional failure: the process itself is not broken; what is broken is that no one followed the card.

| Symptom | Candidate cause | Verification | Action | Prevention |
|---|---|---|---|---|
| Drill records show a blank "problems exposed" column two years running; drilled only on fine days in slack seasons | Drills as theater | One surprise drill with only 1 h notice | Reopen the problem list; the supervisor explains to the council; the surprise result is archived | Three prohibitions + six-year rotation + surprise drills (Section 40.3.3) |
| Ledger shows softwood charcoal requisitions while the furnace logs record hardwood charcoal; substitute batches unmarked | Substitute material quietly used as equivalent | Sample 10% of batch marks; check slag lines and test bars | That batch handled as unfinished process work; re-register through Card 40-01 | Dual-signed "substitute" column on requisitions; zoned storage |
| Monthly stocktake variance >5%; red-line goods out on "borrowing slips" with no returns; books at yellow, reality at red | Red-line stock breached by "temporary borrowing" | Surprise physical count | Restored within 24 h, or real degradation per red-line actions | Two-person two-lock on red-line goods (Section 37.6.1); borrowing requires council approval |
| Plan box opened for inspection with items missing, tools diverted to daily use | Plan box turned junk box | Quarterly open-and-inspect | Restock and reseal; the plan is marked "draft" while items are missing | Seals + inspection sheets + immediate report of any missing item |
| The person named on a stand-in board has left the settlement or died | Board decoupled from the matrix quarterly review | Reconcile against the Card 37-03 quarterly review | Replace and rewrite at once; meanwhile that post degrades per the single-person-failure plan | Board updated in sync with the quarterly review |
| After disaster, mill and machine tools repaired first while drinking water never met criteria | Sequence-skip recovery | Compare against the Card 40-03 checklist | Stop at once, backfill Sequence 1; chase the signature and review | Print the counterexample walkthrough on the recovery card cover |
| Register's performance column contradicts real activation (activation did worse) | Copied another settlement's numbers, or the annual re-verification was missed | Redo the comparative trial production | Amend the register and downgrade the substitution to "unverified" | Annual re-verification + real-activation citation records (Section 40.1.3) |

## Process Card Index

| Card number | Name | Use | Copy to workstation |
|---|---|---|---|
| 40-01 | Alternative Route Registration Card | Four-column registration, trial production, annual check | Accounting office / all workshops |
| 40-02 | Degraded-Mode Plan Card | Trigger criteria and switchover action list | Each line's operating position / copy inside the plan box |
| 40-03 | Disaster Recovery Card | Five-sequence recovery order checklist | Council hall / medic's room |

## Acceptance Criteria L1/L2/L3

| Level | Criterion | Test condition | Evidence kept |
|---|---|---|---|
| L1 | For each of the five resource classes, ≥1 alternative registered in writing with four columns (columns lacking measurements marked "unverified"); every critical line has a written degraded plan with trigger criteria; six-disaster recovery cards and stand-in boards in writing | Items missing from the 8-point pre-work verification are allowed but must be annotated | Register, plan set, recovery cards, stand-in boards |
| L2 | **One real degraded-operation drill completed: one line actually stopped per the plan for ≥24 h, complete five-column record, reviewed within 7 days, problems filed with deadlines**; ≥1 alternative through trial production with measured numbers in all four columns | No fake data in drills; trial production judged by the same referee as the baseline batch | Drill five-column record and review minutes; 3 trial pieces or rejection records |
| L3 | Two consecutive years of drills with all prior-year problems closed out; annual re-verification of the alternative register on file; at least one of the six disasters has actually activated the recovery card, or full six-disaster rotation drills are on record; stand-in boards consistent with the skills matrix; register-vs-ledger cross-check against Chapter 38 shows no irregular requisitions | Reproducible from the records by different people in a different season | Two years of drill files, re-verification records, cross-check sign-offs, stand-in board update records |

## Man-Hours, Labor, and Consumption

| Item | Headcount and duration (empirical) | Notes |
|---|---|---|
| Alternative route registration (per route) | Sampling + trial production 3–20 person-days | Take the upper bound if a furnace must be lit |
| Degraded plan writing (per line) | 4–8 person-hours + plan-box provisioning 0.5–1 person-day | Copying of operating card copies included |
| Annual drill | Full crew of the line × 1 day + review 4–8 person-hours | Stoppage loss = one day's capacity of that line, accrued into the schedule |
| Recovery card and stand-in board maintenance | 2–4 person-hours per quarter | Synced with the matrix quarterly review |
| Annual re-survey of substitute resources | 1–2 person-days per source | Check ore points, forest stands, and flows respectively |
| Six-disaster reserve upkeep | Cisterns, high-ground grain, isolation huts: annual repair 5–15 person-days | Charged to the public works ledger (Section 37.6.1) |

## Safety Boundaries

This chapter has no direct high-temperature, high-pressure process steps, but the following five items are institutional safety steps; failing to execute them counts as not completing this chapter:

1. **Downgrade never downgrades safety**: the night-shift two-person rule, the underground two-person rule, hydrostatic testing at 1.5×, and the like are unchanged by an inch at any degraded tier. Hands are tightest during degradation, which is precisely when violations spike — reschedule shifts per Section 37.4 before touching equipment.
2. **Shut down per the original chapter's procedure**: blast-furnace banking is a professional process step (Chapter 18); a steam engine may be left only after pressure release (Chapter 28); the plan card fixes the order, never the parameters.
3. **Poisoning by substitute fuels**: heating with coal or peat requires a flue leading outdoors; criterion: a dark-yellow flame trailing long smoke means ventilation is insufficient; the night watch is two people in one room, and the moment one feels dizzy both withdraw outdoors — carbon monoxide is colorless and odorless and gives no second chance.
4. **Rescuer self-protection**: measure your retreat before rescuing anyone; after a flood, check for wall lean and foundation damage before entering a building; in mine rescue, no second person goes down before support is complete (Chapter 16); entry to epidemic zones follows the Chapter 49 protection procedures.
5. **Drill safety**: a drill is not an accident reenactment; the assumed accident level is capped at "no risk to persons"; real injuries during a drill are handled under the Section 37.6.2 incident procedure and the drill is halted at once.

## The A/B/C Lists

**A list (executable directly in this chapter):**

| Item | Criterion |
|---|---|
| Alternative route register | Card 40-01 with all four columns filled, trial production on file |
| Degraded plan set | Card 40-02, one per line, the three on-register checks passed |
| Annual drill | Five-column record + review + deadline rectification |
| Six-disaster recovery cards and stand-in boards | Card 40-03 and the five-column stand-in boards on the wall, updated quarterly |
| Plan boxes | Sealed intact, last inspection ≤90 days |

**B list (requires earlier chapters' outputs):**

| Item | Prerequisite |
|---|---|
| Three-color thresholds | Chapter 38 ledger flows |
| Spare parts and bypasses | Chapter 39 spare-parts ledger |
| Skills matrix and schedules | The three cards of Chapter 37 |
| Operating procedures for each degraded line | The corresponding process cards of Chapters 11–33 |
| Flame-color temperature judgment and fracture rejection | Certification under Chapters 12, 18–19 |

**C list (external dependencies and irreducibles):**

| Item | Notes |
|---|---|
| Unpredictability of disasters | Can only shorten downtime; cannot immunize |
| Actual existence of substitute resources | No coal in the territory means no coal route; "obtainable from afar" does not count |
| Climate window for peat drying | Needs an entire dry season; a rainy year loses the tier |
| Outside aid | Neighboring settlements may be hit too; plans are designed for zero outside aid |

## Downstream Dependencies

- **Chapter 38 material-and-energy ledgers**: this chapter's trigger thresholds are calibrated and backfilled year by year from the ledger flows; the ledger's three-color "red-line action" field must be backfilled with this chapter's plan numbers — the ledger supplies the data, this chapter supplies the actions.
- **Chapter 39 maintenance and spare parts**: the spare-parts ledger merges with this chapter's bypasses into one equipment-redundancy master table; the recovery order for the "critical equipment failure" disaster entry cites the Chapter 39 part-replacement acceptance procedure.
- **Chapters 50–53 environment editions**: rewrite this chapter's matrices per environment — the rainforest edition takes softwood charcoal as the normal baseline and tightens the fuel matrix; the tundra edition makes peat and lignite the main tiers; the island edition moves the windmill tier forward and raises the animal-power share; the arid edition lists the drought recovery card first and doubles the water reserve baseline.
- **Chapter 43 archive system**: archiving and master–apprentice transmission of the register, drill records, re-verification records, and full recovery files; the training face of the stand-in boards is carried by the master–apprentice system.
- **Chapter 49 post-disaster sanitation**: the details of Sequence 1 (drinking water) and Sequence 4 (epidemic-sign handling) of the recovery order table — water-source disinfection, corpse handling, isolation, and return-to-work health checks — are expanded in that chapter; this chapter locks only the order and the interfaces.
