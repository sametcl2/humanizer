---
name: humanizer
description: Write and revise prose so it reads like a careful human wrote it, not a chatbot. Use whenever the user asks to "humanize" text, remove the "AI tone", make a draft sound natural or less robotic, de-ChatGPT an article, edit an AI-assisted draft before publishing, or review whether a text shows signs of AI writing. Also use when writing any article, blog post, report, bio, encyclopedia-style entry, email or document the user will publish under their own name. Works in English and Turkish (and other languages by analogy).
---

# Humanizer

Chatbot prose is recognizable less because of single words and more because of a habit
underneath them: language models regress to the mean. They swap the specific, slightly
unusual fact for the generic, broadly palatable statement, then compensate by insisting
loudly that the subject matters. The result is text that is simultaneously vaguer and
more inflated than what a knowledgeable person would write.

This skill is based on the WikiProject AI Cleanup field guide
"Wikipedia:Signs of AI writing" (CC BY-SA 4.0). The full catalog of patterns, with
explanations, lives in `references/patterns.md`. Language-specific guides with
before/after examples: `references/english.md` (English) and `references/turkish.md`
(Turkish).

## The core principle: fix the substance, not just the surface

The Wikipedia guide warns that its signs are symptoms of deeper problems, and that
scrubbing the symptoms alone only hides them. Take that seriously. A text with every
"pivotal" deleted but still full of unsupported claims, padded significance and invented
sources is worse, not better, because it now looks trustworthy.

So the order of work is always:

1. **Substance** - Is every claim specific, true and supported? Is there anything the
   writer actually knows that the text is hiding behind a generality?
2. **Structure** - Does the shape fit the content, or is it a template (intro, three
   bolded bullets, "Challenges", "Conclusion")?
3. **Voice** - Only now: vocabulary, rhythm, punctuation, formatting.

If you don't have the facts needed to make a sentence specific, do not invent them.
Either cut the sentence, ask the user, or mark the gap plainly (e.g. `[source needed:
founding year]`). Fabricated specificity is the most damaging AI tell of all.

## Modes

Decide which mode the request is in:

- **Write** - drafting new text. Apply the rules below as you write; then run the
  self-check.
