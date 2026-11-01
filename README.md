# humanizer

A Claude skill for writing and revising text so it reads like a careful person wrote it,
not a chatbot. It turns the WikiProject AI Cleanup field guide
[Wikipedia:Signs of AI writing](https://en.wikipedia.org/wiki/Wikipedia:Signs_of_AI_writing)
into working instructions for English, and adds a Turkish adaptation.

The skill fixes substance before style. Deleting "pivotal" and "tapestry" from a text that
is still vague, inflated and badly sourced only hides the problem, so the skill asks for
specific facts first, then a structure that fits the content, then wording and formatting.
It never invents facts or citations to make text look more specific.

## What it does

- **Write:** drafts articles, posts, bios, reports and emails without the usual tells.
- **Rewrite:** humanizes an existing draft while keeping every fact, name and number.
- **Audit:** points out where a text reads as AI-assisted and why, with calibrated
  language (signals, not proof).

## Contents

```
.
├── humanizer/
│   ├── SKILL.md             # main instructions (loaded when the skill triggers)
│   ├── references/
│   │   ├── patterns.md      # full pattern catalog with explanations and fixes
│   │   ├── english.md       # English cheat sheet and before/after examples by genre
│   │   └── turkish.md       # Turkish equivalents and a before/after example
│   └── scripts/
│       └── scan.py          # quick surface-level scanner (en/tr)
└── install.sh               # copies the skill into ~/.claude/skills
```

## Install

### Claude Code

Claude Code reads skills from folders on disk, so installing means putting the
`humanizer/` folder where it looks:

```bash
git clone https://github.com/sametcl2/humanizer.git
cd humanizer
./install.sh             # all projects: ~/.claude/skills/humanizer
./install.sh --project   # current project only: ./.claude/skills/humanizer
```

If you downloaded the ZIP instead of cloning and get "permission denied", run
`bash install.sh`. On Windows, copy the `humanizer` folder to
`%USERPROFILE%\.claude\skills\` by hand.

Or copy `humanizer/` there by hand on any system. Start a new session; the skill loads automatically
when you ask to write, humanize or audit text. You can also call it explicitly: "use the
humanizer skill on README.md". To update, `git pull` and run `./install.sh` again.

### Claude.ai / Claude app

Download `humanizer.skill` from [Releases](https://github.com/sametcl2/humanizer/releases/latest) and upload it in Settings > Capabilities >
Skills (or open the file in a chat and choose *Save skill*).

## Scanner

```bash
python humanizer/scripts/scan.py draft.md            # English
python humanizer/scripts/scan.py taslak.md --lang tr # Turkish
cat draft.md | python humanizer/scripts/scan.py - --json
```

It flags word- and format-level signals with line numbers (inflated significance,
trailing "-ing" commentary, promotional phrasing, weasel words, negative parallelisms,
title-case headings, bold-label lists, chatbot leftovers, citation artifacts) and reports
em dash density, triplets and quote style. It cannot judge vagueness or accuracy, and a
hit is not proof of AI authorship.

## A note on detection

None of these patterns proves a text was machine-written: models learned them from
people. Don't use this skill or the scanner to accuse anyone. The Wikipedia guide is
explicit that perfect grammar, formal tone or "fancy" words are not reliable signs.

## License and attribution

This project is licensed under [CC BY-SA 4.0](LICENSE).

The pattern catalog is adapted from
[Wikipedia:Signs of AI writing](https://en.wikipedia.org/wiki/Wikipedia:Signs_of_AI_writing)
by the contributors of WikiProject AI Cleanup, used under CC BY-SA 4.0. The text has
been paraphrased, reorganized and extended (general-writing guidance, Turkish section,
scanner). Changes are not endorsed by Wikipedia or its editors.
