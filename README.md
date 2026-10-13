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
4. Uploading a folder of measurement files and extracting values
   (e.g. yield strength) into metadata
5. Searching records by tag, downloading the data and plotting it

## Agenda

| Time      | Topic                                              |
|-----------|----------------------------------------------------|
| 0:00-0:10 | Introduction and demo                              |
| 0:10-0:20 | Setup check, using the kadi-apy documentation      |
| 0:20-0:35 | Part 2: command line interface                     |
| 0:35-0:55 | Part 3: Python                                     |
| 0:55-1:00 | Break                                              |
| 1:00-1:20 | Part 4: batch upload                               |
| 1:20-1:30 | Part 5: search, download, plot                     |
| 1:30-2:00 | Discussion                                         |

Each part starts with a complete example, followed by a reference of the
functions used (with links to the kadi-apy documentation) and an exercise.

## Repository layout

```
notebooks/
  kadi_apy_workshop.ipynb  workshop notebook (Colab)
docs/
  participant-guide.pdf    participant guide (setup checklist, basics, cheat sheet)
  participant-guide.html   source of the PDF
  participant-setup.md     setup instructions (Colab or local installation)
  kadi-apy-reference.md    functions and commands used, with documentation links
exercises/                 the same parts as scripts (example + exercise), for local use
  01_cli_basics.md
  02_first_script.py
  03_batch_upload.py
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
