from flask import Flask, render_template, request, redirect, url_for, session, flash
import sqlite3
import random
from datetime import datetime

app = Flask(__name__)
app.secret_key = 'iam100k'

def get_db_connection():
    conn = sqlite3.connect('quiz.db')
    conn.row_factory = sqlite3.Row
    return conn

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/start_quiz', methods=['POST'])
def start_quiz():
    username = request.form.get('username')
    if not username:
        flash('Please enter your name!')
        return redirect(url_for('home'))
    
    session['username'] = username
    session['score'] = 0
    session['question_count'] = 0
    session['answered_questions'] = []
    
    return redirect(url_for('quiz'))

@app.route('/quiz')
def quiz():
    if 'username' not in session:
        return redirect(url_for('home'))
    
    conn = get_db_connection()
    
    # Get a random question that hasn't been answered
    answered_ids = session.get('answered_questions', [])
    if answered_ids:
        questions = conn.execute(
            'SELECT * FROM questions WHERE id NOT IN ({})'.format(','.join('?' * len(answered_ids))),
            answered_ids
        ).fetchall()
    else:
        questions = conn.execute('SELECT * FROM questions').fetchall()
    
    conn.close()
    
    if not questions:
        return redirect(url_for('results'))
    
    question = random.choice(questions)
    session['current_question_id'] = question['id']
    session['current_answer'] = question['answer']
    
    return render_template('quiz.html', question=question)

@app.route('/submit_answer', methods=['POST'])
def submit_answer():
    if 'username' not in session:
        return redirect(url_for('home'))
    
    user_answer = request.form.get('answer', '').strip()
    correct_answer = session.get('current_answer', '')
    
    session['question_count'] += 1
    session['answered_questions'].append(session['current_question_id'])
    
    if user_answer.lower() == correct_answer.lower():
        session['score'] += 1
        flash('Correct!', 'success')
    else:
        flash(f'Wrong! The correct answer was: {correct_answer}', 'error')
    
    return redirect(url_for('quiz'))

@app.route('/results')
def results():
    if 'username' not in session:
        return redirect(url_for('home'))
    
    # Save score to database
    conn = get_db_connection()
    conn.execute(
        'INSERT INTO scores (username, score, total_questions) VALUES (?, ?, ?)',
        (session['username'], session['score'], session['question_count'])
    )
    conn.commit()
    
    # Get high scores
    high_scores = conn.execute(
        'SELECT username, score, total_questions, date FROM scores ORDER BY score DESC, date DESC LIMIT 10'
    ).fetchall()
    
    conn.close()
    
    user_score = session['score']
    total_questions = session['question_count']
    username = session['username']
    
    # Clear session
    session.clear()
    
    return render_template('results.html', 
                         user_score=user_score, 
                         total_questions=total_questions,
                         username=username,
                         high_scores=high_scores)

@app.route('/add_question')
def add_question():
    return render_template('add_question.html')

@app.route('/submit_question', methods=['POST'])
def submit_question():
    question = request.form.get('question')
    answer = request.form.get('answer')
    
    if question and answer:
        conn = get_db_connection()
        conn.execute('INSERT INTO questions (question, answer) VALUES (?, ?)', 
                    (question, answer))
        conn.commit()
        conn.close()
        flash('Question added successfully!', 'success')
    else:
        flash('Please fill in both fields!', 'error')
    
    return redirect(url_for('add_question'))

@app.route('/show_score')
def show_current_score():
    if 'username' not in session:
        return redirect(url_for('home'))
    
    # Save current score to database
    conn = get_db_connection()
    conn.execute(
        'INSERT INTO scores (username, score, total_questions) VALUES (?, ?, ?)',
        (session['username'], session['score'], session['question_count'])
    )
    conn.commit()
    
    # Get high scores
    high_scores = conn.execute(
        'SELECT username, score, total_questions, date FROM scores ORDER BY score DESC, date DESC LIMIT 10'
    ).fetchall()
    
    conn.close()
    
    user_score = session['score']
    total_questions = session['question_count']
    username = session['username']
    
    # Clear session
    session.clear()
    
    return render_template('results.html', 
                         user_score=user_score, 
                         total_questions=total_questions,
                         username=username,
                         high_scores=high_scores,
                         early_exit=True)


if __name__ == '__main__':
    app.run(debug=True)
