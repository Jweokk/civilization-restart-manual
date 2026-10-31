# 01 · Restart Conditions and Iron Laws (: Seven Laws)

> This document is one of the constitutions of the whole book. When any chapter conflicts with this document, that chapter shall be revised in accordance with this document.
> adds Iron Law Six and Iron Law Seven, and aligns the wording of the original five Iron Laws with the process card system (Document 02).

---

## 1. Restart Conditions: Where the Reader Starts

All ambiguity in technical routes stems from an unclear starting point. The book defines three starting points:

| Starting point | Initial conditions | Main challenge | Role in this book |
|---|---|---|---|
| A: Purely natural start | No tools, containers, clothing, or any artifacts | Survival and manufacturing from natural resources | Baseline verification line: Part Two is written to this standard |
| B: Limited leftover artifacts | Clothing, a few metal tools, and containers, but no way to replenish them | Use the existing tools to build a sustainable production system | Accelerated route: chapters are tagged with "leftover-artifact shortcuts" |
| C: Knowledge preserved | People remember modern scientific knowledge but have no modern industrial products | Convert knowledge into actual production capability | **Main line** |

Why C is the main line: the value of this book is not to let readers rediscover scientific laws, but to teach readers to rebuild the technology system in a realistically feasible order. But one distinction must be kept in mind at all times—

> **Knowing the principle of a technology does not mean possessing the ability to manufacture that technology.**

A person can describe precisely how integrated circuits work and still be unable to produce silicon wafers, fabricate fine patterns, deposit thin films, or test chips. The book distinguishes three levels for every technology:

1. **Knowledge comprehensible**: the reader can explain the principle.
2. **Technology reproducible**: the reader can manufacture it using available resources.
3. **Production sustainable**: the reader can repeatedly manufacture, test, and repair it, and replenish the tools and materials consumed.

The three must not be conflated. Chapter acceptance criteria must state which level is achieved.

---

## 2. The Seven Inviolable Iron Laws

### Iron Law One: No Tool Time Travel

No chapter may invoke a tool that has not yet been manufactured.

- The pottery chapter may not presuppose metal molds.
- The iron-smelting chapter may not presuppose modern blowers.
- The hand-forging chapter may not presuppose electric grinding wheels.
- The precision machinery chapter may not presuppose CNC machine tools.
- The early power-generation chapter may not presuppose modern insulating materials.
- The semiconductor chapter may not presuppose modern chemical reagents and precision instruments.
- The vacuum-device chapter may not presuppose matched-expansion sealing wire — sealing materials must either provide their own route or be explicitly listed as an external dependency.

If a tool is indispensable, you must first go back to the chapter that manufactures it. **Chapter numbering is the dependency order: Chapter N may only cite results numbered less than N.**

### Iron Law Two: All Precision Must Have a Source

You may not merely say "machine the parts to sufficient precision." You must explain:

- How is a dimension defined? (reference datum)
- How is a dimension replicated? (gauges, templates)
- How are two dimensions compared? (comparative measurement)
- How is error discovered? (inspection methods)
- How do you make a tool more precise than the tools you already have? (bootstrap routes, e.g. three-plate mutual lapping)
- How do you judge whether the precision meets requirements? (acceptance criteria)

Precision manufacturing cannot start from the lathe; it must start from straightedges, square references, marking tools, measuring gauges, standard parts, and error comparison — only then come scraping, lapping, reference surfaces, precision sliding pairs, thread cutting, and mechanical mother machines (machine tools). The book has only two legitimate sources of precision: **Chapter 3 (natural references and comparative measurement) and Chapter 20 (bootstrapping geometric references).**

### Iron Law Three: Every Material Must Have a Complete Chain

Writing "use steel" or "use glass" does not settle the matter. Every key material must be traceable:

> Natural resource → collection → sorting → primary processing → purification or smelting → forming → inspection → use

Iron ore is not iron; iron is not steel; and steel is not necessarily steel fit for pressure vessels. Sand is not optical glass; ordinary glass is not a qualified lens; silicon-bearing minerals are not semiconductor-grade silicon. **Every "equals" between two material names is a process chain that must be accepted on its own.**

### Iron Law Four: Every Technology Has Verifiable Success Criteria

"It looks like it came out right" is not acceptance. Acceptance criteria must state three things clearly: **what to measure, under what conditions to measure it, and what observation counts as pass/scrap.** Examples:

- Pottery: filled with water for 24 h, the level drops < 2 mm; 3 boiling-water → cold-water cycles without cracking.
- Ironware: a fractured test bar shows no large slag-inclusion layers; the spark test for carbon and the fracture grain structure corroborate each other.
- Lenses: can form a sharp image that can be observed repeatedly (resolution-target criteria, see Chapter 24).
- Steam engines: a hydraulic test at 1.5 times working pressure, held for 30 min without leakage — only then is operation discussed.
- Generators: "it spins but gives no electricity" must first pass the troubleshooting checklist (residual magnetism → windings → brush neutral plane, see Chapter 31); condemning it as scrap outright is not allowed.
- Integrated circuits: the specified logic functions are realized in independent testing, repeated across three batches.

Acceptance criteria must correspond to real use, not appearance.

### Iron Law Five: Every Key Technology Must Have a Fallback

The absence of one material must not interrupt the entire civilization route. An alternative route must state explicitly its **performance loss, resource cost, applicable boundaries, and final bottleneck**; the theoretical existence of a substitute does not license the claim that it can fully replace the original technology.

