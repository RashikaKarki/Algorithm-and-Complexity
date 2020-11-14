class BinarySearchTree:

    def __init__(self):
        self.root = None
        self.sizes = 0
    
    class Node:
        def __init__(self,key,value):
            self.leftnode = None 
            self.rightnode = None
            self.key = key
            self.value = value

    # Add a node to the BST
    def add(self, key, value):
        if self.root is None:
            self.root = self.Node(key,value)
        else:
            p = self.root
            while True:
                if(key<p.key):

                    if(p.leftnode is not None):
                        p = p.leftnode
                    else:
                        p.leftnode = self.Node(key,value)
                        break
                else:
                    if(p.rightnode is not None):

                        p = p.rightnode
                    else:
                        p.rightnode = self.Node(key,value)
                        break
        self.sizes += 1

    # Return the number of nodes in the BST
    def size(self):
        return self.sizes

    # Perform inorder traversal. Must return a list of keys visited in inorder way, e.g. [1, 2, 3, 4].
    def inorder_walk(self):
        result = []
        self.inorder(result)
        return result

    def inorder_walk(self):
        result = []
        self._inorder(self.root,result)
        return result

    def _inorder(self,p,result):
        if(p is not None):
            self._inorder(p.leftnode,result)
            result.append(p.key)
            self._inorder(p.rightnode,result)
        return result

    # Perform postorder traversal. Must return a list of keys visited in inorder way, e.g. [1, 4, 3, 2].
    def postorder_walk(self):
        result = []
        p = self.root
        self.postorder(p, result)
        return result

    def postorder(self,p,result):
        if p is not None:
            self.postorder(p.leftnode,result)
            self.postorder(p.rightnode,result)
            result.append(p.key)
        return result

    # Perform preorder traversal. Must return a list of keys visited in inorder way, e.g. [2, 1, 3, 4].
    def preorder_walk(self):
        result = []
        if self.root is None: 
            return result
        lists = []
        p = self.root
        while True:
            while p is not None:
                lists.append(p)
                result.append(p.key)
                p = p.leftnode
            p = lists.pop()            
            p = p.rightnode
            if(len(lists) == 0 and p is None): 
                break
        return result

    # Search the BST for the given key. Return False if the key is not found.
    def search(self, key):
        p = self.root
        while p is not None:
            if (key == p.key):
                return p.value
            elif(key<p.key):
                p = p.leftnode
            else:
                p = p.rightnode  
        return False 

    # Remove a key from the BST. Return False if the key is not present in the BST.
    def remove(self,key, p = None):
        if p == None:
            p = self.root
        else:
            p = p
        if p is None:
            return False
        if not p:
            return p
        if p.key > key: 
            p.leftnode = self.remove(key, p.leftnode)
        elif p.key < key: 
            p.rightnode= self.remove(key, p.rightnode)
        else: 
            if not p.rightnode:
                return p.leftnode	
            if not p.leftnode:
                return p.rightnode
            temp_val = p.rightnode
            mini_val = temp_val.key
            while temp_val.leftnode:
                temp_val = temp_val.leftnode
                mini_val = temp_val.key
            p.rightnode = self.remove(p.key,p.rightnode)
        return p

    # Find the smallest key and return the corresponding key-value pair/tuple, i.e. (key, value)
    def smallest(self):
        p = self.root
        while(p.leftnode is not None):
            p = p.leftnode
        return(p.key,p.value)


    # Find the largest key and return the corresponding key-value pair/tuple, i.e. (key, value)
    def largest(self):
        p = self.root
        while(p.rightnode is not None):
            p = p.rightnode
        return(p.key,p.value)