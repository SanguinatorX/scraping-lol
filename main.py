import re
import requests
from bs4 import BeautifulSoup
from pathlib import Path
from concurrent.futures import ThreadPoolExecutor
from styles_css import css

BASE_URL = "https://www.leagueoflegends.com"

html_output = f"<!DOCTYPE html>\n<html>\n<head>\n<meta charset='utf-8'>\n<link href='./styles.css' rel='stylesheet'></head>\n<body>\n"

session = requests.Session()

def fetch_champion(lien):
    nom = lien.get("aria-label")
    href = lien.get("href")

    if not nom or not href:
        return None

    nom_propre = nom.replace(" ", "").replace("'", "").capitalize()
    img_url = f"https://ddragon.leagueoflegends.com/cdn/img/champion/splash/{nom_propre}_0.jpg"

    description = "Description introuvable."

    try:
        r = session.get(BASE_URL + href, timeout=8)
        if r.status_code == 200:
            soup = BeautifulSoup(r.text, "html.parser")
            script_data = soup.find("script", id="__NEXT_DATA__")

            if script_data:
                match = re.search(
                    r'"description":\{"type":"html","body":"(.*?)"\}',
                    script_data.string
                )
                if match:
                    description = match.group(1).replace("\\n", "<br>").replace('\\"', '"')

    except:
        description = "Erreur chargement"

    return nom, img_url, description


# PAGE LISTE CHAMPIONS
reponse = session.get(f"{BASE_URL}/fr-fr/champions/")
reponse.encoding = "utf-8"

if reponse.status_code == 200:
    soup = BeautifulSoup(reponse.text, "html.parser")
    liens_champions = soup.find_all("a", href=lambda h: h and "/champions/" in h)

    with ThreadPoolExecutor(max_workers=10) as executor:
        results = executor.map(fetch_champion, liens_champions)

        for result in results:
            if not result:
                continue

            nom, img_url, description = result

            print(nom)

            html_output += "<div class='champion-card'>\n"
            html_output += f"  <h2>{nom}</h2>\n"
            html_output += f"  <img src='{img_url}' alt='{nom}'>\n"
            html_output += f"  <p class='description'>{description}</p>\n"
            html_output += "</div>\n"


html_output += "</body>\n</html>"


# DOSSIER OUTPUT
front_end = Path("front-end")
front_end.mkdir(exist_ok=True)

# WRITE FILES
(front_end / "champions.html").write_text(html_output, encoding="utf-8")
(front_end / "styles.css").write_text(css, encoding="utf-8")