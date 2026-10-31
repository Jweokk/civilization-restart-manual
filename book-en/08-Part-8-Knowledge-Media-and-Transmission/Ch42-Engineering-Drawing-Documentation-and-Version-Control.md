# Chapter 42: Engineering Drawing, Technical Documentation, and Version Control

> **Interface with Section 4.8**: This chapter is the full version of the Section 4.8 minimal drawing method (on-board three views / datums / allowances) — the same rules, a new medium (paper), plus duplication / versioning / cross-workshop interfaces. The allowance notation of on-board drawings corresponds one-to-one with this chapter's tolerance annotation.


> This chapter answers two structural criticisms from the first review round. First: "How drawings are drawn, how tolerances are annotated, how they are transferred losslessly between workshops, how versions are controlled — the book has no place for any of it, and Chapter 35's photolithographic alignment needs precisely this language." Second: "Drawings that show only outlines, without datums, dimensions, tolerances, and revision numbers, cannot be reproduced by anyone else"; "metallurgy, machinery, and chemical engineering each pass on their own, yet with interface information missing nothing can be assembled or used." Chapters 18–23 built precision into parts, Chapter 20 provided datums and gauges, Chapter 22 provided go/no-go inspection, and Chapter 35's photomask plates need a millimeter-level graphical language — yet until this chapter, every shape, dimension, and change could be handed on only "with the master present." Chapter 41 supplied paper and ink; on top of paper and ink this chapter erects a second layer of medium: **a language that compresses three-dimensional objects into two-dimensional symbols yet can be decompressed back into the object by a second person with zero ambiguity, plus a version system that keeps that language from going wrong.** Without this chapter, cross-workshop collaboration falls back into the oral era and re-drifts with every change of master.

## Chapter Objectives

Reading this chapter, a settlement should come away with four outputs:

| Output | Specification | Use |
|---|---|---|
| Qualified drawings | Three views + sections + datum-based dimensions + tolerances + surface symbols + a complete title block, from which a second person can independently reproduce the object | The "lossless transfer" medium across people, workshops, and generations |
| Tolerance and fit annotation system | Datum-style dimensioning, tolerance notation, three classes of fits, four-level surface symbols, interfacing directly with the Chapter 20/22 gauges | Drawing tolerance zone = gauge manufacturing order |
| Master drawing and duplication system | Masters never leave the archive + pin-prick stencil duplication (duplicate error ≤0.3 mm) + borrowing register | One master drawing distributed to many workshops |
| Version and change system | Drawing number + version letter + revision record table + dual-sign-off four-step change process + five-item accompanying-information handover card | Eliminates assembly accidents from old versions mixing in |

## Capability Boundaries

**Can do:**

- Establish the ability to draw and read orthographic three views (including full and half sections), converting any machined object into a drawing a second person can reproduce.
- Establish datum-style dimensioning, tolerance notation (nominal size + upper/lower deviations), three classes of fits (clearance / transition / interference), and the four-level surface symbol system, with drawing tolerance zones corresponding directly to the "go/no-go" sizes of the Chapter 22 plug and snap gauges.
- Establish the master drawing archive, pin-prick duplication, and the borrowing register; the version-number rules and the dual-sign-off change process; the five-item accompanying information for cross-workshop handover.
- Train drafters: the Grade-2 standard is "able to independently convert an object into a qualified drawing, and to build a qualified part from the drawing alone."

**Cannot do:**

- **Chemical duplication such as blueprint printing.** Blueprint paper requires ferric ammonium citrate + potassium ferricyanide (cyanotype) or the dichromated-gelatin route, which depends on the stable output of the Chapter 23 chemical industry; this chapter lists it only as an upgrade slot (Section 42.5.4). The current routes are pin-prick duplication and rubbing.
- **Print-grade drawing duplication.** Woodblock and movable type were already listed as upgrade routes in Section 41.1.3; this chapter makes no repeated promise. Bulk distribution of drawings relies on stencil pouncing, at 0.5–1 person-hour per sheet.
- **Hand-drawn line widths below 0.2 mm.** The stable lower limit of reed-pen ink lines is about 0.2 mm (criterion in the parameter master table); finer graphics must take the Chapter 35 enlargement-drawing + microphotography route, and Section 42.7 of this chapter only pre-seeds its drafting conventions.
- **The complete theory of descriptive geometry** (exact development of intersection curves, axonometric drawings). This chapter teaches only the engineering-necessary minimum: three views, sections, scales, and line types. Axonometric pictorials are listed as an elective for drafters advancing to Grade 3.

**External dependencies (counted into the C list):**

1. Chapter 41 paper and ink capacity: a medium apparatus requires about 15–40 drawings (mixed drawing-grade and folio sheets); the master archive consumes 50–100 sheets per month during startup, to be planned jointly with ledger-book paper.
2. Pine soot and charcoal powder: ink making and pouncing transfer share the Chapter 6 charcoal-kiln flue output.
3. Legacy modern drawings (if any exist from starting points B/C): teaching and format reference only; using them directly as master drawings is forbidden — the tolerances and material grades they carry mostly exceed this settlement's process capability (see Section 42.3.2, "Tolerances Must Have a Source").

## Pre-Work Verification

Checklist format. If any item fails, the corresponding process step must not start; missing items and compensations are logged on the same page.

| # | Verification item | Criterion (confirm you have X, with standard Y) | Source chapter |
|---|---|---|---|
| 1 | Drawing-grade paper | 450×600 sized calendered paper, ≥20 sheets; an ink dot held 1 s blots to diameter ≤2 mm (Chapter 41 criterion) | 45 |
| 2 | Folio paper | 210×300 (process-card size), ≥30 sheets, same criterion | 45 |
| 3 | Inspection straightedge | Length ≥600 mm; compared against the Chapter 3 standard ruler, error ≤0.2 mm over 600 mm; edge straightness: laid on a surface plate, light transmission is uniform with no bright gaps | 20 |
| 4 | Square | Flip cross-check: spacing of the two lines <0.1 mm (Chapter 20 criterion) | 20 |
| 5 | Hard charcoal pencils | Willow charcoal sticks soaked in dilute hide-glue solution and shade-dried, ≥2; on sized paper, ten 100 mm lines with no broken core, no powder shedding, erasable with a damp cloth | Section 42.2.5, this chapter |
| 6 | Hard reed pen and fine brush | The reed pen, inked once, draws a 300 mm line without breaking, width uniform; the fine brush writes 10 characters without splaying (Chapter 41 criterion) | 45 |
| 7 | Pine-soot ink | Ground until a drop on paper does not bleed and 100 mm lines come out uniform; after the writing dries, a drop of water does not smear it (Chapter 41 criterion) | 45 |
| 8 | Drawing board | Flat hardwood board ≥500×700 mm; the surface checked in multiple directions against the inspection straightedge's edge, light transmission uniform and consistent; four edges straight enough to serve as a fence datum | 9 |
| 9 | Dividers (compass) | The two points close with no gap; opened to draw a full circle, the start–end mismatch is invisible to the eye; no self-sliding once opened | 20 |
| 10 | Duplication needles | Hardened steel needles (sewing needles or Chapter 19 homemade), ≥3; the point scores the paper leaving a fine trace without raising burrs | 19 |
| 11 | Charcoal powder bag | One bag of fine pine-soot powder in fine cloth (no grit between the fingers, Chapter 41 water-elutriation criterion); when tapped, the powder exits as mist, not clumps | 45 |
| 12 | Drawing archive and stamp | One compartment of a moisture-proof cabinet (Chapter 41 lime dehumidifying cabinet); one borrowing register; one "VOID" stamp (red) | 45 |

## 42.1 Why Words Cannot Build a Machine

### 42.1.1 Three Failure Modes of Oral Transmission

The first is **dimensional drift**. Oral language has no millimeters, only body references — and body references differ from person to person. Take a transmission shaft: the first article was verified against a snap gauge at 20.0 mm diameter, and the master teaches it as "thumb thick":

| Transmission step | Original mnemonic | Reference the apprentice understands | Part built | Deviation from first article |
|---|---|---|---|---|
| First article | Verified against snap gauge | — | 20.0 mm | — |
| First generation | "Thumb thick" | Own thumb width 22 mm | 22.0 mm | +2.0 |
| Second generation | "Same as my master's thumb, slightly thinner" | Estimated from memory | 23.5 mm | +3.5 |
| Third generation | "Two fingers wide" | Two fingers together 26 mm | 26.0 mm | +6.0 |

