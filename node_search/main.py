import random
import math 
import networkx as nx
import matplotlib.pyplot as plt
import math
import threading, queue
import graph 
import state_tree as st_tree
import samplePoints as spoint


while True:

    print()
    print("\tALGORITMOS DE BUSQUEDA")
    print()
    print("+ Generador de grafo 01 (1)")
    print("+ Generador de grafo 02 (2)")
    print("+ Salir (3)")
    print()

    opcion_generar_grafo = int(input("Opcion: "))

    if(opcion_generar_grafo == 1):

        """Iniciando programa"""

        G = nx.Graph()
        num_nodes = int(input("Number of nodes: "))
        num_conexions = int(input("Number conexions: "))


        """ Generando nodos aleatorios que no repiten posicion """

        G.add_nodes_from(range(0,num_nodes))

        for i in range (0,num_nodes):
            G.add_node(i,pos=(0,0),value = i, n_edges = 0, path = False)


        pos_good = spoint.get_good_points(num_nodes,4)

        pos = dict()
        i=0
        while len(pos) < num_nodes:
            xpos = pos_good[i][0] #random.randint(0,300)
            ypos = pos_good[i][1] #random.randint(0,300)
            
            if (xpos,ypos) not in pos.values():
                pos[i] = (xpos,ypos)
                i+=1


        for i in range(0,len(G.nodes)):
            for key in pos:
                if G.nodes[i]['value'] == key:
                    G.nodes[i]['pos'] = pos[key] 
            

        position_node =nx.get_node_attributes(G,'pos')

        """ Conectando nodos a nodos mas cercanos """

        list_node_start = [node for node in pos]
        list_points = [point for point in pos.values()]


        for i in range(0,len(list_node_start)):
            list_node_edges = graph.close_nodes_points(list_points[i],list_points)

            lista_node_end = graph.busca_nodos(list_node_edges,pos)

            """ revisar nodos con muchas conexiones y cero conexiones"""
            lista_node_end = graph.validar_conexion(list_node_start[i],lista_node_end,num_conexions,G)

            #evaluar para no hacer doble enlace

            for j in range(0,len(lista_node_end)):
                G.add_edge(list_node_start[i],lista_node_end[j])


        edges_reverse = []

        for edge in G.edges:
            edges_reverse.append((edge[1],edge[0]))

        for edge in G.edges:
            for j in range(0,len(edges_reverse)):
                if edge == edges_reverse[j]:
                    G.remove_edge(edges_reverse[j])



        nx.draw_networkx_nodes(G,position_node)
        nx.draw_networkx_edges(G,position_node)

        labels = {}
        for i in range(0,num_nodes):
            labels[i] = i

        nx.draw_networkx_labels(G,position_node,labels,font_size=12)

        plt.show()

        """ Busquedas"""
        print()
        print("\tBusquedas")
        print()
        nodo_inicio = int(input("nodo inicial: "))
        nodo_objetivo = int(input("nodo objetivo: "))

        opcion_arbol = 0
        while(opcion_arbol != 1 and opcion_arbol!=2):
            print()
            print("+ Busqueda amplitud sin arbol  [1]")
            print(" (se recorre el grafo como arbol a traves de una cola - Rapido, no contruye todo el arbol) ")
            print()
            print("+ Busqueda amplitud con arbol  [2]")
            print(" (se construye todo el arbol de estados y luego recorrer con una cola - Lento , construye arbol ,con varias conexiones)")
            print()
            opcion_arbol = int(input("Opcion: "))

        if(opcion_arbol == 1):
            st_tree.busqueda_amplitud_sin_arbol(G,num_nodes,position_node,nodo_inicio,nodo_objetivo)

        elif(opcion_arbol == 2):
            st_tree.busqueda_amplitud_arbol(G,num_nodes,position_node,nodo_inicio,nodo_objetivo)
        
        st_tree.hill_climbing(G,num_nodes,nodo_inicio,nodo_objetivo)
        

    elif(opcion_generar_grafo == 2):

        Grafo = nx.Graph()
        print("Ingrese el numero de nodos: ")
        n_nodos=int(input())
        print("\n Ingrese el numero de conexiones: ")
        n_conexiones=int(input())

        lengthss={}
        path_find = False
        distancia_nodo_objetivo={}
        for i in range (0,n_nodos):
            Grafo.add_node(i,pos=(random.randint(0,100),random.randint(0,100)),value = i, n_edges = 0, path = False)
            
        for i in range (0, n_nodos):
            for j in range(0, n_nodos):
                if i != j:
                    lengthss[j]=(round(math.sqrt(((Grafo.nodes[i]['pos'][1]-Grafo.nodes[j]['pos'][1])**2)+((Grafo.nodes[j]['pos'][0]-Grafo.nodes[i]['pos'][0])**2)),2))
                length_sort={k: v for k, v in sorted(lengthss.items(), key=lambda item: item[1])}
            for h in range(0, n_conexiones):
                for g in list(length_sort):
                    if Grafo.nodes[i]['n_edges'] < n_conexiones and Grafo.nodes[next(iter(length_sort))]['n_edges'] < n_conexiones :
                        Grafo.add_edge(i,next(iter(length_sort)))
                        Grafo.nodes[i]['n_edges'] +=1
                        Grafo.nodes[next(iter(length_sort))]['n_edges'] +=1
                    length_sort.pop(list(length_sort.keys())[0])
            lengthss = {}

        pos=nx.get_node_attributes(Grafo,'pos')
        nx.draw(Grafo,pos,with_labels=True)
        plt.show()


        """ Busquedas"""
        print()
        print("\tBusquedas")
        print()
        nodo_inicio = int(input("nodo inicial: "))
        nodo_objetivo = int(input("nodo objetivo: "))


        opcion_arbol = 0
        while(opcion_arbol != 1 and opcion_arbol!=2):
            print()
            print("+ Busqueda amplitud sin arbol  [1]")
            print(" (se recorre el grafo como arbol a traves de una cola - Rapido, no contruye todo el arbol) ")
            print()
            print("+ Busqueda amplitud con arbol  [2]")
            print(" (se construye todo el arbol de estados y luego recorrer con una cola - Lento , construye arbol ,con varias conexiones)")
            print()
            opcion_arbol = int(input("Opcion: "))

        if(opcion_arbol == 1):
            st_tree.busqueda_amplitud_sin_arbol(Grafo,n_nodos,pos,nodo_inicio,nodo_objetivo)
        elif(opcion_arbol == 2):
            st_tree.busqueda_amplitud_arbol(Grafo,n_nodos,pos,nodo_inicio,nodo_objetivo)
        
        st_tree.hill_climbing(Grafo,n_nodos,nodo_inicio,nodo_objetivo)


    elif(opcion_generar_grafo == 3):
        break










