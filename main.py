import random

# ========= ENTRÉES UTILISATEUR =========

len_table = input("DÉFINIR LONGUEUR TABLEAU : ")
len_table = int(len_table)
table_type = input("Choisir le type de tableau :\n 1 - Random \n 2 - Best case \n 3 - Worst case \n")

case = input(
    "Choisir le type de tri :\n tri 1 : tri par selection,\n tri 2 : tri par insertion,\n tri 3 : tri à bulle (ou tri par propagation)\n tri 4 : tri à bulle optimisé \n 0 : Tout les tris \n")

# ========= EVAL POINT  =========

point_tri_selection = 0
point_tri_insertion = 0
point_tri_bulle = 0
point_tri_bulle_opti = 0

#FONCTIONS

# ========= TABLEAU RANDOM =========

def tableau_random():
    table_random = []
    for i in range(int(len_table)):
        table_random.append(random.randint(0, 100))
    print("[========= ========= =========]")
    print("TABLE RANDOM : " + str(table_random))
    print("[========= ========= =========]")
    return table_random

table_random = tableau_random()

# ========= TABLEAU BEST CASE =========

def tableau_best_case():
    table_best_case = []
    for i in range(int(len_table)):
        table_best_case.append(i)
    print("TABLE MEILLEUR SCENARIO : " + str(table_best_case))
    print("[========= ========= =========]")
    return table_best_case

table_best_case = tableau_best_case()

# ========= TABLEAU WORST CASE =========

def tableau_worst_case():
    table_worst_case = []
    for i in range(int(len_table)):
        table_worst_case.append(i)
    table_worst_case.reverse()
    print("TABLE PIRE SCENARIO : " + str(table_worst_case))
    print("[========= ========= =========]")
    return table_worst_case

table_worst_case = tableau_worst_case()

def tri_selection(data):
    databefore = data.copy()
    print("[======= TRI SELECTION =======]")
    print("Tableau avant " + str(databefore))

    point_tri_selection = 0

    for i in range(len(data)):
        min = i
        for u in range(i + 1, len(data)):
            if data[min] > data[u]:
                point_tri_selection += 1
                min = u
        tmp = data[i]
        data[i] = data[min]
        point_tri_selection += 3
        data[min] = tmp

    print("Tableau après " + str(data))
    print("Nombre de point : " + str(point_tri_selection))

    if (databefore == data):
        print("ERREUR TRIAGE")
    else:
        print("TRIAGE OK")
    print("[========= ========= =========]")
    print(" ")

# ========= TRI INSERTION =========

def tri_insertion(data):
    databefore = data.copy()
    print("[======= TRI INSERTION =======]")
    print("Tableau avant " + str(databefore))

    point_tri_insertion = 0

    for i in range(1, len(data)):
        a = data[i]
        j = i - 1
        while j >= 0 and a < data[j]:
            point_tri_insertion += 1
            data[j + 1] = data[j]
            j -= 1
        data[j + 1] = a
        point_tri_insertion += 3
    print("Tableau après " + str(data))
    print("Nombre de point : " + str(point_tri_insertion))

    if (databefore == data):
        print("ERREUR TRIAGE")
    else:
        print("TRIAGE OK")
    print("[========= ========= =========]")

    # ========= TRI A BULLE CLASSIQUE =========


def tri_bulle(data):
    databefore = data.copy()
    print(" ")
    print("[======= TRI À BULLE =======]")
    print("Tableau avant " + str(databefore))

    point_tri_bulle = 0
    n = len(data)
    swapped_elements = True
    while swapped_elements:
        swapped_elements = False
        for j in range(0, n - 1):
            if data[j] > data[j + 1]:
                point_tri_bulle += 1
                swapped_elements = True
                data[j], data[j + 1] = data[j + 1], data[j]
                point_tri_bulle += 3

    print("Tableau après " + str(data))
    print("Nombre de point : " + str(point_tri_bulle))

    if (databefore == data):
        print("ERREUR TRIAGE")
    else:
        print("TRIAGE OK")
    print("[========= ========= =========]")

    return data

    # t========= TRI A BULLE OPTI =========

def tri_bulle_opti(data):
    databefore = data.copy()
    print(" ")
    print("[======= TRI À BULLE OPTIMISÉ =======]")
    print("Tableau avant " + str(databefore))
    point_tri_bulle_opti = 0
    n = len(data)
    swapped_elements = True
    while swapped_elements:
        swapped_elements = False
        for j in range(0, n - 1):
            if data[j] > data[j + 1]:
                point_tri_bulle_opti += 1
                swapped_elements = True
                data[j], data[j + 1] = data[j + 1], data[j]
                point_tri_bulle_opti += 3

    print("Tableau après " + str(tablebulle))
    print("Nombre de point : " + str(point_tri_bulle_opti))
    # afficher un message d'erreur si le tableau trié est différent du tableau avant tri
    if databefore == data:
        print("ERREUR TRIAGE")
    else:
        print("TRIAGE OK")

    print("[========= ========= =========]")

    return data

# FIN DE L'ECRITURE DES FONCTIONS

if table_type == "1":
    print("\n OPTION : TABLEAU RANDOM \n")
    tableselection = table_random.copy()
    tableinsertion = table_random.copy()
    tablebulle = table_random.copy()
    tablebulleopti = table_random.copy()
elif table_type == "2":
    print("\n OPTION : MEILLEUR SCENARIO \n")
    tableselection = table_best_case.copy()
    tableinsertion = table_best_case.copy()
    tablebulle = table_best_case.copy()
    tablebulleopti = table_best_case.copy()
elif table_type == "3":
    print("\n OPTION : PIRE SCENARIO \n")
    tableselection = table_worst_case.copy()
    tableinsertion = table_worst_case.copy()
    tablebulle = table_worst_case.copy()
    tablebulleopti = table_worst_case.copy()
else:
    print("ERREUR")
    exit()


# SELECTION DU TYPE DE TRI
def execution():
    if case == "1":
        tri_selection(tableselection)
        print("TABLE SELECTION EXECUTED WITH CASE : " + str(case))
    elif case == "2":
        tri_insertion(tableinsertion)
        print("TABLE INSERTION EXECUTED WITH CASE : " + str(case))
    elif case == "3":
        tri_bulle(tablebulle)
        print("TABLE BUBBLE EXECUTED WITH CASE : " + str(case))
    elif case == "4":
        tri_bulle_opti(tablebulleopti)
        print("TABLE  EXECUTED WITH CASE : " + str(case))
    elif case == "0":
        tri_selection(tableselection)
        tri_insertion(tableinsertion)
        tri_bulle(tablebulle)
        tri_bulle_opti(tablebulleopti)
        print("ALL SCRIPTS EXECUTED WITH CASE : " + str(case))
    else:
        print("ERROR")

execution()

