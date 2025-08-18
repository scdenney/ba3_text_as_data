# build_stopwords.py
import re, csv, collections, argparse, sys
from pathlib import Path

# --- Token rules ---
HANGUL_WORD = re.compile(r"[가-힣]+")  # only pure Hangul tokens

def tokenize_ko(text: str):
    # keep only Hangul tokens (no underscores, numbers, latin)
    return HANGUL_WORD.findall(text or "")

# --- Base function words / particles / helpers ---
BASE_FUNCTIONALS = {
    "은","는","이","가","을","를","에","에서","에게","으로","로","과","와","도","만","뿐",
    "보다","처럼","까지","부터","마저","조차","의",
    "것","수","등","때","중","동안","이후","이전","부분","경우","전체","각","최근","당시",
    "그리고","그러나","하지만","또한","또","또는","따라서","즉","다만","한편","반면","특히","먼저",
    "하다","되다","있다","없다","이다","아니다",
    "하며","하고","되는","있는","없는","이며","이고","위해","대해","관한","관련","관계","통해","대한","우리","그"
}

# Add common verb/adjective surface forms that show up in your cloud
VERB_SURFACES = {
    "할","함","함으로","함으로써","하면서","하려","하려는","하려고","하면","하는","하였다","해왔다",
    "되는","되어","되며","되도록","되기","되었다","된다","된다면",
    "있는","있으며","있고","있다","없다",
}

# Optional NK boilerplate to squash rhetorical filler
NK_BOILERPLATE = {
    "현시기","위대한","경애하는","령도자","동지","장군님","김일성","김정일","김정은",
    "혁명","혁명적","주체","사회주의","건설","경제건설","위업","노선","사상","과업","투쟁",
    "과제","성과","문제","요구","기본요구","의의","담보"
}

# Profiles
KEEP_ALWAYS_TEXTBOOK = {"대한민국","민족","국가","경제","사회","역사","독립","전쟁"}
KEEP_ALWAYS_NK = set()  # keep minimal; you asked not to keep domain terms for NK

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--csv", required=True, help="Path to corpus CSV (must have 'content' column)")
    ap.add_argument("--text-col", default="content", help="Text column name (default: content)")
    ap.add_argument("--base", help="Existing stopwords file to start from")
    ap.add_argument("--banfile", help="Extra tokens to force-add to stopwords (one per line)")
    ap.add_argument("--out", required=True, help="Output stopwords file")
    ap.add_argument("--profile", choices=["textbook","nk"], default="textbook")
    ap.add_argument("--add-nk-boiler", action="store_true", help="Also include NK boilerplate list")
    ap.add_argument("--topk", type=int, default=120, help="Auto-add top-K frequent function-like tokens")
    ap.add_argument("--minlen", type=int, default=1, help="Drop tokens shorter than this length")
    args = ap.parse_args()

    csv_path = Path(args.csv)
    out_path = Path(args.out)

    # seed with base lists
    stops = set(BASE_FUNCTIONALS) | set(VERB_SURFACES)

    # bring in existing stoplist if provided
    if args.base:
        with open(args.base, "r", encoding="utf-8") as f:
            stops |= {line.strip() for line in f if line.strip()}

    # optional NK boilerplate
    if args.add_nk_boiler or args.profile == "nk":
        stops |= NK_BOILERPLATE

    # choose keep list
    keep_always = KEEP_ALWAYS_TEXTBOOK if args.profile == "textbook" else KEEP_ALWAYS_NK

    # count tokens
    freq = collections.Counter()
    with csv_path.open("r", encoding="utf-8", newline="") as f:
        reader = csv.DictReader(f)
        for row in reader:
            for tok in tokenize_ko(row.get(args.text_col, "")):
                if len(tok) < args.minlen:
                    continue
                freq[tok] += 1

    # heuristics to auto-augment stoplist from top frequency
    ENDINGS = ("으로","에서","까지","부터","하며","하고","하면","하는","하기","적인","적으로")
    auto_add = []
    for w, _ in freq.most_common():
        if len(auto_add) >= args.topk:
            break
        if w in keep_always:
            continue
        if (w in BASE_FUNCTIONALS
            or w in VERB_SURFACES
            or w.endswith(ENDINGS)
            or w in {"그","의","할","문제","요구","의의"}):
            auto_add.append(w)

    stops.update(auto_add)

    # user-provided banfile
    if args.banfile:
        with open(args.banfile, "r", encoding="utf-8") as f:
            stops |= {line.strip() for line in f if line.strip()}

    # write
    final = sorted(stops, key=lambda x: (len(x), x))
    out_path.write_text("\n".join(final) + "\n", encoding="utf-8")

    print(f"[{args.profile}] stopwords: {len(final)} → {out_path}")
    if auto_add:
        print("auto-added (sample):", ", ".join(auto_add[:30]))

if __name__ == "__main__":
    sys.exit(main())
