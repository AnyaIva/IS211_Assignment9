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
    cbs_url = 'https://www.cbssports.com/nfl/stats/player/passing/nfl/regular/qualifiers/'
    url_text = download(cbs_url)
    soup = BeautifulSoup(url_text, features='lxml')
    result_table = soup.find_all('table', class_="TableBase-table")
    rows = result_table[0].find_all('tr')[:21]
    headers = rows[0].find_all('th')
    print(
        f"{headers[0].text.strip():>15} - {headers[8].text.strip():>30} ")

    for row in rows:
        player_name = row.find_all('span', class_="CellPlayerName--long")
        cells = row.find_all('td', class_="TableBase-bodyTd")
        if not player_name:
            continue
        print(f"{player_name[0].text.strip():>15}")
        if not cells:
            continue
        print(f"{cells[9].text.strip():>50}")
   
