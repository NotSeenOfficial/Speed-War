# WAR SPEED

Warspeed est une application qui a pour première mission de jouer à [car wars](#car-wars) sans se prendre la tête avec toute la partie "WARGAME".

La toute première application sera une application sur ordinateur.

La seconde sera sur mobile (android, IOS).

## Index

- [main.py](/WHY%20YOU%20CLICK%20HERE%20!!!/WarSpeend/main.py) : lance l'application
- [ui/](/WHY%20YOU%20CLICK%20HERE%20!!!/WarSpeend/ui/README.md) : lance les écrans (home.py, play.py, setting.py,...)
- [assets/](/WHY%20YOU%20CLICK%20HERE%20!!!/WarSpeend/assets/README.md) : images (fond, logo, fiches véhicules, ...)
- [data/](/WHY%20YOU%20CLICK%20HERE%20!!!/WarSpeend/data/README.md) : fichiers JSON (véhicules prédéfinis et custom)
- [logic/](/WHY%20YOU%20CLICK%20HERE%20!!!/WarSpeend/logic/README.md) : logique métier (chargement, sauvegarde, choix des véhicules, etc.)

## Prérequis

- langage : [Python](#python)
- [car wars](#car-wars) : les règles de jeux, les fiches, ...

## PYTHON

Le langage python est pratique, pas très dure à comprendre. Il a beaucoup de dépendences pour créer une application.

Les dépendances :
-  [Tkinter](#tkinter)
- [CustomTkinter](#customtkinter)
- [PySide6](#pyside6)
- [Pillow](#pillow)
- [Pygame](#pygame)
- [Kivy](#kivy)
- [Flutter](#Flutter)
- [React Native](#react-native)


## Lecture des véhicules

- Tous stocké dans 2 fichiers JSON ([data/](/WHY%20YOU%20CLICK%20HERE%20!!!/WarSpeend/data/README.md))
- Charger lors du choix des différentes enregistrements
- Affichier en Scroll horizontal

## Design UI & Apdatabilité

- Utilise un **layout adaptatif (grid + poids)** pour que ça suive la taille de la fenêtre.
- Utilise des Canvas pour le fond d'écran image.
- Rend les boutons stylés avec des survols (possible avec [CustomTkinter](#customtkinter))



## Tkinter

Tkinter est un module qui permet de créer des fenêtres, à partir de là on créer déjà nôtre application.

## CustomTkinter

C'est un Tkinter plus récent, qui donne un rendu visuel plus intéressant et plus personnalisable.

## PySide6

C'est un QT pour pur python, il donne un rendu bien plus professionnel et plus propre.

## Pillow

Pour afficher des images.

## Pygame

Pour rajouter de la musique dans le fond.

## Kivy

Pour pouvoir lancer python sur mobile.

## Flutter

Module pour l'application mobile

## React Native

Module pour l'application mobile

## WARGAME

exemple :
- Warhammer (40k, age of sigmar, classique fantasy)
- Car wars

## Car Wars