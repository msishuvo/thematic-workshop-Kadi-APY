# Discussion Guide (30 min)

The goal is to turn "nice demo" into "I know what I'll automate first".
A loose Q&A tends to be dominated by 2-3 people; this structure keeps
everyone involved.

## 1. Think-pair (8 min)

Ask everyone to write down, alone (2 min):

> One repetitive data task from your lab week that annoys you.
> Which instrument / file type? How often? How many files?

Then discuss in pairs in breakout rooms (6 min): *Which parts of it could kadi-apy do?*
(creating records, uploading, extracting values into metadata, linking
samples to measurements, finding data later)

## 2. Collect and cluster (12 min)

Go through the pairs; each pair names one task. Write them in a shared document /
online whiteboard, grouped into rough clusters, for example:

| Cluster                       | Typical kadi-apy pattern                        |
|-------------------------------|-------------------------------------------------|
| Instrument output folder      | watch folder → upload + parse header → metadata |
| Sample tracking               | one record per sample, links to measurements    |
| Simulation runs               | create record per run, parameters as extras      |
| Reporting / publication       | search by tag/metadata → download → plot/export |
| Consistency across group      | Kadi4Mat templates + script that fills them     |

For 2-3 of the most common tasks, sketch live on the shared screen which
kadi-apy calls they would need (it's usually the same 5-6 calls from today).

## 3. Open questions and concerns (7 min)

Likely topics; have short answers ready:

- **"Is my token safe?"** Keep it in Colab secrets or the kadi-apy config
  file (`kadi-apy config set-pat`), never in scripts, notebooks or git; give
  tokens an expiry date and minimal scopes.
- **"What if the script runs twice?"** `create=True` with a fixed
  identifier returns the existing record instead of duplicating it;
  `upload_file(..., force=True)` replaces files.
- **"Can I use Colab for my real data?"** Colab runs on Google servers; check
  your institute's data policy first. The same code runs locally with
  `pip install kadi-apy`.
- **"Our instrument PC is offline / old Windows."** CLI on a lab PC with
  a scheduled task, or copy to a network share and upload from there.
- **"Can it import my existing data?"** ELN/RO-Crate import, JSON Schema and
  SHACL template import exist (`kadi-apy misc import-eln`, etc.).
- **"Where do I get help?"** Docs, the kadi-apy issue tracker, and your
  local contact / office hours.

## 4. Close (3 min)

- Each participant writes **one thing they'll try this week** in the chat.
- Announce follow-up: office hours, chat channel, repo link, feedback form.
