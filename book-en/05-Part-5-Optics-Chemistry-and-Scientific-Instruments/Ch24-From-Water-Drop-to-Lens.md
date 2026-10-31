## Chapter Objectives

- Verify that light travels in straight lines with a pinhole camera, establishing an imaging and observation method that depends on no lens at all.
- Establish the imaging rules for convex and concave lenses (object distance—image distance—focal length), and be able to measure the focal length of any lens on the spot.
- Establish blank-selection criteria for optical work: screen the Chapter 14 glass against four hard criteria to find blanks that can be ground into lenses.
- Establish the abrasive settling-classification system and the rough grinding—fine grinding—polishing three-stage process, including making the pitch lap.
- Master the curvature-to-focal-length conversion (curvature measured by the sagitta method), and be able to work backward from a target focal length to grinding parameters.
- Establish two image-quality inspections, the star-point method and the grid plate, with every lens inspected piece by piece before release.
- Produce magnifiers (3–5x), single-lens telescopes (10–30x), and glass-bead microscopes (within the magnification lower bound).
- Define the quantitative limits of single-lens optics: exactly what level chromatic aberration, homogeneity, and surface-figure accuracy each cap image quality at.


## Pre-Work Verification (key-point form)

| 1 | Glass blanks | T-3 grade or better sample pieces, ≥3 pieces |
| 2 | Abrasives | Three-grade settling-classified sand on the books (Section 24.4) |

## Capability Boundaries

**Achievable**: pinhole camera and measured solar angular diameter; focal length measured by three methods with mutual cross-checks; abrasive settling classification; lens grinding with the dual star-point/grid inspection; magnifiers at L2 mass production, Galilean telescope at L2, single-bead microscope at L1–L2.
**Explicitly not achievable**: compound microscope objectives, achromatic cemented doublets (Wall One/Wall Three, see Section 24.8); surface-figure inspection at light-wavelength level (no interferometry/knife-edge method); measured refractive index n (approximated as 1.5, error folded into the tolerance).
**External dependencies**: T-4 grade glass blanks (Chapter 14 pass rate about two in ten); bitumen/rosin polishing media.

## Minimum Preconditions

| Item | Requirement | Source |
|---|---|---|
| Glass blanks | Vessel-grade glass plate/rod, including T-3-or-better sample pieces | Chapter 14, Sections 14.6 and 14.7 |
| Annealing | Ash-pit annealing regime in operation | Chapter 14, Section 14.3 |
| Lapping foundation | Scraping, lapping, flat reference, three-way mutual checking | Chapter 20, Sections 20.3 and 20.4 |
| Measurement | Marking straightedge, scriber, angle plate, balance | Chapter 3 |
| Metal tools | Hardened steel bars, chisels, files, drills | Chapter 19 |
| Birefringent crystal | Iceland spar (if registered), for stress checking | Chapter 8, Section 8.3 |
| Workspace | Ventilated grinding room, dark corner (for inspection) | Chapter 13 |
| Bitumen or rosin | Natural bitumen/pine resin/beeswax, polishing media | Chapter 2 resource survey, Chapter 8 |

---

### 24.1 Pinhole Imaging and the Propagation of Light

**An imaging device that predates every lens**: pierce a small hole in the opaque wall of a box, and an inverted image of the outside scene appears on the opposite inner wall. This step needs no glass at all, yet it is the foundation of all geometric optics — it proves that light travels in straight lines, with image and object point-symmetric about the hole.

**Construction (half a day)**:

1. Box: nail wooden boards into a sealed box about 0.5 rod per side (Chapter 13 carpentry); coat the inner walls with black soot from pot bottoms (Chapter 6).
2. Hole: punch a hole about 1 mm in diameter through a thin metal sheet (wrought-iron sheet) (empirical value, must be field-calibrated: test apertures across 0.5–2 mm); nail the sheet over an opening in the box wall — the hole rim must be thin, for a thick-walled hole clips obliquely arriving light the way a pipe does.
3. Screen: paste white paper or brush white clay slip on the inside of the opposite wall.
4. Light shielding: fit a cloth curtain over the box; the observer slides head and shoulders in to view.

**The physical trade-off of aperture (you only understand it after doing it once by hand)**:

| Aperture | Image sharpness | Image brightness | Reason |
|---|---|---|---|
| Too small (<0.3 mm) | Blurry | Extremely dim | Light diffracts and spreads at the hole rim (record the phenomenon; the mechanism is filled in later) |
| Moderate (about 1 mm at a box depth of 0.5 rod) | Sharpest | Dim | Each object point corresponds to roughly one beam of straight-traveling light |
| Too large (>5 mm) | Ghost images blur into a blob | Bright | Each object point becomes a spot; spot diameter = aperture |

Remember one criterion: **the spot diameter in the image is never smaller than the aperture** — the bigger the hole, the brighter and blurrier; the smaller, the dimmer and sharper. Optimal aperture varies with box depth; determine it by experiment and file it in the archive (one record per box).

**Four direct uses of the pinhole device**:

1. **Solar observation (safety!)**: the pinhole camera is the only homemade device allowed to point directly at the sun — the sun projects through the small hole into a bright spot; measure the spot diameter d, measure the hole-to-screen distance L, and the sun's angular diameter ≈ d/L (radians), averaged over several days. A notch appearing in the bright spot is a record of a solar eclipse. Never look at the sun through any optical device or with the naked eye.
2. **Drawing aid**: project the inverted outside scene onto a translucent screen (thin paper/oiled paper) and trace the outlines — far more accurate than eyeballing freehand; used to record sizes and proportions of plants and machine parts (a tool for the Chapter 3 drawing system).
3. **Pinhole-glasses-style dark room**: black out a room, and the scene outside the window projects through a small hole in the wall onto the opposite wall/cloth — the dark room becomes a giant camera obscura where many people can observe at once (for teaching and verification).
4. **Straightness checking**: a small hole plus two positioning pins forms a "line-of-sight reference" that can check whether two points are collinear (an auxiliary means for the Chapter 20 straightedge check).

**Section outputs**: 1–2 pinhole cameras (one per aperture size) and a solar angular diameter record sheet. **Level: L2** — zero material threshold, inevitably repeatable results; this is the most reliable imaging device in the whole book.

### 24.2 Convex Lenses, Concave Lenses, and the Basic Imaging Principles

**Start from a water drop**: a water drop on a leaf can magnify the leaf veins — light passing through a curved transparent body bends at the interface (the old-style statement of the bending rule: light entering a denser medium from a rarer one bends toward the normal, and away from the normal on exit. The precise statement of the law of refraction awaits the arrival of quantitative conditions; this chapter only requires mastering "the more curved the surface, the stronger the bending" plus the verifiable imaging rules below).