The empirical drift rate is +5–15% per generation (when passed orally with no measured feedback; if every generation verifies against a snap gauge, it drops to within ±2%). Worse is the mating hole: the mnemonic "if it fits in, it's fine" lets the clearance grow from the designed 0.2 mm to 1.5 mm — the shaft turns, but it slops, hammers, and breaks the shaft within three months. **Dimensional drift is the archetypal silent failure: every generation believes it did the right thing, because every generation passed the then-current "it fits in" test.**

The second is **terminological ambiguity**. "A bit thicker," "slightly tighter," "like the last one" — these phrases carry concrete numbers in the speaker's head and none in the listener's. Writing cannot rescue them either: describe a flange's shape, hole positions, and chamfers in two hundred characters, and every "obviously" the writer omits is a pit the reproducer falls into.

The third is **information decay**. When teaching, masters omit details they consider too trivial to mention: which face to measure from (datum), which face to machine first (process sequence), whether a casting needs aging (Chapter 18) — the listener does not know what they do not know. Decay cannot be patched by "asking more questions," because the questions themselves require the drawing language before they can even be posed.

### 42.1.2 Counterexample Walkthrough: The Drawingless Workshop's Second Water Pump

Suppose a workshop copies a second lift pump from the physical first one. Assembly relationship: the pump body's mounting feet have 4 bolt holes at 220×160 mm spacing that must land on the base's 4 bolts.

| Step | What actually happens | Result |
|---|---|---|
| 1 | The master dictates from memory of the first unit: "hole spacing one hand-span plus two fingers, measure from the edge" | One hand-span = 200–230 mm (varies by person), and "edge" never says whether the casting edge or the machined edge |
| 2 | The apprentice measures 235 mm with his own hand-span, starting from the cast edge (unmachined, not straight) | Base hole spacing 235×155, skewed in both directions |
| 3 | The pump body is "traced against" the first physical unit, hole positions noted on a scrap wooden board, which swelled 1% with damp | Pump body hole spacing 222×162 |
| 4 | Final assembly: pump body onto base, 4 holes against 4 bolts, not one hole passes | Full rework |

The rework bill: the base is a casting; scrapping one costs 6–10 person-hours plus one furnace of coke (Chapter 18); re-laying-out, re-drilling, re-tapping 4 person-hours; idle waiting for material 2 days. And what would all of this have cost to prevent? **Drawing one base part drawing with hole spacing and datum annotated: 2 person-hours; drawing the pump body: 2 person-hours.** Four person-hours of drawing against more than twenty person-hours of rework — that is the entire economics of the drawing system. The larger the scale and the finer the division of labor, the more lopsided this account becomes: when two workshops over separate hills each build half of the same machine, no drawings means not a rework problem but a never-assembles problem.

### 42.1.3 Why the Drawing Is the Only Medium of "Lossless Transfer"

| Medium | Across people (author absent) | Across time (author dead) | Across workshops (receiver does not know the author) | Unambiguous (verifiable) |
|---|---|---|---|---|
| Oral teaching | No | No | No | No (the "it fits in" standard drifts) |
| Written description | Yes | Yes | Partial | No (descriptions can omit; the reader does not know what is missing) |
| Physical sample | Yes | Partial (it wears) | Yes | Partial (measurable, but does not say which face is the datum or which are tolerance requirements) |
| Drawing (views + dimensions + tolerances + version) | Yes | Yes | Yes | Yes (every requirement has a number and an inspection method) |

The root of why words cannot build machines: **language is sequential** — sentence after sentence, by the ninth sentence the first is already blurred; **shape is concurrent** — all of a part's dimensions hold simultaneously and constrain one another. A drawing spreads the concurrent relationships onto a plane in one stroke, where the relation of any dimension to any other is visible at a glance; add tolerances (the allowed deviation ranges) and datums (where to measure from), and it becomes the only medium that can move "how to do it right" completely into another person's head. Chapter 37 solved "is the person there"; Chapter 41 solved "what to write on"; this chapter solves "what to write, how to write without error, and how to fix it when written wrong."

## 42.2 Orthographic Drafting Method

### 42.2.1 Three-View Rules

Orthographic projection has one core action: **the line of sight is perpendicular to the projection plane**. No perspective, no tilt — perspective makes near things large and far things small; orthographic does not, so holes of the same size stay the same size in all three views. This is the premise on which "reproducing from the drawing" stands.

Describe an object with three mutually perpendicular projection planes:

| View | Projection direction | Name | Placement |
|---|---|---|---|
| Front view | Looking from directly in front | The face that best expresses the shape features | The reference view, drawn first |
| Top view | Looking from directly above | Fixes length and width | Directly below the front view |
| Left view | Looking from directly left | Fixes height and width | Directly right of the front view |

The three views maintain the "three equals" relationship; both drafting and reading are checked with the same mnemonic:

> **Lengths align** (front and top views equal in length, aligned vertically); **heights level** (front and left views equal in height, aligned horizontally); **widths equal** (top and left views equal in width).

Mnemonic short form: "align, level, equal-width." Self-check method: hold the square's blade against the common direction line of two adjacent views; for every edge and every hole, the projection lines must fall on one straight line — if they do not, either the drawing is skewed or a view was misread; stop immediately and check the projection direction.

Front view selection rule: choose the direction that **best represents the object's shape and working position**. A pump's front view should show the inlet, outlet, and chamber outline, not the end-face circle. Choose the front view wrong and the other two views all follow; rework means redrawing.

### 42.2.2 Sectional Views: Seeing Inside

When invisible features — holes, cavities, slots — grow so numerous that hidden lines exceed about one third of a view, hidden lines piled on hidden lines become unreadable. Then abandon "exterior as-is" and switch to a section: **imagine cutting the object with a plane, removing the front half, and drawing the cut face of the rear half**.

| Section type | Use | Applied to |
|---|---|---|
| Full section | The whole view is cut; the entire cut face is hatched | Asymmetric parts, parts dominated by internal cavities (valve bodies, pump chambers) |
| Half section | A symmetric part drawn half as exterior, half as section | Symmetric parts needing both inside and outside expressed (end caps, sleeves) |

Three rules: (1) The cut position must be labeled — draw cutting symbols (short thick dashes) on another view with letters, and label "A—A" above the sectional view to match. (2) The cut face is hatched: metals use 45° thin solid lines at 2–3 mm spacing; adjacent parts reverse direction or double the spacing; nonmetals use crosshatch. (3) A section is imaginary; the other views are still drawn as the complete object — you may not "cut away half" of the other views too.

### 42.2.3 Scale System

| Scale | Use | Rule |
|---|---|---|
| 1:1 | **Preferred grade.** Small and medium parts drawn at actual size; the object can be laid on the drawing for comparison | If 1:1 works, use no other grade |
| 1:2 | Large parts drawn reduced (bases, frames, furnace parts) | 1 mm on the drawing = 2 mm on the object |
| 2:1 | Small, complex parts drawn enlarged (nozzles, valve cores) | 2 mm on the drawing = 1 mm on the object |
| 5:1, 10:1 | Reserved for photomask enlargement drawings (Section 42.7) | Photolithography layouts only |

Two iron rules. First, **only the standard grades are permitted** — ad hoc scales such as 1:3 or 3:5 are forbidden; nobody can convert a nonstandard scale mentally, and measuring such drawings guarantees errors. Second, the first Iron Law of drafting: **scaling dimensions off the drawing is forbidden**. Every dimension is governed by the annotated number; the lines on the drawing declare only shape, the numbers declare size. Paper expands and contracts (moisture swelling 0.5–1%), lines have width (0.5 mm), eyes err — measure a drawing three times and get three numbers; an annotated number is written once and is forever one number.

### 42.2.4 Line Type Conventions

A part drawing uses only four types of lines, and each means exactly one thing — mixing line types is lying:

| Line type | Width (mm) | Use | Notes |
|---|---|---|---|
| Thick solid | 0.5–0.7 | Visible outlines, drawing frame border, cutting symbols | Thickest on the sheet; the bold–thin contrast layers the drawing |
| Thin solid | 0.2–0.3 | Dimension lines, extension lines, section hatching, leader lines | Thick-to-thin ratio ≥2:1 |
| Hidden (dashed) | Same width as thin solid; dashes 3–4 mm, gaps 1 mm | Invisible contours (internal holes, back-side features) | Convert to sections wherever possible to eliminate hidden lines |
| Center (dash-dot) | Same width as thin solid; dashes 15–20 mm, dot gaps 2–3 mm | Axis lines, symmetry center lines | The first and last segments must be dashes, not dots; the intersection of a circle's center lines is the circle's center |
| Phantom (dash-double-dot) | Same width as thin solid | Extreme positions of moving parts, outlines of adjacent parts (not part of this part) | Draws "where it can move to" and "what sits beside it" |

