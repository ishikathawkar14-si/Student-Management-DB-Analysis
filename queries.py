"""SQL Queries for Student Management Analysis"""

QUERIES = {
    "all_students": "SELECT * FROM Students;",
    
    "average_scores": """
        SELECT 
            ROUND(AVG(MathScore), 2) AS AvgMath,
            ROUND(AVG(ScienceScore), 2) AS AvgScience,
            ROUND(AVG(EnglishScore), 2) AS AvgEnglish
        FROM Students;
    """,
    
    "top_performer": """
        SELECT 
            Name,
            Grade,
            MathScore,
            ScienceScore,
            EnglishScore,
            (MathScore + ScienceScore + EnglishScore) AS TotalScore
        FROM Students
        ORDER BY TotalScore DESC
        LIMIT 1;
    """,
    
    "grade_distribution": """
        SELECT 
            Grade,
            COUNT(*) AS StudentCount
        FROM Students
        GROUP BY Grade
        ORDER BY Grade;
    """,
    
    "high_math_achievers": """
        SELECT 
            Name,
            MathScore,
            Grade
        FROM Students
        WHERE MathScore > 80
        ORDER BY MathScore DESC;
    """,
    
    "gender_analysis": """
        SELECT 
            Gender,
            ROUND(AVG(MathScore), 2) AS AvgMath,
            ROUND(AVG(ScienceScore), 2) AS AvgScience,
            ROUND(AVG(EnglishScore), 2) AS AvgEnglish,
            ROUND(AVG(MathScore + ScienceScore + EnglishScore), 2) AS AvgTotal
        FROM Students
        GROUP BY Gender;
    """
}
