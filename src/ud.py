import requests
from bs4 import BeautifulSoup

url = "https://www.yell.com/ucs/UcsSearchAction.do?"

params = {
    'scrambleSeed': '2019865125',
    'keywords': 'hotels',
    'location': 'uk',
}

headers = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.0.0 Safari/537.36'
}
result = []

res = requests.get(url, params=params, headers=headers)

with open('response.html', 'w', encoding='utf-8') as f:
    f.write(res.text)


soup = BeautifulSoup(res.text,'html.parser')

#scraping process
headers_contents = soup.find_all('div', 'row businessCapsule--mainRow')

for content in headers_contents:
    title = content.find('h2', 'businessCapsule--name text-h2').text
    classification = content.find('span', 'businessCapsule--classification').text
    link_web = content.find('div', 'businessCapsule--ctas').find('a')['href']

    #sorting data
    data_dict = {
        'title' : title,
        'classification' : classification,
        'link web' : link_web,
    }
    print(data_dict)
    result.append(data_dict)
print('jumlah datanya adalah ', len(result))
print("Status code:", res.status_code)

