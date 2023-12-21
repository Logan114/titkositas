ABC = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z",".",":","?","!"," "]
titkosABC = ["X","Y","Z","A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W",".",":","?","!"," "]
titkosSzoveg=""

def szoveg_fajlbol(filename):
    file = open(filename,"r",encoding="UTF-8")
    szoveg = (file.read()).upper()
    titkosSzoveg:str = ""
    print(szoveg)

    for i in range (0, (len(szoveg)),1):
        aktBetu = szoveg[i]
        if aktBetu == "Á":
            aktBetu = "A"
        if aktBetu == "Ö" or aktBetu == "Ő" or aktBetu == "Ó":
            aktBetu = "O"
        if aktBetu == "Ü" or aktBetu == "Ű" or aktBetu == "Ü" or aktBetu == "ú":
            aktBetu = "U"
        if aktBetu in ABC:
            idx = ABC.index(aktBetu)

            titkosSzoveg += titkosABC[idx]

    print(f"A kódolt szöveg:\n {titkosSzoveg}")

