import random
from scipy.spatial.distance import cosine
import gensim.downloader as api
from wordfreq import top_n_list

# ==============================
# LOAD MODEL (ONCE)
# ==============================
MODEL_NAME = "glove-wiki-gigaword-50"
print("Loading GloVe model...")
model = api.load(MODEL_NAME)
print("GloVe model loaded")

# ==============================
# LOAD COMMON WORDS (ONCE)
# ==============================
NUM_COMMON_WORDS = 30000
COMMON_WORDS = top_n_list("en", NUM_COMMON_WORDS)

# ==============================
# SIMILARITY
# ==============================
def similarity(w1, w2):
    return 1 - cosine(model[w1], model[w2])

# ==============================
# SECRET WORD GENERATOR
# ==============================
def generate_secret_word():
    """
    Choose a reasonable secret word:
    - common
    - exists in model
    - not too trivial
    """
    candidates = [w for w in COMMON_WORDS if w in model]
    return random.choice(candidates[100:5000])

# ==============================
# BUILD RANKINGS
# ==============================
def build_rankings(secret_word):
    scores = []

    for word in COMMON_WORDS:
        if word in model:
            score = similarity(secret_word, word)
            scores.append((word, score))

    scores.sort(key=lambda x: x[1], reverse=True)

    return {
        word: rank
        for rank, (word, _) in enumerate(scores, start=1)
    }
