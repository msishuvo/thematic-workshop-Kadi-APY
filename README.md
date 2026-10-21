# Thematic Workshop: Kadi-APY for Everyday Lab Work

Hands-on workshop on using [Kadi-APY](https://gitlab.com/iam-cms/kadi-apy)
([documentation](https://kadi-apy.readthedocs.io/en/stable/)) to automate
routine data management tasks in [Kadi4Mat](https://kadi.iam.kit.edu/).

[![Open in GitHub Codespaces](https://github.com/codespaces/badge.svg)](https://codespaces.new/msishuvo/thematic-workshop-kadiAPY)
[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/msishuvo/thematic-workshop-kadiAPY/blob/main/notebooks/kadi_apy_workshop.ipynb)

- **Date:** Friday, 13 November 2026, 14:00-16:00 (CET)
- **Format:** online, 90 min hands-on and 30 min discussion
- **Environment:** VS Code in GitHub Codespaces (backup: Google Colab), Kadi4Mat at
  <https://kadi4mat.iam.kit.edu>

## Content

1. Finding functions and commands in the kadi-apy documentation
2. Connecting to Kadi4Mat from the command line and from Python
3. Creating records, uploading measurement files and adding metadata
4. Processing a folder of result files with one script: records, calculated values
   (e.g. yield strength) as metadata, files, collections and record links
5. Searching records by tag, plotting their metadata, downloading the data and plotting it

## Agenda

One-page agenda for invitations: [docs/agenda.pdf](docs/agenda.pdf)

| Time | Topic | Content and use case |
|---|---|---|
| 14:00-14:10 | Welcome and demonstration | Kadi4Mat terms and a live demo: three specimens uploaded with one script |
| 14:10-14:20 | Part 1: Kadi setup check, kadi-apy documentation | Kadi4Mat access; finding and reading functions in the Kadi-Apy documentation |
| 14:20-14:35 | Part 2: command line | Record, file, metadata and tags with single commands; for quick one-off steps |
| 14:35-14:55 | Part 3: Python | The same steps as a script; the basis for processing many files |
| 14:55-15:00 | Break |  |
| 15:00-15:20 | Part 4: automation | One script for a folder of result files: records with calculated values as metadata, files, grouped in a collection, and links to related records |
| 15:20-15:30 | Part 5: search, download, plot | Find records by tag, plot their metadata, download the result files and plot the measured data |
| 15:30-16:00 | Discussion | Your own use cases, which functions would automate them, open questions |

Each part starts with a complete example, followed by a reference of the
functions used (with links to the kadi-apy documentation) and an exercise.

## Repository layout

```
notebooks/
  kadi_apy_workshop.ipynb  workshop notebook (VS Code / Codespaces or Colab)
docs/
  agenda.pdf               one-page agenda
  agenda.html              source of the agenda PDF
  participant-guide.pdf    participant guide (setup checklist, basics, cheat sheet)
  participant-guide.html   source of the PDF
  participant-setup.md     setup instructions (Codespaces, own computer, Colab)
  kadi-apy-reference.md    functions and commands used, with documentation links
exercises/                 the same parts as scripts (example + exercise), for local use
  01_cli_basics.md
  02_first_script.py
  03_automation.py
  04_find_and_plot.py
  tensile.py               reading and evaluating the tensile test files
  solutions/
data/
  tensile_tests/           example tensile test data (synthetic)
```

## Setup for participants

1. Create a personal access token in Kadi4Mat (Settings > Access tokens).
2. Open the repository in GitHub Codespaces with the button above.
3. In the VS Code terminal, install and configure kadi-apy, as you would on
   your own computer:
   ```bash
   pip install kadi-apy matplotlib
   kadi-apy config create
   kadi-apy config set-host        # https://kadi4mat.iam.kit.edu
   kadi-apy config set-pat         # your token
   kadi-apy config get-kadi-info   # connection check
   ```
4. Open `notebooks/kadi_apy_workshop.ipynb`, select the Python kernel and run section 0.

Backup: open the notebook in Google Colab with the button above and store the
token as a Colab secret named `KADI_PAT`.

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
