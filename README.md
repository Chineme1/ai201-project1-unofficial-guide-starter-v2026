# The Unofficial Guide

<!-- Replace this line with your name and which corpus you picked. -->

> **This file is your submission.** Fill it in as you go — most sections get
> written during the milestone that produces them, not at the end.
>
> How the starter works, and every command you'll need, is in `RUNNING.md`.
> Leave that file alone.
>
> **Paste everything as text.** No screenshots, no video. A typed table gets
> full credit; a picture of the same table gets none.
>
> Delete these instruction blocks as you replace them. The `<!-- -->` comments
> are notes to you and don't show up when the page renders — you can leave them
> or remove them.

---

# Unit 1

## What This Does

<!-- Three or four sentences. Which corpus you picked, and the kinds of
     questions your system answers. Write it for someone who has never seen
     this repo.

     Milestone 5. -->

## Chunking Strategy

**Chunk size: 200**
**Overlap:**

<!-- What about YOUR documents made you pick these numbers? Short posts and
     long sectioned guides don't want the same chunking, and "800 seemed
     reasonable" earns nothing. Point at something you noticed when you read
     the documents in Milestone 1.

     If you changed your mind partway through, say so and say why. That's worth
     more than pretending you got it right first time.

     Milestone 3. -->

## Sample Chunks

<!-- Five chunks, pasted as text. Label each one and name the file it came from
     AND the function that produced it — the grader checks your code against
     what you claim here.

     `python app.py chunks -n 5` prints all three for you. Copy them straight
     across.

     Milestone 3. -->

**Chunk 1** — source: `admin_add_drop_deadline.txt#0` — produced by: `chunker.py::fallback_split`

```
You can add a course through the end of the second week. Dropping is a longer window — through the end of week six — but a drop after week two shows as a W on your transcript. Nothing anywhere on the registrar's site says this plainly, and students find out from each other.
```

**Chunk 2** — source: `course_biol_160.txt#0` — produced by: `chunker.py::fallback_split`

```
BIOL 160 Cell Biology

I lived here my sophomore year. Format is lecture three times a week with a weekly lab. Assessment: four unit tests and a cumulative final. Not curved.

Expect 9 to 11 hours a week, the heaviest first-year course by reputation.

The one piece of advice: the unit tests come fast, roughly every three weeks; falling behind once is very hard to recover from.
```

**Chunk 3** — source: `course_hist_118_workload.txt#0` — produced by: `chunker.py::fallback_split`

```
Workload for HIST 118 Modern World History

People keep asking so: a lot of reading, about 120 pages a week, but no problem sets. That's real time, not optimistic time.

It's front-loaded — the first month is heavier than the rest, partly because you're learning the format.
```

**Chunk 4** — source: `dining_pellew_dining_hall_followup.txt#0` — produced by: `chunker.py::fallback_split`

```
Re: Pellew Dining Hall

Adding to what people have said about Pellew Dining Hall. The wait figure of 12 to 18 minutes at peak matches what I've seen. If you're trying to eat between classes, go before 11:45 and it's a different building entirely.

Also worth saying: the furthest hall from anywhere, next to the athletics centre. Nobody tells you this at orientation.
```

**Chunk 5** — source: ` housing_innisfree_hall.txt#0` — produced by: `chunker.py::fallback_split`

```
Innisfree Hall — what it's actually like

Transferred in last year, so take this with a grain of salt. Built 1991, renovated 2022. Rooms are doubles arranged as pairs sharing one bathroom between two rooms.

The good: the shared-bathroom-between-two-rooms arrangement is the best compromise on campus.

The bad: no air conditioning, which matters for the first three weeks of September.

Laundry costs $1.75 wash, $1.75 dry, app-based. On noise: moderate; the building is L-shaped and the short wing is much quieter.

For each one, ask: could someone answer a question using only this,
without reading what came before or after?
```

## Sample Answer

<!-- One complete question and answer, pasted as text, with the source line
     visible. Milestone 4. -->

**Question:**

**Answer:**

```
```

**My relevance cutoff:**

<!-- The number you set in config.py, and how you got there.

     You ran five questions your corpus covers and the five in OUT_OF_SCOPE
     that it clearly doesn't, and wrote down the best distance for each. What
     did those two groups look like? Where was the gap? Put the actual numbers
     here — the table below wants all ten rows.

     Milestone 4. -->

| Question | In corpus? | Best distance |
|---|---|---|
|  |  |  |

## How I Used AI

<!-- Two specific moments. For each: what you asked for, what came back, and
     what you changed about it.

     "I asked Claude to write the chunking function from my notes. It ignored
     the overlap, so I added that myself" is the level of detail we're after.
     "I used AI to help me code" is not.

     Milestone 5. -->

**1.**

**2.**

<!-- ── Stretch features ─────────────────────────────────────────────────────
     Doing one? Say so here BEFORE you start. A feature this README never
     claims earns nothing.
     ───────────────────────────────────────────────────────────────────────── -->

---

# Unit 2

<!-- These sections get ADDED to what's already above. Don't delete or rewrite
     unit 1 — the point is that someone can see what you said before you knew
     how it went. -->

## Run Log — Before

