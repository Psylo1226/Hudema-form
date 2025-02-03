import json

with open("model_data.json", "r", encoding="utf-8") as f:
    data = json.load(f)

unique_goals = {item["course_goals"] for item in data if "course_goals" in item}

filtered_data = [{"course_goals": goal} for goal in unique_goals]

with open("course_goals.json", "w", encoding="utf-8") as f:
    json.dump(filtered_data, f, ensure_ascii=False, indent=4)

print(f"Nowy plik JSON został zapisany jako '{f}.json'.")