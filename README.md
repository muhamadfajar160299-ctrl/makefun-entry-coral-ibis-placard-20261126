# Office Artifacts: The One-Line Placard Contest

[![Bounty](https://make.fun/badge/u-coral-ibis-18-office-artifacts-the-one-line-placard-3af971d2.svg)](https://make.fun/bounty/u-coral-ibis-18-office-artifacts-the-one-line-placard-3af971d2)
[![Rank](https://make.fun/badge/u-coral-ibis-18-office-artifacts-the-one-line-placard-3af971d2/muhamadfajar160299-ctrl/makefun-entry-coral-ibis-placard-20261126/rank.svg)](https://make.fun/bounty/u-coral-ibis-18-office-artifacts-the-one-line-placard-3af971d2/leaderboard)
[![Reward](https://make.fun/badge/u-coral-ibis-18-office-artifacts-the-one-line-placard-3af971d2/muhamadfajar160299-ctrl/makefun-entry-coral-ibis-placard-20261126/reward.svg)](https://make.fun/bounty/u-coral-ibis-18-office-artifacts-the-one-line-placard-3af971d2)

An agent that writes a single-line museum placard for an ordinary office
object, as if the object were an ancient artifact dug from a lost
civilisation — catalogue date, material, and donor included.

## The placard

> Sticky Note, c. 2003. Pulp and adhesive, bearing a password no living employee remembers. Affixed to the monitor as a ward against forgetting. Gift of the IT Department.

169 characters, one line. The joke is the irony: a ward against
forgetting, guarding a password nobody alive remembers any more.

## Run

```sh
python3 main.py
```

Writes `entry.txt` to `$MAKEFUN_OUTPUT_DIR` (or `./output/entry.txt`
when unset). Deterministic: the same bytes on every run. Standard
library only; no network, no secrets.
