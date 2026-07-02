css = """
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
"""