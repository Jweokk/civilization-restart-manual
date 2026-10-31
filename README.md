# The Civilization Restart Manual

**From a single stone back to electricity.**

[中文说明](./README.zh.md) · [Read online](https://restart.fly2ai.top/) · [English edition](https://restart.fly2ai.top/en/)

56 chapters · 11 parts · 286 process cards · Chinese + English · CC BY-NC-SA 4.0

---

## What this is

A manual for one specific situation: a generation is left with land, stone, timber, ore and fire, and nobody remembers how to turn those into tools.

It does not argue that collapse will happen. It answers a narrower question — *if it did, and you had to start over with your hands, what would you actually do on Monday morning?* The answer is written as procedures, not as history or speculation: how to build a measurement system without standard tools, how to control fire, how to get from clay to a kiln to glass, from ore to a bloom to a knife, from a water wheel to a generator to a radio. It ends with the parts usually left out of survival books: keeping records, training a successor, running a clinic, organizing a workforce, and living in a desert, an island, or a cold country.

Every chapter follows the same skeleton: **what it is for → what you need → how to do it → how to tell it worked → what goes wrong and in what order to check → what evidence it counts as**.

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
| Appendices | A–E | Dependency map and card master index, three-level acceptance table, safety red lines, terminology, units |

## The process cards

This is the part the book is built around. Every procedure that can only be learned by doing is written as a **process card**: fixed eight fields, one page, meant to be copied out and carried to the bench.

1. Input materials
2. Tools required
3. Operation sequence and control points
4. Experiential parameters and calibration method
5. In-process observation items
6. Accept / rework / scrap criteria
7. Common failures and troubleshooting order (most frequent first)
8. L1 / L2 / L3 evidence

A real one, abridged — card 18-01, one bloomery run:

> **Input materials**: 20–40 kg of concentrate — grade ≥40%, particle size 5–20 mm, dry.
> **Tools required**: bloomery furnace (built and first-fired per card 18-03); bellows, two people alternating; rakes and tongs.
> **Sequence and control points**: ① ignite on a charcoal bed 200 mm above the tuyeres, gentle blast until it catches …
> **Experiential parameters**: ore-to-charcoal 1:1.5–2; 80–120 kg charcoal per run; steady-state consumption 20–35 kg charcoal per kg of dense iron.
> **Accept / rework / scrap**: pass = 1.5–3 kg dense forgeable bloom, slag running freely; rework = low yield but sound bloom; scrap = failed ignition or a furnace frozen with slag.
> **Failures, most frequent first**: ① won't light or heats slowly → wet charcoal, thin bed, weak blast …

Where a figure is experiential, the card says so and says it must be calibrated against local material. Nothing is filled in to make a table look complete — where the book does not know, it says it does not know, and gives the test that would settle it.

## Reading paths

| Your situation | Start with |
|---|---|
| Nothing but open ground | Ch 1–4, then pick a line from the map in Ch 4 |
| Clay and a kiln, wanting vessels and brick | Ch 11–14 |
| Ore, wanting iron | Ch 16–19 |
| Needing precision, power and measurement | Ch 24–27 |
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

## Edition policy

This is a **snapshot, not a living document**. There is no scheduled rebuild and no auto-update: the site you are reading is edition v5.0 and stays v5.0 until a new edition is cut. Corrections are welcome as issues and ship in the next edition.

## License

Text and figures: **CC BY-NC-SA 4.0** — read, share, adapt with attribution, non-commercially, under the same license. See [LICENSE](./LICENSE).

## One caution

Some procedures here involve fire, furnaces, molten metal, electricity, explosives precursors, and medicines. They are written for a world without hospitals, regulators or suppliers — which is exactly why they carry red lines. Read the red lines in Appendix C before you do any of it.
