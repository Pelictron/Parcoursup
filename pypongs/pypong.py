# coding = utf-8
import pygame

# INITIALISATION
# =============================================================================

# Initialisation du module pygame
pygame.init()

# Définition des constantes
LARGEUR = 800  # Taille et titre de la fenêtre
HAUTEUR = 600
TITRE = "pyPong"

ECHELLE = LARGEUR // 80  # Pour adapter l'affichage à la taille de la fenêtre

TAILLE_BALLE = ECHELLE  # Taille de la balle

HAUTEUR_RAQUETTE = 5 * ECHELLE  # Taille des raquettes
LARGEUR_RAQUETTE = ECHELLE

NOIR = (0, 0, 0)  # Code RVB des couleurs
BLANC = (255, 255, 255)

TAILLE_SCORE = 10 * ECHELLE  # Taille du texte des scores

# Définition des variables

termine = False  # Utilisée pour la boucle principale
pause = True  # Utilisée pour mettre le jeu en pause
horloge = pygame.time.Clock()  # Utilisée pour gérer les FPS

x_balle = LARGEUR / 2 # Coordonnées de la balle
y_balle = HAUTEUR / 2

vitesse_balle_x = ECHELLE / 2  # Vitesses de la balle
vitesse_balle_y = 0

x_raquette_gauche = 5 * ECHELLE  # Coordonnées des raquettes
y_raquette_gauche = HAUTEUR / 2
vitesse_raquette_gauche = 0  # Vitesses des raquettes

x_raquette_droite = 75 * ECHELLE  # Coordonnées des raquettes
y_raquette_droite = HAUTEUR / 2
vitesse_raquette_droite = 0  # Vitesses des raquettes

score_gauche = 0  # Score des joueurs
score_droite = 0

police_score = pygame.font.Font("./polices/SuperMarioWorldTextBoxRegular-Y86j.ttf", TAILLE_SCORE)

bip1 = pygame.mixer.Sound('./sons/select_blip1.wav')
bip2 = pygame.mixer.Sound('./sons/select_blip2.wav')
bip3 = pygame.mixer.Sound('./sons/select_blip_error1.wav')

# Initialisation de la fenêtre d'affichage
fenetre = pygame.display.set_mode([LARGEUR, HAUTEUR])

# Visibilité du pointeur de la souris au dessus de la zone de jeu
pygame.mouse.set_visible(False)

# Titre apparaissant dans la barre de titre de la fenêtre
pygame.display.set_caption(TITRE)


# BOUCLE PRINCIPALE
# =============================================================================

