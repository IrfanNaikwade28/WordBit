from scipy.spatial.distance import cosine
import gensim.downloader as api

print("Loading GloVe model...")
model = api.load("glove-wiki-gigaword-100")
print("GloVe model loaded")

def similarity(w1, w2):
    return 1 - cosine(model[w1], model[w2])

print("computer vs laptop:", similarity("computer", "laptop"))
print("computer vs banana:", similarity("computer", "banana"))
