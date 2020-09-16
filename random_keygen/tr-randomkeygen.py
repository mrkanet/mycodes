# coding: utf-8
# Bu kod Türkçe yazılmıştır.
# This code is written in Turkish.



import random

def check (strin,leng):
    ''' Bu fonksiyon, oluşturduğunuz şifreyi kısaltabilmenizi sağlar. Bunu rastgele yapar. Bu sayede daha güvenli bir şifre üretebilirsiniz.'''
    ret = ""
    while(leng != 0):
        ret += strin[random.randrange(len(strin))]
        leng -= 1
    return ret

print("Aşağıdaki seçeneklerden istediklerinize \"1\", istemediklerinize \"0\" yazın.")

tekrar = 1
indis = "0"

kar_say = int(input("Kaç karakterli parola oluşturmak istiyorsunuz?: "))

while (kar_say < 5):
    kar_say = int(input("Lütfen daha uzun karakterli parola isteyin.\nKaç karakterli parola oluşturmak istiyorsunuz?: "))
    
ku = int(input("Parola küçük harf barındırsın mı?: "))
bu = int(input("Parola büyük harf barındırsın mı?: "))
s = int(input("Parola sayı barındırsın mı?: "))
o = int(input("Parola özel karakter barındırsın mı?: "))


    

def kaydet(parola,indis):
    print("Parolanız programın olduğu dizine \"parola"+indis+".txt\" adı altında kaydedilecektir.")
    pdosya = open("parola"+indis+".txt","w")
    pdosya.write("Parola: "+parola+"\n")    
    pdosya.close()
    
    

        
while tekrar == 1:
    
    h_k = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
    h_b = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
    sayilar = ["1","2","3","4","5","6","7","8","9","0"]
    oz_kar = [",","!","'","+","%","&","/","(",")","=","*","?","\""]

    dizi = []
    
    if(ku == 1):
        dizi.append(h_k)
    if(bu == 1):
        dizi.append(h_b)
    if(s == 1):
        dizi.append(sayilar)
    if(o == 1):
        dizi.append(oz_kar)
            
    def random1(k):
        
        a = random.randrange(10000000)
        b = random.randrange(10000000)
        c = random.randrange(10000000)
        d = random.randrange(10000000)
        t = 5*(a-b/2)**2+(15/4)*(b-2*c/3)**2+(10/3)*(c-3*d/4)**2+(25/8)*(d-4/5)**2

        return t%len(dizi[k-1])

    parola = ""
    
    for i in range(kar_say):
        
        k = random.randrange(len(dizi))
        x = random1(k)
        
        parola += dizi[k-1][int(x)]

    print(parola)
    
    print("Aşağıdaki seçeneklerden istediklerinize \"1\", istemediklerinize \"0\" yazın.")  

    kayit = int(input("Parolanızı kaydetmek istiyor musunuz?: "))

    if(kayit == 1):
        kaydet(parola,indis)
        indis = str(int(indis)+1)

    
    tekrar = int(input("Yeni parola oluşturmak istiyor musunuz?: "))
    
    if(tekrar == 0):
        break
    
    kar_say = int(input("Kaç karakterli parola oluşturmak istiyorsunuz?: "))
    
    while (kar_say < 5):
        kar_say = int(input("Lütfen daha uzun karakterli parola isteyin.\nKaç karakterli parola oluşturmak istiyorsunuz?: "))
        
    ku = int(input("Parola küçük harf barındırsın mı?: "))
    bu = int(input("Parola büyük harf barındırsın mı?: "))
    s = int(input("Parola sayı barındırsın mı?: "))
    o = int(input("Parola özel karakter barındırsın mı?: "))
