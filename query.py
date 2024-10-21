import requests
import json

# Инициализация PyGithub с вашим токеном доступа
token = ""
# Замените на имя владельца и репозитория
owner = 'envoyproxy'
repo = 'envoy'

# URL для получения списка Repository Security Advisories
url = f'https://api.github.com/repos/{owner}/{repo}/security-advisories'

# Заголовки для API-запроса
headers = {
    'Accept': 'application/vnd.github+json',
    'Authorization': f'Bearer {token}',
    'X-GitHub-Api-Version': '2022-11-28'
}

# Выполняем запрос к API
response = requests.get(url, headers=headers)

# Проверяем статус ответа
if response.status_code == 200:
    # Если запрос успешен, парсим ответ как JSON
    data = response.json()

    # Выводим данные на экран
    # print(json.dumps(data, indent=4))

    # Сохраняем данные в файл для дальнейшего анализа
    with open('repository_advisories.json', 'w') as f:
        json.dump(data, f, indent=4)
else:
    # Выводим сообщение об ошибке
    print(f"Ошибка: {response.status_code}, {response.text}")