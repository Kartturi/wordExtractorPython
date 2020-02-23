import urllib3
from bs4 import BeautifulSoup

def get_word_info(word):
    word_data = {
        "translation": set(),
        "words": []
    }
    dest_url = "https://www.verbformen.com/conjugation/?w={}".format(word)
    http = urllib3.PoolManager()
    r = http.request("GET", dest_url)
    soup = BeautifulSoup(r.data, 'html.parser')
    translations = soup.find("div", {"lang": "en"}).find_all("span", {"class": ""})
    for translation in translations:
        word_data.get("translation").add(translation.get_text().strip())
    table = soup.select_one(".vTbl table")

    for elem in table.find_all("td"):
        word = elem.get_text().strip()
        if word not in ["ich", "du", "er", "wir", "ihr", "sie"]:
            word_data["words"].append(word)
    print(word_data)
    return word_data


if __name__ == "__main__":
    # execute only if run as a script
    get_word_info("brauchen")