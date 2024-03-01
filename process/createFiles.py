import courseName, fields

for field in fields.career_options:
    with open(f'fieldsJSON/{field}.json', 'w') as f:
        print(f"Create file {field}.json")