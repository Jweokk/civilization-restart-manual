# 02 · Chapter Framework and Process Card System ()

> This document is one of the constitutions of the whole book. The goal of the first-edition template was "complete structure"; the goal of is **forced executability** — it revises the defects exposed by the first edition: the template allowed every item to stay at the noun level (an A-list entry reading only "glass lampworking (Chapter 14)", acceptance criteria reading only "magnify at least 5x"), so the form was complete while the content remained a table of contents. makes "every process must deliver a process card filled with all eight fields" a hard rule: **if the eight fields cannot be filled, the process has not been thought through.**

---

## 1. The Three Tiers: Every Section First Declares Which Tier It Is

| Tier | Meaning | How to tell |
|---|---|---|
| Tier 1 | After reading, you know it exists | Can recite the step names, cannot recite the parameters and criteria |
| Tier 2 | Can follow it once and succeed by luck | If it works, cannot say why; if it fails, does not know where it went wrong |
| Tier 3 | Can manufacture repeatedly, judge acceptance, diagnose failures | A different person or a different batch of raw materials can still reproduce it from the records |

**The book's commitment for main-text processes is Tier 3.** A subsection that cannot reach Tier 3 must open by declaring "this section is Tier X" and state what is missing to move up a tier.

Mapping between the three tiers and the three acceptance levels (L1/L2/L3): L1 = Tiers 1–2 (the phenomenon has been seen); L2 = the manufacturing face of Tier 3 (qualified output can be produced repeatedly); L3 = Tier 3 plus the system face (raw materials, spare parts, records, transmission). The implementation system for L3 is in Chapters 37–39.

---

## 2. The Chapter Skeleton: Nine Blocks (fixed order; a missing block is disqualifying)

| # | Block | Content requirement | One-vote-veto counterexample |
|---|---|---|---|
| 1 | Capability boundary | What can be done, **what explicitly cannot be done**, what is an external dependency (named and entered into the C list) | Writing only what can be done |
| 2 | Pre-work verification | A check-box list. Each line says "confirm you have XX in hand; the criterion is XX," not "see Chapter X" | Pushing the pre-checks onto the reader to figure out |
| 3 | Materials list | Five items per material: identification standard (how to recognize it) / minimum specification (how poor it can be before unusable) / acceptable substitutes (and the performance loss) / signs of defective stock / quantity per piece | Only material names |
| 4 | Tools list | Three items per tool: source chapter / precision requirement / **pre-use calibration method** | Only the source chapter |
| 5 | Process steps | Three questions per step: what to do / to what degree (observable criteria) / how to roll back or salvage if done wrong | "then operate carefully" |
| 6 | Parameter table | All key parameters collected into one table; every empirical parameter carries a **field calibration method** (see §4) | Isolated numbers with no source |
| 7 | Failure modes and diagnostics | Table: symptom → candidate causes → verification method → disposition → prevention. **Sorted by "most common / hardest to detect"** | None |
| 8 | Acceptance methods | For L1/L2/L3 respectively: criteria + test conditions + evidence to be preserved (test bars, records, samples) | Target values without conditions |
| 9 | Labor hours, manpower, and consumption | Head count, skill tier, days, fuel and material unit consumption — supports production planning and the "is it worth doing" judgment | None |

The first edition's closing blocks (the three A/B/C lists, safety boundary, acceptance criteria, next-step dependencies) are all retained, in the same positions and written the same way; entries in the A/B lists must reach the density of blocks 3 and 4 of §2. The fifteen-module self-check table continues to serve as the writing-side checklist.

---

## 3. Process Cards: One Card per Process Topic

One card = one independently executable operation (e.g., "anneal a batch of glass", "quench a file blank", "scrape a pair of surface plates"). The main text explains why; the card explains how. A card can be copied out on its own and taken to the workstation; when it wears out, copy it again; when it changes, reissue it.

**The eight fields (uniform across the book; missing any one voids the card):**

| Field | What to fill in |
|---|---|
| 1 Input materials | For each: minimum specification, acceptable substitutes (with performance loss), quantity per run |
| 2 Required tools | Source chapter, precision requirement, pre-use calibration |
| 3 Operating sequence and control points | Numbered steps; the "to what degree" criterion for each step; key control points in bold |
| 4 Empirical parameters and calibration methods | Parameter value + how to set that value in the field (test bars, controls, gradient tests) |
| 5 In-process observation items | The colors / sounds / hand-feel / readings to be recorded, and in which column |
| 6 Accept / rework / scrap criteria | The three-way split: what counts as accept, what can be reworked (and how), what is scrap |
| 7 Common failures and troubleshooting order | For "multiple causes of the same symptom," give a verification order, not just a list of causes |
| 8 L1/L2/L3 evidence | What physical items and written records to preserve after acceptance at each level |

