def palabras_clave(texto):
    listaaux=[]
    for i in range (1,len(texto)):
        if texto[i-1]=='#' and texto[i]=='#':
            j=i+1
            while texto[j]!='#':
                listaaux.append(texto[j])
                j+=1
            i=j
    return listaaux



def main():
    cadena=["#","#","#","g","o", "#","g","o","#","#","h","o","l","a"]
    resultado=palabras_clave(cadena)
    print(resultado)

if __name__=='__main__':
    main()