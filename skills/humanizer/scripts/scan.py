#!/usr/bin/env python3
"""Flag surface-level signs of AI writing in a text.

Usage:
    python scan.py FILE [--lang en|tr] [--json]
    cat draft.md | python scan.py - --lang tr

This only finds word- and format-level signals. It cannot judge the deeper
problems (vagueness, unsupported claims, invented sources); a clean scan does
not mean a text is fine, and a hit does not prove AI authorship.
Based on the patterns in "Wikipedia:Signs of AI writing" (CC BY-SA 4.0).
"""
import argparse
import json
import re
import sys

# (category, regex) - matched case-insensitively per line
EN_PATTERNS = [
    ("significance", r"\b(stands|serves) as\b|\bis a (testament|reminder)\b|\b(pivotal|crucial|vital|significant|key) (role|moment)\b|\bplays? an? (vital|crucial|pivotal|significant|key|important) role\b|\bunderscores? (its|the) (importance|significance)\b|\breflects? (the )?broader\b|\bkey turning point\b|\bevolving landscape\b|\bindelible mark\b|\bdeeply rooted\b|\bsetting the stage for\b|\bmarks? a (significant )?shift\b|\bfocal point\b"),
    ("participle-commentary", r",\s*(highlighting|underscoring|emphasizing|reflecting|symbolizing|showcasing|ensuring|contributing to|fostering|cultivating|enhancing|solidifying|cementing)\b"),
    ("promotional", r"\bnestled\b|\bin the heart of\b|\bboasts?\b|\bvibrant\b|\brich (cultural )?(heritage|history|tapestry)\b|\bbreathtaking\b|\bstunning natural beauty\b|\brenowned\b|\bgroundbreaking\b|\bcommitment to\b|\bdiverse array\b|\bcontinues? to captivate\b|\bseamless(ly)?\b"),
    ("media-coverage", r"\bindependent coverage\b|\b(local|regional|national|international) media outlets\b|\btrade publications\b|\b(featured|profiled) (in|by)\b|\bactive social media presence\b|\bother prominent (media )?outlets\b"),
    ("vague-association", r"\b(widely |particularly )?associated with\b|\bin connection (with|to)\b|\bin association with\b"),
    ("weasel", r"\b(experts|observers|critics|scholars|researchers|analysts) (argue|note|have noted|say|suggest|have cited)\b|\bindustry reports\b|\bsome critics\b|\bwidely (regarded|considered|interpreted)\b|\bseveral sources\b"),
    ("didactic", r"\bit'?s (important|crucial|critical|worth) (to )?(note|noting|remember|consider|mention)\b|\bit is (important|crucial|critical) to (note|remember|consider|differentiate)\b|\bmay vary\b"),
    ("recap", r"^\s*(in summary|in conclusion|overall|to sum up|ultimately)\b"),
    ("challenges-formula", r"\bdespite (its|their|these|this) .{0,60}\bchallenges?\b|\bfaces? (several|numerous|many) challenges\b|\bfuture (outlook|prospects|directions)\b"),
    ("negative-parallelism", r"\bnot only\b.{0,80}\bbut( also)?\b|\b(it'?s|it is) not (just|only|merely) (about )?.{1,60}[;,—-]\s*(it'?s|it is)\b"),
    ("copula-avoidance", r"\b(serves|stands|functions|acts) as an?\b"),
    ("ai-vocabulary", r"\b(delve[sd]?|delving|crucial|pivotal|underscore[sd]?|underscoring|showcas(e|es|ed|ing)|intricate|intricacies|interplay|tapestry|testament|meticulous(ly)?|garner(ed|ing|s)?|bolster(ed|ing|s)?|fostering|foster(s|ed)?|enhanc(e|es|ed|ing)|align(s|ed)? with|resonat(e|es)? with|enduring|multifaceted|leverag(e|es|ed|ing)|realm|robust|valuable insights?|landscape)\b|^\s*additionally,"),
    ("chatbot-leftover", r"\b(certainly!|of course!|great question|i hope this helps|let me know if|would you like me to|is there anything else|as an ai( language model)?|as a large language model|as of my (last|latest) (knowledge |training )?(update|cutoff)|here is a (draft|summary|breakdown)|feel free to)\b"),
    ("knowledge-gap", r"\b(specific (details|information) (is|are) (limited|scarce))\b|\bnot widely (documented|available|disclosed)\b|\bin the (provided|available) (sources|search results)\b|\bbased on available information\b"),
    ("placeholder", r"\[(insert|name|your|describe|url|source|company|date)[^\]]*\]|\b\d{4}-xx-xx\b|^\s*subject:"),
    ("tool-artifact", r"turn\d+(search|image|news|file)\d+|contentReference\[oaicite|oai_citation|\[attached_file:\d+\]|\[web:\d+\]|attributableIndex|utm_source=(chatgpt\.com|openai)|<\|endoftext\|>|↩"),
]

