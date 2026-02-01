import random
from pathlib import Path
from scipy.spatial.distance import cosine
from gensim.models import KeyedVectors
from wordfreq import top_n_list

BASE_DIR = Path(__file__).resolve().parent.parent

MODEL_PATH = (
    BASE_DIR / "models" / "gensim-data" / "glove-wiki-gigaword-50"
    / "glove-wiki-gigaword-50.txt"
)

print("🔹 Loading GloVe model at startup...")
model = KeyedVectors.load_word2vec_format(
    MODEL_PATH,
    binary=False
)
print("✅ GloVe model loaded")

COMMON_WORDS = top_n_list("en", 30000)


def similarity(w1, w2):
    return 1 - cosine(model[w1], model[w2])


def generate_secret_word():
    candidates = [w for w in COMMON_WORDS if w in model]
    return random.choice(candidates[100:5000])


def get_rank(secret, guess):
    if guess not in model or secret not in model:
        return None

    target_sim = similarity(secret, guess)

    better = 0
    SAMPLE_SIZE = 800

    for w in random.sample(COMMON_WORDS, SAMPLE_SIZE):
        if w in model and similarity(secret, w) > target_sim:
            better += 1

    return better + 1
