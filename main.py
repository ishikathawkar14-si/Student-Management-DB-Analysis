"""
Student Management Database Analysis
Author: Ishika
Maincrafts Technology | Intern ID: MT5500
June 2026
"""

import sqlite3
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from pathlib import Path

# Pastel color palette
PASTEL_COLORS = {
    'primary': '#FFB3BA',
    'secondary': '#FFCCCB',
    'accent1': '#FFE5B4',
    'accent2': '#B4E7FF',
    'accent3': '#D4F1D4',
    'accent4': '#E6D5FF'
}

class StudentDatabase:
    def __init__(self, db_path='students.db'):
        self.db_path = db_path
        self.conn = None
        
    def create_connection(self):
        """Create database connection"""
        self.conn = sqlite3.connect(self.db_path)
        return self.conn
    
    def create_table(self):
        """Create students table"""
        cursor = self.conn.cursor()
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS Students (
                StudentID INTEGER PRIMARY KEY,
                Name TEXT NOT NULL,
                Grade INTEGER NOT NULL,
                Gender TEXT NOT NULL,
                MathScore REAL NOT NULL,
                ScienceScore REAL NOT NULL,
                EnglishScore REAL NOT NULL,
                Attendance REAL NOT NULL,
                DateEnrolled TEXT NOT NULL
            )
        ''')
        self.conn.commit()
    
    def load_data(self, csv_file):
        """Load student data from CSV"""
        df = pd.read_csv(csv_file)
        df.to_sql('Students', self.conn, if_exists='replace', index=False)
        print(f"✓ Loaded {len(df)} student records")
    
    def execute_query(self, query_name, query):
        """Execute SQL query"""
        try:
            result = pd.read_sql_query(query, self.conn)
            return result
        except Exception as e:
            print(f"Error executing {query_name}: {e}")
            return None
    
    def generate_visualizations(self):
        """Generate analysis visualizations"""
        plt.style.use('seaborn-v0_8-darkgrid')
        
        # Get data
        df = pd.read_sql_query("SELECT * FROM Students", self.conn)
        
        # Create figure with subplots
        fig, axes = plt.subplots(2, 3, figsize=(15, 10))
        fig.suptitle('Student Performance Dashboard', fontsize=16, fontweight='bold')
        
        # 1. Average scores by subject
        avg_scores = [df['MathScore'].mean(), df['ScienceScore'].mean(), df['EnglishScore'].mean()]
        axes[0, 0].bar(['Math', 'Science', 'English'], avg_scores, color=[PASTEL_COLORS['primary'], 
                                                                           PASTEL_COLORS['accent1'], 
                                                                           PASTEL_COLORS['accent2']])
        axes[0, 0].set_title('Average Scores by Subject')
        axes[0, 0].set_ylim(0, 100)
        
        # 2. Score distribution
        axes[0, 1].hist([df['MathScore'], df['ScienceScore'], df['EnglishScore']], 
                       label=['Math', 'Science', 'English'], 
                       bins=10, 
                       color=[PASTEL_COLORS['primary'], PASTEL_COLORS['accent1'], PASTEL_COLORS['accent2']])
        axes[0, 1].set_title('Score Distribution')
        axes[0, 1].legend()
        
        # 3. Gender performance
        gender_data = df.groupby('Gender')[['MathScore', 'ScienceScore', 'EnglishScore']].mean()
        gender_data.plot(kind='bar', ax=axes[0, 2], color=[PASTEL_COLORS['primary'], 
                                                           PASTEL_COLORS['accent1'], 
                                                           PASTEL_COLORS['accent2']])
        axes[0, 2].set_title('Performance by Gender')
        axes[0, 2].set_ylabel('Average Score')
        
        # 4. Grade distribution
        grade_counts = df['Grade'].value_counts().sort_index()
        axes[1, 0].bar(grade_counts.index, grade_counts.values, color=PASTEL_COLORS['accent3'])
        axes[1, 0].set_title('Student Distribution by Grade')
        axes[1, 0].set_xlabel('Grade')
        
        # 5. Attendance vs Performance
        df['AvgScore'] = (df['MathScore'] + df['ScienceScore'] + df['EnglishScore']) / 3
        axes[1, 1].scatter(df['Attendance'], df['AvgScore'], alpha=0.6, color=PASTEL_COLORS['accent4'], s=100)
        axes[1, 1].set_title('Attendance vs Average Performance')
        axes[1, 1].set_xlabel('Attendance %')
        axes[1, 1].set_ylabel('Average Score')
        
        # 6. Top performers
        top_5 = df.nlargest(5, 'AvgScore')[['Name', 'AvgScore']]
        axes[1, 2].barh(top_5['Name'], top_5['AvgScore'], color=PASTEL_COLORS['primary'])
        axes[1, 2].set_title('Top 5 Performers')
        axes[1, 2].set_xlabel('Average Score')
        
        plt.tight_layout()
        plt.savefig('student_dashboard.png', dpi=300, bbox_inches='tight')
        print("✓ Dashboard saved as 'student_dashboard.png'")
        plt.close()
    
    def close(self):
        """Close database connection"""
        if self.conn:
            self.conn.close()


def main():
    """Main execution"""
    print("🎓 Student Management Database Analysis")
    print("-" * 50)
    
    # Initialize database
    db = StudentDatabase()
    db.create_connection()
    db.create_table()
    
    # Load data
    if Path('students_data.csv').exists():
        db.load_data('students_data.csv')
    else:
        print("⚠ students_data.csv not found")
        return
    
    # Import queries
    from queries import QUERIES
    
    # Execute all queries
    print("\n📊 Executing Analysis Queries:")
    print("-" * 50)
    
    for query_name, query in QUERIES.items():
        result = db.execute_query(query_name, query)
        if result is not None:
            print(f"\n✓ {query_name}")
            print(result.to_string())
    
    # Generate visualizations
    print("\n📈 Generating Visualizations...")
    db.generate_visualizations()
    
    db.close()
    print("\n✓ Analysis Complete!")


if __name__ == "__main__":
    main()
