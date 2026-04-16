import pandas as pd
import re

# Load your cannabis CSV
df = pd.read_csv("cannabis-strains-final.csv")
df = df.astype(str)
print("Cannabis AI Chat (with ranking + summaries) is ready. Type 'quit' to exit.\n")

# --- Helper: Create a summary for a strain ---
def summarize_strain(row):
    return (
        f"Strain: {row.get('strain_name', 'Unknown')}\n"
        f"Breeder: {row.get('breeder', 'Unknown')}\n"
        f"Type: {row.get('indica_sativa', 'Unknown')}\n"
        f"THC: {row.get('thc', 'Unknown')}%\n"
        f"CBD: {row.get('cbd', 'Unknown')}%\n"
        f"Flavor: {row.get('flavor', 'Unknown')}\n"
        f"Effects: {row.get('effect', 'Unknown')}\n"
        f"Medical: {row.get('medical_strains', 'Unknown')}\n"
        f"Overview: {row.get('overview', 'Unknown')}\n"
    )

# --- Helper: Ranking function ---
def rank_strains(results, query):
    results = results.copy()
    def to_num(x):
        try:
            return float(re.findall(r"\d+\.?\d*", x)[0])
        except:
            return 0.0

    if "thc" in results.columns:
        results["thc_num"] = results["thc"].apply(to_num)
    else:
        results["thc_num"] = 0.0

    q = query.lower()
    if "strongest" in q or "high thc" in q or "potent" in q:
        return results.sort_values("thc_num", ascending=False)

    if "best" in q or "top" in q:
        def score(row):
            s = 0.0
            eff = str(row.get("effect", "")).lower()
            med = str(row.get("medical_strains", "")).lower()
            if "relax" in q and "relax" in eff:
                s += 10
            if "sleep" in q and "sleep" in eff:
                s += 10
            if "anxiety" in q and "anxiety" in med:
                s += 10
            s += row.get("thc_num", 0.0) / 2.0
            if "most_popular_seeds" in row and str(row.get("most_popular_seeds", "")).lower() == "true":
                s += 5
            return s
        results["score"] = results.apply(score, axis=1)
        return results.sort_values("score", ascending=False)

    return results

# --- Main smart search ---
def smart_search(query):
    q = query.lower().strip()
    terms = [t for t in re.split(r"\s+", q) if t]
    matches = []

    for _, row in df.iterrows():
        combined = " ".join([
            str(row.get("strain_name", "")),
            str(row.get("breeder", "")),
            str(row.get("pack_options", "")),
            str(row.get("overview", "")),
            str(row.get("effect", "")),
            str(row.get("sale_item", "")),
            str(row.get("medical_strains", "")),
            str(row.get("strength", "")),
            str(row.get("description", "")),
            str(row.get("climate", "")),
            str(row.get("indica_sativa", "")),
            str(row.get("smell_taste", ""))
        ]).lower()

        score = sum(1 for term in terms if term in combined)
        if score > 0:
            matches.append((score, row))

    if not matches:
        return pd.DataFrame(columns=df.columns)

    matches.sort(reverse=True, key=lambda x: x[0])
    matched_rows = pd.DataFrame([r.to_dict() for _, r in matches])

    # Apply ranking adjustments
    ranked = rank_strains(matched_rows, q)
    return ranked.reset_index(drop=True)

def get_response(use_input):
    user_input = use_input.lower().strip()
    if "creativity" in user_input:
        return "For creativity, try strains like Sour Diesel, Jack Herer, Durban Poison, Lemon Haze, Super Silver Haze, or Green Crack."
    if "relax" in user_input and "not" not in user_input:
        return "For relaxation, try strains like Grandaddy Purple, Northern Lights, Blue Dream, or Purple Kush."
    if "sleeping" in user_input:
        results = smart_search(user_input).head(3)
        if not results.empty:
         return "For sleeping, here are some matches:\n" + results.apply(summarize_strain, axis=1).str.cat(sep="\n---\n")
        else:
            return "Sorry, I could not find any strains matching that sleeping query."
    if "anxiety" in user_input:
        results = smart_search(user_input).head(3)
        if not results.empty:
         return "For anxiety, here are some matches:\n" + results.apply(summarize_strain, axis=1).str.cat(sep="\n---\n")
        return "Sorry, I couldn't find strains matching that anxiety query."

    # Default: attempt smart search and return top summaries
    results = smart_search(user_input).head(3)
    if results.empty:
        return "I'm not sure about that. I couldn't find matching strains."
    return results.apply(summarize_strain, axis=1).str.cat(sep="\n---\n")

if __name__ == "__main__":
    while True:
        try:
            user = input("You: ")
        except (EOFError, KeyboardInterrupt):
            print("\nGoodbye")
            break

        if user.lower().strip() == "quit":
            print("Goodbye")
            break

        response = get_response(user)
        print("Chatbot:", response)