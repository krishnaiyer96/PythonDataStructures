class HashMapping:
    def __init__(self):
        self.MAX = 100
        self.arr = [[] for i in range(self.MAX)]

    def get_hash(self, key):
        h = 0
        for char in key:
            h += ord(char)   # This function will find the ASCII value of the character
        return h % self.MAX       # we are doing a MOD with 100. We are considering 100 as the size of the list assigned.

    def __setitem__(self, key, val):
        h = self.get_hash(key)

        self.arr[h].append((key, val))


    def __getitem__(self, key):
        h = self.get_hash(key)
        return self.arr[h]




if __name__ == '__main__':
    hm = HashMapping()
    hm['krishna'] = 27
    print(hm.arr)
    print(hm['krishna'])
