Signes=["x","o"]
Grille=[[" "," "," "," ","0",")"," "," ","1",")"," "," ","2",")"]
        ,[" "," ","-","-","-","-","-","-","-","-","-","-","-","-"]
        ,["0",")","|"," "," "," ","|"," "," "," ","|"," "," "," ","|"]
        ,[" "," ","-","-","-","-","-","-","-","-","-","-","-","-"]
        ,["1",")","|"," "," "," ","|"," "," "," ","|"," "," "," ","|"]
        ,[" "," ","-","-","-","-","-","-","-","-","-","-","-","-"]
        ,["2",")","|"," "," "," ","|"," "," "," ","|"," "," "," ","|"]
        ,[" "," ","-","-","-","-","-","-","-","-","-","-","-","-"]]

colonnes=len(Grille)

def affichage(colonnes):
    for i in range(colonnes):
        ligne=Grille[i]
        ligne="".join(ligne)
        print(ligne)

def tour(joueur,tours):
    if joueur==1:
        joue(0,tours,joueur)
    else:
        joue(1,tours,joueur)

def lancement():
    joueur=int(input("Donnez le numéro du joueur qui commence(1 ou 2): "))
    print("Que la partie commence!")
    tours=0
    tour(joueur,tours)

def gagnant(joueur):
    if joueur==1:
        print("C'est le joueur 2 qui remporte la partie!")
    else:
        print("C'est le joueur 1 qui remporte la partie!")

def matchnul():
    print("Aucun des deux joueurs n'a remporté la partie =(")
    

def gagner(joueur,tours):
    if (Grille[2][4]==Grille[2][8]!=" ") and (Grille[2][8]==Grille[2][12]!=" ") and (Grille[2][12]==Grille[2][4]!=" "):
        return gagnant(joueur)
    if (Grille[4][4]==Grille[4][8]!=" ") and (Grille[4][8]==Grille[4][12]!=" ") and (Grille[4][12]==Grille[4][4]!=" "):
        return gagnant(joueur)
    if (Grille[6][4]==Grille[6][8]!=" ") and (Grille[6][8]==Grille[6][12]!=" ") and (Grille[6][12]==Grille[6][4]!=" "):
        return gagnant(joueur)
    if (Grille[2][4]==Grille[4][8]!=" ") and (Grille[4][8]==Grille[6][12]!=" ") and (Grille[6][12]==Grille[2][4]!=" "):
        return gagnant(joueur)
    if (Grille[6][4]==Grille[4][8]!=" ") and (Grille[4][8]==Grille[2][12]!=" ") and (Grille[2][12]==Grille[6][4]!=" "):
        return gagnant(joueur)
    if (Grille[2][4]==Grille[4][4]!=" ") and (Grille[4][4]==Grille[6][4]!=" ") and (Grille[6][4]==Grille[2][4]!=" "):
        return gagnant(joueur)
    if (Grille[2][8]==Grille[4][8]!=" ") and (Grille[4][8]==Grille[6][8]!=" ") and (Grille[6][8]==Grille[2][8]!=" "):
        return gagnant(joueur)
    if (Grille[2][12]==Grille[4][12]!=" ") and (Grille[4][12]==Grille[6][12]!=" ") and (Grille[6][12]==Grille[2][12]!=" "):
        return gagnant(joueur)
    else:
        return tour(joueur,tours)
    

def joue(symbole,tours,joueur):
    if tours>9:
        matchnul()
    else:
        tours=tours+1
        print("C'est au tour du joueur ",joueur,"^^")
        pl1=int(input("Donnez le numéro de colonne: "))
        pl2=int(input("Donnez le numéro de ligne: "))
        if pl1==0 and pl2==0:
            Grille[2][4]=Signes[symbole]
            if symbole==0:
                joueur=2
            else:
                joueur=1
            return affichage(colonnes),gagner(joueur,tours)
        if pl1==1 and pl2==0:
            Grille[2][8]=Signes[symbole]
            if symbole==0:
                joueur=2
            else:
                joueur=1
            return affichage(colonnes),gagner(joueur,tours)
        if pl1==2 and pl2==0:
            Grille[2][12]=Signes[symbole]
            if symbole==0:
                joueur=2
            else:
                joueur=1
            return affichage(colonnes),gagner(joueur,tours)
        if pl1==0 and pl2==1:
            Grille[4][4]=Signes[symbole]
            if symbole==0:
                joueur=2
            else:
                joueur=1
            return affichage(colonnes),gagner(joueur,tours)
        if pl1==1 and pl2==1:
            Grille[4][8]=Signes[symbole]
            if symbole==0:
                joueur=2
            else:
                joueur=1
            return affichage(colonnes),gagner(joueur,tours)
        if pl1==2 and pl2==1:
            Grille[4][12]=Signes[symbole]
            if symbole==0:
                joueur=2
            else:
                joueur=1
            return affichage(colonnes),gagner(joueur,tours)
        if pl1==0 and pl2==2:
            Grille[6][4]=Signes[symbole]
            if symbole==0:
                joueur=2
            else:
                joueur=1
            return affichage(colonnes),gagner(joueur,tours)
        if pl1==1 and pl2==2:
            Grille[6][8]=Signes[symbole]
            if symbole==0:
                joueur=2
            else:
                joueur=1
            return affichage(colonnes),gagner(joueur,tours)
        if pl1==2 and pl2==2:
            Grille[6][12]=Signes[symbole]
            if symbole==0:
                joueur=2
            else:
                joueur=1
            return affichage(colonnes),gagner(joueur,tours)

lancement()
        
        
        
       





