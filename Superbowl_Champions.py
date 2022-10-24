import requests
from bs4 import BeautifulSoup


def download(url):
    """
    Reads data from a URL and returns the data as a string
    :param url:
    :return:
    """
    # read the URL
    # pip install requests

    # return the data
    return requests.get(url).text


if __name__ == "__main__":
    """Main entry point"""
    wiki_url = 'https://en.wikipedia.org/wiki/List_of_Super_Bowl_champions'
    url_text = download(wiki_url)
    soup = BeautifulSoup(url_text, features='lxml')
    result_table = soup.find_all('table', class_="wikitable sortable")
    rows = result_table[0].find_all('tr')
    headers = rows[0].find_all("th")
    print(
        f"{headers[0].text.strip():<15} - {headers[1].text.strip():<30}"
        f"{headers[2].text.strip():<30} - {headers[3].text.strip():<30}"
        f"{headers[4].text.strip():<15} - {headers[5].text.strip():<30}"
        f"{headers[6].text.strip():<30} - {headers[7].text.strip():<30} - {headers[8].text.strip():<15}"
    )
    for row in rows:
        cells = row.find_all("td")
        if not cells:
            continue
        print(
            f"{cells[0].text.strip():<15} - {cells[1].text.strip():<40}"
            f"{cells[2].text.strip():<30} - {cells[3].text.strip():<15}"
            f"{cells[4].text.strip():<30} - {cells[5].text.strip():<40}"
            f"{cells[6].text.strip():<30} - {cells[7].text.strip():<15} - {cells[8].text.strip():<30}"
        )
