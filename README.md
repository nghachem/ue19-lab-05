# UE19 - Lab 05

Ce projet est une petite application Python qui interroge le site JokeAPI grâce au module _requests_.  
L’application envoie donc une requête HTTP de type GET à l’API, et analyse le code de la réponse:
- 200 (OK) : La requete est réussie, l'API repond avec une blague que le programme va afficher.
- 400, 404, 500,: Dans ce cas le programme affiche _Erreur_ suivi du code d'erreur.
- 
Ce programme est ensuite copié sur Docker qui vas l'executer dans un environnement isolé.