Line width control: cut the reed pen to a fixed slanted edge; the edge width is the line width. Before drawing, make 5 test lines on scrap paper and inspect with the Chapter 24 3–5x magnifier that the batch's line widths are consistent (the 5 lines of one batch must be visually indistinguishable from one another).

◎ The hand-feel of even lines: one stroke of 100–150 mm, no stopping midway, no retracing, no re-inking. Practice method: lay a sheet over a qualified finished line and trace it 100 times, until traced lines overlap the sample with stable width. Misjudgment compensation (hand-feel is never the sole basis): after each drawing is finished, sample 5 lines; check straightness by laying the straightedge edge along them (uniform light transmission) and check width with the magnifier — the hand-feel of even lines is finally entered into the record on these two physical proofs.

### 42.2.5 Drawing Sequence and the Three Drafting Implements

Drafting uses three implements, each with its own duty: the **hard charcoal pencil** (willow charcoal soaked in dilute hide glue and shade-dried — for the rough draft; its marks wipe off with a damp cloth, so mistakes are allowed); the **hard reed pen in ink** (final thick and thin lines — once written they cannot be changed, permitted only last); the **fine brush** (numerals, text, section hatching). This order is itself error control: separating "what is allowed to be wrong" from "what is not allowed to be wrong" is the common containment logic of every craft (forging, pulping, drafting).

The nine steps of drawing (detailed in Card 42-01): measure the object → set scale and sheet size → lay out the frame positions of the three views → draw the datum lines (center line, base line) → light charcoal draft of the three views (after each view, the three mnemonic checks) → count hidden lines and decide on a section → ink and darken (thick before thin, curves before straights) → dimension and tolerance annotation (Section 42.3) → title block and self-check.

[Card 42-01 Three-View Drawing Card] (eight fields)

