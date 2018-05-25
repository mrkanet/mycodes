import random

print("Plese insert \"1\" or \"0\" to the following")

again = 1
counter = "0"

char_long = int(input("How many characters long is enough for your password?: "))

while (char_long < 5):
    char_long = int(input("Longer please.\nHow many characters long is enough for your password?: "))
    
lc = int(input("Do you want lower case in your password?: "))
uc = int(input("Do you want upper case in your password?: "))
n = int(input("Do you want number in your password?: "))
sc = int(input("Do you want special character in your password?: "))

def kaydet(password,counter):
    print("Your password will be saved to program\'s directory as named \"password"+counter+".txt\"")
    pdosya = open("password"+counter+".txt","w")
    pdosya.write("Password: "+password+"\n")    
    pdosya.close()
    
    

        
while again == 1:
    
    l_c = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
    u_c = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
    numbers = ["1","2","3","4","5","6","7","8","9","0"]
    spec_char = [",","!","'","+","%","&","/","(",")","=","*","?","\""]

    serie = []
    
    if(lc == 1):
        serie.append(l_c)
    if(uc == 1):
        serie.append(u_c)
    if(n == 1):
        serie.append(numbers)
    if(sc == 1):
        serie.append(spec_char)
            
    def random1(k):
        
        a = random.randrange(10000000)
        b = random.randrange(10000000)
        c = random.randrange(10000000)
        d = random.randrange(10000000)
        t = 5*(a-b/2)**2+(15/4)*(b-2*c/3)**2+(10/3)*(c-3*d/4)**2+(25/8)*(d-4/5)**2

        return t%len(serie[k-1])

    password = ""
    
    for i in range(char_long):
        
        k = random.randrange(len(serie))
        x = random1(k)
        
        password += serie[k-1][int(x)]

    print(password)
    
    print("Plese insert \"1\" or \"0\" to the following")
    
    save = int(input("Do you want to save your password?: "))

    if(save == 1):
        kaydet(password,counter)
        counter = str(int(counter)+1)

    
    again = int(input("Do you want new password?: "))
    
    if(again== 0):
        break
    
    char_long = int(input("How many characters long is enough for your password?: "))
    
    while (char_long < 5):
        char_long = int(input("Longer please.\nHow many characters long is enough for your password?: "))
        
    lc = int(input("Do you want lower case in your password?: "))
    uc = int(input("Do you want upper case in your password?: "))
    n = int(input("Do you want number in your password?: "))
    sc = int(input("Do you want special character in your password?: "))
