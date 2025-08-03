import pandas as pd

# Load the dataset
movies = pd.read_csv("movies.csv")

def recommend_by_genre(genre):
    # Filter movies containing the genre (case-insensitive)
    recommended = movies[movies['Genre'].str.contains(genre, case=False)]
    
    # Sort by rating (highest first)
    recommended = recommended.sort_values(by='Rating', ascending=False)
    return recommended[['Title', 'Rating']]

# --- Main Program ---
print("🎬 Welcome to the Mini Movie/Anime Recommender! 🎬")
user_genre = input("Enter a genre you like (Action, Fantasy, Romance, Adventure): ")

recommendations = recommend_by_genre(user_genre)

if not recommendations.empty:
    print("\n🔥 Here are some recommendations for you: 🔥\n")
    for idx, row in recommendations.iterrows():
        print(f"{row['Title']} - ⭐ {row['Rating']}")
else:
    print("\n😢 Sorry, no movies found for that genre.")