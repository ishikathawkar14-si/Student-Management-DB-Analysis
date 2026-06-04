# 🎓 Student Management Database Analysis

![Python](https://img.shields.io/badge/Python-3.8+-blue)
![SQLite](https://img.shields.io/badge/Database-SQLite-blue)
![License](https://img.shields.io/badge/License-MIT-green)
![Status](https://img.shields.io/badge/Status-Active-brightgreen)

A professional SQL data analysis project demonstrating database design, query optimization, and data visualization with pastel aesthetic. Built for **Maincrafts Technology** SQL Data Analyst Internship.

## ✨ Features

- 🗄️ **SQLite Database** - Normalized schema with student records
- 🔍 **6 Advanced SQL Queries** - Comprehensive performance analysis
- 📊 **Professional Visualizations** - Custom pastel color palette
- 📈 **Interactive Dashboard** - 6-panel comprehensive metrics
- 🎨 **Production-Ready Code** - Clean, documented, optimized

## 📖 Table of Contents

- [Quick Start](#-quick-start)
- [Features](#-features)
- [Database Schema](#-database-schema)
- [SQL Queries](#-sql-queries)
- [Visualizations](#-visualizations)
- [Tech Stack](#-tech-stack)
- [Installation](#-installation)
- [Usage](#-usage)
- [Project Structure](#-project-structure)
- [Contributing](#-contributing)
- [License](#-license)

## 🚀 Quick Start

```bash
# 1. Extract the project
unzip Student-Management-DB-Analysis.zip
cd student-management-db

# 2. Install dependencies
pip install -r requirements.txt

# 3. Run the analysis
python main.py

# 4. View results
# - Console: SQL query results
# - File: student_dashboard.png (visualization)
# - File: students.db (SQLite database)
```

## 🎯 Features

### Students Table
```sql
 StudentID (PK)     → Unique identifier
Name              → Student name
Grade             → Academic grade level (9-12)
Gender            → Student gender (M/F)
MathScore         → Mathematics score (0-100)
ScienceScore      → Science score (0-100)
EnglishScore      → English score (0-100)
Attendance        → Attendance percentage
DateEnrolled      → Enrollment date
```

---

## 🔍 SQL Queries Included

1. **all_students** - Retrieve all student records
2. **average_scores** - Calculate average scores across subjects
3. **top_performer** - Identify highest-performing student
4. **grade_distribution** - Analyze student distribution by grade
5. **high_math_achievers** - Find students with Math score > 80
6. **gender_analysis** - Compare performance metrics by gender

---

## 📈 Key Visualizations
- Subject-wise score distribution
- Gender performance comparison
- Grade-level analysis
- Attendance vs performance correlation
- Top performers ranking
- Score distribution histograms

---

## 🛠️ Tech Stack

- **Database**: SQLite3
- **Language**: Python 3.9+
- **Visualization**: Matplotlib, Seaborn
- **Data Processing**: Pandas, NumPy

## 📥 Installation

### Prerequisites
- Python 3.8+
- pip (Python package manager)
- Git (optional, for cloning)

### Setup

1. **Clone or download the repository**
   ```bash
   git clone https://github.com/YOUR_USERNAME/Student-Management-DB-Analysis.git
   cd Student-Management-DB-Analysis
   ```

2. **Create virtual environment (recommended)**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Verify installation**
   ```bash
   python main.py
   ```

## 🎮 Usage

### Run Full Analysis
```bash
python main.py
```

This will:
- Create SQLite database from CSV
- Execute all 6 SQL queries
- Generate professional visualizations
- Display analysis metrics

### Use Specific Queries
```python
from queries import QUERIES
import sqlite3

conn = sqlite3.connect('students.db')
cursor = conn.cursor()

# Execute specific query
cursor.execute(QUERIES['top_performer'])
results = cursor.fetchall()
print(results)

conn.close()
```

### Customize Data
Edit `students_data.csv` with your own data:
```csv
StudentID,Name,Grade,Gender,MathScore,ScienceScore,EnglishScore,Attendance,DateEnrolled
1,Your Name,10,M,95,92,90,95,2026-06-01
```

## 📊 Project Structure

See [PROJECT_STRUCTURE.md](PROJECT_STRUCTURE.md) for detailed file descriptions.

```
├── main.py                 # Main analysis script
├── queries.py             # SQL queries
├── students_data.csv      # Sample data
├── requirements.txt       # Dependencies
├── README.md             # This file
├── LICENSE               # MIT License
├── CONTRIBUTING.md       # Contribution guide
└── .github/
    └── workflows/
        └── python-app.yml  # CI/CD pipeline
```

## 🤝 Contributing

Contributions are welcome! Please see [CONTRIBUTING.md](CONTRIBUTING.md) for details.

## 📄 License

This project is licensed under the MIT License - see [LICENSE](LICENSE) file for details.

### Attribution

**Ishika** | Data Science & Analytics Intern  
Maincrafts Technology | Intern ID: MT5500  
June 2026
