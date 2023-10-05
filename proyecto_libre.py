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
una habilidad sumando el score fijo de su raza y lo conseguido en el dado
"""

def score (atributo,dado):
    return atributo + dado

"""
Esta función permite simplificar el código y permitir el uso de ciclos con el
objetivo que el usuario introduzca un valor correcto para así evitar que hagan
trampa a la hora de generar su personaje por tener mejores estadisticas a las
permitidas
"""

def rango ():
    valor = int(input())
    while valor < 1 or valor > 20:
        valor = int(input("El valor no puede ser menor a 1 o mayor a 20 " +
    "vuelve a intentarlo: "))
    return valor

"""
Aquí empieza el código, se le da la bienvenida al usuario y se toman sus datos
para iniciar su personaje
"""
print("Bienvenido al simplificador de hoja de personaje de D&D")
nombre_j = str(input("¿Cuál es tu nombre aventurero? "))
eleccion1 = int(input("Selecciona con un número que raza te gustaría jugar" +
 " 1. Human, 2. Tiefling, 3.Halfling, 4.Dwarf, 5.Elf, 6.Gnome, " + 
 "7. Half-Orc 8.Dragonborn: "))
"""
Aquí el jugador elige una raza de las que ofrece el juego, todas tiene ciertos
atributos a favor dando puntos extra de inicio en algunas habilidades, esto se
guarda en una lista llamada "stats" que busca llevar todos los datos del 
jugador en una sola variable, la raza Dragonborn es un poco más especial
ya que se debe elegir una "Dragonic Ancestry" que es algo unico de esta raza
por lo que tiene una función de elecciones extra a diferencia de las otras
"""
if eleccion1 == 1:
    stats = [[1,1,1,1,1,1],["30 ft","Humanos"]]
elif eleccion1 == 2:
    stats = [[0,0,0,1,0,2],["30ft","Tiefling"]]
elif eleccion1 == 3:
    stats = [[0,2,0,0,0,0],["25ft","Halfling"]]
elif eleccion1 == 4:
    stats = [[0,0,2,0,0,0],["25ft","Dwarf"]]
elif eleccion1 == 5:
    stats = [[0,2,0,0,0,0],["30ft","Elf"]]
elif eleccion1 == 6:
    stats = [[0,0,0,0,2,0],["25ft","Gnome"]]
elif eleccion1 == 7:
    stats = [[2,0,1,0,0,0],["30ft","Half-Orc"]]
elif eleccion1 == 8:
    stats = [[2,0,0,0,0,1],["30ft","Dragonborn"]]
    eleccion_drag = int(input("Elige que Dragonic Ancestry te gustaría " + 
    "1.Black, 2.Blue, 3.Brass, 4.Bronze, 5.Copper, 6.Gold, " +
    "7. Green, 8.Red, 9. Silver, 10. White: "))
    if eleccion_drag == 1:
        stats[1].append("Black")
        stats[1].append("Acid")
        stats[1].append("5 by 30 ft. line (Dex. save)")
    elif eleccion_drag == 2:
        stats[1].append("Blue")
        stats[1].append("Lightning")
        stats[1].append("5 by 30 ft. line (Dex. save)")
    elif eleccion_drag == 3:
        stats[1].append("Brass")
        stats[1].append("Fire")
        stats[1].append("5 by 30 ft. line (Dex. save)")
    elif eleccion_drag == 4:
        stats[1].append("Bronze")
        stats[1].append("Lightning")
        stats[1].append("5 by 30 ft. line (Dex. save)")
    elif eleccion_drag == 5:
        stats[1].append("Copper")
        stats[1].append("Acid")
        stats[1].append("5 by 30 ft. line (Dex. save)")
    elif eleccion_drag == 6:
        stats[1].append("Gold")
        stats[1].append("Fire")
        stats[1].append("15 ft. cone (Dex. save)")
    elif eleccion_drag == 7:
        stats[1].append("Green")
        stats[1].append("Poison")
        stats[1].append("15 ft. cone (Con. save)")
    elif eleccion_drag == 8:
        stats[1].append("Red")
        stats[1].append("Fire")
        stats[1].append("15 ft. cone (Dex. save)")
    elif eleccion_drag == 9:
        stats[1].append("Silver")
        stats[1].append("Cold")
        stats[1].append("15 ft. cone (Con. save)")
    else:
        stats[1].append("White")
        stats[1].append("Cold")
        stats[1].append("15 ft. cone (Con. save)")

"""
Las estadísticas de D&D son medidas con una tirada de un dado de 20 caras
aquí el usuario podra introducir los valores obtenido por sus tiradas y estas
se añadiran más adelante con los atributos iniciales para así identificar 
el modificador correcto

