import networkx as nx
import matplotlib.pyplot as plt
import math
import threading, queue
import random
import numpy as np


def generar_Tablero():

    Tablero = nx.Graph()
    x = 0

    for i in range (0,8):
        for j in range(0,8):
            if (i % 2 == 0 and j % 2 == 0):
                Tablero.add_node(x,pos=(i,j),value = x, state = "restringido", color = "sin color")
            elif (i % 2 != 0 and j % 2 != 0):
                Tablero.add_node(x,pos=(i,j),value = x, state = "restringido", color = "sin color")
            else:
                Tablero.add_node(x,pos=(i,j),value = x, state = "vacio", color = "sin color")
            x += 1


    for i in range(0,64):
        if (Tablero.nodes[i]['pos'][0] == 0 or Tablero.nodes[i]['pos'][0]== 2):
            if(Tablero.nodes[i]['pos'][1] % 2 != 0):
                Tablero.nodes[i]['state'] = "ocupado"
                Tablero.nodes[i]['color'] = "roja"
        elif (Tablero.nodes[i]['pos'][0] == 1):
            if(Tablero.nodes[i]['pos'][1] % 2 == 0):
                Tablero.nodes[i]['state'] = "ocupado"
                Tablero.nodes[i]['color'] = "roja"
        elif (Tablero.nodes[i]['pos'][0] == 5 or Tablero.nodes[i]['pos'][0] == 7):
            if(Tablero.nodes[i]['pos'][1] % 2 == 0):
                Tablero.nodes[i]['state'] = "ocupado"
                Tablero.nodes[i]['color'] = "negra"
        elif (Tablero.nodes[i]['pos'][0] == 6):
            if(Tablero.nodes[i]['pos'][1] % 2 != 0):
                Tablero.nodes[i]['state'] = "ocupado"
                Tablero.nodes[i]['color'] = "negra"

    return Tablero


