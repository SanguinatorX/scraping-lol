import re
import requests
from bs4 import BeautifulSoup


html_output = """<!DOCTYPE html>
<html>
<head>
    <meta charset='utf-8'>
    <title>LoL Grid Ultra Scale</title>
    <link rel='stylesheet' href='style.css'>
    <script type="module" src="https://cdn.jsdelivr.net/npm/hover-tilt/dist/hover-tilt.js"></script>
    <script src='script.js' defer></script>
</head>
<body>
"""

reponse = requests.get("https://www.leagueoflegends.com/fr-fr/champions/")
reponse.encoding = 'utf-8'

if reponse.status_code == 200:
    liens_champions = BeautifulSoup(reponse.text, "html.parser").find_all("a", href=lambda h: h and "/champions/" in h)

    for lien in liens_champions:
        nom = lien.get("aria-label")
        href = lien.get("href")

        if nom and href:
            print(nom)

            nom_propre = nom.replace(" ", "").replace("'", "").capitalize()
            img_url = f"https://ddragon.leagueoflegends.com/cdn/img/champion/splash/{nom_propre}_0.jpg"

            champ_page = requests.get(f"https://www.leagueoflegends.com{href}")
            champ_page.encoding = 'utf-8'
            description = "Description introuvable."

            if champ_page.status_code == 200:
                champ_soup = BeautifulSoup(champ_page.text, "html.parser")
                script_data = champ_soup.find("script", id="__NEXT_DATA__")

                if script_data:
                    match = re.search(r'"description":\{"type":"html","body":"(.*?)"\}', script_data.string)
                    if match:
                        description = match.group(1).replace("\\n", "<br>").replace('\\"', '"')
                        try:
                            description = description.encode('latin-1').decode('utf-8')
                        except:
                            pass

            # --- SÉCURISATION DES APOSTROPHES (CORRECTION PROBLÈME 1) ---
            description_secu = description.replace("'", "&#39;")
            nom_secu = nom.replace("'", "&#39;")

            # Remplacement par ton scale-factor de 1.70
            html_output += f"<div class='champion-item' data-name='{nom_secu}' data-img='{img_url}' data-desc='{description_secu}'>\n"
            html_output += f"  <hover-tilt shadow shadow-blur='60' scale-factor='1.70' glare-intensity='2.5'>\n"
            html_output += f"    <img src='{img_url}' alt='{nom_secu}' class='champion-img'>\n"
            html_output += f"  </hover-tilt>\n"
            html_output += f"  <h2 class='champion-name'>{nom_secu}</h2>\n"
            html_output += f"</div>\n"

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
</body>
</html>
"""

with open("index.html", "w", encoding="utf-8") as f:
    f.write(html_output)