# Participant Setup

Please complete these steps before the workshop. They take about 20 minutes.
A printable version is on page 1 of the [participant guide](participant-guide.pdf).
If something does not work, reply to the invitation e-mail with a screenshot
of the error.

The workshop uses VS Code in GitHub Codespaces. This is the same VS Code you
would use on your own computer, only in the browser, and the setup steps are
the same as on your own computer. Google Colab is the backup option.

## 1. Kadi4Mat account

Log in at <https://kadi4mat.iam.kit.edu>.

## 2. Personal access token

The token allows kadi-apy to access Kadi4Mat on your behalf.

1. In Kadi4Mat, click your name (top right), then Settings > Access tokens.
2. Create a new token named `workshop` with an expiry date a few days after
   the workshop.
3. Copy the token right away, it is only shown once. Do not paste it into a
   notebook or script that you share.

## 3. Open the workshop in GitHub Codespaces

1. Sign in to GitHub (a free account is enough).
2. Open <https://codespaces.new/msishuvo/thematic-workshop-kadiAPY> and click
   "Create codespace". VS Code opens in the browser with the workshop files.
   The first start takes a few minutes.

## 4. Install and configure kadi-apy

Open a terminal in VS Code (Terminal > New Terminal) and run:

```bash
pip install kadi-apy matplotlib

kadi-apy config create          # creates the configuration file ~/.kadiconfig
kadi-apy config set-host        # enter https://kadi4mat.iam.kit.edu
kadi-apy config set-pat         # paste your token

kadi-apy config get-kadi-info   # checks the connection
```

The token is visible while you paste it, so do not share your screen during
this step.

## 5. Open the notebook

1. Open `notebooks/kadi_apy_workshop.ipynb` in the Explorer on the left.
2. If VS Code asks to install the Python or Jupyter extension, click Install.
3. Click "Select Kernel" (top right) > Python Environments and choose the
   Python version in which kadi-apy was installed.
4. Run the cells in section 0 with Shift + Enter. In cell 0.4, replace `"xy"`
   with your initials.

The setup is complete when the output shows "Setup complete",
"Connected to https://kadi4mat.iam.kit.edu as ..." and "Prefix set to ...".

After the workshop, you can stop or delete the codespace at
<https://github.com/codespaces>.

## On your own computer

The steps are the same: install Python (3.9 or newer) and VS Code, download
this repository (Code > Download ZIP, or `git clone`), open the folder in VS
Code and continue with steps 4 and 5.

## Backup: Google Colab

If Codespaces does not work for you:

1. Open the [workshop notebook in Colab](https://colab.research.google.com/github/msishuvo/thematic-workshop-kadiAPY/blob/main/notebooks/kadi_apy_workshop.ipynb)
   and sign in with a Google account.
2. Save a copy (File > Save a copy in Drive) and work in your copy.
3. Click the key icon (Secrets) in the left sidebar, add a secret with the
   name `KADI_PAT` and your token as value, and switch on "Notebook access".
4. Run the cells in section 0. In Colab, the setup cell installs kadi-apy and
   writes the configuration file from the secret.
