import json
import pandas as pd

input_file = 'repository_advisories.json'
output_file = 'output.xlsx'

with open(input_file, 'r', encoding='utf-8') as file:
    data = json.load(file)

extracted_data = []

# Извлечение необходимых полей
for item in data:
    advisory = {
        "ghsa_id": item.get("ghsa_id"),
        "cve_id": item.get("cve_id"),
        "score": item.get("cvss", {}).get("score"),
        "summary": item.get("summary"),
        "description": item.get("description"),
        "vulnerable_version_range": item.get("vulnerabilities")[0].get("vulnerable_version_range") if item.get("vulnerabilities") else None,
        "patched_versions": item.get("vulnerabilities")[0].get("patched_versions") if item.get("vulnerabilities") else None,
        "published_at": item.get("published_at"),
    }
    extracted_data.append(advisory)

# Создание DataFrame и запись в Excel
df = pd.DataFrame(extracted_data)
df.to_excel(output_file, index=False)

print(f"Данные успешно записаны в файл '{output_file}'")
