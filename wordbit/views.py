from django.shortcuts import render, redirect
from .nlp import generate_secret_word, get_rank, COMMON_WORDS
import random

MAX_HINTS = 3

def home(request):
    # ==========================
    # HANDLE POST FIRST
    # ==========================
    if request.method == "POST":
        action = request.POST.get("action")

        if action == "play_again":
            request.session.flush()
            return redirect("/")

    # ==========================
    # INIT NEW GAME IF NEEDED
    # ==========================
    if "secret" not in request.session:
        secret = generate_secret_word()

        request.session["secret"] = secret
        request.session["guesses"] = {}
        request.session["hints"] = []
        request.session["count"] = 0
        request.session["given_up"] = False


    # ==========================
    # LOAD STATE
    # ==========================
    secret = request.session["secret"]
    print(secret)
    guesses = request.session["guesses"]
    hints = request.session["hints"]
    count = request.session["count"]
    given_up = request.session["given_up"]

    message = None

    # ==========================
    # OTHER ACTIONS
    # ==========================
    if request.method == "POST":
        action = request.POST.get("action")

        if action == "guess" and not given_up:
            word = request.POST.get("word", "").lower().strip()

            if word not in guesses:
                rank = get_rank(secret, word)

                if rank:
                    count += 1
                    guesses[word] = rank
                    request.session["count"] = count
                    request.session["guesses"] = guesses

                    if rank == 1:
                        message = f"You found the word in {count} guesses!"

        elif action == "hint" and not given_up:
            if len(hints) < MAX_HINTS:

                # hint ranges by hint number
                hint_ranges = [
                    (50, 100),   # first hint
                    (20, 50),    # second hint
                    (8, 20),     # third hint
                ]

                low, high = hint_ranges[len(hints)]

                tries = 0
                MAX_TRIES = 100  # safety limit

                while tries < MAX_TRIES:
                    hint_word = random.choice(COMMON_WORDS)

                    # avoid duplicates
                    if hint_word in guesses or hint_word in [h[0] for h in hints]:
                        tries += 1
                        continue

                    rank = get_rank(secret, hint_word)

                    if rank and low <= rank <= high:
                        hints.append((hint_word, rank))
                        request.session["hints"] = hints
                        break

                    tries += 1


        elif action == "giveup":
            request.session["given_up"] = True
            given_up = True

    return render(request, "Index.html", {
        "guesses": sorted(guesses.items(), key=lambda x: x[1]),
        "hints": hints,
        "count": count,
        "message": message,
        "given_up": given_up,
        "secret": secret,
        "max_hints": MAX_HINTS,
    })
