class BinarySearchTree:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None

    def add_child(self,data):
        if data == self.data:
            return
        elif data<self.data:
            #store value in the left node
            if self.left:
                self.left.add_child(data)
            else:
                self.left = BinarySearchTree(data)
        else:
            # store value in the left node
            if self.right:
                self.right.add_child(data)
            else:
                self.right = BinarySearchTree(data)

    def inorder_traversal(self):
        elements = []
        #visit left tree
        if self.left:
            elements += self.left.inorder_traversal()
        #visit base node
        elements.append(self.data)
        #visit right tree
        if self.right:
            elements += self.right.inorder_traversal()
        return elements

    def preorder_traversal(self):
        elements = []
        #visit root
        elements.append(self.data)
        #visit left tree
        if self.left:
            elements += self.left.preorder_traversal()
        #visit right tree
        if self.right:
            elements += self.right.preorder_traversal()
        return elements

    def postorder_traversal(self):
        elements = []
        # visit left tree
        if self.left:
            elements += self.left.postorder_traversal()
        # visit right tree
        if self.right:
            elements += self.right.postorder_traversal()
        # visit root
        elements.append(self.data)
        return elements

    def search(self,val):
        if val == self.data:
            return True
        elif val>self.data:
            if self.right:
                return self.right.search(val)
            else:
                return False
        else:
            if self.left:
                return self.left.search(val)
            else:
                return False

    def find_max(self):
        if self.right:
            return self.right.find_max()
        return self.data

    def find_min(self):
        if self.left:
            return self.left.find_min()
        return self.data

    def calculate_sum(self):
        return sum(self.inorder_traversal())

    def delete1(self,val):
        if val>self.data:
            if self.right:
                self.right = self.right.delete(val)
        elif val < self.data:
            if self.left:
                self.left = self.left.delete(val)
        else:
            if self.left is None and self.right is None:
                return None
            elif self.right is None:
                return self.left
            elif self.left is None:
                return self.right
            max_value = self.left.find_max()
            self.data = max_value
            self.left.delete(max_value)
        return self

    def delete(self,val):
        if val>self.data:
            if self.right:
                self.right = self.right.delete(val)
        elif val<self.data:
            if self.left:
                self.left = self.left.delete(val)
        else:
            if self.left is None and self.right is None:
                return None;
            elif self.left is None:
                return self.right
            elif self.right is None:
                return self.left
            min_val = self.right.find_min()
            self.data = min_val
            self.right = self.right.delete(min_val)
        return self

def build_tree(elements):
    root = BinarySearchTree(elements[0])
    for i in range(1, len(elements)):
        root.add_child(elements[i])
    return root

if __name__=="__main__":
    numbers = [15,12,7,9,14,27,20,23,88]
    root = build_tree(numbers)
    print(root.inorder_traversal())
    print(f"Sum of all elements in the tree:- {root.calculate_sum()}")
    print(root.search(7))
    print(root.search(8))
    print(root.search(88))
    print(root.find_max())
    print(root.find_min())
    root = root.delete(9)
    print(root.postorder_traversal())
    print(root.inorder_traversal())
    print(root.preorder_traversal())
    root = root.delete1(15)
    print(root.preorder_traversal())