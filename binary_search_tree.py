class TreeNode:
    '''
    A class that represents the individual node in a BST.
    '''
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None

    def binary_tree_search(self, find_key):
        '''
        search the binary tree
        '''
        if self.key==find_key:
            print("The node is present")
            return True
        if find_key < self.key:
            if self.left:
                self.left.binary_tree_search(find_key)
                # print("The node is present")
                # return
            else:
                # print("Empty Node")
                return False
        else:
            if self.right:
                self.right.binary_tree_search(find_key)
                # print("The node is present")
                return True
            else:
                # print("Empty Node")
                return False

def new_key_insert(root, new_key):
    '''
    insert new key
    '''
    if root is None:
        root = TreeNode(new_key)
        return root
    if new_key < root.key:
        root.left = new_key_insert(root.left, new_key)
    else:
        root.right = new_key_insert(root.right, new_key)
    return root

def display(root):
    '''
    Function to display the output of the tree
    '''
    if root:
        display(root.left)
        print(root.key)
        display(root.right)

def main():
    '''
    run the BTS
    '''
    tree = TreeNode(50)
    tree = new_key_insert(tree, 30)
    tree = new_key_insert(tree, 20)
    tree = new_key_insert(tree, 40)
    tree = new_key_insert(tree, 70)
    tree = new_key_insert(tree, 60)
    tree = new_key_insert(tree, 80)

    display(tree)
    print()

    item = 0
    output = tree.binary_tree_search(item)
    print(f'{item} is {output}', '\n')

    item = 50
    output = tree.binary_tree_search(item)
    print(f'{item} is {output}')

if __name__ == '__main__':
    main()
