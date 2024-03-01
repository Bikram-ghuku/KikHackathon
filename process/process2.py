import os
for file in os.listdir('./fieldstxt'):
    y = file.replace('.txt', '.json')
    os.rename(f'./fieldstxt/{file}', f'./fieldstxt/{y}')
    print(f"Complete: {y}")