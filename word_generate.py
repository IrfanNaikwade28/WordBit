from wordfreq import top_n_list

# get top 50,000 English words
words = top_n_list("en", 50000)

# optional cleanup (recommended)
clean_words = [
    w for w in words
    if w.isalpha() and len(w) > 2
]

with open("words.txt", "w") as f:
    for word in clean_words:
        f.write(word + "\n")

print(f"Saved {len(clean_words)} words")