def generar_posibles_fichas(Tablero,valor_ficha):
    posib_fichas = []
    color_ficha = ""
    color_ficha_opuesto = ""

    if valor_ficha == 1:
        color_ficha = "roja"
        color_ficha_opuesto = "negra"

        for i in range(0,64):
            if Tablero.nodes[i]['color'] == color_ficha:

                if i+7 < 64 and i+7 > -1:
                    if Tablero.nodes[i + 7]['state'] == "vacio" and Tablero.nodes[i]['state']!= "vacio":
                        posib_fichas.append([i, Tablero.nodes[i]['value'],Tablero.nodes[i + 7]['value'], 0 ])
                  
                    elif Tablero.nodes[i+ 7]['color'] == color_ficha_opuesto and Tablero.nodes[i]['state']!= "vacio":
                        if i+7*2 < 64 and i+7*2 > -1:
                            if Tablero.nodes[i+ 7*2]['state'] == "vacio" and Tablero.nodes[i]['state']!= "vacio":
                                posib_fichas.append([i, Tablero.nodes[i]['value'],Tablero.nodes[i+ 7*2]['value'], 7 ])


                if i+9 < 64 and i+9 > -1:
                    if Tablero.nodes[i + 9]['state'] == "vacio" and Tablero.nodes[i]['state']!= "vacio":
                        posib_fichas.append([i,Tablero.nodes[i]['value'], Tablero.nodes[i + 9]['value'], 0 ])

                    elif Tablero.nodes[i+ 9]['color'] == color_ficha_opuesto and Tablero.nodes[i]['state']!= "vacio":
                        if i+9*2 < 64 and i+9*2 > -1:
                            if Tablero.nodes[i+ 9*2]['state'] == "vacio" and Tablero.nodes[i]['state']!= "vacio":
                                posib_fichas.append([i, Tablero.nodes[i]['value'],Tablero.nodes[i+ 9*2]['value'], 9 ])

                                
                if i-7 < 64 and i-7 > -1:
                    if Tablero.nodes[i- 7]['state'] == "vacio" and Tablero.nodes[i]['state']!= "vacio":
                        posib_fichas.append([i, Tablero.nodes[i]['value'],Tablero.nodes[i- 7]['value'], 0] )

                    elif Tablero.nodes[i- 7]['color'] == color_ficha_opuesto and Tablero.nodes[i]['state']!= "vacio":
                        if i-7*2 < 64 and i-7*2 > -1:
                            if Tablero.nodes[i- 7*2]['state'] == "vacio" and Tablero.nodes[i]['state']!= "vacio":
                                posib_fichas.append([i, Tablero.nodes[i]['value'],Tablero.nodes[i- 7*2]['value'], -7 ])


                if i-9 < 64 and i-9 > -1:
                    if Tablero.nodes[i - 9]['state'] == "vacio" and Tablero.nodes[i]['state']!= "vacio":
                        posib_fichas.append([i,Tablero.nodes[i]['value'], Tablero.nodes[i- 9]['value'] , 0 ])

                    elif Tablero.nodes[i-9]['color'] == color_ficha_opuesto and Tablero.nodes[i]['state']!= "vacio":
                        if i-9*2 < 64 and i-9*2 > -1:
                            if Tablero.nodes[i- 9*2]['state'] == "vacio" and Tablero.nodes[i]['state']!= "vacio":
                                posib_fichas.append([i, Tablero.nodes[i]['value'],Tablero.nodes[i- 9*2]['value'], -9 ])
                

    else:
        color_ficha = "negra"
        color_ficha_opuesto = "roja"

        for i in range(63,-1,-1):
            if Tablero.nodes[i]['color'] == color_ficha:


                if i-7 < 64 and i-7 > -1:
                    if Tablero.nodes[i- 7]['state'] == "vacio" and Tablero.nodes[i]['state']!= "vacio":
                        posib_fichas.append([i, Tablero.nodes[i]['value'],Tablero.nodes[i- 7]['value'], 0] )

                    elif Tablero.nodes[i- 7]['color'] == color_ficha_opuesto and Tablero.nodes[i]['state']!= "vacio":
                        if i-7*2 < 64 and i-7*2 > -1:
                            if Tablero.nodes[i- 7*2]['state'] == "vacio" and Tablero.nodes[i]['state']!= "vacio":
                                posib_fichas.append([i, Tablero.nodes[i]['value'],Tablero.nodes[i- 7*2]['value'], -7 ])


                if i-9 < 64 and i-9 > -1:
                    if Tablero.nodes[i - 9]['state'] == "vacio" and Tablero.nodes[i]['state']!= "vacio":
                        posib_fichas.append([i,Tablero.nodes[i]['value'], Tablero.nodes[i- 9]['value'] , 0 ])

                    elif Tablero.nodes[i-9]['color'] == color_ficha_opuesto and Tablero.nodes[i]['state']!= "vacio":
                        if i-9*2 < 64 and i-9*2 > -1:
                            if Tablero.nodes[i- 9*2]['state'] == "vacio" and Tablero.nodes[i]['state']!= "vacio":
                                posib_fichas.append([i, Tablero.nodes[i]['value'],Tablero.nodes[i- 9*2]['value'], -9 ])

                
                
                if i+7 < 64 and i+7 > -1:
                    if Tablero.nodes[i + 7]['state'] == "vacio" and Tablero.nodes[i]['state']!= "vacio":
                        posib_fichas.append([i, Tablero.nodes[i]['value'],Tablero.nodes[i + 7]['value'], 0 ])

                    elif Tablero.nodes[i+ 7]['color'] == color_ficha_opuesto and Tablero.nodes[i]['state']!= "vacio":
                        if i+7*2 < 64 and i+7*2 > -1:
                            if Tablero.nodes[i+ 7*2]['state'] == "vacio" and Tablero.nodes[i]['state']!= "vacio":
                                posib_fichas.append([i, Tablero.nodes[i]['value'],Tablero.nodes[i+ 7*2]['value'], 7 ])


                if i+9 < 64 and i+9 > -1:
                    if Tablero.nodes[i + 9]['state'] == "vacio" and Tablero.nodes[i]['state']!= "vacio":
                        posib_fichas.append([i,Tablero.nodes[i]['value'], Tablero.nodes[i + 9]['value'], 0 ])

                    elif Tablero.nodes[i+ 9]['color'] == color_ficha_opuesto and Tablero.nodes[i]['state']!= "vacio":
                        if i+9*2 < 64 and i+9*2 > -1:
                            if Tablero.nodes[i+ 9*2]['state'] == "vacio" and Tablero.nodes[i]['state']!= "vacio":
                                posib_fichas.append([i, Tablero.nodes[i]['value'],Tablero.nodes[i+ 9*2]['value'], 9 ])
                

    #print("posF: ",len(posib_fichas))
    return posib_fichas


