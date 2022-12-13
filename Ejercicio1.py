def palabras_clave(texto):
    listaaux=[]
    for i in range (2,len(texto),1):
        if texto[i-1]=='#' and texto[i]=='#':
            j=i+1
            while texto[j]!='#':
                listaaux.append(texto[j])
            i=j
    return listaaux



def main():
    cadena=["#","#","#","g","o", "#","g","o","#","#","h","o","l","a"]
    resultado=palabras_clave(cadena)
    print(resultado)

if __name__=='__main__':
    main()