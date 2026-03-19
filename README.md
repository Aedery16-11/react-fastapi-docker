Pour lancer le projet :

Tout d'abord, assurez-vous d'avoir Docker et Docker Compose installés sur votre machine. Ensuite, mettez ces adresse dans votre fichier hosts pour accéder à vos services via des sous-domaines en local :

front.aaron.com

api.aaron.com

portainer.aaron.com

traefik.aaron.com

Vous pouvez utiliser n'importe quelle adresse, mais assurez-vous de les mettre à jour dans les fichiers de configuration de Traefik et Portainer.

Ensuite, lancez Traefik en premier pour configurer les sous-domaines :

```

docker compose -f traefik-docker-compose-light.yml up -d

```

Cette commande permet de lancer d'abord traefik pour définir nos sous domaines en local.

Ensuite, on peut lancer portainer pour gérer nos conteneurs docker via une interface graphique :

```

docker compose -f portainer-docker-compose.yml up -d

```

Pour accéder à portainer, rendez-vous sur http://portainer.aaron.com:9000 (ou changez l'url) et suivez les instructions pour créer un compte administrateur. Ensuite, connectez-vous à l'instance Docker locale pour gérer vos conteneurs.

Enfin, lancez votre application React et Flask :

```

docker compose -f docker-compose.yml up -d

```

Cette commande va lancer à la fois le frontend React et le backend Flask. Vous pouvez accéder à votre application via http://front.aaron.com (ou changez l'url) et l'API via http://api.aaron.com (ou changez l'url).

Assurez-vous que tous les services sont en cours d'exécution en vérifiant les logs ou en accédant à Portainer pour voir l'état de vos conteneurs.