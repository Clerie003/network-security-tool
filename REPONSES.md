# Réponses – TP 1 : Premiers pas avec Git et GitHub

**Auteur : KARANGWA
Dépôt GitHub : https://github.com/USER/network-security-tool**

## Question 1 : Quelle est la différence entre `git add` et `git commit` ?

`git add` place les modifications choisies (fichiers nouveaux ou modifiés) dans la **zone d'index (staging area)** : on prépare le contenu du prochain commit, sans rien enregistrer dans l'historique. `git commit` prend ce qui est dans l'index et l'enregistre **définitivement dans l'historique** du dépôt local, sous forme d'un commit avec un message, un auteur et une date. Autrement dit : `git add` sélectionne, `git commit` enregistre.

## Question 2 : Que représente un commit dans Git ?

Un commit est un **instantané (snapshot) de l'état du projet** à un instant donné. Il est identifié par un hash unique (SHA-1), contient l'auteur, la date, un message et un pointeur vers le commit parent. Les commits forment la chaîne de l'historique : ils permettent de revenir à une version antérieure, de comparer des versions et de savoir qui a modifié quoi et pourquoi.

## Question 3 : Pourquoi créer une branche plutôt que modifier directement la branche principale ?

Une branche permet de **développer une fonctionnalité de manière isolée**, sans risquer de casser la branche principale (`main`), qui doit rester stable et fonctionnelle. Elle permet de tester et de relire le code avant de l'intégrer, de travailler à plusieurs en parallèle sans conflits immédiats, et d'abandonner facilement un essai raté. L'intégration se fait ensuite de façon contrôlée par une Pull Request.

## Question 4 : Quel est le rôle d'une Pull Request dans un projet collaboratif ?

Une Pull Request (PR) est une **demande de fusion** d'une branche vers une autre (ici `feature/custom-port` vers `main`). Elle sert à présenter les changements, à les faire **relire et discuter** par l'équipe (revue de code), à lancer des vérifications automatiques (tests, analyses de sécurité en CI) et à garder une **traçabilité** des décisions. La fusion n'a lieu qu'après validation, ce qui améliore la qualité et la sécurité du code.

