def fibonacci(termino):
    lista=[0,1]
    if termino == 0:
        return 0
    elif termino == 1:
        return 1
    else:
        for i in range(2,termino+1):
            lista.append(lista[i-1]+lista[i-2])
    return lista[termino]

def main():
    termino = int(input("Ingrese un número entero: "))
    print(fibonacci(termino))

if __name__=='__main__':
    main()
