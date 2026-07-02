# League of Legends Champions Scraper

## 📖 Présentation

Ce projet est un scraper Python qui récupère automatiquement les informations des champions de **League of Legends** depuis le site officiel de Riot Games.

Le script génère ensuite une page HTML contenant une carte pour chaque champion avec :

* Son nom.
* Son image splash officielle.
* Sa description officielle.

L'objectif est de produire un site statique facilement personnalisable.

---

## 📂 Structure du projet

```text
.
├── main.py
├── styles_css.py
├── requirements.txt
├── LICENSE
├── README.md
└── front-end/              (généré automatiquement, non présent sur le dépôt GitHub)
    ├── champions.html
    └── styles.css
```

---

## ⚠️ Important

Les informations affichées sont récupérées depuis le site officiel de Riot Games.

Le fonctionnement du scraper dépend de la structure actuelle du site. Si Riot Games modifie son HTML ou ses données internes, certaines parties du script pourront nécessiter une mise à jour.

Le dossier **`front-end`** ainsi que les fichiers qu'il contient **ne sont volontairement pas présents sur le dépôt GitHub**.

Ils sont générés automatiquement à chaque exécution du script et sont ignorés par Git via le fichier `.gitignore`.

Après avoir exécuté le programme, tu retrouveras automatiquement :

* `front-end/champions.html`
* `front-end/styles.css`

---

## 🚀 Installation

Clone le dépôt :

```bash
git clone [text](https://github.com/SanguinatorX/scraping-lol.git)
cd scraping-lol
```

Installe ensuite les dépendances :

```bash
pip install -r requirements.txt
```

---

## ▶️ Utilisation

Exécute simplement :

```bash
python main.py
```

Le script :

1. Télécharge la liste des champions.
2. Visite la page officielle de chaque champion.
3. Récupère sa description.
4. Génère le contenu HTML.
5. Génère le fichier CSS.
6. Crée automatiquement le dossier `front-end` s'il n'existe pas.
7. Enregistre `champions.html` et `styles.css` dans ce dossier.

---

## 📦 Dépendances

Le projet utilise les bibliothèques suivantes :

* requests
* beautifulsoup4

Installation manuelle :

```bash
pip install requests beautifulsoup4
```

Ou avec le fichier `requirements.txt` :

```bash
pip install -r requirements.txt
```

---

## 📄 Résultat

Une fois le script terminé, ouvre simplement :

```text
front-end/champions.html
```

dans ton navigateur.

---

## 🎨 Personnalisation

Le style CSS est défini dans le fichier :

```text
styles_css.py
```

Ce fichier génère automatiquement :

```text
front-end/styles.css
```

Tu peux modifier le style dans `styles_css.py`, puis relancer le script pour régénérer les fichiers.

---

# 📜 Licence

Le code source de ce projet est distribué sous la **Mozilla Public License 2.0 (MPL-2.0)**. Les conditions complètes de cette licence sont disponibles dans le fichier `LICENSE` présent à la racine du dépôt GitHub.

Les données, images, descriptions, noms de champions, logos et autres ressources relatives à **League of Legends** sont la propriété de **Riot Games** et sont utilisées dans ce projet uniquement à des fins d'apprentissage, de démonstration et de développement.

Ce projet est indépendant et n'est ni affilié, ni soutenu, ni approuvé par Riot Games.

Toute réutilisation ou modification du code source doit respecter les conditions de la licence **MPL-2.0**. Les ressources appartenant à Riot Games restent soumises à leurs propres droits de propriété intellectuelle et à leurs conditions d'utilisation.
