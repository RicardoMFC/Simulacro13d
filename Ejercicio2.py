
def luck_check(lista):
    suma1=0
    suma2=0
    for i in range (int(len(lista)/2)):
        suma1+=lista[i]
        suma2+=lista[len(lista)-1-i]
    if suma1==suma2:
        return True
    else:
        return False

def main():
    lista=[1,2,3,3,2,0]
    resultado=luck_check(lista)
    print(resultado)


if __name__=='__main__':
    main()
