from django.shortcuts import render, redirect
from .nlp import generate_secret_word, build_rankings

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
        rankings = build_rankings(secret)

        request.session["secret"] = secret
        request.session["rankings"] = rankings
        request.session["guesses"] = {}
        request.session["hints"] = []
        request.session["count"] = 0
        request.session["given_up"] = False

    # ==========================
    # LOAD STATE
    # ==========================
    secret = request.session["secret"]
    RANKINGS = request.session["rankings"]
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
            if word in RANKINGS and word not in guesses:
                count += 1
                guesses[word] = RANKINGS[word]
                request.session["count"] = count
                request.session["guesses"] = guesses
                if RANKINGS[word] == 1:
                    message = f"You found the word in {count} guesses!"

        elif action == "hint" and not given_up:
            if len(hints) < MAX_HINTS:
                hint_ranges = [(300, 500), (100, 299), (11, 99)]
                low, high = hint_ranges[len(hints)]
                for w, r in sorted(RANKINGS.items(), key=lambda x: x[1]):
                    if w not in guesses and w not in [h[0] for h in hints] and low <= r <= high:
                        hints.append((w, r))
                        request.session["hints"] = hints
                        break

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
