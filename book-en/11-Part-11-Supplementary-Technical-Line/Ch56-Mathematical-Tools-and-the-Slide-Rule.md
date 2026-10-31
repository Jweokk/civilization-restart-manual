# Chapter 56: Mathematical Tools and the Slide Rule

## Chapter Goals

- Gather the geometric operations scattered across the chapters (3-4-5 layout, true north, circle division) into a **construction-methods set**: perpendiculars, parallels, angle bisection, regular polygons (3/4/5/6/8 sides), proportional scaling up and down, and circle division — each with construction steps, a verification method, and error registration.
- Compile a **local logarithm table**: built by a square-root anchor chain plus equal-ratio cumulative multiplication, with an honest ±1% class commitment; three standard worked examples (multiply, divide, square root) and usage procedures.
- Manufacture a **slide rule**: a C/D/A three-scale system with cursor vernier, and a reading graduation criterion (error <2% on 10 problems).
- Establish **calendar and farming-season calculation**: a shadow solar-term table (solstice determination ±2 days), star rising/setting cross-validation, a leap-day re-synchronization system, and a farming-season/grain-storage alignment table.
- Compile a **practical trigonometric table**: the sine table by dual routes (geometric square-root chain + large-circle chord measurement for mutual checking), slope-to-rise conversion, and chord-based angle measurement.

## Capability Boundaries

**Can do**: the full construction-methods set (three perpendicular methods / two parallel methods / angle bisection / regular polygons / grid scaling / circle division, each method with verification and closure-error registration); a common logarithm table 1.000–10.000 (master table 128 rows + main table 90×10 cells, whole table ±1% class); a slide rule (rule length 250 mm class, readings ±2%); solstice determination ±2 days and a measured year length of 365–366 days; a sine table 0–90° with one row per 7.5° (±0.01 absolute-error class).

**Explicitly cannot do**:
- Field angle measurement above the ±5° class (the ±1° class requires a turned graduated dial — an extension of the Chapter 22 route; not promised in this chapter);
- Four reliable digits in the logarithm table (hand-method table building caps at two reliable digits (±1%), third digit for interpolation reference only; the fourth digit is spurious precision — Section 25.11 discipline);
- Trisecting an arbitrary angle (a classically impossible construction; the procedures expressly forbid attempting it — always route around);
- A precision astronomical calendar (lunar-phase calendar, eclipse prediction — solar terms and farming seasons suffice; this item is not done);
- Densifying the sine table to 1° (ten times the work of the 7.5° table; a separate project on demand).

**External dependencies**: standard rods and bisection-scribed lines (Chapter 3); hardened scribers (Chapter 19); surface plates and angle blocks (Chapters 20, 22); thin glass (Chapter 24); magnifiers (Chapter 24); paper and clay-tablet dual carriers (Chapter 3 Section 3.6, Chapter 41).

## Pre-Start Verification

| # | Verification item | Criterion | Source |
|---|---|---|---|
| 1 | Length standard | Numbered standard rods on hand, monthly-check records on file (three-rod mutual difference ≤1 smallest division) | Chapter 3 Section 3.4 |
| 2 | Compass and dividers | Legs closed show no gap against the light; two arcs drawn at the same opening coincide | Chapter 3 |
| 3 | Scriber | The hardened scriber lines copper plate cleanly without breaking the line | Chapter 19 |
| 4 | Construction board surface | The straightedge laid on the surface in three positions shows no light gap at any of them | Chapter 20 mutual-check concept |
| 5 | Right-angle standard | The 3-4-5 rope and the right-angle square flip-checked against each other show even gaps | Chapter 3 Section 3.2 |
| 6 | Angle blocks (reinforcement item, may be absent) | Full-circle closure error evenly distributed and registered | Chapter 22 Section 22.5 |
| 7 | Manual multiplication | The operator can complete two-digit × two-digit vertical multiplication (each operand two reliable digits (±1%), third digit for interpolation reference only) (reachable with the Section 56.2 half-day training) | This chapter |
| 8 | Recording media | Clay-tablet/paper dual-copy system in place, numbering rules in use | Chapter 3 Section 3.6 |
| 9 | Manpower | Table-building cross-checks need ≥2 people | — |

## Common Materials and Tools for This Chapter

**Materials table (five items)**:

| Material | Identification standard | Minimum specification | Acceptable substitute (cost) | Substandard signs | Amount per unit |
|---|---|---|---|---|---|
| Construction board | Stone slabs or hardwood planks joined into a surface; straightedge fits in two positions with no gap | 1×1 m class flatness | Tamped dry-mud yard (wind-eroded, rain-ruined; shadow yard only) | Warping, see-through gaps | 1 surface per method |
| Bamboo/hardwood rule blanks | Straight grain, knot-free, dense growth rings | Shade-dried one season, weighed across two weeks with unchanged weight (dryness test) | Wrought iron strip (hard to re-engrave but durable) | Bowing, damp core in cross-section | 2–3 blanks for master + working rules |
| Thin-glass sliding window | Flat glass; see objects through it without wavering | One piece 20×30 mm | Bone/horn sheet in a slit frame (narrow reading window, slower speed) | Bubble in the center of the window | 1 piece per rule |
| Beeswax and soot ink | Wax-soak against moisture; ink rubbed into the scribed lines does not bleed | One wax-soak pass forms a film | Tung oil (dries twice as slowly) | Sticky and powdery after application | 20–30 g wax per rule |
| Clay-tablet/paper tables | Numbered-archive system | One master table + one off-site copy | Fired ceramic slab (heavy but damp-proof) | Ruined by water and not stored raised | About 10 tablets/pages for master + main tables |

**Tools table (three items)**:

| Tool | Source chapter | Precision requirement | Calibration before use |
|---|---|---|---|
| Standard rod | Chapter 3 | Primary unit, monthly checks on record | Three-rod mutual comparison |
| Compass/dividers | Chapter 3 | Closes with no gap; opening repeatable | Two trial circles on steel plate coincide |
| Hardened scriber | Chapter 19 | Scribes copper plate without breaking the line | Trial-scribe 10 lines, check continuity against the light |
| Right-angle square | Chapters 3/20 | Flip check shows an even gap | Flip against the surface plate and check |
| Straightedge (certified straight edge) | Chapter 20 | Two-position mutual fit with no gap | Two-position check against the surface plate under light |
| Magnifier | Chapter 24 | 2.5–5× | Scale lines show sharp edges |
| Angle block set | Chapter 22 | Closure error evenly distributed, on file | 90° block cross-checked against the right-angle square |

### 56.1 The Geometric Construction-Methods Set

