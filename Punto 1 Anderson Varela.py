def num():
    n = int(input("Digite un numero "))
    if  n > 0:
        print("El numero ",n,"es positivo")
    elif n < 0 :
         print("El numero ",n,"es negativo ")
    elif n == 0 :
        print("El numero es igual a cero")
    return n
def num2():
    n2 = int(input("Digite un numero "))
    if  n2 > 0:
        print("El numero ",n2,"es positivo")
    elif n2 < 0 :
         print("El numero ",n2,"es negativo ")
    elif n2 == 0 :
        print("El numero es igual a cero")
    return n2

def fibo():
    a = []
    i = 0
    n = 1
    cont = 0
    while cont < 100:
        fibonacci = i + n

        i = n
        n= fibonacci
        cont+=1
        a.append(fibonacci)
    return a
def primo(n):
    for i in range(1,100):

        if n % n == 0 and n % i == 0  :
            print(n, "Es un numero primo")
        elif n // i != 0 :
            print(n,"No es un numero primo")
def primos(n2):
    for i in range(1,100):
        if n2 % n2 == 1 and n2 % i == 0 :
            print(n2, "Es un numero primo")
        elif n2 % n2 != 1 :
            print(n2,"No es un numero primo")

def inter(n,n2):
    l = []
    if n > n2:
        while n > n2 :
            n2 += 1
            
            l.append(n2)
    elif n2 > n :
        while n2 > n:
            n +=1
            l.append(n)
    elif n==n2:
        print("Son iguales")
    for i in range(0,len(l)-1):
        j = i+1
        numa = l[i]+l[j]
        suma = numa
        
        
        
    print(suma)


def main():
    n = num()
    n2 = num2()
    a = fibo()
    if n in a:
        print(n,"Es un numero de la secuencia de fibonacci")
    elif n not in a:
        print(n,"No es un numero de la secuencia fibonacci")
    print()

    if n2 in a:
        print(n2,"Es un numero de la secuencia de fibonacci")
    elif n2 not in a:
        print(n2,"No es un numero de la secuencia fibonacci")

    inter(n,n2)

main()
