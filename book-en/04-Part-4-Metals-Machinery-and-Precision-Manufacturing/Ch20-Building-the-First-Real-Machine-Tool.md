# Chapter 20: How to Build the First Real Machine Tool

## Chapter Objectives

Build the minimal capability chain for "the machine that builds machines": starting from the limits of hand precision, establish in turn the straightness datum, the flatness datum, screw threads, and cylindrical machining, finally build the first metal lathe, and master the bootstrap method of "using first-generation machine tools to build better second-generation machine tools."

**A machine tool is not a device that can simply appear; it is a route along which manufacturing capability accumulates step by step.** This chapter does not promise "modern precision if you follow along." It only promises that every level of precision has a source, is verifiable, and is repeatable.

## Capability Boundaries

**What can be done:**
- Establish from zero the four classes of geometric datums—flatness, straightness, squareness, screw threads—all with bootstrap sources (relying on no imported or inherited templates);
- Three generations of lathes: wooden spring-pole lathe → treadle flywheel lathe → cast-iron bed metal lathe; honest precision ceilings: turning ±0.05–0.1 mm class, scraping ±0.05 mm class, lapping ±0.005–0.01 mm class (empirical values, must be field-calibrated);
- Use error tables and compensation to make the second-generation machine more accurate than the first.

**Explicitly cannot be done:**
- Rolling bearings, ground guideways, milling machines (listed as Class-C dependencies, see the list at the end);
- Interchangeable threads (solved in Chapter 22; in this chapter all threads are used as numbered matched pairs);
- Modern-grade precision (±0.001 mm). Before chasing that number, first make this chapter's criteria solid.

**External dependencies:** The first-generation datum surface plates use **granite/diabase ground stone slabs** (no dependence on metal); cast-iron surface plates/lathe beds are listed as an upgrade item "after pig-iron casting capability is established" (white cast iron cannot be machined and is forbidden as plate/bed material). This chapter is the only place in the whole book where geometric datums are built from nothing—the precision of the Chapter 22 gauge blocks, the Chapter 28 cylinders, and the Chapter 31 rotating shafts all trace back to here.

## Pre-Work Verification (check off each item; do not start until every criterion passes)

| # | Verification item | Criterion | Source |
|---|---|---|---|
| 1 | Standard rods and equal-arm balance | Rods pairwise-compared give identical lengths (within ±0.5 mm); the balance can resolve a 1 g difference | Chapter 3 |
| 2 | 3-4-5 rope right angle | After tensioning, all three sides lie flat on the ground with no arching | Chapter 3 |
| 3 | Woodworking datum surface | Able to plane a board 500 mm long with diagonal difference < 1 mm | Chapters 7, 9 |
| 4 | Abrasive grading | At least three grades: coarse grit/fine grit/fine powder; grading qualifies if finger-rubbing shows no obvious particle-size overlap | Chapter 9 |
| 5 | Stone-slab capability | Able to lap three 300×300×40 mm granite/diabase lapping plates (two faces lapped together + quartz sand; the lapping-bench method of Chapter 9; cast-iron plates are an upgrade item unlocked after pig-iron casting) | Chapter 9 + Section 20.3 of this chapter |
| 6 | Tool steel | A carburized steel file can file cast iron without its own edge curling (edge intact after 10 min of continuous filing) | Chapter 19 |
| 7 | Anvil and hammer | An anvil of 5 kg or more fixed firmly; a 2 kg hand hammer with no loose handle | Chapter 18 |

---

### 20.1 Why Hand Machining Struggles to Guarantee Repeatable Precision

The single-piece limit of handwork is not low: a skilled craftsman using layout lines, a saw, and files can hold one dimension to ±0.3 mm. The problem is **repeatability**:

- Every piece needs the layout redone; errors do not accumulate, but neither do they converge;
- Hand force and angle drift from piece to piece; making 10 pieces may yield 10 different dimensions;
- "Match-fitting" (filing a pin to fit its hole) gives an excellent fit, but the parts are not interchangeable—when one breaks, the whole assembly must be reworked.

The value of a machine tool is not "more accurate than the hand"; it is: **replicating one setup across hundreds or thousands of parts.** The core thread of this chapter is therefore: first establish **datums** that can be preserved and copied (straight lines, planes, angles, threads, circles), then use the datums to constrain the tool's path, and finally let "datum + path" replace hand-feel.