def printGrafo(Tablero):
    color_map = []

    for i in range (0,64):
        if Tablero.nodes[i]['state'] == "restringido" :
                    color_map.append('blue')
        elif Tablero.nodes[i]['color'] == "roja" :
            color_map.append('red')
        else: 
            if Tablero.nodes[i]['color'] == "negra" :
                color_map.append('gray')
            else:
                color_map.append('yellow')

    labels = {}
    for i in range(0,64):
        labels[i] = Tablero.nodes[i]['value']

    pos=nx.get_node_attributes(Tablero,'pos')
    nx.draw_networkx_nodes(Tablero,pos,node_color = color_map)

    nx.draw_networkx_labels(Tablero,pos,labels,font_size=12)
 
    plt.show()


def intercambiar_nodos(Tablero,nodo1,nodo2,nodo_posible_medio):
    
    posicion_change = []

    for i in range(0,64):
        if Tablero.nodes[i]['value'] == nodo1:
            posicion_change.append(i)
        elif Tablero.nodes[i]['value'] == nodo2:
            posicion_change.append(i)

    #print(posicion_change)

    node_temp = []

    node_temp.append(Tablero.nodes[posicion_change[0]]['value'])
    node_temp.append(Tablero.nodes[posicion_change[0]]['color'])
        
    Tablero.nodes[posicion_change[0]]['value'] = Tablero.nodes[posicion_change[1]]['value']
    Tablero.nodes[posicion_change[0]]['color'] = Tablero.nodes[posicion_change[1]]['color']

    Tablero.nodes[posicion_change[1]]['value'] = node_temp[0]
    Tablero.nodes[posicion_change[1]]['color'] = node_temp[1]

    guarda_estado = Tablero.nodes[posicion_change[0]]['state']
    Tablero.nodes[posicion_change[0]]['state'] = Tablero.nodes[posicion_change[1]]['state']
    Tablero.nodes[posicion_change[1]]['state'] = guarda_estado

    if len(nodo_posible_medio) > 0:
        #print("nodo 1: ", Tablero.nodes[posicion_change[0]])
        #print("nodo 2: ", Tablero.nodes[posicion_change[1]])
        #print("nodo en medio: ", nodo_posible_medio[0]," ",nodo_posible_medio[1]," ",nodo_posible_medio[2]," ",nodo_posible_medio[3], "nodo posible: ",nodo_posible_medio)
        #print("nodo comido")

        color_ficha_comida = Tablero.nodes[nodo_posible_medio[0] + nodo_posible_medio[3]]['color']
        

        Tablero.nodes[nodo_posible_medio[0] + nodo_posible_medio[3]]['color'] = "yellow"
        Tablero.nodes[nodo_posible_medio[0] + nodo_posible_medio[3]]['state'] = "vacio"


def contador_fichas_Tablero(Tablero):
    contador_fichas_negras = 0
    contador_fichas_rojas = 0

    for i in range(0,64):
        if Tablero.nodes[i]['color'] == "negra":
            contador_fichas_negras += 1
        elif Tablero.nodes[i]['color'] == "roja":
            contador_fichas_rojas += 1
            
    contador_ficha = []
    contador_ficha.append([contador_fichas_negras,contador_fichas_rojas])

    return contador_ficha


