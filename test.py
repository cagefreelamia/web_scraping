import requests
from bs4 import BeautifulSoup

cookies = {
    '_ga': 'GA1.2.815985871.1667662598',
    '__lotr': 'https%3A%2F%2Fwww.google.com%2F',
    'PHPSESSID': 'astbsqvj0okpoh1fkpkcs4rsug',
    '_csrf': '4d366ad7b22105a405d2b3e6b90dc6bf497a3f6ddebfff5af2a0a2cbe4855e50a%3A2%3A%7Bi%3A0%3Bs%3A5%3A%22_csrf%22%3Bi%3A1%3Bs%3A32%3A%22Yj3HdtzyQDmFKIDCxBhW6EtroPY7p9_H%22%3B%7D',
    '_gid': 'GA1.2.496347883.1669741700',
    '_gat_UA-62444254-1': '1',
}

headers = {
    'authority': 'www.wemakescholars.com',
    'accept': '*/*',
    'accept-language': 'en-GB,en-US;q=0.9,en;q=0.8',
    # Requests sorts cookies= alphabetically
    # 'cookie': '_ga=GA1.2.815985871.1667662598; __lotr=https%3A%2F%2Fwww.google.com%2F; PHPSESSID=astbsqvj0okpoh1fkpkcs4rsug; _csrf=4d366ad7b22105a405d2b3e6b90dc6bf497a3f6ddebfff5af2a0a2cbe4855e50a%3A2%3A%7Bi%3A0%3Bs%3A5%3A%22_csrf%22%3Bi%3A1%3Bs%3A32%3A%22Yj3HdtzyQDmFKIDCxBhW6EtroPY7p9_H%22%3B%7D; _gid=GA1.2.496347883.1669741700; _gat_UA-62444254-1=1',
    'referer': 'https://www.wemakescholars.com/scholarship/search?nationality=64country=64&interest=42-43-44-45-46-47-48-1-2-3-4-5-6-7-8-9-40-41-49-35-36-54',
    'sec-ch-ua': '"Google Chrome";v="107", "Chromium";v="107", "Not=A?Brand";v="24"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36',
    'x-csrf-token': 'S9q3JHdlaVjrunayT-jmHzBB0IdXhyKl5AyN8kiS1W8SsIRsExETIbr-G_QEoaJcSAO40GHCVteLXNTFOKuKJw==',
    'x-requested-with': 'XMLHttpRequest',
}

params = {
    'nationality': '64',
    'interest': '42-43-44-45-46-47-48-1-2-3-4-5-6-7-8-9-40-41-49-35-36-54',
}

response = requests.get('https://www.wemakescholars.com/scholarship/search', params=params, cookies=cookies, headers=headers)

soup = BeautifulSoup(response.content, 'html.parser')

scholarships = soup.find("div", {"class" : "post featured_post"})

print(scholarships.prettify())