# Flask Quiz Application

A modern, interactive web-based quiz platform built with Flask and SQLite that transforms knowledge testing into an engaging experience. This application features real-time scoring, flexible quiz controls, and a beautiful custom-designed interface with seamless question management capabilities.

## ✨ Key Features

- **🎯 Interactive Quiz Experience** - Start quizzes instantly with your name and get immediate feedback
- **⚡ Smart Exit Controls** - End your quiz anytime with "Show Final Score" to see results instantly
- **📝 Easy Question Management** - Add new questions directly from the home page without complex admin panels
- **🏆 Live Leaderboard** - Track high scores and compare your performance with others
- **📱 Responsive Design** - Optimized for desktop, tablet, and mobile devices
- **🎨 Custom Theme** - Beautiful teal-to-purple color scheme for enhanced user experience
- **⚙️ Session Management** - Secure user sessions with automatic score tracking

## 🚀 Quick Start

### Prerequisites
- Python 3.7 or higher
- pip (Python package installer)

### Installation
```bash
# Clone the repository
git clone https://github.com/yourusername/flask-quiz-app.git
cd flask-quiz-app

# Install dependencies
pip install Flask

# Initialize the database with sample questions
python init_db.py

# Launch the application
python app.py
```

**🌐 Access the app at:** `http://localhost:5000`

## 🎮 How to Use

### Playing a Quiz
1. **Enter your name** on the welcome screen
2. **Click "Start Quiz"** to begin your knowledge test
3. **Answer questions** by typing your responses
4. **Monitor your progress** with the real-time score display
5. **Exit anytime** using "Show Final Score" or continue until completion
6. **View results** and check the leaderboard

### Contributing Questions
1. **Click "Add New Question"** from the home page or navigation
2. **Enter your question** and the correct answer
3. **Submit** to instantly add it to the quiz database
4. **Your question** becomes available for all future quizzes

## 🏗️ Project Architecture

```
flask-quiz-app/
├── 📄 app.py                    # Main Flask application & routes
├── 🗄️ init_db.py               # Database initialization script
├── 📋 requirements.txt          # Python dependencies
├── 📊 quiz.db                   # SQLite database (auto-generated)
├── 🎨 static/
│   └── style.css               # Custom styling & responsive design
└── 📄 templates/
    ├── base.html               # Base template with navigation
    ├── home.html               # Welcome page with quiz start
    ├── quiz.html               # Interactive quiz interface
    ├── add_question.html       # Question submission form
    └── results.html            # Score display & leaderboard
```

## 🎨 Design System

### Color Palette
| Color | Hex Code | Usage |
|-------|----------|-------|
| Soft Teal | `#78B9B5` | Primary buttons, CTAs |
| Medium Teal | `#0F828C` | Hover effects, secondary actions |
| Deep Blue | `#065084` | Navigation, primary text |
| Royal Purple | `#320A6B` | Highlights, final scores |

### UI Components
- **Navigation Bar** - Fixed top navigation with contextual links
- **Quiz Interface** - Clean question display with progress indicators
- **Score Display** - Real-time feedback with percentage calculations
- **Responsive Layout** - Mobile-first design with flexible grid system

## 🗃️ Database Schema

### Questions Table
```sql
CREATE TABLE questions (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    question TEXT NOT NULL,
    answer TEXT NOT NULL
);
```

### Scores Table
```sql
CREATE TABLE scores (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    username TEXT NOT NULL,
    score INTEGER NOT NULL,
    total_questions INTEGER NOT NULL,
    date TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
```

## 🔧 Configuration & Extension

### Environment Setup
```python
# Development mode
app.run(debug=True)

# Production mode
app.run(host='0.0.0.0', port=5000, debug=False)
```

### Adding New Features
The modular Flask structure supports easy extensions:
- **User Authentication** - Add login/registration system
- **Question Categories** - Organize questions by topic
- **Timed Quizzes** - Implement countdown timers
- **Difficulty Levels** - Add question complexity ratings
- **Multi-language Support** - Internationalization capabilities

## 🚛 Deployment Options

### Local Network
```bash
# Make accessible on local network
python app.py  # Then modify host in app.py to '0.0.0.0'
```

### Cloud Platforms
- **Heroku** - Git-based deployment with automatic builds
- **Railway** - Modern deployment with GitHub integration
- **PythonAnywhere** - Python-specific hosting solution
- **DigitalOcean** - VPS deployment with full control

### Production Checklist
- [ ] Set `debug=False` for production
- [ ] Configure environment variables for sensitive data
- [ ] Set up database backups
- [ ] Implement SSL/HTTPS
- [ ] Add error logging and monitoring

## 🔄 Development Workflow

### Git Workflow
```bash
# Feature development
git checkout -b feature/new-feature
git add .
git commit -m "feat: add new feature description"
git push origin feature/new-feature

# Create pull request for review
```

### Database Management
```bash
# Reset database
rm quiz.db && python init_db.py

# Backup database
cp quiz.db quiz_backup_$(date +%Y%m%
