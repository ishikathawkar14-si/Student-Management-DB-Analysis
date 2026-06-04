# Project Structure

```
student-management-db/
├── README.md                  # Project documentation
├── requirements.txt           # Python dependencies
├── .gitignore                # Git ignore rules
├── main.py                    # Main analysis script
├── queries.py                 # SQL queries dictionary
├── students_data.csv          # Sample student data
└── student_dashboard.png      # Generated visualization (after running)
```

## File Descriptions

### README.md
Complete project documentation including features, database schema, queries, and tech stack.

### requirements.txt
Python package dependencies for the project:
- pandas: Data manipulation
- numpy: Numerical computing
- matplotlib: Visualization
- seaborn: Statistical visualization
- jupyter: Interactive notebooks
- ipython: Enhanced Python shell

### main.py
Main Python script that:
- Creates SQLite database
- Loads student data from CSV
- Executes all SQL queries
- Generates professional visualizations
- Uses pastel color palette

### queries.py
Contains all SQL queries for analysis:
- all_students: All records
- average_scores: Subject averages
- top_performer: Highest scoring student
- grade_distribution: Student count by grade
- high_math_achievers: Math > 80
- gender_analysis: Performance by gender

### students_data.csv
Sample dataset with 20 student records including:
- StudentID, Name, Grade, Gender
- Math, Science, English scores
- Attendance percentage
- Date enrolled

## Setup Instructions

1. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

2. Run analysis:
   ```bash
   python main.py
   ```

3. Output:
   - Console: Query results and metrics
   - File: student_dashboard.png (6-panel visualization)
   - File: students.db (SQLite database)

## Author
Ishika | Data Science & Analytics Intern
Maincrafts Technology | Intern ID: MT5500
June 2026
