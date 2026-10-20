# Thematic Workshop: Kadi-APY for Everyday Lab Work

Hands-on workshop on using [Kadi-APY](https://gitlab.com/iam-cms/kadi-apy)
([documentation](https://kadi-apy.readthedocs.io/en/stable/)) to automate
routine data management tasks in [Kadi4Mat](https://kadi.iam.kit.edu/).

[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/msishuvo/thematic-workshop-kadiAPY/blob/main/notebooks/kadi_apy_workshop.ipynb)

- **Date:** Friday, 13 November 2026, 14:00-16:00 (CET)
- **Format:** online, 90 min hands-on and 30 min discussion
- **Environment:** Google Colab, Kadi4Mat at <https://kadi4mat.iam.kit.edu>

## Content

1. Finding functions and commands in the kadi-apy documentation
2. Connecting to Kadi4Mat from the command line and from Python
3. Creating records, uploading measurement files and adding metadata
4. Handling a whole test campaign with one script: records, calculated values
   (e.g. yield strength) as metadata, files, collections and record links
5. Searching records by tag, downloading the data and plotting it

## Agenda

One-page agenda for invitations: [docs/agenda.pdf](docs/agenda.pdf)

| Time        | Topic                                   | Content and use case |
|-------------|-----------------------------------------|----------------------|
| 14:00-14:10 | Welcome and demonstration               | Kadi4Mat terms (record, metadata, collection, tag) and a live demo of the final result: three specimens uploaded from a folder with one script |
| 14:10-14:20 | Part 1: Kadi setup check, kadi-apy documentation | Connection test; how to find and read functions and commands in the kadi-apy documentation |
| 14:20-14:35 | Part 2: command line                    | Create a record, upload a file, add metadata and tags with single commands; suited for quick one-off steps and shell scripts |
| 14:35-14:55 | Part 3: Python                          | The same steps in a Python script, e.g. to fill a record with metadata and files in one run; the basis for processing many files at once |
| 14:55-15:00 | Break                                   | |
| 15:00-15:20 | Part 4: automating a test campaign      | One script for a whole folder of result files, e.g. after a measurement series: records with calculated values (yield strength, ...) as metadata, uploaded files, a collection for the campaign and links between specimens and testing machine |
| 15:20-15:30 | Part 5: search, download, plot          | Find records by tag or metadata, download their files and plot the stress-strain curves, e.g. for a report or paper |
| 15:30-16:00 | Discussion                              | Own use cases of the participants, which kadi-apy functions would automate them, open questions |

Each part starts with a complete example, followed by a reference of the
functions used (with links to the kadi-apy documentation) and an exercise.

## Repository layout

```
notebooks/
  kadi_apy_workshop.ipynb  workshop notebook (Colab)
docs/
  agenda.pdf               one-page agenda
  agenda.html              source of the agenda PDF
  participant-guide.pdf    participant guide (setup checklist, basics, cheat sheet)
  participant-guide.html   source of the PDF
  participant-setup.md     setup instructions (Colab or local installation)
  kadi-apy-reference.md    functions and commands used, with documentation links
exercises/                 the same parts as scripts (example + exercise), for local use
  01_cli_basics.md
  02_first_script.py
  03_test_campaign.py
  04_find_and_plot.py
  tensile.py               reading and evaluating the tensile test files
  solutions/
data/
  tensile_tests/           example tensile test data (synthetic)
```

## Setup for participants

1. Create a personal access token in Kadi4Mat (Settings > Access tokens).
2. Open the notebook with the "Open in Colab" button above and save a copy
   (File > Save a copy in Drive).
3. Store the token as a Colab secret named `KADI_PAT` (key icon in the sidebar).
4. Run section 0 of the notebook.

Details: [docs/participant-setup.md](docs/participant-setup.md) and the
[participant guide](docs/participant-guide.pdf). Functions and commands used in
the workshop: [docs/kadi-apy-reference.md](docs/kadi-apy-reference.md).

## Updating the participant guide

Edit `docs/participant-guide.html` and print it to PDF in Chrome
(Print > Save as PDF, margins: none), or run:

```bash
chromium --headless --no-pdf-header-footer \
  --print-to-pdf=docs/participant-guide.pdf \
  docs/participant-guide.html
```