while not termine:
    # Gestion des événements
    #--------------------------------------------------------------------------

    for event in pygame.event.get(): # Boucle de gestion des événements
        if event.type == pygame.KEYDOWN:  # Un joueur a appuyé sur une touche
            if event.key == pygame.K_a:
                vitesse_raquette_gauche = -ECHELLE
            elif event.key == pygame.K_w:
                vitesse_raquette_gauche = ECHELLE
            elif event.key == pygame.K_SPACE:
                pause = False
        if event.type == pygame.KEYUP:   # Un joueur a relaché une touche
            if event.key == pygame.K_a and vitesse_raquette_gauche < 0:
                vitesse_raquette_gauche = 0
            elif event.key == pygame.K_w and vitesse_raquette_gauche > 0:
                vitesse_raquette_gauche = 0
            elif event.key == pygame.K_SPACE:
                pause = False
        
        if event.type == pygame.KEYDOWN:  # Un joueur a appuyé sur une touche
            if event.key == pygame.K_PAGEUP:
                vitesse_raquette_droite = -ECHELLE
            elif event.key == pygame.K_PAGEDOWN:
                vitesse_raquette_droite = ECHELLE
            elif event.key == pygame.K_SPACE:
                pause = False
        if event.type == pygame.KEYUP:   # Un joueur a relaché une touche
            if event.key == pygame.K_PAGEUP and vitesse_raquette_droite < 0:
                vitesse_raquette_droite = 0
            elif event.key == pygame.K_PAGEDOWN and vitesse_raquette_droite > 0:
                vitesse_raquette_droite = 0
            elif event.key == pygame.K_SPACE:
                pause = False
                
        if event.type == pygame.QUIT:   # Clique sur la croix rouge
                termine = True          # fin de la boucle principale

    #--------------------------------------------------------------------------
    # Fin de la gestion des événements

    # Logique de jeu
    #--------------------------------------------------------------------------
    
    
    # Rebond de la balle sur les bords
    if y_balle > HAUTEUR - TAILLE_BALLE / 2:
        vitesse_balle_y = -vitesse_balle_y
        
    if y_balle < 0 + TAILLE_BALLE / 2:
        vitesse_balle_y = -vitesse_balle_y
        
    # Calcul de la nouvelle positions des raquettes
    y_raquette_gauche = y_raquette_gauche + vitesse_raquette_gauche
    y_raquette_droite = y_raquette_droite + vitesse_raquette_droite
    
    # Détection des colisions
    if     (x_raquette_gauche - (LARGEUR_RAQUETTE + TAILLE_BALLE) / 2 < x_balle) \
       and (x_balle < x_raquette_gauche + (LARGEUR_RAQUETTE + TAILLE_BALLE) / 2) \
       and (y_raquette_gauche - (HAUTEUR_RAQUETTE + TAILLE_BALLE) / 2 < y_balle) \
       and (y_balle < y_raquette_gauche + (HAUTEUR_RAQUETTE + TAILLE_BALLE) / 2):
        vitesse_balle_x = -1.1 * vitesse_balle_x
        vitesse_balle_y = (y_balle - y_raquette_gauche) / 5
        bip2.play()
    
    if     (x_raquette_droite - (LARGEUR_RAQUETTE + TAILLE_BALLE) / 2 < x_balle) \
       and (x_balle < x_raquette_droite + (LARGEUR_RAQUETTE + TAILLE_BALLE) / 2) \
       and (y_raquette_droite - (HAUTEUR_RAQUETTE + TAILLE_BALLE) / 2 < y_balle) \
       and (y_balle < y_raquette_droite + (HAUTEUR_RAQUETTE + TAILLE_BALLE) / 2):
        vitesse_balle_x = -1.1 * vitesse_balle_x
        vitesse_balle_y = (y_balle - y_raquette_droite) / 5
        bip1.play()
        
    # Calcule de la nouvelle position de la balle
    if not pause:
        x_balle = x_balle + vitesse_balle_x
        y_balle = y_balle + vitesse_balle_y
        
    # Un joueur marque
    if x_balle > LARGEUR:
        score_gauche = score_gauche + 1
        x_balle = LARGEUR / 2
        y_balle = HAUTEUR / 2
        vitesse_balle_x = -ECHELLE / 2
        vitesse_balle_y = vitesse_balle_y / 2
        pause = True
        bip3.play()
    
    if x_balle < 0:
        score_droite = score_droite + 1
        x_balle = LARGEUR / 2
        y_balle = HAUTEUR / 2
        vitesse_balle_x = -ECHELLE / 2
        vitesse_balle_y = vitesse_balle_y / 2
        pause = True
        bip3.play()
    
    #--------------------------------------------------------------------------
    # Fin de la Logique de jeu
    # Dessin des élèments du jeu
    #--------------------------------------------------------------------------

    # Couleur de fond
    fenetre.fill(NOIR)
    # Affichage de la balle
    left = x_balle - TAILLE_BALLE / 2
    top = y_balle - TAILLE_BALLE / 2
    width = TAILLE_BALLE
    height = TAILLE_BALLE
    pygame.draw.rect(fenetre, BLANC, [left, top, width, height])
    
    # Affichage des raquettes
    left = x_raquette_gauche - LARGEUR_RAQUETTE / 2
    top = y_raquette_gauche - HAUTEUR_RAQUETTE / 2
    width = LARGEUR_RAQUETTE
    height = HAUTEUR_RAQUETTE
    pygame.draw.rect(fenetre, BLANC, [left, top, width, height])
    
    left = x_raquette_droite  - LARGEUR_RAQUETTE / 2
    top = y_raquette_droite - HAUTEUR_RAQUETTE / 2
    width = LARGEUR_RAQUETTE
    height = HAUTEUR_RAQUETTE
    pygame.draw.rect(fenetre, BLANC, [left, top, width, height])
    
    # Affichage des scores
    texte = police_score.render(str(score_gauche), False, BLANC)
    fenetre.blit(texte, (LARGEUR / 4 - texte.get_width() / 2, HAUTEUR / 50))
    
    # Affichage des scores
    texte = police_score.render(str(score_droite), False, BLANC)
    fenetre.blit(texte, ( 800 - LARGEUR / 4  - texte.get_width() / 2, HAUTEUR / 50))
    
    # Affichage du filet
    pas = HAUTEUR // 30
    for y in range(0, HAUTEUR, pas):
        pygame.draw.line(fenetre, BLANC,
                         [LARGEUR / 2, y],
                         [LARGEUR / 2, y + pas / 2],
                         ECHELLE // 2)
    
    #--------------------------------------------------------------------------
    # Fin du dessin des élèments du jeu

    # Demande à pygame d'afficher ce qui a été déssiné
    pygame.display.flip()

    # Fréquence de la boucle principale (nombre d'images par secondes)
    horloge.tick(60)

# Une fois la boucle principale terminée, on ferme la fenêtre.
pygame.quit()