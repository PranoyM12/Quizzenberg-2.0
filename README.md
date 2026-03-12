# Quizzenberg v2 🧠🔥 MySQL Edition

**Interactive Biochemistry Quiz Game with Database Backend, Certificate Generation & Auto-Email Delivery**

[![MIT License](https://img.shields.io/badge/license-MIT-blue.svg)](LICENSE)
[![Python](https://img.shields.io/badge/python-3.7+-blue.svg)](requirements.txt)

## ✨ Features

- **MySQL Database** - Dynamic questions/options (scalable)
- **Interactive GUI** - Tkinter with sound effects (Pygame)
- **Smart Scoring** - 5 pts/question, tiered feedback
- **Certificate Generation** - OpenCV overlays name/score
- **Auto-Email** - Outlook integration with attachments
- **Production Ready** - Error handling, clean code

## 🎮 Demo Flow
```Welcome → 5 Random Questions → Score + Image/Sound → Name/Email → Certificate Email```

## 🗄️ Database Setup

**MySQL (`india` database):**
```sql
CREATE DATABASE india;
USE india;

CREATE TABLE questions (
    id INT PRIMARY KEY,
    question TEXT
);

CREATE TABLE options (
    id INT PRIMARY KEY,
    opt1 TEXT, opt2 TEXT, opt3 TEXT, opt4 TEXT
);
```

## 🗄️ Database Setup (1 Command!)

```bash
mysql -u root -p < database.sql
```

Sample Data (10 questions):

Carbohydrates, Proteins, Vitamins, Elements

Hardcoded answers: [2,1,3,1,0,3,2,1,0,1]

🚀 Quick Start
```bash
# 1. Clone & Install
git clone https://github.com/yourusername/Quizzenberg-v2.git
cd Quizzenberg-v2
pip install -r requirements.txt

# 2. Setup MySQL (localhost/india)
# 3. Add assets: Images/, Sounds/
# 4. Run!
python Quizzenberg 2.0.py
```

📁 Assets Required
```text
Images/
├── QUIZ(2).png
├── Start.png
├── great.png, ok.png, bad.png
└── Certificate of Excellence.png

Sounds/
├── winner.mp3, good.mp3, lost.mp3
└── correct(1).wav
```
🛠️ Local Setup Notes
1. Windows-only (Outlook paths)
2. Update paths in certify() for your system
3. MySQL: ```root/pranoy@localhost/india```

🔧 Tech Stack
```text
Frontend: Tkinter
Database: MySQL Connector
Images: OpenCV
Audio: Pygame
Email: Win32COM
```

📊 v1 → v2 Improvements
| Feature     | v1              | v2          |
| ----------- | --------------- | ----------- |
| Questions   | Hardcoded lists | ✅ MySQL     |
| Scalability | Fixed 10        | ✅ Unlimited |
| Maintenance | Edit Python     | ✅ Edit DB   |

🤝 Contributing
Fork → Branch → PR. Issues welcome!

📄 License
MIT © 2026 Pranoy Mridha

⭐ Star if useful! Questions? Open an issue.
