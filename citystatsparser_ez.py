import locale
from bs4 import BeautifulSoup
import requests


locale.setlocale(locale.LC_ALL, 'uk_UA.UTF-8')

url = "https://bankchart.com.ua/finansoviy_gid/groshi_rodini/novini/mista_ukrayini_za_chiselnistyu_naselennya"
response = requests.get(url)
if response.status_code == 200:
    soup = BeautifulSoup(response.text, features="html.parser")
    table = soup.find("table", {"width": "408"})
    text = table.get_text()
    table_text = text
locale.setlocale(locale.LC_ALL, 'uk_UA.UTF-8')
numbers = []
for tr in table.find_all('tr')[1:]:
    td_list = tr.find_all('td')
    population = td_list[1].text.replace('\xa0', '').replace(' ', '').replace('\u202f', '')
    numbers.append(locale.atoi(population))

max_number = max(numbers)
min_number = min(numbers)
sum_numbers = 0
count_numbers = 0

for num in numbers:
    if num > 0:
        sum_numbers += num
    elif num < 0:
        count_numbers += 1
print(table_text)
print(f"Найбільше жителів в місті Києві: {max_number}")
print(f"Найменше жителів в місті Красноград: {min_number}")
print(f"Всього жителів в усих містах: {sum_numbers}")





