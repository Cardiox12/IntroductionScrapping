# Introduction au scraping

Ce projet est une introduction au concept de scraping et fait suite au live coding sur le serveur [Docstring](https://discord.gg/27mTMyWH), vous y trouverez deux types de scrapers. \
Un scraper pour les sites statiques et un scraper pour les sites dynamiques.

La première étape du projet étant d'introduire les concepts fondamenteux du scraping, qui se déroule en règle général en 6 étapes :

1. Vérifier que le site autoriste le scraping
2. Récupérer le contenu de la page web
3. Etudier la sémantique de la page web
4. Cibler les tags HTML
5. Récupérer le contenu des tags HTML ciblés
6. Exporter les données sous un autre format : CSV, JSON, Base de données.


#### Statique
Pour scraper des sites statiques, en général les modules `requests` et `BeautifulSoup` sont suffisants.
