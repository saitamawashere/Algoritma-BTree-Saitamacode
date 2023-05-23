class BTreeNode:
    def __init__(self, leaf=False):
        self.keys = []
        self.child = []
        self.leaf = leaf

class BTree:
    def __init__(self, t):
        self.root = BTreeNode(True)
        self.t = t

    def insert(self, k):
        root = self.root
        if len(root.keys) == (2 * self.t) - 1:
            temp = BTreeNode()
            self.root = temp
            temp.child.insert(0, root)
            self.split_child(temp, 0)
            self.insert_non_full(temp, k)
        else:
            self.insert_non_full(root, k)

    def insert_non_full(self, x, k):
        i = len(x.keys) - 1
        if x.leaf:
            x.keys.append((None, None))
            while i >= 0 and k < x.keys[i]:
                x.keys[i + 1] = x.keys[i]
                i -= 1
            x.keys[i + 1] = k
        else:
            while i >= 0 and k < x.keys[i]:
                i -= 1
            i += 1
            if len(x.child[i].keys) == (2 * self.t) - 1:
                self.split_child(x, i)
                if k > x.keys[i]:
                    i += 1
            self.insert_non_full(x.child[i], k)

    def split_child(self, x, i):
        t = self.t
        y = x.child[i]
        z = BTreeNode(y.leaf)
        x.child.insert(i + 1, z)
        x.keys.insert(i, y.keys[t - 1])
        z.keys = y.keys[t: (2 * t) - 1]
        y.keys = y.keys[0: t - 1]
        if not y.leaf:
            z.child = y.child[t: 2 * t]
            y.child = y.child[0: t - 1]

    def search(self, k, x=None):
        if isinstance(x, BTreeNode):
            i = 0
            while i < len(x.keys) and k > x.keys[i]:
                i += 1
            if i < len(x.keys) and k == x.keys[i]:
                return True
            elif x.leaf:
                return False
            else:
                return self.search(k, x.child[i])
        else:
            return self.search(k, self.root)

# Main program
if __name__ == '__main__':
    t = int(input("Masukkan nilai t: "))
    btree = BTree(t)

    data = input("Masukkan elemen-elemen B-Tree (pisahkan dengan spasi): ").split()
    data = [int(e) for e in data]

    for item in data:
        btree.insert(item)

    search_key = int(input("Masukkan nilai yang ingin dicari: "))
    found = btree.search(search_key)

    if found:
        print(f"Nilai {search_key} ditemukan dalam B-Tree.")
    else:
        print(f"Nilai {search_key} tidak ditemukan dalam B-Tree.")