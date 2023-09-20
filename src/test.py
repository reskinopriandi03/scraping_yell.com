import requests

response = requests.get('https://www.yell.com')

# Menyimpan respon ke file HTML
with open('response.html', 'w', encoding='utf-8') as f:
    f.write(response.text)

print("Respon telah disimpan ke response.html")
