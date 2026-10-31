# Chapter 47: Disease Diagnosis, Case Records, and Epidemiological Investigation

## Chapter Objectives

After reading this chapter, the settlement should produce four documents; missing any one means this chapter is incomplete:

| Deliverable | Content | Purpose |
|---|---|---|
| One-page case record system | A register with fixed fields + three recording disciplines + a death-case review system | Lets any two cases be compared—only comparability reveals patterns |
| Three-major-syndrome triage tables | Recognition of the three syndrome classes (fever / diarrhea / respiratory), dehydration grading, isolation activation and escalation boundaries | The body of "diagnosis" in a lab-less era: treat by class, not by name |
| Outbreak investigation five-step method | Timeline → map → common factors → hypothesis and comparison → intervention verification | The complete route from "people falling ill en masse" to "cutting the transmission chain" |
| Weekly reports, alert thresholds, and cause-of-death registry | Weekly case tallies, abnormality alert criteria, death registration, and monthly mortality | The settlement's only dashboard of health status |

## Capability Boundaries

**Can do:**

- Establish a comparable case record system with fixed fields, paired with recording disciplines and the death review system.
- Triage of the three major syndromes (fever / diarrhea / respiratory), dehydration grading and oral rehydration indications, and linkage with the Chapter 49 isolation activation table.
- The five-step field outbreak investigation method: hand-drawn epidemic curves, pin maps, naive comparison groups, intervention and verification.
- Graded contact management and the observation-period system (experience values + field calibration).
- Weekly reports, alert thresholds, cause-of-death registry, and rough monthly mortality estimates.

**Cannot do (declared honestly):**

- **Pathogen identification and specific diagnosis.** On this route, "diagnosis" = syndrome classification + epidemiological judgment, both of which can be written down and verified. From start to finish this chapter never says "this is cholera, this is influenza"; it only says "watery diarrhea syndrome, point-source outbreak, evidence points to a certain well." Disease names are unobtainable, and treatment does not wait for a name—Chapter 49's general principle of "prepare for the worst case" holds equally in the domain of diagnosis.
- Individual prognosis and case-fatality prediction—only after-the-fact statistics, no before-the-fact divination.
- Autopsy and pathological examination—cause of death is determined only from pre-death syndrome records + external visual inspection of the body.
- Any lab test, microscopy, or imaging—none whatsoever, all counted on the C list.

**External dependencies (counted on the C list):** microscopy and pathogen testing systems (G01 exclusion table; recovery conditions in the boundaries of Chapters 44–46); water chemistry testing; specific disease names.

## Pre-Work Verification

Checklist format. If any item is not met, the corresponding system runs in degraded mode with the deficiency noted. Distance units follow Chapter 49's convention: 1 pace = 0.6–0.8 m (median from measuring 5 people; a marked pole as backup).

| # | Verification item | Criteria (confirm you have X, and that the standard is Y) |
|---|---|---|
| 1 | Paper-and-ink archive | Chapter 41 paper or equivalent register pages: writing stays clear overnight without bleeding; the Chapter 43 archive position has a moisture-proof storage place |
| 2 | Case register | The register from Section 45.9.3 is open: fields complete, no missing ten-day period—this chapter adds columns to it rather than starting a new register |
| 3 | Day counting and timekeeping | Day count continuous and error-free (cross-checked against the Chapter 3 water clock / sundial); dates for the last 90 days traceable |
| 4 | Temperature judgment | One working thermometer (Chapter 25), or the hygienist has passed ◎ four-grade hand-feel training (Section 47.3.1, 20 person-comparisons) |
| 5 | Settlement plan | Chapter 42 mapping method: marking every household's dwelling, each water source, latrines, cookhouse, isolation hut, prevailing wind direction |
| 6 | Population roster | Chapter 37 roster: every household's members and ages can be called by name; mid-month population can be looked up |
| 7 | Baseline data | Case registrations from the last 90 days (about one season) can serve as baseline—without a baseline, the alert thresholds (Section 47.6) cannot stand; idle-run to accumulate one season first |
| 8 | Measuring implements | A scale or a set of equal-volume spoons (Chapters 3, 22)—for oral rehydration mixing; weigh first, then measure (Section 47.3.3) |

## 47.1 Why "Disease Names" Are Worth Less Than "Case Records"

### 47.1.1 In a Lab-Less Era, the Essence of Diagnosis Is Pattern Recognition

The endpoint of modern diagnosis is one sentence: "What disease is this." Behind that sentence lies an entire evidence chain: microscopy, culture, lab tests. That chain does not exist on this route (G01), so the goal of diagnosis must change: **not to name the disease, but to set the course of treatment.** For the same patient, record the symptoms and signs (observable), the course (day-by-day trajectory), the contact history (where they went before illness, whom they saw, what they ate), the location (where they live, which water they drink), and the outcome (recovered, lingering, dead). With all six in hand, even if the disease name is never known, you know whom to isolate, which well to seal, which people to watch. Diagnosis here is a **craft of classification and traceback**, the same kind as a smith reading flame color to judge furnace temperature (Chapter 18): when direct measurement is impossible, judge from combinations of observable proxy features, write the judgment down, and accept after-the-fact testing.

### 47.1.2 The Three Traps of Naming Diseases by Single Symptoms

The review opinion called out this failure mode; expanded into three items, each of which can cost lives:

| Trap | Mechanism | Worked example |
|---|---|---|
| Same symptom, different diseases | The same symptom arises from entirely different sources, with different treatment paths | Both are "three days of fever": one case is a hand wound infection (Chapter 44: drainage and debridement), the other an intestinal disease (Chapter 45: water-service cutoff, rehydration). Once both are recorded as "fever illness" the two are treated alike—the latter keeps fetching water and helping in the cookhouse, and the transmission chain never breaks |
| Same disease, different symptoms | From the same exposure, different people show symptoms of different severity | In one well-water outbreak: some vomit and purge, some have loose stools only twice and keep working the fields, some feel nothing at all. Sorted by symptom into three names—"vomiting illness," "purging illness," "fine"—the common source is shredded by the names, and you cannot tell this is the same well |
| Taking an epidemic for sporadic cases | Cases scattered across many days of entries, each taken as an individual case | Twelve "diarrhea patients" spread over four days of register pages; each looks ordinary on its own. Plotted by onset date onto one time chart, a single peak stands up—this is one outbreak, not twelve coincidences |

The third is the deadliest: **the epidemic hides inside perfectly proper individual case records.** The only way to see through it is to make the records comparable and aggregateable—which is exactly what the next section's system aims at.

### 47.1.3 The Recording System Precedes Diagnostic Capability

Historical common knowledge [background]: modern epidemiological field investigation matured decades before etiology—nineteenth-century epidemic investigation relied precisely on case-by-case registration, arranging timelines by onset date, and pinning cases onto maps, locating waterborne outbreaks without ever having seen a single pathogen ("Snow's pump" is the exemplar of this craft). The implication for this route is fixed as follows: **diagnostic capability can wait for the laboratory (for decades); investigative capability cannot wait (the next rainy season is coming).** So the order must not be inverted: first establish the recording system (Section 47.2), then triage (Section 47.3), then investigation (Section 47.4). Chapter 45 already said "if that chapter does not register, Chapter 47 has nothing to consult"; this chapter adds the second half: **if records are written carelessly, consulting them is useless—comparability starts with fixed fields.**

