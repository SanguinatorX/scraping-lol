import re
import requests
import shutil
from bs4 import BeautifulSoup
from pathlib import Path
from concurrent.futures import ThreadPoolExecutor

from styles_css import css

BASE_URL = "https://www.leagueoflegends.com"
session = requests.Session()

html_output = """<!DOCTYPE html>
<html>
<head>
    <meta charset='utf-8'>
    <title>League of Legends champions</title>
    <link rel='stylesheet' href='styles.css'>
    <script type="module" src="https://cdn.jsdelivr.net/npm/hover-tilt/dist/hover-tilt.js"></script>
    <script src='script.js' defer></script>
</head>
<body>
    <header>
        <h1>Champions League of Legends</h1>
    </header>
    <main>
"""

# PAGE LISTE
reponse = requests.get(f"{BASE_URL}/fr-fr/champions/")
reponse.encoding = 'utf-8'

def fetch_champion(lien):
    nom = lien.get("aria-label")
    href = lien.get("href")

    if not nom or not href:
        return None

    nom_propre = nom.replace(" ", "").replace("'", "").capitalize()
    img_url = f"https://ddragon.leagueoflegends.com/cdn/img/champion/splash/{nom_propre}_0.jpg"

    description = "Description introuvable."

    champ_page = session.get(f"{BASE_URL}{href}")
    champ_page.encoding = 'utf-8'

    if champ_page.status_code == 200:
        champ_soup = BeautifulSoup(champ_page.text, "html.parser")
        script_data = champ_soup.find("script", id="__NEXT_DATA__")

        if script_data:
            match = re.search(
                r'"description":\{"type":"html","body":"(.*?)"\}',
                script_data.string
            )
            if match:
                description = match.group(1).replace("\\n", "<br>").replace('\\"', '"')

    description_secu = description.replace("'", "&#39;")
    nom_secu = nom.replace("'", "&#39;")
    print(nom_propre)

    return nom_secu, img_url, description_secu


if reponse.status_code == 200:
    liens_champions = BeautifulSoup(reponse.text, "html.parser").find_all(
        "a", href=lambda h: h and "/champions/" in h
    )

    with ThreadPoolExecutor(max_workers=10) as executor:
        results = executor.map(fetch_champion, liens_champions)

        for result in results:
            if not result:
                continue

            nom_secu, img_url, description_secu = result

            html_output += f"""
<div class='champion-item' data-name='{nom_secu}' data-img='{img_url}' data-desc='{description_secu}'>
  <hover-tilt shadow shadow-blur='40' scale-factor='1.25' glare-intensity='1.8'>
    <img src='{img_url}' alt='{nom_secu}' class='champion-img'>
  </hover-tilt>
  <h2 class='champion-name'>{nom_secu}</h2>
</div>
"""

html_output += """
<div id="champion-modal" class="modal">
    <div class="modal-content">
        <span id="close-modal" class="close-btn">&times;</span>
        <div class="modal-container">
            <div class="modal-header">
                <h2 id="modal-name">Nom</h2>
            </div>
            <div class="modal-body">
                <div id="modal-desc" class="modal-left">Description</div>
                <div class="modal-right">
                    <img id="modal-img" src="" alt="">
                </div>
            </div>
        </div>
    </div>
</div>
</main>
</body>
</html>
"""

front_end = Path("front-end")
front_end.mkdir(exist_ok=True)

(front_end / "champions.html").write_text(html_output, encoding="utf-8")
(front_end / "styles.css").write_text(css, encoding="utf-8")

shutil.copy2("script.js", front_end / "script.js")
