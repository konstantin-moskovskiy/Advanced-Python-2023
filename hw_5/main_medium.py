import asyncio
import aiohttp
import json
import os
from bs4 import BeautifulSoup


BASE_URL = 'https://www.avito.ru'
URL = f'{BASE_URL}/moskva/kvartiry'

async def download_page(session, url):
    async with session.get(url) as response:
        return await response.text()

async def scrape_page(session, url):
    page_html = await download_page(session, url)
    soup = BeautifulSoup(page_html, 'html.parser')
    apartments = []
    for ad in soup.find_all('div', {'class': lambda value: value and value.startswith("iva-item-body")}):
        title = ad.find('h3').text.strip().replace(u'\xa0', ' ')
        print(title)
        price = ad.find('span', {'class': lambda value: value and value.startswith("price-text")}).text.strip().replace(u'\xa0', ' ')
        print(price)
        url = ad.find('a',  href=True)['href']
        print(url)
        apartments.append({'title': title, 'price': price, 'url': url})
    return apartments

async def save_data(data):
    with open('apartments.json', 'w') as f:
        json.dump(data, f, ensure_ascii=False, indent=4)

async def main():
    if not os.path.exists('apartments.json'):
        await save_data([])
    while True:
        print("Scraping in progress...")
        try:
            async with aiohttp.ClientSession() as session:
                apartments = await scrape_page(session, URL)
                with open('apartments.json', 'r') as f:
                    old_apartments = json.load(f)
                new_apartments = []
                for apartment in apartments:
                    if apartment not in old_apartments and apartment not in new_apartments:
                        new_apartments.append(apartment)
                if new_apartments:
                    print(f'Found {len(new_apartments)} new apartments!')
                    old_apartments.extend(new_apartments)
                    await save_data(old_apartments)
                else:
                    print('No new apartments found.')
        except Exception as e:
            print(f"Error: {e}")
        print("Scraping completed.")
        await asyncio.sleep(60)

if __name__ == '__main__':
    asyncio.run(main())