import sqlite3
import random

DB_FILE = "game.db"

# Initialize the database and create table if it does not exist
def init_db():
    with sqlite3.connect(DB_FILE) as conn:
        cur = conn.cursor()
        cur.execute("""
            CREATE TABLE IF NOT EXISTS guesses (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                player TEXT NOT NULL,
                guess INTEGER NOT NULL
            )
        """)
        conn.commit()
        
init_db()

# Generate a random number
SECRET_NUMBER = random.randint(1, 100)
print("\n🎮 Welcome to the CLI Number Guessing Game!")
print("🔢 Try to guess the secret number between 1 and 100!")

#Keep allow user enter a name and then guess a number
while True:
    player = input("\nEnter your name: ").strip()
    guess = input(f"{player}, enter your guess: ").strip()

    # if not guess.isdigit():
    #     print("❌ Invalid input! Please enter a number.")
    #     continue

    guess = int(guess)

    # Store the guess in SQLite database
    with sqlite3.connect(DB_FILE) as conn:
        cur = conn.cursor()
        cur.execute("INSERT INTO guesses (player, guess) VALUES (?, ?)", (player, guess))
        conn.commit()

    if guess == SECRET_NUMBER:
        print(f"🎉 Congratulations {player}! You guessed the correct number: {SECRET_NUMBER}!")
        break
    elif guess < SECRET_NUMBER:
        print("⬆️ Too low! Try again.")
    else:
        print("⬇️ Too high! Try again.")
