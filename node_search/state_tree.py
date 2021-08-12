import networkx as nx
import matplotlib.pyplot as plt
import graph
import math
import threading, queue
import random
from time import time


class Node : 

    def __init__(self ,key): 
        self.key = key  
        self.child = [] 


def search_conexions(node,G):
    nodes_connected = []
    for edge in G.edges:
        if edge[0] == node:
            nodes_connected.append(edge[1])
        elif edge[1] == node:
            nodes_connected.append(edge[0])

    return nodes_connected



def printNodeLevelWise(root): 
    if root is None: 
        return 

    queue = [] 
    queue.append(root) 
  
    while(len(queue) >0): 
  
        n = len(queue) 
        while(n > 0) : 
  
            p = queue[0] 
            queue.pop(0) 
            print (p.key) 

            for index, value in enumerate(p.child): 
                queue.append(value) 
  
            n -= 1
        print()



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


def generate_tree(G,nodo_inicial):

    print("...arbol de estados generando")
    print("demora en minutos por mas cantidad de conexiones")


    
    path = []
    level = []

    root = Node(nodo_inicial)

    path.append(root)
    level.append(root)
    
    root_temp = root

    while len(path) != 0:

        if len(level) == 0:
            break

        ### Verfica conexiones de nodo actual ####
        
        list_conexions = search_conexions(level.pop().key,G)

        ### Verifica que existan conexiones ###

        if len(list_conexions) != 0:
            
            ### Si hay mas nodos se borran los nodos conectados que estan presentes en el camino y asi evitar bucles ###

            if len(path)-1 != 0:
                
                ### Evita que cuente el nodo actual y asi evite ciclo del mismo nodo ###
                
                for i in range(0,len(path)):  ### len(path)-1 antes
                    for nodo in list_conexions:
                        if nodo == path[i].key:
                            list_conexions.remove(nodo)          

            ### Si no hay nodos conectados para insertar ###

            if len(list_conexions) == 0:
                """
                for i in range(0,len(path)):
                    print("camino fuera bucle: ",path[i].key)
                print()
                """

                level.append(path.pop())
                
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
     
                for nodo in list_conexions:
                    root_temp.child.append(Node(nodo))
                
                path.append(root_temp.child[0])
                level.append(root_temp.child[0])

                root_temp = root_temp.child[0]

    return root


def busqueda_amplitud_arbol(G,num_nodes,position_node,nodo_inicial,nodo_objetivo):
    
    start_time = time()

    tree_root = generate_tree(G,nodo_inicial)
    camino_found = 0
    print("...buscando el mejor camino")
    root_tmp = tree_root

    print_queue = []

    queue = []
    camino = []
    queue.append([tree_root.key,camino,tree_root])
    print_queue.append([tree_root.key,camino])

    while True:
        #print("cola caminos: ",print_queue)

        if len(queue) == 0:
            camino_found= False
            break

        elif queue[0][0] == nodo_objetivo:
            queue[0][1].append(nodo_objetivo)
            camino_found = queue[0][1]
            break
        
        else:
            
            path = []
            if len(queue[0][1]) == 0:
                path.append(queue[0][0])

            else:
                path = queue[0][1].copy()
                path.append(queue[0][0])

            root_tmp = queue[0][2]

            queue.pop(0)
            print_queue.pop(0)
            
            for i in range(0,len(root_tmp.child)):
                queue.append([root_tmp.child[i].key,path,root_tmp.child[i]])
                print_queue.append([root_tmp.child[i].key,path])


    elapsed_time = time()- start_time
    print("Elapsed time for BA: %.10f seconds." % elapsed_time)
    print()


    if camino_found == False:
        print("No se encontro camino")
        print()

    else:
        print("Camino encontrado busqueda amplitud: ",camino_found)
        print()

        camino_edges = []
        j=0
        for i in range(0,len(camino_found)):
            j += 1
            edge_tmp = (camino_found[i],camino_found[j])
            camino_edges.append(edge_tmp)

            if j==len(camino_found)-1:
                break

        nx.draw_networkx_nodes(G,position_node)
        nx.draw_networkx_nodes(G,position_node,nodelist = camino_found,node_color="green")
        nx.draw_networkx_edges(G,position_node)
        nx.draw_networkx_edges(G,position_node,edgelist=camino_edges,edge_color="r")

        labels = {}
        for i in range(0,num_nodes):
            labels[i] = i

        nx.draw_networkx_labels(G,position_node,labels,font_size=12)

        plt.show()


