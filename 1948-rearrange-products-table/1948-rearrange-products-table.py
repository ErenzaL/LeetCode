import pandas as pd

def rearrange_products_table(products: pd.DataFrame) -> pd.DataFrame:
    products_melt = products.melt(
        id_vars = ['product_id'],
        var_name = 'store',
        value_name = 'price'
    )
    products_melt.dropna(subset = 'price', inplace = True)
    return products_melt