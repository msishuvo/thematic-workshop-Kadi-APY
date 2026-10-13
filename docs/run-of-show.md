# Run of Show (online)

Total: **2 hours** = 90 min hands-on + 30 min discussion.
Main material: the Colab notebook `notebooks/kadi_apy_workshop.ipynb`.
Participants keep the participant guide PDF open on the side.

Guiding principles for this audience (zero to moderate Python):

- **Show the payoff first.** Open with the finished result, not with setup.
- **CLI before Python.** The command line gives non-programmers an early win
  and shows that kadi-apy is not "only for coders".
- **Fill in the blanks, never type from scratch.** Every exercise cell has a
  few clearly marked `TODO` lines and a "Show solution" box below it.
- **One lab story throughout.** All exercises use the same scenario (a tensile
  test campaign on three steel samples), so each step builds on the last.
- **Always have an escape hatch.** Anyone who falls behind copies the solution
  and keeps going.
- **Unique names per person.** Kadi4Mat identifiers are unique across the
  whole instance, so every participant sets their own prefix (initials) in
  notebook cell 0.4.

## Online roles

| Role | Job |
|---|---|
| **Presenter** | Shares screen (Colab + Kadi4Mat tab), large font (browser zoom 150 %), live-codes |
| **Chat moderator** | Watches chat, answers quick questions, tells the presenter when many people are stuck |
| **Helpers** (1 per ~8 people) | Take stuck participants into breakout rooms, ask them to share their screen |

Agree on signals at the start: write **"done"** in the chat (or use the
"thumbs up" reaction) when an exercise is finished; write **"help"** in the
chat when stuck for more than 2 minutes.

---

## 0:00 – 0:10 · Welcome and motivation (talk + demo)

- 2 min: who we are, roles, the done/help signals, "cameras optional,
  questions welcome".
- 3 min: **the pain.** Quick poll (meeting poll or reactions):
  - "Who has uploaded 20+ files to Kadi4Mat one by one?"
  - "Who has copied numbers from a results file into a metadata field by hand?"
  - "Who has a folder called `final_v3_really_final`?"
- 5 min: **live demo of the end result.** In a prepared copy of the notebook,
  run sections 3 and 4 with the solutions filled in: three sample records
  appear in Kadi4Mat with files, extracted yield/tensile strength, tags and a
  collection, then the combined stress–strain plot. Click through the result
  in the Kadi4Mat tab. Then say: *"In 80 minutes you'll have done this yourself."*

## 0:10 – 0:20 · Setup check (hands-on)

Setup should be done before the workshop (participant guide, page 1). This
slot is for verification and rescue.

1. Everyone opens **their saved copy** of the notebook and runs section 0.
2. "done" in the chat when you see the three ✅ lines.
3. Helpers take everyone else into breakout rooms. Common fixes:
   - Secret not named exactly `KADI_PAT`, or *Notebook access* switched off
   - Token copied incompletely, or expired → create a new one
   - Working in the read-only original instead of the saved copy → *File → Save a copy in Drive*
   - Prefix still `xy` → cell 0.4 stops with a friendly message
   - No Google account / Colab blocked → let them follow along on screen
     and pair them with a helper; they can catch up with the local scripts later

While people wait, show the Kadi4Mat web UI and explain the three concepts of
the day: **record**, **collection**, **metadata** (key, type, value, unit),
as on page 2 of the participant guide.

## 0:20 – 0:35 · Section 1: the command line (hands-on)

Participants create a record, upload a file, add metadata and a tag, all
with `!kadi-apy ...` cells. Ask them to keep the Kadi4Mat tab open and
refresh after each step. Small self-made task at the end: add an `operator`
metadatum.

Debrief (2 min): "When would the command line alone be enough for you?"
(e.g. a nightly upload from an instrument PC folder).

## 0:35 – 0:55 · Section 2: first Python script (code-along)

Presenter types, participants follow. Explain only what is needed:

- `manager` = "your login" (created in setup)
- `manager.record(identifier=..., title=..., create=True)` = "get or create"
- metadata = a list of small dictionaries: `key`, `type`, `value`, `unit`
- `record.upload_file(path)` → done

Python concepts introduced just in time: variables, strings, dictionaries,
a function call (page 3 of the participant guide).

## 0:55 – 1:00 · Break / buffer

Camera-off break. Helpers check that everyone has a working section 2
(or has copied the solution).

## 1:00 – 1:20 · Section 3: batch upload a test campaign (hands-on)

The core "daily lab" use case. For every CSV in `data/tensile_tests/`:
create a record, evaluate the curve (yield strength by 0.2 % offset, tensile
strength, ...; the function is provided), store the results as metadata with
units, upload the raw file, tag it, and add it to a collection.

Participants fill in three `TODO` lines. One new concept: the `for` loop
("do this for every file in the folder"). Stretch goal for fast participants:
link every sample to a "tensile machine" record.

## 1:20 – 1:30 · Section 4: find, download, plot (code-along)

Search by tag, print a metadata table, download the CSVs and plot all
curves together. Takeaway: *"Kadi4Mat is not just storage; my data comes back
out in a form I can analyse."*

Wrap-up (last 2 min): links (in the chat too), and "what to try tomorrow":
upload a few of your own files to Colab and adapt section 3 (check your
institute's data policy first).

## 1:30 – 2:00 · Discussion (moderated)

See `discussion-guide.md`.