**Operational definitions of the two lens types**:

- Convex lens (thick in the middle, thin at the edges): converging. Pointed straight at the sun, it gathers a bright spot on a screen — the distance from this spot to the lens center is the **focal length f**, the single most important number of a lens.
- Concave lens (thin in the middle, thick at the edges): diverging. It cannot form a real image on a screen and can only be used together with a convex lens (Section 24.7 Galilean telescope).

**Convex-lens imaging rules (verify each entry with a candle; reciting formulas is not allowed to stand in for experiments)**:

| Object distance u (in units of f) | Nature of image | Image distance v | Typical use |
|---|---|---|---|
| u>2f | Inverted, reduced, real | f<v<2f | Telescope objective imaging |
| u=2f | Inverted, same size, real | v=2f | Copying, comparison (f can be measured at this point: u=v=2f) |
| f<u<2f | Inverted, magnified, real | v>2f | Projection (camera-obscura projection drawing) |
| u<f | Upright, magnified, virtual | Same side, seen by eye | Magnifier |
| u=f | No image (rays exit parallel) | — | Searchlight-style collimation (theoretical position) |

**Three field methods of focal-length measurement (mutual cross-checks)**:

1. **Solar focusing method**: point the lens straight at the sun (**only paper gets illuminated; no human eye may be in the light path**), move white paper to the smallest bright spot, and measure the lens-to-paper distance. The sun is not at infinity; the systematic lengthening is on the order of f²/(1.1×10¹¹), negligible for this chapter's focal lengths (<1 rod).
2. **Equal-size image method**: place the candle and a white screen at equal distances on opposite sides; move the lens until a same-size inverted image appears on the screen; object and image are then each 2f from the lens, so measure and obtain f. This method does not depend on the sun and is the standard method.
3. **Displacement method** (two-position imaging): fix the object-to-screen distance L (L>4f); the lens then has two positions that give a sharp image, separated by d; then f=(L²-d²)/(4L). This method avoids the error of hunting for the "lens center"; left as an exercise for Chapter 25.

**Magnification (magnifier usage)**: M ≈ distance of distinct vision / f. Take the distance of distinct vision as about 0.25 m for a normal adult (record individual differences as measured). A lens with f=50 mm gives M ≈ 5x. **This explains the consequence of chasing high magnification: the higher the magnification, the shorter f, the more curved the lens, the smaller its diameter, and the shorter the working distance** — high magnification is not merely "harder to grind"; it is bought from physics (field of view, depth of field, and chromatic aberration all worsen at once).

**Section outputs**: imaging-rule verification records and focal-length measurement records (one file per lens: number, diameter, focal length, measurement method).

[Card 24-05 Side-Light Projection Glass Selection] (eight fields)

1. **Input materials**: vessel-grade glass blanks (Chapter 14, T-4 grade, about a 20% pass rate); magnifier (for stones and color patches). **Not every piece of glass can become a lens** — this card exists to throw out the unusable ones before any grinding is spent on them.
2. **Tools required**: strong light source (furnace mouth or several candles), white screen, darkroom, ink (for the seep test), Iceland spar (8.3, for stress figures, if available). Calibration source: striae are revealed by side-light projection — **striae are themselves transparent and invisible in transmitted light**.
3. **Sequence and control points (four criteria in elimination order, coarse to fine)**: (1) **no cracks** — tap and listen (clear, long ring is good; a dull thud is rejected), then ink-dot seep test for a seep line; (2) **properly annealed** — Iceland spar held close shows stress figures; without spar, 30 days' storage with no self-cracking plus a tap recheck; (3) **no striae** — strong light from the side onto a white screen; no banded light and dark in the shadow; point bubbles ≤3 per finger-width and <0.3 mm; (4) **no stones, no color patches** — visual plus magnifier on the unmachined face; no hard points, no dark clumps; uniform pale green is acceptable. Control points: the order cannot be reversed — cracks and stress are eliminated first so no work is wasted.
4. **Empirical parameters and calibration**: bubble limit ≤3 per finger-width, each <0.3 mm; expected pass rate about **20%** of vessel grade (empirical, calibrate; rises as melting stabilizes); thickness requirements for passing blanks — magnifier blanks ≥1/6 of blank diameter (a thin center after grinding will break), telescope objective blanks ≥8 mm.
5. **Observations to record**: build a **per-melt selection file** — blanks counted / passed / rejected by cause, tallied by category. The trend in rejection causes feeds back to improve melting in 14.6.
6. **Pass / rework / scrap criteria**: pass = all four criteria met; rework = striae generally over limit but otherwise sound, **downgrade to small-diameter (≤half a finger) beads or bead blanks** — small diameter gives striae less chance to cross the aperture, and bead microscopes (24.7) need exactly this stock; scrap = cracks or unannealed (remelt).
7. **Common failures and diagnosis order**: (1) striae discovered only after grinding → the projection bench was skipped, build it; (2) a whole melt rejected → check the 14.3 melting record: batch or annealing?; (3) implausibly high pass rate → criteria enforced too loosely (especially the bubble limit by feel); recheck with magnifier and rule; (4) blank passes but shatters near the center during grinding → thickness insufficient, the 1/6-diameter rule was not applied.
8. **L1 / L2 / L3 evidence**: L1 = one melt's selection file plus the four-criteria sheet; L2 = three consecutive melts with comparable pass rates and cause distribution, and passing blanks ground into acceptable lenses; L3 = a second person screens one melt from this card alone, pass rates within 5 percentage points.

### 24.3 How to Select Glass for Optical Work

**Not every piece of glass can serve as a lens**. Chapter 14 already graded the output: among vessel-grade glass, only a minority can be ground into lenses. This chapter does not raise glass quality (that is the business of Sections 14.6 and 14.8 and of temperature control in Chapter 25); it only establishes **selection criteria** — screening the glass on hand once against four hard criteria.

**Four selection criteria (executed in elimination order, coarse first then fine)**:

| No. | Criterion | Method | Pass standard |
|---|---|---|---|
| 1 | No cracks | Light tap and listen (a clear, long ring) plus an ink-spot soak to reveal seepage lines | Eliminate any piece with a dull tap sound or seepage lines |
| 2 | Annealing pass | Iceland-spar birefringence check (Section 8.3 crystal) held close to view the stress pattern; crossed polarizers are not a feasible substitute when no crystal exists, so fall back on: 30 days of storage with no self-cracking plus a tap-sound recheck | Weak stress pattern (if checkable); no self-cracking |
| 3 | No striae | **Side-light projection method**: a strong light source (furnace mouth/multiple candles) shines on the blank from the side, with a white screen catching the shadow — striae appear in the shadow as dark/light bands | No banded light-dark variation in the shadow; point bubbles ≤3 per finger-diameter field of view and diameter <0.3 mm (empirical value, must be field-calibrated) |
| 4 | No stones, no color stains | Visual inspection plus magnifier on the unfinished surfaces | No hard points, no dark clumps; an overall pale-green tint is acceptable |