**Three general rules**: ①every method has four complete columns — given conditions, construction steps, verification method, error registration; ②the accuracy ceiling of construction is set by line width: scriber + line reading is 0.5–1 mm, which on a 1 m format is the ±0.1% order — all construction methods share this ceiling, and no promised precision may cross it; ③the error-registration system: for each method's first execution and for quarterly spot checks, register the verification readings in the Section 3.4 error-record format; out of tolerance, that board and that tool are immediately decommissioned.

#### 56.1.1 Perpendiculars (three methods)

**Method 1 (the 3-4-5 rope method, for outdoor layout)**: already in Chapter 3; one added registration item — flipping it back against its original position with an even gap counts as pass; the crossing-angle verification reading goes into the error table.

**Method 2 (the perpendicular-bisector method, for the board)**: given segment AB — ①with center A and radius R (0.7–1.2×AB, empirical window) draw two arcs above and below; ②with center B and the same R draw arcs meeting the first pair at C and D; ③join CD, crossing AB at M — then CD⊥AB and M is the midpoint. **Verification**: measure the four distances AC, BC, AD, BD — all must equal R; and MC=MD. **Error point**: when the two arcs are nearly tangent, the intersections smear — redraw outside the R window; fudging an intersection reading is not allowed.

**Method 3 (the tangent method, for long perpendiculars)**: given line L and an external point P — ①with center P draw an arc cutting L at E and F; ②with centers E and F and equal radius (>EF/2) draw arcs meeting at Q; ③PQ⊥L. **Verification**: the midpoint of EF must fall on PQ (Method 2 cross-check; the two methods verify each other — double insurance).

#### 56.1.2 Parallels (two methods)

**Method 1 (the equidistant double-perpendicular method)**: pick any two points on the known line L, erect a perpendicular at each (Method 3), measure distance d along both perpendiculars to get two points; the line joining them is the parallel. **Verification**: pick another point on the new line and measure its perpendicular distance to L — it must =d; the three points' mutual difference ≤1 line-width passes.

**Method 2 (the double-perpendicular method, a parallel through a point)**: through external point P erect the perpendicular to L, with foot H (Method 3); then through P erect the perpendicular to PH (Method 2 reduced to the "pick two points on a line" case) — the result is the parallel through P. **Verification** as in Method 1. The meaning of the double perpendicular: it reduces "parallel" to two applications of "perpendicular", and perpendicularity is a primitive already verified in this chapter.

#### 56.1.3 Angle Bisection

Steps: given ∠BAC — ①with center A and radius R draw an arc cutting both sides at D and E; ②with centers D and E and equal radius r (0.5–1.0×R, empirical window) draw arcs meeting at F; ③AF is the bisector. **Control point**: AD=AE must be laid out in one and the same compass opening for the two leg positions (two separate openings = systematic error). **Verification**: AF crosses DE at G; then GD=GE and DG⊥AF (perpendicular-bisector mutual check). **Error registration**: the bisector deviates from the midpoint of the line joining the two equidistant points by ≤1 line-width.

#### 56.1.4 Regular Polygons (3/4/5/6/8 sides)

General method: first construct the circumscribed circle, then step around it with fixed chord lengths — the same idea as the Chapter 22 angle blocks: **closure error distributed evenly over the full circle**.

| Sides | Construction | Verification |
|---|---|---|
| 3 | Step around the circle with the compass opened to the radius, connecting alternate points (chord=√3×R, taking two radii with 120° between them) | Mutual difference of the three sides ≤1 line-width |
| 4 | Construct a diameter; construct its perpendicular bisector (56.1.1 Method 2) to get the other diameter; connect the four points | The two diagonals are equal and bisect each other at right angles |
| 6 | Step the radius opening around the circle six times | Six chords walked around return to the start; closure gap ≤2 line-widths |
| 8 | On the 4-side basis, bisect each 90° central angle (56.1.3) to get four points in the 45° directions | Mutual difference of the eight sides ≤1 line-width; closure gap ≤2 line-widths |
| 5 | Method A (approximate construction): draw the circle and two perpendicular diameters; take K as the midpoint of radius OM; with center K and radius KN (N the endpoint of the other diameter) draw an arc cutting the adjacent diameter at P; NP is the side length — a classical approximation, side-length deviation about 0.5% (empirical value). Method B (computed chord): sin18°=0.309 (56.5 table) → side=0.618R, set the compass directly | Mutual difference of the five sides ≤1 line-width; closure gap distributed back over the five sides per the Chapter 22 closure rule |

The 3-, 4-, 6-, and 8-side cases are exact constructions; the 5-side case is approximate + closure correction — the registration sheet must state which side count used the approximate method (an honest precision account).

#### 56.1.5 Scaling Up and Down (the similar-triangle grid method)

Use: enlarging a 1:1 drawing to the layout yard, or shrinking a large yard layout onto a clay tablet.

Steps: ①grid the original drawing with squares whose side = 2–4 times the smallest feature size of the original (empirical window: each cell contains at least one feature point; too fine doubles the work, too coarse distorts); ②grid the target surface at magnification k, cell sides scaled by k in step — **k may only take integer ratios and simple fractions such as 2, 3, 1/2, 1/3** (Section 3.6 discipline: use only re-checkable ratios); ③transcribe cell by cell: feature points are recorded as "which row, which column + position within the cell", the in-cell position transcribed as readings like "so many finger-widths from the left edge, so many from the bottom edge"; ④verification: pick any 3 feature lines spanning multiple cells and measure their lengths — the ratio must =k (±2 line-widths); for circular features re-verify that the radius ratio =k. **Error registration**: grid lines are stepped off at equal spacing with dividers + cell-by-cell checking; mutual difference of cell spacings ≤1 line-width.

#### 56.1.6 Dividing a Circle (construction methods + error registration)

A graded route; each level uses only already-verified operations:

- **2/4/8/16 divisions**: diameters + successive perpendicular bisection (56.1.1 Method 2 applied to radius segments); a closure check at every level.
- **3/6/12 divisions**: chord stepping with the radius opening (chord = radius).
- **5/10 divisions**: the 56.1.4 pentagon Methods A/B.
- **24 divisions (15° per division)**: make 12 and 8 divisions independently, by two routes; check coincidence at the common-multiple points — **intersections of two independent routes coinciding to ≤1 line-width is the hard test of division quality**.
- **90 divisions (4° per division)**: serves 56.5 and the angle gauge; using the chord table (fed back after 56.5 builds it), re-verify one point every 6 divisions.
- **Error registration**: after any division is completed, walk the whole circle and register the "start-to-finish closure error", distributing it evenly back over the segments by division count (the Chapter 22 system) — this compass thereby gains its own "division-correction account", filed.
- **Boundary**: prime-number divisions like 7/9/11 have no construction method — once the sine table exists, route around by computing the chord as "chord=2R·sin(θ/2)"; until then, 7 divisions may only use the approximate chord 0.868R + even closure distribution, registered as a downgraded accuracy class.

