class Nodo:
    def __init__(self, data:any):
        self.data = data

        self.left_child = None
        self.right_child = None

class BinarySearchTree:
    def __init__(self):
        self.root = None

    def insert(self, data:any):
        nuevo_nodo = Nodo(data)

        if self.isEmpty():
            self.root = nuevo_nodo
            return

        nodo_actual:Nodo = self.root

        while True:
            if data < nodo_actual.data:
                if nodo_actual.left_child:
                    nodo_actual = nodo_actual.left_child
                    continue

                else:
                    nodo_actual.left_child = nuevo_nodo
                    print(f"¡Insertado {data} en el BST!")
                    return
                
            elif data > nodo_actual.data:
                if nodo_actual.right_child:
                    nodo_actual = nodo_actual.right_child
                    continue

                else:
                    nodo_actual.right_child = nuevo_nodo
                    print(f"¡Insertado {data} en el BST!")
                    return
                
            else:
                print(f"¡{data} es un valor repetido!")
                return

    def search(self, data:any):
        if self.isEmpty():
            print("¡El BST está vacio!")
            return None

        nodo_actual:Nodo = self.root

        while nodo_actual:
            if data == nodo_actual.data:
                print(f"¡{data} encontrado!")
                return nodo_actual
                
            elif data < nodo_actual.data:
                nodo_actual = nodo_actual.right_child
                continue
                
            elif data > nodo_actual.data:
                nodo_actual = nodo_actual.right_child

        print(f"¡No se encontro {data}!")
        return None

    def in_order(self, nodo_actual = None):
        if nodo_actual is None:
            nodo_actual = self.root

        if nodo_actual.left_child:
            self.in_order(nodo_actual.left_child)

        print(nodo_actual.data)

        if nodo_actual.right_child:
            self.in_order(nodo_actual.right_child)
        
    def find_min(self):
        if self.isEmpty():
            print("¡El BST está vacio!")
            return None

        nodo_minimo:Nodo = self.root

        while True:
            if nodo_minimo.left_child:
                nodo_minimo = nodo_minimo.left_child

            else:
                print(f"¡{nodo_minimo.data} es el minimo!")
                return nodo_minimo

    def find_max(self):
        if self.isEmpty():
            print("¡El BST está vacio!")
            return None
        
        nodo_maximo:Nodo = self.root
    
        while True:
            if nodo_maximo.right_child:
                nodo_maximo = nodo_maximo.right_child
    
            else:
                print(f"¡{nodo_maximo.data} es el maximo!")
                return nodo_maximo

    def remove(self, wanted_data):
        if self.isEmpty():
            return
        
        wanted_node = self.search(wanted_data)

        if not wanted_node:
            return

        self.replaceNode(wanted_node)

    def replaceNode(self, wanted_node:Nodo):
        parent_node = self.findParent(wanted_node)
        children_count = self.getChildrenCount(wanted_node)

        match children_count:
            case 0:
                if not parent_node:
                    self.root = None

                else:
                    if parent_node.left_child == wanted_node:
                        parent_node.left_child = None

                    else:
                        parent_node.right_child = None

            case 1:
                next_node = None
                if wanted_node.left_child:
                    next_node = wanted_node.left_child

                else:
                    next_node = wanted_node.right_child

                if parent_node:
                    if parent_node.left_child == wanted_node:
                        parent_node.left_child = next_node

                    else:
                        parent_node.right_child = next_node

            case 2:
                if not parent_node:
                    pass

                else:
                    if parent_node.left_child == wanted_node:
                        next_node:Nodo = wanted_node.right_child
                        next_node.left_child = wanted_node.left_child

                        parent_node.left_child = next_node

                    else:
                        next_node = wanted_node.left_child
                        next_node.right_child = wanted_node.right_child
                        
                        parent_node.right_child = next_node

    def findParent(self, wanted_node:Nodo):
        current_node:Nodo = self.root
        parent_node = None

        while True:
            if wanted_node == current_node:
                return parent_node

            parent_node = current_node

            if wanted_node.data < current_node.data:
                current_node = current_node.left_child

            elif wanted_node > current_node.data:
                current_node = current_node.right_child

    def getChildrenCount(self, node:Nodo):
        if node.left_child and node.right_child:
            children_count = 2

        elif node.left_child or node.right_child:
            children_count = 1

        else:
            children_count = 0

        return children_count

    def isEmpty(self):
        return self.root == None

BNS = BinarySearchTree()

BNS.search(12)
print()

BNS.insert(10)
BNS.insert(9)
BNS.insert(11)
BNS.insert(12)
BNS.insert(11)
BNS.insert(7)
print()

BNS.search(12)
BNS.search(13)
print()

BNS.in_order()
print()

BNS.find_min()
BNS.find_max()
print()