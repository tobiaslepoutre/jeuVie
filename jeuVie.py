# Tobias Lepoutre (20177637)
# Largo Mas (20175474)
# 31 mars 2021

#Q1: Crée un modèle de la grille de jeux
#Q2: Prend l'enregistrement tailleGrille en paramètre
#Q3: Retourne un tableau à 1 dimension
#Q4: Nom: creerGrille
#Q5: Exemple: creerGrille(tailleGrille)= [0,0,0,0,0,0,0,0,0]
def creerGrille(tailleGrille):
    
    taille=tailleGrille.nx*tailleGrille.ny
    grille=[0]*taille
    return grille

#Q1: Crée l'état initial du modèle de grille
#Q2: Prend le modèle grille en paramètre
#Q3: Retourne un modèle contenant un nombre aléatoire de cellules vivantes,
#    noté 1, compris entre 10% et 50% et placées aléatoirement.
#Q4: Nom: init
#Q5: Exemple: init(grille)= [0,0,1,1,0,1,0,1,0]
def init(grille):
    
    tailleGrille=len(grille)
    foncRandom1=random()*0.4+0.1                 # pourcentage entre 10 et 50
    cellVivantes=round(foncRandom1*tailleGrille) # nombre de cellules vivantes
    for _ in range(cellVivantes):
        foncRandom2=math.floor(random()*(tailleGrille)) # position aléatoire
        while grille[foncRandom2]==1:                   # change si déja prise
            foncRandom2=math.floor(random()*(tailleGrille))
        grille[foncRandom2]=1                           # place la cellule
    return grille

#Q1: Fonction auxiliaire qui colorie les cellules lors de l'affichage
#Q2: Prend le modèle grille, l'enregistrement tailleGrille et la variable
#    ligne en paramètre
#Q3: Colorie les cellules tout en laissant apparaître leurs contours
#Q4: Nom: colorier
#Q5: Exemple: colorier(tailleGrille,grille,ligne)= (voir affichage)
def colorier(tailleGrille,grille,ligne):
    
    pensize(tailleGrille.largeur-2)       # taille de cellule (sans contour)
    case=0
    for _ in range(tailleGrille.ny):      # pour chaque ligne:
        for _ in range(tailleGrille.nx):     # appliquer à chaque cellules:
            if grille[case]==1:
                pencolor(1,0,0)              # du rouge si vivante
            else:
                pencolor(1,1,1)              # du blanc sinon
            fd(1)                            # laisse le contour de la cellule
            pd()
            fd(tailleGrille.largeur-1)       # colorier
            pu()
            case+=1                          # passer à la suivante
        bk(ligne)                         # revenir au début de la ligne
        rt(90)
        fd(tailleGrille.largeur)
        lt(90)                            # positionnement pour nouvelle ligne


#Q1: Affiche l'état du jeux selon le modèle de jeux
#Q2: Prend le modèle grille et l'enregistrement tailleGrille en paramètre
#Q3: Fait l'affichage complet du jeux en utilisant turtle
#Q4: Nom: dessinerGrille
#Q5: Exemple: dessinerGrille(tailleGrille,grille)= (voir affichage)
def dessinerGrille(tailleGrille,grille):
    
    ligne=tailleGrille.largeur*tailleGrille.nx      # longueur d'une ligne
    colonne=tailleGrille.largeur*tailleGrille.ny    # longueur d'une colonne
    sleep(0.1)                                      # durée d'animation
    clear()                                         # change l'affichage
    bk(ligne/2)                                   
    pensize(colonne)                                # faire le fond noir
    fd(ligne+1)                                     # (remplace les contours)
    pu()
    goto(-ligne/2, colonne/2-tailleGrille.largeur/2)  # positionnement
    colorier(tailleGrille,grille,ligne)               # coloriage des cellules
    ht()