TR_PATTERNS = [
    ("significance", r"önemli bir rol oyna|kritik bir öneme sahip|dönüm noktası|silinmez bir iz|derin köklere sahip|simgesi olarak öne çık|daha geniş bir (eğilim|hareket)|kapılarını arala|büyük önem arz"),
    ("participle-commentary", r",\s*[^,.]{0,60}(katkı sağla(makta|yarak)|altını çiz|gözler önüne ser|ön plana çıkar|pekiştir|güçlendir(mekte|erek))"),
    ("promotional", r"kalbinde yer alan|kucağında|eşsiz|büyüleyici|nefes kesen|zengin kültürel miras|kültürel mozaik|göz alıcı|benzersiz bir deneyim|köklü geçmiş|geniş bir yelpaze"),
    ("vague-association", r"ile ilişkilendiril|ile bağlantılı olarak anıl"),
    ("weasel", r"uzmanlara göre|pek çok kaynakta|genel kabul gören|bazı eleştirmenler|olarak değerlendirilmektedir"),
    ("didactic", r"unutulmamalıdır ki|belirtmek gerekir ki|önemle vurgulamak|dikkat edilmesi gereken nokta|değişiklik gösterebilir"),
    ("recap", r"^\s*(sonuç olarak|özetle|genel olarak değerlendirildiğinde|tüm bu bilgiler ışığında)"),
    ("challenges-formula", r"(başarılarına|rağmen).{0,60}zorluklarla karşı karşıya|bu zorluklara rağmen|gelecek perspektifi"),
    ("negative-parallelism", r"(sadece|yalnızca)\s.{1,60}\sdeğil,?\s*(aynı zamanda|ayrıca)"),
    ("copula-avoidance", r"niteliğindedir|konumundadır|olarak hizmet vermektedir|olarak öne çıkmaktadır|bünyesinde barındır"),
    ("ai-vocabulary", r"^\s*ayrıca,|bunun yanı sıra|kapsamlı|çok boyutlu|dinamik|değerli içgörü|derinlemesine|titizlikle|sinerji|ekosistem|ivme kazandır|zenginleştir"),
    ("chatbot-leftover", r"tabii ki!|elbette!|harika bir soru|umarım yardımcı olur|başka bir konuda yardımcı|bir yapay zek[aâ] (dil modeli )?olarak|son bilgi güncellemem"),
    ("placeholder", r"\[(isim|ad|kaynak|tarih|şirket)[^\]]*\]|\b\d{4}-xx-xx\b|^\s*konu:"),
    ("tool-artifact", r"turn\d+(search|image|news|file)\d+|contentReference\[oaicite|oai_citation|utm_source=(chatgpt\.com|openai)|↩"),
]

EMOJI = re.compile("[\U0001F300-\U0001FAFF☀-➿]")
TITLE_CASE_SMALL = {"a", "an", "the", "and", "or", "of", "in", "on", "for", "to", "at", "by", "with", "ve", "ile", "veya"}


