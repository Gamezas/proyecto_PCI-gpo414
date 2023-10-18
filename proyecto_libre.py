"""
Proyecto Libre
Hoja editable de D&D por medio de Python
El programa permite al usuario crear un personaje de D&D de una forma
más cómoda y automática
"""

"""
Biblioteca
Python: https://docs.python.org/3/library/random.html
Esta biblioteca se usará en la generación de numeros aleatorios para
las estadísticas del jugador
"""
import random


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
    Pide un valor numérico al jugador entre 1 y 20, si este valor no
    cumple la condición, se le vuelve a pedir al jugador
    Devuelve: el valor ingresado dentro del parámetro indicado
    """
    valor = int(input())
    while valor < 1 or valor > 20:
        valor = int(input("El valor no puede ser menor a 1 o mayor a 20" + 
        " vuelve a intentarlo: "))
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
ciclo = 1
print("Bienvenido al simplificador de hoja de personaje de D&D")
nombre_j = str(input("¿Cuál es tu nombre jugador? "))
while ciclo == 1:
    #Este ciclo permite reiniciar el programa si el jugador desea
    
    eleccion1 = int(input("Selecciona con un número que raza te gustaría " +
    "jugar:\n1.Human\n2.Tiefling\n3.Halfling\n4.Dwarf\n5.Elf\n6.Gnome" + 
    "\n7.Half-Orc\n8.Dragonborn\n9.Half-Elf:\n"))

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
        eleccion_drag = int(input("Elige con número que Dragonic Ancestry " + 
        "te gustaría: \n1.Black\n2.Blue\n3.Brass\n4.Bronze\n5.Copper\n6.Gold" +
        "\n7.Green\n8.Red\n9.Silver\n10. White:\n"))
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
        eleccion_elfo = int(input("Esta raza te deja elegir 1 punto más" +
        "en dos habilidades que gustes elige la primera:\n1.Fuerza" +
        "\nDestreza\n3.Constitución\n4.Inteligencia\n5.Sabiduría" +
        "\n6.Destreza\n"))
        eleccion_elfo2 = int(input("Elige la segunda\n1.Fuerza\n2.Destreza" +
        "\n3.Constitución\n4.Inteligencia\n5.Sabiduría\n6.Carisma\n "))
        stats = eleccion_raza(eleccion_elfo,eleccion_elfo2,stats)
    eleccionrnd = int(input("Elije con un número si te gustaría introducir " +
    "los valores de tus estadísticas o prefieres que sea aleatorio por el " +
    "sistema:\n1.Introducir valores\n2.Aleatorio\n"))
    
    if eleccionrnd == 1:
        #El jugador ingresa los valores obtenidos por sus dados
        print("Introduce el valor de la estadística de fuerza: ")
        strg = rango()
        print("Introduce el valor de la estadística de destreza: ")
        dex = rango()
        print("Introduce el valor de la estadística de constitución: ")
        const = rango()
        print("Introduce el valor de la estadística de inteligencia: ")
        smart = rango()
        print("Introduce el valor de la estadística de sabiduría: ")
        wisd = rango()
        print("Introduce el valor de la estadística de carisma: ")
        char = rango()
    else:
        """
        Con ayuda de la librería random se puede usar la función 
        "random.randrange()" para obtener un valor desde el 1 
        (incluido) hasta el 21 (no incluido) esto para asimilar la
        tirada de un dado de 20 caras
        """
        strg = (random.randrange(1, 21))
        dex = (random.randrange(1, 21))
        const = (random.randrange(1, 21))
        smart = (random.randrange(1, 21))
        wisd = (random.randrange(1, 21))
        char = (random.randrange(1, 21))

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


    #El jugador tiene la oportunidad de elegir la clase de su personaje
    eleccion2 = int(input("Elige con número una clase:\n1.Rogue\n2.Ranger" + 
    "\n3.Barbarian\n4.Bard\n5.Cleric\n6.Druid\n7.Fighter\n8.Monk\n9.Paladin" +
    "\n10.Sorcerer\n11.Warlock\n12.Wizard\n13.Artificier\n"))

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
    print ("Personaje: ", nombre_p)
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
    print ("\n/////////Estadísticas/////////\n")
    print ("Tu score de habilidad en fuerza es: ", strg_sc, "y tu" +
    "modificador es: ", strg_mod)
    print ("Tu score de habilidad en destreza es: ", dex_sc, "y" +
    "tu modificador es: ", dex_mod)
    print ("Tu score de habilidad en constitución es: ", const_sc, "y tu", 
    "modificador es: ", const_mod)
    print ("Tu score de habilidad en inteligancia es: ", smart_sc, "y tu",
    "modificador es: ", smart_mod)
    print ("Tu score de habilidad en sabiduría es: ", wisd_sc, "y tu" +
    "modificador es: ", wisd_mod)
    print ("Tu score de habilidad en carisma es: ", char_sc, "y tu" +
    "modificador es: ", char_mod)
    ciclo = int(input("¿Te gustaría hacer otro personaje?\n1.Si\n2.No\n"))
print("Buena suerte aventurero")
