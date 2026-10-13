# Organizer Checklist (online workshop)

## T-4 weeks: decisions

- [ ] **Kadi4Mat instance:** <https://kadi4mat.iam.kit.edu> (publicly reachable,
      so Colab can connect to it).
      - Clarify with the Kadi4Mat team how participants **without a KIT
        account** get access, and tell them in the invitation.
      - Workshop records are created on the production instance: they are
        private by default and carry the participant's prefix. Agree with the
        Kadi4Mat team whether that's fine, or whether they prefer a test
        instance or a cleanup afterwards.
- [ ] **Environment: Google Colab** (free tier is enough, participants need any
      Google account). Fallback for people who can't or won't use Google:
      local install + the scripts in `exercises/` (see `participant-setup.md`).
- [ ] **Meeting platform** with breakout rooms, polls and chat (Zoom, BigBlueButton, Teams, ...).
- [ ] **Roles:** presenter, chat moderator, and 1 helper per ~8 participants.
      Helpers must have done the whole notebook themselves.
- [ ] **Registration form** with a short pre-survey:
      - Python experience (none / some scripts / regular)
      - Do you have a Kadi4Mat account? Have you used it?
      - Do you have a Google account you can use for Colab?
      - What kind of data do you produce? (instrument, file type, volume)
      - What annoys you most about data management today?
      Use the answers to tune examples and seed the discussion.

## T-2 weeks: materials

- [ ] Run the **whole notebook in Colab** against kadi4mat.iam.kit.edu with a
      fresh Google account (no cached state), including the solutions.
- [ ] Check the token menu path in the participant guide (Settings → Access
      tokens) against the current Kadi4Mat UI, and which token scopes are needed.
- [ ] Create a short link to the Colab notebook, e.g. for
      `https://colab.research.google.com/github/msishuvo/thematic-workshop-kadiAPY/blob/main/notebooks/kadi_apy_workshop.ipynb`.
- [ ] Fill in the `[FILL IN]` fields in `docs/participant-guide/participant-guide.html`
      (date, meeting link, help e-mail, notebook short link) and regenerate the PDF.
- [ ] Prepare 5-8 slides max: motivation, three concepts, agenda, links.
      Everything else happens in Colab.
- [ ] Prepare a "demo copy" of the notebook with solutions filled in, logged in
      with the presenter's own token.

## T-1 week: participants

- [ ] Send the invitation with the **participant guide PDF** and the meeting link.
      Ask everyone to complete page 1 and reply with a screenshot of the three
      ✅ lines from section 0 of the notebook.
- [ ] Offer a 30 min optional online "setup clinic" 2-3 days before.
- [ ] Follow up personally with people who haven't confirmed setup.

## Day of

- [ ] Open the meeting 15 min early; invite people with setup problems to join then.
- [ ] Presenter: browser zoom ~150 %, notifications off, Colab and Kadi4Mat in
      two tabs, run the demo copy once to warm up.
- [ ] Pin links in the chat: notebook, participant guide PDF, Kadi4Mat.
- [ ] Pre-create a few breakout rooms named "Help 1", "Help 2", ...
- [ ] Decide whether to record (ask for consent; exclude breakout rooms).

## T+1 week: follow-up

- [ ] Send feedback form (3 questions: useful? pace? what next?).
- [ ] Share the repo, slides, recording and a summary of the discussion outcomes.
- [ ] Offer office hours / a chat channel for people adapting the notebook to
      their own instruments; those cases are your best future examples.
- [ ] Remind participants to delete or let expire their workshop tokens, and
      clean up workshop records if agreed with the Kadi4Mat team.
