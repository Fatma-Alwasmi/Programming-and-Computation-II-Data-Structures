# HW4
# REMINDER: The work in this assignment must be your own original work and must be completed alone.
# Don't forget to list any authorized forms of collaboration using a Collaboration Statement
# You might add additional methods to encapsulate and simplify the operations, but they must be
# thoroughly documented


class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
        
    def __str__(self):
        return ("Node({})".format(self.value)) 

    __repr__ = __str__


class BinarySearchTree:
    '''
        >>> x=BinarySearchTree()
        >>> x.insert('mom')  
        >>> x.insert('omm') 
        >>> x.insert('mmo') 
        >>> x.root          
        Node({'mmo': ['mom', 'omm', 'mmo']})
        >>> x.insert('sat')
        >>> x.insert('kind')
        >>> x.insert('ats') 
        >>> x.root.left
        Node({'ast': ['sat', 'ats']})
        >>> x.root.right is None
        True
        >>> x.root.left.right
        Node({'dikn': ['kind']})
    '''

    def __init__(self):
        self.root = None
    # insert method modified to insert a word
    def insert(self, value):

        if self.root is None: 
            self.root = Node({''.join(sorted(value)):[value]})   
        else:
            self._insert(self.root, value)

    # modified insert helper method to allow us to insert a dictionaly in the node 
    # instead of just a number, with the value as the
    # sorted word and the value as a list of  words that were given
    def _insert(self, node, value):
        sorted_value = ''.join(sorted(value)) # sorted value
        for i in node.value.keys(): # return key of the dictionary
            key_node = i 

        if(sorted_value == key_node): # add word to end of list if sorted word == key 
            node.value[key_node].append(value)  
            
        elif(sorted_value < key_node): # create node if sorted word is < key
            if(node.left==None):
                node.left = Node({''.join(sorted(value)):[value]})
            else:
                self._insert(node.left, value)
        else:                         # create node if sorted word is > key
            if(node.right==None):
                node.right = Node({''.join(sorted(value)):[value]})
            else:
                self._insert(node.right, value)


    def isEmpty(self):
        return self.root == None

    @property
    def printInorder(self):
        if self.isEmpty(): 
            return None
        else:
            self._inorderHelper(self.root)
        
    def _inorderHelper(self, node):
        if node is not None:
            self._inorderHelper(node.left) 
            print(node.value, end=' : ') 
            self._inorderHelper(node.right)   



class Anagrams:
    '''
        # Verify class has _bst attribute  
        >>> x = Anagrams(5)
        >>> '_bst' in x.__dict__    
        True
        >>> isinstance(x.__dict__.get('_bst'), BinarySearchTree)
        True
        >>> x = Anagrams(5)
        >>> x.create('words_small.txt')
        >>> x.getAnagrams('tap')
        'No match'
        >>> x.getAnagrams('arm')
        'No match'
        >>> x.getAnagrams('rat')
        ['art', 'tar', 'rat']
        >>> x._bst.printInorder
        {'a': ['a']} : {'adns': ['ands', 'sand']} : {'ahms': ['sham', 'hams']} : {'amt': ['tam', 'mat']} : {'arst': ['arts', 'rats', 'star']} : {'arsty': ['artsy']} : {'art': ['art', 'tar', 'rat']} : 
    '''
    
    def __init__(self, word_size):
        self.word_size = word_size
        self._bst = BinarySearchTree() 
        


    def create(self, file_name):
        with open(file_name) as f: # ensures the file closes after the file operation finishes 
            contents = f.read() # reads the entire file, saving data in contents as string 
        content_list = contents.split()
        for word in content_list: # loop to check length of word if its not too big and inserts it into BST 
            if len(word) <= self.word_size:
                self._bst.insert(word)
            



    def getAnagrams(self, word):
        current = self._bst.root
        sorted_word = ''.join(sorted(word)) # sorted word
        for i in current.value.keys(): # return key of the dictionary
            key_node = i
         
        while current != None: # traverse through BST starting at root
            if sorted_word in current.value: # checks if sorted word is a key in dictionary and returns the value (list of inserted words)
                return current.value[sorted_word]
            elif sorted_word < key_node: # if sorted word not a key in dictionarty, traverse through left subtree
                current = current.left
            else:
                current = current.right # if sorted word not a key in dictionarty, traverse through right subtree
        return 'No match' 
             
        
        

if __name__ == "__main__":
    import doctest
    doctest.testmod()
 