def generar_posibles_tablero(Tablero_inicial,lista_jugadas,color_ficha):
    posibles_tab = []

    for jugada in lista_jugadas:
        ficha_posible_medio = []
        tmp_tab = Tablero_inicial.copy()
        if jugada[3] != 0:
            #print("tablero que come")
            ficha_posible_medio = jugada
        intercambiar_nodos(tmp_tab,jugada[1],jugada[2],ficha_posible_medio)
        cant_fichas = contador_fichas_Tablero(tmp_tab)
        valor_resta = 0
        if color_ficha == 0:
            valor_resta = cant_fichas[0][0] - cant_fichas[0][1]
        else:
            valor_resta = cant_fichas[0][1] - cant_fichas[0][0]
        posibles_tab.append([tmp_tab, jugada, valor_resta])
    return posibles_tab


class Node : 

    def __init__(self ,key): 
        self.key = key  
        self.child = [] 


def buscar_nodo(camino,raiz):

    root_temp = raiz

    if len(camino) == 1:
        return raiz

    i=1
    while i < len(camino):   
        e=0
        while e < len(root_temp.child):
            if camino[i] == root_temp.child[e]:
                root_temp = root_temp.child[e]
                
            e +=1
        
        i += 1

    return root_temp


def printNodeLevelWise(root): 
    print("print arbol")
    if root is None: 
        return 

    cont = 0
    queue = [] 
    queue.append(root) 
  
    while(len(queue) >0): 
  
        n = len(queue) 
        while(n > 0) : 
  
            p = queue[0] 
            queue.pop(0)
            print (cont,"-> ",p.key)
            #printGrafo(p.key[0])
            cont += 1

            for index, value in enumerate(p.child): 
                queue.append(value) 
  
            n -= 1
        print()


def minmax(Tablero, profundidad,ismax):
    tab_inicial = Tablero.copy()
    nodo_posible = []
    number = contador_fichas_Tablero(tab_inicial)
    if profundidad == 0:
        return contador_fichas_Tablero(tab_inicial)[0][0]- contador_fichas_Tablero(tab_inicial)[0][1] 
    if ismax:
        best = -1000
        rojas = 1
        fichas = []
        r_posib_fichas = generar_posibles_fichas(tab_inicial,rojas)
        fichas = r_posib_fichas
        for i in r_posib_fichas:
            if i[3] != 0:
                nodo_posible = i
            intercambiar_nodos(tab_inicial,i[1],i[2],nodo_posible)
            best = max( best, minmax(tab_inicial, profundidad - 1, not(ismax) ) )
            intercambiar_nodos(tab_inicial,i[2],i[1],nodo_posible)  
        return best
                
    else :
        negras = 0
        n_posib_fichas = generar_posibles_fichas(tab_inicial,negras)
        best = 1000
        for i in n_posib_fichas:
            if i[3] != 0:
                nodo_posible = i
            intercambiar_nodos(tab_inicial,i[1],i[2],nodo_posible)
            best = min( best, minmax(tab_inicial, profundidad - 1, not(ismax) ) )
            intercambiar_nodos(tab_inicial,i[2],i[1],nodo_posible)
        return best


def mejor_jugada (Tablero, maquina,profundidad):
    n_posib_fichas = generar_posibles_fichas(Tablero,maquina)
    best_value = -1000
    best_move = []
    nodo_posible =[]
    for i in n_posib_fichas:
        if i[3]!= 0:
            nodo_posible = i

        intercambiar_nodos(Tablero,i[1],i[2],nodo_posible)
        best_move_value = minmax(Tablero,profundidad,True)
        intercambiar_nodos(Tablero,i[2],i[1],nodo_posible)
        if(best_move_value > best_value):
            best_move = i
            best_value = best_move_value
    
    print("mejor move: ",best_move)
    return best_move


