def cambio_matrix(matriz):
    matriz2 = []
    for i in range(len(matriz)):
        matriz2.append([])
        for j in range(len(matriz[i])):
            matriz2[i].append(matriz[j][i])

    for i in range(len(matriz)):
        matriz2[i].reverse()

    return matriz2
    

def main():
    matriz = [[1,2,3],[4,5,6],[7,8,9]]
    print(matriz[2])
    print(cambio_matrix(matriz))


if __name__=='__main__':
    main()




