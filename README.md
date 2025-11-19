1. Quelle est la difference entre une requete GET et une requete POST dans le context
d’un formulaire ?
une requette GET envoie les donnees dans l'URL
et pour la requette POST elle envoie les donnees dans le corps de la requete.Sert a envoyer, ajouter ou modifier des infos

2. À quoi sert redirect(url_for(...)) dans une application Flask ?
sert a rediriger l’utilisateur vers une autre page apres une action

3. Expliquez le rôle des blocs et de l’héritage de templates dans Jinja.
On met le code commun du site dans un fichier "base.html"
Les autres pages utilisent ce fichier en utilisont {% extends "base.html" %}et remplissent seulement les zones qui changent grâce aux blocs{% block content %}
alors ca sert a eviter la repitition du meme HTML et rend le site plus organisé

4. Donnez un exemple de situation où JavaScript côté client est plus adapté que le
traitement côté serveur en Python.
quand on veut une action instantanée dans la page sans recharger
Exemple :filtrer les taches pendant qu’on tape dans une barre de recherche
JavaScript reagit directement dans le navigateur alors que Python necessiterait de recharger la page