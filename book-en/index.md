# The Civilization Restart Manual

How to walk from a single stone back to electricity, after industrial civilization breaks.

This book does not bet on whether collapse will come. It assumes one situation: a generation is left with land, stone, timber and fire, and nobody remembers how to turn those into tools. Fifty-six chapters in eleven parts, starting from building a measurement system and making fire, running through glass, iron and steel, electricity, paper and ink, medicine, and the institutions that hold a workforce together.

## How to read it

- Every procedure that can only be learned by doing is written as a **process card**. Each card has the same eight fields: input materials, tools required, operation sequence and control points, experiential parameters and calibration method, in-process observation items, accept / rework / scrap criteria, common failures and troubleshooting order, and L1 / L2 / L3 evidence.
- A card is meant to be copied onto one page and carried to the bench — chalked on a board, nailed to a wall, folded into a tool bag. There are 286 of them, one set in Chinese and one in English.
- Wherever a figure is experiential, the card says so and says it must be calibrated against local material. No invented precision.
- Field 8 of each card states what evidence that particular procedure has to produce before it counts as passed.

## What's inside

| Part | Chapters | Line |
|---|---|---|
| General constitution | G01–G04 | Iron laws, chapter framework, six technology lineages, dependency map |
| 1 | 1–4 | What restart means, reading the natural world, building measurement from nothing, how to use this book |
| 2 | 5–9 | The first stone tool, controlled fire, cordage and knots, containers, shelter |
| 3 | 10–15 | Food storage and agriculture, the first pot, kiln to high-temperature furnace, lime and cement, glass, textiles and leather |
| 4 | 16–23 | Reading ore, smelting, iron and steel, casting, machines, basic chemistry, saltpeter and gunpowder |
| 5 | 24–27 | Precision work, the birth of quantitative science, optical instruments, temperature/pressure/flow instruments |
| 6 | 28–36 | Heat engines, electricity, the first battery, lamps, vacuum tubes, semiconductors, radio |
| 7 | 37–40 | Production organization, material and energy accounting, maintenance, system governance |
| 8 | 41–43 | Paper, ink and writing surfaces, technical drawing and version control, archives |
| 9 | 44–49 | Trauma care, water and sanitation, materia medica, epidemiology, childbirth, occupational safety |
| 10 | 50–53 | Desert, island, cold country, epidemic |
| 11 | 54–56 | Roads, bridges and vehicles, telegraphy, the mathematics you cannot do without |
| Appendices | A–D | Dependency map and card master index, three-level acceptance table, safety red lines, terminology and units |

## Where to start

What you already have decides which line to read:

| Your situation | Start with |
|---|---|
| Nothing but open ground | Ch 1–4, then pick a line from the map in Ch 4 |
| Clay and a kiln, wanting vessels and brick | Ch 11–14 (pottery, glass, high-temperature furnaces) |
| Ore, wanting iron | Ch 16–19 |
| Needing precision, power and measurement | Ch 24–27 (precision manufacturing and instruments) |
| Needing electricity and communication | Ch 31–36, Ch 55 |
| Enough people that organization matters | Ch 37–40 |
| Records to keep, a next generation to teach | Ch 41–43 |
| Injuries and illness | Ch 44–49 |
| Desert, island, cold country, epidemic | Ch 50–53 |

## Repository layout

```
book/            Chinese text, 56 chapters in 11 parts + appendices
book-en/         English text, chapter for chapter
mkdocs.yml       Chinese site config
mkdocs-en.yml    English site config
assets/          logo
CHANGELOG.md     what changed in each edition
```

## Build the site locally

```bash
python3 -m venv .venv && . .venv/bin/activate
pip install mkdocs-material
mkdocs build                    # Chinese → build/site
mkdocs build -f mkdocs-en.yml   # English → build/site-en
```

## Status of this edition

Fifth edition (v5.0): 56 chapters, 11 parts, 286 eight-field process cards, Chinese and English chapter by chapter. Every technical parameter carries a source or an explicit calibration requirement; nothing was filled in to make a table look complete.

This is a snapshot, not a continuously updated site. Issues are welcome; revisions ship as new editions.

## License

CC BY-NC-SA 4.0 — read, share, adapt freely with attribution, non-commercially, under the same license.

## One caution

Some procedures here involve fire, furnaces, molten metal, electricity, explosives precursors, and medicines. They are written for a world without hospitals, regulators or suppliers — which is exactly why they carry red lines. Read the red lines in Appendix C before you do any of it.
