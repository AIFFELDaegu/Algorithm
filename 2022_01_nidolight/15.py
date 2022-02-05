class Trie:
    def __init__(self):
        self.root = {}
        self.maxDepth = 0

    def insert(self, s):
        cur_node = self.root
        depth = len(s)

        if depth>self.maxDepth:
            self.maxDepth = depth

        for c in s:
            if c not in cur_node:
                cur_node[c] = {}
            cur_node = cur_node[c]
        cur_node['*'] = s

def solution(phone_book):
    dict = Trie()
    
    for num in phone_book:
        dict.insert(num)

    print(dict.root)

    currentDepth = 0
    maxDepth = dict.maxDepth
    answer = recursive(dict.root,currentDepth,maxDepth)

    return answer

def recursive(dict,currentDepth,maxDepth):
    for k in dict:
        if k == '*':
            if currentDepth<maxDepth:
                return False
            else:
                return True
            
        return recursive(dict[k], currentDepth+1,maxDepth)



print(solution(["123","456","789"]))