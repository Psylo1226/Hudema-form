import json
import os
from preprocess import preprocess,lemmatize_text
from download import download_file
import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import spacy
nlp = spacy.load("pl_core_news_sm")

file_path = "lemmatized_courses.json"
# Tworzenie modelu TF-IDF
polish_stopwords = ["i", "w", "na", "do", "że", "ten", "jak", "ale", "jest", "czy", "oraz", "być", "są","pod"]

if not os.path.exists(file_path):
    try:
        download_file(file_path)
    except Exception as e:
        print(f"Błąd podczas pobierania pliku: {e}")
        #preprocess()
        exit(1)

# Wczytanie pliku JSON
with open(file_path, "r", encoding="utf-8") as f:
    courses = json.load(f)


# Przygotowanie wektorów na podstawie lematyzowanych tekstów
course_texts = [c["lemmatized_text"] for c in courses]
course_names = [c["course_name"] for c in courses]

# Tworzenie modelu TF-IDF
vectorizer = TfidfVectorizer(stop_words=polish_stopwords, ngram_range=(1, 3))
course_vectors = vectorizer.fit_transform(course_texts)


def recommend_courses(search_topic, search_skills, search_level, weights=(0.6, 0.3, 0.1), top_n=3):
    # Lematyzacja promptów
    lemmatized_search_topic = lemmatize_text(search_topic)
    lemmatized_search_skills = lemmatize_text(search_skills)
    lemmatized_search_level = lemmatize_text(search_level)

    # Łączymy różne części zapytania w jeden wektor
    query_texts = [lemmatized_search_topic, lemmatized_search_skills, lemmatized_search_level]

    # Wektoryzacja każdej części zapytania osobno
    query_vectors = [vectorizer.transform([text]) for text in query_texts]

    # Obliczamy podobieństwo dla każdej części
    similarities = [cosine_similarity(qv, course_vectors).flatten() for qv in query_vectors]

    # Łączymy wyniki zgodnie z wagami
    total_similarity = (
        weights[0] * similarities[0] +
        weights[1] * similarities[1] +
        weights[2] * similarities[2]
    )

    # Sortujemy kursy według łącznego podobieństwa i wybieramy top_n
    top_n_idx = np.argsort(total_similarity)[-top_n:][::-1]

    # Zbieramy informacje o najlepszych kursach
    top_courses = []
    for idx in top_n_idx:
        best_course = courses[idx]
        course_name = best_course["course_name"]
        course_goals = best_course["course_goals"]
        course_program = best_course["course_program"]
        top_courses.append((course_name, course_goals, course_program))

    return top_courses