- Card number rule: `chapter number - sequence number` (e.g., 20-01). Card numbers are unique across the book; Appendix A carries the master index.
- Card length: 1–2 pages (about 1500–3000 characters). Failure to fill all eight fields = a downgrade declaration for that process; adjectives may not be used to fill the gaps.
- Hospital operating procedures, factory process cards, and flight checklists all have this structure — it is not a new invention; it is the industry baseline this book must meet.

---

## 4. Writing Rules for Criteria and Parameters

1. **Three elements of a parameter**: value + applicable conditions + calibration or verification method. Example: you may not write "annealing temperature about 500 ℃"; write "soda-lime glass annealing point 500–540 ℃ (empirical range); field calibration: take three pieces of glass from the same batch, treat them at 480/520/560 ℃ respectively, then drop them into 60 ℃ warm water — any that crack are below the lower limit."
2. **Criteria must be observable**: who, using what, seeing what counts as accept/scrap. Example: "lapping complete" fails; "spot-color inspection shows ≥ 20 contact points within a 25×25 mm area, evenly distributed, and any two of the three plates give consistent results in pairwise mutual lapping" passes.
3. **Silent failure first**: for processes where a mistake is not immediately visible (metallurgy, annealing, winding, vacuum, concrete curing), write "how to discover the mistake" before writing "how to do it right." For such processes, placing the failure-mode table before the steps is also not an error.
4. **The ◎ hand-feel marker**: steps that cannot be fully put into words (the feel of scraping, forging heat, blowpipe rhythm, thread-twisting tension) are marked ◎ and given two things: a practice method (how many repetitions, on what material) and misjudgment compensation (what measurable physical evidence replaces hand-feel: test bars, test coupons, weighing, templates).
5. **Three-way criteria**: accept / reworkable / scrap. A two-way split by default means there is no rework path and will tempt readers to force defective parts into service.

---

## 5. Numerical Discipline

1. The book is metric throughout: length in mm, mass in g, temperature in ℃, time in min/h; pressure uses both atm and mmHg (the conversion is given at first occurrence).
2. Every "about, roughly, approximately" must carry an order of magnitude: write "about 3 kg (±0.5)", not "a few jin".
3. Order-of-magnitude self-check: every calculated result is followed by a "reasonable-range check" (example: the computed airflow is 200 L/min; check: an adult's lung capacity is about 4–5 L, one bellows bag about 8–15 L; demanding 200 L per minute means 15–25 full compressions per minute — a single person can sustain that briefly but not through a full shift on watch; conclusion: this furnace needs a two-person rotation or a different bellows).
4. Transmission rule: all parameters marked "empirical value, must be field-calibrated" **must be transcribed into the ledger (Chapter 43) once calibration is complete**. The next generation may not work from memory; they may only consult the ledger. Losing the ledger counts as that process being demoted back to Tier 1.

---

## 6. Physical Layout of a Chapter (unified layout)

```
# Chapter X Chapter title
## Objectives of this chapter
## Capability boundary (Block 1)
## Pre-work verification (Block 2)
## X.1–X.n  Main subsections (Blocks 3/4/5 embedded; key operations insert [Process Card X-nn])
## Master parameter table (Block 6)
## Failure modes and diagnostics (Block 7)
## Process card index
## Acceptance criteria L1/L2/L3 (Block 8)
## Labor hours, manpower, and consumption (Block 9)
## Safety boundary
## The three A/B/C lists
## Next-step dependencies
```

---

## 7. Revision Order (execution plan for the rework)

The framework comes first; the main text is then rewritten in the **silent-failure-first** order: measurement (3) → machine tools (20) → steel (19) → iron (18) → high-temperature furnaces (12) → glass (14) → steam (28) → generators (31) → agriculture (10) → electronic devices (33), with the remaining parts to follow. The newly added Parts Eight, Nine, and Ten (production organization and system governance; knowledge carriers and transmission; medicine, hygiene, and occupational safety — Chapters 37–49) fill in the "human maintenance" and "knowledge carrier" blocks that were missing wholesale from the first edition.

---

## 8. Terminology Unification (book-wide usage)

**Process card** = **workstation card** = a numbered job sheet of the form "Card 20-01"; the three are the same thing: the main text calls it a "process card," posted at the workstation it is a "workstation card," and the numbering format is always "chapter number - sequence number." **Fixed blocks** = the five fixed closing subsections of every chapter (failure modes and diagnostics / process card index / acceptance criteria / safety boundary / next-step dependencies). **Preview** = a forward declaration that "this capability will be established in Chapter N"; preview items may NOT be used as existing (the determination method is in Chapter 4). **Downgrade declaration** = the explicit declaration at the start of a process that has not reached Tier 3.
