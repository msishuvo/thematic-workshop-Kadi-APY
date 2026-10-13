# Thematic Workshop: Kadi-APY for Everyday Lab Work

A hands-on workshop for materials scientists on using
[Kadi-APY](https://gitlab.com/iam-cms/kadi-apy)
([docs](https://kadi-apy.readthedocs.io/en/stable/)) to automate routine
data management tasks in [Kadi4Mat](https://kadi.iam.kit.edu/).

- **Format:** 90 min hands-on + 30 min discussion (2 h total)
- **Audience:** materials scientists, zero to moderate Python experience
- **Goal:** participants leave with a working script they can adapt to their
  own lab data the next day

## What participants will be able to do

1. Connect to Kadi4Mat from the terminal and from Python
2. Create records, attach measurement files and add structured metadata
   **without clicking through the web UI**
3. Batch-upload a folder of measurement files, extracting key values
   (e.g. yield strength) into searchable metadata automatically
4. Find their data again by tag or metadata, download it and plot it

## Agenda at a glance

| Time        | Block                                     | Mode            |
|-------------|-------------------------------------------|-----------------|
| 0:00 – 0:10 | Welcome, the "why", live demo of end result | Talk + demo     |
| 0:10 – 0:20 | Setup check: token + connection           | Hands-on        |
| 0:20 – 0:35 | Exercise 1: the CLI, no Python needed     | Hands-on        |
| 0:35 – 0:55 | Exercise 2: first Python script           | Code-along      |
| 0:55 – 1:00 | Break / catch-up buffer                   |                 |
| 1:00 – 1:20 | Exercise 3: batch-upload a test campaign  | Hands-on        |
| 1:20 – 1:30 | Exercise 4: find, download, plot          | Code-along      |
| 1:30 – 2:00 | Discussion: "your lab, your workflow"     | Moderated       |

Full minute-by-minute plan: [docs/run-of-show.md](docs/run-of-show.md)

## Repository layout

```
docs/
  run-of-show.md          detailed timing, talking points, facilitator notes
  organizer-checklist.md  what to prepare and when (T-4 weeks to T+1 week)
  participant-setup.md    send to participants ~1 week before
  discussion-guide.md     structure for the 30 min discussion
exercises/
  01_cli_basics.md        CLI commands, no Python
  02_first_script.py      create a record, add metadata, upload a file
  03_batch_upload.py      upload a whole test campaign + extract metadata
  04_find_and_plot.py     search, download and plot
  solutions/              completed versions of the exercises
data/
  tensile_tests/          synthetic tensile test data used in the exercises
```

## Quick start (participants)

```bash
pip install kadi-apy matplotlib
kadi-apy config create          # enter host URL + personal access token
kadi-apy config get-kadi-info   # should print info about the instance
```

See [docs/participant-setup.md](docs/participant-setup.md) for details.