**The side-light projection method is this chapter's most important inspection invention**: striae are themselves transparent and invisible to the naked eye against the light, but a tiny refractive-index jump deflects a side-coming beam, so they develop on the screen. Dozens of blanks can be screened in an afternoon. Apparatus: a dark corner, one-sided strong light, white screen, blank rack — keep it permanently once built; Chapter 26 uses the same setup for checking liquid homogeneity.

**Selection discipline**:

- Take random samples from every "crucible" of glass (Section 14.3) for full inspection, and build a **crucible-batch selection archive**: number of blanks, number passed, and rejection reasons tallied by category. Trends in rejection reasons feed back to guide Section 14.6 improvements — the selection bench is the glassworks' quality-control department.
- Expected pass rate: about two in ten among vessel-grade glass (empirical value, must be field-calibrated; it will rise once melting stabilizes).
- Thickness requirements for passed blanks: magnifier blanks ≥ 1/6 of blank diameter (insufficient center thickness after grinding will crack); telescope objective blanks ≥ 8 mm.
- **Fallback route**: if a given batch's striae generally exceed limits, downgrade it to small-diameter (≤ half a finger) beads/bead blanks — with small diameter, the probability of a stria crossing through is low. The glass-bead microscope (Section 24.7) is prepared precisely for this fallback.

**Section outputs**: side-light projection inspection bench, four-criteria selection worksheet, crucible-batch selection archive. **Level: L2** (the criteria are repeatable to execute).

[Card 24-01 Abrasive Settling and Grading] (eight fields)

1. **Input materials**: river-bank coarse sand or crushed and screened quartz gravel (Chapter 2); water. Wash the mud out first — mud makes all three settling fractions cloud together.
2. **Tools required**: tall container (the taller, the cleaner the separation), stirring rod, three labeled receiving jars (coarse / medium / fine), scored rule. Calibration source: grading rests on one objective quantity — **settling time** — not on judging grain size by eye.
3. **Sequence and control points**: stir the sand thoroughly in water → **settle 30 s**, pour the suspension into the coarse jar → stir the remainder → **settle 5 min**, pour into the medium jar → stir → **settle 30 min**, pour into the fine jar → let each settle, pour off clear water, dry in shade, label. Control points: pour at the three fixed times, and **pour slowly so the settled sand is not stirred back up**.
4. **Empirical parameters and calibration**: three grades = 30-second (coarse, opens the curve and removes thickness), 5-minute (main fine-grinding stock), 30-minute (polishing mud, or red ochre substitute); the rule is **the longer the settle, the finer the fraction** (empirical, calibrate to local sand density). Before changing grade: wash hands, workpiece, tool, and change the bench cloth — one grain of coarse grit ruins an hour of polishing.
5. **Observations to record**: per batch — source / yield and proportion of each grade / intended use / any cross-contamination.
6. **Pass / rework / scrap criteria**: pass = three grades clearly separated and the fine grade shows no coarse grains in raking light; rework = grades blurred (wrong timing or pouring too fast), regrade the whole batch; scrap = coarse grit has already contaminated a polishing run (that lens returns to fine grinding).
7. **Common failures and diagnosis order**: (1) fractions will not separate → settling times out of order or pouring too fast; (2) coarse grains still in the fine jar → sand not washed first, or not re-stirred before the third pour; (3) low yield → source too coarse, change sand source; (4) long scratches on a polished surface → contaminated fine grade, return to fine grinding.
8. **L1 / L2 / L3 evidence**: L1 = one batch graded and jarred with proportions recorded; L2 = three consecutive batches grading stably (fine grade passes) and one acceptable lens polished with that sand; L3 = a second person grades from this card alone, fine-grade yields within 10%.

[Card 24-04 Pitch Polishing Lap: Making and Tuning Hardness] (eight fields)

1. **Input materials**: natural pitch (or **rosin:beeswax ≈ 2:1 as substitute**); wooden lap disc with a flat face; polishing agent (30-minute fine mud, or hematite red ochre in a thin slurry).
2. **Tools required**: heating vessel (**water bath or furnace-mouth waste heat**, away from open flame), scraper, a tool of the matching curve (for pressing the shape). Calibration source: hardness is read from feel and season, not from a thermometer.
3. **Sequence and control points**: pour pitch onto the disc **about one finger-joint thick** → while warm and plastic, press the matching tool into it to form the curve → cut a grid of grooves (to hold slurry and let air escape) → let it harden → charge with slurry → polish. Control points: **pour thickness and the temperature at pressing** — too cool and the curve will not take, too hot and it runs.
4. **Empirical parameters and calibration**: pitch layer about one finger-joint thick; substitute rosin:beeswax ≈ 2:1 (empirical, calibrate; **the warmer, the softer**); polishing correction <0.1 mm (beyond that you are grinding, not polishing — back to 24.4). **The state of the lap is the thermometer of polishing quality**: pitch that "bites" the glass is too soft (hot weather or soft mix), add rosin; a lap that will not cut is too hard, add beeswax.
5. **Observations to record**: per lap — pour date / mix (pitch, or rosin-beeswax ratio) / ambient temperature / hardness adjustments / number of pieces polished and their results.
6. **Pass / rework / scrap criteria**: pass = lap curve matches the work and polished pieces pass 24.6; rework = biting or refusing to cut, adjust the mix in place; scrap = lap surface scored by coarse grit (repour the whole lap; it cannot be patched).
7. **Common failures and diagnosis order**: (1) glass grabbed and torn → pitch too soft, add rosin; (2) polishes dull for ages → too hard or slurry too dry, add beeswax or thin the slurry; (3) concentric scratch rings → coarse grit residue, clean the whole station; (4) a lap that works in the morning bites in the afternoon → room warmed up, harden it or polish early and late.
8. **L1 / L2 / L3 evidence**: L1 = one lap plus one acceptably polished piece; L2 = two laps across seasons or temperatures with adjustment records comparable; L3 = a second person makes a lap and polishes an acceptable piece from this card alone, both reading "biting" and "not cutting" the same way.

### 24.4 Grinding Tools, Grinding Media, and Surface Finishing