### 56.2 Building the Logarithm Table

**What a logarithm is (one-sentence engineering statement)**: the logarithm demotes multiplication and division to addition and subtraction — log(ab)=log a+log b, log(a/b)=log a−log b. Two lookups, one addition or subtraction, one reverse lookup: three table operations replace one long multiplication. Engineering payoff: multiplication and division of two-digit numbers (two reliable digits (±1%), third digit for interpolation reference only) goes from "half an incense stick of longhand work + error-prone" to "ten breaths + cross-checkable"; and the log table is also the key to roots — **divide by two and reverse-lookup: that is a square root**.

**Precision budget first (silent failure first)**: errors are computed before building — square-root anchor ±0.3% (empirical), cumulative-multiplication drift ±0.5% (empirical), table-lookup interpolation ±0.3%; the relative errors of multiplication/division add (Section 25.11 Rule 2), combining to ≤±1.5%. **Commitment: the first two digits of a result are reliable, the third digit is suspect (interpolation reference only). That is nothing to be ashamed of — spurious precision is.**

#### 56.2.1 Four Steps to Build the Table

**Step 1: square root by construction (the geometric-mean method)** — the whole table's only external input is the single geometric fact that "the square root can be constructed":

1. On a line take O and B with OB=a+1; on OB take A so that OA=1, AB=a;
2. Draw a semicircle on OB as diameter (find the center by 56.1.1 Method 2; peg it in place and draw the circle);
3. Erect the perpendicular to OB through A (Method 2), meeting the semicircle at C — **AC=√a**;
4. Principle: the right-triangle altitude theorem, AC²=OA×AB=1×a. **Verification**: build a square on side AC and compare areas with an a×1 rectangle by cutting and rearranging; take the median of three independent constructions (the 3.4 procedure). **Self-check anchor**: a=4 must give exactly 2; a=9 gives 3 — a technique that fails this gate may not go further. **Precision**: ±0.3% (empirical, must be field-calibrated: the self-check anchor deviation is the demonstrated precision of the technique, entered in the ledger).

**Step 2: the anchor chain**: starting from √10=3.162, construct square roots six times in succession: 10^(1/2)=3.162 → 10^(1/4)=1.778 → 10^(1/8)=1.3335 → 10^(1/16)=1.1548 → 10^(1/32)=1.0746 → 10^(1/64)=1.0366 → **common ratio c=10^(1/128)=1.0182** (the fourth digit is untrustworthy; write only four digits). At each level take the median of three constructions. **Closure check**: the theoretical value of c is 10^(1/128)=1.0182; the constructed value must differ from the table by ≤0.5%; the whole-chain gate is c multiplied back out to 10, with stepwise verification against the master table substituted for physical repeated multiplication (c multiplied by itself 7 times ≈1.13, not a return to 10).

**Step 3: the master table by cumulative multiplication**: a 128-row geometric sequence; row 0=1.000; each row multiplied by c gives the next; row 128 must=10.000; the logarithm of row number m is m/128.

- **Drift control (critical)**: set check anchors every 16 rows — row 16=1.3335, row 32=1.778, row 48=2.371 (=1.3335×1.778), row 64=3.162, row 80=4.217, row 96=5.623, row 112=7.499 (=10÷1.3335), row 128=10.000. The anchor values follow from multiplying one another; the anchor system is self-consistent and needs no new measurements. When a row value differs from its anchor by more than 0.005, the deviation is distributed proportionally back over that 16-row run (corrected directly when the table is transcribed).
- **Cross-check system**: two people each build the master table once; per-row mutual difference ≤0.005; out-of-tolerance rows are adjudicated by a third builder (transplanted 3.4 procedure).

**Step 4: transcribing the main table (90×10 cells)**: rows = true values 1.0–9.9 (step 0.1); columns = second decimal digit (0–9); each cell holds the logarithm to two decimal places (two reliable digits (±1%), third digit for interpolation reference only), the value read from the master table + linear interpolation:

- Interpolation procedure: if x falls between master-table rows m and m+1, then log x≈m/128+(x−row value)÷(next row−row value)×(1/128);
- **Densification points**: the master-table row spacing is 0.018 at 1.0 and 0.18 at 10 — **in segments where the row spacing exceeds 0.1 (roughly x>6), insert midpoint rows first**: midpoint value=√(upper row×lower row); each inserted point is cross-checked by two methods, "square root via the log table" and the arithmetic midpoint; identical values pass;
- The main table's 900 cells take about 2 person-days; spot-check 10 cells by hand computation (multiply 10^log back to the true value, ±0.5%).

#### 56.2.2 Usage Procedures and Three Worked Examples

Five rules: ①table readings give two reliable digits (±1%), third digit for interpolation reference only; mental arithmetic never enters the table; ②magnitude self-check (the Section 25.8 four-piece set) — fix the power of 10 first, then compute the mantissa; ③spot-check one in ten of the critical numbers entering the archive with manual multiplication; ④error annotation per 25.11; ⑤**"the slide rule estimates the scheme, the tables fix the numbers"** (56.3).

**Example 1 (multiplication)**: 472×36.5. log 472=2.674, log 36.5=1.562; sum=4.236; reverse lookup 0.236→1.72; result=1.72×10⁴=17200. Magnitude check: 500×37≈18500, same order ✓. Error: about ±1.5%; report 1.72×10⁴.

**Example 2 (division)**: 850÷46. log 850=2.929, log 46=1.663; difference=1.266; reverse lookup 0.266→1.845; result≈18.5. Magnitude check: 850÷50=17 ✓. Report 18.5 (±2%).

**Example 3 (square root)**: √200. log 200=2.301; ÷2=1.1505; reverse lookup 0.1505→1.414; result≈14.1. Magnitude check: 14²=196 ✓. Report 14.1 (±2%).

