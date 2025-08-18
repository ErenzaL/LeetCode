import pandas as pd

def sales_person(sales_person: pd.DataFrame, company: pd.DataFrame, orders: pd.DataFrame) -> pd.DataFrame:
    order_by_company = orders.merge(company, on = 'com_id', how = 'left')[['sales_id','name']]
    order_by_company.columns = ['sales_id','company_name']

    order_by_sales = order_by_company.merge(sales_person, on = 'sales_id', how = 'right')[['sales_id','name','company_name']]

    sales_Red = order_by_sales[order_by_sales['company_name'] == 'RED']
    
    sales_noRed = [name for name in sales_person['name'] if name not in set(sales_Red['name'])]
    sales_noRed = pd.DataFrame({'name': sales_noRed})
    return sales_noRed