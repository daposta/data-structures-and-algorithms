class Node:
    def __init__(self, value) -> None:
        self.value = value
        self.right = None
        self.left = None



a = Node('a')
b = Node('b')
c = Node('c')
d = Node('d')
e = Node('e')
f = Node('f')


#option A/depth first using stack
def depthFirstValues(root=None):
    if not root:return []
    stack = [root]
    result = []

    while len(stack) > 0:
        current = stack.pop()
        result.append(current.value)

        if current.right: stack.append(current.right)
        if current.left: stack.append(current.left)
    return result

        

a.left =b
a.right = c
b.left = d
b.right = e
c.right = f


# print(depthFirstValues())

#Option B, using recursion/depth first using  stack
def recursionValues(root=None):

    if not root:return []
    leftValues = recursionValues(root.left)
    rightValues = recursionValues(root.right)
    return [root.value, *rightValues, *leftValues]
   

# print(recursionValues(a))


#using breadth-first approach

def breadthFirstValues(root):
    if not root: return []
    result = []
    queue = [root]
    while len(queue) > 0:
        current = queue.pop(0)
        result.append(current.value)

        if current.left: queue.append(current.left)
        if current.right: queue.append(current.right)
    return result


# print(breadthFirstValues(a))

#depth first
# def tree_includes(root, target):
#     if not root: return False

#     queue = [root]
#     while len(queue) > 0:
#         current = queue.pop(0)
#         if current.value== target:
#             return True
#         if current.left: queue.append(current.left)
#         if current.right: queue.append(current.right)
#     return False

# print(tree_includes(a, 'z'))

#uring recursion
def tree_includes(root, target):

    if not root: return False
    # current = root
    if root.value== target:
            return True
    return tree_includes(root.left, target) or  tree_includes(root.right, target)
    



# print(tree_includes(a, 'b'))


# tree sum

a = Node(10)
b = Node(2)
c = Node(3)
d = Node(4)
e = Node(5)
f = Node(6)

a.left =b
a.right = c
b.left = d
b.right = e
c.right = f

def tree_sum(root):
    if not root: return 0
    sum = 0
    queue = [root]
    while len(queue) > 0:
        current = queue.pop(0)
        sum += current.value
        if current.left: queue.append(current.left)
        if current.right: queue.append(current.right)
    return sum


# print(tree_sum(a))


# sum of tree using recursion
def tree_sum_recursion(root):
    if not root: return 0
    # current = root
    return  root.value + tree_sum_recursion(root.left) +  tree_sum_recursion(root.right)
    
# print(tree_sum_recursion(a))


def tree_minimum(root):
    if not root: return -1
    current_min = root.value
    queue = [root]
    while len(queue) > 0:
        current = queue.pop(0)
        if current_min > current.value: 
            current_min = current.value
        if current.left: queue.append(current.left)
        if current.right: queue.append(current.right)
    return current_min

# print(tree_minimum(a))
# n = []
def tree_min_recursion(root):
    print('roott>>.', root)
    if root == None: return -1
    

    
    left_min = tree_min_recursion(root.left) 
    right_min = tree_min_recursion(root.right)
    return min(root.value, left_min, right_min)


print(tree_min_recursion(a))
    
# def maxPathSum(root):
#     if root == None: return -1
#     if ( root.left == None) and  (root.right==None):
#         return root.value
#     maxChildPathSum = max(maxPathSum(root.left), maxPathSum(root.right))
#     return root.value + maxChildPathSum



# print(maxPathSum(a))