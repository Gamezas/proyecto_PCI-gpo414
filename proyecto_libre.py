"""
Proyecto Libre
Hoje editable de D&D por medio de Python
EL programa permite al usuario crear un personaje de D&D de una forma
más comómoda y automática
"""

"""
============Funciones de cálculos============
"""
def modificador (num1):
    """
    (Uso de operadores, Uso de condicionales, Uso de estructuras de
    desición)
    recibe: num1 valor numérico
    compara el valor de num1 
    devuelve: un valor de modificador en base al valor de num1
    """
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

def score (atributo,dado):
    """
    (Uso de operadores)
    recibe: atributo valor numérico, dado valor numérico
    suma ambos valores
    devuelve: suma de los dos valores
    """
    return atributo + dado

def rango ():
    """
    (Uso de Ciclos while)
    No recibe datos
    Pide un valor num´rico al jugador entre 1 y 20, si este valor no
    cumple la condición, se le vuelve a pedir al jugador
    Devuelve: el valor ingresado dentro del parámetro indicado
    """
    valor = int(input())
    while valor < 1 or valor > 20:
        valor = int(input("El valor no puede ser menor a 1 o mayor a 20 " +
    "vuelve a intentarlo: "))
    return valor

"""
============Funciones auxiliares============
"""

def eleccion_raza(eleccion_elfo,eleccion_elfo2,stats):
    """
    Recibe: eleccion_elfo valor numérico, eleccion_elfo2 valor numérico
    stats lista anidada
    Dependiendo el valor de eleccion_elfo y eleccion_elfo2 se le suma
    1 punto a un valor específico de la lista
    Devuelve: Lista modificada
    """
    if eleccion_elfo == 1:
        stats[0][0] = stats[0][0] + 1
    elif eleccion_elfo == 2:
        stats[0][1] = stats[0][1] + 1
    elif eleccion_elfo == 3:
        stats[0][2] = stats[0][2] + 1
    elif eleccion_elfo == 4:
        stats[0][3] = stats[0][3] + 1
    elif eleccion_elfo == 5:
        stats[0][4] = stats[0][4] + 1
    elif eleccion_elfo == 6:
        stats[0][5] = stats[0][5] + 1
    
    if eleccion_elfo2 == 1:
        stats[0][0] = stats[0][0] + 1
    elif eleccion_elfo2 == 2:
        stats[0][1] = stats[0][1] + 1
    elif eleccion_elfo2 == 3:
        stats[0][2] = stats[0][2] + 1
    elif eleccion_elfo2 == 4:
        stats[0][3] = stats[0][3] + 1
    elif eleccion_elfo2 == 5:
        stats[0][4] = stats[0][4] + 1
    elif eleccion_elfo2 == 6:
        stats[0][5] = stats[0][5] + 1
    return stats

"""
============Parte principal del programa============
"""

print("Bienvenido al simplificador de hoja de personaje de D&D")
nombre_j = str(input("¿Cuál es tu nombre jugador? "))
eleccion1 = int(input("Selecciona con un número que raza te gustaría jugar" +
 " 1. Human, 2. Tiefling, 3.Halfling, 4.Dwarf, 5.Elf, 6.Gnome, " + 
 "7. Half-Orc 8.Dragonborn 9.Half-Elf: "))

#Se le da la oportunidad al jugador de elegir una raza

if eleccion1 == 1:
    stats = [[1,1,1,1,1,1],["30 ft","Humanos","Medium"]]
elif eleccion1 == 2:
    stats = [[0,0,0,1,0,2],["30ft","Tiefling","Medium"]]
elif eleccion1 == 3:
    stats = [[0,2,0,0,0,0],["25ft","Halfling","Small"]]
elif eleccion1 == 4:
    stats = [[0,0,2,0,0,0],["25ft","Dwarf","Medium"]]
elif eleccion1 == 5:
    stats = [[0,2,0,0,0,0],["30ft","Elf","Medium"]]
elif eleccion1 == 6:
    stats = [[0,0,0,0,2,0],["25ft","Gnome","Small"]]
elif eleccion1 == 7:
    stats = [[2,0,1,0,0,0],["30ft","Half-Orc","Medium"]]
elif eleccion1 == 8:
    #Esta raza permite más opciones que las otras
    stats = [[2,0,0,0,0,1],["30ft","Dragonborn","Medium"]]
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
elif eleccion1 == 9:
    #Esta raza da uso a la función auxiliar
    stats = [[0,0,0,0,0,2],["30ft", "Half-Elf", "Medium"]]
    eleccion_elfo = int(input("Esta raza te deja elegir 1 punto más en dos " +
    "habilidades que gustes elige la primera 1.Fuerza 2.Destreza " +
    "3. Constitución 4.Inteligencia 5.Sabiduría 6.Carisma: "))
    eleccion_elfo2 = int(input("Elige la segunda 1.Fuerza 2.Destreza " +
    "3. Constitución 4.Inteligencia 5.Sabiduría 6.Carisma: "))
    stats = eleccion_raza(eleccion_elfo,eleccion_elfo2,stats)

#El jugador ingresa los valores obtenidos por sus dados
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

#Se da uso de la función score
strg_sc = score(stats[0][0],strg)
dex_sc = score(stats[0][1],dex)
const_sc = score(stats[0][2], const)
smart_sc = score(stats[0][3],smart)
wisd_sc = score(stats[0][4],wisd)
char_sc = score(stats[0][5],char)

#Se da uso de la función modificador
strg_mod = modificador(strg_sc)
dex_mod = modificador(dex_sc)
const_mod = modificador(const_sc)
smart_mod = modificador(smart_sc)
wisd_mod = modificador(wisd_sc)
char_mod = modificador(char_sc)


#El jugador tiene la oprtunidad de elegir la clase de su personaje
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

#El programa regresa los datos calculados
print ("Tu personaje esta listo!!")
print ("\n/////////Características/////////\n")
print ("Jugador: ", nombre_j)
print ("Presonaje: ", nombre_p)
print ("Tu raza es ", stats[1][1])
print ("El tamaño de tu personaje es: ", stats[1][2])
if eleccion1 == 8:
    print ("Dragonic Ancestry: ", stats[1][3])
    print ("Tipo de daño: ", stats[1][4])
    print ("Rango de esta habilidad: ", stats[1][5])
print ("Tu clase es ", stats[2][0])
print ("La velocidad de tu personaje es ", stats[1][0])
print ("Bonus de competencia: ", stats[2][1])
print ("Puntos de vida o hit dice: ", stats[2][3])
print ("El dado que usarás para hacer daño o hit dice es:", clase[2][2])
print ("\n/////////Estadisticas/////////\n")
print ("Tu score de habilidad en fuerza es: ", strg_sc, "y tu modificador es:",
strg_mod)
print ("Tu score de habilidad en destreza es: ", dex_sc, "y tu modificador",
"es: ", dex_mod)
print ("Tu score de habilidad en constitución es: ", const_sc, "y tu", 
"modificador es: ", const_mod)
print ("Tu score de habilidad en inteligancia es: ", smart_sc, "y tu",
"modificador es: ", smart_mod)
print ("Tu score de habilidad en sabiduría es: ", wisd_sc, "y tu modificador",
"es: ", wisd_mod)
print ("Tu score de habilidad en charisma es: ", char_sc, "y tu modificador",
"es: ", char_mod)
print("Buena suerte aventurero")
