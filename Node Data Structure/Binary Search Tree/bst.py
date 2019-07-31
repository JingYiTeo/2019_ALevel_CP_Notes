class BST:

    #create constructor:
        #     0
        #   0   0 (child level is none)
    def __init__(self, data):
        self.data = data
        self.leftchild = None
        self.rightchild = None


    def insert(self, Newdata):

        if Newdata < self.data:
            if self.leftchild is None:
                #add in the data
                self.leftchild = BST(Newdata)
            else:
                #recursively go over the function
                self.leftchild.insert(Newdata)

        else:
            if self.rightchild is None:
                self.rightchild = BST(Newdata)
            else:
                self.rightchild.insert(Newdata)

    def search(self, target):
        if self.data == target:
            print( self.data, "Found")
        
        #when child level is empty
        elif self.leftchild is None and self.rightchild is None:
            print("Not Found")

     #       0
     #  <- 0   0
        #when search item is smaller than root so move left
     
        elif target < self.data:
            if self.leftchild is None:
                print("None Found")
            else:
                return self.leftchild.search(target)
        else:#right side
            if self.rightchild is None:
                print("Not Found")
            else:
                return self.rightchild.search(target)
            
    def print_inorder(self):
        if self.leftchild:
            self.leftchild.print_inorder()
        print(self.data, end="\n")
        if self.rightchild:
            self.rightchild.print_inorder()



bst = BST(50)
bst.insert(10)
bst.insert(20)
bst.insert(30)
bst.insert(5)
bst.insert(15)
bst.print_inorder()
bst.search(60)
bst.search(10)

    
                
            
                
