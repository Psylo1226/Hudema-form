import os
import requests

file_url = 'https://www.dropbox.com/scl/fi/bok0z7jpzhaeg8kk9ul1g/lemmatized_courses.json?rlkey=asxt8vy6ngdzc2s71kwk54o0a&st=yhxi0pfv&dl=1'


def download_file(file_path):
    # Pobierz plik z Dropbox
    response = requests.get(file_url, stream=True)

    # Sprawdź, czy odpowiedź jest poprawna
    if response.status_code == 200:
        with open(file_path, 'wb') as f:
            for chunk in response.iter_content(chunk_size=8192):
                f.write(chunk)
        print(f"Plik {file_path} został pobrany.")
    else:
        print(f"Błąd podczas pobierania pliku: {response.status_code}")