**Principle carried over from Chapter 20**: lapping = abrasive rolling and cutting between workpiece and lap tool. This chapter transplants that regime onto glass with two glass-specific additions: the lap tool must be softer than the glass (iron, copper, or hardwood all work; glass lapped against glass ruins both), and every change of abrasive grade requires thorough cleaning (coarse-grit residue is the number-one source of scratches).

**Abrasive grades in sequence (both dimensions — hardness and fineness — must be managed)**:

| Grade | Abrasive | Source | Purpose | Stop criterion (move to next grade) |
|---|---|---|---|---|
| Rough grinding | Crushed sandstone/quartz pebbles, broken and sieved | Chapter 2 riverbanks | Establish curvature, remove thickness allowance | Full coloring (grind marks uniformly cover the surface), sagitta within <0.5 mm of the target curvature |
| Medium grinding | Fine quartz sand (0.1–0.3 mm) | Section 14.2 sieve set | Unify the grind marks | Within 5 minutes after switching to the fine sand, all old marks are gone |
| Fine grinding | Settling-classified sand | Newly made in this section | Eliminate medium-grind marks | Viewed obliquely against the light, no visible scratches remain, only a uniform matte surface |
| Polishing | Settling fine sludge/iron-oxide red rouge (if hematite is registered) | This section/Chapter 2 | Matte surface turns transparent | Lens imaging passes the Section 24.6 inspection |

**Settling classification (fineness no sieve can sort — let water and time do the sieving)**:

1. Fill a tall tub (≥1 cubit deep) with water, sprinkle in fine sand, and stir evenly.
2. Let stand t minutes, then siphon (or decant) the upper suspension into a second tub — the result is "t-minute sand".
3. Classification scheme (empirical value, must be field-calibrated; rule: the longer the settling, the finer the yield): 30-second grade (coarser than fine-grinding), 5-minute grade (the fine-grinding mainstay), 30-minute grade (polishing).
4. Dry each grade and store it in a numbered ceramic jar. **Scratch mutual checking**: test-grind each grade of abrasive on a fresh glass piece for 1 minute; the scratch size should be clearly smaller than that of the previous grade — if it fails, re-classify the whole grade.

**Curvature lap tools: concave–convex mutual lapping plus sphere-diameter rings**:

- Plano-concave and plano-convex lenses need only one pair of lap tools: cast-iron or hard-copper disks (Chapter 17 copper, Chapter 18 iron), one concave and one convex.
- **Mutual-check method (the curved-surface version of Chapter 20's three-way mutual checking)**: lap the convex disk against the concave disk with fine abrasive; if contact is uniform (color-contact check), the two surfaces share the same curvature — the lap tools must pass mutual lapping themselves before touching glass.
- Press the glass against the convex tool (to grind a concave surface) or the concave tool (to grind a convex surface). Technique: **figure-eight motion plus clockwise rotation of grip** — the workpiece travels a figure eight around the tool, and the grip orientation changes once a minute to prevent one-sided uneven wear. The figure-eight method is the key discipline of curved-surface uniformity and matters more than brute force.
- **Sphere-diameter rings (curvature test rings)**: turn a hardened steel ring (Chapter 19) to a true-circular mouth and set it on the ground curvature, viewing against the light for gaps — uniform light transmission = curvature matches; localized light leak = deviation at that spot. Keep a set of rings of different diameters, each ring corresponding to one grade of curvature.

**Pitch polishing (the final stage of surface finishing)**:

1. Lap: pour a layer of natural bitumen (or a rosin:beeswax ≈ 2:1 substitute — empirical value, must be field-calibrated; the warmer, the softer) about one finger-joint thick onto a wooden disk.
2. Press-forming: while the pitch is warm and plastic, press it firm with the matching curvature lap tool to obtain a curved surface that fits the workpiece.
3. Polishing agent: 30-minute-grade fine sludge or red rouge mixed with water into a thin slurry.
4. Operation: same figure-eight motion, light pressure, slow grinding; add slurry every few minutes.
5. Pitch "grabbing" the glass = pitch too soft (hot weather/soft formula); add rosin to harden. Won't polish = too hard; add beeswax to soften. **The pitch lap's condition is the number-one factor in polishing success or failure; record every condition change in the archive.**

**Process discipline (violators rework)**:

- Changing abrasive grade = wash hands, wash workpiece, wash lap tools, swap the bench's wet cloth — a single coarse grain is enough to ruin an hour of polishing.
- Wet-grind with water throughout. Dry-grinding glass = dust inhalation plus torn grind marks (safety boundaries at chapter end).
- At the end of each stage, view the workpiece obliquely against a lamp: the grind-mark directions should be uniform in all directions. One-directional bright marks = monotonous motion; return to the figure eight.

**Section outputs**: abrasive settling-classification tub set, concave–convex lap-tool pair, sphere-diameter ring set, pitch lap. **Level: L2** (fine-grinding sand classification is repeatable; polishing pitch depends on registered materials — regions lacking materials see the alternative route).

**Alternative route (regions lacking bitumen/rosin)**: hardwood disk plus a beeswax/grease coating for polishing — it can polish bright but holds its figure poorly, and image quality drops half a grade (usable for magnifiers, marginal for objectives); boundary: it cannot support the Section 24.7 telescope objective batch. Regions lacking hematite substitute the finest settling sludge for red rouge, with polishing time roughly doubled (empirical value).

[Card 24-02 Sagitta Method for Curvature, and a Home-Made Spherometer] (eight fields)

1. **Input materials**: the lens under test, or a tool whose curve is already ground; a ring of known internal diameter d (three-point ring). Without a ground surface there is nothing to measure — curvature has to exist before it can be checked.
2. **Tools required**: **three-point ring** (three feet define one plane) plus a central measuring screw (Chapter 20 thread) or a depth comparator; a flat glass plate for the zero. Calibration source: zero the screw on flat glass before every measurement — **an unchecked zero invalidates every reading**.
3. **Sequence and control points**: zero the spherometer on flat glass → move to the convex surface, all three feet seated → turn the screw down to contact and read the sagitta h → compute R. Control points: **all three feet must sit on the spherical surface** (on a chamfer the reading runs high), and **re-zero for each lens**.
4. **Empirical parameters and calibration**: shallow-sphere approximation **R ≈ d²/(8h)**; example: ring d = 60 mm, h = 3 mm, R ≈ 3600/24 = 150 mm. Focal conversion: plano-convex f ≈ 2R, bi-convex f ≈ R, with n ≈ 1.5 (the error is absorbed into focal tolerance). Focal tolerance ±10%; out of tolerance means downgrade, never scrap.
5. **Observations to record**: per lens — ring diameter d / reading h / computed R / converted f / deviation from design in percent.
6. **Pass / rework / scrap criteria**: pass = f within ±10%; rework = out of tolerance in the thin direction, continue grinding in 24.4 (**once a tool reaches its sagitta, its curve becomes the reference**; later lenses are matched to it by coloring, no re-measurement each time); scrap = no such grade — out-of-tolerance lenses are downgraded.
7. **Common failures and diagnosis order**: (1) readings jump → feet not seated or screw loose; (2) R wildly off expectation → h was not zero-corrected, or d was measured across the outside instead of between the feet; (3) f does not follow from R → the glass is not n = 1.5 (heavier flint deviates more); back-calculate n from measurement instead of forcing 1.5; (4) focal lengths scatter across a batch → the tool curve has drifted, re-measure the tool.
8. **L1 / L2 / L3 evidence**: L1 = one lens with d, h, R, f fully recorded; L2 = a batch (≥5) within ±10% and the tool curve registered as a reference; L3 = a second person measures the same lens from this card alone, R values within 2%.

### 24.5 Lens Curvature and Focal Length

**The sphere is the only curved surface that can be ground stably**: mutual lapping naturally converges to a sphere (concave and convex tools lapped against each other self-correct). So all lenses in this chapter take spherical surfaces; "surface-figure accuracy" means how far the surface deviates from a sphere.

**The sagitta method (measuring and copying curvature)**: the radius of curvature R is large and cannot be measured directly; what can be measured is the sagitta (chord height) h — how much the spherical surface sinks/rises within a ring mouth of diameter d.

- Relation (shallow-sphere approximation): R ≈ d²/(8h). Example: ring mouth d=60 mm, h=3 mm, so R≈3600/24=150 mm.
- **Homemade spherometer**: a three-pointed-foot ring (three feet define a plane) plus a central measuring screw (Chapter 20 screw threads) or a depth-comparison pin. First set it on flat glass and record the zero position, then move it onto the lens and read the central foot's in–out difference = h. Graduation relies on the screw pitch (feed per full turn) and a graduated dial (Chapter 3 rule engraving), readable to 1/20 of the pitch (empirical value, must be field-calibrated).
- **Copying**: once a lap tool is ground until its sagitta meets spec, its curvature becomes the "standard piece" for that ring mouth — subsequent lenses need only a color-contact mutual check against the tool to copy the same focal length, with no re-measurement of every piece (the Chapter 22 standard-piece idea applied to curved surfaces).

**Curvature → focal length (this chapter's lens calculation table)**: take the glass refractive index as n≈1.5 (Chapter 14 glass, true value unmeasured — from Chapter 25 onward the liquid-immersion comparison method can close in on it; this chapter always uses the approximate value and folds the error into the focal-length tolerance).

| Lens form | Curvature condition | Focal length approximation |
|---|---|---|
| Plano-convex | Convex surface radius R | f≈2R |
| Equiconvex | Each surface radius R | f≈R |
| Glass bead (full sphere of radius R) | — | f≈1.5R (the bead's limiting magnification follows from this) |

Example: for a target magnifier with f=50 mm, grind equiconvex surfaces with R≈50 mm; with a d=60 mm sphere-diameter ring, the target sagitta is h≈d²/(8R)=3600/400=9 mm.

**Tolerances (pragmatic conventions; avoid chasing impossible precision)**:

- Focal-length tolerance: ±10% (empirical value, must be field-calibrated; exceeding it only affects finished-piece grading, not scrapping — re-grade and renumber by measured f).
- Sagitta control points: rough grinding leaves a 0.5 mm allowance into fine grinding; fine grinding to the tolerance midpoint; polishing correction <0.1 mm.
- **The two surfaces concentric**: judge centering by the edge-thickness difference — lay the lens flat on a platform and run a surface gauge around the outer edge once; the height variation must be <2% of the diameter (empirical value). Out-of-tolerance pieces sit tilted when mounted in tubes, and the image skews.

**Final focal-length acceptance is by optical method**: sagitta is a process-control quantity; every finished piece has f measured by the Section 24.2 equal-size image method and is engraved with its number — both the "calculated value ≈ measured value ±10%" entries go into the archive, and deviation trends in turn check whether the spherometer has drifted (a foretaste of the Chapter 22 reference mutual-check system).

**Section outputs**: spherometer, curvature–focal-length calculation table, lap-tool sagitta standard archive. **Level: L2**.

[Card 24-03 Star-Test Image Quality Inspection] (eight fields)

1. **Input materials**: lens under test; star source (a candle flame in a dark corner, better a **pinhole lamp — 0.5 mm hole in a box wall**, reusing the 24.1 technique); white screen (ground glass best, thin paper acceptable).
2. **Tools required**: screen holder that moves fore and aft, dark cloth or darkroom. Calibration source: pinhole size checked with Chapter 3 rules; "image-pattern form" judged against a reference table, not personal impression.
3. **Sequence and control points**: in darkness, form a real image of the star on the screen → **move the screen forward and back** to watch the pattern change → classify the defect against the table → decide the rework destination. Control points: must be dark, must be a single point source, and must be read at **three positions — inside focus, at focus, outside focus**; reading only at focus misses spherical aberration.
4. **Empirical parameters and calibration**: pinhole 0.5 mm; **effective aperture grading A ≥80%, B ≥50%**; useful magnification ceiling 10–30× for telescopes (an honesty boundary — beyond it the limit is the inspection method, not the grinding).
5. **Observations to record**: per lens — pattern at the three positions / effective aperture grade / defect location (center or edge) / rework destination.
6. **Pass / rework / scrap criteria**: pass = grade A or B with a symmetric pattern; rework = spherical aberration or astigmatism, back to fine grinding and polishing in 24.4; scrap = bubbles or striae beyond limits (back to the 24.3 selection criteria; remake as a smaller-diameter item).
7. **Common failures and diagnosis order**: (1) hazy pattern → grinding marks not removed, return to fine grinding; (2) decentered pattern, one side bright → off-center (edge-to-center thickness difference over 2% of diameter), regrind the center thickness; (3) rainbow at the edge → chromatic aberration, inherent to a single lens — downgrade, do not rework; (4) the same lens passes today and fails tomorrow → source or screen distance not fixed, standardize the bench first.
8. **L1 / L2 / L3 evidence**: L1 = one lens with three-position records and a grade; L2 = a batch (≥5) inspected piece by piece, with A/B ratio and rework causes tallied; L3 = a second person grades the same batch from this card alone, agreeing on A/B classification ≥80% of the time.

### 24.6 How to Inspect Image Quality

A lens that has "turned transparent" is not the same as "passed". The image-quality inspection trio; every piece is inspected, and failures return to Section 24.4 for rework:

**1. Star-point method (most sensitive to single-lens image quality)**:

- Star-point source: a point candle flame in a dark corner, or better — a pinhole-shrouded lamp (a 0.5 mm hole in the lamp-box wall, reusing the Section 24.1 technique).
- Operation: the lens forms a real image of the star point on a white screen (ground glass or thin paper is best); nudge the screen slightly back and forth and observe the image-spot shape.
- Interpretation table:

| Phenomenon | Diagnosis | Action |
|---|---|---|
| Image point small and round, expanding symmetrically into a disk with slight back-and-forth movement | Good figure | Pass |
| Image point trails into a comet shape | Local grinding bias/poor centering | Check the edge-thickness difference; re-fine-grind |
| Image point scatters into an irregular blob | Figure disturbed (worn lap tool or monotonous motion) | Re-round the lap tools by mutual lapping, then regrind |
| Image-spot shape jumps (asymmetrically) with slight back-and-forth movement | Striae crossing the effective aperture | Change the blank (a selection-stage miss) |
| Image point edged with a colored fringe | Chromatic aberration (inherent to a single lens, not a process defect) | Record the color-fringe width; downgrade pieces over the limit (see Section 24.8) |

**2. Grid-plate inspection (distortion and overall sharpness)**:

- Place a ruled grid plate (Chapter 3 straightedge + scriber, line spacing one finger) within the focus and project it through the lens into a real image on a screen.
- Measure the grid in the image: bent straight lines = distortion (tolerable in magnifiers, recorded for objectives); sharp center with blurry edge = strong spherical aberration (inherent to a single lens; record the usable aperture); doubled lines or locally broken lines = striae or scratches (return to Section 24.4).
- Assign each lens its **effective aperture** from "the aperture fraction over which the grid lines are seen clearly" — the finished-piece tag carries both numbers, "effective aperture/full aperture," and only the effective aperture is used.

**3. Pit-and-scratch visual inspection**: dark background, single side light, black velvet backing; examine zone by zone with a magnifier. Point pits ≤5 within the effective aperture, no clustering; isolated scratches are acceptable so long as a fingernail drawn across the lens surface does not catch (alternative method: scratches that do not cross the star-point image zone may be released).

**Inspection record sheet (one per lens, filed with the piece)**: number, blank crucible batch, measured f, effective aperture, star-point conclusion, grid conclusion, pit count, grade (A/B/C), inspector and date.

**Grade determination**: A = star point round, effective aperture ≥80% of full aperture; B = star point essentially round, effective aperture ≥50%; C = everything else (magnifiers only). Only Grade A qualifies as a telescope objective — **grade-tiered sale and grade-tiered use** are the key to material utilization.

**Section outputs**: star-point bench (pinhole lamp + matte screen), grid plate, lens inspection-sheet system. **Level: L2**.

### 24.7 Magnifiers, Simple Telescopes, and Microscopes

**1. Magnifier (the production mainstay; make twenty pieces first)**:

- Specification: diameter 1–2 fingers, equiconvex R≈50–100 mm (f=50–100 mm, M≈2.5–5x).
- Mounting: wooden frame or copper band + handle (Chapter 17 rolled copper sheet band; adhesive from Chapter 13, or beeswax-rosin).
- Uses that cash in immediately: fine-grind scratch checking, weight engraving verification, fabric thread density (Chapter 15), seed sorting (Chapter 10), and bootstrapping lens/glass inspection — **the magnifier is the tool for inspecting magnifiers; the first batch must be made first**.

**2. Single-lens telescope (Galilean — upright image, observer-friendly)**:

- Objective: Grade A convex lens, f≈2–5 rods (1–2.5 m), diameter 2–3 fingers. Long focal length = the angular size of chromatic and spherical aberration shrinks — **the whole trick of the single-lens telescope is "the objective's focal length must be long"**; a fat, long, clumsy tube is the accepted price.
- Eyepiece: concave lens f≈50 mm (Grade B suffices).
- Tube: two nested draw sections (inner and outer tubes slide to focus, Chapter 20 round-wood turning); total length about f(objective) − f(eyepiece). Coat the inside of the paper/wood tube with soot to kill stray light.
- Magnification: M ≈ f(objective)/f(eyepiece) ≈ 20–50x nominal, **but the actually useful magnification, limited by image quality, is about 10–30x** — beyond that the image blurs and detail is lost instead (see Section 24.8).
- Mount: three-legged wooden stand + azimuth pivot (Chapter 21 shafts and bearings). Handheld at 20x and above, shake makes observation impossible; the mount is not an accessory but a necessity.
- First observation targets (acceptance items): lunar craters discernible, Jupiter's four bright moons discernible, Saturn showing a non-circular outline, stars showing no disk magnification (verifying "stars are too far away").
- **Safety red line: the telescope is never pointed at the sun** (projection is feasible but the first-generation product does not do it — the heat risk to the objective's cementing/paint surfaces is unknown; do not gamble with eyes).

**3. Glass-bead microscope (single-bead type; this chapter's highest magnification)**:

- Bead: small glass pieces rejected at selection (the Section 24.3 fallback) melted at the end of a fine glass rod into a round bead 1–2 mm in diameter (Section 14.3 lamp-flame/furnace-mouth rod-pulling skill). The bead is the lens: f≈1.5R≈1–3 mm, M ≈ distance of distinct vision/f ≈ 100–200x nominal.
- Mounting: the bead is clamped in a small hole drilled through thin metal sheet; the specimen sits extremely close behind the bead (working distance <1 mm); focusing = a screw pushing the specimen stage (Chapter 20 fine-pitch thread). This is the device's only precision part.
- What can be seen (pragmatic expectations matched to historical experience): the striations of fibers (linen, wool), fly wing veins, pollen grains, diatom shells in dried-out pond residue, yeast (in suspension, needs strong oblique light). Cell-nucleus-level clear observation is **not promised** — limited by chromatic aberration and illumination.
- Illumination: a small mirror/white screen under the stage reflects and concentrates light onto the specimen — the bead lens has a small aperture, so **illumination is the first bottleneck**; dark-field matters more than magnification.
- **Positioning**: the single-bead microscope is an L1–L2 device (bead consistency is poor; inspect and select bead by bead; with f so short, precise per-bead measurement is impossible — enter the actual resolution into the archive as the acceptance criterion). It opens the microscopic world, but a "repeatably manufacturable microscope" requires multi-lens combinations and is blocked by each of the walls in Section 24.8.

**4. Preview of the compound route (not pursued)**: a compound microscope with two-stage objective + eyepiece magnification (hundreds of times total historically) needs a low-aberration short-focus objective design — it depends on achromatic glass and finer figures; it is explicitly listed as a next-step dependency, and extrapolating from single-bead experience is not allowed.

**Section outputs**: magnifier batch, 1–2 Galilean telescopes + mounts, 1 single-bead microscope. **Levels**: magnifier L2, telescope L2 (first unit L1, moved to L2 after a second unit verifies it), bead microscope L1–L2.

### 24.8 Why High-Quality Optical Components Are Hard to Make

**Conclusion first**: what this chapter achieves is "useful optics". The four walls below each seal off one upgrade path, and the order for scaling them is fixed — skip any wall and the product stays stuck at L1.

**Wall One: the glass itself (the materials wall)**.

- Striae and homogeneity: the root of star-point jumps and broken grid lines is inhomogeneous refractive index in the blank. The fix is melt stirring + precision annealing (the Section 14.8 checklist) — which needs temperature-controlled furnaces (temperature control begins in Chapter 25, maturing after the heat engine in Chapter 28).
- Single glass type: achromatism requires at least two glasses matched by refractive index/dispersion (high-lead flint + crown). Lead-glass formulations belong to the chemical capability of Chapter 23 and beyond; **with only one glass, chromatic aberration is mathematically impossible to cancel, and the only route around it is small aperture with long focal length** — this is why the Galilean telescope is long and slender: not aesthetics, but the engineering price of a materials defect.
- **The three prerequisites of the cemented doublet (reviewer's note: achromatism is not "sticking two pieces together")**: (1) the refractive indices and dispersions of the two glasses must be **measured into tables** (liquid-immersion comparison approximation, after Chapter 25); (2) the curvatures of the two elements must be computed in pairs under achromatic conditions (the mathematics of Wall Three); (3) **the cement layer's refractive index must lie between the two glasses** and the cement thickness must be uniform — natural resin cements (a Canada-balsam-style rosin/oil formulation) are usable, but cement shrinkage and thermal drift make image quality wander month by month, requiring monthly star-point re-inspection. Missing any one of the three, a cemented doublet is "two pieces of glass and an illusion".

**Wall Two: surface-figure accuracy (the measurement wall)**.

- Once chromatic aberration caps the usable aperture, image-quality sensitivity to figure error rises steeply. Precision figures demand "error below light-wavelength level" — **at present we have not even measured the number that is the wavelength of light** (the diffraction observed with the pinhole camera is the starting point; quantification must wait for the marriage of slits and measurement science).
- The current means (sphere-diameter rings, color-contact mutual checks) cap the figure at the "visibly smooth" level, corresponding to a useful-magnification ceiling of about 30x (telescope). The next level needs the knife-edge shadow test (sensitive to spherical mirrors) and, later still, interferometry — **interferometry needs good lenses to build good instruments, and good instruments need interferometry for acceptance; this loop cannot be untied from the inside** — the only way out is the mirror (reflecting; no glass homogeneity needed) route opening a side door: a concave mirror images without chromatic aberration, and its grinding and testing can use the knife-edge method — **alternative route: the reflecting telescope**; the materials threshold drops sharply (speculum bronze/glass substrate + polish suffices), at the price of higher sensitivity to mirror figure and an obstruction problem. Listed as a next-stage objective.

**Wall Three: design and calculation (the methods wall)**.

- Correcting aberration across multiple lenses is the inverse problem of "finding the surface combination for given materials", requiring a systematic law of refraction, trigonometry, and iterative calculation — long-term accumulation belonging to the era after Chapter 25's quantitative methods. This chapter's calculation tables cover only single spherical elements.

**Wall Four: the inspection of inspections (the bootstrap wall)**.

- Lens A inspects lens B, but who inspects A? This chapter anchors on nature with "sun—star point—grid" (solar angular diameter, straight lines, grid), which is already the optimal solution; finer inspection anchors (wavelength, standard resolution targets) do not yet exist. **Before the anchors are upgraded, every report of "I ground a better lens" must first answer whether the inspection method was upgraded in step** — write this discipline onto every inspection sheet.

**Quantitative boundary summary table (an honest capping of this chapter's capability)**:

| Device | Stably achieved | Reason for the ceiling |
|---|---|---|
| Magnifier | 2.5–5x, L2 mass production | Chromatic aberration (visible color fringing above 5x) |
| Telescope | 10–30x effective, L2 | Chromatic aberration + figure + mount stability |
| Bead microscope | ~100–200x nominal, L1–L2 | Illumination + chromatic aberration + bead consistency |
| Compound microscope | Not pursued | Wall One + Wall Three |
| Achromatic objective | Not pursued | Wall One (lacking lead glass) |
| Photolithography-grade optics | Long term, depends on the full chain | All of Walls One through Four + more |

**Where this leaves the reader**: after this chapter you can resolve the lunar surface, see microorganisms in a pond, and hang a 5x magnifier at every inspection workstation — enough to support all the instrument needs of Chapters 25 and 26 (thermometer reading magnification, engraved-line checking, specimen observation). **Do not let the frustration of "we cannot make microscope objectives" obscure the leap of "observation tools from nothing to something"**; and do not let one accidentally successful bead microscope (L1) be mistaken for a microscope industry (L3).

---

## Parameter Summary Table ( supplement)

| Parameter | Value | Category |
|---|---|---|
| Pinhole aperture window | 0.5–2 mm (grade set by test at box depth) | Empirical |
| Focal-length tolerance | ±10% (out-of-tolerance only downgrades the grade, never scraps) | Empirical |
| Curvature approximation | R≈d²/(8h); plano-convex f≈2R, equiconvex f≈R | Formula |
| Refractive index approximation | n≈1.5 (error folded into the focal-length tolerance) | Approximation |
| Settling classification | Three grades: 30 s / 5 min / 30 min | Empirical |
| Blank pass rate | About two in ten for vessel grade | Empirical |
| Bubble limit | ≤3 per finger-diameter field and <0.3 mm | Empirical |
| Centering edge-thickness difference | <2% of diameter | Empirical |
| Effective aperture grading | A ≥80% / B ≥50% | Criterion |
| Useful magnification ceiling | Telescope 10–30x | Honest boundary |

## Process Card Index ( supplement)

## Labor Hours, Manpower, and Consumables ( supplement)

| Item | Manpower | Labor hours (empirical values) |
|---|---|---|
| One pinhole camera | 1 person | Half a day |
| One batch of abrasive settling classification | 1 person | Half a day (including drying) |
| One magnifier (rough grinding to polishing) | 1 skilled worker | 1–2 days |
| One telescope objective | 2 people | 3–5 days |
| One single-bead microscope | 2 people | 2–3 days |
| Consumables | Abrasives, bitumen, glass blanks (two in ten pass) | Entered in the Chapter 38 ledger |

---

## A. Existing Tools List

- Chapter 3: marking straightedge, scriber, angle plate, balance and weight set, record system.
- Chapter 8: Iceland spar registry entry (for birefringence checks, if available); alkali ash.
- Chapter 13: carpentry and workshop construction.
- Chapter 14: the full glass-melting set, vessel-grade glass plate/rod, T-grade sample-piece library, rod-pulling skill, annealing ash pit.
- Chapters 17/18: copper and iron sheet and bar stock.
- Chapter 19: hardened steel (sphere-diameter rings, three pointed feet, engraving needles), files, drills, chisels.
- Chapter 20: scraping and lapping regime, three-way mutual checking, screw-thread cutting, flat reference.

## B. New Tools Added This Chapter

| Tool | Manufactured in |
|---|---|
| Pinhole camera (with multi-aperture plate set) | Section 24.1 (Chapter 13 carpentry + iron sheet) |
| Focal-length measurement bench (object–screen slide rail + equal-size image method) | Section 24.2 (Chapter 3 measuring tools + Chapter 13 wood parts) |
| Side-light projection inspection bench | Section 24.3 |
| Abrasive settling-classification tub set and abrasive-grade archive | Section 24.4 (Chapter 11 ceramic jars + Chapter 14 sieve-set extension) |
| Concave–convex lap-tool pair, sphere-diameter ring set | Section 24.4 (Chapter 18 iron/Chapter 17 copper + Chapter 20 mutual lapping) |
| Pitch lap | Section 24.4 |
| Spherometer (three feet + screw) | Section 24.5 (Chapter 19 hardened parts + Chapter 20 screw threads) |
| Star-point inspection bench (pinhole lamp box + matte screen) | Section 24.6 |
| Grid inspection plate | Section 24.6 (Chapter 3 engraved lines) |
| Lens inspection sheets and grading system | Section 24.6 |
| Magnifier batch (2.5–5x) | Section 24.7 |
| Galilean telescope + tripod mount | Section 24.7 (Chapter 20 sleeves + Chapter 21 mounts) |
| Single-bead microscope (screw focusing) | Section 24.7 (Chapter 14 bead melting + Chapter 20 fine-pitch thread) |

## C. Unresolved Dependencies

- Achromatic glasses (a second type such as lead glass): blocked on the chemical purification and formulations of Chapter 23 and beyond.
- Precision annealing furnace: blocked on temperature control (the Chapter 25 thermometer comes first, maturing after the heat engine) — the hard ceiling on glass stress and homogeneity.
- Measurement of the wavelength of light and interferometric/knife-edge inspection: prerequisites for upgrading figure accuracy; the reflecting telescope (mirror route) is the side-door objective.
- Glass blowing and tube pulling (left over from Chapter 14): a shared prerequisite for thermometers, microscope tubes, and chemical vessels; next-stage objective.
- Compound microscope objective design methods: depends on accumulated quantitative optics.
- Means of measuring refractive index: this chapter approximates with n≈1.5, error folded into the tolerance.

## Safety Boundaries

- **Never look directly at the sun or bright sources near it through any lens or telescope**; observe the sun only by pinhole projection. Post a warning sign beside the telescope.
- Wet-grind with ventilation throughout when grinding glass: inhaled silica dust causes pneumoconiosis — dry-grinding glass dust is absolutely forbidden; sieve sand and pour powder away from drafts, with mouth and nose covered (Chapter 8 dust rules).
- Handle broken glass per the Chapter 14 procedures: wooden collection box, leather gloves, and for puncture wounds remove splinters and flush.
- Heat bitumen/rosin with a water bath or furnace-mouth residual heat, away from open flames — bitumen is flammable; at the first smoke, leave the fire; treat burns per the Section 6.8 cold-water flushing procedure.
- Bead-melting operation: insert the rod end into the flame gradually to prevent spatter; wear eye protection (smoked glass shards block only part of the light — **never use them to stare at the furnace mouth**; follow the Chapter 14 narrow-slit viewing rule).
- Chamfer the edges of pitch laps and iron lap disks to prevent cuts.

## Acceptance Criteria

- **L1 proof-of-principle**: pinhole camera forms an image and the solar angular diameter is measured; one magnified observation completed with a water drop/bead; one hand-ground lens forms a real image of a candle flame.
- **L2 repeatable manufacture**: 10 magnifiers produced consecutively and passing inspection (measured f within ±10% of nominal, star point Grade B or better); the second telescope repeats the first unit's performance (Jupiter's four moons discernible); abrasive grades consistent between batches (test-grind scratch comparison passes); lens inspection sheets and selection archives operating on file.
- **L3 sustainable production**: a blank—selection—grinding—inspection—grading closed loop, with monthly trend records of blank pass rate and finished-product yield; stable bitumen/abrasive supply chain (the settling-classification system is reproducible); lap tools and pitch laps can be repaired and remade; magnifiers issued as standard workstation equipment with periodic re-inspection.
- Current position: magnifiers and inspection system L2; telescope L2; bead microscope L1–L2. Missing for L3: glass supply-chain stability (Chapter 14 crucible-batch variation) and precision annealing.

## Next-Step Dependencies

- Chapter 25: thermometer glass tubing (depends on the tube-pulling objective), magnified scale observation (this chapter's magnifiers), balance and spherometer mutual checks.
- Chapter 26: observation and inspection for chemical experiments (magnifiers, side-light projection bench); glassware blanks reuse this chapter's criteria.
- Chapter 27: optical readout devices (magnifier + engraved lines); a mechanical prototype for upgrading the spherometer into a comparator.
- Long term: reflecting telescope development (mirror route); achromatic optics (lead glass, after Chapter 23 chemistry); measurement of the wavelength of light (slit diffraction, once quantitative methods mature).

## Failure Modes and Diagnostics supplement

| Symptom | Candidate causes (by probability) | Verification | Action |
|---|---|---|---|
| Star point grows a comet tail | Grinding bias/poor centering | Re-measure the edge-thickness difference | Re-fine-grind; check the figure-eight technique |
| Irregular image blob | Worn lap tool/monotonous motion | Re-round the tools by mutual lapping | Lap the tools against each other; change the stroke pattern |
| Image spot jumps with slight movement | Striae crossing the effective aperture | Re-check by side-light projection | Change the blank |
| Polishing scratches | Coarse-abrasive residue | Oblique dark-field illumination | Re-state the cleaning procedure; return to fine grinding |
| Won't polish/pitch grabs | Pitch too hard/too soft | Hand feel and season | Adjust the rosin/beeswax ratio |
| Measured focal length runs long | Spherometer zero drift | Re-zero on flat glass | Recalibrate; record the correction |