def heading_is_title_case(text):
    words = [w for w in re.findall(r"[^\W\d_]+", text) if w]
    if len(words) < 3:
        return False
    big = [w for w in words[1:] if w.lower() not in TITLE_CASE_SMALL]
    return bool(big) and all(w[0].isupper() for w in big)


def scan(text, lang):
    patterns = [(c, re.compile(p, re.IGNORECASE)) for c, p in (TR_PATTERNS if lang == "tr" else EN_PATTERNS)]
    hits = []
    lines = text.splitlines()
    for n, line in enumerate(lines, 1):
        for cat, rx in patterns:
            for m in rx.finditer(line):
                hits.append({"line": n, "category": cat, "match": m.group(0).strip()})
        stripped = line.strip()
        if re.match(r"^#{1,6}\s+\S", stripped) and heading_is_title_case(stripped.lstrip("#")):
            hits.append({"line": n, "category": "title-case-heading", "match": stripped})
        if re.match(r"^([-*•–]|\d+[.)])\s+\*\*[^*]+:?\*\*:?", stripped):
            hits.append({"line": n, "category": "inline-header-list", "match": stripped[:60]})
        if EMOJI.search(line) and re.match(r"^(#{1,6}\s*|[-*•]\s*|\d+[.)]\s*)?\S*" + EMOJI.pattern, stripped):
            hits.append({"line": n, "category": "emoji-decoration", "match": stripped[:60]})

    words = max(len(re.findall(r"\w+", text)), 1)
    stats = {
        "words": words,
        "em_dashes_per_1000_words": round(text.count("—") * 1000 / words, 1),
        "bold_spans": len(re.findall(r"\*\*[^*]+\*\*", text)),
        "curly_quotes": len(re.findall("[“”‘’]", text)),
        "straight_quotes": len(re.findall("[\"']", text)),
        "triplets": len(re.findall(r"\b\w+, \w+,? (and|ve|ile) \w+\b", text)),
        "bullet_lines": sum(1 for l in lines if re.match(r"^\s*([-*•–]|\d+[.)])\s", l)),
    }
    return hits, stats


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("file", help="path to a text/markdown file, or - for stdin")
    ap.add_argument("--lang", choices=["en", "tr"], default="en")
    ap.add_argument("--json", action="store_true", help="machine-readable output")
    args = ap.parse_args()

    text = sys.stdin.read() if args.file == "-" else open(args.file, encoding="utf-8").read()
    hits, stats = scan(text, args.lang)

    by_cat = {}
    for h in hits:
        by_cat.setdefault(h["category"], []).append(h)

    if args.json:
        print(json.dumps({"stats": stats, "counts": {k: len(v) for k, v in by_cat.items()}, "hits": hits}, ensure_ascii=False, indent=2))
        return

    density = len(hits) * 1000 / stats["words"]
    level = "strong" if density > 15 else "moderate" if density > 6 else "weak"
    print(f"Words: {stats['words']}  |  flags: {len(hits)}  |  {density:.1f} per 1000 words  ->  {level} surface signals")
    print(f"Em dashes/1000w: {stats['em_dashes_per_1000_words']}  bold spans: {stats['bold_spans']}  "
          f"curly/straight quotes: {stats['curly_quotes']}/{stats['straight_quotes']}  "
          f"'X, Y and Z' triplets: {stats['triplets']}  bullet lines: {stats['bullet_lines']}")
    for cat in sorted(by_cat, key=lambda c: -len(by_cat[c])):
        print(f"\n[{cat}] x{len(by_cat[cat])}")
        for h in by_cat[cat][:12]:
            print(f"  L{h['line']}: {h['match']}")
        if len(by_cat[cat]) > 12:
            print(f"  ... {len(by_cat[cat]) - 12} more")
    print("\nReminder: surface flags only. Check substance (specifics, sourcing, accuracy) by reading.")


if __name__ == "__main__":
    main()