**Precision magnitude route (empirical values, must be field-calibrated)**: layout/saw/file ±0.3 mm → scraping against a datum ±0.05 mm → lapping ±0.005–0.01 mm → lathe turning ±0.05–0.1 mm (depending on the machine's own grade).

Calibration method: for each process, make 10 test pieces of the same dimension, measure each with the Chapter 3 standard rods + snap gauges; maximum minus minimum is the scatter. If the scatter exceeds twice the values in the table above, the process is below standard; return to that section's criteria and re-check.

### 20.2 Straightedges, Squares, and Basic Measuring Gauges

#### 20.2.1 The Three-Edge Mutual-Check Method for Making Straightedges

Two straightedges mated together can only reveal "complementary bending"; three are needed to prove truth:

1. Take three bars of the same batch of steel (or hardwood), width 25–40 mm, thickness 5–8 mm, length 500–800 mm; first plane/file them to visually straight;
2. Mate A with B and observe the gap against the light: a uniform gap means one is concave and one convex, or both are flat—**record the gap shape and mark the high spots**;
3. Check A–C and B–C the same way. If the gap shapes of the three pairings disagree, mark the convex/concave positions and file the high spots;
4. Repeat the cycle until any two bars mated show "no light" or a gap uniform as a hair.

Why it converges: three bars cannot happen to be pairwise complementary (the gap shapes of the three combinations convex-concave, convex-concave, concave-concave must contradict one another); the contradictions are the true high spots. **The straightedge's straightness is produced by the mutual-check procedure itself**—this is the first lesson of "precision comes from method, not equipment," of the same lineage as the three-plate method in Section 20.3.

Empirical scale for judging gaps against the light (◎ watch the light; requires practice): no visible gap ≈ 0.005 mm class; a faint uniform glow ≈ 0.01 mm class; clearly visible light ≈ 0.05 mm class or worse. Misjudgment compensation: for any doubtful section, apply marking compound, mate and slide apart, and inspect the dye-spot distribution.

#### 20.2.2 Squares and the "Flip-Over Cross-Check"

1. On a scraped-flat surface plate (the output of Section 20.3), construct a perpendicular by the equal-radius arc method: define segment AB; with A and B as centers and the same radius greater than AB/2, swing arcs; the line through the two intersection points is the perpendicular bisector;
2. Independently verify once with the 3-4-5 rope (verification item 2); continue only when the two methods agree;
3. After making a square, perform the **flip-over self-check**: hold the square against a fixed straightedge and draw a line along the square's other edge; flip the square 180° and draw a second line. The distance between the two lines = 2× the squareness error. Scrape the square's datum edge to center, repeat until the two lines coincide (spacing < 0.1 mm).

Cross-checking two squares against each other: place them back to back, inspect the gap against the light; a uniform gap means both are true right angles or complementary—then compare each with its flip-over result to assign the fault.

#### 20.2.3 Snap Gauges (First-Generation Gauges)

Using the checking straightedge and a scriber, reproduce on steel plate/hardwood a set of snap gauges that "fix dimensions by notch" (one step per 1 mm, or as needed). Dimensional consistency is verified against the standard rods. **A snap gauge has only two readings, "go/no-go," and no numeric value**—this is exactly its value: it does not depend on reading skill and cannot be misread.

At this point you have: checking straightedges ×3, squares ×2, one set of snap gauges. Stamp all with numbers and register them in the ledger (the Chapter 4 records system).

### 20.3 Establishing and Reproducing the Flatness Datum: Three-Plate Mutual Lapping

**Figure 20-1 Three-plate mutual lapping rotation (schematic)**

```
        A ←→ B        Round 1: lap A-B, scrape the spots
          ╲  ╱
           ╳
          ╱  ╲
        A ←→ C        Round 2: lap A-C, scrape the spots
          ╲  ╱
           ╳
          ╱  ╲
        B ←→ C        Round 3: lap B-C, scrape the spots
          (cycle until all three pairs match in point count)

  A(convex)─lap→B,C(concave) → B,C mutual lapping exposes high spots → high spots scraped off → convergence to a plane
```


The flat plane is the mother datum of all machinery (guideways, beds, and gauge blocks all derive from planes). **Two plates lapped against each other forever yield only "complementary curved surfaces"** (one convex, one concave, perfectly mated, each believing itself flat); a third plate is required to break the symmetry.

Why it converges: if A is convex, B and C are scraped by it toward concave; when B and C are then lapped together, two concave faces cannot mate fully, high spots are exposed and scraped away—the bending errors cancel one another through the rotation, and the limit is a plane. **Nothing exists that is flatter than the plates; the plates' flatness is produced by the mutual-lapping procedure itself.**

Requirements for the plates themselves (to prevent "procedure right, plates wrong"):
- Three plates, same size and grade (e.g., 300×300, 400×400 mm), thickness ≥ side/12 (empirical: a 300 plate ≥ 25 mm thick);
- Cast stiffening ribs on the back; first file/mill obvious warpage off the working face (check diagonal warpage with a straightedge; just remove the big bumps, do not chase perfection);
- Castings must first be **naturally aged**: leave outdoors 1–3 months to release casting stresses (in a hurry: heat to 100–150 ℃, hold one day, then cool slowly—effect reduced; empirical value). A plate whose aging is skipped warps by itself within weeks of scraping—this is the most common "finished yet failed."

**Homemade marking compound**: pine-soot charcoal black (pine smoke ash sifted fine) or red iron powder (hematite ground and water-sifted fine), mixed with cooked vegetable oil or animal fat into a thin paste. Application: dab with a finger or cloth and **rub until no accumulation is visible, only a uniform thin film**. Too thick a film = false spots (see the failure-mode table). Red lead (if the lead-smelting line is up) spots best, but the lead-toxicity limits of Chapter 49 apply—this route defaults to not using it.

**Contact-point density criterion (points inside a 25 mm×25 mm box)**:

| Stage | Points | Use |
|---|---|---|
| Rough scraping done | 4–6 points | Not yet a datum; removes only macro unevenness |
| Fine scraping done | 8–12 points | First-grade datum: lathe guideways, scraping inspection |
| Precision scraping done | 20–25 points | Precision datum: gauge-block working faces, precision guideways |

Points must be uniformly distributed (the box must pass anywhere on the plate); the outer 10 mm is exempt. All three plates, in **any pairwise** combination, must meet the criterion—stopping after testing only one or two pairs is a false pass.

[Card 20-01 Three-Plate Mutual Lapping] (eight fields)

1. **Input materials**: aged cast-iron plates ×3 (same grade and size, thickness ≥ side/12, a 300 plate ≥25 mm; stiffening ribs cast on the back; castings aged outdoors 1–3 months, or 100–150 ℃ × 1 day then a slow cool in a hurry, effect reduced); marking compound (pine-soot black or red iron powder mixed with cooked oil / animal fat); cleaning cloths (oily cloths kept separate, never mixed with plate-wiping cloths).
2. **Tools required**: rough / fine scrapers (Chapter 19 carburized steel, hardened; edge checked straight with a straightedge; negative rake 15–25°); 25×25 mm point-count box (bent wire, clear inside 25 mm square); checking straightedges ×3; a carrying pole for two-person plate moves.
3. **Sequence and control points**: ① degrease and clean the faces → ② thin marking film (rubbed until no accumulation shows, only a uniform film) → ③ lap two plates: stroke 1/3–1/2 of plate length, figure-eight alternating with straight strokes, uniform pressure, 5–8 passes per lapping → ④ separate and read: bright spots = high areas, dark zones = low → ⑤ scrape the high spots (only the bright centers; strokes crossed 45°–60° to the previous round) → ⑥ rotate the pairings A-B → A-C → B-C → A-B…, **every round must cover all three pairs** → ⑦ every 3–4 rounds count points with the box and record. Control point: testing only one or two pairs and stopping is a false pass.
4. **Empirical parameters and calibration**: point density (inside a 25×25 mm box) rough 4–6 / fine 8–12 / precision 20–25, the outer 10 mm exempt; lapping 5–8 passes; scraping depth 0.005–0.01 mm per stroke. **All empirical values, to be calibrated to local conditions.** Calibration: spots elongated into lines = over-lapped, reduce the pass count; the film is judged by mating two flat glass plates (uniform film color, not blotches); chips must come off as curled flakes, not crumbly dust.
5. **Observations to record**: per round — the point count of each of the three pairings, a spot-distribution sketch (where the convex zones are), the number of scraper regrinds, the film-thickness judgment, and the start / end positions used that round (to catch pausing at one spot).
6. **Pass / rework / scrap criteria**: pass = all three pairings at the target point count with uniform distribution (the box passes anywhere on the plate); rework = count met but concentrated in one corner → extra-scrape that corner 2–3 rounds (never the whole plate); scrap = the plate cracked, or overall warpage >0.5 mm from insufficient aging (re-age and re-scrape — the plate is not lost, the labor is).
7. **Common failures and diagnosis order**: (1) counts swinging up and down → film too thick (most common; check the film first); (2) a rim that never takes points → strokes always start and stop at the same position; change them; (3) two pairs good, one poor → the third plate lacks stiffness or sits on uneven support (switch the feet to three-point support: three points define a plane, four always rock); (4) spots "growing into lines" → monotonous lapping path; switch to figure-eight; (5) counts never converging → the film first, then the aging, then whether a pairing was missed in the rotation.
8. **L1 / L2 / L3 evidence**: L1 = any one pairing at 4–6 points with a rubbing kept; L2 = all three pairs at 8–12 points with three rubbings plus the point-count record sheet; L3 = the semiannual mutual-check regime in operation (all three pairs retested without loss of points) with every historical record kept.

Labor (empirical values, must be field-calibrated): rough filing 2 people × 4 days; scraping to 8–12 points 2 people × 12–18 days; to 20–25 points add another 10–15 days. **This is one of the most labor-dense operations in the whole book; do not compress it**—the legitimacy of all later precision grows from here.

The three plates are made together and stored together (stood on edge, not stacked, away from stove heat), mutually checked every six months. Taking any single plate away for "dedicated shim duty" is a violation—dedication makes it wear unevenly and ruins the whole datum set.

### 20.4 Scraping, Lapping, and the Formation of Fitted Surfaces

#### 20.4.1 Scrapers and Scraping Technique

Scraper: forged from Chapter 19 carburized steel, quenched and tempered (temper to pale yellow; hardness takes priority); flat blade 10–20 mm wide, edge honed on a fine oilstone (Chapter 9) until a straightedge check shows no gap.

Operation (◎ hand-feel; must be practiced):
- Push scraping: brace the scraper handle against thigh/hip, both hands press the blade, **negative rake about 15–25°** (the edge "shovels" off the plate surface rather than "planing" it), one stroke 30–60 mm, wrist flicks the cut off—chips should fly out as curled flakes;
- Each time **scrape only the bright center of the marked spot**, one stroke per spot, with the scratch direction crossed about 45–60° from the previous round;
- Practice method: 500–1000 strokes on scrap cast iron; the standard is curled chips of consistent depth (compare with a depth template or by feel); misjudgment compensation: after each spotting round, count and record points; if the count drops instead of rising after scraping, the blade is digging too deep or the strokes are not crossed;
- Flaking (regular half-moon pattern): used in the final scraping stage; first, it stores oil; second, it forces uniform crossing of the tool path; third, when the plate wears, the pattern disappears, signaling re-scraping—**the pattern is the plate's wear indicator**.

[Card 20-03 Scraping and Point-Count Acceptance] (eight fields)

1. **Input materials**: plate or guideway face already rough-filed to remove gross unevenness (check diagonal warpage with a straightedge; take off the big bumps, do not chase perfection); marking compound (thin film, rubbed to an even layer); scrap cast iron for practice.
2. **Tools required**: scraper (forged from Chapter 19 carburized steel, quenched and tempered — **temper to pale yellow, hardness takes priority** — flat blade 10–20 mm wide, honed on a fine oilstone until a straightedge shows no gap), depth template (or comparison by feel), 25×25 mm point-count box, checking straightedge, rubbing paper.
3. **Sequence and control points**: ① thin marking film → ② lap to pick up spots (the Section 20.3 stroke and rotation rules) → ③ push scraping: handle braced against thigh / hip, both hands pressing, **negative rake 15–25° (the edge shovels the surface rather than planing it)**, one stroke 30–60 mm, wrist flicks the cut off → ④ **scrape only the bright center of each spot, one stroke per spot, strokes crossed 45°–60° to the previous round** → ⑤ every 3–4 rounds count points with the box and record → ⑥ add flaking at the finish (regular half-moon pattern, which doubles as the wear indicator). Control point: if the count drops instead of rising after a round, stop, regrind the blade and scrape shallower — the blade is digging in or the strokes are not crossed.
4. **Empirical parameters and calibration**: depth per stroke 0.005–0.01 mm; negative rake 15–25°; stroke 30–60 mm; point density rough 4–6 / fine 8–12 / precision 20–25 per 25×25 mm, outer 10 mm exempt; 500–1000 practice strokes on scrap cast iron. **All empirical values, to be calibrated to local conditions.** Calibration: curled flake chips of consistent depth pass; crumbly dust means digging in — regrind the blade and go shallower.
5. **Observations to record**: per round — point count / spot-distribution sketch / chip form (curled flake or crumbly dust) / angle between this round's strokes and the last / number of scraper regrinds / whether flaking was applied.
6. **Pass / rework / scrap criteria**: pass = target point count reached with uniform distribution + curled flake chips + a regular flake pattern; rework = the count dropping or the distribution skewed to one area (scrape shallower, force crossing; extra-scrape that area 2–3 rounds); scrap = a chipped edge scoring the datum face, or the face gouged into deep pits (re-file and re-scrape that face; the labor is re-counted).
7. **Common failures and diagnosis order**: (1) the count drops after scraping → digging in (negative rake too large) or strokes not crossed; fix the blade first, then go shallower; (2) points always in the same corner → the start / end positions are fixed; change them and extra-scrape that corner; (3) counts swinging → marking film too thick (false spots); reduce the film and re-apply; (4) the edge does not last → the temper color went past pale yellow; requench and re-temper per Section 19.3.3.
8. **L1 / L2 / L3 evidence**: L1 = 4–6 points scraped on scrap cast iron with curled chips; L2 = one working face at 8–12 points with uniform distribution, point-count records and a rubbing kept; L3 = two people reading the same face's point count in agreement, with a continuous scraper-regrind record and the card reproducible by a second person.

#### 20.4.2 Lapping

Abrasive (Chapter 9: sand → fine sand → iron-oxide fine slurry) + oil (fat/vegetable oil) applied to the lap, and the workpiece lapped against it. Lapping reaches ±0.005 mm class and mirror finish (empirical values, must be field-calibrated: the lapped face mated to the surface plate shows spots in continuous patches).

**Abrasive grades must never be mixed**: store different grits in separate containers, graded by water-sieving (settling-time fractions; see Chapter 9). Carrying the previous stage's coarse scratches into the next stage is the number-one cause of "lapping that makes it worse."

For flat work, one of the three plates serves directly as the lap (keep an account of how often each serves as a lap so wear is shared); for round holes, use a cast-iron lapping mandrel (turned on the lathe, with grooves for forward and reverse rotation).

#### 20.4.3 Fitted Surfaces

The sliding fit of shaft in hole relies not on "accurate dimensions" but on the **contact band**—apply a thin film of marking compound, assemble and rotate, and observe whether the friction band is uniform, sits in the middle, and covers over 60% of the length. Contact at both ends, open in the middle = the hole is barrel-shaped; hard contact at one end = the hole is tilted. Fix: scrape the hole (using the lapping mandrel) or scrape the bearing bush (see Section 20.8 plain bearings).

### 20.5 Threads, Nuts, and Repeatable Fastening

The screw thread is the only source of "adjustable, lockable, replicable linear motion," and the foundation of the later micrometer and lead screw. The handcraft route before there is a lathe (the first generation chooses **coarse pitch**: around 3 mm pitch—larger is easy to make, smaller is hard by hand):

1. **Make the cylinder round first**: rotate the blank in a V-block, measure in many directions with straightedge and snap gauges, file round until diameter difference < 0.2 mm (the snap gauge passes in all four orientations 0°/90°/180°/270°);
2. **Scribe the helix**: a right-triangle paper/leather template, base = cylinder circumference (π×diameter—measure the circumference by the Chapter 3 method rather than computing—wrap paper around once and the fit gives it), height = pitch. The hypotenuse is one turn of the helix. Wrap the template tightly around the cylinder and scribe along the hypotenuse;
3. **File the thread**: with a three-square (triangular) file (Chapter 19), file V-grooves along the line, shallow first then deeper; after every 3–4 file passes, test-thread once against the template nut;
4. **Template nut (the trick of two tools that measure each other)**: take a thicker steel block and drill a hole (hole diameter = screw minor diameter, i.e., major diameter − 2×thread depth; thread depth ≈ pitch×0.55, empirical value), saw a slot to make an "adjustable nut," and screw it onto the screw—nut thread and screw thread **grind each other in**: wherever it binds, fix there; after a few rounds a matched pair of screw and nut with "identical thread profiles" is born. Both are stamped with the same number;
5. **Use as pairs**: in the hand-thread stage there is no "interchangeability"; each screw-nut pair is numbered as a pair. Interchangeability waits for Chapter 22.

Inspection: threads in over the full length with no local binding; hold the nut and rock it axially, movement < 0.3 mm (empirical value; feeler gauge, or feel + dial-indicator class). Excess wobble = uneven thread depth; return to the template nut for more mutual lapping.

[Card 20-02 Hand Threading by the Template-Nut Method] (eight fields)

1. **Input materials**: steel rod of roundness <0.2 mm (snap gauge passes at 0°/90°/180°/270°); steel block of thickness ≥4×pitch for the template nut; first generation uses a coarse pitch around 3 mm; scribing template (paper / leather, base = measured circumference, height = pitch).
2. **Tools required**: V-block, snap gauges, center punch, three-square file (edge angle matched to the 60° thread form), saw (to slot the nut), fine file and oilstone, number stamps for pairing, feeler gauges (or feel plus dial-indicator class).
3. **Sequence and control points**: ① make the cylinder round first (rotate it in the V-block, measure in several directions with straightedge and snap gauges, diameter difference <0.2 mm) → ② scribe the helix (template wrapped tight, scribe along the hypotenuse) → ③ file the V-groove, **shallow first then deeper**, test-threading against the template nut every 3–4 file passes → ④ drill the template nut (hole = minor diameter = major diameter − 2×thread depth), saw a slot, screw it on and let nut and screw grind each other in — fix wherever it binds → ⑤ stamp screw and nut with the same number and use them as a pair (no interchangeability at this stage). Control point: thread-depth increment ≤0.2 mm per round, one test-thread per round.
4. **Empirical parameters and calibration**: thread depth ≈0.55×pitch; minor-diameter hole = major diameter − 1.1×pitch; crest flat 0.1×pitch (a sharp crest chips); roundness difference <0.2 mm; axial wobble <0.3 mm. **All empirical values, to be calibrated to local conditions.** Calibration: make one scrap test pair first, measure the actual wobble, correct the hole diameter, and transcribe this batch's value into the card.
5. **Observations to record**: rod diameter in four orientations / measured circumference / pitch / depth increment per round / where the binding sits when test-threading (one spot = roundness; tight all round = depth insufficient; loose all round = depth too great) / full-length engagement / axial wobble reading / pair number.
6. **Pass / rework / scrap criteria**: pass = full-length engagement with no local binding + axial wobble <0.3 mm; rework = local binding (correct that spot's flanks and test again); scrap = excessive depth giving wobble >0.6 mm (demote to the next coarser pitch; no forcing a repair).
7. **Common failures and diagnosis order**: (1) the thread "wanders" → the template was not wrapped tight; re-scribe the helix; (2) full-length binding at one fixed spot → poor roundness there or a crooked helix; mark it, unscrew, measure the diameter and correct locally with a file; (3) a thin, pointy profile that chips at the crest → filed too sharp; leave a crest flat of 0.1×pitch; (4) wobble over the limit → uneven thread depth; back to the template nut for more mutual lapping.
8. **L1 / L2 / L3 evidence**: L1 = one pair engaging through; L2 = three independently made pairs all passing plus wobble records; L3 = the template nut's own regrind regime in operation (rework at 0.1 mm wear).

Labor (empirical values): one M12×3 screw (150 mm long), skilled worker 1.5–2 days including quenching.

### 20.6 Hand Drilling, Boring, and Cylindrical Machining

**Drilling upgrade**: Chapter 7 bow drill + Chapter 9 abrasive grinding → now: hardened steel drill bits (Chapter 19; flat-spade/three-point forms), with wooden or iron **drill jigs** (with guide holes) guaranteeing position and perpendicularity; hole perpendicularity checked by standing a square against it. Jig guide holes wear and enlarge—drill jigs are consumables; stamp them with numbers and log their life.

**Boring—the origin of round** (the direct precursor of the Chapter 28 cylinders): change "tool rotates" to "**boring bar rotates, workpiece fixed, tool fed radially**":

1. Cast the workpiece with a pre-formed hole (Chapter 17, clay core, leaving 3–5 mm boring allowance);
2. **Make the boring bar as thick as possible** (diameter ≥ 0.5–0.7 of the hole diameter; empirical: thick = rigid = no tool deflection);
3. Support both ends of the bar in stands with bearing seats (bearing bores scrape-fitted; clearance set so "rotation is smooth and radial wobble is just perceptible," about 0.05 mm—empirical, must be calibrated);
4. Clamp the workpiece fixed (clamping force must keep the workpiece from shifting without distorting it—clamping distortion of thin-walled pieces is a common cause of out-of-round holes);
5. Rotate the bar (hand crank, or bowstring reciprocation + ratchet for one-way drive); radial feed of the tool is fine-adjusted by a wedge on the tool post, 0.1–0.3 mm per pass (empirical value); [Process Card 20-04 summary] Input: casting with pre-formed hole (allowance 3–5 mm); Tools: boring bar + twin-support stands + wedge-feed tool + inside calipers and outside-diameter standard rods (comparison measurement); Control points: **both end supports tightened in sync**, measure the bore once per pass (measure the hole with inside calipers, then open them onto the outside-diameter standard rod for comparison reading—the inside-measured, outside-compared transfer method); Parameters: speed set so chips flow continuously without clogging (◎ listen: a uniform hiss = normal; a sharp squeal = dull tool; a muffled roar = feed too large); Criteria: three-point method (0°/120°/240°) bore difference ≤ 0.1 mm and end-to-end bore difference ≤ 0.15 mm/300 mm; Troubleshooting: bellmouth at the hole entrance = cantilevered bar deflecting (add support/reduce feed); tilted hole axis = loose clamping or supports; chatter marks on the surface = bearing clearance too large or tool overhang too long. Evidence: L1 through hole meets the taper requirement; L2 three pieces consecutively meet standard; L3 boring-bar bearing scraping and wedge calibration records on file.

[Card 20-04 Boring-Bar Hole Boring] (eight fields)

1. **Input materials**: casting with a pre-formed hole (clay core, boring allowance 3–5 mm); packing blocks or wedges to keep thin walls from clamping distortion; marking compound (for scrape-fitting the bearing seats).
2. **Tools required**: boring bar (diameter ≥0.5–0.7×hole diameter), twin-support stands (bearing bores scrape-fitted), wedge-feed tool holder, inside calipers + outside-diameter standard rods (comparison measurement), hand crank or bowstring + ratchet, square.
3. **Sequence and control points**: ① cast the hole with 3–5 mm allowance → ② make the bar as thick as possible and support both ends in stands with bearing seats, **both end supports tightened in sync** → ③ clamp the workpiece so it neither shifts nor distorts → ④ rotate the bar (crank, or bowstring reciprocation + ratchet for one-way drive), fine-adjust the radial feed with the wedge, 0.1–0.3 mm per pass → ⑤ **measure the bore once per pass** (inside calipers into the hole, then opened onto the outside-diameter standard rod for the comparison reading — the inside-measured, outside-compared transfer method) → ⑥ re-measure by the three-point method (0°/120°/240°), including the end-to-end difference. Control points: synchronized supports and per-pass measurement; miss either and the out-of-round can no longer be recovered.
4. **Empirical parameters and calibration**: bar diameter ≥0.5–0.7×hole diameter; feed 0.1–0.3 mm per pass; bearing clearance about 0.05 mm ("rotation smooth, radial wobble just perceptible"); criteria bore difference ≤0.1 mm and end-to-end difference ≤0.15 mm/300 mm. **All empirical values, to be calibrated to local conditions.** Calibration: set the speed so chips flow continuously without clogging (◎ listen — a uniform hiss = normal, a sharp squeal = dull tool, a muffled roar = feed too large).
5. **Observations to record**: three-point bore readings per pass / end-to-end bore difference / chip form and sound / the order in which the supports were tightened / any workpiece shift / where chatter marks appear.
6. **Pass / rework / scrap criteria**: pass = three-point bore difference ≤0.1 mm, end-to-end ≤0.15 mm/300 mm, and the through hole meeting the taper requirement; rework = local chatter or slight taper (reduce feed, re-scrape the bearing clearance, take one more pass); scrap = the bore wall gouged, or the axis so far off that no allowance remains.
7. **Common failures and diagnosis order**: (1) bellmouth at the hole entrance → the bar deflects as a cantilever (add support, reduce feed); (2) tilted hole axis → loose clamping or loose supports; (3) chatter marks on the surface → bearing clearance too large or the tool overhanging too far; (4) bore large at both ends and small in the middle → cantilever deflection; add a centre support and cut the feed.
8. **L1 / L2 / L3 evidence**: L1 = one through hole meeting the taper requirement, on file; L2 = three consecutive pieces meeting standard with complete three-point readings; L3 = boring-bar bearing scraping and wedge calibration records on file, with a second person reproducing the same taper from this card.

**The error-budget idea (the single most important table in this chapter)**: every machine imposes a different roundness requirement on its holes; do the accounting first, then decide the machining grade—

| Use | Allowed roundness/taper | Machining means |
|---|---|---|
| Newcomen atmospheric engine cylinder (Chapter 28) | ±0.5–1 mm (leather packing seal absorbs error) | Cast hole + rough boring is enough |
| Ordinary plain bearing housing | ±0.1 mm | Scraping + boring |
| Watt-style steam engine cylinder (Chapter 28 upgrade) | ±0.1–0.2 mm | Fine boring + honing (Chapter 28 honing bar) |
| Machine-tool spindle bearings | ±0.02–0.05 mm | Scraping + lapping |

**Spend precision where it counts**: using high-precision means on low-requirement parts wastes labor; using low-precision means on high-requirement parts plants a landmine. The very existence of this table is the operational form of "precision must have a source."

### 20.7 Working Principles and Early Structures of Simple Lathes

A three-generation evolution, each generation constrained by the datums of the last:

**Generation 1: spring-pole lathe (wood)**—Chapter 7 woodworking capability suffices:
- Workpiece held between two centers (center holes punched for location, 1–2 mm deep, 60° conical); foot treadle + cord wrapped 2–3 turns around the workpiece drives reciprocating rotation; the spring pole (a flexible wooden pole, suspended overhead) provides the return stroke;
- The hand-held turning tool rests against a **wooden tool rest** (a fixed baffle). The rest is the key: a hand in mid-air has no datum; against the baffle it does;
- For wood and soft-copper work. Roundness depends on the two centers being coaxial: align tip-to-tip with a straightedge + stretched line (the line touches both center tips; if it is not bent out of line they are coaxial—precision about the 0.2 mm class, empirical value);
- Acceptance: turn a 300 mm round wooden rod; three-point-method roundness ≤ 0.5 mm.

**Generation 2: treadle crank + flywheel lathe**—crank mechanism (detailed in Chapter 21) + a large flywheel for energy storage (wooden wheel 0.8–1.2 m in diameter, rim fitted with an iron band for added inertia), converting reciprocation into one-way continuous rotation; a cast-iron tool rest can clamp the tool fixed, leaving the hand only the feed. Can turn iron work (small depth of cut 0.2–0.5 mm, many passes).
- Acceptance: turn a φ30 iron test bar; roundness ≤ 0.2 mm, taper ≤ 0.3 mm/300 mm.

**Generation 3: the metal lathe**—this chapter's destination:
- Cast-iron bed (Chapter 17 casting; first aged 1–3 months), guideway surfaces corrected by three-plate mutual lapping + scraping to 8–12 points;
- The saddle moves along the guideways; **clearance adjusted with gibs (tapered strips)**: gib taper 1:20–1:50 (empirical value), adjusted until "the saddle slides smoothly through its full travel when hand-pushed, yet cannot be rocked fore-aft"; gibs are consumable parts, micro-adjust them periodically;
- **Lead screw drives the saddle**: the lead screw is an extended version of the Section 20.5 screw. The first long lead screw is still hand-finished (checked tooth by tooth against a pitch template, high spots filed off), and thereafter serves as the **master lead screw** from which better lead screws are copied—when turning, the tool advances one pitch per workpiece revolution, so the master screw's errors are "averaged" into every new thread (the errors do not vanish but are diluted, and can be recorded and compensated—see Section 20.9);
- Two centers + driving plate (a lathe dog carries the workpiece); tailstock quill with screw micro-feed;
- Capability at this point: turning outside diameters, facing, grooving, thread cutting (relying on the master lead screw + change gears).

Acceptance (each generation on its own): turn a test bar and measure roundness by the three-point method; after facing, check flatness with a straightedge + spotting; the diameter difference between the two ends of the test bar is the taper (if taper exceeds standard, first check tailstock offset, then the guideways).

### 20.8 Belts, Gears, Shafts, and Plain Bearings

- **Belts**: leather, or sewn rings of thick fabric (Chapter 15), with joints staggered (joints distributed at staggered positions along the belt length, not aligned on one line); tension set for 10–20 mm deflection under finger pressure (◎ hand-feel; calibration: compare press-down deflection against belt slip—draw a chalk line across pulley and belt, run 10 revolutions under load, and the offset in revolutions is the slip; >2% requires re-tensioning).
- **Step-pulley speed changing**: make 2–3-step stepped pulleys on driver and driven shafts; move the belt to change speed; speed ratio = inverse ratio of diameters. For cutting iron use low speed and high torque; for wood, high speed.
- **Gears**: the first generation uses **wooden gears** (made with Chapter 9 tools; pin teeth or wedge teeth)—low precision demands, easy to replace when broken. Iron gears use Chapter 17 casting + hand tooth finishing, tooth profiles approximated by layout (see Section 21.1), with each meshing pair spotted and its contact patch corrected (the contact patch should sit in the middle; bias toward tip or root must both be corrected). Honest positioning of first-generation gears: **transmission-ratio fluctuation of the ±5% class** (empirical value)—usable only for speed changing and counting, not for indexing (indexing: Chapter 22).
- **Plain bearings**: journals scrape-fitted (Section 20.4.3); clearance set so "the feel is smooth and radial wobble is just perceptible" (about 0.05–0.1 mm, empirical value, must be field-calibrated); bearing housings get oil grooves (X-shaped crossing grooves, opening to the unloaded side), lubricated with fat/oil; **temperature monitoring**: after 30 min of running, if the back of a hand on the bearing housing endures 3 s ≈ within 60 ℃ (◎ hand-feel; compensation: stick on a wax chip—soft but not melting ≈ 55–60 ℃). Over temperature, check three things: clearance too tight, oil groove blocked, load skewed.
- Axial location: shaft shoulder + bronze/cast-iron thrust washer, washer replaceable when worn—**designing wear parts as replaceable parts** is the first design rule on the road from "can be built" to "can be relied upon" (expanded in Chapter 39).

### 20.9 Lead Screws, Change Gears, and Pitch Compensation: The Bootstrap of the Second Generation

**The mother-machine principle (be honest about this)**: parts made by a machine tool are usually less accurate than the machine itself. Relying only on "inheritance," precision decays generation by generation. Gains in precision rely on the **transfer method**—precision is not inherited from the mother machine; it comes from the methods built into the process:

1. **Flatness**: the guideways of any generation are ultimately corrected by three-plate mutual lapping + scraping—the plates do not depend on the machine; they sit one level above it;
2. **Threads**: the pitch errors of the master lead screw are recorded tooth by tooth into an error table—pitch measuring method: measure the total length of 10 threads with a steel rule and divide by 10 (this dilutes the steel rule's 0.5 mm graduation error tenfold); the error table itself becomes a source of precision, compensated during cutting by **fine-tuning the change gears** (example: lead screw pitch 3.00 mm, a certain section measured to average 3.02 mm; when turning that section, correct the gear ratio by 3.00/3.02, i.e., 0.7%, meaning the driver gear drops one tooth size);
3. **Roundness**: spindle runout is detected by holding a scriber close and watching the gap as it turns + three-point-method turning of a test bar (upgraded to direct reading once the Chapter 22 micrometer exists); if out of tolerance, correct by scraping the bearing bore.

**Change-gear calculation** (thread cutting): workpiece pitch = lead screw pitch × driver teeth/driven teeth. Example: screw 3 mm, want 2 mm → tooth ratio 2/3 → 40 teeth/60 teeth. Prefer tooth counts from the "common set" 20/30/40/60/80 (identical module is required for meshing).

**Mismatch protection** (when thread cutting, if you withdraw mid-pass and re-enter, you must re-enter the original thread groove): if the workpiece-to-screw drive ratio makes the workpiece turn a whole number of revolutions within a whole number of screw revolutions, then engaging at any moment never mismatches; when that is not satisfied, the first-generation method is **never disengaging the split nut through the whole pass**—the tool withdraws radially and is cranked back on the return: slow, but it never mismatches. Decision rule: count the workpiece:screw revolution ratio; 2 workpiece turns per 1 screw turn (i.e., a pitch ratio that is an integer multiple of 1:2) never mismatches; 1.5:1 will mismatch—operate by "never disengage."

**Temperature discipline**: when turning a long lead screw, the workpiece heats and lengthens; after cooling the pitch shrinks. Countermeasures: separate rough and finish passes; before finish turning let the workpiece cool to hand temperature (◎); cool with saponified-oil water (Chapter 23 soap by-product) poured over it. Measure all lead screws of the same batch at the same temperature (the first hour of the morning's work).

[Card 20-05 Thread-Cutting Change Gears and Mismatch Protection] (eight fields)

1. **Input materials**: master lead screw (the first one hand-finished: checked tooth by tooth with a pitch template, high spots filed); workpiece blank to be threaded; change-gear set (common set 20/30/40/60/80, identical module); saponified-oil water (Chapter 23 soap by-product).
2. **Tools required**: lathe (third-generation metal lathe: two centres + driving dog + lead-screw-driven saddle), change gears and quadrant, steel rule (to measure 10 threads), pitch template, split nut (engagement lever), gibs (taper 1:20–1:50), error-table record sheet.
3. **Sequence and control points**: ① measure the master screw's pitch error — steel rule over 10 threads divided by 10, segment by segment into an error table (the rule's 0.5 mm graduation error is diluted tenfold) → ② calculate the gears: workpiece pitch = lead-screw pitch × driver teeth / driven teeth (example: 3 mm screw, 2 mm thread → ratio 2/3 → 40/60 teeth) → ③ fine-tune the ratio to compensate per the error table (example: a section averaging 3.02 mm when cutting 3.00 mm → correct by 3.00/3.02, i.e. 0.7%, the driver dropping one tooth size) → ④ **judge mismatch**: if the workpiece-to-screw revolution ratio is a whole-number multiple (e.g. 2 workpiece turns per 1 screw turn) engaging at any moment never mismatches; at 1.5:1 it will mismatch → **never disengage the split nut through the whole pass; withdraw radially and crank back** → ⑤ separate rough and finish passes, and let the workpiece cool to hand temperature before finishing. Control point: work out the revolution ratio before engaging; if it is not a whole-number multiple, disengaging is forbidden.
4. **Empirical parameters and calibration**: first-generation pitch 3 mm coarse; change gears from the common set 20/30/40/60/80 (identical module required to mesh); compensation taken from the measured average; lead-screw cumulative error criterion <0.15 mm/300 mm; measure a batch of lead screws at one temperature (the first hour of the morning). **All empirical values, to be calibrated to local conditions.**
5. **Observations to record**: measured 10-thread values for each segment of the master screw / the error table / the gear-tooth combination used / the actual moment of engagement / whether the split nut was ever disengaged / workpiece temperature / pitch re-measured after cutting / chatter marks.
6. **Pass / rework / scrap criteria**: pass = the cut thread matches the master screw's pitch, runs through tooth by tooth without binding, and cumulative error <0.15 mm/300 mm; rework = local mismatch (recut that section by the "never disengage" rule); scrap = mismatch over a whole section, or a screw with no compensation left (demote to short-screw duty).
7. **Common failures and diagnosis order**: (1) mismatch when thread cutting → the split nut was disengaged mid-pass (the most common cause; recut by the no-disengage rule); (2) pitch drifting section by section → measurements taken at different temperatures (re-measure at one temperature, finish-cut after cooling); (3) pitch uniformly too coarse or too fine → gear ratio miscalculated or driver and driven swapped; recompute and verify by idling; (4) taper out of limits on a long part → check tailstock offset first, then guideway wear, then workpiece thermal growth.
8. **L1 / L2 / L3 evidence**: L1 = one screw cut and running through against the master screw as a pair; L2 = three consecutive screws of matching pitch plus the error table established and filed; L3 = compensated gearing proven (cumulative error falls after the error-table correction), with the annual inspection records and error table kept continuously on file.

The second-generation machine's bill: a longer, stiffer bed, hardened guideway faces (Chapter 19; restorable by re-scraping when worn), a thread-feed gearbox with changeable gears, an independent tailstock. **No claim of modern precision**—the honest ceiling of this route is about the ±0.02–0.05 mm class (empirical value, must be field-calibrated); beyond that requires the long accumulation of the Chapter 22 gauge-block system and the Chapter 27 comparator.

### 20.10 How to Inspect the Machine Tool's Own Errors (Annual Inspection System)

| Error | Inspection method | Criterion (first generation) |
|---|---|---|
| Guideway straightness | Straightedge + spotting; or a spirit level (Chapter 3 bubble vial) in segmented relay | Spots continuous, or segmented readings with monotonic deviation < 0.05 mm/500 mm |
| Two-center coaxiality | Stretch a fine line between front and rear centers, measure deviation up/down/left/right; runout at both ends of a test bar | Deviation < 0.1 mm |
| Spindle radial runout | Scriber held close to the journal, watch the gap over one revolution (dial indicator after Chapter 22) | < 0.05 mm |
| Saddle motion parallel to spindle | Turn a long test bar and measure taper; straightedge side gap while the tool rest moves longitudinally | Taper < 0.2 mm/300 mm |
| Lead screw cumulative pitch error | Measure 10 threads per segment with a steel rule; record the error table | < 0.15 mm/300 mm, error table on file |
| Gib and bearing clearance | Push the saddle through its full travel by hand; rock the spindle and judge by feel | Smooth with no perceptible wobble |

Machine-tool inspection **once a year**, plus added inspections after impacts/relocation/major overhaul. Inspection records go into the archive (Chapter 4 system; Chapter 43 ledger). **Order of handling out-of-tolerance findings: first check fasteners and gibs (most common), then scrape the guideways, and only last touch the spindle bearings.**

---

## Master Parameter Table

| Parameter | Value | Class |
|---|---|---|
| Plate thickness | ≥ side/12 (300 plate ≥ 25 mm) | Empirical, must be calibrated |
| Casting aging | Outdoors 1–3 months (urgent: 100–150 ℃ × 1 day, effect reduced) | Empirical |
| Contact-point density | Rough 4–6 / fine 8–12 / precision 20–25 points per 25×25 mm | Criterion |
| Depth per scraping stroke | 0.005–0.01 mm | Empirical |
| Scraper negative rake | 15–25° | Empirical |
| First-generation hand pitch | 3 mm coarse thread | Recommended |
| Thread depth | 0.55×pitch; crest flat 0.1×pitch | Empirical |
| Boring bar diameter | ≥ 0.5–0.7×hole diameter | Empirical |
| Boring feed per pass | 0.1–0.3 mm | Empirical |
| Plain bearing clearance | 0.05–0.1 mm (wobble just perceptible) | Empirical; calibration in Section 20.8 |
| Gib taper | 1:20–1:50 | Empirical |
| Bearing temperature ceiling | ≈ 60 ℃ (back of hand 3 s / wax-chip method) | Empirical |
| Belt deflection | 10–20 mm (slip < 2%) | Empirical; calibration in Section 20.8 |
| Turned test bar acceptance | Roundness ≤ 0.1 mm, taper ≤ 0.2 mm/300 mm | L2 criterion |

## Failure Modes and Diagnosis

| Symptom | Candidate causes (by probability) | Verification | Disposition |
|---|---|---|---|
| Plate point count never converges | ① film too thick (false spots) ② insufficient aging, plate still deforming ③ the rotation missed a pairing | Re-apply an extremely thin film and re-spot; set aside a week and retest whether point counts drift; check the operation record that all three pairs were run | Reduce film and re-scrape; re-age; run the missed pair |
| Points concentrated in one corner of the plate | Lapping strokes always start/stop at the same position | Watch the lapping habit; change start/end positions | Extra-scrape that corner for several rounds |
| Two plate pairs good, one pair poor | Third plate lacks stiffness/uneven support | Flip the plate and retest; check the three-point foot support | Thicken the feet, three-point support (three points define a plane; four points always rock) |
| Point count drops after scraping | Digging in (negative rake too large) or strokes not crossed | Look at the chip form (crumbly dust = digging in) | Regrind the scraper, shallower scraping, force crossing |
| Screw binds at one fixed spot along its length | Poor roundness or helix scribed off | Mark the binding spot, unscrew, measure the diameter there | Local file correction; re-scribe the helix |
| Large thread wobble | Depth too great or profile too thin | Measure the minor diameter and compare | Scrap and move to the coarser pitch step; or match-fit the nut with a fuller thread |
| Thread mismatch during cutting | Nut disengaged mid-pass | Review the operation | Re-cut following the mismatch rule: never disengage |
| Bored hole large at both ends, small in the middle | Cantilevered bar deflection | Measure the bore by the three-point method in segments | Add intermediate support, reduce feed |
| Taper over standard on long work | ① tailstock offset ② guideways worn unevenly ③ workpiece thermal elongation | Compare by turning head-for-tail; check annual inspection records; feel for temperature | Readjust the tailstock; scrape the guideways; separate rough/finish + cooling |
| Test bar barrel-shaped | Poor workpiece rigidity, deflection (slender shaft) | Mid-length diameter vs. both ends | Add a follow rest/steady rest, reduce depth of cut |
| Lead screw pitch drift | Measurements taken at inconsistent temperatures | Retest at the same temperature | Fix measurement to early morning, finish-turn only after cooling |
| Bearing overheats beyond 60 ℃ | ① clearance too tight ② oil groove blocked ③ load skewed | Check in that order | Scrape to enlarge clearance, clear the groove, realign |

## Process Card Index

## Acceptance Criteria

- **L1 proof-of-principle**: three-plate mutual lapping complete, any two plates ≥ 4 points per 25×25 mm (rubbings on file); hand-made screw and nut engage over the full length with no binding; spring-pole lathe turns a wooden rod to roundness ≤ 0.5 mm. Evidence: rubbings, test pieces, record sheets.
- **L2 repeatable manufacture**: all three plate pairs at 8–12 points; the third-generation metal lathe turns test bars to roundness ≤ 0.1 mm, taper ≤ 0.2 mm/300 mm; cut thread pitch matches the master lead screw (paired inspection + error table established). Evidence: measurement records for 3 consecutive test bars, the lead screw error table.
- **L3 sustainable production**: bed guideway annual-inspection system running (records on file); wear parts such as scrapers, files, lead screws, and gibs can be self-repaired or rebuilt on the machine itself (mother-machine closed loop); parts from the same drawing scatter ≤ 0.3 mm within a batch (transition toward Chapter 22 interchangeability). Evidence: annual inspection records, spare-part rebuilding records, batch scatter statistics.

## Labor, Manpower, and Consumption

| Item | Manpower | Labor hours (empirical values) |
|---|---|---|
| One set of three plates (to 8–12 points) | 2 people | Forging/casting 3 days + rough filing 4 days + scraping 12–18 days |
| One hand-made screw-nut pair (M12×3, 150 mm) | 1 skilled worker | 1.5–2 days (including quenching) |
| Generation 1 spring-pole lathe | 2 people | 5–7 days |
| Generation 2 treadle flywheel lathe | 3 people | 15–20 days |
| Generation 3 metal lathe (including the bed aging wait) | 4–6 people | Net labor 60–90 days (aging wait 1–3 months extra) |
| Abrasive/marking compound consumption | — | Per scraping day: abrasive 50–100 g, grease/oil 20 g (enter into the Chapter 38 account book) |

## Safety Boundaries

- **Rotating machinery**: loose clothing and loose long hair are strictly forbidden near rotating parts; never start the machine with the workpiece clamping insecure; never step over a running belt or straighten it by hand; clear iron chips only after stopping (use a hook, not hands).
- **Scraping**: sheath scrapers when not in use; carry plates two-person with carrying poles; guard against tipping when plates stand on edge (a 300 plate is the 20 kg class; a crushed foot can maim).
- **File filings and grinding dust**: filings in the eye are this chapter's most frequent injury; position yourself out of the chip-ejection direction and wear mesh protection if needed; quartz dust from dry grinding carries a chronic lung-damage risk (silicosis); prefer wet grinding; the protection regime is in Chapter 49.
- **Lathe**: long stock protruding from the spindle must have a steady rest or stock support, or it will whip and injure; remove the chuck key immediately after use—starting the machine with the key left in the chuck is a classic cause of arm-loss accidents.
- **Heat-treated parts**: never judge the temperature of a quenching part by eye when retrieving it from the fire (dark red ≈ 500–600 ℃ still burns); always use tongs.

## A. Existing Tool Inventory (partial)

| Tool | Source |
|---|---|
| Standard rods, equal-arm balance, 3-4-5 rope | Chapter 3 |
| Bow drill, woodworking tools, workbench clamping | Chapters 7, 9 |
| Graded abrasives | Chapter 9 |
| High-temperature furnace, bellows, refractory clay | Chapter 12 |
| Sand molds, crucibles | Chapter 17 |
| Anvil, iron hammer, forge welding | Chapter 18 |
| Carburized steel, quench/temper, chisels/saws/three-square files | Chapter 19 |

## B. New Tools Added in This Chapter

Three checking straightedges; squares ×2 (with the flip-over cross-check method); snap-gauge set; **the three-plate datum set**; scraper set with marking compound and point-count checking box; lapping mandrel; template nut and matched screw; drill jigs; boring bar with twin-support boring stands; the generation-1 spring-pole lathe; the generation-2 treadle flywheel lathe; **the generation-3 metal lathe (bed + saddle + lead screw + two centers + gibs)**; the step-pulley belt system; the change-gear set (common gear set); the machine-tool error annual-inspection procedure and the lead-screw error table system.

## C. Unsolved Dependencies

- Rolling bearings (need higher hardness and grinding capability; plain bearings used for now);
- Ground finishing of hardened guideways (lapping can partially substitute);
- Milling machines and boring machines (lathe + drill jig + boring stands can temporarily substitute);
- Interchangeable threads and gauge blocks (solved in Chapter 22);
- Direct-reading dial indicators (inspection upgraded after Chapter 22).

## Next-Step Dependencies

- Chapter 21: shafting, gears, water wheels, and power distribution use this chapter's lathe and scraped surfaces directly;
- Chapter 22: the lead screw is the micrometer's parent; the three plates are the gauge blocks' grandparent;
- Chapter 28: the steam engine cylinder depends on the Section 20.6 boring route (the Wilkinson boring-machine idea) and the error-budget table;
- Chapter 31: generator rotors, bearings, and slip rings all depend on this chapter;
- Chapters 34–35: the wafer slicing machine's spindle is a distant descendant of this chapter's spindle;
- Chapters 37–39: this chapter's labor-hour and consumption quotas enter the labor scheduling and maintenance cycle tables.
