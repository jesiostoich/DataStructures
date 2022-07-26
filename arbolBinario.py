from dataclasses import dataclass
from typing import Any, Union


### Para saber MAXIMO y MINIMO nodo. ---> Esta funciones las ponemos fuera de la
###                                       clase porque pueden ser usadas tambien
###                                       para otras estructuras

def max_(node):                  
    if node is not None:
        while node.right is not None:
            node=node.right
    return node

def min_(node):
    if node is not None:
        while node.left is not None:
            node=node.left
    return node
##########################################

class SearchBinaryTree():

    @dataclass
    class _Node:
        key: any  #CLAVE. Es comparable solamente
        value: any   #VALOR
        parent: Union['_Node', '_Root']= None
        left: '_Node'= None
        right: '_Node'= None

    @dataclass
    class _Root:
        left: '_Node'= None
        right: '_Node'= None
        parent: '_Node'= None

    __slots__=['_root', '_len']

    def __init__(self, iterable=None): #Debe recibir una tupla
        self._root= self._Root()
        self._len= 0
        if iterable is not None:
            for key, value in iterable:
                self.insert(key, value)


    def isEmpty(self):
        return self._len==0

    def insert(self, key, value=None):  #RECURSIVE
        def do_insert(node, parent):
            if node is None:
                node=SearchBinaryTree._Node(key, value, parent)
                self._len+=1
            elif key<node.key:
                node.left= do_insert(node.left, node)
            elif key>node.key:
                node.right= do_insert(node.right, node)
            else:
                node.value=value
            return node
        self._root.left= do_insert(self._root.left, self._root)

    def find(self, key):
        def do_find(node, key):
            if node is None:
                return False
            elif key<node.key:
                do_find(node.left, key)
            elif key>node.key:
                do_find(node.right, key)
            elif node.key==key:
                coord=SearchBinaryTree._Coordinate(node)
                return coord
            return node
            
        return do_find(self._root.left, key)

    def clear(self):
        self._root.left=None
        self._len=0

    def maximum(self):
        return SearchBinaryTree._Coordinate(max_(self._root.left))

    def minimum(self):
        return SearchBinaryTree._Coordinate(min_(self._root))


     def erase(self, key):
         def search_and_erase(node):
             if node is None:
                 return False
             elif key==node.key:
                 coord= SearchBinaryTree._Coordinate(node)
                 return coord
             elif key<node.key:
                 search_and_erase(node.left)
                 else:  #key>node.key
                     searcha_and_erase(node.right)


        def extractMax(




































    

    def erase(self, key):
         def do_erase(node):
            if node is None:
                result = False
            elif key < node.key:
                result, node.left = do_erase(node.left)
            elif key > node.key:
                result, node.right= do_erase(node.right)
            else:  # key == node.key
                result = True  
                node = eraseNode(node)  #Le pasa el NODO a ELIMINAR a esta funcion para borrarlo
            return result, node

        def eraseNode(node):
            parent=node.parent
                        if node.left is None:
                node = node.right
            elif node.right is None:
                node = node.left
            else:
                node = extract_maximum_from(node)
            assign_parent(node, parent)
            self._len -= 1
            return node


        def extract_maximum_from(root):  #Toma el mas grande de la IZQUIERDA
            prev = None
            maximum = root.left
            while maximum.right is not None:
                prev = maximum
                maximum = maximum.right

            assign_parent(maximum, root.parent)
            
            maximum.right = root.right
            assign_parent(maximum.right, maximum)

            if prev is not None:
                prev.right = maximum.left
                assign_parent(prev.right, prev)
                maximum.left = root.left
                assign_parent(maximum.left, maximum)
            
            return maximum


        def assign_parent(node, parent):
            if node is not None:
                node.parent = parent

        result, self._root.left =do_erase(self._root.left) #Do_erase retorna 2 COSAS      
        return result, coord


    def begin(self):
        return SearchBinaryTree._Coordinate(min_(self._root))

    def end(self):
        return SearchBinaryTree._Coordinate(self._root)

    def copy(self):
        
                    
                
                

        
        
        
                          
        
                
                
        
