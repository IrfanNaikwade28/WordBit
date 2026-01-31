# 🎯 WordBit

> A Contexto-style semantic word guessing game built with **Django** and **NLP**.

WordBit challenges players to guess a hidden word.  
Each guess is ranked based on **semantic similarity** to the secret word using **word embeddings**, not keyword matching.

---

## 📌 Overview

Unlike traditional word games, WordBit measures how *close in meaning* a guessed word is to the secret word.  
The game uses **vector embeddings** and **cosine similarity** to generate accurate semantic rankings.

---

## 🚀 Features

- 🔤 Semantic word guessing with ranked feedback
- 🧠 NLP-based similarity using **GloVe embeddings**
- 💡 Progressive hint system (3 levels: weak → strong)
- 🚩 Give-up option to reveal the secret word
- 🔄 New Game / Play Again functionality
- 📖 Built-in *How to Play* guide
- 🎨 Clean, modern UI inspired by *Contexto*
- ⚡ Rankings computed once per game (performance optimized)

---

## 🕹️ How to Play

1. Enter a word and submit your guess  
2. The game returns a **rank** based on semantic similarity  

### Rank Interpretation

| Rank | Meaning |
|----|--------|
| **1** | 🎉 Correct word |
| Lower | Closer in meaning |
| Higher | Farther in meaning |

3. Use up to **3 hints** if needed  
4. Give up anytime to reveal the secret word  
5. Start a **New Game** to play again  

---

## 🛠️ Tech Stack

### Backend
- **Django**

### NLP & Data
- **Gensim**
- **GloVe** (`glove-wiki-gigaword-50`)
- **wordfreq** (frequency-based vocabulary filtering)

### Frontend
- HTML  
- CSS  
- Vanilla JavaScript  

### State Management
- Django Sessions

---

## ⚙️ Architecture