## 47.2 The One-Page Case Record System

### 47.2.1 Field Table

One page = one case, one illness episode. Fields and their order are fixed, one format settlement-wide—the format itself is the source of comparability. Expanding the Chapter 49 register fields to thirteen columns:

| # | Field | What to record (criteria) | Common mistakes |
|---|---|---|---|
| 1 | Case number | Year–serial number (e.g., "Year 11–047"); one number per illness episode per person; a relapse gets a new one | Reusing the old number, conflating two episodes into one |
| 2 | Person | Name, age (years; under one year record months), sex, household number (matching the plan) | Age recorded as "old," "middle-aged" |
| 3 | Onset date | **The day the first symptom appeared**, not the report date—the whole timeline takes this as its axis | Recorded as the report date; the epidemic curve shifts right wholesale |
| 4 | Chief complaint | The patient's (or family's) own words, in quotes: "Griping belly pain, everything coming out is water" | Rewriting it as "dysentery"—once a diagnostic word enters the register, it contaminates the whole book |
| 5 | Signs (observable items) | Temperature grade (◎ four grades, Section 47.3.1); rash (location, morphology, **whether it blanches under finger pressure**); pupils (equal / unequal); dehydration degree (mild / moderate / severe, Section 47.3.3); whether the chin can touch the chest; other visually observed items | Recording unobservable sentences like "general condition acceptable" |
| 6 | Daily course record | One line per day: date / temperature grade / vomiting and purging counts / food intake / able to work or not—until the outcome | Only the first day recorded, the rest blank |
| 7 | Contact history | Within the pre-illness lookback window (intestinal 3–5 days; fever and respiratory 7–10 days; experience values in the parameter table): which **patients** were contacted (by name), which households visited, which meals eaten, which water drunk | Blank or "nothing special" |
| 8 | Drinking water source | Usual source + the one question "did you switch water before falling ill" (the rainy season often forces temporary switches) | Recording only the usual source, missing temporary water drawing |
| 9 | Outcome | One of three + date: recovered (day all symptoms gone and work resumed) / protracted (unresolved at a full 14 days) / death (date + main pre-death manifestations) | Left blank, never closed out |
| 10 | Disposition record | Isolation start and release dates, rehydration volume, medications (drug name / dose / days; continues the Chapter 46 trial records) | Isolation without recorded start and end |
| 11 | Recorder | Signature on every line—record quality traceable to a person | Unclaimed |
| 12 | Record date minus onset date | A separate column, for quality spot checks (the supervising ruler of the same-day discipline) | — |
| 13 | Review flag | Check mark on death cases—triggers the Section 47.2.3 review | Missed flag |

### 47.2.2 The Three Recording Disciplines

1. **Record the same day.** That evening before roll call, open pages for the day's new cases and complete the day's course line for every case on the books. The reason is the half-life of memory: after one day a third of the contact history is forgotten; after three days only "didn't go anywhere" remains. Late entries must be marked "late entry + date of late entry"; late-entered content may only be appended, never overwrite the original sentence.
2. **Record the original words, not diagnostic conclusions.** The chief complaint and course are written as spoken and as seen; the syndrome classification (Section 47.3) goes in the header classification box, not into the chief complaint. Once a diagnostic word enters the register, later comers simply repeat it and no one ever goes back to check the original words—the record is contaminated from then on.
3. **Sign.** Every page and every course line has a recorder. Traceability creates responsibility, and responsibility creates quality; the signature must be paired with the "no-blame" commitment in the next item, otherwise signing becomes a motive for concealment.

### 47.2.3 Mandatory Review of Every Death Case (No-Blame System)

For every death, before month's end the hygienist + one council member + the caregiving family member hold one review meeting (1–2 h), walking the whole course against the register: days from onset to death, delay in seeking care, gap between the isolation activation day and the first-case day (Section 45.7.1 convention), execution of rehydration and care, points to improve. The output is written into minutes and archived (Chapter 43); **every case review must land on at least one procedural change** (which table to change, which criterion, who executes).

The review principle is fixed: **look for holes in the system, not sins in people.** Under a blame system, families delay reporting and hygienists under-record, and the next death queues up as a result. Same logic as Section 37.6.2's "stop-work without blame; concealment is blamed": the review meeting's enemy is concealment, not error.

### 47.2.4 Physical Management of the Register

