import random

class Node:
    def __init__(self,value,left=None,right=None,parent=None,height=None):
        self.value = value
        self.left = left
        self.right = right
        self.parent = parent
        self.height = height
        self.height_below = 0
        
    def insert(self,data):
        if self.value==data:
            return False
        
        height = self.height+1
        
        if not self.left:
            self.left = Node(data,height=height,parent=self)
            self.update_height_below(1)
            return True
        if not self.right:
            self.right= Node(data,height=height,parent=self)
            return True
        if self.left.height_below < self.right.height_below:
            return self.left.insert(data)
        return self.right.insert(data)
    
    def get_height(self):
        if self.left and self.right:
            return 1 + max(self.left.get_height(),self.right.get_height())
        elif self.left:
            return 1 + self.left.get_height()
        elif self.right:
            return 1 + self.right.get_height()
        return 1
    
    def update_height_below(self,value):
        self.height_below+=value
        if self.parent:
            self.parent.update_height_below(value)
            
    def inorder(self):
        if self:
            if self.left:
                self.left.inorder()
            print(self.value)
            if self.right:
                self.right.inorder()
                
    def display(self):
        """Returns list of strings, width, height, and horizontal coordinate of the root."""
        # No child.
        if self.right is None and self.left is None:
            line = '%s' % self.value
            width = len(line)
            height = 1
            middle = width // 2
            return [line], width, height, middle

        # Only left child.
        if self.right is None:
            lines, n, p, x = self.left.display()
            s = '%s' % self.value
            u = len(s)
            first_line = (x + 1) * ' ' + (n - x - 1) * '_' + s
            second_line = x * ' ' + '/' + (n - x - 1 + u) * ' '
            shifted_lines = [line + u * ' ' for line in lines]
            return [first_line, second_line] + shifted_lines, n + u, p + 2, n + u // 2

        # Only right child.
        if self.left is None:
            lines, n, p, x = self.right.display()
            s = '%s' % self.value
            u = len(s)
            first_line = s + x * '_' + (n - x) * ' '
            second_line = (u + x) * ' ' + '\\' + (n - x - 1) * ' '
            shifted_lines = [u * ' ' + line for line in lines]
            return [first_line, second_line] + shifted_lines, n + u, p + 2, u // 2

        # Two children.
        left, n, p, x = self.left.display()
        right, m, q, y = self.right.display()
        s = '%s' % self.value
        u = len(s)
        first_line = (x + 1) * ' ' + (n - x - 1) * '_' + s + y * '_' + (m - y) * ' '
        second_line = x * ' ' + '/' + (n - x - 1 + u + y) * ' ' + '\\' + (m - y - 1) * ' '
        if p < q:
            left += [n * ' '] * (q - p)
        elif q < p:
            right += [m * ' '] * (p - q)
        zipped_lines = zip(left, right)
        lines = [first_line, second_line] + [a + u * ' ' + b for a, b in zipped_lines]
        return lines, n + m + u, max(p, q) + 2, n + u // 2
       
class BinaryTree:
    
    def __init__(self):
        self.size = 0
        self.root = None
        
    def insert(self,data):
        if self.root:
            if self.root.insert(data):
                self.size+=1
                return True
            else:
                return False
        
        self.root = Node(data,height=0)
        self.size+=1
        return True
        
    def inorder(self):
        if self.root:
            return self.root.inorder()
        return None
    
    def display(self):
        if self.root is None:
            print('empty tree')
        else:
            lines, _, _, _ = self.root.display()
            for line in lines:
                print(line)
            
    def build_from_list(self,l):
        for i in l:
            self.insert(i)
            
def get_fast_bt(size=10,seed=1):
    bt = BinaryTree()
    random.seed=1
    for _ in range(size):
        bt.insert(random.randint(0, 100))
    return bt

def countNonleaf(root): 
      
    # Base cases.  
    if (root == None or (root.left == None and 
                         root.right == None)):  
        return 0
  
    # If root is Not None and its one of   
    # its child is also not None  
    return (1 + countNonleaf(root.left) + 
                countNonleaf(root.right)) 
        
def count_internal_nodes(tree):
    bt=BinaryTree()
    bt.build_from_list(tree)
    return countNonleaf(bt.root)

if __name__ == "__main__":
    tree = [1, 3, 1, -1, 3]
    print (count_internal_nodes(tree)) # should print 2