<!-- Your five criteria, three runs each. `python run_eval.py --label before`
     runs the questions, puts the OUT_OF_SCOPE ones through the gate, and
     writes it all into results/ for you. Targets come from criteria.md; the
     verdict column is your call.

     Criterion 3 is measured in one deterministic pass rather than three, so
     the same number goes in all three run columns. That's correct, not lazy.

     Milestone 1. -->

 # | Criterion | Verdict | How I decided |
|---|---|---|---|
| 1 | Retrieved chunk contains answer | MET | [Target 4 of 5; runs were 4/4/4. Fewer than 4 in any run = MISSED.] |
| 2 | Every answer names a source | MISSED | [Target 2 of 5; any answer without a source = MISSED.] |
| 3 | Gate stops out-of-corpus | MET | Gate refused 5 of 5; it's deterministic, so the same count applies to all three runs, above the 4 of 5 target. |
| 4 | Answer whole in one chunk | MET | [Target 4 of 5; runs were 4 of 5.] |
| 5 | Answer contains expected fact | MISSED | Only 1 of 5 answers contained the expects phrase, in all three runs, far below 4 of 5. |

<!-- Underneath, paste the REAL output for each criterion from one of your
     runs — the actual text your system produced, not a description of it.
     Name the file and function that produced it. -->

## Verdicts

<!-- MET or MISSED for each of the five, against the target you wrote last
     unit — not a new one. Plus a sentence on how you decided. That sentence
     matters most where it was close.

     If your target said 4 of 5 and your runs came out 4, 3, 4, that's a MISS.
     The target has to hold, not show up occasionally.

     Milestone 2. -->

| Criterion | Target | Run 1 | Run 2 | Run 3 | Verdict |
|---|---|---|---|---|---|
| 1. Retrieved chunk contains the answer | 4 of 5 | 4/5 | 4/5 | 4/5 | MET |
| 2. Every answer names a source | 5 of 5 | 5/5 | 5/5 | 5/5 | MET |
| 3. Gate stops out-of-corpus questions | 4 of 5 | 5/5 | 5/5 | 5/5 | MET |
| 4. Answer sits whole in one chunk | 3 of 5 | 3/5 | 3/5 | 3/5 | FAIL |
| 5. Answer contains expected fact | 4 of 5 | 1/5 | 1/5 | 1/5 | MISSED |

Produced by `run_eval.py`, file `results/run_2026-10-03_0250_before.md`.

**Criterion 3 output:**
refused (best distance 0.838) What is the capital of Mongolia?
refused (best distance 0.871) How do I change the oil in a diesel engine?
refused (best distance 0.787) Who won the 1994 World Cup?
refused (best distance 0.769) What is the recommended dosage of ibuprofen for a headache?
refused (best distance 0.840) How do I write a for loop in Rust?
-> gate refused 5 of 5

**Criterion 5 output:**
Is it odd to go to office hours? — pass ×3 (best distance 0.343)
How often does the campus shuttle run? — fail ×3 (0.566)
What is the best time to get to campus? — fail ×3 (0.585)
What is the easiest class to take as a freshman? — fail ×3 (0.497)
What professor has the best ratings? — fail ×3 (0.594)

**Criteria 1, 2, 4 output:** [paste one question's retrieved chunks and answer from the results file]
## Diagnoses

**Criterion 5 (1/5):** All four failing questions passed the relevance gate (distances 0.497–0.594, under the 0.6 cutoff), so the gate isn't the cause. The one passing question matched at 0.343, much closer than any failure, which points to retrieval: no post closely matched the other four questions, so the model answered from loosely related chunks. [Confirm from results file: the expected fact was / was not in the retrieved chunks.]

**Pattern:** Three of the four failures ("best time to get to campus", "easiest class", "best ratings") are opinion questions with no single right answer. Even with good chunks, the model can give a reasonable answer that doesn't contain one specific expects phrase. This is one problem behind three failures: my questions, not just my pipeline.
## The Improvement

**What I changed:**

**Why I picked it:**

<!-- Connect it to a specific diagnosis above in one sentence. If you can't,
     you picked a fix because it sounded impressive. -->

### Run Log — After

**What I changed:** `config.py` TOP_K, 5 → 10.
**Why I picked it:** The failing questions had weak best matches (0.5–0.6), suggesting the relevant post may rank below the top 5. Retrieving more chunks gives it a chance to reach the model.

### Run Log — After
[same table, filled from the after file]

**Did it help?** Criterion 5 went from 1/5, 1/5, 1/5 to 3/5, 4/5, 5/5 (`results/..._before.md` vs `results/..._after.md`). [If unchanged: "No — the relevant facts weren't ranking 6–10 either, which suggests the corpus doesn't contain direct answers to these questions."]

**Did it help?**

<!-- Say plainly whether it did, and how you know. If it made things worse,
     say that — a change that backfired, honestly reported, earns full credit
     and is more interesting than one that worked. What matters is that you can
     tell.

     Milestone 4. -->

## What's Still Broken

Criterion 5 is still missed [if true]. Next I'd try hybrid search (BM25 + embeddings), since exact terms like "shuttle" may be getting lost in semantic search. I stopped because [I ran out of time / the opinion questions can't be fixed by pipeline changes alone].

## What I'd Do Differently

I'd rewrite my test questions and criterion 5 together. Three of my five questions were opinions ("easiest class", "best ratings"), so a single expects phrase couldn't judge them fairly. Next time every question would have one factual answer stated in a specific post, like the shuttle question, and I'd check that the fact exists in the corpus before writing it down.