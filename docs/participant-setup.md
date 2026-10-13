# Participant Setup (please complete before the workshop)

This takes about 15 minutes. If anything fails, don't worry: reply to the
invitation email with a screenshot and we'll sort it out before the day.

## 1. Kadi4Mat account

Log in to the workshop Kadi4Mat instance: `<INSTANCE URL>`

## 2. Create a personal access token (PAT)

A token lets scripts act on your behalf, like a password for programs.

1. In Kadi4Mat, open your user menu → **Settings** → **Access tokens**.
2. Create a new token, name it e.g. `workshop`, and give it an expiry date
   shortly after the workshop.
3. Copy the token and keep it somewhere safe. **You will only see it once.**
   Never put it in a script you share or commit to git.

## 3. Install kadi-apy

You need Python 3.9 or newer. In a terminal (Windows: "Anaconda Prompt" or
"Command Prompt"):

```bash
pip install kadi-apy matplotlib
```

## 4. Connect kadi-apy to Kadi4Mat

```bash
kadi-apy config create
```

When asked, enter the host (`<INSTANCE URL>`) and your token. This writes a
config file (`.kadiconfig`) in your home directory, so you don't need to put
the token in any script.

## 5. Test it

```bash
kadi-apy config get-kadi-info
```

If this prints information about the Kadi4Mat instance, you're ready.
Please reply to the invitation with the output (or a screenshot).

## 6. Get the workshop material

Download this repository (green "Code" button → "Download ZIP") and unzip
it somewhere you can find it, or `git clone` it.
