import pandas as pd

def calculate_special_bonus(employees: pd.DataFrame) -> pd.DataFrame:
    employees['bonus'] =[
    0 if (eid % 2 == 0 or name.startswith('M')) else salary
    for eid, name, salary in zip(employees['employee_id'], employees['name'], employees['salary'])]
    employees = employees[['employee_id', 'bonus']].sort_values(by ='employee_id')
    return employees
    