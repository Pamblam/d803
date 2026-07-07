import csv
import json
import re
import contractions
import spacy

nlp = spacy.load("en_core_web_sm")
NEGATIONS = {"not", "no", "never", "nor", "none", "nothing", "neither", "cannot"}

def main():
    counter = 0
    
    with open("reviews.json") as f:
        reviews = json.load(f)

    csvfile = open("reviews_preprocessed.csv", "w", newline="", encoding="utf-8")
    writer = csv.writer(csvfile)
    writer.writerow(["id", "original_text", "cleaned_text", "tokens", "stars", "caps_emphasis_count"])

    for review in reviews:
        comment = review.get("comment", "")
        original_comment = comment
        stars = review.get("stars", "")
        
        # Ensure star values are valid
        if stars not in ("1", "2", "3", "4", "5"):
            continue
        
        # Convert stars to integers
        stars = int(stars)
        
        # Remove URLs
        comment = re.sub(r"https?://\S+|www\.\S+", "", comment)

        # Remove emojis
        comment = re.sub(
            r"[\U0001F300-\U0001FAFF\U00002600-\U000027BF\U0001F1E0-\U0001F1FF]+",
            "",
            comment,
        )
        
        # Convert hyphenated words into separate words
        comment = re.sub(r"(?<=\w)-(?=\w)", " ", comment)

        # Determine the number of capital words that are at least four letters long - use to determine emphasis (yelling)
        caps_emphasis_count = len(re.findall(r"\b[A-Z]{4,}\b", comment))

        # Convert all comments to lowercase
        comment = comment.lower()

        # Expand contractions
        comment = contractions.fix(comment)
        
        # Remove punctuation
        comment = re.sub(r"[^\w\s]", "", comment)
        
        # Remove excess whitespace
        comment = re.sub(r"\s+", " ", comment).strip()

        # Split the comment into tokens
        tokens = [token.text for token in nlp(comment)]

        # Remove stopwords, but keep negations so they don't flip the sentiment of the next token
        tokens = [t for t in tokens if t in NEGATIONS or t not in nlp.Defaults.stop_words]

        # Lemmatize the remaining tokens
        tokens = [token.lemma_ for token in nlp(" ".join(tokens))]

        # Handle missing data
        if 0 == len(tokens):
            continue

        counter += 1
        writer.writerow([counter, original_comment, comment, " ".join(tokens), stars, caps_emphasis_count])

    csvfile.close()


if __name__ == "__main__":
    main()
