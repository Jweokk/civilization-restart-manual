# Chapter 39 Maintenance, Spare Parts, Life, and Quality Traceability

## Chapter Objectives

After finishing this chapter, a settlement should be able to produce four documents and run them at the workstations:

| Document | Contents | Purpose |
|---|---|---|
| Equipment spot-inspection sheets | Daily/weekly/monthly/annual four-tier inspection sheets; every item states "what to check, how to check, condemnation criteria" | So that wear, corrosion, and fatigue are seen before they become accidents |
| Spare-parts ledger | Class A/B/C three-tier spare-part classification, minimum stock quantities, and inspection records of the stocked parts themselves | When a part must be replaced, a part is on hand—and it is a good one |
| Life calibration table | the Section 39.4 empirical life table + measured columns for this settlement, heat by heat and piece by piece | Upgrades "empirical values" into "this settlement's numbers," supporting production scheduling and spare-part minimums |
| Failure-analysis archive | three-tier batch numbers, the failed-sample library, five-step-method analysis sheets, and process-card version change records | The same kind of bad part fails only once; knowledge lives in the archive, not in personal memory |

## Capability Boundaries

**Can do:**

- Establish the three institutions—spot inspection, spare parts, quality traceability—and tie them to the Chapter 37 shift roster and the Chapter 38 ledger.
- Use the five senses (look, listen, touch, smell, compare) plus simple tools (feeler gauge, steel rule, wax chips, kerosene and chalk powder, magnet, scale) to find observable precursors of wear, corrosion, and fatigue.
- Use ledger measurements to calibrate every line of the Section 39.4 empirical life table into the settlement's own life data.

**Cannot do:**

- **Nondestructive testing**: ultrasonics, magnetic particles, penetrant dye, and X-rays are all unavailable (they depend, respectively, on the electronics industry and high-pressure equipment; no route exists before Chapter 33). Internal cracks and subsurface inclusions can only be handled by the kerosene-chalk method for surface-opening cracks plus post-hoc fracture-face reading; unopened internal defects cannot be found.
- **Precise life calculation**: the stress–cycle curve of fatigue life (the S-N curve) requires controlled-load testing of hundreds of specimens; this stage has no such capability. This chapter does not predict "how many more hours this shaft can turn"; it does two things only: keep hours in the ledger, and condemn on precursors.
- **Online monitoring**: there are no continuous-recording instruments. Temperature is measured only "at the moment of inspection"; clearance only "at the moment of shutdown." Degradation between inspections is hedged by shortening periods, not by instruments.

**External dependencies (counted in the C List):**

1. A continuous small-scale supply of lubricating grease and oil (animal fat, vegetable oil, graphite—Chapters 8, 15). Without grease there is no steady-wear period for a sliding pair; bearing life is cut by half or more.
2. ≥1 year of local humidity, freeze–thaw, and acid-mist exposure records—the foundation for calibrating corrosion rates; without this line, all anti-corrosion periods are temporary numbers.

## Pre-Start Verification

Checklist format. If any item is unmet, the corresponding institution runs on a "temporary period" first and marks it in the sheet header; life figures must not be extrapolated from it.

| # | Verification item | Criterion (confirm you have X in hand; the standard is Y) |
|---|---|---|
| 1 | Equipment register | Every furnace, kiln, machine tool, waterwheel, and bellows has a number (e.g., JC-01, Machine No. 1) and a current-status mark (in use / awaiting repair / mothballed) |
| 2 | Existing tool archive | The Chapter 19 cutting-tool archive is on the books: every piece has a number, material batch number, and regrind count; unarchived tools are marked "unverified items" |
| 3 | Operating ledger | Each machine has accumulated operating hours (or heats, kiln firings) on record; if none, this table starts from zero |
| 4 | Weights and measures | Feeler gauge (Chapter 20), steel rule, scale, and calipers mutually cross-checked (Chapters 3, 22); wax chips prepared (thin slices of beeswax or mineral wax) |
| 5 | Accounts-office linkage | The Chapter 37 accounts-office monthly stocktake is running, and the spare-parts store can be hooked into the stocktake |
| 6 | Maintenance responsible person | Every machine has a named inspection owner on the shift roster, skill Grade 2 (Section 37.5) or above; the annual inspection must be chaired by a Grade 3 |
| 7 | Anti-corrosion materials | Grease, oiled paper / waxed-cloth wraps, and dunnage in stock; stock quantities per the Section 39.3 Class-C consumables table |
| 8 | Failed-sample shelf | A shelf or cabinet has been set aside (dry, sheltered from rain, adequate load capacity); the tagging rules are in Section 39.6.3 |

## 39.1 Three Ways Machines Die: Wear, Corrosion, Fatigue

All failures of human-made artifacts are classified, in this chapter's framework, as three ways of dying. If you cannot tell the modes apart, you will treat fatigue as wear and "tighten up the clearance," or treat corrosion as fatigue and "fit a new shaft"—and the new shaft breaks again three months later. Learn to identify first; talk about inspection and spares after.

| Death mode | Mechanism | Typical sites | Development speed | Inspection focus |
|---|---|---|---|---|
| Wear | gradual loss of surface material from a friction pair | journal–bearing, saddle–guideway, nut–lead screw, piston–bellows wall, cutting edges | chronic: months to years | clearance, accuracy, wear debris, sound |
| Corrosion | chemical or electrochemical dissolution of the surface | furnace and kiln steel parts, ironwork in acid-mist areas, sweaty fingerprints, dissimilar-metal contact faces, items in storage | slower but never stops: it rusts even while shut down | surface products, weight loss, remaining cross-section |
| Fatigue | crack initiation and growth under alternating stress, sudden fracture | shafts, springs, chains, slings, gear tooth roots, bellows links | latent without signs, breaks in an instant | cracks, sudden deformation change, dead sound, the hours ledger |

### 39.1.1 Wear: The Chronic Death of Friction Pairs

