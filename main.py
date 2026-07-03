import requests
import shutil
from bs4 import BeautifulSoup
from pathlib import Path
from concurrent.futures import ThreadPoolExecutor

BASE_URL = "https://www.leagueoflegends.com"
DD_BASE = "https://ddragon.leagueoflegends.com"

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
    <img src="lol-logo.png" alt="LoL logo">

    <div class="header-text">
        <h1>Champions League of Legends</h1>
        <p>Ici vous trouverez tous les personnages (champions) du jeu League of Legends</p>
    </div>

    <img src="lol-logo.png" alt="LoL logo">
</header>
<div id="search">
    <label for="searcher">Saississez le nom du champion :</label>
    <br />
    <input id="searcher" placeholder="Nom du champion" type="text" />
</div>
<main>
"""

# 🔥 DATA DRAGON (source stable, pas Riot HTML fragile)
DD_VERSION = "14.1.1"  # tu peux update si besoin
champion_json = session.get(
    f"https://ddragon.leagueoflegends.com/cdn/{DD_VERSION}/data/fr_FR/champion.json"
).json()["data"]


def fetch_champion(lien):
    nom = lien.get("aria-label")
    href = lien.get("href")

    if not nom or not href:
        return None

    # nom normalisé
    key = None
    for k, v in champion_json.items():
        if v["name"].lower() == nom.lower():
            key = k
            break

    if not key:
        return None

    champ_data = champion_json[key]

    img_url = f"{DD_BASE}/cdn/img/champion/splash/{key}_0.jpg"

    description = champ_data.get("blurb", "Description introuvable.")
    roles = champ_data.get("tags", [])

    nom_secu = nom.replace("'", "&#39;")
    description_secu = description.replace("'", "&#39;")
    roles_str = ", ".join(roles) if roles else "unknown"

    print(f"[OK] {nom}")

    return nom_secu, img_url, description_secu, roles_str


# 🌐 LISTE CHAMPIONS (juste pour les noms + liens)
reponse = session.get(f"{BASE_URL}/fr-fr/champions/")
reponse.encoding = "utf-8"

if reponse.status_code == 200:
    soup = BeautifulSoup(reponse.text, "html.parser")

    liens_champions = [
        a for a in soup.find_all("a")
        if a.get("aria-label") and a.get("href") and "/champions/" in a.get("href")
    ]

    with ThreadPoolExecutor(max_workers=10) as executor:
        results = executor.map(fetch_champion, liens_champions)

        for result in results:
            if not result:
                continue

            nom_secu, img_url, description_secu, roles_str = result

            html_output += f"""
<div class='champion-item'
     data-name='{nom_secu}'
     data-img='{img_url}'
     data-desc='{description_secu}'
     data-roles='{roles_str}'>

  <hover-tilt shadow shadow-blur='40' scale-factor='1.15' glare-intensity='1.2'>
    <img src='{img_url}' alt='{nom_secu}' class='champion-img'>
  </hover-tilt>

  <h2 class='champion-name'>{nom_secu}</h2>
  <span class='role-badge'>{roles_str}</span>
</div>
"""

# 🪟 MODAL
html_output += """
<div id="champion-modal" class="modal">
    <div class="modal-content">
        <span id="close-modal" class="close-btn">&times;</span>

        <div class="modal-header">
            <h2 id="modal-name">Nom</h2>
        </div>
        <div class="modal-body">
            <div id="modal-desc" class="modal-left"></div>
            <div class="modal-right">
                <img id="modal-img" src="" alt="">
            </div>
        </div>
    </div>
</div>

</main>
</body>
</html>
"""

# 💾 EXPORT
front_end = Path("front-end")
front_end.mkdir(exist_ok=True)

(front_end / "champions.html").write_text(html_output, encoding="utf-8")
shutil.copy2("script.js", front_end / "script.js")
shutil.copy2("styles.css", front_end / "styles.css")
shutil.copy2("lol-logo.png", front_end / "lol-logo.png")