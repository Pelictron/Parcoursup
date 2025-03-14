# coding: utf-8

from PIL import Image

def mettre_code_dans_image(image,code):
    code += (3 - len(code)%3)*"0" 
    colonne,ligne=image.size
    image_transformee = Image.new(image.mode, image.size)
    nbr = 0     
    for i in range(ligne):
        for j in range(colonne):
            pixel = image.getpixel((j,i)) # récupération du pixel
            r,v,b = pixel
            if nbr < len(code):
                    
                if str(code)[nbr]=="1" and int(r)%2==1 or str(code)[nbr]=="0" and int(r)%2==0:
                    nbr += 1
                else:
                    r += 1
                    nbr += 1 
                if str(code)[nbr]=="1" and int(v)%2==1 or str(code)[nbr]=="0" and int(v)%2==0 :
                    nbr += 1
                else :
                    v += 1
                    nbr += 1
                if str(code)[nbr]=="1" and int(b)%2==1 or str(code)[nbr]=="0" and int(b)%2==0:
                    nbr += 1
                else:
                    b += 1
                    nbr += 1
            pixel = (r,v,b)
            image_transformee.putpixel((j,i), pixel )
            
    return image_transformee


def code_binaire(message):
    
    code=""
    binaire=""
    nb=0
    
    for lettre in message:
        binaire = f"{ord(lettre):b}"
        nb = 8 - len(binaire)
        code += '0'*nb +str(binaire)
#         f"{37:08b}"
    code += "00000000"
    return code

    

if __name__=="__main__":
    ImageFile = 'pumpkin.png'
    img = Image.open(ImageFile)
    print (img.format,img.size, img.mode)
    
    mess = "to cesc lokemyez dbyz pkx no co aeo to cesc ox dbksx no pksbo"
    message = code_binaire(mess)
    
    image_mess = mettre_code_dans_image(img, message)
    image_mess.save("pumpkin_mess1.png")
    
