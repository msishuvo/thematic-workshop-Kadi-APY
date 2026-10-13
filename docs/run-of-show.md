# Run of Show

Total: **2 hours** = 90 min hands-on + 30 min discussion.

Guiding principles for this audience (zero to moderate Python):

- **Show the payoff first.** Open with the finished result, not with installation.
- **CLI before Python.** The CLI gives non-programmers an early win and shows
  that kadi-apy is not "only for coders".
- **Fill in the blanks, never type from scratch.** Every exercise is a
  prepared file with a few clearly marked `TODO` lines. Typos eat workshops.
- **One lab story throughout.** All exercises use the same scenario (a tensile
  test campaign on three steel samples), so each step builds on the last.
- **Always have an escape hatch.** Every exercise has a solution file; anyone
  who falls behind copies it and keeps going.
- **Unique names per person.** Kadi4Mat record identifiers are unique across
  the whole instance. Every participant uses their own prefix (e.g. initials,
  `jd-`) or 20 people will try to create `sample-s01` at the same time.

---

## 0:00 – 0:10 · Welcome and motivation (talk + demo)

- 2 min: who we are, helpers, how to ask for help (sticky notes: green = done,
  red/pink = need help, on the laptop lid).
- 3 min: **the pain.** Ask for a show of hands:
  - "Who has uploaded 20+ files to Kadi4Mat one by one?"
  - "Who has copied numbers from a results file into a metadata field by hand?"
  - "Who has a folder called `final_v3_really_final`?"
- 5 min: **live demo of the end result.** Run `exercises/solutions/03_batch_upload.py`
  on screen: in ~10 seconds, 3 sample records appear in Kadi4Mat with files,
  extracted yield/tensile strength as metadata, tags, links and a collection.
  Open the web UI and click through it. Then say: *"In 80 minutes you'll have
  written this yourself."*

## 0:10 – 0:20 · Setup check (hands-on)

Most setup should be done before the workshop (see
`participant-setup.md`). This slot is for verification and rescue.

1. Everyone runs `kadi-apy config get-kadi-info`.
2. Green sticky note if it works. Helpers go to every red one.
3. Common fixes:
   - Wrong host URL (must be the base URL, e.g. `https://kadi4mat.example.org`)
   - Token copied with a trailing space, or created without needed scopes
   - `kadi-apy` not on PATH → use `python -m kadi_apy ...` or reopen terminal
   - Corporate proxy / SSL issues → have participants use the prepared
     JupyterHub instead (see organizer checklist)

Facilitator tip: while people wait, show the Kadi4Mat web UI and explain the
3 concepts used today: **record** (one sample / one measurement), **collection**
(a project or campaign), **extras** (structured metadata: key, type, value, unit).

## 0:20 – 0:35 · Exercise 1: the CLI (hands-on)

File: `exercises/01_cli_basics.md`

Participants create a record, upload a file, add metadata and a tag,
entirely from the terminal. Takeaway: *"I can script this in a shell loop
or call it from any tool."*

Debrief (2 min): open the record in the browser. Ask: "When would the CLI
alone be enough for you?" (e.g. a nightly backup of an instrument PC folder).

## 0:35 – 0:55 · Exercise 2: first Python script (code-along)

File: `exercises/02_first_script.py`

Instructor types on a big font, participants follow. Explain only what is
needed:

- `KadiManager()` reads the config you created → "your login"
- `manager.record(identifier=..., title=..., create=True)` → "get or create"
- metadata is a list of small dictionaries: `key`, `type`, `value`, `unit`
- `record.upload_file(path)` → done

Python concepts introduced (just in time, nothing more): variables,
strings, dictionaries, a function call. Keep it at that.

## 0:55 – 1:00 · Break / buffer

Use it as a catch-up buffer. Helpers make sure everyone has a working
Exercise 2 (or copied the solution).

## 1:00 – 1:20 · Exercise 3: batch-upload a test campaign (hands-on)

File: `exercises/03_batch_upload.py`

The core "daily lab" use case. For every CSV in `data/tensile_tests/`:

1. create a record per sample
2. compute yield strength (0.2 % offset) and ultimate tensile strength
   from the CSV (the function is provided; participants don't write it)
3. store them as metadata with units
4. upload the raw CSV
5. tag it and add it to a collection for the campaign

Participants only fill in ~5 `TODO` lines. Introduce one new concept: the
`for` loop ("do this for every file in the folder").

Stretch goal for faster participants: link each sample record to a
"tensile test machine" record with `record.link_record(...)`.

## 1:20 – 1:30 · Exercise 4: find, download, plot (code-along)

File: `exercises/04_find_and_plot.py`

Search for all records with the tag from Exercise 3, print a small table of
their metadata, download the CSVs and plot all stress-strain curves into one
figure. Takeaway: *"Kadi4Mat is not just storage; my data comes back out
in a form I can analyse."*

Wrap-up (last 2 min): one slide with links (docs, this repo, support
contact) and "what to try tomorrow": replace `data/tensile_tests` with a
folder from your own instrument.

## 1:30 – 2:00 · Discussion (moderated)

See `discussion-guide.md`.
