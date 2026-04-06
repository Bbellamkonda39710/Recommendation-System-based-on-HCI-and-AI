# Importing required libraries
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# Loading dataset
df = pd.read_csv("C:/Work/IMDB-Movie-Data.csv")

# Cleaning duplicate rows
df = df.drop_duplicates()

# Selecting required columns
df = df[['Title', 'Genre', 'Description', 'Rating', 'Votes']]

# Renaming columns for simplicity
df.columns = ['name', 'category', 'description', 'rating', 'votes']

# Removing missing values
df = df.dropna(subset=['name', 'category', 'description'])

# Converting numeric data types (fixed syntax error)
df['rating'] = pd.to_numeric(df['rating'], errors='coerce')
df['votes'] = pd.to_numeric(df['votes'], errors='coerce')

# Filling missing values
df['rating'] = df['rating'].fillna(df['rating'].mean())
df['votes'] = df['votes'].fillna(0)

# Creating combined text feature
df['content'] = df['category'] + " " + df['description']

# Resetting index values
df = df.reset_index(drop=True)

# Building TF-IDF matrix
tfidf = TfidfVectorizer(stop_words='english')
matrix = tfidf.fit_transform(df['content'])

# Computing cosine similarity
sim = cosine_similarity(matrix)

# Mapping movie names to indices
index_map = pd.Series(df.index, index=df['name']).drop_duplicates()

# Printing system header
print("\n🎬 IMDB Movie Recommendation System")

while True:
    # Displaying menu options
    print("\n1. Recommend similar movies")
    print("2. Recommend by genre")
    print("3. Show popular movies")
    print("4. Exit")

    # Getting user choice
    choice = input("Enter choice: ")

    # Handling similar movie recommendation
    if choice == "1":
        movie = input("Enter movie title: ")

        # Checking movie availability
        if movie not in index_map:
            print("Movie not found.")
            continue

        idx = index_map[movie]

        # Calculating similarity scores
        scores = list(enumerate(sim[idx]))
        scores = sorted(scores, key=lambda x: x[1], reverse=True)

        top = scores[1:6]
        indices = [i[0] for i in top]

        # Displaying recommendations
        print("\nRecommended Movies:")
        print(df.loc[indices, ['name', 'category', 'rating']])

    # Handling genre based recommendation
    elif choice == "2":
        genre = input("Enter genre: ")

        # Filtering movies by genre
        filtered = df[df['category'].str.lower().str.contains(genre.lower())]

        # Checking empty results
        if filtered.empty:
            print("No movies found.")
        else:
            # Sorting top rated movies
            result = filtered.sort_values(
                ['rating', 'votes'],
                ascending=False
            ).head(5)

            # Displaying genre results
            print("\nTop Movies in Genre:")
            print(result[['name', 'category', 'rating']])

    # Handling popular movies
    elif choice == "3":
        # Sorting popular movies
        popular = df.sort_values(
            ['rating', 'votes'],
            ascending=False
        ).head(5)

        # Displaying popular list
        print("\nPopular Movies:")
        print(popular[['name', 'category', 'rating']])

    # Handling exit option
    elif choice == "4":
        print("Exiting system...")
        break

    # Handling invalid input
    else:
        print("Invalid input, try again.")