The case register is the settlement's least-losable paper (Chapter 45 / Chapter 43 conventions), with four rules: no page may be torn from the register—voided pages get an X and stay in the book; at each month's end transcribe one copy for storage elsewhere (the original travels with the hygienist, the copy goes into the archive cabinet); the transcriber signs and answers for the numbers, and when copy and original disagree the earlier one governs and the discrepancy is traced; rainy-season moisture protection—the register wrapped in oilcloth, hung on a rack, touching neither floor nor wall, ≥0.3 m off the ground (inheriting the same lesson as Chapter 49's beds-off-the-floor rule). Loss of a ledger is treated as that system dropping back to tier one (Iron Law Six), and for the case register this holds double: **a lost filter bucket can be rebuilt, but a twelve-year mortality curve, once lost, can never be re-recorded.**

[Card 47-01 Case Record Card] (eight fields)

1. **Input materials**: register paper (Chapter 41; criterion: writing stays clear overnight without bleeding), charcoal pencil or ink; one-page template (the thirteen columns of Section 47.2.1 copied as the grid, with the syndrome-class box and review flag left in the header). Substitutions and losses: without a template, rule the thirteen columns by hand in the same order, never reordered; per-use quantity: one page per case per episode, a new page for a recurrence.
2. **Tools required**: day-counting means (Chapter 3 water clock / sundial, cross-checked first); thermometer (Chapter 25) or the ◎ four-grade hand feel (Section 47.3.1, trained on a 20-person comparison); population roster (Chapter 37, for household number and age); oilcloth wrap and hanging rack for the register (≥0.3 m off the ground, touching neither floor nor wall). Calibration before use: thermometer checked by the Chapter 25 fixed-point method; hand-feel grades judged independently by two people, and on disagreement record "between hot and slight," taking the higher grade.
3. **Sequence and control points**: ① open the page the same day and fill columns 1–5 (case number / person / onset date / chief complaint / signs); **② the onset date is the day the first symptom appeared, never the report date**; ③ ask the contact history with four fixed questions, recording each answer as it is asked (at whose house did you eat these days before illness / which patient did you care for / which water did you drink / which places did you visit); ④ one line per day for the course, **finished before that evening's roll call**; ⑤ close out the outcome column with one of three (recovered / protracted at 14 days / died, with date); ⑥ flag death cases for review; ⑦ sign every line; ⑧ fill column 12, "record date − onset date," on the spot.
4. **Empirical parameters and calibration**: contact lookback window intestinal 3–5 days, fever and respiratory 7–10 days (empirical values); one case registered in 10–15 min and the daily course line in 2–3 min (labor conventions, Chapter 47 man-hour table); protracted judged at 14 days. Calibration: measure from this settlement's own register the "household first case → next case onset-date gap"; the modal value is this settlement's generation interval and the lookback window is taken at its upper bound—revised once per season and transcribed to the ledger (Chapter 43).
5. **Observations to record**: the thirteen columns themselves; the column 12 "record date − onset date" difference for every case; and a month-end count of four numbers—pages opened, pages closed out, pages still open, pages carrying a review flag—which must reconcile (a mismatch means missing entries, so go and find them).
6. **Pass / rework / scrap criteria**: pass = no empty column (write "unknown" when the answer cannot be obtained; blanks forbidden) + chief complaint in quoted original words + all signatures present + column 12 filled; rework = a disease name or an empty column appears—strike through, correct, date and sign; scrap = an entire page rewritten afterward from memory—the original stays on file marked "void," the rewrite marked "re-recorded."
7. **Common failures and diagnosis order** (most frequent first): ① contact-history columns identical across households (everyone copied one sentence) → switch to the fixed questions, asked one by one and household by household; ② course with missing days → dictated late entry by the household head marked "late entry + date," additions only, never overwriting the original line; ③ a disease name in the chief-complaint column → strike it out, restore the quoted words, keep the class word in the header box only; ④ outcomes never closed out → one month-end close-out and count; ⑤ onset date recorded as the report date → check the first course line of that case and whether the whole curve has shifted right.
8. **L1 / L2 / L3 evidence**: L1 = one complete sample page of a real case (retrospectively entered data acceptable); L2 = a 20-case spot check: same-day recording ≥90%, signatures complete, no disease names in chief complaints; L3 = a quarter with no missing ten-day period + every death review closed-loop + one recorder brought up to open pages independently to standard.

## 47.3 Three-Major-Syndrome Triage Tables (the Body of "Diagnosis" on This Route)

The general rule in one sentence: **classify by observable features; treat for the worst case.** The three classes cover the great majority of acute illnesses in the settlement; outside them set an "other" column (unexplained swellings, jaundice, convulsions without fever, etc.), registered separately—once 3 cases accumulate, run a small investigation per Section 47.4.

### 47.3.1 Four Temperature Grades (◎ Hand Feel)

Without a thermometer, or when thermometers fall short, judge the four grades by pressing the palm to forehead and chest:

| Grade | Palm-on-skin criterion (hold 2–3 breaths, about 10–15 s) | Corresponding magnitude (verify when a thermometer is available) | How recorded |
|---|---|---|---|
| Scalding | Unbearable on the forehead, immediate urge to pull the hand away | About ≥40 °C | "scalding" |
| Hot | Clearly hotter than oneself, tolerable | About 38–39.5 °C | "hot" |
| Slight | Slightly warmer than oneself; recheck on the chest | About 50.5–38 °C | "slight" |
| Normal / low | Same as oneself; low = cool with cold sweat | <37.5 °C | "normal" / "low" |

◎ This is a hand-feel step. Practice method: judge and judged first sit still for a quarter hour (to avoid misjudgment right after labor), palm to the forehead and to both sides of the chest once each, accumulating 20 person-comparisons—with a thermometer, check each time; without one, two people judge independently, and on disagreement record "between hot and slight," taking the higher grade. Misjudgment compensation: **better to report the higher grade than the lower**—triage activates by the higher grade; the cost of over-reporting is one extra day of isolation, the cost of under-reporting is Section 45.7.1's "watch two more days" (each day of delayed activation roughly doubles next-generation cases).

### 47.3.2 Fever-Class Triage Table

Fever is a symptom, not a diagnosis; split into four tracks by the signs that accompany it, each track given isolation activation criteria (continuing Section 45.7.1) and escalation boundaries:

| Syndrome | Recognition points (observable) | Isolation activation criteria (per Chapter 49) | Escalation boundary |
|---|---|---|---|
| Fever + rash | Scalding or hot grade + rash on trunk and limbs; **finger-pressure test**: press the rash spot with a fingertip—blanching means a red rash, non-blanching means petechiae (pressing with the Chapter 14 transparent cup works the same) | Petechiae = a single case counts as virulent, **isolate the same day, do not wait for a second case** (row one of Section 45.7.1); ordinary rash: single room until fever gone + 2 days | ≥2 cases of the same syndrome within 5 days → cluster activation; any petechia case → medic on site the same day |
| Fever + respiratory | Hot grade + cough, sore throat, shortness of breath | Single ventilated room until fever gone + 2 days; **a cook who falls ill stops at the stove immediately and is replaced** (Section 45.5.3) | Shortness of breath goes to the respiratory class below; ≥2 cases in one dwelling → whole-family observation (Section 47.5) |
| Fever + diarrhea | Hot grade + watery or bloody stools | Two-track handling: fecal-contamination track (Sections 45.3, 45.7.2) + rehydration track (Section 47.3.3) | Severe dehydration appearing → Chapter 48 emergency level |
| Fever + nervous system | Hot grade + neck stiffness (chin cannot touch the chest), severe headache, altered consciousness, convulsions | **A single case is already top grade**: single dim, quiet room, dedicated caregiver, report to the medic the same day; whole family listed for observation—the only track of the four where a single case triggers whole-family observation | Any new case → activate the full epidemic-period table (Card 45-03) |

### 47.3.3 Diarrhea-Class Triage Table

Deaths in diarrhea-class cases come almost entirely from dehydration, not from the "purging" itself—so the core of diarrhea-class "diagnosis" is **dehydration grading** and rehydration indications.

**Three-grade dehydration scale (observable criteria):**

| Grade | Observable criteria (check item by item) | Oral rehydration indication | Stop oral intake (transfer to Chapter 48) |
|---|---|---|---|
| Mild | Thirsty, slightly dry lips, slightly reduced urine | After each watery stool: adults 300 ml, under five 100–150 ml, drink up proactively | None |
| Moderate | **Sunken eyes**, slow skin-pinch recoil (◎ item below), dry mouth and tongue, markedly less urine, weakness | **75 mL/kg ÷ 4 h** (60 kg adult ≈ 4.5 L; children same formula), a small cup every 10–15 min with a dedicated person watching the drinking; re-grade dehydration every 1–2 h | Unstoppable vomiting (after emptying, rest 10 min and retry small sips; still vomiting after two tries) |
| Severe | Half a day without urine, drowsiness or impaired consciousness, cold limbs, thready weak pulse, deeply sunken eyes | Transfer to emergency care immediately | **Impaired consciousness = oral intake forbidden** (aspiration risk) |

◎ The skin-pinch test (pinch up the skin of the abdominal wall or the back of the hand, then release) is a hand-feel step. Practice method: on 3 healthy adults, practice pinching and recoil 20 times to build a memory of "flattens immediately"; on patients, two people judge together. Misjudgment compensation: count the recoil in breaths—pinch, release, **if flattening takes more than two breaths (about 4–6 s), record "slow recoil"**; do not decide by vague feel.

**Oral rehydration formula (experience value + calibration)**: per 1 L clean water + sweetener (honey or malt sugar, Chapters 10, 23) 40 g (about 3 level porcelain spoonfuls) + table salt 3.5 g (about half a level beer-bottle cap). Calibration: first weigh out 40 g and 3.5 g on the scale (Chapters 3, 22), then measure the actual capacity of the spoon and the bottle cap and graduate a dedicated measuring spoon—thereafter measure by the spoon, not by the shaking hand. Taste criterion: faintly salty, close to thin broth, drinkable; **distinctly salty-bitter = too salty, discard the whole batch and remix** (a high-sodium solution is dangerous for infants and small children; two-person check of every mixing).

**Sorting the three types of diarrhea:**

| Type | Recognition | Handling points |
|---|---|---|
| Watery | Thin watery stools, large volume, often with vomiting | Rehydration first; rehydrate for as long as the purging lasts; **no forbidding the purge, no anti-diarrheal drugs** ("stopping the purge" is on the Chapter 46 forbidden-trial list: the purge is the water-loss channel; forcibly stopping it without rehydrating is a double danger); fecal waste removed separately (Section 45.7.2) |
| Bloody | Stool with blood or mucus-pus, often with abdominal pain and fever | Handle on the "fever + diarrhea" two tracks; rehydration continues; report to the medic the same day |
| With vomiting | Vomiting and purging together | The rehydration difficulty is "keeping it down": small sips, doubled frequency, rest 10 min after vomiting and retry; two consecutive vomits = escalate |

### 47.3.4 Respiratory-Class Triage Table

| Syndrome | Recognition points | Handling and isolation | Escalation boundary |
|---|---|---|---|
| Cough (no fever or slight fever) | Cough, runny nose, sneezing | Stay home with ventilation (Section 45.6.1 low-in high-out), sleep alone, cover coughs with the arm (Section 45.8.3); no isolation, no work stoppage | A full 7 days of coughing without easing → register under the next row |
| Sore throat with fever | Hot grade + throat pain, painful swallowing | Single room until fever gone + 2 days; liquid food | White membrane behind the throat on opening the mouth, or labored breathing → medic the same day |
| Shortness of breath / wheeze | **Three signs of labored breathing**: cannot speak in full sentences, intercostal spaces sinking on inhalation, still wheezing at rest | Stop work immediately, semi-sitting position, ventilation, dedicated care—Chapter 48 emergency level | Any shortness-of-breath case listed separately in the weekly report (Section 47.6) |
| Chronic wasting lung disease (consumption-like) [background] | Cough with sputum **beyond half a month** without healing + wasting (belt gradually loosening, monthly weigh-in down more than 5%) + afternoon hot flashes or night sweats, or blood-streaked sputum | **Respiratory isolation (this class spreads by droplet; isolation works and is mandatory)**: separate ventilated room or upwind single room; cover the mouth when coughing and spit into an ash crock (Section 45.8.3); multi-layer cloth mask or turn the head away to cough; **separate eating utensils and cloths (red cord) and separate sleeping**; no sharing a room with small children; dwelling ventilated a notch above Section 45.6; family listed in observation registration; the dedicated register kept as usual | Heavy coughing of blood → Chapter 48 emergency; death → cause registered under the "chronic wasting" class (Section 47.7) |

[Background] Note on the label: the correlation of chronic wasting with crowding, darkness, and unventilated dwellings is historical experience; the mechanism cannot be verified on this route. But the engineering implications (ventilation, density, sputum etiquette) are executed as usual, not shelved because the mechanism is unclear—same convention as Section 45.6.4.

## 47.4 Field Epidemiological Investigation: The Five-Step Method (An Epidemic Detective's Handbook)

The five-step method runs through one worked case. **Base case: Lishu'ao, 118 people, 42 households; two water sources—the old east-village well (71 users) and the west-village mountain stream (47 users); one common cookhouse (Section 45.5 procedures in force). In a certain week of the third month a watery-diarrhea outbreak occurred, 12 cases in all.** Every step below walks through this base case.

Before starting, establish the **investigator's three principles** (each learned from failure). First, **speed**—the value of an outbreak investigation decays by the hour; lay out the case line list the same day as the first report; the later the interviews, the more completely the contact histories are forgotten. Second, **dirty data beat no data**—if it cannot be recorded precisely, record the interval ("the ninth or the tenth"); if the inquiry cannot be completed, mark "unknown"; blanks on the grounds of imprecision are forbidden. Third, **write conclusions to be refutable**—at the close of every investigation, put down one line: "most likely it is X; if Y appears, this is overturned," letting the next epidemic test this one's judgment. Investigation does not aim to be right the first time; it aims to be wrong in a way that can be seen.

### 47.4.1 Step One: Draw the Timeline (Hand-Drawing the Epidemic Curve)

Rearrange the register's cases into a line list by **onset date** (not report date), then draw a bar chart: horizontal axis one cell per day, vertical axis one cell per case, bars drawn up from the zero line.

**Peak-shape interpretation table (the language of curves):**

| Peak shape | Meaning | Criterion (experience value) | Treatment pointer |
|---|---|---|---|
| Single peak | Point-source outbreak (one common exposure) | All cases fall within a span no longer than the class's incubation ceiling (about 5 days for the intestinal class), steep rise and steep fall | Ask "what did everyone eat together in those days, which water did they drink" |
| Plateau / multiple peaks not falling | Continuous exposure (the contamination source is still there) | While the exposure remains, cases every day | Hunt the continuing source: the well, the cookhouse, an infected kitchen worker |
| Staircase (generation by generation) | Person-to-person transmission dominant | Peak-to-peak spacing ≈ one generation interval (measured; parameter table) | Main effort on isolation and contact management (Section 47.5) |

**Worked calculation (Lishu'ao)**: first case on the ninth of the third month (call it D0); D1 five cases, D2 four cases, D3 two cases; D4–D6 zero; 12 cases in all. The peak is at D1, and the whole-episode span of 4 days < the 5-day ceiling—**single peak, point source**. Back-calculate the exposure time: peak day D1 minus the intestinal class's common incubation of 1–3 days puts the exposure between D-2 and D0. Probing those days: on D-2 (the seventh) there was heavy rain. Clue noted; on to step two.

### 47.4.2 Step Two: Draw the Map (Pin Map)

On the plan (Chapter 42), one dot per case (multiple cases in one household drawn as a count of dots), then **trace and overlay three things onto it: water sources, latrines, cookhouse**. Clustering appearing at a glance is this step's normal output—the pin map's value is turning "can't see it" into "see it at once."

**Worked calculation**: 11 dots land on the households served by the old well; the stream-user area is clean. The twelfth case (a child of a stream household) hangs alone—probing found that on the rainy seventh he had played beside the old well's apron and drunk raw water. After tracing latrines and cookhouse, no clustering. **The map points at the old well.**

### 47.4.3 Step Three: Find the Common Factor (The Four-Question Table)

Run each case through the four questions, arranged as a matrix: same water source? Same meal (a public feast before illness, the same stove)? Same dwelling? Same-stove kitchen help? Once the four questions are answered, the common factor converges on its own.

**Worked calculation**: same water source 12/12 (including the child who drank raw water at the well apron); public feast 0/12 (checked the cookhouse records: no feast around the seventh); same-dwelling cases are only family clusters within 4 households, and their onset dates are later than the first case's—more like secondary spread than a common source. **The common factor converges on the old well.**

### 47.4.4 Step Four: Build a Hypothesis and Test It (Naive Comparison)

Write the hypothesis as one refutable sentence: "The old well water is contaminated; those who drink it fall ill." Test it by counting in groups—this is the lab-less era's "experiment":

| Group | People | Cases | Attack rate |
|---|---|---|---|
| Drank old-well water (including the child who drank raw water at the apron) | 72 | 12 | About 17% (one sixth) |
| Drank only stream water | 46 | 0 | 0 |

**Interpretation**: one group has one sixth falling ill, the other has zero of 46; if the source were the cookhouse (both groups eat there together), the stream households should not be clean—a difference this large cannot be explained by luck (experience judgment). Declare the limitation honestly: naive comparison is biased—well households and stream households may differ in other ways too (terrain, household type, livelihood), so the comparison only supports "most likely"; treatment still follows Chapter 49's general rule of the **worst case**: seal the well.

### 47.4.5 Step Five: Intervene and Watch the Curve (Intervention Is Verification)

**The intervention is executed the same day the hypothesis stands; do not wait for perfect evidence.** Worked calculation: on D3 itself—① the old well's apron sealed and covered, posted out of service, the backup source (the mountain stream) activated (Section 45.2.1); ② the whole settlement switched to boil-everything (Section 45.2.6; fuel passed through the Chapter 42 accounts first); ③ investigation found that the seventh's heavy rain had washed latrine-pit overflow from beside the well apron into the apron's hollow, and the old well had no raised apron lip (violating Section 45.2.5)—the latrine pit closed down and sealed over; ④ cases and household contacts graded per Section 47.5.

**Verification**: continue the curve daily for 7 days. D4–D6 zero new cases; on D7 two new cases appear—case A's wife and case D's grandson, both of whom cared for patients before falling ill and had no well-water exposure: **second-generation cases, a small person-to-person component**, contained by contact management; no second peak formed; the outbreak is judged cut off. Here one seductive sentence must be written out: **a point-source outbreak's curve falls back naturally on its own (a single exposure exhausts itself); the fall-back alone is not evidence the intervention worked; the evidence of success is "no second peak, no persistent plateau."** If cases continue daily after the well is sealed, return to step two—either the exposure was not cut, or the wrong thing was cut.

**After-action output** (within a week of the epidemic's end): the old well gets its complete three-piece set of apron lip, well cover, and public bucket (Section 45.2.5); the latrine pit is relocated (≥30 paces from water-draw points, Section 45.2.2); the event's full set of charts is filed into the ledger; the measured generation interval (first case D0 → second generation D7) is transcribed into the parameter table and the observation period corrected.

[Card 47-02 Epidemic Curve and Pin Map Drawing Card] (eight fields)

1. **Input materials**: case register (onset date, household number, address columns complete); settlement plan (Chapter 42, already marking dwellings, water sources, latrines, cookhouse, isolation house, prevailing wind); gridded paper (self-drawn grid: 1 horizontal cell = 1 day, 1 vertical cell = 1 case). Substitutions and losses: without gridded paper, rule the grid by hand on the back of the register with one straightedge for every cell—no eyeballing.
2. **Tools required**: straightedge (Chapter 3, length-compared against the standard rule); pins or charcoal dots; marked pole (Chapter 3, for distances); day-counting means. Calibration before use: compare the straightedge; verify one cell = one day after ruling; compute the axis start from the first-case date before putting pen down.
3. **Sequence and control points**: ① rearrange the case line list by **onset date** (not report date); ② draw the axes: horizontal from 2 days before the first case (keeping the exposure period in view), vertical from the zero line at 1 case per cell; ③ draw the bars day by day—**the sum of bar heights must equal the register's case count**; ④ interpret against the peak-shape table (single peak / sustained plateau / staircase) and write the conclusion in the footnote; ⑤ pin map: one dot per case, several cases in one household drawn as a count; **⑥ overlay-trace the three edges—water sources, latrines, cookhouse**; ⑦ the title carries all five items (event name, start and end dates, case count, draftsman, date).
4. **Empirical parameters and calibration**: axis start = first-case date minus 2 days (empirical, intestinal class); point-source criterion = whole-episode span ≤ that class's incubation ceiling (intestinal 5 days, fever with rash 14 days; empirical values); the stair-step interval uses this settlement's measured generation interval (from the 47.4.5 after-action, transcribed to the parameter table), never an outside value.
5. **Observations to record**: the footnote interpretation; the reconciliation record against the register ("curve 12 cases = register 12 cases, reconciliation done" plus the checker's signature); dot count and multi-case household counts; visible trace of the three overlaid edges; the five title items.
6. **Pass / rework / scrap criteria**: pass = counts reconcile + interpretation written in the footnote + all five title items + three edges overlaid on the drawing; rework = the report date was used (redraw) or one edge was omitted (trace it in and date it); scrap = bar count disagrees with the register and cannot be reconciled (void and re-investigate, original kept on file).
7. **Common failures and diagnosis order** (most frequent first): ① peaks shifted right wholesale → check whether the report date was used; ② no clustering visible on the pin map → check whether several cases in one household were drawn as one dot, and whether the water-source edge was overlaid; ③ staircase flattened → check whether days were merged by ten-day period (**must be drawn by day**); ④ counts do not reconcile → match case numbers one by one and look for missed or duplicated cases; ⑤ interpretation with no conclusion → a footnote that names the shape but not where it points is not an interpretation.
8. **L1 / L2 / L3 evidence**: L1 = one curve + one pin map (retrospectively entered data acceptable); L2 = a complete chart set for one outbreak whose interpretation matches the subsequent course; L3 = chart files archived with the epidemic + after-action minutes citing the originals + an apprentice drawing independently to standard.

[Card 47-03 Outbreak Investigation Five-Step Card] (eight fields)

1. **Input materials**: case register (onset date, household number, address); settlement plan (Chapter 42); population roster (Chapter 37); weekly-report baseline and alert table (Section 47.6); blank gridded paper (as Card 47-02); Card 45-03 (isolation activation) carried on the person.
2. **Tools required**: gridded paper, straightedge, marked pole (Chapter 3), day-counting means; interview sheets (the fixed four-question table); a means of keeping interview distance (≥1 pace, about 0.7 m, from the patient). Calibration before use: compare pole against pace rope (1 pace = 0.6–0.8 m, median of 5 people measured); reconcile the case count against the register before starting.
3. **Sequence and control points**: ① reconcile the case count the same day (bars = register); ② draw the timeline (Card 47-02); ③ draw the pin map and **always overlay the water-source edge**; ④ run every case through the four-question table (same water source / same meal / same dwelling / same cookhouse duty); ⑤ write the hypothesis as one refutable sentence ("the water of well X is contaminated; those who drink it fall ill") + run the naive comparison and compute attack rates; **⑥ execute the intervention on the day the hypothesis stands** (seal the source, boil all water, isolate, grade contacts—do not wait for a perfect comparison); **⑦ continue the curve daily for 7 days**, watching for a second peak and a plateau; ⑧ after-action minutes + ledger filing + correct the parameters from the measured generation interval.
4. **Empirical parameters and calibration**: comparison groups should each be ≥20 people (smaller groups are reference only, and must be labelled so); continued observation 7 days (corrected by the measured generation interval); incubation ceilings looked up per syndrome in the parameter table (intestinal 5 days, rash 14 days); exposure back-calculation = peak day minus 1–3 days of incubation; contacts traced two layers deep, and ≥3 cases among second-layer contacts means a new outbreak that runs this card again.
5. **Observations to record**: each step's output—case line list, curve, pin map, four-question matrix, comparison table (group / people / cases / attack rate), intervention order with the hour it was executed, 7-day continued curve. **A file missing any one of these is non-conforming.**
6. **Pass / rework / scrap criteria**: pass = all five-step outputs present + intervention on the day the hypothesis stood + continued curve on file + a closing line stating "most likely X; refuted if Y appears"; rework = a missing step is supplied (done, with date and who did it); scrap = conclusions resting on word of mouth with no chart and no table (not counted; redo).
7. **Common failures and diagnosis order** (most frequent first): ① skipping steps ②③ and guessing from impression → force the card's sequence to completion before concluding; ② waiting for "perfect evidence" before intervening → same-day intervention discipline; whether the comparison was biased is an after-action question; ③ forgetting the continued curve after the epidemic → step ⑦ fixed at 7 days, written into the after-action checklist; ④ exposed people mixed into the comparison group (only the usual water source asked, visits for a drink missed) → ask each person "where did you drink in the days before illness," regroup and recompute; ⑤ treating the curve's natural fall as proof of success → the proof is "no second peak, no sustained plateau" (a point-source curve falls on its own).
8. **L1 / L2 / L3 evidence**: L1 = one tabletop drill's complete file; L2 = one real or exercise outbreak's complete file (all five-step outputs); L3 = two complete files within a quarter + measured parameter corrections transcribed to the ledger + one independent investigator brought up (a different person walks the whole card).

## 47.5 Contact Management

### 47.5.1 Contact-Line Tracing Table

Contact definition (any one condition suffices): during the case's infectious period, having **lived in the same dwelling, eaten from the same stove, cared for the case (including delivering meals, feeding, cleaning fecal waste), shared a meal, or shared utensils, towels, or cloths** with the case. Infectious-period experience conventions: intestinal class from onset day until all symptoms gone + 2 days; respiratory class from 1 day before onset until fever gone + 2 days (experience values, corrected by measurement).

Tracing table fields: case number → contact person (name / age / household) → contact mode → last contact date → daily observation record (temperature grade + presence of vomiting, purging, cough) → fell ill or not → if ill, open a new case page immediately (Card 47-01) and **trace one more layer**.

Tracing depth is fixed: **trace two layers**—the case's contacts, and the contacts of contacts who fall ill. Unlimited tracing is infeasible in manpower; two layers already cover the great majority of secondary chains. If ≥3 cases of illness appear in the second layer, run Section 47.4 again as a new outbreak.

### 47.5.2 The Observation-Period System (Experience Values + Calibration)

| Syndrome | Observe from last contact | Basis and calibration |
|---|---|---|
| Intestinal class | 7 days | Experience value; corrected by this settlement's measured generation interval (Section 47.4.5), transcribed to the ledger |
| Respiratory class | 7–10 days | Same as above |
| Fever with rash | 14 days | Same as above |
| Fever + nervous system | 14 days | Same as above |

Observation period expires with no illness → close-out entry (date + signature).

### 47.5.3 Grading: "The Ill Are Isolated at Once; the Not-Yet-Ill Are Watched Diligently"

| Grade | Determination | Measures |
|---|---|---|
| Fallen ill | Any symptom of that syndrome appearing | Isolate immediately (Section 45.7.2), open a case page |
| Not ill · ordinary contact | No symptoms | Once-daily temperature grade + questions on vomiting / purging / cough; works as usual; must not cook, draw water, or care for small children and elders (same convention as Section 45.5.3) |
| Not ill · virulent contact | Contacted a "fever + rash / fever + nervous system" case | Two checks daily + restricted from public gatherings (no feasts, no leaving the village) for 14 days |
| Caregivers (including meal deliverers) | Fixed name list | The full Section 45.7.2 procedure + themselves listed for observation |

Deprivation too heavy breeds concealment—observation is not confinement; the right to work is retained (virulent contacts excepted). This item and the review system's "no-blame" belong to the same anti-concealment design.

## 47.6 Reporting and Alert System

### 47.6.1 The Weekly Report

On a fixed day each week the hygienist summarizes one page from the register: the week's case counts by syndrome (four fever sub-classes, three diarrhea types, four respiratory types, "other" listed separately), deaths, persons currently in isolation, persons currently under observation, and the **sick-leave-to-labor column** (person-days of work lost to illness that week, forwarded to the Chapter 41 shift table and the Chapter 42 accounts). Zero-case weeks still report "0"—an empty week and an unreported week are indistinguishable on paper, so zero must also be written. Weekly reports are transcribed monthly and archived under Chapter 43.

### 47.6.2 Alert Thresholds (Fixed in Advance, Not Debated on the Spot)

- **Baseline**: for each syndrome take the mean of weekly case counts over the last 12 weeks (about one season), drop the single highest week, and average the rest (to keep one old outbreak from inflating the baseline).
- **Multiple line**: a syndrome's weekly case count > 2× baseline → start an investigation within that week (at least completing steps ①②③ of Section 47.4).
- **Absolute line**: when the baseline < 1 case/week the multiple method fails; use instead—≥3 cases of the same syndrome in a single week is an alert.
- **Three hard alerts** (baseline ignored): any single "fever + nervous system" case; any single "fever + petechiae" case; any death of unknown cause. Any one of the three = report the same day, on site the next day.
- When an alert triggers, notify at once: the council, the cookhouse, and the Chapter 45 patrol line.

### 47.6.3 Linkage

One data source, many uses of one register: register → weekly report → alert → isolation activation (Section 45.7.1) → sick-leave-to-labor conversion (Chapters 41, 38). During an epidemic, sick leave's impact on output is counted weekly: sick-leave person-days × average daily work points (Chapter 37 convention) entered into the Chapter 42 accounts under a separate "epidemic cost" line—this is the settlement's on-paper basis for judging "is sanitation engineering worth the firewood and the manpower."

## 47.7 Cause-of-Death Registry and the Population Health Account

### 47.7.1 The Death Registration Form

Every death registered the same day: number (continuing the case number), name, age, sex, onset date, death date, **illness duration in days**, cause-of-death syndrome (recorded per the Section 47.3 classification, e.g., "diarrhea class · severe dehydration"—no disease name), main pre-death manifestations (verbatim), **pregnancy-related flag** (females 15–45 who were pregnant / gave birth / miscarried within the year before death get a check mark; details continue Chapter 52), **infant flag** (under 1 year flagged separately; under 28 days flagged again), disposition summary, registrar.

### 47.7.2 Rough Monthly Mortality Calculation

- **Monthly crude death rate** = deaths in the month ÷ mid-month population (the Chapter 37 roster base figure) × 1000‰ (per month); annualize by ×12.
- **Infant deaths counted separately**: deaths under 1 year among that year's live births ÷ live births × 1000‰ (the live-birth count continues the Chapter 52 birth-attendant registry).
- How to read it [background]: pre-industrial settlements' annual mortality often ran in the 20–40‰ range (historical common knowledge; an order-of-magnitude reference only). **The use is comparing with yourself**: this month against last month, against the same month last year, before and after sanitation-engineering changes—trend matters more than absolute value. After each engineering retrofit in Chapter 45 (well apron, filtration line, latrine relocation), the mortality curve should step down; if it does not, go back to Chapter 49 to check execution—not back to this chapter to change the numbers.

### 47.7.3 Why This Is the Only Dashboard

In an era without lab tests or disease names, the settlement's health status leaves only three measurable number groups: syndrome composition (who is sick with what), death rate (how severe the sickness), infant deaths (the condition of the most fragile group). Chapter 37 governs manpower, Chapter 38 governs materials; this chapter's page of numbers governs "how much margin remains in the human system"—it is simultaneously the parent source from which the Chapter 50 drug trials and the Chapter 53 occupational-disease registry draw.

**The account's rhythm**: in the first three days of each month the hygienist transcribes the previous month's three number groups onto one page and posts it at the council hall (numbers only, no names—Safety Boundary item 5); at each quarter's end the twelve months' mortality points are joined into one curve chart and archived. The point of numbers on the wall is not prettiness: let the whole settlement see that "the month after the well apron was fixed, the curve dropped," and the next time Chapter 49 asks for people to dig a ditch, no one will ask again "why spend the labor." The dashboard is not only for the hygienist to read; it is for the people who supply the labor to read.

## Parameter Summary Table

| Parameter | Experience value | Field calibration method | Section |
|---|---|---|---|
| Four temperature grades | Scalding ≥40 °C / hot 38–39.5 °C / slight 50.5–38 °C / normal <37.5 °C | ◎ palm-on-skin comparison over 20 persons; checked each time when a thermometer exists | 47.3.1 |
| Contact-history lookback window | Intestinal 3–5 days; fever and respiratory 7–10 days | Take the upper bound of this settlement's measured generation interval; revise each season | 47.2 |
| Oral rehydration formula | 1 L water + sweetener 40 g + salt 3.5 g | Weigh on the scale, then make the dedicated measuring spoon; taste "faintly salty, near thin broth"; salty-bitter means discard | 47.3.3 |
| Rehydration dose | Mild: after each purge, adults 300 ml, under five 100–150 ml; moderate: **75 mL/kg ÷ 4 h (weight method, same formula for adults and children)** | Entered in the disposition column and checked day by day | 47.3.3 |
| Skin-pinch recoil | Flattening in >2 breaths (about 4–6 s) = slow recoil | 20 trials against healthy adults + two judges together | 47.3.3 |
| Protracted determination | Unresolved at a full 14 days | Register course lines | 47.2 |
| Infectious-period convention | Intestinal: onset until all symptoms gone + 2 days; respiratory: 1 day before onset until fever gone + 2 days | Corrected by measurement | 47.5 |
| Observation period | Intestinal 7 days / respiratory 7–10 days / fever with rash and nervous system 14 days | Corrected by the measured generation interval, transcribed to the ledger | 47.5.2 |
| Tracing depth | Two layers; ≥3 second-layer cases of illness = treat as a new outbreak | Verified by drill | 47.5.1 |
| Point-source criterion | Whole-episode span ≤ incubation ceiling (intestinal 5 days / rash 14 days) | Curve comparison | 47.4.1 |
| Exposure back-calculation | Peak day minus 1–3 days of incubation | Curve + day-by-day probing | 47.4.1 |
| Comparison-group floor | Each group should be ≥20 people | If smaller, note "reference only" | 47.4.4 |
| Post-intervention observation | Continue the curve daily for 7 days, watching for a second peak and a plateau | Continued curve drawing | 47.4.5 |
| Weekly-report baseline | Mean of the last 12 weeks minus the highest week | Recomputed each season | 47.6.2 |
| Alert threshold | Weekly cases > 2× baseline; when baseline < 1 case/week, ≥3 cases in a single week | Checked against the weekly report | 47.6.2 |
| Monthly crude death rate | Deaths ÷ mid-month population × 1000‰ (monthly), annualized ×12 | Chapter 37 roster base figure | 47.7.2 |

## Failure Modes and Diagnosis

Ordered by most common and hardest to detect. This chapter's silent failures are mostly on paper: the numbers keep being filled in while the system has already gone idle.

| Symptom | Candidate causes | Verification | Remedy | Prevention |
|---|---|---|---|---|
| Records backfilled and distorted afterward (contact histories identical over large stretches) | Same-day discipline not followed; fixed questions never asked | Check the column 12 "record date − onset date" difference; compare whether households' contact histories are the same sentence | Revisit and re-ask the blanks (mark "late entry") | Registration before the daily roll call + signature system |
| Diagnosis-first contaminates the record (disease names in the chief complaint column) | The recorder wrote classification words into the chief complaint | Spot-check whether chief complaints are quoted verbatim | Strike through and add the original words + annotation | Print "record original words, not disease names" in the header |
| Investigation seeks only biological explanations (person-to-person), ignoring the water source | Skipped steps ②③ of the five-step method and guessed directly | Check whether the file lacks the pin map's water-source overlay | Go back and complete steps ②③ before concluding | Card 47-03 lists the water-source overlay as a fixed step |
| Alert thresholds numbed by "quiet times" (weekly reports stopped or copied verbatim) | Slackness after months without alerts | Randomly ask 3 members whether anyone was ill last week; check against the weekly report | File the missing reports + rebuild the baseline | Write "0" even in zero-case weeks + post weekly reports publicly |
| Curve peaks shifted right wholesale | Drew with the report date by mistake | Check the onset-date field definition | Redraw | Bold step ① of Card 47-02 |
| Exposed people mixed into the comparison group, diluting the attack rate | Asked only about the usual water source, missing water drunk while visiting | Re-ask each person "in the days before illness, where did you drink water" | Regroup and recompute | Ask the four-question table item by item |
| Contact list grows uncontrollably longer with each layer | Unlimited tracing | Check second-layer case counts | Cap at two layers; ≥3 cases = treat as a new outbreak | Depth fixed in Section 47.5.1 |
| Review meetings turn into blame sessions; late reports increase afterward | Reviews turned into blame assignment | Check whether the minutes point at "people" rather than "procedures" | Restate the no-blame principle; rewrite the minutes | The output must be a procedural change |

## Process Card Index

| Card | Name | Section | Purpose | Posted at |
|---|---|---|---|---|
| 47-01 | Case Record Card | end of 47.2.4 | Thirteen columns on one page + three recording disciplines + review trigger | Hygienist / medic workstation |
| 47-02 | Epidemic Curve and Pin Map Drawing Card | end of 47.4 | Curve drawing, peak-shape reading, three-edge pin-map overlay | Hygienist / council hall |
| 47-03 | Outbreak Investigation Five-Step Card | end of 47.4 | Five-step order, same-day intervention, 7-day continued curve | Carried by the hygienist |

## Acceptance Criteria L1/L2/L3

| Level | Criteria | Test condition | Evidence kept |
|---|---|---|---|
| L1 | The thirteen-column case record in use with one real, complete sample page; one hand-drawn epidemic curve (retrospectively entered data acceptable); one weekly report trial fill; the three-major-syndrome triage tables on the wall | Items passed on the spot | Sample page, curve chart, weekly report page |
| L2 | One real or drill **complete outbreak investigation file**: curve + pin map + four-question matrix + comparison table + intervention record + continued observation curve + after-action minutes, all five-step outputs present; spot-check of 20 cases with same-day recording rate ≥90% | A different person can still walk the full course by Card 47-03 | Complete file into the Chapter 43 ledger |
| L3 | One full quarter (≥12 weeks) of weekly reports with no gaps (zero weeks written as 0); a monthly mortality curve of three points joined into a chart; observation periods corrected by the measured generation interval and transcribed to the ledger; all death reviews closed-loop; one independent investigator brought up (passing the drill) | Quarterly audit | Weekly report files, mortality chart, ledger correction records, apprentice drill file, review minutes |

## Work Hours, Manpower, and Consumption

| Item | Manpower and duration (experience values) | Notes |
|---|---|---|
| Single-case registration (including contact-history interview) | 10–15 min/case | Executed by the hygienist |
| Daily course recording | 2–3 min per case per day | Done incidentally on rounds |
| Weekly report compilation | 1 person × 1 h/week | Transcribed and tallied from the register |
| Outbreak investigation (≤20 cases) | 2 persons × 2–3 days | Including charting and interviews |
| Curve + pin map | 0.5–1 h each per instance | Card 47-02 |
| Death review meeting | 3 persons × 1–2 h/case | Before month's end |
| Contact two-checks | 2 min per person per check | Virulent contacts checked twice daily |
| Staffing | A 300-person settlement: 0.5–1 hygienist (continuing Section 45.9.1, adding investigative-duty assessment) | Chapter 37 skill matrix |

## Safety Boundaries

> **Hard gate restated (implementing the Part declaration)**: wherever a medical card's criteria section in this chapter writes "beyond the boundary," all hands stop; treatment reduces to warming / rehydration / pain relief / attendance / recording (see the Part declaration in Chapter 44).

1. **The investigator entering sick households and epidemic zones**: follow Section 45.8's five moments + soap wash and change of clothes; interview at ≥1 pace (about 0.7 m) from the patient, no shared meals, no accepting kept-back food—the investigation itself must not become a transmission event.
2. **Autopsy forbidden**: cause of death is determined only from pre-death syndrome records + external visual inspection (no touching); suspected epidemic deaths are handled by dedicated personnel per Section 45.7.4, and the investigator only records.
3. **Two-person check of the rehydration formula**: an overly salty, high-sodium solution is dangerous for infants and small children; taste rule "salty-bitter means discard."
4. The rash finger-pressure test uses light fingertip pressure and the cup test light cup-wall contact—never break the skin.
5. Register use boundary: full names for investigation and statistics; **public posting reports numbers only, no names**—the price of one sick family being ostracized is the next family's concealment.
6. Virulent contacts' movement restrictions top out at 14 days; at expiry a review and close-out are mandatory—open-ended "observation" becomes detention, and detention breeds flight.

## A/B/C Three Lists

**A list (zero material threshold, executable directly in this chapter):**

| Item | Criteria |
|---|---|
| Thirteen-column case record system + three disciplines | Sample page passes, signatures present |
| Three-major-syndrome triage tables | On the wall + the hygienist can recite the four isolation activation criteria |
| Outbreak investigation five-step method | Card 47-03 carried on the person, one tabletop drill done |
| Two-layer contact tracing and observation-period grading | Tables on file, close-out system executed |
| Weekly report and alert threshold criteria | Weekly reports out every week, zero weeks written as 0 |
| Death registration and review system | Every case registered + review minutes closed-loop |

**B list (requires earlier chapters' outputs):**

| Item | Prerequisite |
|---|---|
| Paper-and-ink archive | Chapter 41 paper and ink + Chapter 43 archive system |
| Case register | Opened in Chapter 45, Section 45.9.3 |
| Plan and population roster | Chapter 42 mapping method + Chapter 37 roster |
| Isolation facility linkage | The full Chapter 45 set (carpentry and rammed earth from Chapters 7, 13) |
| Oral rehydration sweetener | Chapters 10, 23 honey, malt sugar |
| Thermometer | Chapter 25 (if absent, ◎ four-grade hand feel, with a degraded-mode declaration) |
| Timekeeping and measuring implements | Chapter 3 water clock and sundial + Chapters 3, 22 scales |

**C list (external dependencies and non-eliminable items):**

| Item | Notes |
|---|---|
| Pathogen identification and disease names | Require microscope + culture + identification system (G01 exclusion table; Chapters 44–46 give the boundaries)—this chapter replaces them entirely with "syndrome" language |
| Lab tests and specific diagnosis | Same as above |
| Vaccines and specific treatment | Same as above; treatment means stop at isolation, rehydration, and environmental intervention |

## Next-Step Dependencies

- **Chapter 48 Obstetrics and Infants**: the death registry's pregnancy-related flags and infant mortality statistics feed Chapter 48 directly; Chapter 48's birth registry in turn completes the case records' obstetric fields; the denominator of the infant death rate (the live-birth count) is defined by Chapter 48.
- **Chapter 49 Occupational Medicine**: Chapter 49's occupational-disease registry is a subset of this chapter's case records sliced along the "job-exposure" dimension—fields, disciplines, and weekly-report conventions all carry over from this chapter; only an exposure column is added.
- **Chapter 46 Drug and Dosage Trials**: this chapter's daily course records are the data source for Chapter 50's "drug effective / ineffective" observations—without daily records, Chapter 46's judgments have no basis; Chapter 46's medication must be backfilled into this chapter's disposition column.
- **Chapter 38 Energy and Materials Account**: epidemic-period sick-leave labor conversion and the boil-everything firewood consumption (Section 45.2.6) are entered into the accounts, with "epidemic cost" as a separate line.
- **Chapter 37 Labor Organization**: the hygienist's investigative duties enter the skill-matrix assessment; sick leave links with the shift table.
