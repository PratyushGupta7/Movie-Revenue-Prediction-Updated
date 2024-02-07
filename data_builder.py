import pandas as pd

def merge_datasets():
    df1 = pd.read_csv('datasets/movies.csv')
    df2 = pd.read_csv('datasets/budget.csv')

    df2['movie_title'] = df2['movie_title'].str.rstrip()

    merged_df = pd.merge(df1, df2, left_on='name', right_on='movie_title', how='inner')

    return merged_df

def remove_duplicates(df):
    cols_to_drop = ['movie_title', 'plot_keywords', 'movie_imdb_link', 'language', 'country_x', 'country_y', 'content_rating', 'color', 'duration', 'facenumber_in_poster', 'movie_facebook_likes', 'num_voted_users', 'num_user_for_reviews', 'num_critic_for_reviews', 'title_year', 'aspect_ratio', 'director_facebook_likes', 'actor_3_facebook_likes', 'actor_2_facebook_likes', 'actor_1_facebook_likes', 'cast_total_facebook_likes', 'company', 'released', 'votes', 'rating', 'writer', 'year', 'runtime', 'director_name', 'genres', 'imdb_score', 'star', 'actor_3_name', 'budget_x']
    df.drop(cols_to_drop, axis=1, inplace=True)

    df.drop_duplicates(subset=['name'], inplace=True)

    return df

def write_to_csv(df, filename):
    df.to_csv(filename, index=False)

def main():
    merged_df = merge_datasets()
    cleaned_df = remove_duplicates(merged_df)
    write_to_csv(cleaned_df, 'final_dataset.csv')

if __name__ == "__main__":
    main()