#Q1: Compte le nombres de cases (ou cellules) vivantes autour des cellules du
#    bord en haut de la grille (sans les coins) et applique les modifications
#Q2: Prend le modèle grille, l'ancien modèle tab et variable nx en paramètre
#Q3: Traite les cellules du bord en haut de la grille et modifie la grille
#Q4: Nom: bordHaut
#Q5: Exemple: bordHaut(nx,tab,[0,1,0,0,0,0,0,0,0])= [0,0,0,0,0,0,0,0,0]
def bordHaut(nx,tab,grille):
    
    for i in range(1, nx-1):           # pour toutes les cellules i du bord:
        case=0                         # faire le compte
        if tab[i-1]==1: case+=1
        if tab[i+1]==1: case+=1
        if tab[i+nx-1]==1: case+=1
        if tab[i+nx]==1: case+=1
        if tab[i+nx+1]==1: case+=1     
        verification(case,grille,i)    # appliquer les changements à la grille

#Q1: Compte le nombres de cases (ou cellules) vivantes autour des cellules du
#    bord gauche de la grille et applique les modifications
#Q2: Prend 4 paramètres: modèle grille, ancien modèle tab, variables nx et i
#Q3: Traite les cellules du bord gauche de la grille et modifie la grille
#Q4: Nom: bordGauche
#Q5: Exemple: bordGauche(nx,tab,i,[0,0,0,1,0,0,0,0,0])= [0,0,0,0,0,0,0,0,0]
def bordGauche(nx,tab,i,grille):
    
    case=0
    if tab[i-nx]==1: case+=1
    if tab[i-nx+1]==1: case+=1
    if tab[i+1]==1: case+=1
    if tab[i+nx]==1: case+=1
    if tab[i+nx+1]==1: case+=1     
    verification(case,grille,i)

#Q1: Compte le nombres de cases (ou cellules) vivantes autour des cellules du
#    bord droit de la grille et applique les modifications
#Q2: Prend 4 paramètres: modèle grille, ancien modèle tab, variables nx et i
#Q3: Traite les cellules du bord droit de la grille et modifie la grille
#Q4: Nom: bordDroit
#Q5: Exemple: bordDroit(nx,tab,i,[0,0,0,0,0,1,0,0,0])= [0,0,0,0,0,0,0,0,0]
def bordDroit(nx,tab,i,grille):
    
    case=0
    if tab[i-nx-1]==1: case+=1
    if tab[i-nx]==1: case+=1 
    if tab[i-1]==1: case+=1
    if tab[i+nx-1]==1: case+=1
    if tab[i+nx]==1: case+=1  
    verification(case,grille,i)

    
#Q1: Compte le nombres de cases (ou cellules) vivantes autour des cellules du
#    bord en bas de la grille (sans les coins) et applique les modifications
#Q2: Prend modèle grille, ancien modèle tab, variables nx et ny en paramètre
#Q3: Traite les cellules du bord en bas de la grille et modifie la grille
#Q4: Nom: bordBas
#Q5: Exemple: bordBas(nx,ny,tab,[0,0,0,0,0,0,0,1,0])= [0,0,0,0,0,0,0,0,0]
def bordBas(nx,ny,tab,grille):
    
    for i in range(nx*(ny-1)+1, nx*ny-1):
        case=0
        if tab[i-nx-1]==1: case+=1
        if tab[i-nx]==1: case+=1
        if tab[i-nx+1]==1: case+=1
        if tab[i-1]==1: case+=1
        if tab[i+1]==1: case+=1  
        verification(case,grille,i)

        
#Q1: Compte le nombres de cases (ou cellules) vivantes autour des cellules du
#    centre de la grille et applique les modifications
#Q2: Prend 4 paramètres: modèle grille, ancien modèle tab, variables nx et i
#Q3: Traite les cellules du centre de la grille et modifie la grille
#Q4: Nom: casNormaux
#Q5: Exemple: casNormaux(nx,tab,i,[0,0,0,0,1,0,0,0,0])= [0,0,0,0,0,0,0,0,0]
def casNormaux(nx,tab,i,grille):
    
    case=0
    if tab[i-nx-1]==1: case+=1
    if tab[i-nx]==1: case+=1
    if tab[i-nx+1]==1: case+=1
    if tab[i-1]==1: case+=1
    if tab[i+1]==1: case+=1
    if tab[i+nx-1]==1: case+=1 
    if tab[i+nx]==1: case+=1
    if tab[i+nx+1]==1: case+=1
    verification(case,grille,i)

    
