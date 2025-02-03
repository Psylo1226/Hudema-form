import json
import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import nltk

# Wczytanie pliku JSON
with open("coursedata 1.json", "r", encoding="utf-8") as f:
    courses = json.load(f)

# Łączymy pola kursów w jeden ciąg tekstowy dla każdego kursu
course_texts = [
    " ".join([c["course_name"], c["course_goals"], c["course_results"], c["course_program"]])
    for c in courses
]

course_names = [c["course_name"] for c in courses]  # Zachowujemy nazwy kursów

# Tworzenie modelu TF-IDF
polish_stopwords = ["i", "w", "na", "do", "że", "ten", "jak", "ale", "jest", "czy", "oraz", "być", "są","pod"]

# Wektoryzacja wszystkich kursów (jeden model TF-IDF dla wszystkich pól)
vectorizer = TfidfVectorizer(stop_words=polish_stopwords)
course_vectors = vectorizer.fit_transform(course_texts)

def recommend_course(search_topic, search_skills, search_level, weights=(0.6, 0.3, 0.1)):
    # Łączymy różne części zapytania w jeden wektor
    query_texts = [
        search_topic,
        search_skills,
        search_level
    ]

    # Wektoryzacja każdej części zapytania osobno
    query_vectors = [vectorizer.transform([text]) for text in query_texts]

    # Obliczamy podobieństwo dla każdej części
    similarities = [cosine_similarity(qv, course_vectors).flatten() for qv in query_vectors]

    # Łączymy wyniki zgodnie z wagami
    total_similarity = (
        weights[0] * similarities[0] +  # Temat ma największą wagę
        weights[1] * similarities[1] +  # Umiejętności są mniej istotne
        weights[2] * similarities[2]    # Poziom ma najmniejszą wagę
    )

    # Wybór najlepszego kursu
    best_match_idx = np.argmax(total_similarity)
    return course_names[best_match_idx]
