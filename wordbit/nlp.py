import random
from scipy.spatial.distance import cosine
import gensim.downloader as api
from wordfreq import top_n_list

MODEL_NAME = "glove-wiki-gigaword-50"
model = None   # ❌ don't load at import

COMMON_WORDS = top_n_list("en", 30000)

def load_model():
    global model
    if model is None:
        print("Loading GloVe model...")
        model = api.load(MODEL_NAME)
        print("GloVe model loaded")

def similarity(w1, w2):
    load_model()
    return 1 - cosine(model[w1], model[w2])

def generate_secret_word():
    load_model()
    candidates = [w for w in COMMON_WORDS if w in model]
    return random.choice(candidates[100:5000])

def build_rankings(secret_word):
    load_model()
    scores = []
    for word in COMMON_WORDS:
        if word in model:
            score = similarity(secret_word, word)
            scores.append((word, score))
    scores.sort(key=lambda x: x[1], reverse=True)
    return {word: rank for rank, (word, _) in enumerate(scores, start=1)}
