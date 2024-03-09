# Partie I: Les opérations d'entrée/sortie sur les images 
 
import matplotlib.pyplot as plt 
import numpy as np 
 
def AfficherImg(image, title): 
    plt.axis("off") 
    #Ajouter un titre à l'image 
    plt.title(title)
 
    # Vérifier si l'image a une seule couche (format gris) ou plusieurs couches (format RGB) 
    if len(image.shape) == 2: 
        # Si l'image a une seule couche, la convertir en format RGB en ajoutant deux couches vides 
        image = np.stack((image, image, image), axis=2) 
    plt.imshow(image, interpolation="nearest") 
    # plt.imshow(img, cmap = "gray")#palette predefinie pour afficher une image 
    plt.show() 
 
def ouvrirImage(chemin): 
    image_data=plt.imread(chemin) 
    return image_data 
 
def saveImage(image_to_save): 
    plt.imsave("image1.png",image_to_save)         
 
 
#  Partie II. Les images Noir et blanc 
 
 
# Créer une image noir 
 
def image_noire(h, l): 
    return np.zeros((h, l)) 
 
# Créer une image blanche 
 
def image_blanche(h, l): 
    return np.ones((h, l)) 
 
#Créer une image noir et blanc 
 
def creerImgBlancNoir(h, l): 
    # Créer une matrice de zéros de la taille souhaitée 
    image = np.zeros((h, l)) 
    # Parcourir chaque pixel de l'image 
    for i in range(h): 
        for j in range(l): 
            # Calculer la valeur du pixel en fonction de sa position 
            pixel = (i + j) % 2 
            # Affecter la valeur du pixel à la matrice 
            img[i, j] = pixel 
    return image 
 
#Négatif: 
 
def negatif(Img): 
    hauteur, largeur = Img.shape 
    for i in range(hauteur): 
        for j in range(largeur): 
            if Img[i, j] == 0: 
                Img[i, j] = 1 
            else: 
                Img[i, j] = 0 
 
    return Img 
 
# ============================ TESTING ============================ 
 
 
img_noire = image_noire(100, 100) #Création d'une image noire de taille 100*100 
AfficherImg(img_noire, "Image noire") 
 
img_blanche = image_blanche(100, 100) #Création d'une image blanche de taille 100*100 
AfficherImg(img_blanche, "Image blanche") 
 
img_blanc_noir = creerImgBlancNoir(100, 100) #Création d'une image noir et blanc de taille 100*100 
AfficherImg(img_blanc_noir, "Image noir et blanc") 
 
img_negatif = negatif(img_noire) #Création de l'image négatif de 'img_noire' de taille 100*100 
AfficherImg(img_negatif, "Négatif de l'image noire") 
 
 
# # Partie III. Les images en niveau de gris 
 
#Luminance: 
 
def luminance(Img): 
    # Calculer la moyenne des valeurs de la matrice 
    avg_luminance = np.mean(Img) 
    return avg_luminance 
 
#Contraste: 
 
def contraste(Img): 
 
   # Calculer la moyenne des valeurs de la matrice 
    moyenne = sum(Img) / len(Img) 
    # Calculer la variance des valeurs de la matrice 
    variance = sum((x - moyenne) ** 2 for x in Img) / len(Img) 
    return variance    
 
#Profondeur: 
 
def profondeur(Img): 
    # Trouver la valeur maximale d'un pixel dans la matrice 
    profondeur_img = np.max(Img) 
    return profondeur_img 
 
#Ouvrir une image:  
 
def Ouvrir(chemin): 
    img_ouv=plt.imread(chemin) 
    return img_ouv
     
#On prend l'image 'portrait_bw.jpg' comme exemple et on affinche sa matrice 
 
img = Ouvrir("portrait_bw.jpg") 
print("La matrice de l'image est: ", img) 
     
 
 
# # Partie IV. Opérations élémentaires sur les images en mode gris 

#Inverser une image: 
 
def inverser(imge): 
    # Inverser les valeurs de la matrice en soustractant chaque pixel de la valeur maximale de l'image. 
    # Puique on travaille avec des images en niveaux de gris, la valeur maximale est 255. 
    img_invers = 255 - imge
    return img_invers 
 
#Symétrie verticale: 
 
def flipH(image): 
    # Inverser les colonnes de la matrice en utilisant la méthode flip() de NumPy 
    img_flipeH = np.flip(image, axis=1) 
    return img_flipeH 
 
 
#Concaténation horizontale: 
 
def poserV(img1, img2):
    # Concaténer les deux matrices verticalement en utilisant la méthode vstack() de NumPy 
    img_posV = np.vstack((img1, img2)) 
    return img_posV 
 
 
#Concaténation verticale: 
 
def poserH(img1, img2): 
    # Concaténer les deux matrices horizontalement en utilisant la méthode hstack() de NumPy 
    img_posH = np.hstack((img1, img2)) 
    return img_posH 
#================================== TESTING ============================================     
 
img = Ouvrir("portrait_bw.jpg") 
AfficherImg(img, "Image Originale") #Image d'origine 
 
img_inverse = inverser(img) 
AfficherImg(img_inverse, "Image Inversée") #Image inversée 
 
