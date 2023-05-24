# Projet étudiant - Quiz App

Ce projet a été réalisé par Ragavi SAGEEKARAN, Audric DAVIAU et Michael TRAN dans le cadre de nos études. Il s'agit d'une application de Quiz en ligne qui permet aux utilisateurs de répondre à une liste de questions et d'obtenir un score en fonction de leurs réponses.
## Fonctionnalités
- Les utilisateurs peuvent répondre à une liste de questions.
- Les scores des utilisateurs sont enregistrés sur le site.
- Un classement des participants est affiché.

## Installation et exécution

Pour lancer le site Quiz App, suivez les étapes ci-dessous :

1. Clonez le référentiel GitHub : quiz-app
2. Assurez-vous d'avoir Docker installé sur votre machine.
3. Image Docker pour la partie back-end :
    - Utilisez la commande suivante pour télécharger l'image Docker :
    ```
        docker pull audricdaviau/quiz-prod-api
    ```
    - Exécutez l'image Docker :

    ```
        docker run -p 5000:5000 audricdaviau/quiz-prod-api
    ```

4. Image Docker pour l'interface graphique :
    - Utilisez la commande suivante pour télécharger l'image Docker :
    ```
        docker pull audricdaviau/quiz-prod-ui
    ``` 
    - Exécutez l'image Docker :
    ```
    docker run -p 8080:8080 audricdaviau/quiz-prod-ui
    ```

Accédez au site Quiz App en ouvrant votre navigateur et en visitant l'URL suivante : http://localhost:8080

## Liens des images Docker
    - Image Docker pour la partie back-end : https://hub.docker.com/r/audricdaviau/quiz-prod-api
    - Image Docker pour l'interface graphique : https://hub.docker.com/r/audricdaviau/quiz-prod-ui


Remarque : Ce projet a été réalisé à des fins d'apprentissage et de démonstration dans un contexte étudiant.