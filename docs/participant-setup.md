# Participant Setup

Please complete these steps before the workshop. They take about 15 minutes.
A printable version is on page 1 of the [participant guide](participant-guide.pdf).
If something does not work, reply to the invitation e-mail with a screenshot
of the error.

## 1. Kadi4Mat account

Log in at <https://kadi4mat.iam.kit.edu>.

## 2. Personal access token

The token allows kadi-apy to access Kadi4Mat on your behalf.

1. In Kadi4Mat, click your name (top right), then Settings > Access tokens.
2. Create a new token named `workshop` with an expiry date a few days after
   the workshop.
3. Copy the token right away, it is only shown once. Do not paste it into a
   notebook or script that you share.

## 3. Google Colab

1. Open the [workshop notebook in Colab](https://colab.research.google.com/github/msishuvo/thematic-workshop-kadiAPY/blob/main/notebooks/kadi_apy_workshop.ipynb)
   and sign in with a Google account.
2. Save a copy (File > Save a copy in Drive) and work in your copy.
3. Click the key icon (Secrets) in the left sidebar, add a secret with the
   name `KADI_PAT` and your token as value, and switch on "Notebook access".
4. Run the cells in section 0 with Shift + Enter. In cell 0.4, replace `"xy"`
   with your initials.

The setup is complete when the output shows "Setup complete",
"Connected to https://kadi4mat.iam.kit.edu as ..." and "Prefix set to ...".

## Alternative: local installation

If you prefer to work on your own computer (Python 3.9 or newer):

```bash
pip install kadi-apy matplotlib

kadi-apy config create     # creates an empty config file (~/.kadiconfig)
kadi-apy config set-host   # enter https://kadi4mat.iam.kit.edu
kadi-apy config set-pat    # paste your token

kadi-apy config get-kadi-info   # prints information about the Kadi4Mat instance
```

Then download this repository (Code > Download ZIP) and use the scripts in
`exercises/`.
