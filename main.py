import titkositas
import dekodolas


valasztas:str = input ("(K)ódolni vagy (D)ekódolni szeretne? ")
fajlnev:str = input("Kérem adja meg a bemeneti fájl nevét: ")

if valasztas.upper() == "K":
    titkositas.szoveg_fajlbol(fajlnev)
if valasztas.upper() == "D":
    dekodolas.szoveg_fajlbol(fajlnev)