def generate_tree(Tablero,ficha_color,profundidad):

    print("...arbol de estados generando")
    print("...demora en minutos")


    path = []
    level = []

    tab_inicial = Tablero.copy()
    root = Node([tab_inicial, 0,0, 0])

    path.append(root)
    level.append(root)
    
    root_temp = root
    profundidad_alcanzada = False


    while len(path) != 0:
        #print("aun en bucle")
        list_tableros = []
        posib_fichas = []

        if len(level) == 0:

            level.append(path.pop())
            list_tableros.append(1)
            #break
        
        else:
            tablero_borr = level.pop().key
            color_ficha = ficha_color
            if ficha_color==0:  
                #print("juega negra")         
                posib_fichas = generar_posibles_fichas(tablero_borr[0],0)
                ficha_color = 1
            else:
                #print("juega roja")
                posib_fichas = generar_posibles_fichas(tablero_borr[0],1)
                ficha_color = 0

            list_tableros = generar_posibles_tablero(tablero_borr[0],posib_fichas,color_ficha)
            
        
        if len(list_tableros) != 0:

            if profundidad_alcanzada == True:
            
                list_tableros.pop()
                profundidad_alcanzada = False
                #print("posib sub")
                #level.append(path.pop())
                
                ### retorna nodo padre del nodo actual ###
                
                root_temp = buscar_nodo(path,root)
                
                subida = False
    
                while True:
                    """
                    print("root: ",root_temp.key)
                    for i in path:
                        print("camino element: ",i.key)
                    print()"""

                    for i in range(0,len(root_temp.child)):
                        ### Evalua que el nodo padre solo tenga un hijo para buscar padre de ese nodo ###

                        if i+1 == len(root_temp.child):
                            subida = True
                            break     
                        
                        ### Evalua que el nodo padre tenga mas hijos para trabajar con nodo hijo siguiente ###
                        

                        elif root_temp.child[i] == level[0]:

                            path.append(root_temp.child[i+1])
                            level.pop()
                            level.append(root_temp.child[i+1])
                            root_temp = root_temp.child[i+1]
                            subida = False
                            break

                    ### Se busca un nuevo nodo padre ###

                    if subida == True:
                        #print("subida arbol")
                        level.pop()
                        level.append(path.pop())

                        if len(path) == 0:
                            subida = False
                            break         

                        root_temp = buscar_nodo(path,root)

                    ### Ya se trabaja con el nodo con el flujo normal ###

                    elif subida == False:
                        break
 
            ### Si hay nodos conectados para insertar ###

            else:
                #print("creo hijos  prof padre: ",root_temp.key[2])

                if root_temp.key[3]+1 <= profundidad:
                    #printGrafo(root_temp.key[0])
                    for nodo in list_tableros:
                        nodo.append(root_temp.key[3] + 1)
                        #print("nodo hijo: ",nodo)
                        root_temp.child.append(Node(nodo))
                        #printGrafo(nodo[0])
                    
                    path.append(root_temp.child[0])
                    level.append(root_temp.child[0])

                    root_temp = root_temp.child[0]
                
                else:
                    profundidad_alcanzada = True


    return root


def  juego_yo(Tablero,ficha):

    fichas = []

    print("Posibles movimientos: ")
    if ficha == 0:
        
        print()
        print("Fichas negras")
        print()
        fichas = generar_posibles_fichas(Tablero,0)

    else:

        print()
        print("Fichas rojas")
        print()
        fichas = generar_posibles_fichas(Tablero,1)

    for i in fichas:
        print("ficha posible escoger: ",i[1], " ficha a donde mover: ",i[2])
    intercambio_ficha = False
    ficha_escogida = 0
    ficha_change = 0
    printGrafo(Tablero)
    ficha_posible_medio = []

    while(True):
        ficha_escogida = int(input("Ficha escogida: "))
        ficha_change = int(input("Ficha a donde mover: "))
        for i in fichas:
            if i[1] == ficha_escogida and i[2] == ficha_change:
                intercambio_ficha = True
                if i[3] != 0:
                    ficha_posible_medio = i

        if intercambio_ficha:
            break
        else:
            print("No puede mover su ficha asi")

    if intercambio_ficha:
        intercambiar_nodos(Tablero,ficha_escogida,ficha_change,ficha_posible_medio)