Wear occurs on a **pair** of surfaces; it is not a disease of a single part: as the journal wears thin, the bearing bore wears large, and the clearance is the sum of both wears. Development has three stages: the run-in period (a new pair's initial wear, clearance rises slightly—normal), the steady period (extremely slow wear, ninety percent of life), and the accelerating period (clearance large enough for impact loading, wear avalanches). The entire meaning of inspection is to intervene before the accelerating period.

**Visible precursors (field observation methods):**

1. **Clearance growth**: with the machine stopped, rock the part radially by hand—from "just perceptible" to "obviously loose" (the Chapter 20 acceptance for a scraped bearing is about 0.05–0.1 mm; empirical value, must be field-calibrated). Quantify with feeler blades or the lead-wire crush (place a lead wire between journal and bearing, turn half a revolution, remove, and measure its thickness).
2. **Accuracy decline**: on the machine tool, turn the same test bar in the same chuck, and the diameter difference between the two ends (taper) grows month by month; re-measure the lead screw's thread-cutting tooth-by-tooth error table (Chapter 20, Section 20.9). A pitch error exceeding 1.5 times the original table means the guideways or lead screw are worn beyond limits.
3. **Wear debris in the oil**: draw oil from the bearing housing's oil port and pick up the sludge with a magnet—in the steady period it comes out as gray-black fine mud; shiny flakes or obvious iron filings mean the accelerating period has begun. Quantification: once a month, take the magnet-picked sludge from the same spot, shade-dry and weigh it, and enter it in the ledger.
4. **Sound change**: a sliding pair goes from "sh-sh" to "clack-clack" (clearance impact). There are no rolling bearings in this framework, but gears behave the same way, going from a continuous hum to knocking.

◎ Judging clearance by ear is a hand-feel step. Practice: on the same machine, listen 10 times each just after overhaul, in the steady period, and just before the limit is exceeded, to build your own "scale of sounds." Misjudgment compensation: whenever sound is in doubt, always return to the lead-wire crush to measure clearance—hand feel is only for screening "this needs measuring now," never for waiving measurement.

### 39.1.2 Corrosion: The Death That Never Stops

Corrosion runs on two tracks. Chemical corrosion: acid mist, salt fog, and high-temperature oxidation directly dissolve the surface—the ironwork of the distillation workshop (Chapter 26), all steel on islands and salt works (Chapter 52), the high-temperature scale on furnace-door steel. Electrochemical corrosion: a water film plus two metals in contact (copper–iron, or iron from different heats) forms a galvanic cell, and the contact seams rot fastest—riveted seams, copper gaskets on iron shells, sweaty fingerprints (salt) leaving rust.

**Visible precursors:**

1. **Surface products**: iron's red-brown rust layering and peeling, copper's green patina, white bloom on lead-gray parts, varnish-like tackiness in wood-ash (potash) areas. Condemnation looks at depth, not area: after scraping off the rust scale, measure the remaining cross-section with calipers; a stressed part with >10% section loss is condemned (empirical value, must be field-calibrated; calibration method: load-test three same-batch pieces at different rust depths, with the Chapter 19 scratch sequence as auxiliary confirmation that the material itself is unchanged).
2. **Weight loss**: the **coupon method**—3–5 thin iron sheets from one batch, numbered and weighed (precision 0.1 g, Chapter 22), hung at four points: beside the furnace, in the acid-mist workshop, in the storeroom, and in the open air. Each month remove them, pickle off the rust (soak in dilute acetic acid, rinse in clean water, dry), and reweigh. This yields each workshop's monthly corrosion rate (g/dm²·month), convertible into a penetration speed. Any workshop whose coupon loses >0.05 g/dm² per month (empirical value) halves the inspection period for its ironwork.
3. **Cross-section loss and seizure**: a bolt rusted solid and twisted off inside its hole is the costliest corrosion failure. The precursor is rust nodules on the threads and "it won't turn"—when it won't turn, hard twisting is forbidden; first soak with oil (kerosene or hot grease) for 24 h, then work it back.

Three anti-corrosion methods (write them into the inspection sheet): grease-and-wrap preservation for idle items (grease the whole piece + wrap in oiled paper); off-floor, off-wall storage on wooden dunnage (a damp storeroom floor is the number-one killer of stocked parts); leather or greased separator layers at dissimilar-metal contacts.

### 39.1.3 Fatigue: Sudden Death Without Warning

For parts under alternating load (a rotating shaft takes one bending cycle per revolution, a spring one tension–compression cycle per stroke, a chain one impact per engagement), cracks initiate at surface stress concentrations (keyway corners, section steps, old scratches), grow slowly, the remaining cross-section shrinks and shrinks, and then in one instant comes brittle fracture—**almost no deformation before breaking**. This is the fundamental difference between fatigue and wear or overload. So fatigue inspection is not about "measuring clearance" but about "finding cracks" and "counting hours."

**Visible precursors:**

1. **Surface cracks—the kerosene-chalk method**: clean the suspected spot, brush with kerosene and let it soak 10–15 min, wipe dry, brush on a coat of chalk slurry (lime slurry works as a substitute); kerosene seeps out of the crack, showing a dark hairline. This method only finds cracks **open to the surface**; depth is unknown—find one and condemn; do not gamble.
2. **Sudden deformation change**: early fatigue often shows as slight bending first. The belt suddenly drifts, gear meshing suddenly bottoms at the tooth roots, a seal suddenly wears off-center—check the shaft that carries them: run a dial indicator against the shaft through one full turn (Chapter 27); radial runout >0.2 mm (empirical value, must be field-calibrated) → stop the machine and inspect.
3. **Sound deadening**: a sound piece rings bright with a long sustain; a cracked piece sounds hoarse and muffled with short sustain. ◎ Strike-listening is a hand-feel step. Practice: strike a known-good shaft and its fractured counterpart 20 times each, and compare. Misjudgment compensation: any audible suspicion goes straight to the kerosene-chalk method; never close the case on hearing alone.
4. **Fracture-face reading (afterward, for failure analysis)**: a flat, smooth fracture face with arc-shaped "beach marks" spreading from one edge point = fatigue (beach marks are the growth rings of the crack advancing cycle by cycle); a rough, fully crystalline, glittering face = brittle fracture; a dull, fibrous face with obvious necking = ductile overload fracture. The fracture-reading conclusion goes directly into step 5 of Card 39-02.

Fatigue's management tool is the **hours ledger**, not instruments: accumulate operating hours for each machine (blast furnace by heats, chains by tonnes hoisted); as a part approaches the lower bound of its life interval in the table, double the inspection period (monthly inspection escalates to a ten-day inspection). This is the other half of the reason the Section 39.2 daily inspection exists—the daily check both looks for wear and keeps time for fatigue.

## 39.2 The Inspection Institution: Tiered Inspection Sheets

### 39.2.1 Four-Tier Periods and Responsible Persons

| Tier | Period | Performed by | Time | Scope |
|---|---|---|---|---|
| Daily | before start-up each shift | operator (Grade 1 suffices) | ≤10 min | the four acts—look, listen, touch, record: oil level, abnormal noise, temperature, obvious damage |
| Weekly | once a week | workshop master or Grade-2 worker | half a day | all daily items + hand-feel clearance + magnet pick of wear debris + cutting-tool archive check + walk-through of stocked parts |
| Monthly | same day each month as the accounts-office stocktake | Grade-2 worker + accounts office | 1 day | all weekly items + quantitative measurement (feeler gauge, lead-wire crush, coupon weighing, test-bar turning) + spare-parts stocktake |
| Annual | yearly shutdown | chaired by a Grade 3, all hands take part | 3–5 days | teardown inspection, accuracy re-measurement (guideway scraping point counts, remaking the lead-screw error table), furnace-lining major-repair assessment, life-table calibration summary |

Principle: **periods may only be shortened, never lengthened**; the grounds for shortening (abnormal precursors) are recorded at the foot of the sheet. Lengthening a period must go through the Section 39.7 change-control dual signature.

### 39.2.2 Object Inspection Sheet (what to check / how to check / condemnation criteria)

| Object | What to check | How to check | Condemnation criteria |
|---|---|---|---|
| Furnace/kiln lining | cracks, spalling, erosion depth | after shutdown and cooling, lamp-light the inner wall and scribe each zone with a steel rod (slag line, tuyere zone, hearth bottom); compare against the new lining's baseline scribe marks | crack wider than 5 mm or deeper than 30 mm; slag-line erosion deeper than 1/3 of wall thickness; either one reached → patch the furnace or relinish the lining. Empirical life 3–8 campaigns (see Section 39.4), recorded heat by heat |
| Tuyere ceramic tubes | end burn-through, blockage, cracking | shut off blast, pull out, inspect visually; measure the end's inner diameter | bore enlarged >1/3 (burn-through) or cracked to the point of air leakage → swap in the spare tube (the Chapter 18 keep-2-spares rule) |
| Bellows | flap seals, valve plates, housing cracks | press the valve plates by hand to check seating; hold a candle near the seams and watch for the flame being sucked in (air leak); listen for creaking of the housing (wood cracking) | flaps hardened and cracked, seating gap >1 mm → replace flaps (Class-C spare); housing crack leaking longer than 10 cm → tear down and repair |
| Machine-tool guideways | scraping point count, scratches, rust | annual: straightedge bridge + point-revealing spotting rub (the Chapter 20 method), count points per 25×25 mm | dropped from 8–12 points (first-tier baseline) to <6, or a scratch deeper than 0.2 mm running longer than 50 mm → re-scrape (Chapter 20), not scrap |
| Machine-tool spindle and bearings | temperature, clearance, abnormal noise | after 30 min of running, the back of the hand on the bearing housing tolerable for 3 s ≈ within 60 °C (◎; compensation: press on a wax chip—wax softens without melting ≈55–60 °C, Chapter 20); with the machine stopped, measure clearance by lead-wire crush | over 60 °C → stop immediately and run the three checks (clearance, oil groove, alignment); clearance >0.3 mm (empirical value, must be field-calibrated) → re-scrape the bearing |
| Lead screw and nut | pitch error, thread-flank wear | remake the error table at annual inspection: measure the total length of 10 threads with a steel rule ÷10 (Chapter 20), compare against the original table | any section's average pitch error >1.5 times the original table → downgrade (Section 39.5) to an ordinary power-transmission lead screw; a new master lead screw is made separately |
| Cutting tools | edge chipping, edge curling, hardness | visual check at every return to the store + file test (Chapter 19: press a standard file on the edge; it bites and cuts shavings = too soft) | chipped edge >2 mm, or regrind count in the Chapter 19 archive at its cap → condemned per Chapter 19: re-quench or return to furnace |
| Waterwheel | bearing-bush wear, blade erosion, timber rot | weekly: listen at the bushes (a clack = dry running or big clearance); monthly: feel the bushes' temperature rise (a water-cooled part should be near water temperature); annual: shut the water, drain, inspect the timber | bush clearance >3 mm (empirical value, must be field-calibrated) → replace the bush; blade erosion deeper than 1/4 of timber thickness → replace the blade; timber condemned per Chapter 13 timber construction |
| Gears | tooth-face pitting, broken teeth, backlash | inspect tooth faces visually (pits merging into patches = pitting advancing); roll against red-lead powder to read the contact pattern; measure backlash with the feeler gauge | a single tooth broken → replace the wheel (wooden wheels can take a single-tooth insert, Chapter 21); pits covering >1/3 of the tooth face, or backlash >0.5 mm (empirical value, must be field-calibrated) → replace the wheel or flip it for reversed use |
| Building roofs | rain leaks, displaced tiles, rotten rafters | before the rainy season, go up and check room by room; in rain, map the damp stains from inside | more than 3 adjoining rafters rotted, or load-bearing sag exceeding 1/100 of rafter length → replace rafters per Chapter 13 |
| Drainage | ditch silting, foundations soaking | within 2 h after rain, check for standing-water points; when a ditch's depth is halved, dredge it | workshop floor staying damp for more than 3 days → check drainage and the underlayer, to prevent equipment foot rot and rust |

### 39.2.3 The Five-Sense Inspection Method

Look (cracks, rust color, wear debris, drift) → listen (abnormal noise, dead sound, strike sustain) → touch (temperature, vibration, looseness) → smell (scorched odor = lubrication failure; sour odor = corrosion environment worsening) → compare (against last month's numbers, against spare parts, against identical machines). **Comparison is the chief of the five senses**: a single reading becomes information only when placed into a ledger series. The daily sheet accepts only numbers or "no abnormality seen + signature"; writing the bare word "normal" and being done with it is forbidden—this is precisely the root disease named in the first row of the failure-modes table.

[Card 39-01 Equipment Inspection Card (with period-table template)] (eight fields)

1. **Input materials**: the equipment register (every unit numbered); grease (Chapters 8, 15); chalk or lime wash and kerosene (for oil-stain crack reveal); paper forms or a chalkboard.
2. **Required tools**: feeler gauges and lead wire, steel rule, calipers (Chapter 22, cross-checked before use), wax sheet, magnet, small hammer, lamp. Accuracy needed: 0.1 mm-class calipers suffice; home-made feeler leaves are each checked for thickness against the calipers.
3. **Operating sequence and control points**: (1) work through the register unit by unit — **the four daily actions (look, listen, feel, record) are never skipped**; (2) every quantitative item (clearance, weight loss, counts) **must carry a number**; (3) any over-line item gets an "out of service" board on the spot and is reported to the workshop head; (4) the form's footer records "items whose period was shortened this round, and why"; (5) the monthly inspection runs on the same day as the counting-house monthly stocktake, with the spares column checked on the same form.
4. **Empirical parameters and calibration**: scrap thresholds are in the 39.2.2 table, all marked "empirical, calibrate in the field"; calibration method: at the annual inspection take the distribution of measured values in this settlement, set each threshold between "the worst unit still passing" and "the earliest unit to fail," then copy each value into the ledger and update this card.
5. **Process observation and recording items**: daily entries are a number or "no abnormality," plus a signature; an over-line item records four columns — phenomenon, value, action, reporter; the weekly check records abrasive-debris weight; the monthly check records coupon weight loss.
6. **Pass / rework / scrap criteria**: pass = every item recorded within its period and every quantitative item carries a number; rework = a missed day (make it up that week, marked "make-up"; more than 2 misses in a month sends that unit's responsible person back to training); record scrap = two consecutive periods with no entries (the unit is treated as unmaintained and must be re-assessed before use).
7. **Common failures and troubleshooting order**: inspection done and the failure still happened → first check whether quantitative items were written as "normal" → then whether periods were extended verbally → then whether over-line items were boarded and handled → then whether the responsible person was a lone Level-1 stand-in with no second check.
8. **L1 / L2 / L3 evidence**: L1 = at least one unit with four consecutive weeks of inspection forms; L2 = one month of records for every registered unit plus one monthly quantitative ledger; L3 = a year of records + an annual accuracy re-verification report + at least one case where inspection caught degradation early (caught = taken out of service, stripped, and the defect confirmed).

**Inspection period-table template (copy per unit, one sheet each):**

| Unit no.: __  Responsible: __ | Daily | Weekly | Monthly | Annual |
|---|---|---|---|---|
| Oil level / grease quantity (number) | | | | |
| Abnormal noise (location) | | | | |
| Bearing temperature (wax-sheet result) | | | | |
| Clearance (mm, lead squeeze / feeler) | — | | | |
| Abrasive debris on magnet (dry weight, g) | — | | | |
| Oil-stain crack reveal (yes/no) | — | | | |
| Running hours / furnace cycles cumulative | | | | |
| Over-line item handling (four columns) | | | | |

## 39.3 The Spares System: Three Tiers and Minimum Levels

The spares system answers one question: **when something breaks in hand, how long is the downtime?** The answer comes from tiering plus minimum levels together. More spares is not better — stock ties up materials and hours and rusts on the shelf; nor is waiting for breakage to rebuild — per Chapter 19, one chisel from stock to tool runs the full carburize-quench-temper chain, one to several days. Tiering exists to spend money and hours on the parts whose downtime costs most.

### 39.3.1 Three Spares Tiers

| Tier | Definition | Examples | Minimum rule |
|---|---|---|---|
| A (critical single item) | single-point failure: one broken piece stops a line, no on-site substitute | blast tuyere tubes, bellows flaps and valve plates, waterwheel bearing shells, transitional master lead screw, crucibles, precast lining bricks | **≥2 per machine** (1 in use, 1 spare), extending Ch. 18's "2 tuyeres in stock" and Ch. 19's "≥2 critical blades" rules |
| B (common interchangeable) | shared across machines; one failure degrades but does not stop the line | bolts, pins, keys, wedge irons, bushings, wooden gears, bearing scraping blanks, belt joints | ≥2–3 per spec; interchangeable items pooled |
| C (consumables) | continuous consumption, managed by burn rate | files, whetstones, wax plates, grease, oil paper, charcoal (workshop ledger), hemp line, leather scraps | minimum = daily use × replenishment lead (days) × 1.5 safety factor |

Calibration of the minimum formula: lead time measured by the Chapter 38 ledger — from "reorder triggered" to "spare in store," log days per occurrence and take the upper quartile; the 1.5 safety factor is empirical, raised to 2.0 in lean or harvest-busy seasons (37.3.3 derating). **Stock below minimum triggers a rebuild order — never wait for exhaustion** (generalizing the Chapter 9 institution).

### 39.3.2 Minimum-Quantity Table (empirical, field-calibrate)

| Spare | Tier | Minimum | Calibration |
|---|---|---|---|
| Blast tuyere tubes (per furnace) | A | ≥2 | log burn-through rate per furnace (bore widening mm/smelt); stock 3 smelts' worth |
| Bellows flaps / valve plates (per box) | A | ≥2 sets | log flap hardening cycle (months) per shift |
| Waterwheel bearing shells (per wheel) | A | ≥1 pair + 1 wooden blank | annual measured clearance-growth rate |
| Crucibles (glass / copper) | A | ≥2 | checked against 39.4 melt-life and production plan |
| Furnace lining bricks and refractory mud (per furnace) | A | half a reline | log patch-mud consumption per furnace; reline size back-computed from measured lining erosion |
| Critical blades (chisels, saws, drills, each type) | A | ≥2 | Ch. 19 institution; corrected by regrind cycle and requench yield |
| Files (coarse/fine, each spec) | C | 2–4 | per 39.4 filing-hours life ÷ weekly filing hours |
| Wax plates | C | ≥10 | measured monthly use |
| Grease | C | ≥30 days' worth | summed monthly weigh-ins across lube points |
| Belt leather and joints | B | 1 belt's worth | belt life (39.4) + tension-adjustment margin |
| Whetstones (coarse/fine) | C | 1 each + blanks | monthly weigh-in wear |

### 39.3.3 Inspecting the Spares Themselves (a shelf is not a safe)

Spares rotting on the shelf is the stealthiest failure: the part is fetched for an swap and found rusted solid or moldy — the whole minimum-level institution has failed. Stock inspection is folded into the monthly check:

| Check | Method | Scrap / disposition |
|---|---|---|
| Metal corrosion | visual + touch per item; oiled items checked for intact film | surface rust removed and re-oiled; rust into the base metal judged per 39.1.2 |
| Leather mold/stiffness | visual mold spots; finger-flex for elasticity | brush off mold, re-grease; crack network on flex → downgrade to C |
| Wooden items (bearing blanks, gears) | cracks, insect bores, moisture (cool-damp feel = absorbed water) | dry in shade and re-weigh; warp >1 mm/100 mm → downgrade |
| Ceramic items (tuyeres, crucibles) | crisp ring on tap (◎ listen; compensation: soak and watch for bubble streams) | dull ring or visible crack = scrap — it would shatter in service |
| Grease rancidity | smell: acid; touch: sticky, separated | downgraded to non-bearing rust protection |
| Storage conditions | ≥200 mm off ground on sleepers, off walls, ventilated, rain-proof | violations corrected that month, entered in the monthly sheet |

[Card 39-03 Spares Ledger Card] (eight fields)

1. **Input materials**: equipment register, Chapter 38 ledger (consumption flow), 39.3.2 minimum table, monthly stock-inspection records.
2. **Required tools**: ledger book, scale, calipers; cross-checked per Chapters 3, 22 before use.
3. **Operating sequence and control points**: ① one row per spare: number, tier, minimum, on hand, location; **② every issue and receipt entered immediately — "use first, record later" forbidden**; ③ rows below minimum flagged red, triggering a rebuild work order copied to scheduling (Ch. 37); ④ monthly stocktake reconciles books and goods; gap >5% investigated that month (Ch. 37 warehouse rules); ⑤ stock-inspection results entered in the "stock status" column.
4. **Empirical parameters and calibration**: minimums and lead times per 39.3.1; validated quarterly against actual cutoff/overstock events — a cutoff = minimum too low; overstock >1 year = minimum too high or storage poor.
5. **Process observation and recording items**: issue date/use/issuer; receipt date/making batch (per 39.6 batch number); stock-status monthly column.
6. **Pass / rework / scrap criteria**: pass = books match goods, no below-minimum rows, all stock inspections passed; rework = below-minimum rows appeared (rebuild that week; halve the affected machines' inspection intervals meanwhile); scrap = books-goods gap >5% unresolved (all spares treated as unverified that month, individually re-inspected before issue).
7. **Common failures and troubleshooting order**: a spare found broken at swap time → was stock inspection actually run? → check oil-seal and sleeper conditions → check whether it was uninspected at intake; always one spare short → is the rebuild order entering production scheduling? → is the measured lead time underestimated?
8. **L1 / L2 / L3 evidence**: L1 = one filled ledger; L2 = one month books-match-goods + one cutoff/overstock back-check with correction; L3 = one quarter's ledger + minimums corrected by event back-check + zero missed stock inspections.

**Spares ledger template (copy from card):**

| Number | Name | Tier | Minimum | On hand | Location | Last issue | Rebuild order no. | Stock status (monthly) |
|---|---|---|---|---|---|---|---|---|
| | | | | | | | | |

## 39.4 Life Table: All Empirical Values, Field-Calibrate

This table is the book's master expected-life ledger for consumables, gathering scattered data and filling gaps. **Every row is an empirical value** — inferred from historical magnitudes, not settlement-measured; every row must be replaced in the "measured" column by settlement ledger data at annual inspection. General method: record each retired item as "install/start date + cumulative running hours (or firings, cycles) + scrap reason"; after one year, each row's settlement distribution is the measured life.

| Item | Empirical life | Unit | Pre-scrap signs (linking 39.1/39.2) | Main variables |
|---|---|---|---|---|
| Bloomery/small blast furnace lining (rammed refractory) | 3–8 campaigns | campaign (between major relines) | slag-line erosion >1/3 wall, cracks >5 mm | slag basicity, temperature, ramming quality (Ch. 18) |
| Furnace hot-patch mud | 1–3 smelts | smelt | patch falls away exposing red | patch mix and drying |
| Pottery/lime kiln body | 30–100 firings | firing | roof spalling, firebox arch spreading | heating/cooling rates (Ch. 12) |
| Crucibles (glass/copper) | 5–20 melts | melt | wall down to 2/3 original, glassy skin weeping | melt temperature, alkalinity (Ch. 14) |
| Blast tuyere tubes | 3–10 smelts | smelt | bore widening >1/3 | blast pressure, slag-line position |
| Scraping blades | 20–40 regrinds | count | blade shortened to hard-to-grip; hardened layer ground away | regrind overheating (Ch. 19) |
| Files | 40–100 filing hours | h | tip polish >1/3; won't cut wrought iron | filing hard stock, rust, no brush cleaning |
| Leather drive belts | 1–3 years | year | tension adjustment exhausted, still slipping; delamination | slip heating, damp (Ch. 15) |
| Hemp rope (static lashing) | 1–2 years | year | fuzzed and stiff; yarns breaking in strands | damp, UV |
| Hemp rope sling | 50–200 hoists | hoist | one broken strand = downgrade/no hoist; two = scrap | shock loading, sharp edges |
| Leather seals (bellows flap, piston ring) | 3–12 months | month | hardening; fit gap >1 mm | action frequency, grease (Ch. 12, 15) |
| Wood bearings (oiled hardwood) | 0.5–2 years | year | clearance >3 mm; journal wearing wood dust | water/dust environment, lubrication |
| Cast-iron/bronze bearing shells | 3–10 years | year | same but several times slower | completeness of the metallurgical chain |
| Springs (valve, bow-saw) | 10⁴–10⁶ cycles | cycle | oil reveals crack lines; free length short >10% | stress amplitude, rust onset (Ch. 19) |
| Drive chain | 1–5 years | year | elongation >2% pitch; dull running | lubrication, shock |
| Machine oil (grease) | change every 30–90 days | day | oil blackened and dry; magnet picks much iron dust | ambient dust |

**Wood vs. metal bearing trade-off** (a decision basis, not a quality verdict):

| Item | Wood bearing (oiled hardwood, Ch. 21) | Metal bearing (cast-iron/bronze shell, Ch. 17, 19) |
|---|---|---|
| Life | 0.5–2 years | 3–10 years |
| Replacement cost | half a day; wooden blank self-made | scraping fit 1–3 days + metallurgical chain |
| Failure mode | gradual loosening, visible wear dust — ample warning | also gradual but with high seizure risk (heat welding) |
| Fit | waterwheels, low-speed drives (<~1 m/s peripheral, empirical) | machine tools, steam engines; metal always where >60 ℃ line applies |
| Spares strategy | wooden blanks stocked (tier B); swap on failure | scraping blanks stocked; rescrape and reuse |

◎ Judging "wood or metal for this shaft" by touch (feel heat, listen) is insufficient — the criterion always returns to the 60 ℃ line and the speed ledger.

[Card 39-04 Spare-Part Life Card (Life-Table Calibration and Retirement Registration)] (eight fields)

1. **Input materials**: the original 39.4 life table (empirical column); the item-number file (commissioning date, cumulative usage); Card 39-03 spares ledger (issue and restock flow, rebuild lead time); scrap tickets (item number, reason, scrapping person, signed at Level 2 and above); the Card 39-02 stub for any item retired for an abnormal cause.
2. **Required tools**: ledger book (one row per item, the replacement table copied onto the flyleaf); scale and calipers (wear, wall thickness, elongation measurement), steel rule and scriber, a time base (sundial or water clock, Ch. 3, for accumulated running hours). Calibrate before use: zero and full-scale check on the scale, zero the calipers, cross-check per Chapters 3 and 22 — out-of-tolerance instruments are withdrawn.
3. **Operating sequence and control points**: ① on entry into the register fill item number, commissioning date, and unit of measure at once, **taking the unit row by row from the 39.4 table (furnace campaign / furnace / kiln firing / crucible melt / lift / cycle / year / day / h) — never mixing them**; ② at every retirement fill cumulative usage + scrap reason + scrapping person on the spot, scrap authority resting at Level 2 and above; ③ merge same-type items into one row and give the settlement's measured range (shortest value to median); **④ recompute the whole table on the annual inspection day, replacing the empirical column with measured values on every row that has them and noting the replacement year**; ⑤ items retired for abnormal causes — fatigue fracture, early corrosion — are flagged "abnormal" at the row end and force-routed to Card 39-02 for the five-step analysis and into the failure-sample library (39.6.3); ⑥ copy the measured rebuild lead time (upper quartile) into the minimum-formula field of Card 39-03 and recompute the minimum.
4. **Empirical parameters and calibration**: take every life range from the 39.4 table — furnace lining 3–8 campaigns, kiln body 30–100 firings, crucible 5–20 melts, tuyère clay pipe 3–10 furnaces, file 40–100 filing hours, sling 50–200 lifts, leather seal 3–12 months, wood bearing 0.5–2 years, metal bearing shell 3–10 years, spring 10⁴–10⁶ cycles, drive chain 1–5 years, machine oil changed every 30–90 days. General calibration: record three columns per item (commissioning date + cumulative usage + scrap reason); after one year each row's local distribution is the measured life. **A row with too few samples must not be replaced by a single item's value** — note the item count beside the measured column and keep the empirical range.
5. **Process observation and recording items**: item number, commissioning date, unit of measure and cumulative usage, scrap date and reason, scrapping person, whether the retirement was abnormal, whether it entered the sample library, number of retired items of that type with measured median, and the measured rebuild lead time in days.
6. **Pass / rework / scrap criteria**: pass = every retirement carries the three-column record, the measured column states item count and year, and the Card 39-03 minimum has been recomputed from the measured rebuild lead time; rework = commissioning date or cumulative usage missing (pull the item-number file within the deadline; if still missing, leave the empirical column and mark the row "file gap"); scrap = filling the measured column from impression or guesswork (the whole column is voided, the table reverts to empirical values, and the annual calibration is redone).
7. **Common failures and troubleshooting order**: spares always one short → first check whether the measured column still carries empirical values → then whether the rebuild lead time used unmeasured days → then whether the minimum was computed with the 1.5 safety factor (39.3.1) → only then add stock; same-type items dying early over and over → check whether abnormal retirements were missed for Card 39-02 → run the 39.2 three checks (oil, alignment, load) → check whether the 60 ℃ line was crossed; measured lives uniformly shorter than the empirical range → check for mixed units (firings vs. campaigns, lifts vs. years).
8. **L1 / L2 / L3 evidence**: L1 = one page of the life table with the three-column record complete for every retirement; L2 = at least 3 rows carrying the settlement's measured column (with item count and year) + one record of the minimum recomputed from measured rebuild lead time; L3 = a full year's table calibration + the trace of measured values replacing empirical ones + one dual-signed registration of a minimum changed on measured life (37.6.3) + the quarterly count showing every abnormal retirement transferred into the sample library.

**Blank life-table page (copy and use, one row per item):**

| Item | Item no. | Commissioned | Unit of measure | Cumulative usage | Scrapped | Scrap reason | Scrapping person | Abnormal (to Card 39-02) | Measured here (count / median) |
|---|---|---|---|---|---|---|---|---|---|
| | | | | | | | | | |

## 39.5 Scrap Criteria and Retirement: Scrap Is a Resource, Not Garbage

### 39.5.1 Scrap Authority and Tagging

Scrap authority sits with Level-2 workers and above, registered through Card 39-03 (item number, reason, scrapping person). A scrapped item is **handled on the spot, one of three ways**: tagged "downgraded," tagged "material," or tagged "sample" — untagged piles are forbidden and processed per the 39.6 failure mode. Any item retired for **abnormal causes** — fatigue fracture, early corrosion — is force-entered into the failure-sample library (39.6.3) for one five-step analysis; an abnormal retirement is itself a free information product.

### 39.5.2 The Downgrade Chain

A worn precision part is not waste; it is a crude-use part. Each link of the chain states its criterion and destination:

| Item | Level 1 (primary duty) | Down one | Down again | End point |
|---|---|---|---|---|
| Master lead screw | thread-cutting master | off-pitch ordinary drive screw | grinding mandrel / scraping-bar core | to furnace (steel sorting bin) |
| File | precision file | dull → coarse file, wood sawing | blank → scraper blank (good steel, Ch. 19) | to furnace |
| Scraper | scraping | rough chipping, rust removal | — | to furnace |
| Bearing shell (metal) | precision fit | rescraped for coarse equipment | — | to furnace |
| Crucible | glass melting | low-alkali melts / annealing cover | broken → refractory grog aggregate (Ch. 11) | furnace-founding filler |
| Lining bricks | — | broken grog backfilling | — | furnace-founding filler |
| Hemp rope | sling | lashing | mats, fire-lighting fuses | fuel (clean rope only; oiled rope burned separately, never in the cooking stove) |
| Leather | seal / drive | washers, handle wrap | polishing wheel | fat boiling (Ch. 15) |

Two downgrade disciplines: first, **downgraded items are hole-punched or notched** (e.g., a 3 mm hole in the tail = down one level) to prevent them flowing back to precision posts — a downgraded part mistakenly returned to the master machine is a leading precision accident; second, the downgrade destination is entered in the ledger, and the materials store sorts into four pools ("steel / iron / grog / wood" — an extension of the Ch. 19 grading store), with high-carbon steel items (old files, springs) entering the steel pool separately — they are precious carburizing stock at remelt.

### 39.5.3 Remelt and Recovery

Retired metal ultimately returns to the furnace: iron into the Ch. 18 re-smelting flow; steel (blades, springs, files) broken up as high-carbon stock for Ch. 19 carburizing and charging. **Remelted items must carry their source batch number** (39.6) — a batch repeatedly remelted accumulates impurities and elemental uncertainty; the Ch. 19 archive system requires no more than 2 remelts before a stock loses blade eligibility, becoming casting stock from the third. The rule runs without instruments: batch numbers and the ledger are the whole apparatus.

## 39.6 Quality Traceability: Batch Numbers, the Failure-Sample Library, and the Five-Step Failure Analysis

Before Chapter 37, knowledge lived in two heads: the old smith remembered the last ore batch differed; the bookkeeper remembered last month had more scrap. One death, one illness, one forgetting — and the knowledge is gone. Quality traceability has a single purpose: **make the information from every failure outlive the person.** The review review named the root disease: "storing only successful recipes, never failure conditions, material differences, or damaged samples." This section's batch system makes "differences traceable"; the sample library keeps "the physical evidence alive"; the five-step method makes "conclusions reusable."

### 39.6.1 Three-Level Batch Numbers: Furnace–Batch–Item

| Level | Definition | Numbering (example) | Use |
|---|---|---|---|

| Level | Definition | Numbering (example) | Use |
|---|---|---|---|
| Furnace no. | output of one smelt / one kiln firing / one crucible | date + same-day sequence: `L261029-02` = 2nd smelt of Oct 29 | locks raw-material batches (ore, charcoal, sand) and furnace-condition records |
| Batch no. | a post-processing batch under a furnace no. | suffix on furnace no.: `L261029-02-T3` = 3rd anneal batch of that furnace's output | locks process parameters (carburizing time, annealing curve, temper color) |
| Item no. | lifetime number of a critical single item | post code + sequence: `GD-014` = 14th blade from the forge post | locks the item's full history of regrinds, inspections, downgrades, scrap (linking the Ch. 19 tool archive) |

Execution rules:

1. **Travelling transfer**: batch numbers chalked/soapstone-marked on the item or tied as a wooden tag; the next process copies the number before starting. Three places must agree (on the item, on the travelling tag, in the ledger).
2. **Parallel recording of material differences**: every furnace number must record its ore batch and charcoal batch (source pit / kiln load) and the day's weather (rain-wet feed directly changes smelting behavior); Ch. 14 glass additionally logs the sand and soda batches. Raw-material batches themselves are numbered — ore by pit + pile, charcoal by kiln load.
3. **Traceability drill**: each quarter, one finished product is drawn and traced backwards from item number to ore and charcoal batches within half a stick of incense (about 1 hour). A broken trail = a broken traceability chain; the item is treated as unverified. This drill is the institution's acceptance test — traceability is proven by exercise, not by ledger thickness.

### 39.6.2 The Failure-Sample Library: Every Failed Part Is a Teaching Aid

Every scrapped and accident item whose failure was abnormal (early fracture, unusual corrosion, the first piece of a batch scrap, failed trials) enters the library, not the bin. Four zones: fracture (broken parts), corrosion, wear (out-of-tolerance items), scrap zone (batch scraps keep 3 samples: best, worst, middle). **Every item carries a four-field tag**:

| Field | Content |
|---|---|
| Symptom | broke / cracked / went soft / rusted through; when and where found |
| Parameters at the time | batch number, shift record summary (temperature band, medium, load), material batches |
| Autopsy conclusion | fracture reading (39.1.3), file and scratch tests (Ch. 19), weight and caliper measurements |
| Disposition | was the process card revised, to what version, by whom |

The library's enemy is becoming a junk pile: untagged items are counted quarterly; two consecutive quarters untagged = back to the furnace as material — **an untagged sample is not knowledge; it is clutter**. On intake, a one-line index is transcribed (item / date / batch / one-sentence conclusion) for teaching apprentices — the failure-sample library is the best physical teaching aid of the apprenticeship system (toward Ch. 43); one real fracture beats ten verbal descriptions.

### 39.6.3 The Five-Step Failure Analysis

**Step 1: Preserve the scene.** Do not move the item, do not wipe the fracture faces, do not mate the broken halves (mating crushes the fracture marks); sketch the scene first (position, orientation, scattered pieces); cover the fracture with a dry cloth against hand-sweat rust. When injury occurred, merge scene preservation with the Ch. 37 "24 h three tasks."

**Step 2: Gather all parameters.** Back-trace by batch number: material batches and differences (this batch's ore/charcoal/sand vs. the last), shift and handover records, recent inspection-sheet values, weather and season, the item's full history (item archive: regrinds, downgrades, remelts). Incomplete parameters are themselves part of the conclusion — note "inspection record missing" as a candidate cause.

**Step 3: Rank hypotheses by probability.** Common before rare; mark each as verifiable or not: ① human execution deviation (card not followed) ② material differences (checkable by batch comparison) ③ wrong process parameter (the card itself wrong) ④ equipment degradation (inspection chain) ⑤ environment (weather, season) ⑥ material defect (the batch's metallurgical history). Jumping straight to ⑥ to blame the material is the lazy answer when nothing else was checked.

**Step 4: Single-variable verification.** Change one variable at a time; lock everything else to the card; run controls (same material batch, same station, old vs. new parameters, 3 pieces each). This is Ch. 26's experimental discipline applied to maintenance. Verdicts rest on physical evidence — test bars, fracture faces, scratch sequences — never on "it looks fine now."

**Step 5: Archive the conclusion and revise the process card.** The conclusion is three lines: root cause, evidence, fix. The fix lands on the card as a revision — header version +1 (e.g., Card 19-03 v2 → v3); the old version is **not destroyed** but archived with the superseded reason (linking the Ch. 43 archive); register on the Card 39-02 stub and circulate card swaps to all holding stations. If the root cause is in the equipment rather than the process, revise the inspection sheet or spares minimum — with the same version trail.

[Card 39-02 Failure Analysis Card (Five-Step Flow Sheet)] (eight fields)

1. **Input materials**: the failed item (preserved), travelling batch tags, shift and inspection records, material batch ledger, item archive.
2. **Required tools**: magnifier (Ch. 24), steel rule and calipers (cross-checked), standard file and hardness reference set (Ch. 19), scale, kerosene and whiting powder, paper. Dry-brush fracture faces before examination; water washing forbidden.
3. **Operating sequence and control points**: ① sketch the scene and number scattered pieces; **② fracture read before touched: judge beach marks / coarse grain / fibrous and draw**; ③ back-trace batch numbers to ore and charcoal lots; missing links logged as "chain broken"; ④ hypothesis list ranked by probability, each marked verifiable / not-yet-verifiable; **⑤ single-variable verification requires controls — verification without a control group is void**; ⑥ three-line conclusion + card revision number registered + swap signed.
4. **Empirical parameters and calibration**: the hypothesis order (human → material → process → machine → environment → material defect) is an empirical sequence; calibration: each quarter tally the settlement's concluded root-cause distribution — if "material defect" exceeds 30%, re-check whether the first four hypotheses were敷衍'd.
5. **Process observation and recording items**: scene sketch, fracture drawing, parameters and 3-piece results per verification group, revision number and swap recipients.
6. **Pass / rework / scrap criteria**: pass = five steps complete, controls present, conclusion lands as a card revision; rework = steps skipped or no controls (redo step 4 and re-close); scrap = conclusion unarchived or old cards uncollected (analysis voided; case reopened).
7. **Common failures and troubleshooting order**: same failure recurring → did the last conclusion actually change the card? → did swapped cards reach the stations? → were controls run?; analysis stuck at "bad material" → check whether hypotheses 1–4 were individually excluded with a trace.
8. **L1 / L2 / L3 evidence**: L1 = one completed five-step sheet; L2 = one case closed with a controlled test and a card revision; L3 = a year's analysis binder + fully tagged sample library + a no-recurrence record (any recurrence triggers re-examination of the prior analysis).

**Failure analysis sheet template (copy from card):**

| Step | Record |
|---|---|
| ① Scene sketch and piece numbering | |
| ② Fracture reading (form / origin / drawing) | |
| ③ Batch back-trace (to ore/charcoal lots; where the chain broke) | |
| ④ Hypothesis ranking (1–6, verifiability) | |
| ⑤ Single-variable verification (parameters / 3 controlled results) | |
| ⑥ Three-line conclusion + card revision no. + swap signatures | |

## 39.7 Change Control: Dual Signatures, First-Article Inspection, and Rollback

This section lands Ch. 37's 37.6.3 change control in maintenance and quality contexts. **Any change to a process parameter, inspection interval, scrap threshold, or spares minimum is a change**, subject to the same rules:

1. **Dual signature**: changing a parameter = the process-card holder (Level 3) + the works supervisor, both required; five items entered in the ledger (date, old value, new value, reason, verification result), linking to Ch. 37.
2. **First-article inspection after any change**: the first **3 pieces are 100% inspected** (not sampled) — against the corresponding chapter's acceptance criteria item by item (test bar, fracture, scratch sequence, full dimensions); all 3 must pass before normal production resumes; one first-article piece is retained in the sample library's scrap or control zone.
3. **Rollback conditions (any one restores the old parameter, with a registered rollback)**: a first-article failure; one same-type failure within 30 days of the change; abnormal life shortening after the change (inspection finds precursors early — e.g., clearance growth at twice the historical rate); new scrap appearing in adjacent processes.
4. **Rollback also requires dual signatures**, and rollback is not case closure — the root cause returns to Card 39-02 for a fresh five-step analysis. Anyone holds the right to request a rollback (Ch. 37); suppressing such a request is itself an accountability violation.

Change control is accepted by drill too: each quarter, draw any parameter's current value from the ledger — its "why is it this value" registration chain (original card + every change's five items + verification result) must be findable within one hour. Not findable = change control lost; the whole line is treated as unverified process.

## Parameter Master Table

| Parameter | Empirical value | Calibration | Section |
|---|---|---|---|
| Sliding-bearing clearance ceiling | 0.05–0.1 mm (new pair) → 0.3 mm triggers rescrape | lead-wire/feeler sequence per machine | 39.2.2 |
| Bearing temperature red line | ≈60 ℃ (3 s on the back of the hand / wax plate soft but not melting) | wax-plate method (Ch. 20) | 39.2.2 |
| Corrosion section-loss scrap | >10% of loaded section | load tests on same-batch pieces of differing rust depth | 39.1.2 |
| Corrosion-coupon alarm | monthly mass loss >0.05 g/dm² → halve the interval | four-point coupons weighed monthly | 39.1.2 |
| Fatigue shaft runout | >0.2 mm → stop and inspect for cracks | dial indicator on the rotating shaft (Ch. 27) | 39.1.3 |
| Tier-A spares minimum | ≥2 per machine | quarterly cutoff/overstock back-check | 39.3.1 |
| Tier-C spares minimum | daily use × lead × 1.5 (2.0 in lean seasons) | lead time from ledger, upper quartile | 39.3.1 |
| Furnace lining life | 3–8 campaigns | erosion depth and cracks logged per smelt | 39.4 |
| Crucible life | 5–20 melts | wall thickness calipered per crucible | 39.4 |
| Scraper regrind life | 20–40 times | per-grind archive | 39.4 |
| File life | 40–100 filing hours | ledger hours accumulated | 39.4 |
| Leather seal life | 3–12 months | monthly flex-elasticity check | 39.4 |
| Wood/metal bearing life | 0.5–2 yr / 3–10 yr | measured clearance growth | 39.4 |
| Sling scrap | one broken strand = downgrade; two = scrap | visual per hoist + hoist ledger | 39.4 |
| Change first-article inspection | 3 pieces, 100% | corresponding chapter criteria | 39.7 |
| Rollback window | 30 days after change | same-type failure and life precursor monitoring | 39.7 |
| Traceability drill time limit | one item's batch chain traced within ~1 hour | quarterly spot check | 39.6.1 |

## Failure Modes and Diagnosis

Ordered by "most common, hardest to detect." Most of this table's diseases lie not in the equipment but in institutional execution — that is this chapter's thesis: equipment degradation is physics; institution-as-decorations is self-inflicted.

| Symptom | Candidate causes | Verification | Disposition | Prevention |
|---|---|---|---|---|
| Inspection sheets full of ticks, yet sudden failures | inspection as decoration: quantitative fields written "normal," or the sheet back-filled | ask the inspector "last Wednesday's clearance reading for this machine" — no answer = decoration; compare handwriting and ink dates | machine reverts to unverified status; re-inspect and restart; handler retrained | Card 39-01 rule 6 bans the word "normal"; monthly spot re-checks one item |
| Spares cabinet opened at swap: spare rusted solid / moldy | stock inspections not run; storage without sleepers; uninspected intake | check 39.3.3 monthly column gaps; check oil films | full-cabinet re-inspection; failed items sorted per 39.5; storage corrected | stock inspection folded into the monthly stocktake; violations per Card 39-03 scrap clause |
| Spares ledger has entries without goods, goods without entries | issues not recorded ("use first, record later"); private borrowing | trace every monthly gap >5% row | resolved within the month; unresolved spares all re-inspected as unverified | issue-time recording is Card 39-03 control point ② |
| Same-type failure recurring within 3 months | last analysis was shallow: wrong root cause (blamed material), revised cards never reached stations, no controlled verification | pull the last Card 39-02: five-step completeness, swap signatures, control records | reopen the analysis, excluding hypotheses 1–4 with traces; old conclusion marked "overturned by recurrence" and archived | closure must land as card revision + signed swaps; recurrence triggers re-examination |
| Fractured parts tossed; sample library untagged | "broken is broken" mindset; no tagging institution | on-site check: do scrapped items carry one of the three tags? | untagged items to furnace as material; tagging retraining | scrap three-way (downgrade/material/sample) forced through Card 39-03 |
| Precision drops suddenly; scrap spikes | downgraded parts flowed back to precision posts (unmarked); or inspection intervals verbally extended | check downgrade punch/notch marks; check sheet tails for extended intervals | recall mis-installed parts; rescrape; extension handled as unauthorized change | downgrade punch/notch institution (39.5.2); interval changes via dual signature |
| Traceability drill cannot complete the batch chain | travelling tag lost and not replaced; raw batches themselves unnumbered | find the break point link by link from the item number | outputs from the broken link treated as unverified | three-place number agreement (item, tag, ledger); ore/charcoal batch numbering upstream |
| Bearing repeatedly over 60 ℃ even after swap | swapping without root cause: blocked oil groove, misalignment, load change (Ch. 20 three-check) | run the three-check; check belt tension and foundation settlement | clear groove; realign; check the building (39.2.2 building row) | daily temperature column + monthly alignment re-check |
| Store grease rancid; bearings wearing early | expired grease still entering sliding pairs | smell + sticky separation (39.3.3) | rancid grease demoted to rust protection; all early-wear bearings inspected | tier-C grease rotated on the 30–90 day cycle |

## Process Card Index

| Card no. | Name | Purpose | Copy to |
|---|---|---|---|
| 39-01 | Equipment inspection card (with interval templates) | four-tier inspection execution and records | beside each machine / workshops |
| 39-02 | Failure analysis card (five-step flow sheet) | failure closure, card revisions, recurrence re-checks | works supervisor / teaching hall |
| 39-03 | Spares ledger card | three-tier minimums, monthly stocktake and stock inspection | spares store / bookkeeping office |
| 39-04 | Spare-part life card (life-table calibration and retirement register) | life-table measured-column calibration, retirement records, spares-minimum re-check | spares store / bookkeeping office |

## Acceptance Criteria L1/L2/L3

| Level | Criterion | Test conditions | Evidence retained |
|---|---|---|---|
| L1 | One binder each for the three institutions: 4 weeks of inspection sheets for one machine, one spares ledger, one completed five-step analysis sheet | pre-start verification items may have gaps, marked "provisional intervals" | original sheets, ledger, analysis sheet |
| L2 | All registered machines inspected ≥1 month with no "normal" in quantitative fields; spares monthly gap ≤5%; one failure analysis closed with a controlled test and a card revision swap; life table has ≥3 rows of settlement-measured values | inspections and stocktake same basis; 3 pieces per control | quantitative monthly ledger, stocktake records, closed analysis sheet, old and new cards |
| L3 | Three institutions running >1 season: ≥1 degradation intercepted early by inspection (confirmed by teardown); traceability drill completed; no same-type recurrence (or recurrence re-examined and closed on record); sample library fully tagged and quarterly-counted; change register contains ≥1 first-article inspection and ≥1 rollback | reproduced through staff and season changes; annual first full life-table calibration | a season's ledgers, teardown records of interceptions, drill records, library count book, change chain, annual calibration report |

## Labor Hours and Consumption

| Item | Crew and duration (empirical) | Notes |
|---|---|---|
| Daily inspection | ≤10 min per machine, by the operator | folded into shift start; no extra staffing |
| Weekly inspection | half-day per workshop, by the master or a Level-2 worker | includes swarf weighing and blade-archive check |
| Monthly inspection | 1 day, Level-2 worker + bookkeeper | same day as the stocktake to save one stop |
| Annual inspection | 3–5 days downtime per workshop, led by Level 3 | lining relines counted separately (Ch. 12, 18) |
| Total maintenance quota | 5–15% of workshop hours (empirical, calibrate) | below 5% = overdrawing equipment life; hours "saved" are repaid as accidents |
| One failure analysis | 1–3 days, 2–3 people | scene preservation + back-trace + 3-piece controlled trials |
| Sample-library count | half a day per quarter, 1 person | apprentice teaching additional |
| Consumables | grease every 30–90 days; wax plates, oil paper, kerosene per tier-C minimums | all into the Ch. 38 ledger's maintenance line |

## Safety Boundaries

Most actions here occur stopped and cold, but the following are part of the procedure — failing to execute them equals failing the chapter:

1. **De-energize stored-energy parts first**: unload or lock springs, tensioned belts, and slings before disassembly; fatigue-fracture fragments flying out and spring ejection are this chapter's two direct injury sources.
2. **Entering furnaces for inspection**: furnace ≤60 ℃ (wax-plate verified) and ventilated ≥15 min before entry, two-person rule (Ch. 37); CO is odorless — entering by feel is a violation.
3. **Roof and height checks in pairs**, roped or railed; wet roofs after rain are off-limits.
4. **Scrapped slings cut up on the spot** to prevent回流 misuse; scrapped items punched/notched before leaving hand.
5. **Chronic-exposure recording**: inspections also log exposure hours for dust (swarf, charcoal), noise (forging, riveting), and acid mist (Ch. 26 shops), filed monthly — this is the raw data of occupational health, handed to Part 9 (toward Ch. 49) for filing. Maintenance workers themselves are a high-exposure group; this line may not be skipped.

## A/B/C Lists

**A list (executable with this chapter):**

| Item | Criterion |
|---|---|
| Four-tier inspection sheets | Card 39-01 running at stations, quantitative fields holding numbers |
| Spares tiering and minimums | Card 39-03 three tiers complete; below-minimum rows triggering rebuild orders |
| Stock inspection | 39.3.3 table run monthly, folded into the stocktake |
| Failure-sample library and tagging | four-field tags complete; untagged items quarterly-counted |
| Five-step failure analysis | Card 39-02 closures always land as card revisions |
| Change control | dual signature, 3-piece first-article inspection, three rollback conditions on record |

**B list (requires prior chapters):**

| Item | Prerequisite |
|---|---|
| Life-table calibration | running ledgers of Ch. 18, 19, 20, 12, 14, 15, 21 equipment |
| Scrap and downgrade chains | Ch. 19 grading store and fracture reading, Ch. 11 grog recipe, Ch. 17 casting |
| Quantitative inspection | Ch. 20 scraping and error tables, Ch. 22 measures, Ch. 27 dial indicator |
| Rosters and skill linkage | Ch. 37 rosters, skill matrix, change control |
| Books-goods and consumption entry | Ch. 38 material and energy ledgers |

**C list (external dependencies and irreducibles):**

| Item | Note |
|---|---|
| Non-destructive testing | ultrasonic/magnetic/radiographic: no route (before Ch. 33); internal cracks managed indirectly by surface indication + hours logs + fracture reading |
| Precise fatigue-life computation | no S-N testing capability; log and watch precursors only — no prediction |
| Continuous lubricant supply | depends on the small-scale oil chains of Ch. 8, 15, 26; a cutoff halves every sliding pair's life |
| ≥1 year of weather-exposure records | the foundation of corrosion-rate calibration; without it, anti-corrosion intervals are provisional numbers |

## Next Dependencies

- **Ch. 40 Redundancy and disaster resilience**: the off-site double store for spares and bypass designs for critical equipment — this chapter manages "the spare is ready"; Ch. 40 manages "what if the store burned."
- **Ch. 43 Archives and transmission**: long-term preservation of card versions, ledger transcriptions, and the sample-library index — every binder this chapter produces must outlive a generation in the Ch. 43 archive.
- **Ch. 49 Occupational health**: the monthly dust/noise/acid-mist exposure records accumulated in this chapter's inspections are the raw data source for occupational monitoring; maintenance workers' protection procedures unfold there.
- **Ch. 38 ledgers (linked)**: maintenance lines (grease, spares, consumables) merge into the material and energy ledgers — "the maintenance cost behind every ton of product" becomes computable.
- **Whole-book backstop**: the words "sustainable production" in every process chapter's L3 acceptance, Chapters 1–42, gain a testable meaning from this chapter's three institutions — **without inspection, spares, and traceability, L3 is institutionally idle; with them, "runs for the long term" becomes, for the first time, a criterion that can be checked off.**
