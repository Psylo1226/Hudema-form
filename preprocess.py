import json
import spacy

nlp = spacy.load("pl_core_news_sm")

def lemmatize_text(text):
    doc = nlp(text)
    return " ".join([token.lemma_ for token in doc if not token.is_stop])

# Wczytanie danych
with open("coursedata 1.json", "r", encoding="utf-8") as f:
    courses = json.load(f)

# Lematyzacja i zapis do nowego pliku
def preprocess():
    for course in courses:
        combined_text = " ".join(
            [course["course_name"], course["course_goals"], course["course_results"], course["course_program"]])
        course["lemmatized_text"] = lemmatize_text(combined_text)
        # Zapis lematyzowanych danych
        with open("lemmatized_courses.json", "w", encoding="utf-8") as f:
            json.dump(courses, f, ensure_ascii=False, indent=4)