1. **Input materials**: One physical part or wooden pattern; one Size-2 sheet (210×300, Chapter 41 criterion); pine-soot ink (a drop on paper must not bleed); fine cloth (for wiping the charcoal draft).
2. **Tools required**: Drawing board (pre-work verification item 8); inspection straightedge (Chapter 20, length re-verified once before use); square (flip cross-checked, <0.1 mm); dividers; hard charcoal pencil; hard reed pen; fine brush; 3–5x magnifier (Chapter 24).
3. **Operating sequence and control points**: (1) Measure all functional dimensions of the object and record them on a draft (measure twice and take matching values; if they differ, measure again). (2) Choose the scale against the sheet-size table using the largest overall dimensions (1:1 if possible). **(3) Draw the datums first: the center line (dash-dot) and the base line — every dimension grows from these.** (4) Charcoal-draft the three views, front → top → left; **after each view, immediately run the three mnemonic checks (align / level / equal-width)**. (5) Count the hidden lines; if more than one third of the view, switch to a section and label A—A. (6) Ink lines: thick before thin, curves before straights, one stroke of 100–150 mm. (7) Annotate dimensions and tolerances per Section 42.3. (8) Fill the eight title-block fields (Section 42.4.2). (9) Final check: the five-question self-check mnemonic.
4. **Empirical parameters and calibration**: Two line-width grades, 0.5–0.7 and 0.2–0.3 mm (after cutting the reed pen edge, set the grade by comparing same-batch test lines under the magnifier); hidden dashes 3–4 mm, hatch spacing 2–3 mm, dash-dot segments 15–20 mm — on first drawing, scribe a standard sample length at the paper edge with the dividers and follow it.
5. **Process observation and recording items**: Corrections are allowed in the charcoal stage; in the ink stage only one scrape-and-fix is permitted. On the back of each sheet, record start/end times and the rework count (for building the drafter labor-hour baseline statistics).
6. **Pass / rework / scrap criteria**: Pass = all five self-check questions answered + a free link left in the dimension chain (Section 42.3.1) + unambiguous datums + no missing title-block fields. Rework = charcoal-draft error (wipe clean with a damp cloth and redraw that view); localized ink error (light scrape with a blade, burnish with a bone folder, re-ink — allowed only once at the same spot; a second error there is judged scrap). Scrap = wrong datum choice or layout overflowing the sheet (redraw the entire sheet; the old sheet is archived as void).
7. **Common failures and troubleshooting order**: Views fail the mnemonic → first check whether the top view was placed directly below the front view (placing it beside is the beginner's first error) → check the projection direction is perpendicular → check for omitted hidden lines. Ink bleeds → check the paper is Chapter 41 qualified sized stock → check whether the ink was ground too thin. Circle not round → check the dividers' hinge for looseness → check it was drawn in one stroke (a retraced circle never closes).
8. **L1 / L2 / L3 evidence**: L1 = one part drawing passing the five self-check questions; L2 = that drawing verified through the blind-build test (Section 42.8 L2); L3 = 20 or more part drawings of different parts all verified by blind build or workshop use, with labor-hour statistics entered in the ledger.

**Self-check mnemonic (copy at the edge of the drawing board):**

> First question — datums: are the center line and base line drawn?
> Second question — the mnemonic: align, level, equal-width — checked item by item?
> Third question — hidden lines: is a section needed, and if sectioned, is A—A labeled?
> Fourth question — dimensions: does every dimension have a datum, a tolerance, and is a free link left?
> Fifth question — title block: are all eight fields filled and the version letter written?

## 42.3 Dimension and Tolerance Annotation

### 42.3.1 Datum Faces: Where Dimensions Are Measured From

**A datum is the starting point of dimensions and must be an actually existing face, line, or center line** — a machined base face, end face, or axis. Unmachined blank surfaces may not serve as datums (not flat; Chapter 20 blank-face flatness reaches only the ±1 mm grade). Phrases like "measure from the edge" are outright banned by the datum system: which edge? Machined face or blank face?

Three datum selection rules: choose the **largest machined face** (the base's bottom face); choose the **assembly locating face** (the face that mates with other parts); choose the **face machined first** (the process reference for everything that follows).

The notation system has exactly one opposition: **datum-style is required; chain-style is forbidden**. Chain dimensioning lays dimensions segment after segment — each segment carrying its own ±0.2 deviation, so over four segments the worst-case position error of the last hole relative to the first end is four ±0.2's added (±0.8). Datum-style measures every segment from the same datum, so any segment's deviation is only its own ±0.2:

| Dimensioning method | Four-hole positions (datum = machined face at left end) | Worst-case position error of last hole | Verdict |
|---|---|---|---|
| Chain | Hole 1 at 50±0.2 from end; Hole 2 at 60±0.2 from Hole 1; Hole 3 at 60±0.2 from Hole 2; Hole 4 at 60±0.2 from Hole 3 | ±0.8 | Forbidden |
| Datum | Hole 1 at 50±0.2 from end; Holes 2, 3, 4 at 110, 170, 230 from end, each ±0.2 | ±0.2 | The only legal form |

One companion rule: **a closed dimension chain may never be annotated**. If you dimension every segment plus the overall length from the datum, you form a closed loop end to end — manufacturing cannot simultaneously satisfy four mutually contradictory tolerances. The correct practice is to leave one **free link** (usually a non-functional segment) unannotated, letting manufacturing error deposit entirely into this unimportant segment.

### 42.3.2 Tolerance Notation: Nominal Size + Upper/Lower Deviations

Tolerance is the drawing's contract with the maker: **nominal size + upper deviation + lower deviation**, written after the dimension number, upper deviation above, lower deviation below:

| Notation | Reading | Meaning |
|---|---|---|
| 20 +0.2/−0.1 | Nominal 20, upper +0.2, lower −0.1 | Acceptable range 19.9–20.2 mm |
| 20 ±0.1 | Symmetric upper and lower | Acceptable range 19.9–20.1 mm |
| φ25 +0.10/0 | Hole, lower deviation zero (hole-basis notation) | Acceptable range 25.0–25.10 mm |
| 30° ±1° | Angular tolerance | — |
| Untoleranced dimensions | Title block carries the blanket note "untoleranced dimensions ±0.5" | All non-functional dimensions follow this without exception |

Writing rules: upper and lower deviations must use the same number of decimal places (write +0.20/−0.10, not +0.2/−0.1); diameters take φ, radii take R; the deviation characters are half the size of the nominal size characters.

**Tolerances must have a source (Iron Law Two)**: a drawing may not demand a tolerance the process cannot deliver. Every machining method has a "capability band"; the drawing's tolerance band may not be narrower than 1.5 times that workstation's capability band (safety factor, empirical value). Capability bands are not memorized — they are field-calibrated:

| Workstation / process | Capability band (empirical) | Field calibration method | Source chapter |
|---|---|---|---|
| Cast or forged blank faces | ±1–2 mm | Cast 5 pieces consecutively from the same wooden pattern; measure the range of the same-named dimensions | 11, 18 |
| Layout, sawing, filing | ±0.3–0.5 mm | Make 5 right-angle pieces consecutively at the same workstation; measure the range | 20 |
| Turning (three-grade lathe) | ±0.1 mm | Turn 5 shafts in one batch; snap gauge + measured range | 20 |
| Scraping | ±0.05 mm | Spotted contact against a surface plate (≥8–12 points per 25×25 mm) | 20 |
| Lapping | ±0.01 mm | Three-plate mutual lapping (≥20 points per 25×25 mm) | 20 |

Transcribe the calibration results (each workstation's measured range) into the ledger (the companion account of the Chapter 37 skill matrix); the next drawing revision takes its values from the ledger. **Demanding a tolerance tighter than the current workstation is not done by writing smaller numbers — it is done by adding a scraping or lapping operation to the drawing and marking the surface symbol** — the legal source of a tolerance always lives in the process, never at the pen tip.

**Interface with the Chapter 22 gauges — the drawing tolerance zone is the gauge manufacturing order**:

| Drawing notation | Plug gauge for holes | Snap gauge for shafts |
|---|---|---|
| Hole 20 +0.2/0 | Go end at 20.0 (must pass), no-go end at 20.2 (must stop) | — |
| Shaft 20 −0.1/−0.25 | — | Go end at 19.9 (must pass), no-go end at 19.75 (must stop) |

Rule: for any mating dimension toleranced on the drawing, its inspection **must** be governed by the corresponding go/no-go gauge (the Chapter 22 system); piece-by-piece measurement with rulers and calipers may not replace batch gauge inspection — one inspector can check hundreds of pieces per day with gauges, and the criterion does not vary by person. Drawing, gauge, and inspection form one closed loop: the drawing defines the tolerance zone → the gauge casts that zone into a physical object → inspection applies the gauge's verdict to every piece.

### 42.3.3 Fits: Clearance, Transition, Interference (Hole-Basis System)

Two parts embracing each other can relate in only three ways. This manual uses the **hole-basis system**: holes are hard to machine (limited by tooling), so make the hole at nominal size first (lower deviation always 0), then fit the shaft — a smaller shaft gives clearance, a larger shaft gives interference. Taking nominal 20 mm as the example:

| Fit | Hole | Shaft | Limit clearance/interference (mm) | Example use |
|---|---|---|---|---|
| Clearance | 20 +0.2/0 | 20 −0.1/−0.25 | Clearance 0.10–0.45 | Sliding guides, pump shaft and bearing bush |
| Transition | 20 +0.2/0 | 20 +0.05/−0.10 | Interference 0.05 to clearance 0.30 | Locating pin seats, handwheel to shaft |
| Interference | 20 +0.2/0 | 20 +0.40/+0.25 | Interference 0.05–0.40 | Pressing a bushing into a hole |

Using interference fits at hand-work tolerance grades (±0.1 mm class) requires two supporting measures. First, **selective matching** — measure each piece before pressing; re-mate any with insufficient interference; stamp both mating pieces with the same mating number (the Chapter 22 pairing concept: mated pairs must never be separated and swapped). Second, **hot assembly** — heat the hole member in a furnace, slip it on, and let it grip as it cools. Order-of-magnitude sanity check: steel's coefficient of linear expansion is about 12×10⁻⁶/°C; heating a 20 mm hole to 200 °C expands it about 0.05 mm — exactly covering the lower-limit interference. Assemblies with more than 0.05 mm interference require hot assembly or a press; cold hammering always damages the surfaces.

### 42.3.4 Surface Requirements: Four-Level Symbols

Tolerances govern "is the size right"; surface symbols govern "how is the face obtained". Four symbols correspond to four process routes and inspection criteria, marked on the leader line of the face in question:

| Symbol | Level | Means of achieving | Inspection criterion | Source chapter |
|---|---|---|---|---|
| ∽ | Rough face | No machining after casting/forging | No bubbles, slag inclusions, or cracks (visual) | 11, 18 |
| ▽ | Ordinary face | Filing, turning | Inspection straightedge edge laid on the face gives uniform light transmission, no visible steps | 20, 21 |
| ▽▽ | Scraped face | Scraping | Spotted contact: 8–12 points within 25×25 mm, evenly distributed | 20 |
| ▽▽▽ | Lapped face | Lapping | ≥20 points within 25×25 mm; a 0.02 mm feeler gauge will not enter | 20 |

Consistency rule: a ▽▽▽ face must carry a dimensional tolerance ≤±0.05 mm, a ▽▽ face ≤±0.1 mm. Marking a lapped face while giving a ±0.3 tolerance burns lapping hours for nothing; conversely, a ±0.01 tolerance marked with ▽ alone is an order that cannot be built. The drafter checks this pairing item by item on every drawing with the Card 42-02 checklist.

[Card 42-02 Tolerance Annotation Card] (eight fields)

1. **Input materials**: The drawing with completed views (output of Card 42-01); the workstation capability ledger page for this part; the list of gauges to be used (Chapter 22).
2. **Tools required**: Straightedge, fine brush; counting rods or abacus for fit calculations (Chapter 3).
3. **Operating sequence and control points**: (1) Confirm the datum face by face (which face? machined or not?) and mark it on the drawing with a short thick bar plus the character "基" (datum). **(2) Annotate every functional dimension directly from the datum; dismantle and rearrange all chain dimensioning without exception.** (3) Write a tolerance on every dimension; before writing, check the capability table: the tolerance band must be ≥1.5x the workstation's range; if not achievable, add a scraping/lapping operation with the matching ▽ symbol. (4) Check mating hole–shaft pairs: same nominal, deviations one of the three classes in the Section 42.3.3 table. (5) Leave one free link unannotated. (6) Write "untoleranced dimensions ±0.5" in the title block. (7) Tick through the checklist's nine questions one by one.
4. **Empirical parameters and calibration**: Safety factor 1.5 (empirical; calibration: schedule the first articles at 1.5 and track the out-of-tolerance rate over 20 pieces — if it exceeds 5%, raise the factor to 1.8 and re-examine workstation capability). Untoleranced dimensions ±0.5 (filing-grade default; cast and forged part drawings use ±1).
5. **Process observation and recording items**: Note the source abbreviation beside every tolerance (e.g., "turned 5 pcs, range 0.15" → ledger page number). A tolerance with no identifiable source is treated as a placeholder and must not go down to the workshop.
6. **Pass / rework / scrap criteria**: Pass = all nine checklist questions answered + every tolerance has a ledger source. Rework = an individual tolerance lacks a source (re-check the capability ledger and add the note). Scrap = datum placed on a blank face or chain dimensioning left intact (rearrange the entire drawing; this is a structural error).
7. **Common failures and troubleshooting order**: Assembly does not fit → first check whether the two drawings' datums are the same face → check for chain accumulation → check that the mating hole and shaft nominals match. Gauge contradicts drawing → check whether the go and no-go ends were made to the tolerance band's upper and lower limits respectively → check whether the drawing's deviation decimal places were miscopied.
8. **L1 / L2 / L3 evidence**: L1 = one annotated drawing passing all nine questions; L2 = parts built to that drawing passing Chapter 22 go/no-go inspection for 20 consecutive pieces; L3 = the checklist archived together with its ledger sources, with two workshops each building mating parts from the drawing and assembling successfully on the first try.

**The checklist's nine questions (copy with the card):** Is the datum a machined face? / Was the chain dismantled? / Was a free link left? / Is the tolerance ≥1.5x the capability band? / Are the deviation decimal places aligned? / Is the untoleranced tolerance written into the title block? / Do the mating hole and shaft share one nominal? / Does the surface symbol match the tolerance? / Does every tolerance have a ledger source?

## 42.4 Standard Sheet Sizes and the Title Block

### 42.4.1 Sheet Size Series (Folding Series)

The sheet sizes adopt the Chapter 41 paper grades directly, with no new sizes — delivering on Chapter 41's promise that "later engineering drawing chapters will reuse this series":

| Sheet | Size (mm) | Chapter 41 grade | Use |
|---|---|---|---|
| Size 0 | 450×600 | Drawing grade | General assembly drawings, large apparatus |
| Size 1 | 300×420 | Full sheet | Subassembly drawings, photomask enlargements |
| Size 2 | 210×300 | Folio | Part drawings (most common), process cards |
| Size 3 | 150×210 | Quarter sheet | Change forms, accompanying cards, index cards |

The folding law: fold the next size up in half and trim the deckle edges to get the next size down (a Size 0 folded ≈ two Size 1s, and so on); binding, folding, and archiving run on one size system end to end. Drawing frame: the frame line sits 10 mm from the paper edge, 20 mm on the binding side; for archive folding, always fold to Size 3 with the drawing number folded to the outside.

### 42.4.2 The Title Block: All Eight Fields, None Optional

The title block is drawn in the drawing's bottom-right corner (140×45 mm on a Size 2 sheet); it is the drawing's "ID card + contract signature area":

| Field | How to fill | Example |
|---|---|---|
| Drawing number | Apparatus code – assembly number – part number (Section 42.4.3) | SP-02-07 |
| Name | The part's functional name, not the material name | Pump body (not "cast-iron piece") |
| Material | Grade designation + source chapter | Gray cast iron (Chapter 18 Grade-3 material) |
| Scale | One of the standard grades | 1:2 |
| Drawn by / date | Handwritten signature and date | |
| Checked by / date | Signature of a Grade-3 craftsperson or the workshop supervisor | |
| Version | A letter; first issue A | B |
| Revision record | Version / date / what changed / who changed / who approved | Table placed above the title block |

Criterion (checked before release to the workshop): **if any one of the eight fields is missing, the drawing may not be issued to a workshop**. No checker's signature = nobody is answerable for the tolerances; no version number = the start of change-control failure; no material = Chapter 18 smelted three heats and nobody knows which one to use.

### 42.4.3 Drawing Number Rules and the Parts List

Drawing numbers have three segments: **apparatus code (two letters or an abbreviation) – assembly number (two digits) – part number (two digits)**. Apparatus codes are assigned centrally by the settlement's drawing archive (water pump SP, lathe CH, annealing kiln K12, ...); assembly numbers are organized by assembly unit; part numbers run serially within the assembly. A whole-apparatus general drawing's number stops at the assembly level (SP-02); on the assembly drawing each part is additionally numbered with a leader line + circled number, and each circled number corresponds to a parts-list row.

Parts list (drawn above the title block on Size 0/1 assembly drawings, filled bottom-up):

| Item | Drawing no. | Name | Qty | Material | Remarks |
|---|---|---|---|---|---|
| 1 | SP-02-01 | Pump body | 1 | Gray cast iron (Chapter 18) | ▽▽ bottom face |
| 2 | SP-02-07 | Shaft | 1 | Medium-carbon steel (Chapter 19) | Quenched and tempered; ▽▽▽ journals |

Rule: the parts list must correspond one-to-one with the circled numbers in the drawing. Standard parts (Chapter 22 threaded parts) get their specification in the name field (e.g., "square-thread screw M8×1.25") with a reference to the standard parts album — standard parts get no separate part drawings; this is the first means of shrinking the total drawing count while preserving interchangeability.

## 42.5 Drawing Duplication and Transfer

### 42.5.1 The Master Drawing System: Originals Never Leave the Archive

Drawings are kept in three layers, each in its place:

| Layer | Item | Storage | Permitted movements |
|---|---|---|---|
| Master drawing | The sole original | Drawing archive moisture-proof cabinet (Chapter 41), double-locked | **Never leaves the archive room**; consultation inside the archive only |
| Stencil | Duplication tooling (Section 42.5.2) | Drawing archive | Used inside the archive |
| Duplicate | Working drawings | The workshops | Collected when worn out; all recalled and destroyed when a new version is issued |

Why the master cannot leave the archive: once out, a drawing enters five risks — fire, water damage, oil stains, folding tears, and casual line edits. In the handcraft era a complex master drawing costs 8–24 person-hours; destroying a master zeroes out that apparatus's design record. **What goes to the workshop is the duplicate; if it is ruined, pounce another** — this is layering "the non-regenerable" apart from "the regenerable," isomorphic with the Chapter 41 layered-medium system.

The borrowing register (applying to both stencils and in-archive consultations) has five columns: drawing number / date out / date back / handler / purpose. The archive keeper takes inventory every ten days; if drawings, stencils, and register do not reconcile, all issue of that drawing number is frozen until the discrepancy is resolved.

### 42.5.2 Pin-Prick Duplication: The Stencil Pouncing Method

The duplication route is pin-pricking rather than hand copying, for three reasons: the stencil guarantees the relative positions of shapes and dimension lines with no distortion; it is fast (0.5–1 person-hour for one Size-2 sheet, versus 2–4 person-hours to hand-copy one part drawing); and the copyist needs no drafting knowledge — half a day of training suffices — a decisive advantage for settlements short on craftspeople.

Stencil making (one-time, 1–2 person-hours):

1. Lay fresh paper over the master drawing; align the two sheets at the four corners and along the diagonals (diagonal mismatch ≤2 mm); weight the corners.
2. Prick holes along all thick-solid contours and center lines with the hardened steel needle. Prick density: **straight segments get only three holes — both endpoints plus the midpoint; arcs get one hole every 15°–20°; arbitrary curves get 1–2 mm hole spacing** (empirical spacing; calibration: after pricking the first stencil, pounce through it, compare the dot outline with the master, and add holes and re-prick wherever the outline deviates more than 0.3 mm).
3. Numerals and text get **only position frames pricked, never strokes** — text is copied by hand, preventing pin distortion from creating wrong characters.

Duplication (reusable 30–50 times):

4. Lay the stencil over fresh paper, align the four corners and clamp; tap the charcoal powder bag lightly over all hole areas, so the powder passes through and leaves a dot matrix on the sheet below.
5. Lift the stencil; lightly connect the dots into lines with the hard charcoal pencil, verify each line against the dot matrix, then ink.
6. **Copy character by character** from the master all numerals, text, and the title block; copy the title block's version letter as-is, and add "duplicate," the duplicator's name, and the date.
7. A second person **reads the duplicate aloud against the master, character by character** (the "read-back system"): the reader calls out the master's numbers while the checker points at the duplicate — miscopied numbers are duplication's most dangerous and hardest-to-detect failure (+0.2 copied as −0.2 flips inspection end to end).

◎ The hand-feel of pricking: needle perpendicular to the paper, wrist fixed, fingers push. Practice method: prick 100 holes in scrap paper; a qualified hole is round with no burrs or tearing at the rim; burrs mean the needle tilted, tearing means too much force. Misjudgment compensation: hand-feel is never the sole basis — after the first duplication from a new stencil, **sample 5 dimensions and compare with the master**; the stencil passes only if deviations are ≤0.3 mm; thereafter sample 1 in every 10 duplicates for re-checking.

Criteria in three grades: Pass = sampled 5-dimension deviation ≤0.3 mm + zero read-back errors. Rework = individual lines out of tolerance (add holes there and re-pounce). Scrap = stencil holes burring generally, or the sheet swelling/shrinking (remake the stencil; also remake once the duplicate count has reached 30–50 sheets). Stop duplication in rainy weather or while the paper is not fully dry — paper swells 0.5–1%, so a 300 mm drawing carries a 1.5–3 mm systematic error; this is the leading hidden source of "the duplicate passed but the part will not assemble."

### 42.5.3 Rubbing and Hand Copying (Conditional Routes)

Carved-line plates (standard symbols, table frames, common layouts) are duplicated by the Chapter 41 rubbing method; purely textual technical documents (process cards, inspection procedures) continue on the Chapter 41 hand-copying + master–apprentice card-copying system. Both routes hold only auxiliary status: **anything carrying dimensions and tolerances goes through stencil pouncing, without exception** — making a carved rubbing plate itself requires carving from a drawing, and every transfer adds another hand's error.

### 42.5.4 Blueprint Printing: Upgrade Slot (Declared, Not Promised)

Blueprint printing (photosensitive copying) raises duplication speed by an order of magnitude, but it needs a stable chemical source of ferric ammonium citrate + potassium ferricyanide (cyanotype) or dichromated gelatin — the former depends on the Chapter 23 iron-salt and organic-salt routes, the latter on chrome ore or Chapter 26 wet chemistry. **Trigger condition: Chapter 23 produces acceptable photosensitive salts for three consecutive batches AND monthly drawing demand exceeds 50 sheets.** Until then, blueprint paper remains an upgrade slot and may not appear in any L1–L3 acceptance or production scheduling. Microphotographic duplication (the Chapter 35 route) serves photomask plates only, not engineering drawings.

### 42.5.5 Storage

Drawings follow the Chapter 41 archive-layer protections: moisture-proof cabinet, smoke fumigation against insects, light avoidance, folded to Size 3 and stored upright. Two drawing-specific additions: first, for important apparatus, one best-quality duplicate of the master is kept off-site (another workshop's archive or a stone cellar) as disaster backup (the Chapter 41 two-copy off-site system); second, voided drawings are never burned — after a red "VOID" slash is stamped across them they move to the obsolete-drawing area and stay archived; they are the only physical evidence for accident tracing (Section 42.6.4).

## 42.6 Version Control and Change Management

### 42.6.1 Version Numbering Rules

First issue A; each revision advances one letter: A→B→C (beyond ten revisions means the design has not converged — the apparatus should be re-reviewed as a whole). The numeric form (1/2/3) is an equivalent style, but **one archive may use only one form**, and once registered the two may never be mixed.

What must trigger a new version: any change to dimensions, tolerances, material, heat-treatment requirements, fit relationships, or process references. What does not: adding an omitted line, correcting a clerical slip — record a "same-version erratum" in the revision record table; the drawing number and version stay unchanged, but the error on the sheet must be scraped out completely — two versions of one number left on a drawing are forbidden.

Revision record table (carried on every drawing, placed above the title block, append-only):

| Version | Date | Change content | Changed by | Approved by |
|---|---|---|---|---|
| A | — | First issue | | |
| B | | Hole spacing 220→240; datum changed to bottom face | | |

Rule: the revision table **only appends and never rewrites history rows** — who changed what, on which day, and why is the drawing's autobiography; tearing out a page breaks a segment of the traceability chain.

### 42.6.2 The Four-Step Change Process

Changing a drawing is not the drafter's private affair; it is a formal process that walks through five sheets of paper:

| Step | Action | Owner | Output and criterion |
|---|---|---|---|
| 1 Propose | Fill the change form: drawing number / current version / what changes / why / which parts and workshops are affected | Anyone (the discoverer) | Change form entered in the register |
| 2 Review with dual sign-off | Verify the change's impact on mating parts, gauges, and inventory | Process holder (Grade 3) + workshop supervisor **dual sign-off**; either alone is invalid (Section 37.6.3 of Chapter 37) | Signed change form |
| 3 Issue new version | Redraw or scrape-revise the master; advance the version; register in the revision record table; make a new stencil | Drafter | New master + new stencil, registered in the archive |
| 4 Recall old version | **All working duplicates recalled and destroyed; recalled count = total ever issued (counted sheet by sheet)**; old stencil destroyed; old master stamped with a red "VOID" and moved to the obsolete-drawing area | Archive keeper + workshop supervisor | Recovery tally sheet |
| 5 First-article verification | Build the first batch of 3 pieces to the new version; release to production only after passing inspection | Workshop | Verification record filed in the ledger |

Step 4 is the step on which the whole system lives or dies. **Mixed old versions are the source of assembly accidents.** Walk it through: in March the pump body drawing advances to version B (hole spacing 220→240); five version-A duplicates still sit pressed in Workshop B's drawer, recalled by no one; in April Workshop B releases material and builds 10 pieces to version A; in May at Workshop A they are mated with version-B bases — not one hole lines up. Rework 40 person-hours, production idled waiting for parts, and in the accident investigation everyone can prove innocence: Workshop B built to the drawing, and the drawing says A in black and white. Prevention has only two hard measures: write the version letter in ink in the duplicate's upper-right corner as **permanent version lettering** (written in at duplication time, not a pasted label); and count recall against "issued = recalled," chasing a single missing sheet to a named person.

### 42.6.3 The Five-Item Accompanying Information: The Cross-Workshop Interface Standard

When two workshops hand over workpieces (blank → machining, machining → assembly, Workshop A building half and Workshop B the other half), the physical item must carry a Size-3 accompanying card with all five columns, none optional:

| # | Information | Content | Source |
|---|---|---|---|
| 1 | Measured dimensions | Key mating dimensions measured piece by piece: e.g., "hole φ20.08, φ20.11" | Chapter 22 gauges |
| 2 | Material batch | Furnace or batch number: e.g., "Chapter 18, heat 4-12" | Chapter 18, 38 ledgers |
| 3 | Heat-treatment state | State and criterion: e.g., "annealed; HB criterion see Chapter 19 Card 19-xx" | Chapter 19 |
| 4 | Inspection record | Inspector, criterion, result (go/no-go gauge pass/stop record) | Chapter 22 |
| 5 | Version number | Version letter of the drawing used to build it | This chapter |

This card is the direct answer to the review criticism that "metallurgy, machinery, and chemical engineering each pass on their own, yet with interface information missing nothing can be assembled or used": the iron is fine (furnace number traceable), the machining is fine (measurements on the card), and when assembly does not fit — put the two accompanying cards side by side, and whether the hole ran large or the shaft ran small, whether the problem is this heat or this drawing version, is located within five minutes. Without accompanying cards, every interface accident is an unsolved case investigated from scratch each time. The card travels with the part and joins that apparatus's archive after assembly.

[Card 42-03 Version Change Card] (eight fields)

1. **Input materials**: Change form (Size 3; five columns: drawing number / current version / what and why / affected parts list / proposer and date); parts lists of the affected drawings; gauge list (Chapter 22).
2. **Tools required**: Archive register; VOID stamp; recovery tally sheets; master-drawing scraping knives and bone folder (same set as Card 42-01).
3. **Operating sequence and control points**: (1) The change form must be complete; without the "affected parts list" it may not enter step 2. **(2) Dual sign-off: the Grade-3 process holder verifies the technical impact, the workshop supervisor verifies the inventory and production-schedule impact, and both sign in person.** (3) The drafter revises the drawing: advance the version, append one row to the revision table (append-only), and re-run the Card 42-02 nine questions on any datums and tolerances needing re-annotation. (4) Make the new stencil; destroy the old stencil on the spot. **(5) Recall: count the old-version duplicates sheet by sheet against the borrowing register and all issue records; after destruction, both parties sign the recovery sheet; any shortage freezes issue of that drawing number and triggers recovery.** (6) Build the first 3 pieces to the new version; release to production after passing Chapter 22 inspection. (7) Archive the three papers: change form, recovery sheet, verification record.
4. **Empirical parameters and calibration**: Full change process 0.5–1 day (empirical; calibration: the archive ledger logs time on each run; after five runs this settlement has its baseline). Stencil remake 1–2 person-hours.
5. **Process observation and recording items**: Change form number (format: drawing number – date serial), dual-sign-off time, recalled count versus issued count, verification batch inspection results.
6. **Pass / rework / scrap criteria**: Pass = all three papers complete + recalled = issued + verification batch acceptable. Rework = verification batch fails (rollback: restore the old parameters per the revision table and re-run the process — a rollback is itself a change; register it, never delete it). Scrap = the drawing revised without dual sign-off (that drawing version is void; the output is handled as an "unfinished process step" per Chapter 37 and may not be accepted).
7. **Common failures and troubleshooting order**: Assembly does not fit and the two workshops each insist they are right → first compare the accompanying cards' version numbers → then compare the measured dimensions → only then examine the process. Recall shortage → check the borrowing register for borrowed-but-unreturned sheets → check workshop drawers and drawings in use on the floor → check whether sheets were discarded together with scrapped parts.
8. **L1 / L2 / L3 evidence**: L1 = one change dossier completing all five steps (the three papers); L2 = an inventory record showing no old-version parts entering assembly in the month after the change; L3 = three consecutive months of archive "issued = recalled" counts with no gap + at least one recorded rollback handling.

**Change form template (copy with the card):**

| Column | Content |
|---|---|
| Drawing number / current version | |
| What changes (old value → new value) | |
| Why (defect / improvement / material substitution) | |
| Affected parts and workshops | |
| Proposer / date → dual sign-off → recovery tally → verification result | |

### 42.6.4 Four-Step Accident Tracing: How to Investigate an Old Part Built to an Old Drawing

When assembly finds an old part that "was built to the drawing but will not fit," investigate in fixed order — guessing before checking is forbidden:

1. **Read the title block**: drawing number + version letter — if the part carries an accompanying card (Section 42.6.3, column 5), read the version directly.
2. **Check the revision record table**: for that drawing number, work backward from the current version to the version and content of the last dimension change — "hole spacing 220→240" is the dividing line.
3. **Check the issue ledger**: which workshops received old-version duplicates over time and whether the recall count closes — the gap marks the old part's birthplace.
4. **Measure against the card**: measure the old part's key dimensions and compare with column 1 of the accompanying card. Inside the old version's tolerance band = a legitimate old part (disposition: scrap per the old version or retain as an old-version spare). Outside both versions = a manufacturing out-of-tolerance; open a separate quality case.

After the four steps, "whose fault" becomes "which version, which heat, which drawing" — the disposition targets the system gap (recall not closing), not the person. This is where the Chapter 37 accident-handling authority's "post-mortem examines the system" lands within the drawing system.

## 42.7 From Drawings to Photolithography Masks: Three Drafting-Side Conventions (Pre-Seeded)

Chapter 35's photomask plates and overlay alignment already cite "the Chapter 20 datum concept"; they still need this chapter to supply the drafting-side language. This section locks only three conventions; the process details (photosensitizing, etching, microphotography) belong entirely to Chapter 35 and are not expanded here:

**First, the enlargement-drawing system.** Mask layouts are drawn as enlargements at 5:1 or 10:1, then reduced to target size by microphotography. Three drafting rules: every annotated dimension on the enlargement equals the **final actual size on the photomask plate** (not the drawn length on the paper — the scale field reads "10:1, reduced to 1:1"); registration and line-width tolerances are likewise annotated as final values; the enlargement's sheet size = layout actual size x magnification, checked against the Section 42.4.1 sheet table (a 30×30 mm layout at 10:1 is 300×300, using a Size-0 sheet). Omitting annotations by "drawing it bigger and shrinking it" is forbidden — the microphotography distortion calibration (Chapter 35) rescues scale, not missing annotations.

**Second, black-and-white region definition.** Only two kinds of region are allowed on an enlargement: pure ink black (= the mask's opaque region) and pure blank (= the transparent region). Gray, diluted ink, and washes are all invalid — after reduction a gray region becomes uncertain transmission and the plate is ruined. Mask drawings therefore may not finalize directly from a charcoal draft; everything must be ink lines; filled black must be dense, verified by holding the sheet to the light with no mottling. Positive/negative conversion is handled in the Chapter 35 microphotography step; the drafting side always draws "opaque = black."

**Third, registration cross marks.** One cross at each of the plate's four corners and one at the center of the graphics area; cross lines 5–10 mm long (on the drawing), line width equal to the plate's finest line width; cross center spacing annotated datum-style (Section 42.3.1 — chain dimensioning is forbidden on mask drawings). The overlay criterion carries over from Chapter 35: the two plates' cross coincidence ≤ half the plate's finest line width (on the enlargement = that line width x magnification ÷ 2); no separate figure is created. Mask drawing numbers prefix an M to the ordinary drawing number and are **number-frozen in pairs with the process card** — Chapter 35's "changing one parameter = opening a new version; verbal changes forbidden" is carried by this chapter's Section 42.6 process.

## Parameter Master Table

| Parameter | Empirical value | Calibration method | Section |
|---|---|---|---|
| Thick line width | 0.5–0.7 mm | Reed pen edge width + magnifier comparison of same-batch test lines | 42.2.4 |
| Thin line width | 0.2–0.3 mm (thick-to-thin ratio ≥2:1) | Same | 42.2.4 |
| Hidden dash / gap | 3–4 / 1 mm | Scribe a sample length at the paper edge and follow it | 42.2.4 |
| Hatch spacing | 2–3 mm, 45° | Same | 42.2.2 |
| Dash-dot segment / dot gap | 15–20 / 2–3 mm | Same | 42.2.4 |
| Scale grades | 1:1, 1:2, 2:1 (masks add 5:1, 10:1) | Standard grades only | 42.2.3 |
| Sheet sizes | 450×600 / 300×420 / 210×300 / 150×210 | Reuse Chapter 41's four grades | 42.4.1 |
| Frame margin | 10 mm; binding side 20 mm | Measured with straightedge | 42.4.1 |
| Title block | 140×45 mm (Size 2 sheet), eight fields | A missing field = no release to the workshop | 42.4.2 |
| Untoleranced tolerance | ±0.5 mm (cast/forged part drawings ±1) | Written into the title block | 42.3.2 |
| Tolerance safety factor | ≥1.5x workstation capability band | First 20 pieces out-of-tolerance rate ≤5%; if exceeded, raise to 1.8 | 42.3.2 |
| Capability bands by process | Blank ±1–2 / file ±0.3–0.5 / turn ±0.1 / scrape ±0.05 / lap ±0.01 mm | Measured range over 5 pieces per workstation, transcribed to the ledger | 42.3.2 |
| Clearance fit (hole-basis, 20 example) | Hole +0.2/0, shaft −0.1/−0.25 | Clearance 0.10–0.45 | 42.3.3 |
| Hot-assembly expansion for interference fits | 20 mm hole heated to 200 °C ≈ 0.05 mm | Linear expansion 12×10⁻⁶/°C estimate + measured verification | 42.3.3 |
| Prick hole spacing | Straight: three points; arc: every 15°–20°; curve: 1–2 mm | First stencil pounced and compared with the master; densify where deviation exceeds 0.3 mm | 42.5.2 |
| Stencil life | 30–50 sheets | Remake when sampling exceeds limits | 42.5.2 |
| Duplicate error ceiling | ≤0.3 mm (5 sampled dimensions) | First piece per stencil + 1 in every 10 sampled | 42.5.2 |
| Paper moisture swelling | 0.5–1% | Stop duplication in rainy weather | 42.5.2 |
| Version letters | A→B→C; beyond ten revisions, full re-review | One form mandated archive-wide | 42.6.1 |
| Full change process | 0.5–1 day | Archive logs time each run; five runs set the baseline | Card 42-03 |
| Blueprint trigger line | Monthly drawing demand >50 sheets + three Chapter 23 batches of acceptable photosensitive salts | Both conditions simultaneously | 42.5.4 |

## Failure Modes and Diagnosis

Ordered from "most common → hardest to detect." The first three rows account for most drawing accidents; miscopied numbers and mixed old versions are the two most typical silent failures — the part shows no visible anomaly at all.

| Symptom | Candidate causes | Verification method | Disposition | Prevention |
|---|---|---|---|---|
| Second person cannot build a qualified part from the drawing | Missing dimensions / no datum / missing tolerance / views violating the mnemonic | Verify the drawing per the Section 42.6.4 four steps + Card 42-02 nine questions, item by item | Supplement the drawing and advance the version; run the Section 42.6.2 change process | L2 blind-build test included in acceptance |
| Two workshops each build half; the interface does not fit | Inconsistent datums (A measures from the machined face, B from the blank edge) or different nominal-size conventions for hole and shaft | Compare the interface drawings' datum definitions; measure both parts against the accompanying cards | Redefine a single datum on the interface drawing; both workshops re-sign | Single-point definition of interface dimensions + the five accompanying items |
| Assembly accumulates out of tolerance while every single part passes | Broken dimension chain: chain-style accumulation (Section 42.3.1 example ±0.8) or no free link left | Add the segments' upper/lower deviations in the worst direction and recompute the overall length | Switch to datum-style annotation; advance the version | Card 42-02 questions 2 and 3 |
| Duplicate lines distorted; parts out of tolerance | Prick spacing too sparse / paper moisture swelling / connected lines off the dot matrix | Sample 5 dimensions against the master; check the day's weather and the paper's dryness | Destroy that batch of duplicates; densify and remake the stencil or re-pounce in the dry season | Duplicate only on dry paper; stop work in rain; sample 1 in 10 |
| Numbers or signs miscopied (+0.2 as −0.2) | Duplication without read-back | Second person reads back character by character; compare with the master | Destroy the duplicates and recopy | "Read-back system" written into Cards 42-01/46-02 for execution |
| Old-version parts reach assembly; hole spacing does not match | Old-version recall not closed (Section 42.6.2 walkthrough) | Read the accompanying card version → revision table → issue ledger (Section 42.6.4) | Stop use; rework per the new version; chase the recall gap | Permanent version lettering + issued = recalled counting |
| Old part built from an old drawing (tracing mystery) | Broken information chain across version changes | The Section 42.6.4 four-step fixed order | Register and close the system gap; do not chase individual blame first | Revision table append-only; voided drawings archived, never burned |
| Drawing demands tolerances the machine tools cannot achieve | Tolerance with no source, copied from legacy drawings | Check the workstation capability ledger (range over 5 pieces) | Relax the tolerance, or add a scraping/lapping operation with the surface symbol | Tolerance ≥1.5x the capability band |
| Master drawing damaged or lost | Borrowed and unreturned / fire, water, insect damage | Archive ten-day inventory: drawings, stencils, register three-way match | Remake the master from the best off-site duplicate (version unchanged, marked "remade") | Masters never leave the archive + off-site disaster copy |

## Process Card Index

[Card 42-01] Three-view drawing card (card at end of 42.2) | [Card 42-02] Tolerance annotation card (card at end of 42.3) | [Card 42-03] Version change card (card at end of 42.6.3)

All three cards can be copied onto a single page and carry the full eight fields; 42-01 is posted at the drawing board edge, 42-02 in the drafting room, 42-03 travels with the change form.

## Acceptance Criteria L1/L2/L3

| Level | Criterion | Test conditions | Evidence retained |
|---|---|---|---|
| L1 | One Size-2 part drawing passing the five self-check questions and the nine tolerance questions; one pin-prick duplicate sampling ≤0.3 mm with zero read-back errors | All 12 pre-work verification items in place | Original drawing, duplicate, sampling records |
| L2 | **Blind-build test**: drafter A draws the full drawing set for a physical sample; builder B, who has never seen the sample, independently builds the part from the drawings (+ accompanying card) alone; B's part's measured values for all functional dimensions fall inside the drawing's tolerance bands. Also: the four-step change process completed once end to end (including a closed recovery count) | B and A may not communicate at any point; measuring tools calibrated and valid per Chapter 22 | **Comparison record table of drawing A versus measured part B** (dimension / drawing value / measured value / verdict, listed line by line) and the three change papers |
| L3 | Archive system running ≥3 months: ≥20 master drawings, no gaps in the borrowing register, ten-day inventories with drawings–stencils–register all matching, zero version mixing; cross-workshop handovers executing the five accompanying items with ≥2 qualified instances; ≥2 drafters at Grade 2 (Chapter 37 skill matrix standard) | Reproducible per records across personnel changes and season changes | Three months of inventory registers, accompanying card stubs, skill matrix assessment evidence, one stencil remake record |

The L2 blind-build test is this chapter's proof of existence: it measures "lossless transfer" directly — the drawings and accompanying card are all the information B possesses; a qualified B part means the language works, an out-of-tolerance B part means the drawing is deficient. Failing the first blind build is normal (empirically the first drawing omits 2–5 annotations); supplement, advance the version, retest, until one clean pass — framing that pass record would not be excessive; it is the settlement's birth certificate for cross-workshop collaboration.

## Labor Hours, Staffing, and Consumption

| Item | Staffing and duration (empirical) | Notes |
|---|---|---|
| Drafter training | 100–150 person-hours (about 20 drawings) to reach Grade 1–2; 6–12 months to Grade 2 | Cross-train from Grade-3 craftspeople with spatial imagination; literacy is a prerequisite (Chapter 4) |
| Medium part drawing | 4–8 person-hours | Including measurement, annotation, self-check |
| Subassembly drawing + parts list | 8–24 person-hours | A full medium-apparatus drawing set: 15–40 sheets, 80–150 person-hours |
| Stencil making | 1–2 person-hours | Life 30–50 sheets |
| Duplicates | 0.5–1 person-hour/sheet | Copyist trained and on the job in 0.5 day |
| Full change process | 0.5–1 day | Mostly the dual-sign-off meeting + recovery counting |
| Archive management | 0.2–0.3 person (part-time) | Ten-day inventories, registration, moisture checks (Chapter 41 cycle) |
| Drafting establishment | 1 drafter per 6–10 craftspeople | A 2,000-person town: about 3–6, including ≥2 at Grade 2 |
| Paper and ink unit consumption | Master archive startup: 50–100 sheets/month (drawing grade + folio) | Merged into the Chapter 38 materials account, planned jointly with ledger books |

## Safety Boundaries

This chapter has no high-temperature or high-pressure steps, but the following four items are part of the process steps; not executing them counts as not completing this chapter:

1. **Prick needle protection**: point the needle outward, the needle never leaves the board; when duplicating, work over a flat wooden board; holding the paper in mid-air while pricking is forbidden. On a prick wound: squeeze out the contaminated blood, rinse with clean water, compress and bandage; deep punctures are reported to the medic post (Chapter 37 medic establishment).
2. **Charcoal powder inhalation**: wear a mask when pouncing (same rule as Chapter 41), operate with the wind at your back, never tap the powder bag toward anyone's face; wash hands before eating after operations.
3. **Eyesight protection**: drafting and line work require daylight or ample lamplight; continuous fine-line work ≤2 h with long-distance gazing between sessions (per the Chapter 37 fatigue rules). Drafters hold one of the few posts in the settlement "whose means of production is their eyes"; losing eyesight is losing output.
4. **Archive fire safety**: concentrating drawings concentrates fire risk. No open flames in the archive; keep away from furnaces and kilns (straight-line distance through walls ≥15 m); lime dehumidifying cabinets away from every ignition source (Chapter 41 archive protection); the off-site disaster-copy system (Section 42.5.5) is the final backstop.

## The A/B/C Lists

**A list (executable directly by this chapter):**

| Item | Criterion |
|---|---|
| Drafter training and the three-view system | Card 42-01 five self-check questions; labor hours for 20 drawings entered in the ledger |
| Datum-style annotation and tolerance system | Card 42-02 nine questions all passed; every tolerance with a ledger source |
| Drawing number, version, and title block system | Drawings with any of the eight fields missing may not reach workshops (enforced by the archive) |
| Master archive and pin-prick duplication | Masters never leave the archive; duplicate sampling ≤0.3 mm + zero read-back errors |
| Four-step changes and the five accompanying items | Card 42-03 with all three papers complete; issued = recalled |

**B list (requires prior chapters' results):**

| Item | Prerequisite |
|---|---|
| Drawing paper and ink | Chapter 41 paper/ink capacity (drawing grade 450×600) |
| Straightedge, square, dividers | Chapter 20 geometric datums and flip cross-checks |
| Gauges and go/no-go inspection | Chapter 22 plug and snap gauges |
| Workstation capability band calibration | Chapter 20 machine tools and scraping/lapping |
| Magnifier line-width checks | Chapter 24 |
| Photomask enlargement conventions | Chapter 35 microphotography and overlay alignment |
| Dual-sign-off change system | Chapter 37, Section 37.6.3 |
| Furnace numbers and batches | Chapter 18 + Chapter 38 ledgers |

**C list (external dependencies and irreducible items):**

| Item | Notes |
|---|---|
| Blueprint chemicals | Until Chapter 23 delivers three acceptable batches, duplication tops out at stencil pouncing |
| Legacy modern drawings | Teaching material only; their tolerances and grades exceed this settlement's process capability — forbidden to copy straight down to workshops |
| Graphite / pine-soot gaps | Hard charcoal pencil line width caps one grade coarser; without pine soot, ink lines lose water resistance (a Class-C dependency knock-on from Chapter 41) |
| Hand-drawn precision ceiling | The 0.2 mm line width is the wall; finer graphics must take the Chapter 35 microphotography route |

## Downstream Dependencies

- **Chapter 35 (loop back)**: the three mask conventions (enlargement-drawing system, black/white region definition, registration crosses) get their language from Section 42.7 of this chapter — Chapter 35's "millimeter-level layout matching millimeter-level precision" thereby gains its drafting-side anchor; mask drawing numbers merge into this chapter's version-freeze system.
- **Chapter 43 archive system**: the master archive, borrowing register, revision records, accompanying card stubs, and obsolete-drawing area all merge into the Chapter 43 general archive — drawings are the densest information class in the archive system; **the negative-results clause is pre-seeded here: voided drawings and failed blind-build records are archive too — every detour the next generation will not have to walk is inside them.**
- **Chapter 22 standard parts album**: standard parts going without part drawings presumes the standard album is built — this chapter's drawing-number system reserves numbering space for it.
- **Whole-book loop**: Iron Law Six, "acceptance must retain evidence," and the Chapter 37 L3 record system now have the drawing as their medium: every chapter's process cards and every piece of equipment across the first forty-five chapters can be "drawn, toleranced, and versioned" — **the settlement that reaches this point truly possesses engineering technology that can be handed to the next generation, not just machines that make noise.**
