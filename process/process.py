import os
import requests
import courseName, fields

x = len(fields.career_options_comp)
i = 1
for field in fields.career_options_comp:
    headers = {
        'Content-Type': 'application/json',
        'Authorization': 'Bearer ' + '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',
    }

    json_data = {
        'model': 'gpt-3.5-turbo',
        'messages': [
            {
                'role': 'user',
                'content': str(courseName.couseName),
            },
            {
                'role': 'user',
                'content': f'based on the given courses recommend the courses for {field} with 0 for not recommended and 100 for most recommended return result as json'
            }
        ],
        'temperature': 0.7,
    }

    response = requests.post('https://api.openai.com/v1/chat/completions', headers=headers, json=json_data)
    with open(f'fieldstxt/{field}.txt', 'w') as f:
        f.write(response.json()['choices'][0]['message']['content'])
    print(f"Complete {field} {i}/{x}")
    i+=1

print(response.json()['choices'][0]['message']['content'])