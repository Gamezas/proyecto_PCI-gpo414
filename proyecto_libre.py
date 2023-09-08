"""
El objetivo de esta función es calcular el modificador de las habilidades del
jugador de froma rápida
"""
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
"""
Esta función aunque es simple permite calcular el score total del jugador en 
una habilidad sumando el score fijo de su rza y lo conseguido en el dado
"""
"""
Esta funcion a pesar de ser simple permite indetificar su uso y facilitar el 
uso de operadores del código
"""
def score (atributo,dado):
    return atributo + dado

print("Bienvenido al simplificador de hoja de personaje de D&D")
nombre_j = str(input("¿Cuál es tu nombre aventurero? "))
eleccion1 = int(input("Selecciona con un número que raza te gustaría jugar" +
 " 1. Humano, 2. Tiefling, 3.Halfling, 4.Dwarf, 5.Elfo, 6.Gnomo: "))
"""
Aquí se coloca la elección de razas lo que provoca que algunas estadisticas 
tengan ciertos atributos a favor desde un inicio de igual forma ayuda a mantener
un seguimiento de las mismas
"""
if eleccion1 == 1:
    strg_atr = 1
    dex_atr = 1
    const_atr = 1
    smart_atr = 1
    wisd_atr = 1
    char_atr = 1
    speed = "30 ft"
    raza = "Humano"
elif eleccion1 == 2:
    strg_atr = 0
    dex_atr = 0
    const_atr = 0
    smart_atr = 1
    wisd_atr = 0
    char_atr = 2
    speed = "30 ft"
    raza = "Tiefling"

elif eleccion1 == 3:
    strg_atr = 0
    dex_atr = 2
    const_atr = 0
    smart_atr = 0
    wisd_atr = 0
    char_atr = 0
    speed = "25 ft"
    raza = "Halfling"

elif eleccion1 == 4:
    strg_atr = 0
    dex_atr = 0
    const_atr = 2
    smart_atr = 0
    wisd_atr = 0
    char_atr = 0
    speed = "25 ft"
    raza = "Dwarf"

elif eleccion1 == 5:
    strg_atr = 0
    dex_atr = 2
    const_atr = 0
    smart_atr = 0
    wisd_atr = 0
    char_atr = 0
    speed = "30 ft"
    raza = "Elfo"

else:
    strg_atr = 0
    dex_atr = 0
    const_atr = 0
    smart_atr = 0
    wisd_atr = 2
    char_atr = 0
    speed = "25 ft"
    raza = "Gnomo"
    
"""
Las estadísticas de D&D son medidas con una tirada de un dado de 20 caras
aquí el usuario podra introducir los valores obtenido por sus tiradas y estas
se añadiran más adelante con los atributos iniciales para así identificar 
el modificador correcto
"""
print ("Bien ahora vayamos con tus valores de habilidad")
strg = int(input("Tira un dado de 20 caras y valor escribelo aquí" +
"este será tu valor de fuerza: "))

dex = int(input("Tira otro dado de 20 para tu valor de destreza: "))
const = int(input("Tira otro dado de 20 para tu valor de constitución: "))
smart = int(input("Tira otro dado de 20 para tu valor de inteligencia: "))
wisd = int(input("Tira otro dado de 20 para tu valor de sabiduría: "))
char = int(input("Tira otro dado de 20 para tu valor de carisma: "))

"""
Utilizando la función score sacamos el score total de las habilidades del 
usuario
"""
strg_sc = score(strg_atr,strg)
dex_sc = score(dex_atr,dex)
const_sc = score(const_atr, const)
smart_sc = score(smart_atr,smart)
wisd_sc = score(wisd_atr,wisd)
char_sc = score(char_atr,char)
"""
Utilizando la función modificador conseguimos el valor del modificador de las
habilidades del usuraio
"""
strg_mod = modificador(strg_sc)
dex_mod = modificador(dex_sc)
const_mod = modificador(const_sc)
smart_mod = modificador(smart_sc)
wisd_mod = modificador(wisd_sc)
char_mod = modificador(char_sc)

"""
Aquí el jugador va a poder elegir que clase va a querer para su personaje, lo
que va a permitir mayor cantidad de posibilidades para lo que el jugador quiera
 experimentar en su partida, se elige hasta este punto ya que se necesita el 
modificador para calcular la vida del jugador
"""
eleccion2 = int(input("¿Que clase quieres jugar? 1.Rogue, 2.Ranger, " + 
"3.Barbarian, 4.Bard: "))

if eleccion2 == 1:
    clase = "Rogue"
    p_bonus = "+2"
    hit_dice = "1d8"
    hit_points = 8 + const_mod
elif eleccion2 == 2:
    clase = "Ranger"
    p_bonus = "+2"
    hit_dice = "1d10"
    hit_points = 10 + const_mod
elif eleccion2 == 3:
    clase = "Barbarian"
    p_bonus = "+2"
    hit_dice = "1d12"
    hit_points = 12 + const_mod
else:
    clase = "Bard"
    p_bonus = "+2"
    hit_dice = "1d8"
    hit_points = 8 + const_mod

nombre_p = str(input("Para terminar ¿cómo vas a llamar a tu personaje? "))

"""
Se le dan al usuario todas las estadisticas calculadas por el programa
"""
print ("Tu personaje esta listo!!")
print ("Jugador: ", nombre_j)
print ("Presonaje: ", nombre_p)
print ("Tu raza es ", raza)
print ("Tu clase es ", clase)
print ("La velocidad de tu personaje es ", speed)
print ("Bonus de competencia: ", p_bonus)
print ("Puntos de vida o hit dice: ", hit_points)
print ("El dado que usarás para hacer daño o hit dice es:", hit_dice)
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
