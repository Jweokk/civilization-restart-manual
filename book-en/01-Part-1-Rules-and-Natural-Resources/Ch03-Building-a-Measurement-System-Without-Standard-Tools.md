# Chapter 3 Building a Measurement System Without Standard Tools

## Chapter Objectives

- Establish physical carriers and reproduction methods for four classes of temporary standards: **length (the standard rod), mass (the equal-arm balance + weight-stone set), time (solar shadow, beats, and the water clock), temperature (the phase-change anchor card)**.
- Establish three geometric standards (straight line, right angle, circle) and one physical standard (level), all directly constructible from natural objects.
- Establish **body-unit error statistics** (using data to prove why cross-person handover is forbidden) and the **true-north determination by construction method**.
- Establish the error-recording method (repeat measurement, range, two-person cross-measurement) and the unit management system (primary standard + secondary standards + monthly check).
- This chapter is cited repeatedly throughout the book: from Chapter 6's combustion timing to the process control before Chapter 35, the capability that runs through everything is reliable measurement and repetition (lineage IV). **The only legitimate sources of precision in this book are this chapter and Chapter 20.**

## Capability Boundaries

**Can do:** length halved down to the "finger" level, balance equilibration at 1–2% of load, time anchored to the day + water-clock segments, temperature with four anchors + feel grades; true-north orientation to half-finger-width-level deviation (multi-day re-measurement).

**Explicitly cannot do:** interpolation between temperature anchors (awaits the glass thermometer, Chapter 25); short-duration high-precision timing (the water clock is nonlinear; the constant-head method is only a mitigation); uniform ten-way division of scribed lines (awaits a hard scribe point, Chapter 19); tracing units back to old-world standards (no impact; external settlements convert by mutual comparison).

**This chapter starts from zero**: every procedure is bare-handed + picked-up natural objects, with no prerequisite tools.

## Pre-Work Verification

| # | Verification item | Criterion | Source |
|---|---|---|---|
| 1 | Boundary rules | Picked-up objects may be used directly; this does not constitute time travel | Chapter 1 |
| 2 | Materials | 3 straight-grained dry wooden rods, rattan / long grass stems (untwisted), clay, a set of stones, a palm-sized flat stone | Chapter 2 survey |
| 3 | Recording medium | Clay-tablet temporary-storage system in place | Chapter 2 |
| 4 | Manpower | Cross-measurement needs ≥2 people (error statistics recommend ≥6) | — |

---

### 3.1 Length, Weight, Time, and Temperature

**Why these four classes**: length constrains every dimension; mass constrains every ratio; time constrains every process cycle; temperature constrains every thermal process. The pre-industrial overall strategy: **compress "absolute measurement" to a minimum and solve most problems with "comparative measurement"** — comparison needs no true value, only stability.

**Master table of natural anchors for the four classes of standards**:

| Class | Absolute anchor (naturally existing) | Comparative means (established in this chapter) |
|---|---|---|
| Length | No stable natural absolute anchor (solar shadow length varies with the season) | Standard rod + secondary rods; body units (single-person self-use only) |
| Mass | None | Equal-arm balance: comparison and equilibration only; it never reads "how much" |
| Time | Day, sunrise, noon (astronomical anchors, highly reliable) | Beats; water clock (segmented calibration) |
| Temperature | Ice water 0; body temperature about 36–37; beeswax about 63±2 (if available); boiling water about 100 (at sea level) | Feel grades + phase-change anchor card |

**Using the temperature anchor card, and its honest boundaries**:
- Four feel grades: icy (≈0–5), cool, neither cold nor hot (about 32–35 — the neutral point where skin "feels no difference" lies below body temperature; empirical value), warm (tolerable for long contact), hot (withdrawn at one touch);
- The boiling point varies with altitude and solutes: roughly 1 ℃ lower per about 300 m of elevation; salt water boils higher (approximately +0.5–1). Take "the locally measured boiling point" as your anchor;
- Fire-color temperature estimation is auxiliary only: error on the order of ±100 ℃, **must not be treated as quantitative detection**; its formal placement is in Chapter 12.

**Key insight for the mass standard**: the equal-arm balance gives only "equal / not equal"; only with a weight-stone set does it become counting. Proportioning by ratio is nothing but repeated equilibration, which suffices to support all proportioning from Chapter 8 onward.

#### 3.1.1 Error Statistics of Body Units (Setting the Rule with Data)

The problem with body units (elbow, hand-span, finger, pace) is that **they differ from person to person**. Do not trust "roughly about the same" — measure on the spot:

**Measurement protocol (once, half a day, ≥6 people)**:
1. Each person measures in turn: index-finger width (widest point of the proximal phalanx face), hand-span (thumb tip to little-finger tip at full stretch), elbow (elbow tip to middle-finger tip), pace (mean of 10 natural paces), arm span (tip to tip of the two middle fingers with the arms raised horizontal);
2. Each item is measured 3 times per person and the median taken; all readings go into the error record sheet;
3. Compute for each item the **in-team range** (max minus min) and the **range/median** percentage.

