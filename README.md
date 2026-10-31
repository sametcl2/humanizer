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
├── .claude-plugin/
│   ├── plugin.json          # Claude Code plugin manifest
│   └── marketplace.json     # lets this repo act as a one-plugin marketplace
├── skills/humanizer/
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

**Option A: plugin (recommended, easy to update).** Inside Claude Code:

```
/plugin marketplace add <github-user>/humanizer
/plugin install humanizer@humanizer
```

Update later with `/plugin marketplace update humanizer`.

**Option B: plain skill folder.**

```bash
git clone https://github.com/<github-user>/humanizer.git
cd humanizer
./install.sh             # all projects: ~/.claude/skills/humanizer
./install.sh --project   # current project only: ./.claude/skills/humanizer
```

Or copy `skills/humanizer/` there by hand. Start a new session; the skill loads
automatically when you ask to write, humanize or audit text. You can also call it
explicitly: "use the humanizer skill on README.md".

### Claude.ai / Claude app

Download `humanizer.skill` from Releases and upload it in Settings > Capabilities >
Skills (or open the file in a chat and choose *Save skill*).

## Scanner

```bash
python skills/humanizer/scripts/scan.py draft.md            # English
python skills/humanizer/scripts/scan.py taslak.md --lang tr # Turkish
cat draft.md | python skills/humanizer/scripts/scan.py - --json
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

---

## Türkçe özet

`humanizer`, Wikipedia'daki "Signs of AI writing" rehberine dayanan bir Claude skill'i.
Metinleri yapay zekâ kokmayacak şekilde yazar, mevcut taslakları bilgileri koruyarak
yeniden yazar ya da bir metinde hangi kalıpların yapay zekâ izlenimi verdiğini raporlar.
Önce içeriği (somutluk, kaynak, doğruluk), sonra yapıyı, en son dili düzeltir; bilgi veya
kaynak uydurmaz. İngilizce rehber ve örnekler `references/english.md`, Türkçe kalıplar `references/turkish.md` dosyasındadır, tarayıcı
`--lang tr` ile Türkçe metinlerde çalışır.

Claude Code kurulumu: Claude Code içinde `/plugin marketplace add <github-kullanıcı>/humanizer`
ve `/plugin install humanizer@humanizer`, ya da repoyu klonlayıp `./install.sh`.
