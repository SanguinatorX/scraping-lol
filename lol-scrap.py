import re
import requests
from bs4 import BeautifulSoup
from pathlib import Path

css = """
<style>
   body {
       font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
       background-color: #1a1a24;
       color: #f0e6d2;
       display: flex;
       flex-wrap: wrap; /* Permet aux cartes de passer à la ligne */
       justify-content: center; /* Centre les cartes au milieu de la page */
       gap: 25px; /* Espace entre les cartes */
       padding: 30px;
   }

   .champion-card {
       background-color: #091428; /* Bleu très sombre */
       border: 2px solid #c8aa6e; /* Bordure dorée (Gold) */
       border-radius: 10px;
       box-shadow: 0 8px 16px rgba(0, 0, 0, 0.5);
       width: 350px; /* Largeur fixe de la carte */
       padding: 20px;
       display: flex;
       flex-direction: column;
       align-items: center;
   }

   .champion-card h2 {
       color: #c8aa6e;
       margin-top: 0;
       text-transform: uppercase;
       letter-spacing: 2px;
   }

   .champion-card img {
       width: 100%; /* L'image prend 100% de la carte */
       border-radius: 5px;
       border: 1px solid #c8aa6e;
   }

   .description {
       font-size: 14px;
       line-height: 1.6;
       text-align: justify;
       margin-top: 20px;
   }
</style>
"""

html_output = f"<!DOCTYPE html>\n<html>\n<head>\n<meta charset='utf-8'>\n{css}\n</head>\n<body>\n"

reponse = requests.get("https://www.leagueoflegends.com/fr-fr/champions/")
reponse.encoding = 'utf-8'

if reponse.status_code == 200:
   liens_champions = BeautifulSoup(reponse.text, "html.parser").find_all("a", href=lambda h: h and "/champions/" in h)

   for lien in liens_champions:
       nom = lien.get("aria-label")
       href = lien.get("href")

       if nom and href:
           print(f"{nom}")

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

           html_output += "<div class='champion-card'>\n"
           html_output += f"  <h2>{nom}</h2>\n"
           html_output += f"  <img src='{img_url}' alt='{nom}'>\n"
           html_output += f"  <p class='description'>{description}</p>\n"
           html_output += "</div>\n"

html_output += "</body>\n</html>"



if Path("./champions.html").exists():
   with open("champions.html", "w", encoding="utf-8") as f:
    f.write(html_output)
else:
   with open("champions.html", "x", encoding="utf-8") as f:
    f.write(html_output)
