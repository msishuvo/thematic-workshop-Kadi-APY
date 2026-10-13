# Organizer Checklist

## T-4 weeks: decisions

- [ ] **Choose the Kadi4Mat instance.** Prefer a test/sandbox instance (or a
      dedicated group on your institute's instance) so workshop records don't
      clutter production. Confirm with the instance admins that ~N new
      accounts and a few hundred records in one hour are fine.
- [ ] **Choose the Python environment.** In order of preference for this
      audience:
      1. A JupyterHub (or similar browser-based environment) with `kadi-apy`
         and `matplotlib` pre-installed. Zero installation, no admin rights
         needed, no proxy problems.
      2. Participants' own laptops with a simple `pip install` (needs a
         pre-workshop install check, see below).
      Avoid mixing: it doubles the troubleshooting.
- [ ] **Room:** power sockets for everyone, stable Wi-Fi, a projector that
      shows code readably (test font size from the back row).
- [ ] **Helpers:** 1 helper per ~8 participants. Helpers must have done all
      exercises themselves on the actual instance.
- [ ] **Registration form** with a short pre-survey:
      - Python experience (none / some scripts / regular)
      - Do you already have a Kadi4Mat account? Have you used it?
      - What kind of data do you produce? (instrument, file type, volume)
      - What annoys you most about data management today?
      Use the answers to tune examples and seed the discussion.

## T-2 weeks: materials

- [ ] Run every exercise and solution end-to-end on the target instance
      with the pinned kadi-apy version (record `pip show kadi-apy`).
- [ ] Verify search parameters in Exercise 4 (tag search) work on that
      instance's Kadi4Mat version.
- [ ] Prepare 5-8 slides max: motivation, 3 concepts (record / collection /
      extras), agenda, links. Everything else happens in the terminal/editor.
- [ ] Prepare a cleanup script (or ask admins) to delete workshop records
      afterwards, if using a shared instance.

## T-1 week: participants

- [ ] Send `participant-setup.md` and ask everyone to complete it and reply
      with the output of `kadi-apy config get-kadi-info` (or a screenshot).
- [ ] Offer a 30 min optional "install clinic" online 2-3 days before.
- [ ] Assign each participant a unique prefix (e.g. initials) for identifiers.

## Day of

- [ ] Arrive 30 min early; test projector, Wi-Fi, the demo script.
- [ ] Run the demo once and delete the result so it's fresh for the live demo.
- [ ] Have the repo URL and instance URL written on a board / first slide.
- [ ] Sticky notes (two colours), name tags.
- [ ] Have a few spare tokens / a fallback shared account ready in case
      someone's account doesn't work (only if your instance policy allows it).

## T+1 week: follow-up

- [ ] Send feedback form (3 questions: useful? pace? what next?).
- [ ] Share the repo, slides and a summary of the discussion outcomes.
- [ ] Offer office hours / a chat channel for people adapting scripts to
      their own instruments; those cases are your best future examples.
- [ ] Clean up workshop records on the instance if agreed.
