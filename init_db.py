import sqlite3

def create_database():
    conn = sqlite3.connect('quiz.db')
    c = conn.cursor()
    # Create questions table
    c.execute('''CREATE TABLE IF NOT EXISTS questions (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        question TEXT NOT NULL,
        answer TEXT NOT NULL
    )''')
    
    # Create scores table
    c.execute('''CREATE TABLE IF NOT EXISTS scores (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        username TEXT NOT NULL,
        score INTEGER NOT NULL,
        total_questions INTEGER NOT NULL,
        date TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    )''')
    
    # Insert sample questions
    sample_questions = [
        ("What is the capital of France?", "Paris"),
        ("What is 2 + 2?", "4"),
        ("Who wrote Romeo and Juliet?", "Shakespeare"),
        ("What is the largest planet in our solar system?", "Jupiter"),
        ("What year did World War II end?", "1945")
    ]
    
    c.executemany("INSERT OR IGNORE INTO questions (question, answer) VALUES (?, ?)", 
                  sample_questions)
    
    conn.commit()
    conn.close()
    print("Database created successfully!")

if __name__ == '__main__':
    create_database()
