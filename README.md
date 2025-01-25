
# 🎯 Guess the Number Game

A fun, interactive Python game where you challenge yourself to guess a randomly generated number! Test your intuition and aim for the leaderboard by guessing the number in the fewest tries. 🎉

---

## 🕹️ How to Play

1. Run the program.
2. Enter your name.
3. Choose a range for the random number (e.g., 1 to 100).
4. Start guessing! Hints will guide you:
   - "Too high!" means your guess is above the target.
   - "Go higher!" means you're below the target.
5. Keep going until you guess correctly.
6. Your score (number of tries) will be recorded in the leaderboard. Can you top it?

---
Ready to play? [Play Now](https://pranavkhaspa.github.io/guess-the-number/)


## 📋 Features

- **Dynamic Difficulty:** You decide the range for the number.
- **Hints Provided:** Receive real-time feedback on your guesses.
- **Persistent Leaderboard:** Scores are saved to `scores.csv` and persist across sessions.
- **Simple Setup:** No external dependencies required—just Python!

---

## 🛠️ Getting Started

### Prerequisites

- Python 3.x installed on your system.

### Installation

1. Clone this repository:
   ```bash
   git clone https://github.com/pranavkhaspa/guess-the-number-game.git       
                                  cd guess-the-number-game
   ```

2. Run the script:
   ```bash
   python guess_the_number.py
   ```

---

## 🌟 Leaderboard System

Your scores are saved in `scores.csv` in the following format:

```
name,Leaderboard position
Alice,3
Bob,5
```

- **Leaderboard Logic:** The best score (fewest tries) is always at the top.
- If it's your first time playing, a new `scores.csv` file will be created.

---

## 📂 File Structure

```
|-- guess_the_number.py   # Main game script
|-- scores.csv            # Automatically created leaderboard file
```

---

## 📖 Example Gameplay

```
Enter your name > John
Enter the starting range > 1
Enter the end range > 20
Guess the number > 15
Too high! Try again!
Guess the number > 8
Go higher! Try again!
Guess the number > 10
John, you guessed it right in 3 tries!!
```

---

## 🚀 Future Improvements

- Improve leaderboard functionality with timestamps.
- Create a GUI version of the game.

---

## 🤝 Contributions

Want to enhance the game? Contributions are welcome! Fork this repository, implement your changes, and submit a pull request. Let’s build something awesome together! 🚀

---

## 📜 License

This project is open-source! Feel free to use, modify, and share it. Your creativity is the limit! 🎉

---

### 🎮 Ready to Play?

Clone the repository and start guessing your way to victory! 🔥  
Or simply visit the game online: [Play Now](https://pranavkhaspa.github.io/guess-the-number/)