(Square = the special case of multiplication, log×2; reciprocal = 0−log — one table covers five operations: multiplication, division, squaring, square root, reciprocal.)
[Card 56-01 Logarithm table compilation ] (eight fields)
1. **Input materials**: 1 construction board (passing the two-position fit check), standard rods, two carriers for the master table; one 128-row pass takes about 2 tablets. Substitute: all-clay-tablet in the paperless period (raises transcription frequency).
2. **Required tools**: compass and dividers (repeatable opening), right-angle square and scriber (Chapter 19), certified straightedge, magnifier; calibration: the compass's two trial circles coincide; the straightedge passes the two-position check against the light.
3. **Operation sequence and control points**: square-root self-check (a=4→2, a=9→3) → six anchor-chain levels in succession (median of three at each level) → **c checked against the table value 1.0182 (difference ≤0.5%) — failing this, going further is forbidden** → master table by cumulative multiplication → anchor verification every 16 rows, deviation distributed back proportionally → two independent builders, mutual difference ≤0.005 → main table transcribed with interpolation (densify the x>6 segment first) → spot-check 10 cells by back-multiplication (±0.5%).
4. **Empirical parameters and calibration**: c=1.0182 (±0.3%; calibration: median of three constructions + the self-multiply-7-times closure check); anchor-deviation red line 0.005 (calibration: from the first table, tally whole-table anchor deviations and take the measured P95; transcribe into the ledger, Chapter 43).
5. **In-process observation records**: three readings per square-root level; anchor deviations entered in an "anchor-deviation column" every 16 rows; both builders and the date in the table header; any change of compass opening noted by row number.
6. **Pass / rework / scrap criteria**: pass = all anchor deviations pass, mutual differences on target, all spot checks pass; rework = individual rows out of tolerance (re-multiply and re-distribute that 16-row segment); scrap = c^7 closure failure (>0.5%) — return to the self-check anchors, retrain the construction technique, then rebuild.
7. **Common failures and troubleshooting order**: the master table drifting ever further off → first check for a miscopied fourth digit of c, then skipped rows, finally miscopied anchor values; isolated wrong cells in the main table → first check whether they lie in the un-densified x>6 region, then transcription line-skips, finally identical errors by both builders (identical errors mean a bad master-table row — return to the master table).
8. **L1/L2/L3 evidence**: L1 = master table + the three worked examples on paper; L2 = main table + spot-check records + a third person's blind check passed; L3 = dual backup at separate sites, the c value and anchor table entered in the ledger, the next generation reproducing it independently from the card.

### 56.3 Slide-Rule Manufacture

**Why it is worth making**: the log table is "compute by lookup" — three lookups per problem; the slide rule is **the logarithm table engraved on a stick** — push the slide and read directly — ten breaths per problem. Input versus output: the master rule costs 3–5 person-days; thereafter each working rule takes 1–2 days to copy; consumption is near zero; the whole settlement uses it for ten years — the same investment class as machine-tool metrology.

#### 56.3.1 Scale Principle and the Three-Scale System

- **Principle**: on the rule, the mark for x sits at distance L·log(x) from the left end — "multiplication of numbers" becomes "addition of lengths". Push the slide so that C's 1 aligns with D's a; then the D reading under C's b = ab (two lengths added).
- **Rule length L=250 mm class** (empirical, must be field-calibrated: the longer L, the finer the reading; a short 150 mm-class rule degrades to ±4% error — carry-along quick-calculation only, no ±2% promise).
- **The C/D/A three-scale system**: the D scale (lower fixed stock) runs 1–10; main line positions = L×log value, each computed from the 56.2 master table and registered into a "scale-line position table" — **this is the construction drawing for engraving the rule; estimating lines by eye in the field is forbidden**. The C scale (the slide) is graduated exactly like D. The A scale (second row of the lower fixed stock) runs 1–100, line positions = L×log(x)/2 — when the cursor line reads a on D, the same line on A reads a²; conversely, read N on A and look at D to get √N.
- **The line-density trade-off (honest)**: graduating all of 1–10 to two reliable digits (±1%), third digit for interpolation reference only, would take about 500 lines on 250 mm — beyond hand methods. The trade-off: **the 1.0–2.0 segment at 0.02 per division, 2.0–5.0 at 0.05 per division, 5.0–10 at 0.1 per division** — a log scale is naturally dense on the left, sparse on the right; this segmentation follows the density, about 120 secondary lines in all, within scriber reach.
- **The master-rule system**: build one master rule first; after it passes inspection it serves as the template from which working rules are copied (the Chapter 22 first-article-inspection concept); the master rule is sealed away, and working rules are checked against it monthly (the Chapter 3 monthly-check system transplanted).

#### 56.3.2 Engraving and Cursor Workmanship

- **Rule blanks**: bamboo/linden, shade-dried one season (dryness test: weighed across two weeks with no weight change — Chapter 3 standard transplanted), wax-soaked against moisture; the working face mated to the surface plate shows no gap against the light (Chapter 20 concept).
- **Engraving**: scribe along a certified straightedge, depth judged by "a fingernail stroke can feel it, yet it does not prick the hand"; after engraving, rub soot ink in to raise contrast.
- **Slide groove**: the slide sits between the upper and lower stocks, running freely over the whole travel with no lateral play — **lateral play = systematically wrong readings**. Criterion: push to mid-travel and lift the slide lightly; verify 0.3 mm with the paper-gauge method (two 0.3 mm sheets together will not enter; a single sheet will — empirical value).
- **Cursor**: a wooden frame clamping a glass window (Chapter 24), a fine copper wire waxed at the window's center as the hairline; line-straightness criterion: rotate the window 45° and the line shows no kink.
- **Reading technique ◎**: the line of sight must be perpendicular to the rule face — **parallax is the slide rule's number-one error**. Practice: stand a small mirror of polished copper sheet beside the rule; when the hairline and its mirror reflection join into one line, the sight line is perpendicular. With no mirror, two people cross-check (one reads, one watches the sight angle from the side). Misjudgment compensation: for critical readings, nudge the cursor half a division left and right and take the midpoint of the two readings.

#### 56.3.3 Graduation Criterion and Typical Usage

**Graduation (the 10-problem method)**: the quiz-setter works out 10 problems by hand (4 multiplications, 3 divisions, 2 proportions, 1 square — all two-digit numbers, two reliable digits (±1%), third digit for interpolation reference only); the trainee completes them on the slide rule within half an incense stick. **All errors <2% and not a single magnitude error** passes; three groups, all passed, on 3 consecutive days, graduates. A magnitude error (a 10× error) is an automatic veto — the slide rule reads only significant figures; **the power of ten must be held by your own mental arithmetic**: this is the procedure's second maxim.

Table of typical uses:

