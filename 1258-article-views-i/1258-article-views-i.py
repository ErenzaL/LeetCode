import pandas as pd

def article_views(views: pd.DataFrame) -> pd.DataFrame:
    df = views.loc[views['author_id'] == views['viewer_id']]
    df = df.drop_duplicates(subset=['author_id','viewer_id']).sort_values(by='author_id')
    df = df[['author_id']].rename(columns= {'author_id' : 'id'})
    return df