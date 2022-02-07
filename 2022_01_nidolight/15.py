class Trie:
    def __init__(self):
        self.root = {}

    def insert(self, s):
        cur_node = self.root
        for c in s:
            if c not in cur_node:
                cur_node[c] = {}
            cur_node = cur_node[c]
        cur_node['*'] = s

def solution(phone_book):
    PBdict = Trie()

    for num in phone_book:
        PBdict.insert(num)

    return recursive(PBdict.root)

def recursive(d):
    for k in d.keys():
        if k == '*' and len(d) > 1:
            return False
        if type(d[k]) is dict:
            newDict = d[k]
            if not recursive(newDict):
                return False
    return True

print(solution(["12", "123", "1235", "567", "88"]))
