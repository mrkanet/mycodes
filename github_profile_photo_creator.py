from PIL import Image, ImageDraw
import random


#12x12 boyutunda gibi islem yapilacak. 12*40x12*40 boyutunda
#im_frame = Image.new('RGB', (440,440), color=(240,240,240))
#iceride bloklarin yerlestirilecegi yerin çerçevesi, ilk bloklar çerçeveye
#sonra da cerceve asil görselin üstüne

#im_blok = Image.new('RGB', (80,80), color=blok_color)
#bir adet mavi blok

#blok_color = (124,203,223)






def random_blok_list(size = 5):
    r_list = []
    for i in range(size):
        r_list.append([])
        for j in range(size):
            r_list[i].append(random.randint(0,1))
    return r_list



def make_image(blok_list):
    blok_color = '#7ccbdf'
    out_color = '#7cc5df'
    #blok_list = [[1,0,1,0,1],[0,1,0,1,0],[1,1,1,1,1],[0,0,1,0,0],[0,1,1,1,0]]
    blok_size = 80
    im_size = (len(blok_list)+1)*80
    img = Image.new('RGB', (im_size,im_size), color = (240,240,240))

    image = ImageDraw.Draw(img)

    for i in range(len(blok_list)):
        for j in range(len(blok_list)):
            if blok_list[i][j] == 1:
                _is = i*80+40
                _js = j*80+40
                shape = [(_js,_is),(_js+80,_is+80)] 
                image.rectangle(shape, fill = blok_color, outline = out_color)
    img.show()
    save = input("save? (1/0): ")
    if save == "1":
        return blok_list
    else:
        return []
    





bloks = []
while(True):
    new_blok = make_image(random_blok_list())
    if new_blok != []:
        bloks.append(new_blok)
    cont = input("Continue?: ")
    if cont == "1":
        break
    







    
