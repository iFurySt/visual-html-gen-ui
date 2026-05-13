## [2026-05-13 14:46] | Task: Polish gallery scroll restore

### Execution Context

- Agent ID: `codex`
- Base Model: `GPT-5`
- Runtime: `local CLI`

### User Query

> Fix the visual jump where refreshing a hashed domain first lands around another section before moving to the target, and reduce side-to-side wobble in the floating domain tag bar during fast scrolling. Verify with OBU.

### Changes Overview

- Area: `index.html` gallery generation
- Key actions:
  - Disabled browser scroll restoration for the gallery and added a short hidden hash-restore state while the target domain is aligned.
  - Replaced delayed forced hash realignment with immediate alignment plus a zero-delay verification pass.
  - Kept the active domain tag locked during programmatic smooth scrolling so scroll events do not briefly select the previous section.
  - Made the sticky domain tag bar geometry stable by removing negative margins, removing padding transitions, and keeping one padding size for stuck and unstuck states.
  - Updated gallery validation to enforce the new hash restore and stable sticky-bar behavior.

### Design Intent

Refresh and hash navigation should feel intentional rather than visibly corrected after the page paints. The gallery now hides only the transient restore frame, lands directly on the target section, and avoids sticky-bar layout changes that can read as horizontal wobble while scrolling.

### Files Modified

- `scripts/build-gallery.py`
- `scripts/validate-gallery.py`
- `index.html`