#Q1: Compte le nombres de cases (ou cellules) vivantes autour des coins de
#    la grille et applique les modifications
#Q2: Prend 4 paramètres: modèle grille, ancien modèle tab, variables nx et ny
#Q3: Traite les cellules des coins de la grille et modifie la grille
#Q4: Nom: casSpeciaux
#Q5: Exemple: casSpeciaux(nx,ny,tab,[1,0,1,0,0,0,1,0,1])= [0,0,0,0,0,0,0,0,0]
def casSpeciaux(nx,ny,tab,grille):
    
    case=0
    if tab[1]==1: case+=1
    if tab[nx]==1: case+=1
    if tab[nx+1]==1: case+=1
    verification(case,grille,0)
    case=0
    if tab[nx-2]==1: case+=1
    if tab[2*nx-2]==1: case+=1
    if tab[2*nx-1]==1: case+=1
    verification(case,grille,nx-1)
    case=0
    if tab[nx*(ny-2)]==1: case+=1
    if tab[nx*(ny-2)+1]==1: case+=1
    if tab[nx*(ny-1)+1]==1: case+=1        
    verification(case,grille,nx*(ny-1))
    case=0
    if tab[nx*(ny-1)-2]==1: case+=1
    if tab[nx*(ny-1)-1]==1: case+=1
    if tab[nx*ny-2]==1: case+=1
    verification(case,grille,nx*ny-1)

#Q1: Applique les modifications au modèle grille
#Q2: Prend 3 paramètres: modèle grille, le compte des cases et la variable i 
#Q3: Modifie la grille en fonction du nombre de cellules vivantes autour de i
#Q4: Nom: verification
#Q5: Exemple: verification(case,grille,i)= (voir affichage)  
def verification(case,grille,i):
    
    if case<2: grille[i]=0
    if case==3: grille[i]=1
    if case>3: grille[i]=0

#Q1: Crée un grille, l'initialise et démare le jeux en boucle infinie
#Q2: Prend l'enregistrement tailleGrille en paramètre
#Q3: Fonction principale du jeux qui se fait aléatoirement avec tailleGrille 
#Q4: Nom: jouer
#Q5: Exemple: jouer(tailleGrille)= (voir affichage) 
def jouer(tailleGrille):
    
    grille=creerGrille(tailleGrille)
    init(grille)
    dessinerGrille(tailleGrille,grille)
    while True:
        tab=grille.copy()                     # copie temporaire de la grille
        nx=tailleGrille.nx
        ny=tailleGrille.ny
        casSpeciaux(nx,ny,tab,grille)         # traite les coins 
        bordHaut(nx,tab,grille)               # traite le bord du haut
        for i in range(nx, nx*(ny-1)):  # traitement différent du centre et
            if i%nx==0:                 # des bords latéraux pour l'éfficacité
                bordGauche(nx,tab,i,grille)   # traite le bord gauche
            elif i%nx==nx-1:
                bordDroit(nx,tab,i,grille)    # traite le bord droit
            else:
                casNormaux(nx,tab,i,grille)   # traite le centre
        bordBas(nx,ny,tab,grille)             # traite le bord du bas
        dessinerGrille(tailleGrille,grille)   # affiche les changements
        
tailleGrille=struct(nx=20,ny=20,largeur=10)    
jouer(tailleGrille)

#########################
# Tests unitaires:
def bordHautTest():
    # on va tester ces 2 structures sur tous les bords de la grille
    nx=4
    grille=[1,1,1,1,1,1,1,1,0,0,0,0,0,0,0,0]
    tab=grille.copy()
    bordHaut(nx,tab,grille)
    assert grille==[1,0,0,1,1,1,1,1,0,0,0,0,0,0,0,0]
    
    grille=[1,0,0,1,0,1,1,0,0,0,0,0,0,0,0,0]
    tab=grille.copy()
    bordHaut(nx,tab,grille)
    assert grille==[1,1,1,1,0,1,1,0,0,0,0,0,0,0,0,0] 
    
def bordGaucheTest():
    nx=4
    ny=4
    grille=[1,1,0,0,1,1,0,0,1,1,0,0,1,1,0,0]
    tab=grille.copy()
    for i in range(nx, nx*(ny-1)):
        if i%(nx)==0:
            bordGauche(nx,tab,i,grille)
    assert grille==[1,1,0,0,0,1,0,0,0,1,0,0,1,1,0,0]
    
    grille=[1,0,0,0,0,1,0,0,0,1,0,0,1,0,0,0]
    tab=grille.copy()
    for i in range(nx, nx*(ny-1)):
        if i%(nx)==0:
            bordGauche(nx,tab,i,grille)
    assert grille==[1,0,0,0,1,1,0,0,1,1,0,0,1,0,0,0]

