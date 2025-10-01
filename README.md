🩺 Pathology Hangman (Python)

A fun twist on the classic **Hangman game** built in Python, where you guess **pathology terms** based on clues. Perfect for medical students to learn while playing!

✨ Features

* Randomly selects a medical term from a predefined word bank.
* **Easy & Hard terms** with corresponding clues.
* Shows word progress with underscores (`_`).
* Tracks number of **lives (6 chances)**.
* Prevents repeating letters.
* Victory and defeat messages.
* Option to **play again** after each round.

🛠️ Technologies Used

* **Python 3**
* Built-in libraries only (`random`, `string`).

---



📜 Rules of the Game

1. You have **6 lives**.
2. Each round, you see a **clue** about the pathology term.
3. Guess one letter at a time.
4. Correct guess → letter revealed in the word.
5. Wrong guess → you lose a life.
6. Win if you guess all letters before lives run out.
7. Lose if lives reach 0 (the correct term will be shown).


📸 Example Gameplay

```
🎉 Welcome to Pathology Hangman! 🎉
Try to guess the word based on the clue. You have 6 lives.

👉 Clue: Swelling, redness, and pain due to injury or infection.

Word: _ _ _ _ _ _ _ _ _ _ _ _
❤️ Lives left: 6
👉 Enter your guess (a single letter): i

Word: i _ _ _ _ _ _ _ _ i _ _
❤️ Lives left: 6
👉 Enter your guess (a single letter): z
❌ Z is not in the word.
❤️ Lives left: 5
```
 me to also add an **ASCII gallows drawing** for each life lost (like 👤, rope, etc.) in the Python version? Would make it more fun for players.
