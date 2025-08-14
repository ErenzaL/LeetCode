import pandas as pd

def calculate_special_bonus(employees: pd.DataFrame) -> pd.DataFrame:
    even_id = employees['employee_id'] % 2 == 0
    name_starts_with_m = employees['name'].str.startswith('M')
    employees['bonus'] = employees['salary'].where(~(even_id | name_starts_with_m), 0)
    employees = employees[['employee_id', 'bonus']].sort_values(by= 'employee_id')

    return employees