| Task | Operation sequence | Worked example |
|---|---|---|
| Multiplication | Set C's 1 against D's a; read the D line under C's b | 4.72×3.65→read 17.2 (actually 17.23); magnitude check 4.7×3.7≈17 |
| Division | Set C's b against D's a; read under C's 1 | 850÷46: set 4.6 against 8.5, read 1.85 under the 1→18.5 |
| Proportion chain | Set C's a against D's b; thereafter read below any number on C for the answer | Saltpeter boiling 5:1 (Chapter 23): after 60 is set against 12, any nitre-earth quantity on C reads its required ash quantity directly below |
| Square | Set the cursor line to a on D; read A on the same line | D 2.41→A 5.81 |
| Square root | Set the cursor line to N on A (N<10 use the left half, 10–100 the right half — the place-determination mnemonic), read D | A 2.00→D 1.41 |

**Accuracy division-of-labor statement**: the slide rule is ±2% (the first two digits reliable); numbers entering the archive are re-verified with the log table or by hand — "the slide rule fixes the scheme, the tables fix the numbers" is written into the system.
[Card 56-02 Slide-rule engraving ] (eight fields)
1. **Input materials**: shade-dried bamboo/wood blanks (2 fixed stocks + 1 slide, straight grain, knot-free), 1 thin-glass window, 1 length of fine copper wire, 20–30 g beeswax, soot ink. Substitute: with no glass, read the rule face directly (parallax risk rises — switch to a two-person mutual-reading system).
2. **Required tools**: scriber (Chapter 19, trial-scribes 10 lines without a break), certified straightedge, surface plates for mutual fitting, magnifier, **an accepted logarithm table (56.2, the data source for the scale lines)**; calibration: the blank faces mutually fitted show no gap against the light.
3. **Operation sequence and control points**: compute the scale-line position table (register L×log values line by line) → engrave the master rule D/C → inspect (field 6) → engrave working rules by copying the master → cut the groove and fit the slide (play ≤0.3 mm) → fit the cursor hairline → wax-soak and ink-fill → engrave the serial number and the L value on the rule's underside. **Control points: the position table must come from an accepted logarithm table; a master rule that has not passed inspection may not be copied into working rules**.
4. **Empirical parameters and calibration**: L=250 mm (calibration: actually measured with a standard rod, engraved into the rule's underside); line segmentation 0.02/0.05/0.1 (calibration: trial-engrave a 50 mm stretch and set the class by whether the second digit is readable); play 0.3 mm (the two-sheet paper gauge).
5. **In-process observation records**: a "computed/actually engraved" comparison column for every main scale line; slide paper-gauge records; hairline rotated-window checks; an error list from 5 trial calculations.
6. **Pass / rework / scrap criteria**: pass = all main-line position errors ≤0.3 mm, all 5 multiplication trials <2%, the slide running freely over the whole travel; rework = individual lines out of tolerance (scrape the wax and re-engrave that line); scrap = warped blank (gaps show in mutual fitting) or groove play beyond repair — new blank, remake.
7. **Common failures and troubleshooting order**: trials biased in the same direction → first check whether the measured L and the position table carry the same value, then whether the slide is mounted reversed, finally whether the hairline is not perpendicular to the rule's long axis; the second digit unreadable in the 1.0–2.0 segment → wrong segmentation boundaries (return to field 4 and re-set); the slide sticky → wax lumps or uneven groove width (scrape the groove and refit).
8. **L1/L2/L3 evidence**: L1 = one master rule + the 5-problem trial sheet; L2 = monthly-check records for 2 working rules + the graduation records of 3 groups of 10 problems; L3 = the position table archived, the master-rule seal system, a second person building a rule independently from the card.

### 56.4 Calendar and Farming-Season Calculation

The engineering essence of a calendar: turning "when to sow, when to open the stores and check the grain" from memory into **tables that can be registered, re-checked, and handed over**. The error red line: a farming-season drift of ±5 days ruins a season — the Chapter 10 reserve system presumes that farming seasons are predictable; this chapter's solstice determination is ±2 days, leaving double the margin against the red line.

#### 56.4.1 The Shadow Solar-Term Table

- **Site**: the 3.2.1 true-north-line site (scribed lines and set pegs in place) and the same gnomon pole (about 1.5 m tall, plumbed straight in two directions).
- **Daily registration**: every day at noon, measure the "pole base to shadow tip" length and enter it on the calendar board (one board per season; two columns, date + shadow length). Noon-fixing method: mark the shadow tip twice before and twice after noon and take the shortest position — watch the shadow, never the sun (a Chapter 3 red line).
- **Solstice determination (the ±2-day method)**: near the solstice, the change in shadow length approaches zero — criterion: **for 3 consecutive days, mutual differences in shadow length ≤1/5 of the average daily change over the previous 10 days (empirical value, must be field-calibrated: after the first full-year table is complete, look back at the solstice window, re-verify this threshold, and transcribe it into the ledger)**; take the median day of the 3 as the solstice. Winter solstice = the longest-shadow window; summer solstice = the shortest-shadow window.
- **Why only ±2 days (honest)**: near the solstice the shadow curve is "flat-topped", its day-to-day differences flattened to the same order as measurement error — ±2 days is the single-year limit of hand methods; ±1 day would need multi-year averaging, listed as a multi-year system and kept out of the first-round commitment.
- **Measuring the year's length**: register the number of days between consecutive years' solstices (median days) on counting tallies (one notch per day, five dots to a bar, 3.6) — a single year must yield 365 or 366; **deciding the leap on 1 year alone is forbidden**; average 4 consecutive years and it converges to near 365¼.

#### 56.4.2 Leap-Year Correction (hand-method re-synchronization)

- The regular system: the calendar face runs 365 days/year; the measured mean is about 365¼ → insert 1 leap day after the winter solstice every 4 years;
- **The re-synchronization red line (harder than the leap-year rule)**: the measured winter solstice must be taken every year; **when the calendar-face solstice and the measured solstice differ by ≥3 days, insert a leap day to re-synchronize immediately — waiting for the next scheduled leap year is forbidden** — the farming-season red line is ±5 days; re-synchronization triggers at ±3 days, leaving a buffer;
- The precision correction "subtract 1 day every 128 years" is declared as it stands: that is a millennial system — not promised in the first rebuild, only written into the ledger notes, so later generations do not mistake it for a first-round task.

#### 56.4.3 Fixing the Season by Star Risings and Settings (cross-validation)

The shadow table fears long overcast spells — in the cloudy season, stars stand in. Choose 3–5 bright stars in the local eastern sky and register their "morning first-appearance" dates (first seen above the eastern horizon before dawn). Three institutional rules: ①the same site (the true-north-line site), the same observing position; ②the "first-appearance" criterion = **visible on two consecutive days** (a single day may be a misidentification); ③the same observer throughout — changing observers requires a two-season handover star-check (Chapter 43). Source of the star table: the Chapter 53 island edition already has the "self-made star rising/setting azimuth table" system — this chapter converts it from a navigation tool into cross-validation for the solar-term calendar: each star's morning first-appearance recurs on the same date every year; cross-check it against the shadow table's solstice; **a disagreement between the two routes of more than ±3 days sends you back to the observation records** (the astronomical version of the Chapter 23 dual-route mutual check).

#### 56.4.4 The Farming-Season/Grain-Storage Cycle Alignment Table

Three-column comparison (calendar-face skeleton × farm work × grain storage; action items reference Chapter 10):

| Solar-term anchor (calendar face) | Farm action (Chapter 10) | Storage/ledger action |
|---|---|---|
| Winter solstice (year-start anchor) | Annual seed-selection plan; cold-moist stratification started | Whole-store inventory; accounting-year settlement (Chapter 38) |
| Sowing window (local shadow-length value + phenological anchors) | Field sowing | Verify the reserve seed quantity (next season's sowing quantity ×2) |
| Summer solstice | Intertillage; mid-season irrigation inspection | Semiannual spot check: open and inspect one batch each of the dried/smoked/fermented/pit stores |
| Autumn-equinox slot (the shadow length falls back through its registered value) | Harvest begins; ear-selection seed-saving in parallel | Into the store, onto the books |
| 30 days after the solstice (locally fixed slot) | Late-autumn field-care wrap-up | Stored-grain seasonal pest-and-damp inspection (Chapter 10 cycle) |

- **The system**: the sowing window and the harvest window are locally measured phenological values — the first year relies entirely on registered shadow-length values + 3 local phenological anchors (apricot blossom opening, first frog calls, and the like — chosen locally and registered year by year); from the second year on, alignment corrections apply; **the "phenological-anchor-to-shadow-length correspondence book" is this chapter's most important agricultural asset**, transcribed into the ledger (Chapter 43) with an off-site copy (3.6).
[Card 56-04 Solar-term calendar table ] (eight fields)
1. **Input materials**: 1 true-north-line site (scribed lines and pegs intact), 1 gnomon pole (1.5 m class), calendar boards (one per season), counting tallies. Substitute: in the no-clay-tablet period, notched wooden strips + a knotted-cord index (3.6, as index only).
2. **Required tools**: standard rod (measuring shadow lengths), A-frame level (annual site check), plumb line; calibration: the pole plumbed in two directions against the line; the true-north line's annual check — the intersection angle re-measured on two days differs ≤half a finger-width (3.2.1).
3. **Operation sequence and control points**: register noon shadow lengths day by day (missed days are back-filled the next day, marked "back-filled") → identify the solstice window → fix the solstice anchor → count the year's length → star first-appearance cross-validation → at year's end transcribe the next year's calendar face and the alignment table. **Control point: the solstice may never be judged by "feeling that the shadow has stopped shortening" — you must back-calculate the average daily change over the previous 10 days against the threshold**.
4. **Empirical parameters and calibration**: solstice threshold = 1/5 of the average daily change over the previous 10 days (re-calibrated with the first year's data); re-synchronization trigger ±3 days (basis: the ±5-day red line minus the shadow table's own ±2 days, then halved); 3 phenological anchors (their class set by two years of alignment correction).
5. **In-process observation records**: daily shadow length, weather (overcast days entered as "no shadow", not counted), observer; star first-appearance dates and the consecutive-visibility judgment; leap-day insertion dates and reasons.
6. **Pass / rework / scrap criteria**: pass = the solstice has 3-day window evidence + star-table mutual difference ≤±3 days; rework = insufficient window evidence (carry on with the interval median and mark the class downgraded); scrap = the site was disturbed (true-north annual check out of tolerance) — that season's data voided and re-measured.
7. **Common failures and troubleshooting order**: solstices misaligned between two years → first check for a change of observer and of stance, then pole-base settlement (if the pole's height changes, every shadow changes), finally the density of missed records (a season with >10 missed days is downgraded); a large star-table/shadow-table disagreement → first check the star criteria (single-day misrecords), then the true-north site, finally a missed leap-day insertion.
8. **L1/L2/L3 evidence**: L1 = one season's shadow-length board + solstice determination records; L2 = two consecutive years' solstices + year-length counting + leap-day system operation records; L3 = the alignment table and phenological-anchor book entered in the ledger with dual backup, handover star-check records, the next incumbent continuing the tables from the card.

### 56.5 Practical Trigonometric Tables

**Why needed**: ramp layout (Chapter 13), the ice road's descending gradient (Chapter 51 Section 51.13), measuring tower and tree heights, judging the sun's angle — every case of "know the angle, find the side; know the side, find the angle". This chapter builds only a sin/tan table over 0–90° in 7.5° steps: 13 rows suffice, interpolation covers the gaps between rows.

#### 56.5.1 Building the Sine Table by Dual Routes

**Route A (geometric square-root chain, paper computation)**:

1. Three base angles constructed exactly: sin30°=0.5 (opposite side over side in an equilateral triangle), sin45°=0.707 (diagonal over side in a square, √2 by constructed square root), sin60°=0.866;
2. The half-angle chain downward: sin²(θ/2)=(1−cosθ)/2 — apply square roots repeatedly (the log-table method: log÷2 then reverse lookup, 56.2 Example 3) to get 15°, 7.5°, 3.75°;
3. Angle-sum accumulation: sin(α+β)=sinα·cosβ+cosα·sinβ — generate the whole table cell by cell in 7.5° steps (multiplications via the log table);
4. Precision: the whole table at the ±0.01 absolute-error class (empirical); small-angle rows have large relative error but small absolute values — the 3.75° row is ±2% relative, registered as it is.

**Route B (large-circle chord measurement, physical measurement, cross-checked against A)**:

1. On level ground draw a large circle of R=1 m (radius measured independently twice with a standard rod, difference ≤2 mm);
2. Lay out central angle 2θ (24 circle divisions give 15° central angles — verified in 56.1.6; angle blocks from Chapter 22 can reinforce it) and measure the subtended chord s;
3. **sinθ=s/2R** (inscribed-angle theorem: the chord subtending central angle 2θ = 2R·sinθ) — chord readings ±2 mm → sin to the ±0.001 class (when R=1 m);
4. **Mutual check**: the two tables compared row by row; mutual difference ≤0.005 passes; out-of-tolerance rows are adjudicated by a third method — re-measure the construction or re-do the arithmetic — and the agreeing value taken.

tan column: tanθ=sinθ/cosθ (log-table division); **guaranteed only over 0–45°** — tan diverges at large angles; above 45° use the cot reverse lookup (written into the system; forcing a direct lookup is not allowed).

Table sample (first 5 rows illustrative; the full 13-row table enters the archive):

| θ | sinθ (value taken after A/B mutual check) | tanθ |
|---|---|---|
| 7.5° | 0.131 | 0.132 |
| 15° | 0.259 | 0.268 |
| 22.5° | 0.383 | 0.414 |
| 30° | 0.500 | 0.577 |
| 45° | 0.707 | 1.000 |

#### 56.5.2 Three Application Procedures

**Procedure 1 (slope-to-rise conversion, serving Chapter 13 layout and the Chapter 51 ice road)**: slope is uniformly expressed as "a rise of n finger-widths per rod" (avoiding percentage mental arithmetic). Worked example: a slope run 20 rods long, rising 6 finger-widths per rod → total rise 120 finger-widths (about the 2.2 m class, per the local finger-to-rod conversion); reverse the table for the angle: 6 finger-widths per rod is roughly a 5–6° slope angle (interpolated in the tan table). Ice-road routes should be gentle — the ≤3 finger-widths per rod class (within 3°): Chapter 51 only gives route selection and haulage-formation discipline; the slope class is set by reverse lookup in this table, entered in the ledger.

**Procedure 2 (measuring heights, tower/tree/cliff)**: stand d rods from the target, measure the elevation angle θ with the chord angle-gauge; height=d×tanθ+eye height. Worked example: 15 rods from a tower, elevation 10° (±1°) → height=15×0.176=2.64 rods; error: at ±1°, tan10° changes by about ±10% relative (25.11: the angle error dominates) → report 2.6 rods (±10%). **Error-reduction method**: switch to the two-station method — measure the angle at two stations and take the difference; the gauge's systematic bias cancels in the difference (the dividend of comparative measurement).

**Procedure 3 (the chord angle-gauge, an extension of the Chapter 22 angle blocks)**: a semicircular plate with main graduations at 24 divisions (the 15° class, 56.1.6), chord interpolation down to the 5° class; two pins as the sighting device. **Accuracy commitment: the ±5° class** — criterion: reading back a known 90°/45° angle on the true-north site differs by ≤1 class; falsely labeling it ±1° is forbidden (spurious-precision discipline).
[Card 56-03 Sine table by measurement ] (eight fields)
1. **Input materials**: level ground ≥2.5×2.5 m (stone slab/tamped earth), thin wooden strips as chord rules, several pegs. Substitute: with no large ground available, draw an R=0.5 m circle (sin precision degrades twofold to the ±0.002 class — registered as an honest downgrade).
2. **Required tools**: standard rod (R=1 m measured twice), long-arm compass (pole + rope substitute), scriber, right-angle square, angle block set (Chapter 22); calibration: the long-arm compass draws a full circle whose 8-direction radii differ by ≤2 mm.
3. **Operation sequence and control points**: draw the large circle → 24 divisions (closure check passed) → connect chords angle by angle → measure each chord three times and take the median (one pass by a different person) → divide by 2R to get sin → compare row by row with the Route A table, mutual difference ≤0.005 → transcribe the passing rows into the main table. **Control points: both chord ends must be read at scribed-line centers; the pegs are checked once on the day**.
4. **Empirical parameters and calibration**: R=1.000 m (calibration: two independent radius measurements differing ≤2 mm; re-measured across seasons); chord readings ±2 mm (calibration: demonstrated by the range of three passes by two people on the same chord); mutual-difference red line 0.005 (after the first table, the class is re-set from the measured distribution and entered in the ledger).
5. **In-process observation records**: three chord readings per angle and the observer; temperature anchor (cool/warm class — the ground expands and contracts); the source of each central angle (division number or angle block number).
6. **Pass / rework / scrap criteria**: pass = all 13 rows meet the mutual-difference target; rework = individual rows out of tolerance (re-draw the chord at that angle and re-measure; if 3 passes still fail, adopt the Route A value and annotate "measured check failed, computed value used"); scrap = the circle center has shifted or the re-measured radius differs >2 mm — the whole table voided and re-measured.
7. **Common failures and troubleshooting order**: the whole table biased high → first check whether the measured R came out small, then whether chords were read on the outer arc line (line-width reading bias), finally whether central angles ran large (closure error not distributed); individual rows off → first check peg looseness at that angle, then bowing of the chord rule (two-position straightness check).
8. **L1/L2/L3 evidence**: L1 = one 13-row table + A/B mutual-difference records; L2 = a second person's independent re-measurement on target + the angle gauge's readback records on known angles; L3 = the main table archived with dual backup, red-line values entered in the ledger, the slope-conversion worked example entered into the teaching materials (Chapter 43).

## Master Parameter Table

| Parameter | Value | Category |
|---|---|---|
| Construction line width | 0.5–1 mm; ±0.1% order on a 1 m format | Physical limit |
| Square-root construction precision | ±0.3% (self-checks a=4→2, a=9→3) | Empirical |
| Log table whole-table accuracy | ±1% class; the first two digits promised reliable | Boundary |
| Master table anchor-deviation red line | 0.005 (re-set from measured P95, entered in the ledger) | Criterion |
| Slide-rule length | 250 mm class; 150 mm class downgraded to ±4% | Empirical |
| Slide-rule reading accuracy | ±2%; a magnitude error is an automatic veto | Criterion |
| Slide play | ≤0.3 mm (two-sheet paper gauge) | Empirical |
| Graduation criterion | all 10 problems <2%, 3 groups over 3 consecutive days | System |
| Solstice determination | ±2 days (3-day window criterion) | Boundary |
| Leap-day re-synchronization trigger | calendar face vs. measurement differ ≥3 days — insert immediately | System |
| Farming-season drift red line | ±5 days | Red line |
| Sine table | 0–90° in 7.5° steps, ±0.01 absolute-error class; A/B mutual difference ≤0.005 | Boundary |
| Angle-gauge accuracy | ±5° class (no false labeling); slope expressed as n finger-widths per rod | Boundary |

## Failure Modes and Diagnosis

| Symptom | Candidate causes (by probability) | Verification | Disposition |
|---|---|---|---|
| Log table drifts further with every multiplication | miscopied c / skipped row in cumulative multiplication / wrong anchor values | c^7 closure check; re-read the anchor-deviation column | Re-multiply that segment; re-construct wrong anchors |
| Slide-rule trials biased in one direction | inconsistent L / C scale mounted reversed / hairline tilted | Measure L and compare against the position table | Unify the L value; re-mount the slide |
| Frequent slide-rule magnitude errors | power-of-ten mental arithmetic not guarded | Add power-of-ten checks to the problems | Retrain on the procedure; delay graduation |
| Master rule drifts at monthly check | blank swollen by moisture | Weigh to judge water content (Chapter 3) | Re-wax-soak; replace the blank if over limit |
| Solstices misaligned between years | observer changed / pole settled / many missed records | Review the annual-check records | Handover star-check; re-set the pole |
| Star table vs. shadow table differ >3 days | single-day misrecord / leap day missed | Re-verify with the two-consecutive-days criterion | Insert the missed leap day and re-synchronize |
| Sine table systematically biased | R measured small / chords read on the outer arc | Re-measure the radius | Re-measure R; re-read at line centers on the inner arc |
| Interpolated results out of tolerance | x>6 segment not densified | Check row spacing in the interpolated region | Add midpoint rows and re-interpolate |

## Process Card Index

【56-01】Logarithm table compilation (embedded in 56.2)｜【56-02】Slide-rule engraving (embedded in 56.3)｜【56-03】Sine table by measurement (embedded in 56.5)｜【56-04】Solar-term calendar table (embedded in 56.4)

## Acceptance Criteria L1/L2/L3

- **L1**: every method of the construction set executed once with verification and registered; one master table + three worked examples; one master rule + a 5-problem trial sheet; one season's shadow-length board + solstice determination records; one 13-row sine table + A/B mutual-difference records.
- **L2**: the main table's 900 cells transcribed, the 10-cell spot check fully passed; 2 working rules under monthly check against the master rule, on record; the two-person master-table cross-build within mutual-difference target; two consecutive years' solstices + star-table corroboration; the sine table independently re-measured by a second person, on target; the angle gauge reads back known angles to ≤1 class.
- **L3**: the slide-rule graduation system running (graduation records for ≥3 people); the alignment table and phenological-anchor book entered in the ledger with dual backup; any damaged master item (master table / master rule / calendar site) rebuilt within 7 days per the card and meeting the mutual-difference target; a second settlement independently reproducing one table and one rule from the card (blind-build verification, 3.7).

## Work Hours, Manpower, and Consumption

| Item | Manpower | Work hours (empirical) |
|---|---|---|
| Full drill + registration of the construction-methods set | 2 people | 2–3 days |
| Anchor chain + master table 128 rows (cross-builds included) | 2 people | 1 person-day each |
| Main table 90×10 transcription + spot checks | 2 people | 2–3 person-days |
| Master rule engraving (position table included) | 1–2 people | 3–5 days |
| Copying working rules | 1 person | 1–2 days per rule |
| Slide-rule graduation training | 1 master with ≤4 apprentices | apprentice 6–10 days (one group per day) |
| Shadow calendar, first year | 1 person (about 5 min per day) | ongoing all year + half a day transcribing boards at season's end |
| Sine table, dual routes | 2 people | 2–3 days |
| Consumables | wax, soot ink, bamboo/wood blanks, clay tablets/paper | entered in the Chapter 38 ledger |

## Safety Boundaries

- The long-arm compass and scriber are passed point-down, gripped by the handle, never carried in the mouth; while scribing, the other hand stays out of the line's extension direction (extension of the Chapter 3 red line);
- Looking directly at the sun is forbidden during shadow observation — fix noon by watching the shadow, not the sun; avoid bright light for the 10 min before star observation to preserve dark adaptation, and clear the site of obstacles;
- Keep wax-soaking work away from fire (wax is flammable); mix soot ink at a ventilated spot (echoing 25.8);
- Night visits to the calendar site go in pairs; lamps stay clear of the peg zone.

## A. Existing Tool Inventory

Standard rods and bisection-scribed lines, the true-north line and shadow yard (Chapter 3); three-rod mutual check and surface plates (Chapter 20); hardened scribers (Chapter 19); angle blocks and even closure-error distribution (Chapter 22); magnifiers and thin glass (Chapter 24); rough error-propagation calculation, the five recording elements, and the engineering-estimation four-piece set (Chapter 25); the star rising/setting azimuth table system (Chapter 53); the ledger and blind-build verification (Chapter 43, 3.7); paper-and-ink carriers (Chapter 41); ice-road route-selection standards (Chapter 51 Section 51.13).

## B. New Tools Added in This Chapter

The geometric construction-methods set (three perpendicular methods / two parallel methods / angle bisection / regular polygons 3-4-5-6-8 / grid scaling / circle division with closure-error registration); the square-root construction (geometric mean + self-check anchors); the local logarithm table (master table 128 rows + main table 90×10, ±1% class) with the three worked-example procedures for multiply, divide, and square root; the slide rule (C/D/A three scales, cursor hairline, mirror parallax check, 10-problem graduation system, master-rule seal system); the shadow solar-term table and ±2-day solstice determination; year-length counting and the leap-day re-synchronization system (±3-day trigger); the star first-appearance cross-validation table; the farming-season/grain-storage alignment table and the phenological-anchor book; the dual-route sine table and tan column; the slope-to-rise conversion procedure (n finger-widths per rod); the chord angle-gauge (±5° class, two-station method).

## C. Unresolved Dependencies

- Four-digit precision for the log table (needs more anchors; an open problem, not scheduled); chord-table methods for prime-number divisions like 7/9 (unlocked once the sine table feeds back);
- Precision angle measurement at the ±1° class (graduated-dial turning, an extension of Chapter 22); densifying the sine table to 1° (ten times the work; a project on demand);
- A precision astronomical calendar (lunar phases, eclipses) — explicitly not done; old-world-class calculators — permanently "not done";
- 500-line-class dense engraving and replication processes for slide rules (the Chapter 27 instrument line).

## Next-Step Dependencies

- **All parts of the book**: the log table and the slide rule directly serve every multiplication and division in Section 25.8 estimation, the Chapter 38 ledger, and Chapter 37 population balancing — "estimate first, then fix the scheme" now has tools underneath it;
- Chapters 10/13: the farming-season alignment table back-fills the sowing window; slope conversion back-fills building and canal layout;
- Chapter 51: ice-road slope classes are set using 56.5.2 Procedure 1;
- Chapters 22/27: angle blocks and the angle gauge cross-calibrate each other; the graduated-dial upgrade line;
- Chapter 43: the phenological-anchor book, the sealed master table and master rule, and the graduation records enter the inheritance chain — **losing the ledger is treated as this chapter's processes being demoted back to Tier 1** (the G02 inheritance rule).
