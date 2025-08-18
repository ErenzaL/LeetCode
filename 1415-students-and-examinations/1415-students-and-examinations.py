import pandas as pd

def students_and_examinations(students: pd.DataFrame, subjects: pd.DataFrame, examinations: pd.DataFrame) -> pd.DataFrame:
    student_df = students.merge(subjects, how = 'cross')
    student_df.sort_values(by = ['student_id','subject_name'], inplace = True)

    exam = examinations.groupby(['subject_name','student_id'], as_index = False).size()
    student_exam = student_df.merge(exam, on = ['student_id','subject_name'], how = 'left')
    student_exam['size'].fillna(0, inplace = True)
    return student_exam.rename(columns = {'size': 'attended_exams'})