def busqueda_amplitud_sin_arbol(G,num_nodes,position_node,nodo_inicial,nodo_objetivo):
    
    start_time = time()

    tree_root = nodo_inicial
    camino_found = 0
    print("...buscando el mejor camino")
    root_tmp = tree_root

    print_queue = []

    queue = []
    camino = []
    queue.append([tree_root,camino])
    print_queue.append([tree_root,camino])

    while True:
        #print("cola caminos: ",print_queue)

        if len(queue) == 0:
            camino_found= False
            break

        elif queue[0][0] == nodo_objetivo:
            queue[0][1].append(nodo_objetivo)
            camino_found = queue[0][1]
            break
        
        else:
            
            path = []
            if len(queue[0][1]) == 0:
                path.append(queue[0][0])

            else:
                path = queue[0][1].copy()
                path.append(queue[0][0])

            root_tmp = queue[0][0]
            list_children = search_conexions(root_tmp,G)

            for j in path:
                for i in list_children:
                    if i == j:
                        list_children.remove(i)

            queue.pop(0)
            print_queue.pop(0)
            
            for i in range(0,len(list_children)):
                queue.append([list_children[i],path])
                print_queue.append([list_children[i],path])


    elapsed_time = time()- start_time
    print("Elapsed time for BA: %.10f seconds." % elapsed_time)
    print()


    if camino_found == False:
        print("No se encontro camino")
        print()

    else:
        print("Camino encontrado busqueda amplitud: ",camino_found)
        print()

        camino_edges = []
        j=0
        for i in range(0,len(camino_found)):
            j += 1
            edge_tmp = (camino_found[i],camino_found[j])
            camino_edges.append(edge_tmp)

            if j==len(camino_found)-1:
                break

        nx.draw_networkx_nodes(G,position_node)
        nx.draw_networkx_nodes(G,position_node,nodelist = camino_found,node_color="green")
        nx.draw_networkx_edges(G,position_node)
        nx.draw_networkx_edges(G,position_node,edgelist=camino_edges,edge_color="r")

        labels = {}
        for i in range(0,num_nodes):
            labels[i] = i

        nx.draw_networkx_labels(G,position_node,labels,font_size=12)

        plt.show()


def get_key(val,dist_neighbors): 
    for key, value in dist_neighbors.items(): 
         if val == value: 
             return key 
    return "key doesn't exist"


def hill_climbing(Grafo,n_nodos,nodo_ini,nodo_objetivo):
    
    start_time = time()

    distancia_nodo_objetivo={}

    for i in range(0,n_nodos):
        if i != n_nodos:
            distancia_nodo_objetivo[i]=(round(math.sqrt(((Grafo.nodes[i]['pos'][1]-Grafo.nodes[nodo_objetivo]['pos'][1])**2)+((Grafo.nodes[nodo_objetivo]['pos'][0]-Grafo.nodes[i]['pos'][0])**2)),2))


    nodo_inicial = nodo_ini
    nodo_final = nodo_objetivo
    nodo_cam = Grafo.nodes[nodo_inicial]
    i = 0
    path = []
    path.append(nodo_inicial)
    while nodo_cam['value'] != nodo_final:
        dist_neighbors = {}
        menor = 0
        key = 0
        hijo = 0
        for edges in Grafo.edges([nodo_cam['value']]):
            hijo = edges[1]
            if (Grafo.nodes[hijo]['path'] != True):
                dist_neighbors[hijo]=distancia_nodo_objetivo[hijo]
                if (hijo == nodo_final or distancia_nodo_objetivo[hijo] == 0 ):
                    menor = distancia_nodo_objetivo[hijo]
                    break
                if menor == 0:
                    menor = distancia_nodo_objetivo[hijo]
                if distancia_nodo_objetivo[hijo] < menor and distancia_nodo_objetivo[hijo] != 0 and nodo_cam['path']!= True:
                    menor = distancia_nodo_objetivo[hijo]
        key = get_key(menor,dist_neighbors)
        if key == "key doesn't exist":
            print ("Camino no encontrado")
            path_find = False
            break
        else:
            path_find = True
        path.append(key)
        nodo_cam['path']=True
        nodo_cam = Grafo.nodes[key]
        Grafo.nodes[nodo_inicial]['path'] = True


    elapsed_time = time()- start_time
    print("Elapsed time for Hill-Climbing: %.10f seconds." % elapsed_time)
    print()

    Grafo.nodes[nodo_final]['path'] = True
    color_map = []
    for i in range (0,n_nodos):
        if Grafo.nodes[i]['path'] == True :
            color_map.append('red')
        else:
            color_map.append('green')    

    if path_find:
        print ("Camino encontrado hill-climbing: ",path)
        pos=nx.get_node_attributes(Grafo,'pos')
        nx.draw(Grafo,pos, node_color = color_map,with_labels=True)
        plt.show()

