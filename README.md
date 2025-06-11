# Mini-Projet-B---Groupe-7-MGA802
Ce dépôt contient le code du mini-projet B pour l'équipe B. Ce projet à pour but de manipuler la librairie numpy de python et d'analyser la performance des différentes méthodes d'intégration (rectangle, trapèze, simpson). Un rapport sera rendu séparement, il présentera la convergence des intégrales, l’évaluation des intégrales sur un intervalle(erreur relative), et leurs éfficacité en temps de calcul.

# Objectifs du code
 L’objectif de l’exercice est de démontrer la performance de la bibliothèque NumPy pour le
 calcul numérique. On va calculer l’aire sous la courbe I d’une fonction polynomiale du 3e ordre
 f à l’aide de plusieurs méthodes implémentées en python seulement et avec NumPy. Nous utiliserons et comparerons : 
 - Methode des rectangles en python
 - Methode des rectangles en numpy
 - Methode des trapèzes en python
 - Methode des trapèzes en numpy
 - Methode de simpson en python
 - Methode de simpson en numpy

# Structure du dépôt
Le dépot est composé de deux fichiers et de quatre dossiers contenant les fonctions utiles au bon fonctionnement du code.
- Le ReadMe
- Le fichier `main.py` : fichier principale du rendu qui contient le code python
- Le dossier `fonctions` qui contient les fonctions qui permettent de générer des polynomes aléatoires et les fonctions liées aux interactions utilisateurs.
- Le dossier `intégration numérique` séparé en deux sous dossiers (numpy et python). Chacun des sous dossiers contient les fonctions de calcul des intégrals.
- Le dossier `performance` n'est pas utilisé dans le fonctionnement normal du code. Il sert seulement à évaluer les performances des fonctions. Il contient les fonctions permettant de faire l'analyse de l'écart numérique des polynomes et les temps de calcul.
- Le dossier `Ressources` contient nos courbes obtenues.



# Comment utiliser le code
Pour pouvoir utiliser le programme de César plusieurs options s'offrent à toi.
Attention dans tous les cas tu dois éxecuter le code dans le dossier dans lequel sont les fichiers.

## Clonage du dépot
1. Clique sur le bouton `Code` en haut à droite du dépot
2. Copie le lien
3. Ouvre ton IDE favori sur lequel est configuré git
4. Clone le dépot soit de manière graphique soit en utilisant :
   ```bash
   git clone <https://github.com/JordanScordinoMGA802/Mini-Projet-B---Groupe-7-MGA802.git>
   ```
5. Ouvre le fichier `main.py`.
6. Execute-le, il n'y a plus qu'à suivre les instructions dans le terminal

## Téléchargement du fichier 
1. Télécharge directement le fichier `main.py` 
2. Crée un dossier et mets les fichiers à l'intérieur
3. Ouvre le dossier dans ton IDE favori et éxecute `main.py`

## Usage des fonctions d'analyse de performance.
Si jamais vous souhaitez utiliser les fonctions d'analyse de performances:
- Pour analyser le temps d'éxecution il suffit de lancer le script `time_analysis.py`. **Attention** l'execution peut prendre du temps car il y a beaucoup d'itérations.
- Pour analyser l'erreur numérique il suffit de lancer le script  `erreur_numerique.py`


# Structure du code
Le code est decomposé en différentes fonctions mais la fonction la plus importante est : 
- `main()` se charge de demander le polynome est la méthode d'intégration que l'on souhaite utiliser. En fonction du choix de l'utilisateur nous appellons les fonctions numpy en questions (numpy car fonctions les plus efficientes)



# Références
Le site <ref1> a été utilisé pour.
Le site <ref2> a été utilisé pour.