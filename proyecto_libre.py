print("Bienvenido al simplificador de hoja de personaje de D&D")
eleccion1 = int(input("Selecciona con un número que raza te gustaría jugar" +
 "1. Humano, 2. Tiefling: "))

if eleccion1 == 1:
    strg_sc = 1
    dex_sc = 1
    const_sc = 1
    smart_sc = 1
    wisd_sc = 1
    char_sc = 1
    Speed = "30 ft"
    raza = "Humano"
else:
    strg_sc = 0
    dex_sc = 0
    const_sc = 0
    smart_sc = 1
    wisd_sc = 0
    char_sc = 2
    speed = "30 ft"
    raza = "Tiefling"

print ("Bien ahora vayamos con tus valores de habilidad")
strg = int(input("Tira un dado de 20 caras y valor escribelo aquí" +
"este será tu valor de fuerza: "))

dex = int(input("Tira otro dado de 20 para tu valor de destreza: "))
const = int(input("Tira otro dado de 20 para tu valor de constitución: "))
smart = int(input("Tira otro dado de 20 para tu valor de inteligencia: "))
wisd = int(input("Tira otro dado de 20 para tu valor de sabiduría: "))
char = int(input("Tira otro dado de 20 para tu valor de carisma: "))

strg_sc = strg_sc + strg
dex_sc = dex_sc + dex
const_sc = const_sc + const
smart_sc = smart_sc + smart
wisd_sc = wisd_sc + wisd
char_sc = char_sc + char

def modificador (num1):
    if num1 >= 0 and num1 <= 1:
        mod = 0 - 5
        return mod
    elif num1 >= 2 and num1<= 3:
        mod = 0 - 4
        return mod
    elif num1 >= 4 and num1 <= 5:
        mod = 0 - 3
        return mod
    elif num1 >= 6 and num1 <= 7:
        mod = 0 - 2
        return mod
    elif num1 >= 8 and num1 <= 9:
        mod = 0 - 1
        return mod
    elif num1 >= 10 and num1 <= 11:
        mod = 0 + 0
        return mod
    elif num1 >= 12 and num1 <= 13:
        mod = 0 + 1
        return mod
    elif num1 >= 14 and num1 <= 15:
        mod = 0 + 2
        return mod
    elif num1 >= 16 and num1 <= 17:
        mod = 0 + 3
        return mod
    elif num1 >= 18 and num1 <= 19:
        mod = 0 + 4 
        return mod
    elif num1 >= 20 and num1 <= 21:
        mod = 0 + 5
        return mod
    else:
        mod = 0 + 6
        return mod


strg_mod = modificador(strg_sc)
dex_mod = modificador(dex_sc)
const_mod = modificador(const_sc)
smart_mod = modificador(smart_sc)
wisd_mod = modificador(wisd_sc)
char_mod = modificador(char_sc)

print ("Tu personaje esta listo!!")
print ("Tu raza es" + raza)
print ("Tu score de habilidad en fuerza es: ", strg_sc, "y tu modificador es:",
strg_mod)
print ("Tu score de habilidad en destreza es: ", dex_sc, "y tu modificador",
"es: ", dex_mod)
print ("Tu score de habilidad en constitución es: ", dex_sc, "y tu", 
"modificador es: ", dex_mod)
print ("Tu score de habilidad en inteligancia es: ", smart_sc, "y tu",
"modificador es: ", smart_mod)
print ("Tu score de habilidad en sabiduría es: ", wisd_sc, "y tu modificador",
"es: ", wisd_mod)
print ("Tu score de habilidad en charisma es: ", char_sc, "y tu modificador",
"es: ", char_mod)
print("Buena suerte aventurero")