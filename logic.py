import json
import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import nltk

# Wczytanie pliku JSON
with open("coursedata 1.json", "r", encoding="utf-8") as f:
    courses = json.load(f)

# Łączenie pól tekstowych kursów
course_texts = [" ".join([c["course_name"], c["course_goals"], c["course_results"], c["course_program"]]) for c in courses]
course_names = [c["course_name"] for c in courses]

# Tworzenie modelu TF-IDF
nltk.download("stopwords")
nltk.download('punkt')
polish_stopwords = ["i", "w", "na", "do", "że", "ten", "jak", "ale", "jest", "czy", "oraz", "być", "są","pod"]

vectorizer = TfidfVectorizer(stop_words=polish_stopwords)
course_vectors = vectorizer.fit_transform(course_texts)

def recommend_course(user_input):
    user_vector = vectorizer.transform([user_input])
    similarities = cosine_similarity(user_vector, course_vectors).flatten()
    best_match_idx = np.argmax(similarities)
    return course_names[best_match_idx]
