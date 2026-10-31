# Chapter 54 Transport and Civil Engineering

## Chapter goals

After finishing this chapter, a settlement should be able to produce five deliverables: a **road network classification map** (three tiers — trunk/branch/track — marking grades, bridge sites, and maintenance responsibility sections; the foundation of production scheduling and freight budgeting), a **bridge selection record** (each crossing selected by span/hydrology, governing passage safety and flood survival), a **vehicle ledger** (wheel type, axle type, rated load, braking method, governing load classification and annual inspection), a **per-animal fitting record** (load-bearing points and chafing checks, feeding the draft-efficiency account), and a **rainy-season maintenance schedule** (before/during/after-rain three-phase actions + responsibility roster).

## Capability boundaries

**Can do:**

- Construction and rainy-season maintenance of three tiers of road surface (earth/crushed stone/stone slab); vehicle roads with grades ≤8% and turning radii computed for the steering turntable.
- Single-span timber beam bridges ≤6 m, multi-span timber bridges ≤15 m total length, stone arch bridges ≤4 m clear span, double-rope suspension bridges ≤10 m (executing the 7.12 specification).
- Complete vehicle manufacture from solid wheels to spoked wheels; wooden/iron axles with sliding bearings (the 21.3 system); four-wheelers with a steering turntable and wedge-block brakes.
- Per-animal fitting and chafing management for pack frames, pack saddles, neck yokes, and collar harnesses.

**Explicitly cannot do:**

- Rolling bearings and high-speed wheel axles (same boundary as Chapter 21) — all bearings in this chapter are sliding type.
- Stone arch bridges with clear span >4 m (centering and masonry experience not yet reached; outlook register at the end of 54.2.3).
- Canals and locks — registered only, not chartered as projects (54.5.1 has the earthwork order-of-magnitude account).
- All-weather trunk traffic through the rainy season — operation is universally downgraded (load and speed restrictions).

**External dependencies (counted into List C):**

1. Draft animals: ≥2 registered with pack-transport trial-run records (Chapter 10, 10.7).
2. Wrought-iron and iron-hoop shrink-fitting capability (Chapters 17, 18, 21) — spoked wheels, iron axles, and wedges all consume iron.
3. Lime-mortar test-cube regime in use (13.4) — for mortared arches and joint pointing.
4. Fully dried hardwood supply (Chapter 7 monthly-check method) — wet stock is forbidden for beams, spokes, hubs, and shafts.

## Pre-construction verification

Checklist style. If any item fails, the corresponding section's output is downgraded to "temporary works" and marked on the road network map.

| # | Verification item | Criterion (confirm you hold __; the standard is __) |
|---|---|---|
| 1 | Measuring tools | Spirit level, stretched line, measuring rope (Chapter 3); water-bowl leveling re-measures a 10 m height difference with run-to-run difference ≤10 mm |
| 2 | Timber | Beams, spokes, hubs fully dried: monthly-check weight method (Chapter 7) with weight loss <1% for two consecutive months |
| 3 | Ironwork | Shrink-fit hoops, open pins, and wedges forgeable in-house; after cooling, a knife tip cannot enter between hoop and part (Chapter 21 method) |
| 4 | Lime | Mortar test cubes hold together for 7 days (13.4); stock ≥1.2 times this bridge's masonry volume |
| 5 | Stone | Rings clean when struck, no bedding-plane cracks (Chapter 17 method); arch stones strike-checked piece by piece |
| 6 | Ropes | Bridge main cables static-load calibrated (Chapter 7: working load = breaking value ÷ 5; ÷ 10 when carrying people) |
| 7 | Draft animals | At least 2 animals pulling 1/2 rated load over 100 m of level ground with no limping |
| 8 | Ledger | Chapter 37 regime in force: every project has a responsibility roster and a labor account |

## 54.1 Road engineering

**General principle: the enemy of a road is water, not vehicles.** Ruts, mud pumping, collapsed side ditches — the root cause is always water softening the subgrade. 13.6 already established that "a soaked foundation is the leading cause of uneven settlement"; roads are that same law carried out onto the open ground.

### 54.1.1 The three subgrade layers

Standard cross-section (branch roads and above):

| Layer | Material | Thickness (empirical) | Method and criterion |
|---|---|---|---|
| Base course | Large cobbles/rubble stone 80–150 mm across, voids choked with crushed stone | compacted 150–250 mm | Laid in two courses, each rammed with a 50 kg stone rammer until "rammer marks do not sink and stones do not ring hollow" |
| Surface course | Crushed stone, coarse (20–40 mm) below, fine (5–20 mm) on top | compacted 80–120 mm | Water the fines and sweep them into the joints; wheel traffic knits a crust in 7–10 days. Criterion: puddles after rain cover <5% of the surface |
| Road crown | —— | cross slope 2–4% | A convex hump highest at the center, raised 20–40 mm per meter of width. Criterion: no standing water 30 min after rain stops |

**Drainage side ditches**: one on each side, bottom width ≥200 mm, depth ≥300 mm, longitudinal ditch gradient ≥0.5% (≥500 mm of fall per 100 m) — on a crushed-stone surface without ditches, rain scours out the base course within two years (empirical). Every 30–50 m, provide an overflow outlet to carry water away from the subgrade; **ditch water must never be allowed to cross the road surface** (where it must cross, build a stone submersible causeway, 54.1.4).

Subgrade width: single lane 1.8–2.2 m (**wheel track + 300 mm margin on each side** — once chosen, the wheel track is uniform across the whole network, see the rut rule in 54.1.2); double lane 3.2–3.6 m. Passing bays: on single-lane roads, widen a section every 100–150 m (width ≥5 m, length ≥8 m).

### 54.1.2 Grades and turning radius

| Grade | Classification | Discipline |
|---|---|---|
| ≤5% (1:20) | Normal on trunk roads | Fully loaded passage unrestricted |
| 5–8% (1:20–1:12) | Load-restricted section | Fully loaded vehicles halve their load; descending requires the brake wedge engaged (54.3.4); escape buffer strips every 50 m along the roadside |
| >8% | Prohibited on trunk roads | Only empty ascending traffic on tracks; reroute heavy loads or build switchbacks (each level platform ≥2 vehicle lengths) |

Grade measurement method: stretch a 10 m line with one end on the pavement at the foot of the slope, raise the other end, and measure the vertical height difference — height ÷ length is the grade; 500 mm corresponds to 5%. Grades must be measured: the eye cannot tell 6% from 9%, and that is the boundary between load-restricted and prohibited.