img_flipH = flipH(img) #Image symétrique verticale 
AfficherImg(img_flipH, "Symétrie verticale") 
 
img_poseV = poserV(img, img_inverse) #Image concaténée verticalement 
AfficherImg(img_poseV, "Concaténation verticale") 
 
img_poseH = poserH(img, img_inverse) #Image concaténée horizontalement 
AfficherImg(img_poseH, "Concaténation horizontale" ) 
 
 
 
 
 
#  Partie VI. Les images RGB 
 
 
 
M= [[[210, 100, 255],[100, 50, 255],[90, 90, 255],[90, 90, 255],[90, 90, 255],[90, 80, 255]], 
[[190, 255,89],[ 201, 255,29],[200, 255,100],[100, 255,90],[20, 255,200], [100, 255,80]], 
[[255,0, 0],[ 255,0, 0],[255,0, 0],[255,0, 0],[255,0, 0], [255,0, 0]] ] 
 
#Valeur des expressions: 
 
print(f"La valeur de M[0][1][1] est: {M[0][1][1]}") 
print(f"La valeur de M[1][0][1] est: {M[1][0][1]}") 
print(f"La valeur de M[2][1][0] est: {M[2][1][0]}") 
 
 
# La quantité de mémoire nécessaire en octets(8 bits) pour stocker le tableau représentant une image RGB: 
# Pour stocker un tableau représentant une image en couleur au format RGB (rouge, vert, bleu), vous aurez besoin de 3 octets par pixel. Cela signifie que la quantité de mémoire nécessaire dépendra de la taille de l'image en pixels. 
# Par exemple, pour une image de 200x300 pixels, vous aurez besoin de 200x300x3 = 180 000 octets de mémoire pour stocker le tableau. Cela correspond à environ 180 ko (kilooctets). 

import random 
 
#Initialiser une image RGB: 
 
def initImageRGB(imgRGB): 
    # Obtenir la hauteur et la largeur de l'image 
    hauteur, largeur = imgRGB.shape[:2] 
    # Générer des valeurs aléatoires entre 0 et 255 (inclus) pour chaque pixel de l'image 
    imgRGB = np.empty((hauteur, largeur, 3), dtype=np.uint8) 
    for i in range(hauteur): 
        for j in range(largeur): 
            # Générer une valeur aléatoire entre 0 et 255 (inclus) pour chaque canal de couleur 
            imageRGB[i, j, 0] = random.randrange(256) 
            imageRGB[i, j, 1] = random.randrange(256) 
            imageRGB[i, j, 2] = random.randrange(256) 
    return imgRGB 
 
 
#===> Exemple dutilisation de la fonction initImageRGB() <=== 
 
# Créer un tableau vide de 200x300 pixels 
imageRGB = np.empty((200, 300, 3), dtype=np.uint8) 
# Initialiser l'image avec des valeurs aléatoires 
imageRGB = initImageRGB(imageRGB) 
print("Matrice de l'image RGB:", imageRGB) 
AfficherImg(imageRGB, "Initialisation aléatoire de l'image RGB") 
 
 
#  Symétrie: 
 
def symetrieH(imge): 
    # Inverser l'ordre des colonnes de l'image en utilisant la méthode flip() de NumPy 
    img_sym = np.flip(imge, axis=1) 
    return img_sym 
 
def symetrieV(imge): 
    # Inverser l'ordre des lignes de l'image en utilisant la méthode flip() de NumPy 
    img_sym = np.flip(imge, axis=0) 
    return img_sym     
 
 
# RGB vers niveaux de gris:     
 
def grayscale(imagRGB): 
    # Obtenir la hauteur et la largeur de l'image 
    hauteur, largeur = imagRGB.shape[:2] 
    # Créer un tableau vide de la même taille pour stocker l'image en niveaux de gris 
    image_gris = np.empty((hauteur, largeur), dtype=np.uint8) 
    for i in range(hauteur): 
        for j in range(largeur): 
            # Obtenir le pixel RGB à l'emplacement (i, j) 
            pixel = imagRGB[i, j] 
            # Chercher le maximum et le minimum des valeurs de couleur
            max_couleur = max(pixel) 
            min_couleur = min(pixel) 
            # Calculer la moyenne et arrondir la valeur au nombre entier le plus proche 
            valeur_gris = int((max_couleur + min_couleur) / 2) 
            # Affecter la valeur au pixel de l'image en niveaux de gris 
            image_gris[i, j] = valeur_gris 
    return image_gris 
 
def grayscale2(imgRGB): 
    # Convertir l'image en uint16 pour obtenir une meilleure précision 
    imgRGB = imgRGB.astype(np.uint16) 
    # Calculer la moyenne de chaque pixel sur les trois couches 
    image_gris = np.mean(imgRGB, axis=2) 
    # Convertir l'image en uint8 avant de la retourner 
    return image_gris.astype(np.uint8)     
 
#===> Exemple dutilisation de la fonction grayscale() <=== 
 
rgb = Ouvrir("portrait_rgb.jpg")     
AfficherImg(rgb, "Image RGB") 
 
gris = grayscale2(rgb) #On a utilisé grayscale2() pour avoir une meilleure performance | grayscale() est aussi valable mais plus lente !!!   
AfficherImg(gris, "Image en niveaux de gris")