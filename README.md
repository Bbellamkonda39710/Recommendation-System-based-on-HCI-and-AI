# Recommendation-System-based-on-HCI-and-AI

# Project Description

The use of artificial intelligence methods and human-computer interaction concepts were incorporated in creating a movie recommendation system. An IMDB movie dataset was used to generate movie suggestions. Content based filtering with TF-IDF and cosine similarity are used in the system to suggest movies that are alike the preferences of the user.

# Features
The system will have features like the recommendation of similar movies, the recommendation of movies by genre and the display of popular movies to the users. It also offers interactive menu-based, text-driven interface which improves the human-computer interaction and easy navigation.

# Dataset

The data utilized in this project is IMDB movie-based. It contains movie title, genre, description, director, actors, rating, votes, and revenue. These characteristics are used to detect the similarities between films.

# Technologies Used

Python and libraries like Pandas and NumPy were used to implement the project and handle and preprocess data. TF-IDF vectorization and cosine similarity were applied with the help of scikit-learn to create correct movie recommendations.

# System Workflow

The system workflow involves loading the dataset, which is then followed by cleaning of the data by removing any missing and duplicate value. Other key attributes like genre, director, actors, and description are then concatenated and vectorised with the help of TF-IDF, and cosine similarity is then computed to determine the correlation between movies. The system uses these similarity scores to give movie recommendations and present the results in an interactive menu-driven interface that is easy to interact with.

# Sample Execution

**Input:**
Select Option: 1
Enter movie name: La La Land

**Output:**
Recommended Movies:

Rules Don't Apply
The Neon Demon
Straight Outta Compton
The Nice Guys
Inherent Vice

# Learning Outcomes

The project aided in the knowledge of the recommendation systems and application of content-based filtering based on TF-IDF and cosine similarity. It also led to the improvement of the skills in data preprocessing and development of the user-friendly interactive intelligent system.

# Future improvements

Future improvements in the code include adding a graphical user interface (GUI) to enhance user interaction and deploying the system as a web application for wider accessibility
