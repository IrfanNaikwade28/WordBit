🎯 WordBit
WordBit is a Contexto‑style word guessing game built with Django + NLP.
Players try to guess a secret word, and each guess is ranked by how close in meaning it is to the secret word using word embeddings.

🚀 Features
🔤 Guess words and get semantic rank feedback

🧠 NLP‑based similarity using GloVe embeddings

💡 Progressive hints (3 levels: weak → strong)

🚩 Give up option to reveal the secret word

🔄 New Game / Play Again with a fresh secret word

📖 Built‑in How to Play guide

🎨 Clean, modern UI (Contexto‑inspired)

⚡ Rankings built once per game (optimized)

🕹️ How to Play
Enter a word and submit your guess

You’ll receive a rank:

Rank 1 → 🎉 You found the secret word

Lower rank → closer in meaning

Higher rank → farther in meaning

Use up to 3 hints if you’re stuck

Give up anytime to reveal the word

Start a New Game to play again

🛠️ Tech Stack
Backend: Django

NLP: Gensim, GloVe (glove-wiki-gigaword-50)

Word Frequency: wordfreq

Frontend: HTML, CSS, Vanilla JS

Session Management: Django sessions