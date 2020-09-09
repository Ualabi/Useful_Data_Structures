class Trie:
    def __init__(self):
        self.sons = {}

    def insert(self, word: str) -> None:
        curr = self.sons
        for x in word:
            if x not in curr:
                curr[x] = {}
            curr = curr[x]
        curr['*'] = '*'

    def search(self, word: str) -> bool:
        return self.startsWith(word+'*')

    def startsWith(self, prefix: str) -> bool:
        curr = self.sons
        for x in prefix:
            if x in curr:
                curr = curr[x]
            else:
                return False
        return True

##################################################
# Example code
##################################################
obj = Trie()
for word in ['cat','good','god','go','goodness']:
    obj.insert(word)
print(obj.search('good'))
print(obj.startsWith('g'))