def bordDroitTest():
    nx=4
    ny=4
    grille=[0,0,1,1,0,0,1,1,0,0,1,1,0,0,1,1]
    tab=grille.copy()
    for i in range(nx, nx*(ny-1)):
        if i%nx==nx-1:
            bordDroit(nx,tab,i,grille)
    assert grille==[0,0,1,1,0,0,1,0,0,0,1,0,0,0,1,1]
    
    grille=[0,0,0,1,0,0,1,0,0,0,1,0,0,0,0,1]
    tab=grille.copy()
    for i in range(nx, nx*(ny-1)):
        if i%nx==nx-1:
            bordDroit(nx,tab,i,grille)
    assert grille==[0,0,0,1,0,0,1,1,0,0,1,1,0,0,0,1]
        
def bordBasTest():
    nx=4
    ny=4
    grille=[0,0,0,0,0,0,0,0,1,1,1,1,1,1,1,1]
    tab=grille.copy()
    bordBas(nx,ny,tab,grille)
    assert grille==[0,0,0,0,0,0,0,0,1,1,1,1,1,0,0,1]
    
    grille=[0,0,0,0,0,0,0,0,0,1,1,0,1,0,0,1]
    tab=grille.copy()
    bordBas(nx,ny,tab,grille)
    assert grille==[0,0,0,0,0,0,0,0,0,1,1,0,1,1,1,1] 
    
def casNormauxTest(): 
    nx=5
    ny=5
    # structure qui ne change pas
    grille=[0,0,0,0,0,0,0,1,0,0,0,1,0,1,0,0,0,1,0,0,0,0,0,0,0]
    tab=grille.copy()
    for i in range(nx, nx*(ny-1)):
        if i%nx!=0 and i%nx!=nx-1:
            casNormaux(nx,tab,i,grille)
    assert grille==[0,0,0,0,0,0,0,1,0,0,0,1,0,1,0,0,0,1,0,0,0,0,0,0,0]
    # structure qui ne change pas
    grille=[0,0,0,0,0,0,1,1,0,0,0,1,1,0,0,0,0,0,0,0,0,0,0,0,0]
    tab=grille.copy()
    for i in range(nx, nx*(ny-1)):
        if i%nx!=0 and i%nx!=nx-1:
            casNormaux(nx,tab,i,grille)
    assert grille==[0,0,0,0,0,0,1,1,0,0,0,1,1,0,0,0,0,0,0,0,0,0,0,0,0]
    # structure qui oscille
    grille=[0,0,0,0,0,0,0,1,0,0,0,0,1,0,0,0,0,1,0,0,0,0,0,0,0]
    tab=grille.copy()
    for i in range(nx, nx*(ny-1)):
        if i%nx!=0 and i%nx!=nx-1:
            casNormaux(nx,tab,i,grille)
    assert grille==[0,0,0,0,0,0,0,0,0,0,0,1,1,1,0,0,0,0,0,0,0,0,0,0,0]
    
def casSpeciauxTest():
    # on change les dimensions de la grille tout en vérfiant les coins
    nx=3
    ny=4
    grille=[0,1,0,1,1,0,0,0,0,0,0,0]
    tab=grille.copy()
    casSpeciaux(nx,ny,tab,grille)
    assert grille==[1,1,0,1,1,0,0,0,0,0,0,0]
    
    nx=4
    ny=3
    grille=[1,0,0,1,0,0,0,0,1,0,0,1]
    tab=grille.copy()
    casSpeciaux(nx,ny,tab,grille)
    assert grille==[0,0,0,0,0,0,0,0,0,0,0,0]
    
    nx=2
    ny=2
    grille=[1,1,1,1]
    tab=grille.copy()
    casSpeciaux(nx,ny,tab,grille)
    assert grille==[1,1,1,1]


# (la fonction 'verification' est comprise dans les fonctions testées et ne 
#  nécessite donc pas de test)

#bordHautTest()    
#bordGaucheTest()
#bordDroitTest()
#bordBasTest()
#casNormauxTest()
#casSpeciauxTest()