Se aprovechan ciclos aquí ya que los valores de las tiradas no pueden ser 
menores a 1 o mayores a 20, esto para evitar que los jugadores hagan trampa
en la creación de sus estadísticas
"""

print("Tira un dado de 20 caras y valor escribelo aquí" +
"este será tu valor de fuerza: ")
strg = rango()
print("Tira otro dado de 20 para tu valor de destreza: ")
dex = rango()
print("Tira otro dado de 20 para tu valor de constitución: ")
const = rango()
print("Tira otro dado de 20 para tu valor de inteligencia: ")
smart = rango()
print("Tira otro dado de 20 para tu valor de sabiduría: ")
wisd = rango()
print("Tira otro dado de 20 para tu valor de carisma: ")
char = rango()

"""
Utilizando la función score sacamos el score total de las habilidades del 
usuario
"""
strg_sc = score(stats[0][0],strg)
dex_sc = score(stats[0][1],dex)
const_sc = score(stats[0][2], const)
smart_sc = score(stats[0][3],smart)
wisd_sc = score(stats[0][4],wisd)
char_sc = score(stats[0][5],char)
"""
Utilizando la función modificador conseguimos el valor del modificador de las
habilidades del usuraio este modificador tiene cierta influencia en algunas
estadísticas como la salud del jugador
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
"3.Barbarian, 4.Bard, 5.Cleric, 6.Druid, 7.Fighter, 8.Monk, 9.Paladin, " +
"10.Sorcerer, 11.Warlock, 12.Wizard, 13.Artificier: "))

if eleccion2 == 1:
    clase = ["Rogue","+2","1d8"]
    clase.append(8 + const_mod)
    stats.append(clase)
elif eleccion2 == 2:
    clase = ["Ranger","+2","1d10"]
    clase.append(10 + const_mod)
    stats.append(clase)
elif eleccion2 == 3:
    clase = ["Barbarian","+2","1d12"]
    clase.append(12 + const_mod)
    stats.append(clase)
elif eleccion2 == 4:
    clase = ["Bard","+2","1d8"]
    clase.append(8 + const_mod)
    stats.append(clase)
elif eleccion2 == 5:
    clase = ["Cleric","+2","1d8"]
    clase.append(8 + const_mod)
    stats.append(clase)
elif eleccion2 == 6:
    clase = ["Druid","+2","1d8"]
    clase.append(8 + const_mod)
    stats.append(clase)
elif eleccion2 == 7:
    clase = ["Fighter","+2","1d10"]
    clase.append(10 + const_mod)
    stats.append(clase)
elif eleccion2 == 8:
    clase = ["Monk","+2","1d8"]
    clase.append(8 + const_mod)
    stats.append(clase)
elif eleccion2 == 9:
    clase = ["Paladin","+2","1d10"]
    clase.append(10 + const_mod)
    stats.append(clase)
elif eleccion2 == 10:
    clase = ["Sorcerer","+2","1d6"]
    clase.append(6 + const_mod)
    stats.append(clase)
elif eleccion2 == 11:
    clase = ["Warlock","+2","1d8"]
    clase.append(8 + const_mod)
    stats.append(clase)
elif eleccion2 == 12:
    clase = ["Wizard","+2","1d6"]
    clase.append(6 + const_mod)
    stats.append(clase)
else:
    clase = ["Artificier","+2","1d8"]
    clase.append(8 + const_mod)
    stats.append(clase)
    
nombre_p = str(input("Para terminar ¿cómo vas a llamar a tu personaje? "))

"""
Se le dan al usuario todas las estadisticas calculadas por el programa
"""
print ("Tu personaje esta listo!!")
print ("Jugador: ", nombre_j)
print ("Presonaje: ", nombre_p)
print ("Tu raza es ", stats[1][1])
if eleccion1 == 8:
    print ("Dragonic Ancestry: ", stats[1][2])
    print ("Tipo de daño: ", stats[1][3])
    print ("Rango de esta habilidad: ", stats[1][4])
print ("Tu clase es ", stats[2][0])
print ("La velocidad de tu personaje es ", stats[1][0])
print ("Bonus de competencia: ", stats[2][1])
print ("Puntos de vida o hit dice: ", stats[2][3])
print ("El dado que usarás para hacer daño o hit dice es:", clase[2][2])
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