- No high-grade iron ore → which partial technologies can copper, wood, bone, and stone advance?
- Lacking lens raw materials → start with pinhole imaging, reflective observation, and simple measurement.
- No coal → charcoal, water power, wind power.
- No conditions for silicon chips → first build relay, vacuum electronic device, or germanium transistor routes.
- No matched sealing wire → carbon electrodes, transitional sealing with coarse lead wires, or demoting vacuum tubes to an external dependency (Chapter 33).

### Iron Law Six: Every Parameter Has a Calibration Method, Every Process Has Failure Criteria, Every Acceptance Preserves Evidence

This Iron Law is new in and targets "silent failure" — for smelting, annealing, winding, and vacuum processes, a mistake often does not fail at once but **fails invisibly**: what comes out is cast iron instead of wrought iron, looking almost identical; unannealed glass does not crack that day, then shatters on a hot plate three days later; a generator with miswired windings and one with insufficient residual magnetism show the same symptom, "it spins but gives no electricity." A reader without criteria will not know they are wrong; they will only think their luck is bad, and then repeat the same batch of scrap. Therefore:

1. **Parameters**: any "empirical value" must be written together with its field calibration method; a parameter without a calibration method is a placeholder and may not be used for acceptance.
2. **Failure criteria**: every process must answer "what does a botched job look like, and how do you verify where it went wrong"; the manual may omit a shortcut, but it may not omit a single failure mode.
3. **Evidence**: every acceptance leaves behind physical items (test bars, test coupons, failed parts) and written records (parameters, criteria, dates), filed into the ledger (Chapter 43). **A pass without evidence is not a pass; it is an impression.**

### Iron Law Seven: Labor Is the Primary Asset

Depreciation of equipment, furnaces and kilns, and power grids can all be rebuilt; the death or maiming of a craftsman cannot. Therefore:

1. In every chapter, the safety boundary ranks equal to the process itself: **for any step that can kill, maim, or cause chronic poisoning, safety measures are not "precautions" but part of the process steps**; skipping them counts as not completing the step.
2. Production planning must account for people: the minimum shift crew of continuous processes (blast furnaces, kilns, steam-engine tending) is written into the labor-hours block (Chapter 37); a process book written from a single-person perspective collapses at the second step.
3. Medicine, hygiene, and occupational health (Chapters 44–49) carry the same weight as metallurgy and machinery: they are the "human maintenance system," the only safeguard in the book that lets the reader live through a twenty-year horizon. Epidemics and silicosis kill a workforce faster than equipment wears out, and irreversibly.

---

## 3. Technologies Explicitly Excluded (Writing Them into the Book Would Turn It into Pseudoscience)

The following technologies are **not given manufacturing routes**; the relevant chapters only explain the reasons for exclusion and the conditions for future restoration. Readers who try to force them by the book will die:

| Technology | Reason for exclusion | Conditions for restoration |
|---|---|---|
| Vaccines, antibiotics, biological preparations | Require controlled culture, aseptic filling, batch testing, and a cold chain | Microscope + aseptic technique + strain library + assay system (Chapters 44–46 define the boundaries) |
| Electrolytic aluminum | Requires high-purity alumina, corrosion-resistant high-temperature electrolytic cells, and stable high current | Far beyond the "millimeter-scale handcrafted process" ceiling; aluminum is listed as an external dependency of this route |
| Tungsten filaments for incandescent lamps | The powder metallurgy, sintering, swaging, and wire drawing of tungsten are high-purity heavy industry | The carbon-filament route is usable (Chapter 33); tungsten filament is listed as a Class-C item |
| Marine chronometers and longitude determination | An independent precision-machinery tech tree that departs from the main line | Astronomical rough positioning is usable (Chapters 3 and 25) |

---

## 4. The Tool Lineage Concept: Every Tool Must Answer Four Questions

Both writing and reading check themselves against this:

1. What is needed to manufacture it?
2. How were those things manufactured in turn?
3. During manufacturing, which tools will be damaged, worn out, or need replacement?
4. If one of those resources is missing, can another route be taken?

Example — you may not merely write "use an iron chisel to work stone"; it must be traceable:

> Iron chisel ← usable iron stock ← reduction of iron ore and forging ← furnaces/kilns and charcoal ← refractory materials and temperature-control capability ← pottery kilns, fuel processing, and basic measurement

The iron chisel also needs: abrasives that allow repeated regrinding, a hand hammer to deliver impact, a fixture that holds the workpiece safely, a method for judging the edge condition, and the ability to re-heat-treat when necessary. **When a tool is damaged, the manual must state whether it can be repaired and what repair requires — not "replace it with a new one."**

---

## 5. From One-Off Fabrication to a Production System

Manufacturing one part ≠ building a system that can keep producing that part. In the acceptance criteria at the end of each chapter, the book separates "single-part success" (L1) from "system established" (L3). The minimum elements that sustain continuous production:

- Raw-material stockpiles and resupply routes (Chapter 38, materials ledger)
- Sustainable consumption rates for fuel/energy (Chapter 38, energy ledger)
- Tool wear rates and repair/replacement arrangements (Chapter 39, maintenance and spare parts)
- Process records (parameters, failure cases) (Chapter 43, archival system)
- Quality inspection methods (Chapters 22 and 27 + Chapter 39, quality traceability)
- Skilled labor and transmission (Chapter 37, labor organization; Chapter 43, master–apprentice system)

**The ceiling of a technical route is often set not by tools but by the scale of the division of labor.** This is also why the environment versions of Part Eleven evaluate the "labor and time" dimension.
