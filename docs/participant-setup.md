# Participant Setup (please complete before the workshop)

The short, printable version of this is the participant guide PDF
([participant-guide.pdf](participant-guide.pdf)), page 1.

We use **Google Colab**: Python in your browser, nothing to install. It takes
about 15 minutes. If anything fails, reply to the invitation with a screenshot
and we'll sort it out before the day.

## 1. Kadi4Mat account

Log in at <https://kadi4mat.iam.kit.edu>.

## 2. Create a personal access token (PAT)

A token is like a password for programs.

1. In Kadi4Mat, click your name (top right) → **Settings** → **Access tokens**.
2. Create a new token, name it e.g. `workshop`, and give it an expiry date
   a few days after the workshop.
3. Copy the token right away. **It is shown only once.** Never put it
   directly in a notebook or script you share.

## 3. Open the notebook in Colab

1. Open the notebook:
   [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/msishuvo/thematic-workshop-kadiAPY/blob/main/notebooks/kadi_apy_workshop.ipynb)
   and sign in with a Google account.
2. **File → Save a copy in Drive**. Work in your copy.
3. Click the **key icon** (Secrets) in the left sidebar → **Add new secret**:
   name `KADI_PAT`, value: your token. Switch on **Notebook access**.
4. Run the cells of section 0 with **Shift + Enter**, one after the other.
   In 0.4, change `"xy"` to your initials.

You're ready when you see: ✅ Ready, ✅ Connected, ✅ Your prefix is ...

---

## Alternative: run locally instead of Colab

Only if you prefer your own computer (e.g. for real lab data later).
You need Python 3.9 or newer.

```bash
pip install kadi-apy matplotlib

kadi-apy config create     # creates an empty config file (~/.kadiconfig)
kadi-apy config set-host   # enter: https://kadi4mat.iam.kit.edu
kadi-apy config set-pat    # paste your token

kadi-apy config get-kadi-info   # should print information about Kadi4Mat
```

Then download this repository (green "Code" button → "Download ZIP") and use
the scripts in `exercises/`.