**Turning radius and axle length**: when a vehicle with a fixed front axle turns, the front and rear rut lines are offset (offset = wheelbase × steering angle); a four-wheeler without a steering turntable side-slips and bends its axle in any turn — **four-wheelers must have a steering turntable (54.3.3)**. The minimum turning radius of a four-wheeler with a turntable ≈ 1.5–2 times the vehicle length (empirical; calibration: turn an empty vehicle through a full circle on flat ground — the distance from the front outer wheel rut to the circle's center is the radius). Minimum trunk-road radius **≥12 m**; where that cannot be met, treat the section as single lane + passing points. **Rut discipline: one wheel track figure for the entire network (recommended 1400 mm, empirical; field-calibrate against the most common vehicle type, write it into the ledger, and never change it); any rut deeper than 50 mm goes onto a surface-regrading work order.**

### 54.1.3 Road surface material tiers

| Tier | Surface material | Structure | Application | Annual maintenance labor (empirical) |
|---|---|---|---|---|
| Track | Bare earth | Clear vegetation, fill potholes, compact level; crown ≥4% (earth roads need drainage even more) | Forest and field, fair-weather traffic | 15–30 person-days per km |
| Branch | Crushed stone | Base course + surface course + side ditches (full 54.1.1 package) | Main routes between settlements and workshops | 30–60 person-days per km |
| Trunk | Stone slabs or interlocked crushed stone | Dry-laid stone slabs (≥120 mm thick) on a crushed-stone bed, joints filled with coarse sand; or a double crushed-stone layer thickening the surface to 150 mm | Short heavy-load sections (mine mouths, docks, 50 m at each end of bridges) | 20–40 person-days per km |

Tier-selection principle: **classify by traffic volume, not by prestige** — building a branch road for <50 t/year of traffic is waste; the 50 m at each end of a bridge and dock yards must be trunk-grade (heavy braking and starting concentrate there, and the surface fails there first).

### 54.1.4 Rainy-season maintenance regime

| Period | Action | Criterion |
|---|---|---|
| One month before the rains | Clear all side ditches, repair crowns; stock small piles of crushed stone every 100 m along the road (0.3–0.5 m³); post a list of mud-pumping-prone sections on the wall | Ditches pass water along the full length; materials checked against the list |
| During the rains | Patrol the line within 24 h after each heavy rain (≥2 h), in pairs with spades | Soft sections settled >80 mm flagged and logged the same day |
| After the rains | Mud-pumping remediation: excavate soft soil to firm base (or replace with 300 mm of crushed stone), level the surface; smooth out ruts; desilt the ditches | Treated sections carry traffic without sinking; entry closed out in the ledger |

**Submersible causeway**: where a low stretch must let water pass, build a submersible causeway instead of a culvert — dry-laid large stone for the pavement, a drop-apron toe protection at the downstream end; close it when floodwater overtops the road (water-level marker posts: overtopping means closure; reopen after the water recedes and silt is cleared). Responsibility follows 37.6.1: **benefiting workshops share the labor; the section-by-section responsibility roster is agreed at the start of the year and supervised by the accounting house.**

[Card 54-01 Roadbed Construction] (eight fields)

1. **Input materials**: rubble stone/cobbles 8–12 t (80–150 mm across, ringing when struck, flat and elongated pieces picked out); crushed stone 6–9 t (two grades, 20–40 mm and 5–20 mm); for earth roads, stock sand and clay blended to the local soil.
2. **Tools required**: 1 stone rammer (50 kg class), iron spades and picks (Chapter 6), measuring rope and spirit level (Chapter 3; cross-check the two before use: placed on the same flat surface, bubble offsets must agree), crown template (an arched board 1 m wide, 30 mm high at the middle).
3. **Sequence and control points**: ① Set out the alignment; measure grades per 54.1.2. ② Strip topsoil to undisturbed soil (soil that does not stick to the spade, no root-mat layer). ③ Place fill in 300 mm layers; only lay the next layer once the back-excavation footprint is <10 mm. ④ **Lay the base course in two courses, each rammed until "rammer marks do not sink and stones do not ring hollow"**. ⑤ Surface course: coarse grade then fine grade, sweep joints and water. ⑥ Hang the crown template across the edge stakes and scrape out the convex crown. ⑦ Cut side ditches 300 mm deep, longitudinal gradient ≥0.5%. ⑧ After 7–10 days of traffic knits the crust, re-scrape the surface.
4. **Empirical parameters and calibration**: base 150–250 mm, surface 80–120 mm — lay trial strips of both thicknesses in 1 m × 1 m test plots; after one rainy season, dig them open and check whether fines have invaded the base course; if so, thicken. Crown 2–4% — check standing water 30 min after rain stops; if water stands, raise the crown. Close out ramming passes when "two more passes change nothing" (◎ hand-feel; practice method: divide one test plot into three strips rammed 30/40/50 passes and compare by back-excavation; complete 3 plots before going on the job; compensation: back-excavate to check density every 20 passes).
5. **Observations to record**: stake numbers, fill/cut depths, ramming passes, standing-water sections after rain and mud-pumping flag locations; enter into the road-section work order.
6. **Pass / rework / scrap criteria**: pass = fully loaded vehicle crosses 3 times with rut depth ≤50 mm, no standing water 30 min after rain, ditches pass water end to end; rework = localized mud pumping or ponding (excavate, replace, and re-lay that section); scrap = base-course stone weathers and shatters over wide areas (re-lay from a new source; mixing new stone over the old face is not allowed).
7. **Common failures and diagnosis order**: potholes within one season of laying → first check surface thickness → then check small stones (<50 mm) mixed into the base → then check for blocked ditches; deep ruts after rain → check whether the crown has flattened (re-scrape); recurring mud pumping → dig open and check for groundwater; if water seeps up, switch to seepage-drain drainage instead of endlessly thickening.
8. **L1 / L2 / L3 evidence**: L1 = 100 m completed + work order; L2 = after one rainy season, mud pumping ≤5% of the line and closed out; L3 = two seasons of maintenance records + responsibility-roster labor account + thickness and gradation calibration conclusions entered in the ledger (Chapter 43).

## 54.2 Bridges

**Selection order**: prefer a rope bridge over a beam bridge, prefer a beam bridge over an arch bridge — the simpler the structure, the sooner it carries traffic. Move to a stone arch bridge only when a beam bridge's middle piers are scoured year after year, or the span is pinned at 4–6 m while both banks have stone and skilled labor.

### 54.2.1 Timber beam bridges: span–beam-depth empirical table

The design rule comes from the beam deflection law in 25.8: **doubling the span multiplies sag eightfold; doubling beam depth cuts sag to one-eighth** — every step up in bridge span is a step up in beam depth. The red line follows 25.8: **if sag exceeds span/100, the beam must be thickened or a middle post added.**

Empirical table for single-lane timber beam bridges (hardwood, fully dried; wheel load taken as 800 kg total on two axles, shared among the beams):

| Clear span | Single-beam section (width × depth) | Number | Cross beams (under the deck boards) | Notes |
|---|---|---|---|---|
| ≤2 m | 100×150 mm | 4 | spaced 500–600 mm | Track grade suffices |
| 2–4 m | 120×250 mm | 4–5 | same | Standard branch-road span |
| 4–6 m | 150×400 mm | 5–6 | same | Ultimate single span on trunk roads; near 6 m add a pair of diagonal braces under the beams |

When beam depth is insufficient, use **stacked beams**: two shallow beams superimposed, pinned along the length with wood or iron pins in pairs every 400–500 mm — look up a stacked beam in the table by its **total depth**, but pin spacing must be close enough; otherwise the two beams bend independently and the added depth is wasted (verification: load a stacked beam and a single equal-depth beam over the same span; only similar sag counts as truly acting as one).

**Main-beam end bearing**: bearing length ≥200 mm at each end; bearing pads of stone (or hardwood) keep the beam ends from sinking into the abutment soil; leave 20–30 mm expansion joints between beam ends — they must not butt hard against each other.

### 54.2.2 Multi-span timber bridges and piers

Beyond a 6 m single span, add middle piers — **splicing long beams together is not allowed** — the deflection law at a 6 m span has already consumed the safety margin, and extrapolating the table to a 10 m span demands timber of the 700 mm class, which the forest can neither supply nor men lift.

- **Timber pile frame piers**: piles of hardwood ≥200 mm in diameter, driven ≥1.5 m into the riverbed (criterion: stop driving when penetration is <30 mm per 20 hammer blows); a capping beam over the pile tops carries the main beams; diagonal braces between the piles resist the current. Where piles cannot be driven into a cobble bed, switch to a **stone-filled timber crib foundation** (crib filled with cobbles and sunk to the bottom, top face 300 mm above normal water level).
- **Scour protection**: riprap ≥0.5 m³ on the upstream face of every pile; a **cutwater** (a pair of inclined piles) upstream of the pier group — bridges die from floods hollowing out pier feet, not from beams snapping.
- **No joints at midspan**: each span's main beam is one continuous piece; only if stock is too short may the joint be placed over a pier top (lap length ≥1.5 times beam depth, locked with bolted side plates or iron pins).
- **Flood-level calibration**: ask the oldest residents on both banks + inspect mud marks and vegetation lines on the bank walls; take the higher of the two and raise it 500 mm as the design flood level; the underside of the bridge deck must clear this line.

### 54.2.3 Introduction to stone arch bridges (dry-laid arches and springing thrust)

Clear spans ≤3 m may be dry-laid (no mortar); 3–4 m uses lime-mortar masonry per 13.4. The arch is the right form for a stone bridge because stone resists compression, not bending — the arch ring converts load into compression traveling along the curve to both banks, using the material exactly where it is strongest. The price is that **the arch pushes outward on both banks**: the same logic as the roof horizontal thrust in 13.7, scaled up — a roof frame cancels it with tie beams, an arch bridge cancels it with abutments.

- **Arch ring dimensions**: ring thickness at the crown ≥ 1/10 of the clear span (≥300 mm for a 3 m span, ≥400 mm for a 4 m span); voussoirs chiseled wedge-shaped (wider outside, narrower inside); in a dry-laid arch, dress the contact faces of adjacent stones flat and wedge them tight with crushed stone — **only when every stone, struck, does not ring hollow is it truly set**.
- **Rise**: take 1/4–1/3 of the clear span. The smaller the rise, the greater the thrust (see the formula below); where the site allows, take 1/4.
- **Arch centering (falsework)**: a wooden half-frame laid out at 1:1, erected on the pier tops or inside the abutments; **it must not be loosened or moved** while the arch is being built. Mortared arches cure 7 days after closing (13.4) before the centering is struck; dry-laid arches may be struck the same day. Strike by loosening the wedges first and lowering symmetrically in stages, with settlement difference between the two ends <10 mm.
- **Rough springing thrust calculation**: H (thrust, kg) ≈ W × L ÷ (8 × f). Take W as the total weight (kg) of the half-span arch ring plus fill, L as the clear span (m), f as the rise (m).
  Order-of-magnitude sanity check example: clear span 3 m, rise 1 m, half-span stone plus fill about 1500 kg → H ≈ 1500×3÷8 ≈ 560 kg. The abutment resists thrust by self-weight friction (stone-on-soil friction coefficient taken as 0.5); with a 3× safety factor → **effective abutment weight ≥3.5 t, or embedment ≥1 m into undisturbed soil on both banks** (embedment in rock counts as embedment in soil). Backfill behind the abutment must be compacted in layers — loose backfill tilts the abutment forward and opens diagonal cracks at the crown (settlement-crack interpretation per 13.7).
- **1.5× static-load verification**: same discipline as 7.4 — stack 1.5 times the rated passage load on the crown, let stand 1 h; pass requires crown settlement <5 mm and no new cracks.
- **Outlook register**: arches of 5–8 m clear span need experience with multi-ring arch construction and total falsework lowering, beyond this manual; when the demand is established, transition "beam first, arch later" — erect a temporary timber beam to keep traffic moving, then convert to an arch in place once labor and materials accumulate.

### 54.2.4 Rope bridges (execute 7.12 directly)

Foot crossings with spans ≤10 m follow the 7.12 double-rope suspension bridge specification without exception (main cables 10–16 mm, sag 8–12%, anchor displacement under 1.5× static load <5 cm). This chapter adds three siting rules:

1. **Anchor points must be rock mass or ground piles driven into undisturbed soil** — 7.12 permits wrapping a living tree, but permanent rope bridges use ground piles exclusively (a tree struck by lightning or hollowed by insects is a bridge-collapse accident);
2. **The deck underside must be ≥1 m above the design flood level** (calibration per 54.2.2);
3. Rope bridges **carry people only, never vehicles** — the dynamic impact factor for wheeled loads has not been calibrated and must not be estimated.

### 54.2.5 Bridge deck drainage and railings

- Bridge deck longitudinal gradient ≥1% (falling toward both banks), cross slope ≥2% toward both sides; timber decks leave 20–30 mm board gaps that double as drainage.
- Railing height ≥1 m, post spacing ≤1.5 m; acceptance by a **1.5× crowd lateral load push test** — three people side by side pushing horizontally, top-of-railing displacement <30 mm.
- Bridge approach ramps: within 10 m of each end, the road surface grade difference from the deck must be <3%, preventing vehicles from bumping onto the bridge and hammering the beam ends (approach bumping is the leading cause of beam-end bearing failure).

[Card 54-02 Timber Beam Bridge Construction] (eight fields)

1. **Input materials**: 4–5 fully dried hardwood main beams (120×250×4800 mm, passing the monthly check), 8 cross beams (80×150×1600 mm), deck boards 50 mm, 4 bearing pads (≥400×400×150 mm), 2 pile timbers (φ200×3.5 m, only for soft-soil riverbeds), iron pins and bolts ≥8 kg (Chapter 18).
2. **Tools required**: woodworking chisels, adze, auger, saw (Chapter 7), stretched line, spirit level, and water-bowl level (Chapter 3, cross-checked), hammer and wedges; midspan deflection measured with a long straight template + plumb line.
3. **Sequence and control points**: ① Site the bridge (narrowest riverbed, firm banks) and measure the clear span. ② Excavate the abutments to undisturbed soil and ram in the bearing pads. ③ Set the main beams: end bearing ≥200 mm, four beams leveled by line (mutual difference ≤10 mm). ④ Lay cross beams (spacing 500–600 mm, iron pins or mortise-and-tenon). ⑤ Lay deck boards with 20–30 mm gaps. ⑥ **1.5× static load: stack 1.2 t over a 1 m width at midspan, let stand 1 h, sag ≤40 mm (1/100 of the 4 m span)**. ⑦ Railings and approach ramps.
4. **Empirical parameters and calibration**: select beam depth from the 54.2.1 table; for off-table spans, convert by the deflection law and upsize the beams — first make a short-beam specimen from the same batch of stock and measure sag under stacked load; if deviation from the table value exceeds 30%, correct the selection by measurement and record it in the ledger.
5. **Observations to record**: beam stock numbers and dry weights, leveling readings, static-load sag values; re-measure sag before and after each rainy season — cumulative increase >10 mm is a warning.
6. **Pass / rework / scrap criteria**: pass = both static-load criteria met + 3 fully loaded crossings; rework = sag over the red line but beam bodies intact (add diagonal braces at midspan or add companion beams); scrap = cracking sounds or visible cracks during the static load (replace stock; patching and continued use is not allowed).
7. **Common failures and diagnosis order**: sag grows after opening to traffic → first check for wet stock mixed in (creep) → then check beam-end bearing settlement → then check pinned cross beams working loose (a single beam carrying load alone); approach bumping → check the approach grade difference; beam-end rot → check ponding at the bearings (raise the pads and leave gaps).
8. **L1 / L2 / L3 evidence**: L1 = completion + static-load record; L2 = one flood (or one week of fully loaded traffic) with no anomaly + re-measured sag; L3 = flood-level ledger, annual re-measurement folded into Chapter 39 spot checks, one spare beam in store.

## 54.3 Vehicles

### 54.3.1 Upgrade path: solid wheel → spoked wheel

| Generation | Wheel type | Characteristics and use |
|---|---|---|
| First generation | Solid wooden wheel (three plies of boards cross-laminated and pinned, or a thick cross-grain disc) | Simplest to make, extremely heavy, jarring; journals wear fast; used on ox carts and sledges, speed ≤ walking pace |
| One-and-a-half generation | Rough wooden spoked wheel (spokes plugged straight into hub and rim, no pre-tensioning) | Half the weight; on rough roads the spokes gradually loosen and the wheel goes oval — low speed and short trips only |
| Second generation | Spoked wheel (pre-tensioned assembly + rim segments tenon-joined + shrink-fit iron hoop, shrink-fitting per the Chapter 21 method) | Target form: light, resilient, repairable — spokes and rim segments can both be replaced in the field |

**Wheel diameter**: ox/horse cart wheels φ900–1100 mm, handcart wheels φ500–600 mm (empirical). The larger the diameter, the less draft effort (smaller wheels climb out of potholes worse); the limit is the timber cross-section available for hub and rim — check stock before fixing diameter.

**Spoke assembly and pre-tensioning (the key to the second-generation wheel)**:

1. Hub: φ250–300 mm hardwood, axle bore match-fitted per 54.3.2; cut a wedge notch at the outer end of each spoke hole.
2. Spokes: 12–16, tenoned ends fitting the hub bores, **spokes set dished outward (5–8° from the vertical plane, the "spoke umbrella")** — so side loads do not snap spokes.
3. Rim: 6–8 curved segments tenon-joined into a ring, closed with a shrink-fit iron hoop.
4. **Pre-tensioning**: after each spoke is driven home, drive its wedge and strike to hear the tone — **uniform tone across the whole wheel = uniform pre-tension** (◎ hand-feel; practice method: train the ear 50 times on a batch of spokes with known tightness, checked against disassembly and reassembly; compensation: press each spoke mid-length with the thumb and watch the deflection — the give should feel identical spoke to spoke). A dull note = loose; re-drive the wedge; if the same spoke is still loose after three re-drives, the tenon socket is worn loose — replace the stock.
5. Why pre-tensioning works: **load presses down through the spokes at the top of the wheel, and pre-tension keeps every spoke permanently in compression, never unloading** — in an un-tensioned wheel, spokes hammer in their bores as load reverses, and the wheel goes oval within three months.

### 54.3.2 Axles and bearings (Chapter 21 system)

- **Wooden axles**: turned hardwood (radial runout per the Chapter 21 lower grade: wheel axle ≤0.5 mm), **journals wrapped with iron hoops** — a bare wood journal rubbing a hardwood bush rolls oval within a week (a hard-earned lesson, not an estimate). Hoop shrink-fitting method and acceptance same as the Chapter 21 rim hoops.
- **Iron axles**: wrought-iron square billet forged round (Chapter 18), journals turned on a lathe; four-wheelers rated ≥800 kg use iron axles without exception.
- **Bearings**: sliding system (21.3): slow ox carts use grease-soaked hardwood bushes, heavy fast loads use bronze bushes; bushes scraped to a bearing contact band (21.3 method); **top clearance measured by the lead-wire method, target ≈ 1–1.5‰ of journal diameter** (on a φ40 journal that is 0.04–0.06 mm, with temperature rise and hand-turning both converging).
- **Lubrication regime**: animal fat replenished every half day; temperature rise red line 60 ℃ (wax-chip compensation, 21.3). **Grease before departure, check bush temperature after shutdown** — both entries go into the vehicle ledger.
- **Wheel-end fastening**: large washer + open pin (through pin); **no permanent fastening allowed** — wheel and axle must be separable within 30 min; breaking a wheel in the field and swapping the spare is routine.

### 54.3.3 Steering turntable (front-axle turntable)

A four-wheeler with a fixed front axle cannot turn (54.1.2); four-wheelers must steer on the front axle:

- Structure: a lower turntable fixed at the middle of the front axle, an upper turntable under the frame's front cross-member; between the two plates a friction pair + central pivot (kingpin). Turntables are hardwood with an annular grease groove; the ≥800 kg class uses cast-iron plates (Chapter 17, verified by strike tone).
- Pivot diameter ≥40 mm, tapered fit wedged tight — **the pivot is the vehicle's number-one safety part**; when it breaks, the front wheels wander and the vehicle is effectively out of control. Disassemble and inspect quarterly; replace as soon as a shoulder is worn.
- Steering angle limit ±35–40° (empirical): limit blocks on the turntable keep the wheel felloes from scraping the frame bottom.
- Acceptance: an empty vehicle turns a full circle in place with the front inner wheel leaving no side-slip scuffing; a loaded vehicle turns a 12 m radius circle (the 54.1.2 trunk standard) without the outer front wheel leaving the lane.

### 54.3.4 Load classification and braking (wedge-block brakes)

| Vehicle type | Rated load (empirical, must be field-calibrated) | Accompanying equipment |
|---|---|---|
| Hand-pushed single/two-wheel cart | 80–150 kg | Human power, with parking wedge |
| Two-wheel animal cart (single ox/horse) | 300–500 kg | Wedge-block brake + hand lever |
| Four-wheel animal cart (two animals) | 800–1200 kg | Wedge-block brake per wheel + hand lever, double wedges on grades |

Calibration: measure draft force fully loaded on level ground (Section 25.5 brake-dynamometer method or a spring scale pulling the shafts) and reconcile it with the 54.4.3 draft-efficiency account — a mismatch means the vehicle is too heavy or the bearings too stiff; fix the vehicle before talking about more load.

**Wedge-block braking**: hardwood brake blocks mounted on hinged levers; the hand-lever rod presses the block against the inner face of the felloe (or a foot pedal actuates the same structure). Criterion: **a fully loaded vehicle descending an 8% grade, braked, has stopped wheels and does not creep** (tested in the open on a load-restricted section). Grade discipline: descending >5% requires the brake engaged + a parking wedge pre-placed at the vehicle tail; parking always means wedges under the wheels. Brake-shoe wear checks fold into the vehicle ledger's annual inspection: **replace when the block face is scorched and glossy or 1/3 of its thickness is worn away**.

[Card 54-03 Spoked Wheel Assembly] (eight fields)

1. **Input materials**: 1 hub blank (φ280×280 mm dry hardwood), 16 spokes (φ40×450 mm dry stock, tenons pre-cut, **2 spares**), 8 rim arc segments (60 mm thick, assembling to φ1000), 1 iron hoop (inner diameter = rim outer diameter −1–2 mm interference, forged per Chapter 18), 32 hardwood wedges, 1 set of bronze bushings or grease-soaked wooden liners for the axle bore.
2. **Tools required**: lathe (Chapter 20), chisels and files (Chapter 7), forge and shrink-fit jig (Chapters 18, 21), hammer, stretched line and square; one spare spoke serves as the tapping stick.
3. **Sequence and control points**: ① Turn the hub; match-fit the axle bore, cut the keyway, stamp the number (Chapter 20). ② Lay out 16 equally spaced spoke holes (Chapter 3 method) and cut the wedge notches. ③ **First install the four cross-position spokes for alignment, then fill in diagonally** — after each spoke is inserted, drive the wedge and strike to hear the tone. ④ Fit the rim: spokes into the rim mortises, segments paired and joined. ⑤ **Shrink-fit the iron hoop: heat the hoop to dull cherry-red (Chapter 6 fire colors) and hot-fit; once cooled it must sound solid when struck and a knife tip must not enter the hoop seam**. ⑥ Re-strike the whole wheel; re-drive wedges on any that have gone dull. ⑦ Let stand one day and re-strike (slackening mostly appears in the first day and night).
4. **Empirical parameters and calibration**: spoke-umbrella angle 5–8° — calibration: apply 50 kg side load to the assembled wheel; pass if rim lateral shift <10 mm with no "click" from the spokes; measure the actual angle and enter it in the ledger. Iron hoop interference 1–2 mm — calibration: trial-fit a hoop of the same diameter onto a scrap rim segment; if the cold hoop slips on, interference is insufficient; if the rim cracks during shrink-fitting, interference is excessive; take the middle setting.
5. **Observations to record**: tone grade of each spoke (dull/clear), wedge numbers, re-drive counts; knife-tip test of the hoop seam after shrink-fitting; re-strike results after standing.
6. **Pass / rework / scrap criteria**: pass = uniform tone across the wheel + tight hoop + with the axle installed, hand pressure on the rim gives no wobble and one full turn shows no runout at the axle bore (scriber re-check ≤2 mm); rework = individual loose spokes (re-drive wedges or swap spares); scrap = cracked hub, cracked rim segment, or rim scorched during hoop shrink-fitting (replace that part — glued patches and splicing of wheel parts are not allowed).
7. **Common failures and diagnosis order**: mixed tones across the finished wheel → first check whether the rim failed to close round (segment joints misaligned) → then check wedge notches cut backward (wedges taking no load) → then check for spokes of mixed batch thickness; loose hoop → check the interference setting → check insufficient shrink-fit temperature (hoop not fully expanded); oval feel when the wheel turns → check for unloaded spokes (locate by re-striking, then replace).
8. **L1 / L2 / L3 evidence**: L1 = one wheel assembled + tone records; L2 = full vehicle runs 10 km at rated full load with no spoke re-loosening; L3 = 3 wheels built in a row by the same process with pass rate ≥2/3, spoke spares entered in inventory, angle and interference calibration conclusions entered in the ledger.

## 54.4 Pack gear and harnesses

### 54.4.1 Pack frames and pack saddles (deepening the 10.7 Iron Law)

10.7 already established the Iron Law: **pulling force must land on chest, shoulders, and haunches; throat-strangling neck-collar pulling is forbidden**. Pack gear is the static version of the same Iron Law — where the pack weight presses matters more than how much is packed:

- **Pack saddle**: felt-core saddle pad with a leather face, one **saddle bow** at each end (retaining rims — the front one against sliding back, the rear one against pitching forward); the pad's job is **spreading concentrated pressure into area pressure**. Criterion: no pressure marks or red welts on the animal's back after unsaddling (red marks = uneven contact or flattened padding; refelt and replace the pad).
- **Pack frame**: an A-shaped wooden frame riding on the saddle, cargo lashed to both sides — **cargo never touches the animal's body directly**; chafing and bruising both start with cargo pressed straight against the hide. Frame feet land on the saddle bows and must not hang loose or rock.
- **Straps**: breast strap (against sliding back), belly band (holding the saddle), tail strap (against pitching forward) — all three used together. Belly-band tightness: a flat hand slides in, a fist does not (◎ hand-feel; practice method: trial-insert and compare on three draft animals with known fit, 15 times; compensation: trial-insert a 40 mm thick wooden gauge).
- **Load and rhythm**: long-term pack load ≤1/5 of body weight, short trips ≤1/4 (10.7); half a day's travel, then unsaddle and water; first pack runs start at 1/10 body weight and increase day by day.
- **Chafing check regime**: every day after unsaddling, palpate four spots in a fixed order — front edge of the shoulder blades, back midline, belly-band position, tail root. Red marks: adjust pad position the same day; broken skin: stop packing, dress the wound (treatment in Part 9) until scabbed — **scabbed spots carry no load again**.

### 54.4.2 Harnesses: restating the collar ban and shaft-height matching

**Collar ban restated**: rope or strap pulling around the neck (force passing over the throat's windpipe and carotid arteries) is a **forbidden item** — under a throat-strangling harness the animal suffocates with every effort; this is the primary mechanism behind the 3× efficiency gap in 54.4.3 and the leading cause of animal injury. Step one of any harness acceptance: **the load-bearing strap centerline passes over the rear edge of the shoulder blades and the chest underside, not over neck or throat**.

Two correct routes:

- **Oxen: the yoke (neck yoke)** — a curved crossbar set before the neck and shoulders, with the two shafts or two ropes tied to its ends; the load-bearing surface is the yoke's inner curve where it rests against neck and shoulder, wrapped with soft padding. The inner curve is match-fitted to each ox's neck and numbered (the Chapter 20 match-fitting regime extended to harnesses).
- **Horses and donkeys: the collar harness (chest-shoulder type)** — a ring packed with soft material (felt/hemp) around the neck and shoulders, **load-bearing strap at the rear of the shoulder blades and the chest underside**, with the pull line running down along the rear edge of the shoulder blade; the shoulder strap holds the collar down against riding up. When the inner packing compresses into a hard crust, refurbish it (a hard crust = pressure climbing back up, a chafing source).

**Shaft-height matching (the core fitting number)**: the shafts' load-bearing surface and the animal's shoulder load-bearing point must be **at the same height, within ±30 mm**.

| Shaft condition | Consequence |
|---|---|
| Too high (pull line angles upward) | The yoke rides up and presses the throat, the saddle front presses the shoulder blades — the number-one cause of simultaneous chafing and oxygen deprivation |
| Too low (pull line angles downward) | Shoulders sink, forelegs trip easily, no power on upgrades |
| Correct, ±30 mm | Pull passes along the horizontal through the load-bearing surface, fully converted into effective draft force |

Calibration: check shaft height with the **vehicle empty and stationary** — the shafts should rest level on the load-bearing point without pressing; when loaded the shafts are pressed lower, so leave 20–30 mm of clearance in the empty state (empirical). Register fit data per vehicle per animal; a changed animal means a new fitting.

### 54.4.3 The draft-efficiency account: why good and bad harnesses differ 3-fold

| Harness | Effective draft force (400 kg-class ox, empirical) | Mechanism |
|---|---|---|
| Throat-strangling type (forbidden) | 40–60 kg | Force crosses the throat: every increase in pull cuts off oxygen first — the animal's self-preservation limit locks output at small draft forces; long-term use permanently damages the throat |
| Chest-shoulder type (yoke/collar) | 120–150 kg | Load-bearing surface of hundreds of cm², low pressure, breathing unobstructed — sustains horizontal draft force ≈ 30–35% of body weight |

The 3× gap is not a materials gap, it is a **physiological pathway gap**: one fights breathing for the pathway, the other yields breathing its own path. Calibration: have good and bad harnesses each pull the same load (1/2 rated) over the same 100 m section, recording time and rest stops — halved time and zero rest stops under the chest-shoulder type is the typical result; convert draft force × distance ÷ time into effective power and cross-check against the Chapter 21 figure of 0.5–0.7 kW animal power. **One animal in a mis-matched harness equals losing two animals — harness fitting is the highest-return labor in this chapter.**

[Card 54-04 Harness Assembly] (eight fields)

1. **Input materials**: 1 collar harness or yoke (selected by the animal's neck circumference and shoulder width, 2 blanks in reserve), felt/hemp lining material, leather straps and buckles (Chapter 15 leatherwork, stitched joints staggered), 1 pair of shafts (already mounted on the vehicle).
2. **Tools required**: tape measure (for neck and chest girths), straightedge, spirit level; cross-check levels before use.
3. **Sequence and control points**: ① Measure the animal: neck circumference, shoulder-blade height and width, chest underside position; enter on the animal's record sheet. ② Select and match the collar/yoke: load-bearing strap centerline aligned to the rear edge of the shoulder blades, **pull line not crossing neck or throat** (visual + finger probe: lower edge of the load-bearing strap at least one hand-width above the throat position). ③ Fit the harness: smooth the lining face, strap tension per the 54.4.1 three-strap standard. ④ **Shaft height: with the vehicle empty and at rest, the shafts' load-bearing surface level with the shoulder load-bearing point within ±30 mm**, loaded clearance 20–30 mm; check level with a spirit level held against the shafts. ⑤ Trial pulls: empty 50 m → half load 100 m → full load 100 m; after each stage palpate the load-bearing surface and the four chafing points. ⑥ Enter data (number of shaft spacers, lining thickness, buckle hole position) on the animal's record sheet and tag the pair with numbers.
4. **Empirical parameters and calibration**: shafts ±30 mm, clearance 20–30 mm — calibration: try spacers in 10 mm steps; converged when felt indentation on the load-bearing surface is uniform after trial pulls (no spot compressed through); belly band by the 40 mm gauge trial insert.
5. **Observations to record**: indentation positions and depths after each trial-pull stage, the animal's breathing and gait (panting = load-bearing strap obstructing breathing, stop immediately), willingness to rest; all entered on the record sheet.
6. **Pass / rework / scrap criteria**: pass = 100 m fully loaded with no rest stops, uniform indentation on the load-bearing surface, no red marks after removal; rework = indentation concentrated in one spot (adjust lining thickness/spacers and re-try); scrap = collar or yoke body cracked, lining core caked and beyond refurbishing (replace the part and refit).
7. **Common failures and diagnosis order**: animal refuses to move during trial pulls → first check whether the load-bearing strap presses the throat (finger probe) → then check whether the shafts are too high and angling up → then check hoof and leg injuries (to exclude non-harness causes); one-sided chafing → check the left-right height difference of the shafts and the symmetry of the yoke holes; frequent head-tossing mid-pull → check whether the shoulder strap is too tight and pressing the neck.
8. **L1 / L2 / L3 evidence**: L1 = one animal one vehicle fitted + record sheet; L2 = the same fit runs 10 consecutive working days with no chafing red marks; L3 = all draft animals fitted, per-animal records in the ledger, quarterly re-fitting regime (lining replacement cycle) established.

## 54.5 Water transport reinforcement

### 54.5.1 Canals and locks [background/outlook; registered only, not chartered]

Concept registration: moving bulk goods by boat costs an order of magnitude less energy than by cart; a canal extends that advantage to places without natural waterways. Two components: **contour routing** (the channel follows the contours, its bed nearly level) and **the lock** (lock chamber + two gates, upstream and downstream + filling ports — boat enters the chamber, close the upstream gate, release water down to the downstream level, exit through the downstream gate; water-level differences descend in steps).

**Why it is not chartered — order-of-magnitude sanity check**: a minimal canal, 3 m bottom width and 1.5 m water depth, moves ≈ 3×1.5×1000×1.2 (trapezoid correction) = 5400 m³ of earthwork per km; at 1.5–2.5 m³/person·day for digging, hauling, and ramming (empirical) → **2000–3600 person-days per km**. Against 37.3: a 300-person settlement frees only 15–45 full-time workers — a 10 km canal would consume more than a year of the whole settlement's construction labor. Lock gates also drag in planking, water sealing, and operating hardware (Chapter 22 standard-part class). **Re-evaluation conditions (all must hold before chartering)**: annual freight demand above the 500 t·10 km order, ≥2000 people mobilized, and the road network already at full capacity. Transitional scheme: on rapid sections of natural rivers, build **bank towpaths** (capstan + towpath, equipment per 54.5.2); earthwork drops by two orders of magnitude.

### 54.5.2 Docks and cargo handling

- **Siting**: stable bank slope, yard space above flood level, main current hugging the bank; water depth = light-loaded draft + 500 mm.
- **Two structure types**: ramp dock (stone-slab ramp on the bank slope, grade ≤1:4); pile trestle (timber piles per 54.2.2, gangplank lapped onto the bow). Select gangplank thickness from the 54.2.1 table (the 2 m entry suffices); **1.5× static load per the 7.4 discipline**.
- **Capstan**: vertical push-bar capstan; ratchet backstop per the 21.11 ratchet mechanism (pawl tips 45–60°, hardened per that specification); rope diameter per Chapter 7 working load = breaking value ÷ 5; drum diameter ≥ rope diameter × 20 (small diameters abuse rope).
- **Lifting boom**: wooden inclined mast + pulley block at the top + capstan; rated lift = rope working load × number of effective rope parts × 0.8 (pulley friction derating, empirical); lifting per the 7.12 three-point discipline (trial lift 10 cm, sling angle <120°, no one standing below).
- **Yard discipline**: yard surface paved with stone or compacted crushed stone (no vehicles bogging down in the rainy season); stack height limited, 1 m gangways between stacks (same lineage as the 13.7 fuel-store discipline); loading and unloading entered in the Chapter 38 materials account.

## Parameter summary table

| Parameter | Empirical value | Calibration method | Section |
|---|---|---|---|
| Road crown cross slope | 2–4% (take the upper limit on earth roads) | No standing water 30 min after rain | 54.1.1 |
| Trunk-road grade limit | 8% (5–8% load-restricted) | Measured with the rope; eyeballing forbidden | 54.1.2 |
| Trunk minimum turning radius | ≥12 m; 1.5–2 times vehicle length | Empty vehicle turns a circle; measure to the front outer wheel rut | 54.1.2 |
| Wheel track (uniform network-wide) | 1400 mm | Set by the mainline vehicle type, entered in the ledger unchanged | 54.1.2 |
| Timber beam bridge span–depth | 2–4 m→250 mm; 4–6 m→400 mm | Corrected by short-beam specimen stacked-load tests | 54.2.1 |
| Deflection red line | span/100 | 25.8 deflection law + measurement | 54.2.1 |
| Stone arch ring thickness | ≥1/10 of clear span | Back-checked against cracking in built arches | 54.2.3 |
| Springing thrust | H ≈ W×L/(8f); effective abutment weight ≥3× H | Weigh the half-span and substitute into the formula | 54.2.3 |
| Spoke-umbrella angle | 5–8° | 50 kg side load, lateral shift <10 mm | 54.3.1 |
| Bush top clearance | 1–1.5‰ of journal diameter (lead-wire method) | Temperature rise ≤60 ℃ + smooth hand-turning | 54.3.2 |
| Two-wheel animal cart rating | 300–500 kg | Draft force measured per 25.5 | 54.3.4 |
| Four-wheel cart rating | 800–1200 kg | Same | 54.3.4 |
| Braking criterion | Full load on an 8% grade: braked to a stop without creeping | Tested in the open on a load-restricted section | 54.3.4 |
| Long-term pack load | ≤1/5 body weight | Incremental trial runs per 10.7 | 54.4.1 |
| Shaft height difference | ±30 mm; empty clearance 20–30 mm | Spacers tried in 10 mm steps | 54.4.2 |
| Chest-shoulder effective draft force | 30–35% of body weight | Same animal, same road, good vs. bad harness | 54.4.3 |

(Side ditch longitudinal gradient 0.5%, rut depth 50 mm, rope bridges ≤10 m, railing push test, steering limit ±35–40°, drum diameter ≥20× rope diameter, and similar parameters are already in their sections and not repeated here.)

## Failure modes and diagnostics

Ordered by "most common, hardest to detect". **Harness misfit and soaked subgrade are the two great silent failures**: the first surfaces as season-by-season decline in draft power (the animal cannot complain), the second as next year's mud pumping.

| Symptom | Candidate causes | Verification | Remedy | Prevention |
|---|---|---|---|---|
| Draft power "weakens", cannot pull former loads | Harness chafing (load-bearing-surface indentations/red marks); shafts too high, throat-strangling | Unharness and palpate the four spots; check load-bearing strap position | Adjust padding, re-fit; broken skin means standing down | Card 54-04 per-animal records + daily palpation |
| Widespread mud pumping the second year | Blocked ditches or flattened crown (invisible the first year) | Check standing water 30 min after rain; walk the ditches end to end | Excavate and replace pumping sections, re-crown, open the ditches | Card 54-01 pre-rain ditch-clearing regime |
| Timber bridge sag grows year by year | Wet-stock beam creep; beam-end bearing settlement | Compare dry-weight records; check pad settlement | Add a middle post or companion beams; re-embed pads | Dry-stock verification (checklist item 2) |
| Wheel goes oval, vehicle runs with a rhythmic clatter | Uneven spoke pre-tension; wedges slackening back | Strike-tone check spoke by spoke | Re-drive wedges, replace spokes | Card 54-03 uniform-tone acceptance + standing re-strike |
| Axle runs hot (too hot to touch) | Lubrication cut off; top clearance too small; uneven bush wear | Re-grease and re-check temperature; re-measure by lead wire | Wash the bush, renew grease, re-scrape | Grease-before-departure + temperature-check-after-shift regime |
| Tail swings in turns, outer wheel scuffs its rut | Loose turntable; pivot wear | Rock the front axle and listen for slop; disassemble and check the pivot shoulder | Replace pivot; rework turntable friction faces | Quarterly pivot disassembly inspection |
| Cannot stop on grades (most dangerous) | Glazed block faces; overloading on restricted sections | Check block face gloss and thickness; audit load records | Replace block faces; enforce load-restricted classification | Annual block-thickness inspection + double-wedge grade discipline |
| Flood topples bridge piers | Scour hollowing pier feet (invisible above the waterline) | After the water recedes, probe around the piles (rod probing) | Riprap reinforcement, restore cutwater | Probe pier feet after every flood |
| Diagonal cracks appear at the arch crown | Abutment tilting backward (loose backfill) | Point the cracks with mortar, date and observe | Grout and compact behind the abutment; patch cracks after movement stabilizes | Settlement-crack interpretation per 13.7; layer-compacted backfill |

## Process card index

| Card number | Name | Purpose | Copy to workstation |
|---|---|---|---|
| 54-01 | Roadbed construction | Three-layer method for the 100 m standard section and rainy-season criteria | Road-building section |
| 54-02 | Timber beam bridge construction | 4 m standard-span selection, erection, and static-load acceptance | Bridge crew |
| 54-03 | Spoked wheel assembly | Pre-tension strike-tone method and shrink-fit iron hoop | Cart workshop |
| 54-04 | Harness assembly | Per-animal per-vehicle load-bearing-point matching and the chafing defense line | Draft-animal team |

Card positions: 54-01 at the end of 54.1, 54-02 at the end of 54.2, 54-03 at the end of 54.3, 54-04 at the end of 54.4. All four cards carry the full eight fields and can be copied one page each for the workstation; the chapter parameter table governs when copying.

## Acceptance criteria L1/L2/L3

| Level | Criteria | Test conditions | Evidence kept |
|---|---|---|---|
| L1 | One ≥100 m branch-road subgrade, one timber beam bridge (both static-load criteria met), one spoked wheel, one animal-vehicle fitting complete | All eight fields of each card filled | Four card records + completion data |
| L2 | Road section passes one rainy season with mud pumping ≤5%; bridge passes a flood or a week of full load with no anomaly; wheel runs 10 km on the full vehicle at full load with no re-loosening; fit runs 10 consecutive working days with no chafing | Re-measured on the same basis | Rainy-season ledger, re-measured sag records, chafing inspection sheets |
| L3 | Road network classification map and maintenance responsibility roster on file; bridge under annual spot check folded into Chapter 39; vehicle ledger includes annual inspection; harness per-animal records + quarterly re-fitting; deflection, interference, shaft-height-difference calibration conclusions entered in the ledger (Chapter 43) | Reproducible from records by a different person in a different season | Two-season records, spare beam/wheel/wedge inventory, calibration ledger |

## Labor, staffing, and consumption

| Item | Headcount and duration (empirical) | Notes |
|---|---|---|
| Branch-road subgrade 100 m (with ditches) | 4–6 people × 8–12 days | Stone quarrying and hauling is half of it; crushed-stone stockpiling adds 1–2 person-days/m³ |
| One timber beam bridge (4 m span) | 3–4 people × 10–15 days | Abutment earthwork extra depending on bank slope |
| One stone arch bridge (3 m span, dry-laid) | 4–6 people × 25–40 days | Voussoir dressing takes most of the schedule |
| One spoked wheel (including hub turning) | 1–2 people × 3–5 days | Double for the first one (templates and trial-and-error) |
| One complete vehicle (four-wheel, including its two wheels) | 2 people × 20–30 days | Excludes metal-forging labor (counted separately, Chapter 18) |
| Fitting one harness set | 1 person × 1–2 days | Trial pulls and record keeping take half |
| Lubricating fat | Axles replenished every half day | Entered on the Chapter 38 ledger consumption page |

## Safety boundaries

1. **Grade Iron Law**: descending a grade >5% requires the brake engaged + a parking wedge pre-placed at the vehicle tail; heavy loads are prohibited above 8%. Parking always means a wedge under the wheels — "the hand lever is on" is not parking (shoe rebound means the vehicle rolls).
2. **Shrink-fit hoops and lifting**: shrink-fitting per the Chapter 6 fire colors, clearing dry grass from the work area and keeping water at hand; lifting per the 7.12 three-point discipline, no one standing below during raises and lowers.
3. **No stopping on bridges**: fully loaded vehicles must not halt or pass one another on the deck; single-lane bridges carry one vehicle one direction at a time, with a lookout-and-hail system at the bridge heads.
4. **Rope bridges carry people only, never vehicles**; flooded sections and overtopped causeways are closed without exception, reopening after the water recedes and silt is cleared.
5. **Draft-animal welfare is safety**: broken skin means standing down, scabs do not restore duty — an injured animal that startles and jumps flips vehicles; this is discipline, not a humanitarian option.

## A/B/C three lists

**List A (executable directly in this chapter):**

| Item | Criteria |
|---|---|
| One branch-road subgrade section | Card 54-01, all eight fields complete, accepted by 3 fully loaded passes |
| One timber beam bridge | Card 54-02, both 1.5× static-load criteria met |
| One spoked wheel | Card 54-03, uniform tone + tight hoop |
| One animal one vehicle fitting | Card 54-04, 100 m fully loaded with no chafing |
| Rainy-season maintenance schedule | Before/during/after-rain three-phase actions + responsibility roster on the wall |

**List B (requires upstream chapter outputs):**

| Item | Prerequisite |
|---|---|
| Iron axles, iron hoops, wedges | Chapters 17, 18, 21 forging and shrink-fitting |
| Mortared arches and abutment masonry | Chapter 13 mortar and test-cube regime |
| Lathe turning of hubs and journals | Chapter 20 |
| Lead-wire clearance measurement, bush scraping to contact band | Chapter 21 bearing system |
| Static-load verification and the deflection law | Chapter 7 (7.4), Chapter 25 (25.8) |
| Ratchet capstan | Chapter 21 (21.11) |
| Labor accounts and maintenance responsibility roster | Chapter 37 |

**List C (external dependencies and irreducibles):**

| Item | Notes |
|---|---|
| Draft animals registered with trial-run records | Chapter 10 (10.7); without animals, this part's cart transport drops to human pushing |
| Fully dried hardwood supply | Chapter 7; wet stock is an outright veto |
| Stone and lime | Local sources passing strike inspection |
| Historical knowledge of flood levels | Ask the oldest residents + mud marks and vegetation lines; the error cannot be eliminated — hedge by building bridges higher |
| Floods, bank collapses, epidemic losses of draft animals | Unpredictable; hedged partly by spare beams and wheels and by shared responsibility rosters |

## Downstream dependencies

- **Chapters 37–39 (organization and maintenance)**: section-by-section responsibility assignments, vehicle annual inspections, and bridge spot checks fold into their ledgers and spot-check regimes — this chapter supplies "what to inspect"; "who inspects, how often" belongs to Chapter 37.
- **Chapter 38 materials-and-energy ledger**: the freight page (converted to t·km) is benchmarked on this chapter's load classification and draft-force account; canal re-evaluation accounting also runs through that ledger.
- **Chapters 50–53 (environment editions)**: the rainforest edition prioritizes rope bridges and pile trestle walkways; the permafrost edition handles subgrade thaw settlement (raising the bed + timber-mat base course); the desert edition prioritizes the pack-gear line (building roads without water is uneconomic). Each environment recomputes grades and load tables by this chapter's methods; copying verbatim is not allowed.
- **Chapter 22 (standard parts)**: once wheel track, axle diameters, and pin diameters enter the ledger they are managed as standard parts — the road network lasts 30 years; vehicle-generation changes must not alter the wheel track.