**Empirical intervals (prefilled values, to be overwritten by the team's own measurements)**:

| Item | Typical median | In-team range (empirical) | Relative difference |
|---|---|---|---|
| Finger width | 17–20 mm | 5–7 mm | ≈30% |
| Hand-span | 180–220 mm | 40–60 mm | ≈25% |
| Elbow | 420–490 mm | 60–80 mm | ≈15% |
| Pace length (natural) | 650–780 mm | 100–150 mm | ≈18% |
| Arm span | ≈ one's own height | Varies with height | ≈15% |

**Conclusion written into the unit charter**: a relative difference of 15–30% means — Jia's "five hand-spans" may be Yi's "four hand-spans". **Body units are permitted for single-person self-use only (you make it, you check it yourself); cross-person handover and entry into archives are forbidden**. For cross-person handover, the smallest permitted unit starts from the "standard rod". The personal pace calibration card (3.7) solves the reliability problem of "using your own pace for your own work".

[Card 03-05 Body-Unit Error Statistics] (eight fields)

1. **Input materials**: ≥6 subjects from the same team; a standard rod (as the conversion reference); a clay scribing field or tablets.
2. **Tools required**: standard rod, marking tool, error record sheet (the 3.4 template). Calibration source: body units record only the differences among people and are never converted outward; every outward conversion is made against the standard rod.
3. **Sequence and control points**: each person measures in turn finger width (widest point of the proximal phalanx face), hand-span (thumb tip to little-finger tip at full stretch), elbow (elbow tip to middle-finger tip), pace (mean of 10 natural paces), arm span (tip to tip of the two middle fingers) → 3 measurements per item, median taken → all readings onto the sheet → compute the in-team range and the range ÷ median percentage → write the conclusion into the unit charter. Control points: one protocol per item (landmarks fixed in the sheet header); re-zero between the 3 runs.
4. **Empirical parameters and calibration**: ≥6 people, half a day; prefilled empirical intervals — finger width median 17–20 mm, in-team range 5–7 mm (≈30%); hand-span 180–220 mm, 40–60 mm (≈25%); elbow 420–490 mm, 60–80 mm (≈15%); pace 650–780 mm, 100–150 mm (≈18%); arm span ≈ one's own height (≈15%). All empirical values, to be overwritten by the team's own measurements.
5. **Observations to record**: person / item / the 3 readings / median / in-team range / range ÷ median percentage / measurement conditions (wet-dry, cold-hot).
6. **Pass / rework / scrap criteria**: pass = all five items present, 3 readings each, ranges and percentages complete; rework = an item short of 3 readings or measured at inconsistent landmarks — retest; scrap = fewer than 6 subjects (too thin to set a rule; the conclusion is reference only and may not enter the charter).
7. **Common failures and diagnosis order**: (1) one item's range is abnormally large → first check the landmarks (finger width at the widest point of the proximal phalanx face is the easiest to place differently), then whether anyone spread or curled deliberately; (2) the hand-span / arm-span ratio is clearly off → check whether the hand-span was taken at full stretch; (3) pace dispersion is large → first check for a deliberate pace, then the ground state; (4) the conclusion will not go into the charter → too few subjects or missing items; retest (the commonest cause of rework).
8. **L1 / L2 / L3 evidence**: L1 = one five-item statistics table for ≥6 people; L2 = the conclusion written into the unit charter and used to forbid cross-person handover; L3 = a second team repeats the method and lands in the same relative-difference order (15–30%).

### 3.2 How to Make the First Straight Lines, Right Angles, and Circles

**Straight lines (three kinds, each with a reliable source)**:
1. **Plumb line**: a stone hammer tied to rattan and hung freely; a gravity-defined line, the most reliable (doubles as the vertical standard);
2. **Stretched cord**: taut untwisted rattan / grass stem approximates a straight line — the error is sag from the cord's own weight; beyond a span of about 20 paces the mid-span sag becomes perceptible and intermediate support is required;
3. **Three-rod mutual-check straightedges**: fit three dry wooden rods against each other pairwise, grind away the high spots and repeat, until all three rods fit pairwise without gaps. Two rods can only detect bending; three are needed to average the curvature out (the straight-line prototype of Chapter 20's "three-plate mutual lapping"). Hand-shaved rod straightness reaches only "no gap visible against the light"; quantified testing awaits Chapter 20.

**Right angle (the 3-4-5 cord method)**:
1. Take rattan about 14 elbows long; using any stick as a temporary unit, measure off 12 equal segments, one hard knot per segment (12 knots, 13 points);
2. With small stakes form a triangle of sides 3, 4, 5 knot-spacings, all three sides taut;
3. The angle between the 3 side and the 4 side is the right angle;
4. Error control: knot spacings all measured with the same stick (the systematic error cancels automatically); readings uniformly referenced to knot centers; work on a leveled clay platform;
5. Self-check: flip it over and fit it back in place; a uniform gap means it is true.

**Circle**: staked-circle method — the stake is the axis, the rattan the radius, a hardwood-tipped scribe; one full turn scribes the circle. Roundness check: measure the radius of the same circle in 8 directions; a range ≤1 finger width passes as a rough circle. To copy a circle, compare against a radius-scribed rod.

#### 3.2.1 True-North Determination by Construction (Equal-Shadow Method, Multi-Day Re-Measurement Orientation)

Orientation is the common prerequisite of layout (Chapter 13 kiln foundations, house orientation) and of the calendar (farming times, Chapter 10). **Do not rely on a magnetic needle** (magnetic declination is unknown and varies widely by region; the compass must wait for calibration until after Chapter 30's magnetism) — use the sun:

**Construction steps (completed in one day, verified by re-measurement the next day)**:
1. Level a clay surface of about 2×2 m (leveled with the A-frame); stand a rod at the center (about 1.5 m tall), **trued plumb** (plumb line against the rod in two directions);
2. In the morning (about 2–3 h after sunrise) drive small stake A at the rod-shadow tip, and immediately, as a graduated compass, scribe an arc with the "rod-base-to-A distance" as radius and the rod base as center;
3. All day long, at intervals of about one section (command beats), drive a recording stake at each shadow tip — the shadow-tip track is an arc swinging outward through the morning, shortest at noon, swinging back in the afternoon;
4. In the afternoon, when the shadow length **again equals** the arc radius (the shadow tip has returned onto the arc), drive stake B;
5. **The line joining A and B is the east-west line**; construct the perpendicular bisector of AB (the rattan fold-in-half midpoint method, the bisection technique of 3.5) through the rod base — **this line is the north-south line**; in the northern hemisphere, the side where the shadow tip lies is north (the noon shadow points north);
6. Fixing the line: scribe a groove along the north-south line and bury stakes at both ends.

**Verification and precision**: re-measure every 1–2 days; the angle difference between the two lines should be ≤ half a finger width (eyeball estimate, ◎; compensation: measure the distance difference between the end stakes of the two lines). Multi-day averaging can lower the error further. **Principle of equal-shadow symmetry**: the sun is symmetric about noon between morning and afternoon, so two shadows of equal length are necessarily symmetric about the north-south line — this is given by geometry and does not depend on any tool precision.

[Card 03-02 True-North Determination by Construction] (eight fields)

1. **Input materials**: one straight-grained dry wooden rod (about 1.5 m tall); small stakes; rattan for scribing the arc; a scribe; a level clay surface about 2×2 m.
2. **Tools required**: plumb line (to true the rod), A-frame level (to level the clay surface), scribing tool. Calibration source: the plumb line relies on gravity and needs no calibration; the arc radius is the "rod-base-to-A distance", taken with the same length of rattan that scribes the arc.
3. **Sequence and control points**: level the clay surface → stand the rod and true it plumb (plumb line against the rod in two directions) → in the morning drive stake A at the shadow tip and scribe an arc about the rod base → all day, every one section or so, record the shadow-tip stake → in the afternoon, when the shadow length **again equals** the arc radius, drive stake B → the A–B line is the east-west line → fold the rattan in half to take the midpoint, construct the perpendicular bisector of AB through the rod base: that is the north-south line → scribe a groove along it and bury stakes at both ends. Control points: **the rod must be plumb**; **B may be driven only when the equal shadow finally arrives**.
4. **Empirical parameters and calibration**: clay surface 2×2 m; rod about 1.5 m; drive A about 2–3 h after sunrise; recording interval about one section (command beats); re-measure every 1–2 days — a two-day inter-line angle difference ≤ half a finger width passes (eyeball, ◎; compensation: measure the distance difference between the end stakes); multi-day averaging lowers the error further.
5. **Observations to record**: day name / section count at staking / morning and afternoon shadow-tip stake positions / inter-line angle difference (eyeballed in half-finger units) / weather (overcast days are not used).
6. **Pass / rework / scrap criteria**: pass = re-measurement inter-line angle difference ≤ half a finger width; rework = over limit — re-measure and average over several days; scrap = the site is obstructed or the clay surface collapses — move to a new site and start over (the old scribed line may not be reused).
7. **Common failures and diagnosis order**: (1) large angle between two runs → first check whether the rod is plumb, then whether the arc radius was misread (it must be the original radius of the arc-scribing rattan), last whether the afternoon really waited for the equal shadow (staking B early is the commonest error); (2) scattered shadow-tip stakes → the recording interval is too coarse; tighten it to "about one section"; (3) no usable shadow on an overcast day → stop and redo another day; (4) the scribed line will not line up with the shortest noon shadow → north and south are swapped (in the northern hemisphere the shadow-tip side is north).
8. **L1 / L2 / L3 evidence**: L1 = one scribed true-north line plus a next-day re-measurement record; L2 = two consecutive months of shadow-position re-measurement; L3 = a second person constructs the line from this card alone, within half a finger width.

### 3.2.2 Bootstrapping the Angle Standard (the Sole Source of Every "Angle Plate" in This Book)

Later chapters cite the "angle plate" in many places (chisel edge angles 40°–50°, mesh-texture angle 45°, turning-tool angles, etc.) — it does not appear out of thin air in Chapter 5; it is generated by this section's three bootstrap lines:

1. **45°**: fold the right angle made by the 3-4-5 cord (the diagonal is 45°) — construction: with the right-angle vertex as center, scribe an arc of arbitrary radius crossing both legs at A and B; then with A and B as centers and the same radius, scribe arcs intersecting at C; the line vertex–C is the 45° bisector;
2. **30°/60°**: trisect the 45° (approximate construction: probe the two division points against the arc intersections; close within ≤2° and accept — honestly labeled "approximate 30/60"); the interior angles of an equilateral triangle (three cords of equal length closed up) are exactly 60°, which is the harder source;
3. **Making the angle plate**: carve the above standard angles on the edge of a hardwood board / bone plate, fitted with "snap-plate" fit testing (fit the angle under test against the plate angle and hold up to the light; an uneven gap is an error).

**Honest boundary**: this section can guarantee only the three hard standards 90/45/60 plus the ±2–3° approximate grade; arbitrary angles (e.g., 73°) cannot be done at this stage — any process requiring an arbitrary angle is rewritten as a combination of the three grades or as "functional-test acceptance".

### 3.3 How to Use a Water Surface to Establish a Level Standard

Principle: a still water surface is a level surface. Four methods (progressing by range):
1. **Basin-water scribe-line method** (local): let water in a container stand still, scribe a line on the vessel wall at the water surface;
2. **A-frame level** (portable): tie two equal-length wooden rods into an A shape, connect the midpoints of the two legs with a crossbar, hang a stone-hammer line from the apex, scribe a mark at the crossbar midpoint — when the hammer line passes the midpoint, the frame face is level. **Key self-calibration — the reversal method**: read the offset in the normal orientation, turn the whole frame around 180° and read again; the midpoint of the two offsets is the true midpoint (it eliminates the systematic error of unequal legs and may not be omitted);
3. **Plumb line**: the vertical standard; mutually 90° with the horizontal;
4. **Segmented level transfer** (long distance): basin-water scribe lines set the heights + the A-frame and range poles transfer level segment by segment; error accumulates per segment (about half a finger per segment; calibration: transfer back and forth between the same two points and compare the closing error). Precise leveling awaits Chapter 25.

**Application preview**: workbench leveling (Chapter 9), kiln-foundation layout (Chapter 12), channel gradient (Chapter 13 — when a deliberate slight slope is intended, express it with proportional rules of the "raise one finger per pace" type).

**Failure modes**: wind acting on the hammer line (windbreak); rattan stretching when damp (calibrate the dry and wet states separately); tie cords loosening (run the reversal self-check before every use).

[Card 03-03 A-Frame Reversal Self-Calibration] (eight fields)

1. **Input materials**: two equal-length wooden legs; one crossbar; one stone hammer; rattan (for lashing and for the hammer line).
2. **Tools required**: plumb line (stone hammer on rattan, hanging free), marking tool. Calibration source: **no external standard** — self-calibration rests only on the 180° reversal, not on the legs being equal.
3. **Sequence and control points**: lash the two legs into an A → connect the midpoints of the two legs with the crossbar → hang the stone-hammer line from the apex → scribe a mark at the crossbar midpoint → read the offset in the normal orientation → turn the whole frame 180° and read again → take the midpoint of the two offsets as the true midpoint. Control points: the reversal must turn the whole frame (legs not swapped); **the reversal step may not be omitted**.
4. **Empirical parameters and calibration**: reversal angle 180°; criterion = the hammer line passing the true midpoint, meaning the frame face is level; residual error is of the "about half a finger per segment" order (accumulating per segment in segmented level transfer; empirical value — must be calibrated to local conditions); calibrate the dry and wet states separately (rattan stretches when damp).
5. **Observations to record**: frame number / normal-orientation offset (in finger widths) / offset after reversal / true-midpoint correction / pre-use self-check date / weather (wind).
6. **Pass / rework / scrap criteria**: pass = the true midpoint is fixed after reversal and the hammer line passes it; rework = both offsets equal and in the same direction (the ground or the support is at fault — re-shim and recalibrate); scrap = a leg is cracked or the lashing will not tighten — replace the stock.
7. **Common failures and diagnosis order**: (1) the hammer line swings without settling → add a windbreak first (wind is the first cause), then check whether the stone hammer is too light; (2) the offset is identical before and after reversal → not unequal legs but an uneven support or ground; shim level and recalibrate; (3) accuracy drifts away after some use → the tie cords have loosened; run the reversal self-check before every use; (4) overall deviation grows in the rainy season → rattan stretched when damp; calibrate the dry and wet states separately.
8. **L1 / L2 / L3 evidence**: L1 = one reversal self-calibration record; L2 = two consecutive months of re-checks; L3 = a second person calibrates the same frame from this card alone, and the two true midpoints agree by scribed-line overlap.

### 3.4 How to Repeat Measurements and Record Errors

**Iron Law II made concrete: every measurement must answer "how large is the error", and the lowest-cost answer is repetition.**

**Repeat-measurement protocol**:
1. Measure every quantity at least 3 times, re-zeroing and re-reading each time, without memorizing the previous result;
2. Record all readings and compute the range R = max − min;
3. Report the median as the value, R as the dispersion flag, with the uncertainty roughly estimated as ≈R/2;
4. Two-person cross-measurement: for the same nominal value, 2 people each measure independently 3 times; if the difference between the two reported values is greater than either person's R, judge a systematic error — switch person, tool, and method in turn to localize the source.

**Error record sheet template**:

| Column | Content | Example |
|---|---|---|
| Date / recorder | Day name + person name | Day 31 / Yi |
| Object | Number + name | Standard rod 1 vs secondary rod 2 |
| Nominal value | Expected value | Should be equal length |
| Readings | Each measured value | 3 comparisons: equal / shorter by one finger / equal |
| Range R | Max − min | One finger |
| Tools used | Tool numbers | Rod 1, rod 2 |
| Conditions | Weather / wet-dry / temperature anchor | Dry season, overcast, cool grade |
| Disposition | Conclusion + follow-up | R over limit, re-measure next month |

**Naive discrimination between systematic and random error**: if the value stabilizes after repeated averaging, random error dominates (measuring more helps); if averaging leaves an overall offset (someone's pacing always runs long), it is a systematic error — change the standard or add a correction; more measuring is useless.

**Drift detection of the standard rod (monthly check)**: at each full moon compare the primary rod with the two secondary rods pairwise; if any pair differs by more than 1 smallest graduation, replace and remake. Wood's wet swelling and dry shrinking is the main drift source — the dryness criterion = rod weight unchanged across two consecutive monthly checks (weighing on the balance to judge moisture stability; a closed loop).

### 3.5 How to Establish Unified Units of Measure

**Principles**:
1. The absolute magnitude of a unit is unrelated to the old world, and that is fine — what matters is **stability, shareability, rebuildability**;
2. Body units are permitted for single-person self-use only (per the 3.1.1 measured data); **cross-person handover is forbidden**.

**Length unit charter**:
- Primary unit = the full length of the standard rod (the "rod"), made of shade-dried hardwood, cross-marks at both ends, the rod body numbered;
- Sub-units by halving: half-rod, quarter-rod ... down to the "finger". **No decimal graduations** — hand-scribed marks cannot achieve uniform tenths; halving can be achieved exactly by the fold-in-half method;
- 2 secondary standards, the three rods stored in three places (against simultaneous loss); monthly check per 3.4; if the three rods mutually exceed tolerance, remake the third rod by majority rule.

**Mass unit charter**:
- Unit weight = the calibrated stone: equilibrate the two pans repeatedly to select one of handy size and number it;
- Multiple copies via a binary equilibration chain: obtain a 1/2, 1, 2, 4, 8 weight set; any integer mass can be composed;
- Weight stones are notch-marked and registered into the archive.

**Time unit charter and water-clock calibration method**:

Public anchors: sunrise, noon (the shortest-shadow moment on the north-south line), sunset. Two short-duration levels:
1. **Beats**: agree a fixed command or chant as "one section"; each person long-term records "heartbeats per section" and takes the average; the beat is governed by the command, heartbeats serve only as a cross-check;
2. **Water clock**: a bamboo segment or gourd holds water; a small hole is pierced in the bottom with a natural sharp point. **Defect declared honestly: the drip rate slows as the water level falls, so timing is not linear.** Two responses:

[Card 03-01 Drip-Rate Segmented Calibration] (eight fields)

1. **Input materials**: one bamboo-segment or gourd water vessel (inner wall blackened with soot so the water level is visible); a natural sharp point to pierce the bottom hole; a scribe needle; clay tablet and charcoal for records.
2. **Tools required**: scribe needle (to score the inner-wall graduations), command beats as the time ruler, marking tool. Calibration source: graduation spacing comes from the fold-in-half bisection, not from a rule; the only time ruler is the command beat — no outside clock is borrowed.
3. **Sequence and control points**: pierce the bottom hole → score equal divisions on the inner wall (4–8 divisions by fold-in-half bisection) → calibrate division by division (while the level falls from line i to line i+1, count command sections, repeat 3 times and record the range) → make the "division-to-time table" and hang it beside the pot. Control points: **each division is calibrated on its own; never infer the rest from one division**; a new pot means recalibrating the whole table.
4. **Empirical parameters and calibration**: 4–8 divisions; 3 repeats per division; range criterion ≤1/10 of that division's total section count; winter drip rate slows by 5–10% (empirical value — must be calibrated to local conditions), recalibrate on season change; two-pot cross-comparison difference <10% (L2 criterion).
5. **Observations to record**: per division — pot number / division number / the 3 section counts / range / water-temperature grade (Chapter 3 anchors) / recalibration date.
6. **Pass / rework / scrap criteria**: pass = the 3 runs of every division fall within ≤1/10 of that division's total section count; rework = one division's range is over limit — recalibrate that division only; scrap = the pot body cracks and leaks — replace the pot and recalibrate the whole table (**a new pot means a new table; the old table may not be carried over**).
7. **Common failures and diagnosis order**: (1) readings always run slow → first check whether another division's table is in use, then whether the season changed without recalibration (winter slowing 5–10%); (2) the drip runs as a continuous thread → hole too large, fit a finer hole and recalibrate the whole table; (3) no drops form → first check whether the hole is blocked (clear it with a bamboo sliver), then whether the level is too low; (4) two runs of the same division far apart → the command beat is unsteady; have one person call the beat.
8. **L1 / L2 / L3 evidence**: L1 = one division-to-time table; L2 = a two-pot cross-comparison difference <10%; L3 = the season-change recalibration system running, with recalibration records on file.

**Constant-head water clock (upgrade technique; switch as soon as materials allow)**: the root of the uneven drip rate is: water level changes → pressure changes. Cure: **twin-pot constant head** — the upper pot is continuously topped up and overflows from a side port, holding the dripping pot's liquid surface constant at the overflow-port height → constant pressure at the drip hole → constant drip rate. The upper pot can be a pierced pottery jar (after Chapter 11). The constant-head pot needs only one calibration of "drips per beat", and all divisions take the same time.

**Unit charter clay tablet**: all unit definitions are written only on the "unit charter" tablet; changing a unit = issue a new charter tablet, deprecate the old one and archive it. On contact with external settlements, exchange standard-rod copies and record mutual comparisons.

#### 3.5.1 Process Card for Making the Equal-Arm Balance (3-06, the Root of the Proportioning Line)

The balance on which all later proportioning (from Chapter 8 on) depends is given its manufacturing method here, no longer just "pick a stone":

[Card 03-06 Equal-Arm Balance] (eight fields)

1. **Input materials**: one straight hardwood beam (70–90 cm, knot-free, straight-grained); cord in three grades; two shell / hardwood hanging pans; a set of calibration stones (chosen by repeated balancing of the two pans, each numbered); a scribing needle and charcoal; a clay tablet (for the record and the notch numbers).
2. **Required tools**: scribing needle (zero line and end lines); chisel (shallow V notch); hard-bone / hardwood seat block (carrying the V); crossbar (to hang the beam); pillar (three lines scribed); fine needle (pointer); the smallest-unit calibration stone. Calibration sources: equal arms are measured with **one and the same cord wrapped round the beam** and **cross-checked by the reversal method** (same method as Card 03-03); weights are copied level by level as a **binary balancing chain** (1/2, 1, 2, 4, 8) — no external weights are borrowed.
3. **Operating sequence and control points**: ① scribe the zero line at the exact middle; at both ends wrap the same cord to measure equal distances and scribe the end lines → ② **reversal cross-check**: place the same stone at each end and swap them — if it does not balance, the ends differ in weight or in arm length; repair until the tilt direction is unchanged after swapping → ③ chisel a shallow V notch in the top midline, seat it on a hard-bone / hardwood block, hang the beam from the crossbar → ④ hang a fine needle from the bottom midline; scribe three lines on the pillar (left / middle / right, one finger width apart) → ⑤ sensitivity test: after balancing empty, add the smallest-unit stone — **a pointer deflection ≥ half a line width passes** → ⑥ weight multiplication 1→2 (duplicate by placing two stones side by side) →4→8, copying level by level with the balance, each piece notch-numbered and archived. Control points: **the V notch is where the whole balance's precision resides — ground smooth, never chipped**; if sensitivity falls short, only lighten the beam or shorten the hang distance — never add stones to fake a reading; **the pans and hanger cords must never lift loads or people** (structural strength unverified).
4. **Empirical parameters and calibration methods**: beam 70–90 cm, straight-grained, knot-free; end lines measured with one and the same cord (no rule); V notch shallow and ground smooth, seated on hard bone / hardwood; the three pillar lines one finger width apart (Chapter 3 body unit, single-person use only); sensitivity criterion = the smallest-unit stone deflects the pointer ≥ half a line width; weight chain binary 1/2, 1, 2, 4, 8, calibrated by level-by-level balancing duplication with each piece notch-numbered and archived.
5. **In-process observation records**: beam number / beam length and weight / zero-line and end-line scribes / tilt direction in the two reversal cross-checks / V-notch condition (grooved, chipped) / sensitivity measurement (stone added, pointer deflection) / notch numbers and balancing result at each level of the weight chain / handler.
6. **Pass / rework / scrap criteria**: pass = tilt direction unchanged after reversal + empty balance + smallest-unit stone deflects the pointer ≥ half a line width + weight chain 1→8 balanced level by level on file; rework = sensitivity short (lighten the beam or shorten the hang distance, then re-measure), unequal end lines (re-scribe and cross-check again); scrap = cracked beam, chipped V notch, or a beam warped by moisture (replace the beam; the old weight chain must be re-balanced).
7. **Common failures and troubleshooting order**: ① the same object weighs differently twice → first check whether the V notch has worn a groove (new seat, re-grind) → then check hanger-cord lengths and the two pans' weights (equal-length cords, swap the pans) → finally check whether the beam has taken up moisture (weigh it to judge dryness, remake); ② pointer does not move, or moves sluggishly → first check whether the fulcrum is binding → then whether the beam is too heavy or the hang distance too long → finally whether the "smallest-unit" stone is itself a reject; ③ pans at unequal height → first adjust the beam midpoint, then fit equal-length hanger cords.
8. **L1 / L2 / L3 evidence**: L1 = one usable balance + weight chain 1→8 notch-numbered on file; L2 = two consecutive monthly balancing re-tests (same object weighed twice, difference within the range, recorded and explained) + the weight chain reviewed by a second person; L3 = a second person builds one blind from this card and it is verified usable (Chapter 3 acceptance L3) + a damaged standard rebuilt within two days per the charter, old-to-new deviation ≤ one finger width.

## 3.6 How to Preserve Technical Drawings and Process Records

**Recording media list**:

| Medium | Advantages | Drawbacks and countermeasures |
|---|---|---|
| Shade-dried clay tablet | Scribeable, high volume, locally sourced | Destroyed by water: store elevated off the ground, cover boards, transcribe a second copy at another site before the rainy season; fired hardening awaits Chapter 11 |
| Carved wood | Water-resistant | Small capacity, short entries only |
| Knotted cords | Portable | Reminder index only, cannot store parameters |
| Ground scribing field | Large drawings possible | Weathers; important drawings must be transcribed to clay tablets |

**Drawing standards**:
1. Scales in integer multiples only: 1:1, 2:1, 1:2. Arbitrary scales are forbidden — there is currently no fine-division capability, and arbitrary scales cannot be re-verified;
2. Dimensions marked with scribe symbols: one rod = primary-unit symbol, one finger = sub-unit symbol; quantities counted with scribed dots (five dots and one bar);
3. Three kinds of drawing: outline, assembly relationships, full-size layout field (1:1 ground layout).

**Archive system**: one tablet, one matter; numbering = date + serial; build the catalog tablet before establishing files; key drawings and recipes kept in two copies at different sites; symbols follow the Chapter 2 key table, and new symbols are updated in both copies simultaneously. **Failure mode**: damp tablets, lost symbols, the gamble of "keeping it in the head" — results at L2 level and above must be put in writing.

### 3.7 From Personal Experience to Reproducible Craft

**Turning "I can do it" into "it works from the record": four means**:
1. **Retelling test**: the artisan dictates the complete procedure → another person executes blind, following only the dictation → differences backfilled item by item. Until the dictation is proven by blind execution, it is deemed "an incomplete procedure";
2. **Parameter-window method**: for each parameter record three values — minimum usable / usual / maximum usable. A failure outside the window is not a surprise; it is a known boundary;
3. **Process card format** (one card per tablet): procedure steps + parameter window + failure modes + acceptance criteria + version number;
4. **Journeyman criterion**: an apprentice may work independently only after N consecutive acceptable pieces (generally N=3; critical materials and safety parts N=5, empirical value).

**Version management**: every improvement issues a new version of the process card; the old card is archived marked "superseded by version X", searchable in both directions. **Verbal changes to processes are forbidden** — any practice change that has not entered a new card version is logged as an operational error.

[Card 03-04 Pace Calibration] (eight fields)

1. **Input materials**: one standard rod (the primary "rod" unit, shade-dried hardwood); small stakes (to mark the ends of the measured distance); clay tablet or marking board.
2. **Tools required**: standard rod, marking tool, error record sheet (the 3.4 template). Calibration source: every pace count is converted into "rods", never into millimetres — this chapter has no millimetre-level absolute standard.
3. **Sequence and control points**: pick level, dry, firm ground → measure off a known distance with the rod (say 10 rods, stakes at both ends) → the person walks it at a natural pace and counts paces → walk it out and back once each → repeat 3 times and take the median → compute "paces per rod" and score it onto the personal pace calibration card. Control points: **a natural pace only** (no deliberate overstriding); restart the walk each time without carrying the previous count.
4. **Empirical parameters and calibration**: the natural pace is read as the mean of 10 paces; each item is measured 3 times per person and the median taken; typical median pace length 650–780 mm with an in-team range of 100–150 mm (empirical value — must be calibrated to local conditions); pass criterion = pacing dispersion 1–2%; a round-trip difference >2 paces per 10 rods means change the venue (slope, grass height, soft mud all alter pace).
5. **Observations to record**: person / venue / measured distance in rods / outbound paces / return paces / median of 3 / paces per rod / weather and ground state.
6. **Pass / rework / scrap criteria**: pass = round-trip difference ≤2 paces per 10 rods and the 3 runs inside the 1–2% dispersion; rework = over limit — recalibrate on level, dry, firm ground; scrap = the same person's results from two venues are systematically inconsistent (that pace may be used only at that venue, never generally).
7. **Common failures and diagnosis order**: (1) the round-trip difference grows with every calibration → check the venue first (slope, grass height, soft mud) and change it; (2) two counts of the same walk disagree → a deliberate pace was used; switch to a natural pace and restart; (3) the pace is markedly shorter than at the last calibration → fatigue or load; record the current state separately without overwriting the historical value; (4) the converted distance will not match the rod measurement → first check whether someone else's pace table is in use (body units may not be handed across persons).
8. **L1 / L2 / L3 evidence**: L1 = one personal pace calibration card (paces per rod); L2 = one calibration record per venue at two venues, each stating where it applies; L3 = pacing a distance with the card and landing within the 1–2% dispersion of the standard-rod measurement.

---

### 3.8 Calendar and Farming Times (C3 supplement)

**Solar-term determination**: measure the rod shadow length at noon every day and enter it in a table — the longest-shadow day = winter solstice, the shortest-shadow day = summer solstice (judgment error ±2 days; take the mean over three consecutive years); between the two equinoxes and two solstices, use linear interpolation of shadow length to divide out the eight sections. **Season marking by star rise/set**: choose the last bright star in the eastern sky before dawn (heliacal rising) and the first bright star in the western sky after dusk (heliacal setting), and record the star names day by day — the same star rising and setting at the same time year after year is a natural yearly calendar. **Leap-year correction**: fix the year by the winter solstice — if the "year length" (the interval between two winter solstices) consecutively exceeds 365 days by more than one beat, insert an intercalary month to realign (folk rule: 12 lunar months fall short of the year by about 11 days; three years one leap as a starting point). **Farming-time alignment**: sowing window = solar term + local correction (phenological anchors: record when a certain tree flowers / a certain insect first chirps, and revise year by year against yields — corrections transcribed into the ledger; doing it from memory is forbidden).

## Master Parameter Table

| Parameter | Value | Class |
|---|---|---|
| Body-unit in-team relative difference | Finger width ≈30%, hand-span ≈25%, elbow/pace ≈15–18% | Measured-protocol prefilled |
| Balance equilibration discrimination limit | 1–2% of load (calibrated by the small-stone increment method) | Empirical |
| Minimum reliable hand-scribed line spacing | 2–3 mm (mean of 10 successive divisions) | Empirical |
| Pacing dispersion | 1–2% (change the venue if the round-trip difference is >2 paces per 10 rods) | Empirical |
| Rough roundness check | 8-direction radius range ≤1 finger width | Criterion |
| True-north re-measurement | Two-day inter-line angle difference ≤ half a finger width | Criterion |
| Water-clock division range | ≤1/10 of that division's total section count | Criterion |
| Winter drip-rate change | Slows by 5–10%, recalibrate on season change | Empirical |
| Cord sag | Span >20 paces requires mid support | Empirical |

## Failure Modes and Diagnostics

| Symptom | Candidate causes (by probability) | Verification | Disposition |
|---|---|---|---|
| Dimensions mismatch on two-person handover | A body unit was used across persons | Check the "tools" column of the record sheet | Switch to the standard rod across the board; re-measure |
| Standard-rod monthly check mutual difference over limit | Rod not fully dry / absorbed moisture | Weigh and compare against the monthly-check records | Replace and remake the rod; add moisture protection to the storage |
| Right-angle layout skewed | Uneven knot spacing / uneven ground / wet rattan stretched | Flip self-check | Measure with the same stick; level the platform; re-test in the dry state |
| Large angle between the two true-north lines | Rod not plumb / arc radius misread / afternoon did not wait for the equal shadow | Re-check plumb; re-measure | Re-measure and average over multiple days |
| Water-clock readings always slow | Wrong division table used / winter viscosity / hole worn larger | Cross-check against the table; recalibrate on season change | Follow the table; recalibrate |
| Balance pans unequal height | Beam midpoint offset / hanger cords of unequal length | Hang the empty beam and fine-tune | Adjust the midpoint; equal-length hanger cords |
| Cross-measurement difference greater than either party's range | Systematic error (someone's technique / a rod's defect) | Switch person and tool, bisect to localize | Add a correction or change the standard |

## Process Card Index

[Card 03-01] Drip-rate segmented calibration (card in 3.5, before the constant-head drip section) | [Card 03-02] True-north determination by construction (card at the end of 3.2.1) | [Card 03-03] A-frame reversal self-calibration (card at the end of 3.3) | [Card 03-04] Pace calibration (card at the end of 3.7) | [Card 03-05] Body-unit error statistics (card at the end of 3.1.1) | [Card 03-06] Equal-arm balance (card in 3.5.1)

All six cards copy out onto a single page with the eight fields complete: input materials / required tools (including calibration sources) / operating sequence and control points / empirical parameters and calibration methods / in-process observation records / pass–rework–scrap criteria / common failures and troubleshooting order / L1–L3 evidence.

## Acceptance Criteria

- **L1**: one physical anchor built for each of the four classes of standards, each with 1 recorded measurement; the true-north line scribed with a next-day re-measurement record; the body-unit error statistics table completed.
- **L2**: two consecutive monthly checks (three-rod mutual comparison, equilibration re-test, shadow-position re-measurement); ≥10 entries in the error record sheet with no column missing; the two-person cross-measurement difference recorded and explained; the water-clock division-to-time table verified by a two-pot cross-comparison; the charter and catalog tablet in the archive.
- **L3**: any damaged standard rebuilt within two days per the charter, with an old-to-new deviation ≤1 finger width; at least 1 process card verified usable by a second person's blind execution; the double-backup archive running, with one transcription drill completed before the rainy season. Evidence: monthly-check sheets, transcription records, blind-execution records.

## Labor Hours, Manpower, and Consumption

| Item | Manpower | Hours (empirical) |
|---|---|---|
| Body-unit error statistics | ≥6 people | Half a day |
| Standard rod, three rods + mutual check | 1–2 people | 1 day (material selection and shade drying counted separately) |
| True-north determination + re-measurement | 2 people | 2 half-days |
| Water clock making and full-table calibration | 1 person | Half a day per pot |
| Balance and weight chain | 1 person | 1 day |
| Monthly check | 1 person | Half a day per month |

## Safety Boundaries

- The balance hanging pans and hanger cords must never hoist heavy loads or people — structural strength unverified;
- Guard against scalds from boiling water and molten wax (beeswax at 63 ℃ can already cause injury): never touch hot objects bare-handed, insulate hot containers with multiple layers of dry leaves; the full heat-safety procedure is in Chapter 6;
- Solar shadow observation reads the shadow tip; **looking directly at the sun is forbidden**;
- The hanging stone hammer must never be suspended overhead; while working with a scribing point, the other hand must never be placed along the extension of the scribe line.

## A. Existing Tool Inventory

Chapter 1 starting-point determination checklist, dependency-tracing four-question card, dependency graph template; Chapter 2 resource survey record sheet, resource map, symbol key table, streak plate, hardness reference set, ten-step identification procedure card, natural container set.

## B. New Tools Introduced in This Chapter

Standard rod (primary length unit) + secondary rods ×2; 12-division cord and the 3-4-5 right-angle cord method; plumb line; A-frame level (with reversal self-calibration); equal-arm balance and weight-stone set (1/2–8 binary chain); solar-shadow pole + shadow-tip scribing field + **true-north scribed line**; temperature anchor card; **body-unit error statistics table**; **water clock (segmented calibration) and the constant-head water clock upgrade**; error record sheet template; unit charter clay tablet + catalog tablet + archive system.

## C. Unresolved Dependencies

Interpolation between temperature anchors (Chapter 25 glass thermometer); short-duration high-precision timing (mitigated by the constant-head method; precision clocks long-term); uniform fine-division scribing (Chapter 19 hard scribe point); knife-edge balance (after Chapter 20); magnetic-compass orientation calibration (after Chapter 30 — until then, always use the equal-shadow method).

## Next Dependencies

Standard rod, right-angle cord, A-frame level, **true-north line** → Chapter 9 workbench, Chapter 12 kiln foundations, Chapter 13 building layout and orientation; balance and weights → Chapter 8 recipes, Chapter 11 proportioning, Chapter 23 stoichiometry; temperature anchors → the thermal processes of Chapters 6/11/12; water clock and beats → Chapter 6 combustion timing, Chapter 11 firing cycles; error records and the archive system → every L2 acceptance in the book; the ledger and archive systems of Chapters 37–43 upgrade this chapter's clay-tablet system as their prototype.
