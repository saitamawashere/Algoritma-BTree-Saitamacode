#Error output - did not find
class BTree:
    def __init__(self, t):
        self.root = None
        self.t = t

class BTreeNode:
    def __init__(self, t, leaf=True):
        self.leaf = leaf
        self.keys = []
        self.child = []

def print_tree(node, level=0):
    if node is None:
        return
    
    for i in range(len(node.keys)):
        if not node.leaf:
            print_tree(node.child[i], level + 1)
        print('   ' * level + str(node.keys[i]))
    
    if not node.leaf:
        print_tree(node.child[-1], level + 1)


def insert(root, key):
    if root is None:
        return BTreeNode(leaf=True, keys=[key])

    if len(root.keys) < (2 * t) - 1:
        insert_non_full(root, key)
    else:
        new_root = BTreeNode(leaf=False)
        new_root.child.append(root)
        split_child(new_root, 0, root)
        insert_non_full(new_root, key)
        root = new_root
    
    return root


def insert_non_full(node, key):
    i = len(node.keys) - 1

    if node.leaf:
        node.keys.append(None)
        while i >= 0 and key < node.keys[i]:
            node.keys[i + 1] = node.keys[i]
            i -= 1
        node.keys[i + 1] = key
    else:
        while i >= 0 and key < node.keys[i]:
            i -= 1
        i += 1
        if len(node.child[i].keys) == (2 * t) - 1:
            split_child(node, i, node.child[i])
            if key > node.keys[i]:
                i += 1
        insert_non_full(node.child[i], key)


def split_child(parent, i, child):
    new_child = BTreeNode(leaf=child.leaf)
    parent.keys.insert(i, child.keys[t - 1])
    parent.child.insert(i + 1, new_child)
    new_child.keys = child.keys[t:2 * t - 1]
    child.keys = child.keys[:t - 1]

    if not child.leaf:
        new_child.child = child.child[t:2 * t]
        child.child = child.child[:t - 1]


def main():
    root = None
    
    while True:
        choice = input("Pilih operasi (1: Insert, 2: Print, 3: Keluar): ")
        
        if choice == '1':
            key = int(input("Masukkan kunci yang akan diinsert: "))
            root = insert(root, key)
            print("Kunci", key, "berhasil diinsert.")
        elif choice == '2':
            print("Bentuk visual B-Tree:")
            print_tree(root)
        elif choice == '3':
            break
        else:
            print("Pilihan tidak valid.")


if __name__ == "__main__":
    t = int(input("Masukkan nilai t untuk B-Tree: "))
    main()