import pandas as pd
from sklearn.metrics.pairwise import cosine_similarity
from sklearn.model_selection import train_test_split
data = {
    'User': ['User1', 'User2', 'User3', 'User4', 'User5'],
    'Movie1': [5, 4, 0, 0, 1],
    'Movie2': [4, 5, 0, 1, 2],
    'Movie3': [0, 0, 5, 4, 2],
    'Movie4': [0, 1, 4, 5, 0],
    'Movie5': [1, 2, 0, 0, 5]
}

df = pd.DataFrame(data)
train_data, test_data = train_test_split(df, test_size=0.2)
user_similarity = cosine_similarity(train_data.iloc[:, 1:])
def recommend_movies(user, num_recommendations=5):
    user_index = df[df['User'] == user].index[0]
    user_ratings = train_data.iloc[user_index, 1:]
    weighted_avg = user_similarity[user_index].dot(user_ratings)
    recommended_movies = df.columns[1:][user_ratings == 0]
    recommended_movies = sorted(recommended_movies, key=lambda x: weighted_avg[df.columns.get_loc(x)], reverse=True)
    return recommended_movies[:num_recommendations]
target_user = 'User1'
recommended_movies = recommend_movies(target_user)
print(f"Recommended movies for {target_user}: {', '.join(recommended_movies)}")
