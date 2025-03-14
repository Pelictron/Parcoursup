# coding: utf-8

from PIL import Image

def decode_binaire(code):
    """code est une chaîne de caractère contenat du binaire.
    Chaque série de 8 bits correspond, au point de code d'un caractère.
    La fonction renvoie le mesasge ainsi formé.
    La fin du message est marquée par le point de code 0."""
    
    message=""
    binaire=""
    continuer = True
    nb=0
    
    while continuer :
        binaire += code[nb]
    
        if len(binaire)==8 :
            nb_decimal = int(binaire,2)
            if nb_decimal == 0 :
                    return message
            message += chr(nb_decimal)
            nb_decimal = 0
            binaire=""
            
        nb += 1

                

                
    
def recup_code_dans_image(image):
    """ La fonction parcours image pixel par pixel, pour chaque composante RVB
    - si elle est paire, ele correspond au bit 0.
    - si elle est impaire elle correspond au bit 1.
    La fonction renvoie une chaîne de caractères composée des 0 et des 1 obtenus."""
    
    colonne,ligne=image.size
    imgtransformee=Image.new(image.mode,image.size)
    bin=""
    
    for i in range(ligne):
        for j in range(colonne):
            pixel = image.getpixel((j,i)) # récupération du pixel
            r,v,b = pixel
            bin += str(r%2) + str(v%2) +str(b%2)
    return bin






    

if __name__=="__main__":

    
    
    
    ImageFile = 'pumpkin_mess1.png'
    img = Image.open(ImageFile)
    # affichage des caractéristiques de l'image
    print (img.format,img.size, img.mode)
    code = recup_code_dans_image(img)
    print (decode_binaire(code))

    
