# Pattern catalog

A paraphrased, reorganized summary of the WikiProject AI Cleanup field guide
"Wikipedia:Signs of AI writing" (https://en.wikipedia.org/wiki/Wikipedia:Signs_of_AI_writing),
licensed CC BY-SA 4.0. The original is descriptive and Wikipedia-specific; this version
is adapted for general writing. Each entry gives the pattern, why it reads as machine
output, and how to fix it.

## Contents

1. Content patterns
2. Language and grammar
3. Style and formatting
4. Chatbot leftovers
5. Citations and sourcing
6. Miscellaneous
7. Unreliable indicators (do not use as evidence)

---

## 1. Content patterns

### 1.1 Inflated significance, legacy and "broader trends"
**Watch for:** stands/serves as, is a testament/reminder, plays a vital/crucial/pivotal/
significant/key role, pivotal moment, underscores/highlights its importance, reflects
broader, symbolizing its enduring/lasting, contributing to the, setting the stage for,
marks/represents a shift, key turning point, evolving landscape, focal point, indelible
mark, deeply rooted, "the distinction matters because".

**Why it's a tell:** Models attach statements about how some arbitrary detail
"represents" or "contributes to" something larger, even for population figures or
etymology. Variants: placing the subject inside vague "debates" or "public discussions";
admitting the subject is minor and then claiming importance anyway ("Though it saw only
limited use, it contributes to the broader history of..."); for species, tenuous
ecosystem links and long notes about conservation status that is actually unknown.

**Fix:** Delete. If there's real significance, state the concrete fact behind it.

### 1.2 Canned emphasis on notability, attribution and media coverage
**Watch for:** independent coverage, local/regional/national media outlets, trade
publications, featured/profiled/cited in, "and other prominent outlets", written by a
leading expert, maintains an active social media presence.

**Why:** The text tries to prove importance by listing where the subject appeared and
classifying the sources, instead of saying what the sources reported. Models also
attribute their own analysis to named sources that never said it.

**Fix:** Use the content of the coverage, or cite it quietly. Drop social-media-presence
filler.

### 1.3 Superficial analysis (trailing participle clauses)
**Watch for:** sentence-final ", highlighting...", ", underscoring...", ", emphasizing...",
", reflecting...", ", symbolizing...", ", showcasing...", ", ensuring...",
", contributing to...", ", fostering...", ", enhancing...", "valuable insights",
"aligns/resonates with".

**Why:** A disembodied narrator tells the reader what a fact "means". The strongest
signal is an inanimate subject doing the highlighting: a sign, a date or an event cannot
underscore anything.

**Fix:** Cut the clause. If the interpretation is important, attribute it to a real
person or source.

### 1.4 Promotional, brochure-like language
**Watch for:** boasts a, vibrant, rich (heritage/history), profound, nestled, in the heart
of, breathtaking, stunning natural beauty, renowned, groundbreaking, showcasing,
exemplifies, commitment to, diverse array, continues to captivate, seamlessly.

**Why:** Models struggle to keep a neutral register. Places read like travel guides,
companies like press releases. Rewrites that claim to "remove promotional tone" often add
it. Newer models are more subtly positive than older ones but still use the same stock
phrases regardless of topic.

**Fix:** Neutral, factual description. Let readers judge.

### 1.5 Vague connection or association
**Watch for:** associated with, in connection with, connected to, in association with,
"particularly/widely associated".

**Why:** Instead of "X was CEO of Y", the text says "X was associated with leadership of
Y". It sounds careful but says less.

**Fix:** State the actual relationship (role, dates, action).

### 1.6 Vague attribution and overgeneralized opinion (weasel words)
**Watch for:** experts argue, observers have noted, industry reports, some critics argue,
researchers say, several sources (when one or two exist), "widely interpreted", "such as"
before a complete list.

**Why:** Claims are pinned on an unnamed authority, one source becomes "scholars", and
complete lists are made to look like samples.

**Fix:** Name the source or remove the claim. Match quantity words to reality.

### 1.7 Didactic disclaimers
**Watch for:** it's important/crucial/worth noting/remembering/considering, may vary,
"always check...", "it is crucial to differentiate...".

**Fix:** Delete unless it's genuinely necessary information; then state it directly.

### 1.8 Section summaries and recap endings
**Watch for:** In summary, In conclusion, Overall, To sum up, a "Conclusion" section in
non-essay text; paragraphs ending by restating their own point.

**Fix:** End when the content ends.

### 1.9 Formulaic "challenges" and "future outlook"
**Watch for:** "Despite its [praise], X faces several challenges...", "Despite these
challenges...", headings like "Challenges and Legacy", "Future Outlook/Prospects", ending
on vague optimism or speculation about initiatives.

**Note:** Mentioning difficulties is fine. The tell is the rigid formula.

**Fix:** Integrate real, specific problems where they occur in the narrative.

### 1.10 "X and Y" headings / "Awards and recognition"
Paired-noun headings ("Legacy and impact", "Awards and recognition") are much more
common in model output. Use headings that describe the actual content.

### 1.11 Treating a topic title as a proper noun
For descriptive titles (lists, broad topics), the first sentence defines the title as if
it were a real-world entity: "'List of songs about X' is a curated compilation of...".
**Fix:** Start with the subject itself.

---

## 2. Language and grammar

### 2.1 High density of "AI vocabulary"
Individual words are harmless; clusters are a strong signal. Lists drift by model era:

- **2023-mid 2024:** Additionally (sentence-initial), boasts, bolstered, crucial, delve,
  emphasizing, enduring, garner, intricate/intricacies, interplay, key, landscape,
  meticulously, pivotal, underscore, tapestry, testament, valuable, vibrant
- **Mid 2024-mid 2025:** align with, bolstered, crucial, emphasizing, enhance, enduring,
  fostering, highlighting, pivotal, showcasing, underscore, vibrant
- **Mid 2025-mid 2026:** emphasizing, enhance, highlighting, showcasing, plus the
  notability/attribution phrasing in 1.2
- **Mid 2026 on:** challenge, clearer, dependable, echoed, foster, leverage, matters,
  multifaceted, practical, prioritize, quietly, steady, universally; short sentences in a
  narrow 8-20 word band with heavy period/comma use
- Grok in particular overuses pseudo-scientific words: causal, empirical, correlate.

Take the lists literally: a word being overused doesn't mean its synonyms are. Mind
context ("underscore" can mean an underline or film music).

**Fix:** Rewrite the passage around the actual fact; don't just swap in synonyms.

### 2.2 Copula avoidance
"Serves as", "stands as", "functions as", "boasts", "features", "represents" where "is"
or "has" would do. **Fix:** use the plain verb.

### 2.3 Negative parallelisms
"Not only... but also", "It's not just about X; it's Y", and the same move spread over
two sentences ("X was famous. His life, however, took a different path..."). Unsuitable
for neutral writing. **Fix:** state the claim positively.

### 2.4 Outlines of negatives
Strings of short negations ending in a reveal: "No profiles. No coverage. Just TikTok
clips." / "Not a career, not a body of work - just a moment." Common in AI-written
arguments and comments. **Fix:** make the argument in normal sentences.

### 2.5 Rule of three
Adjective triplets, three-phrase lists, three bullet points by reflex - used to make thin
analysis look thorough. **Fix:** use the real number of items.

### 2.6 Elegant variation
A repetition penalty pushes models to cycle synonyms: "Yankilevsky... the artist... the
non-conformist... the visionary". **Fix:** repeat the name or use a pronoun.

### 2.7 False ranges
"From X to Y" where X and Y don't sit on any real scale ("from the Big Bang to the
cosmic web, from stellar birth to dark energy"). Real ranges (1990 to 2000, mild to
severe) and true merisms (head to toe) are fine. **Fix:** list the items plainly.

---

## 3. Style and formatting

### 3.1 Title Case Headings
Capitalizing All Main Words in section headings. **Fix:** sentence case unless house
style differs.

### 3.2 Excessive boldface
Mechanical bolding of key terms, often every occurrence, in "key takeaways" style
inherited from slide decks and listicles. **Fix:** remove nearly all bold in body text.

### 3.3 Inline-header vertical lists
Bullets or numbers followed by a **Bold header:** and a sentence. Pasted as plain text,
bullets may appear as •, -, –, # or emoji. **Fix:** prose, or a plain list where truly
appropriate.

### 3.4 Emoji decorations
Emoji in front of headings or bullets (🧠, 🚨, 📌). **Fix:** remove in formal text.

### 3.5 Em dash overuse
Humans use em dashes too; models use more, in places where people use commas,
parentheses or colons, often for sales-like "punch". Useful only together with other
signs. **Fix:** vary punctuation; keep dashes rare.

### 3.6 Curly quotes and apostrophes
Models tend to emit curly quotes, sometimes mixed with straight ones. Weak signal on its
own (word processors and phones auto-convert). **Fix:** use the destination's convention
consistently.

### 3.7 "Subject:" lines
Messages that start with an email subject line even when not an email.

### 3.8 Markdown in the wrong place
`**bold**`, `## headings`, `---` rules or ```` ``` ```` fences pasted into Word, email, a CMS
or wikitext, sometimes mixed with broken attempts at the target markup. Markdown alone is
not suspicious (many people write in it); mixed and broken markup is.

---

## 4. Chatbot leftovers (unambiguous)

### 4.1 Collaborative communication
"Certainly!", "Of course!", "You're absolutely right!", "I hope this helps", "Let me know
if...", "Would you like me to...", "Is there anything else...", "Here is a draft...",
"more detailed breakdown", meta-text about what "this article" or "this section" will do,
or advice addressed to the user that was pasted in as content.

### 4.2 Knowledge-cutoff and gap disclaimers
"As of my last knowledge update", "up to my training data", "while specific details are
limited/scarce", "not widely documented", "in the provided sources/search results",
"based on available information", usually followed by speculation about what is
"likely". The "not documented" claim itself is often unfounded.

### 4.3 Prompt refusals
"As an AI language model, I can't...", "I'm sorry, but..." (now rare).

### 4.4 Placeholders and templates
`[Entertainer's Name]`, `[Describe the section...]`, `[URL of reliable source]`, dates like
`2025-xx-xx`, notes like "(the following are placeholders...)".

### 4.5 Tool artifacts
`citeturn0search0` / `turn0image0`, `:contentReference[oaicite:0]{index=0}`,
`oai_citation`, `[attached_file:1]`, `[web:1]`, `({"attribution":{"attributableIndex":...}})`,
`↩` footnote markers, `<|endoftext|>`.

---

## 5. Citations and sourcing

- **Broken links** that never existed (not even in web archives).
- **Invalid ISBNs or DOIs**, DOIs that resolve to unrelated papers, book citations
  without page numbers, authors who couldn't have written the work.
- **Unconventional reference use:** wrong re-use syntax, a citation after every sentence
  pointing to the same irrelevant source, aggregator names left inline ("socialstarage.com
  +2").
- **`utm_source=chatgpt.com` / `utm_source=openai`** on URLs: proves ChatGPT was used to
  find the source (not necessarily to write the text).
- **Hallucinated categories / padded "See also"** lists filled to at least three links.

When writing: cite only what you have actually verified. When rewriting: never invent a
reference; flag missing support instead.

---

## 6. Miscellaneous

- **Abrupt cut-offs** where generation stopped.
- **Sudden style shifts** within one author's writing (e.g. flawless grammar appearing
  suddenly), or a variety mismatch (American English defaults in text by and about
  someone from a British-English context).
- **Over-long, formal, first-person edit/change summaries** that itemize conventions
  ("Refined the tone for neutrality, ensured factual accuracy, improved clarity...").
- **Self-justifying notes to reviewers** inserted in a submission explaining why it meets
  standards.
- Text predating 30 Nov 2022 (ChatGPT's public launch) is very unlikely to be LLM output.

---

## 7. Unreliable indicators (do not use as evidence)

False accusations harm people. These are commonly cited but weak or misleading:

- **Perfect grammar** - many humans write well.
- **"Bland" or "robotic" prose** - default model output is actually effusive and verbose.
- **Fancy, academic or unusual words** - models favor a specific set of words, not rare
  vocabulary in general; truly unusual words are less likely in model output.
- **Letter-like formality** by itself - people wrote formal letters long before LLMs.
- **Connective words** ("moreover", "however") by themselves - normal in essays.
- **Random broken markup** - more often editor or extension bugs.
- **AI detector scores** - tools like GPTZero beat chance but have real error rates and
  are easily fooled by paraphrasing or new models. Human judges also do poorly, except
  heavy LLM users, who in one 2025 study caught about 90% of AI text with few false
  positives.

Also note: human writing is itself drifting toward LLM vocabulary, while LLM output is not
drifting toward human writing. Judge clusters and substance, not isolated words.
