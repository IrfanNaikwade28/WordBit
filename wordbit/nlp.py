import random
from scipy.spatial.distance import cosine
import gensim.downloader as api
from wordfreq import top_n_list

MODEL_NAME = "glove-wiki-gigaword-50"
model = None

COMMON_WORDS = top_n_list("en", 30000)

def load_model():
    global model
    if model is None:
        print("🔹 Loading GloVe model...")
        model = api.load(MODEL_NAME)
        print("✅ GloVe model loaded")

def similarity(w1, w2):
    load_model()
    return 1 - cosine(model[w1], model[w2])

def generate_secret_word():
    load_model()
    candidates = [w for w in COMMON_WORDS if w in model]
    return random.choice(candidates[100:5000])

def get_rank(secret, guess):
    load_model()

    if guess not in model or secret not in model:
        return None

    target_sim = similarity(secret, guess)

    better = 0
    SAMPLE_SIZE = 150  # 🔥 REDUCED (VERY IMPORTANT)

    for w in random.sample(COMMON_WORDS, SAMPLE_SIZE):
        if w in model and similarity(secret, w) > target_sim:
            better += 1

    return better + 1