- **Rewrite** - the user gives a draft to humanize. Preserve every fact, name, number and
  the author's intended meaning. Change wording and structure, not content. Do not add
  new claims. If you remove something substantive (e.g. a vague claim you can't verify),
  say so in your notes.
- **Audit** - the user wants to know whether / where a text reads as AI. Report specific
  passages, which pattern each one shows, and why. Be calibrated: these are signals, not
  proof (see "Calibration" below). Don't rewrite unless asked.

## Writing rules

### Content

- **Say the specific thing.** "Invented the first automatic train coupler in 1873" beats
  "a revolutionary titan of industry". Concrete nouns, numbers, dates, names, places.
- **Don't announce importance; show it or drop it.** Delete sentences whose only job is to
  say something "plays a pivotal role", "stands as a testament", "marks a significant
  shift", "reflects broader trends", "leaves an indelible mark". If the significance is
  real, state the fact that makes it significant.
- **No trailing "-ing" commentary.** Sentences ending in ", highlighting its importance",
  ", underscoring...", ", reflecting...", ", contributing to...", ", ensuring...",
  ", fostering..." are a disembodied narrator editorializing. Facts and events don't
  "highlight" anything; people do. Cut the clause or make it a real, attributed claim.
- **Neutral tone unless the genre calls for promotion.** Avoid travel-brochure and
  press-release language: nestled, in the heart of, boasts, vibrant, rich (heritage,
  tapestry), breathtaking, stunning natural beauty, renowned, groundbreaking, commitment
  to, diverse array, showcasing, seamlessly.
- **State relationships directly.** "She was CEO of X from 2017 to 2020", not "she was
  associated with leadership at X" or "known in connection with X".
- **Attribute precisely or not at all.** No "experts argue", "observers note", "industry
  reports suggest", "some critics" unless you can name who. Don't turn one source into
  "several sources" or "widely regarded". Don't write "such as" before a list that is
  actually complete.
- **Don't parade sources.** Listing outlets that "featured" or "profiled" a subject, or
  noting "an active social media presence", is not evidence of anything. Use what the
  sources actually say.
- **No formulaic challenges/future section.** Avoid "Despite its [praise], X faces
  several challenges... Despite these challenges, X continues to thrive." Mention
  difficulties where they belong in the narrative, with specifics.
- **No moralizing asides.** Drop "it's important to note/remember/consider", "it is
  crucial to differentiate", unasked-for safety reminders, and "may vary" hedges that add
  nothing.
- **No recap endings.** Don't close sections or the piece with "In summary", "In
  conclusion", "Overall" restating what was just said. End when the content ends.
- **Don't fake knowledge gaps either.** No "while specific details are limited..." followed
  by speculation about what is "likely". If information is missing, say so once, plainly,
  and don't fill the hole.

### Language

- **Plain verbs.** Use "is" and "has" instead of "serves as", "stands as", "functions as",
  "boasts", "features", "represents".
- **Watch the AI vocabulary.** These words are fine individually but cluster in model
  output: delve, crucial, pivotal, key (as filler adjective), underscore, highlight (verb),
  showcase, emphasize, enhance, foster, garner, bolster, align with, resonate with,
  intricate/intricacies, interplay, tapestry, landscape (abstract), testament, enduring,
  meticulous, robust, valuable insights, multifaceted, leverage, navigate (abstract),
  realm, seamless, "Additionally," at sentence start. When you see two or three in one
  paragraph, rewrite the paragraph rather than swapping synonyms.
- **Break the rule of three.** Models default to triplets ("innovation, collaboration, and
  growth"). Use the number of items that actually exist: one, two, four.
- **Avoid negative parallelisms.** "Not only X but also Y", "It's not just X, it's Y",
  "no X, no Y, just Z". Say what the thing is.
- **Avoid false ranges.** "From ancient rituals to modern festivals" only works if there is
  a real scale between the endpoints. Otherwise, just list the items.
- **Repeat the right word.** Don't rotate synonyms to avoid repetition ("the artist... the
  painter... the creative visionary..."). Use the name or a pronoun.
- **Vary sentence length naturally,** but don't perform variety. Some long sentences, some
  short, driven by what's being said.
- **Match the writer's variety and register.** British vs American English, regional
  spelling, formality. Don't silently Americanize.

### Formatting

- **Prose by default.** Don't convert narrative into bullet points. Reserve lists for
  genuinely list-like content (steps, specs, parallel items).
- **No "bold label: explanation" bullet lists** as a default shape.
- **Bold sparingly** - almost never in body text, and never every occurrence of a term.
- **Sentence-case headings** ("Early life and education", not "Early Life And
  Education"), unless the house style says otherwise.
- **No emoji** in headings or bullets in formal text.
- **Em dashes in moderation.** Prefer commas, parentheses, colons or a new sentence. Don't
  use the dash for dramatic "punch" ("It's not a meme - it's a movement").
- **Use the punctuation convention of the destination** (straight vs curly quotes) and be
  consistent.
- **Match the target markup.** Don't leave Markdown (`**`, `##`) in text going into Word,
  a CMS, email or wikitext.

### Leftovers that must never appear

These are unambiguous giveaways. Remove them in every mode:

- Chatbot correspondence: "Certainly!", "Of course!", "Great question", "I hope this
  helps", "Let me know if you'd like...", "Would you like me to...", "Here is a...",
  "As an AI language model", knowledge-cutoff statements ("as of my last update").
- Placeholders: `[Name]`, `[Insert source]`, `2025-xx-xx`, "Subject:" lines on things that
  aren't emails.
- Tool artifacts: `citeturn0search0`, `:contentReference[oaicite:N]`, `oai_citation`,
  `[attached_file:1]`, `{"attribution": ...}`, `utm_source=chatgpt.com` / `openai` in URLs,
  `↩` footnote marks, stray ```` ``` ```` fences.
- References you cannot verify. Never output an invented citation, DOI, ISBN or URL.

## Workflow

1. Identify the mode, genre, audience, language and destination format.
2. For Rewrite/Audit on longer texts, run the scanner first to get a quick map:
   `python scripts/scan.py <file>` (or pipe text via stdin; add `--lang tr` for Turkish).
   It flags word-level and formatting signals with line numbers. It does not catch the
   deeper content problems - that's your job.
3. Read `references/patterns.md` if you need the explanation of a flagged pattern. For
   the language you're writing in, read `references/english.md` or
   `references/turkish.md` (cheat sheet plus worked before/after examples).
4. Work through substance, then structure, then voice.
5. Self-check before returning (below).

## Self-check

Read the result once as a skeptical editor and ask:

- Could any sentence be pasted into an article about a different subject unchanged? Make
  it specific or cut it.
- Does any sentence exist only to tell me something is important, rich, vibrant or
  significant?
- Is every attribution to a nameable source? Every number and name preserved from the
  original (in Rewrite mode)?
- Are there triplets, "not only... but", trailing -ing clauses, or a recap ending left?
- Is the formatting what a human would use in this destination?
- Any leftover chatbot phrasing, placeholders or tool artifacts?

## Output

- **Write / Rewrite:** return the text. If the user wants it, add a short "What changed"
  note (3-6 lines: patterns removed, anything cut for lack of support, open gaps marked).
  Don't lecture.
- **Audit:** a short verdict ("strong / moderate / weak signs"), then the passages with the
  pattern name and a one-line reason, most telling first. Close with the substantive
  issues (unsupported claims, vague sourcing) separately from the stylistic ones.

## Calibration

None of these patterns proves AI authorship. Language models learned them from human
writing - press releases, travel guides, student essays, blogs. Perfect grammar,
"fancy" vocabulary, formal letter style or a plain, "robotic" tone are not reliable signs
on their own. What is telling is density and clustering: many patterns together, in a
text that says little. When auditing, say "reads as AI-assisted because..." rather than
"was written by AI", and never base a judgment on one em dash or one "delve".

Also remember that the specific overused words drift between model generations (e.g.
"delve" faded after 2024; newer models lean on words like "quietly", "steady",
"practical", "leverage", "matters", with short, clipped sentences). Focus on the
underlying habits - inflation, vagueness, formula - which persist across models.
