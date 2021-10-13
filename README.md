#6GEI311_Lab2

##Description
Cours: 6GEI311 - Architecture des Logiciels
Laboratoire 2: Cr�ation d'un module python en C/C++
Auteurs: Rapha�lle Martin (MARR24569507) et David-Emmanuel Perron-Chouinard (PERD17119702)

##Instructions d'utilisation:

Avant d'ex�cuter le programme:
-Aller dans le fichier lab2.py � la ligne #23
-Modifier la ligne afin qu'elle contienne l'emplacement du ficher "Exemple.vi",voir exemple ci-dessous:
    Lab2.Start("", "PATH_TO_FILE/Example.avi")

-Toujours dans le fichier lab2.py, aller � la ligne #5
-Modifier la ligne afin qu'elle contienne l'emplacement du dossier "Release", voir exemple ci-dessous:
    sys.path.append("PATH_TO_FOLDER/6GEI311_lab2/x64/Release")


##Instructions de compilation (facultatif):
Le programme est compil� directement dans Visual Studio. 
Il ne devrait pas �tre n�cessaire de recompiler la librairie C++ dans Visual Studio. 

Les instructions de configuration sont tout de m�me fournis ci-dessous en cas de besoin:
    -Veuillez vous assurer d'�tre en mode "Release"
    -Clique droit sur "6GEI311_lab2" et aller dans properties
    -General -> configuration type = dynamic librairy (.dll)
    -General -> Target Name = Lab2
    -Advanced -> target file extension = .pyd
    -VC++ directories -> include directories: ajouter le path vers le dossier "include" de Python
    -VC++ directories -> librairy directories: ajouter le path vers le dossier "libs" de Python

## D�pendances:
L'utilisateur doit avoir "DirectShow" et "Python 3" install� sur son ordinateur.


## Guide d'utilisation
Le programme doit �tre ex�cut� avec python, en ouvrant un indice de commande et en entrant la commande suivante:
	python PATH_TO_FILE
Cette commande peut varier selon votre installation de Python
Lors de l'ex�cution du programme les commandes: P, A, R et Q peuvent �tre entr�es dans la console ex�cutant le programme.

Appuyer sur la touche P pause la vid�o si elle jouait et la fait jouer si elle �tait paus�e
Appuyer sur la touche A met la vitesse de la vid�o � 2x le rythme normal si elle �tait au rythme normal. Si la vid�o �tait d�j� acc�l�r�e, cette touche remet sa vitesse � la normale
Appuyer sur la touche R recommence la vid�o au d�but
Appuyer sur la touche Q ferme le programme