if __name__ == "__main__":

    while(True):
        print("\tJUEGO DE LAS DAMAS")
        print()
        print("+ Jugar [1]")
        print("+ probando arbol [2]")
        print("+ Salir [0]")
        print()
        opcion = int(input("Opcion: "))

        if opcion == 0:
            break

        elif opcion == 2:
            Tablero = generar_Tablero()
            #generate tree paremtros: tablero inicial, ficha con que comienza a jugar 0 negra 1 roja, nivel de profundidad de arbol
            profundidadTree  = int(input("Profundidad de arbol: "))
            root_tree = generate_tree(Tablero,0,profundidadTree)
            printNodeLevelWise(root_tree)

        elif opcion == 1:
            Tablero = generar_Tablero()
            
            print("\tCOLOR DE FICHA")
            print()
            print("+ negra [1]")
            print("+ roja  [0]")
            print("+ Salir [2]")
            print()
            opcion_sub_sub = int(input("Opcion: "))

            if opcion_sub_sub == 2:
                break

            elif opcion_sub_sub == 0:
                profundidad = int(input("Profundidad: "))
                empieza = int(input("Quien empieza?  Humano[0]  Maquina[1]: "))

                while(True):
                    if empieza == 1:
                        printGrafo(Tablero)
                        print("MAQUINA")
                        jugada = mejor_jugada(Tablero,0,profundidad)
                        ficha_posible_medio = []
                        if jugada[3] != 0:
                            ficha_posible_medio = jugada
                        intercambiar_nodos(Tablero,jugada[1],jugada[2],ficha_posible_medio)

                        print("HUMANO")
                        juego_yo(Tablero,1)
                        
                        print("Quieres seguir? Si [1]  No[0]")
                        opcion = int(input("Opcion: "))

                        if opcion == 0:
                            break
                    
                    else:
                        printGrafo(Tablero)
                        print("HUMANO")
                        juego_yo(Tablero,1)
                        print("MAQUINA")
                        jugada = mejor_jugada(Tablero,0,profundidad)
                        ficha_posible_medio = []
                        if jugada[3] != 0:
                            ficha_posible_medio = jugada
                        intercambiar_nodos(Tablero,jugada[1],jugada[2],ficha_posible_medio)
                        printGrafo(Tablero)

                        print("Quieres seguir? Si [1]  No[0]")
                        opcion = int(input("Opcion: "))

                        if opcion == 0:
                            break                       


            elif opcion_sub_sub == 1:
                profundidad = int(input("Profundidad: "))
                empieza = int(input("Quien empieza?  Humano[0]  Maquina[1]: "))

                while(True):
                    if empieza == 1:
                        printGrafo(Tablero)
                        print("MAQUINA")
                        jugada = mejor_jugada(Tablero,1,profundidad)
                        ficha_posible_medio = []
                        if jugada[3] != 0:
                            ficha_posible_medio = jugada
                        intercambiar_nodos(Tablero,jugada[1],jugada[2],ficha_posible_medio)

                        print("HUMANO")
                        juego_yo(Tablero,0)
                        

                        print("Quieres seguir? Si [1]  No[0]")
                        opcion = int(input("Opcion: "))

                        if opcion == 0:
                            break
                    
                    else:
                        printGrafo(Tablero)
                        print("HUMANO")
                        juego_yo(Tablero,0)
                        print("MAQUINA")
                        jugada = mejor_jugada(Tablero,1,profundidad)
                        ficha_posible_medio = []
                        if jugada[3] != 0:
                            ficha_posible_medio = jugada
                        intercambiar_nodos(Tablero,jugada[1],jugada[2],ficha_posible_medio)
                        printGrafo(Tablero)

                        print("Quieres seguir? Si [1]  No[0]")
                        opcion = int(input("Opcion: "))

                        if opcion == 0:
                            break