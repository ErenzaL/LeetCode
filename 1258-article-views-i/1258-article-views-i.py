import pandas as pd
import numpy as np

def article_views(views: pd.DataFrame) -> pd.DataFrame:
    df = views[views['author_id'] == views['viewer_id']]
    authors = np.sort(df['author_id'].unique())
    result = pd.DataFrame({'id': authors})
    return result
    