from words import keys
class TrieNode(): 
    def __init__(x): 
          
        # Initialising one node for trie 
        x.children = {} 
        x.last = False
  
class Trie(): 
    def __init__(x): 
          
        # Initialising the trie structure. 
        x.root = TrieNode() 
        x.word_list = [] 
  
    def formTrie(x, keys): 
          
        # Forms a trie structure with the given set of strings 
        # if it does not exists already else it merges the key 
        # into it by extending the structure as required 
        for key in keys: 
            x.insert(key) # inserting one key to the trie. 
  
    def insert(x, key): 
          
        # Inserts a key into trie if it does not exist already. 
        # And if the key is a prefix of the trie node, just  
        # marks it as leaf node. 
        node = x.root 
  
        for a in list(key): 
            if not node.children.get(a): 
                node.children[a] = TrieNode() 
  
            node = node.children[a] 
  
        node.last = True
  
    def search(x, key): 
          
        # Searches the given key in trie for a full match 
        # and returns True on success else returns False. 
        node = x.root 
        found = True
  
        for a in list(key): 
            if not node.children.get(a): 
                found = False
                break
  
            node = node.children[a] 
  
        return node and node.last and found 
  
    def suggestionsRec(x, node, word): 
          
        # Method to recursively traverse the trie 
        # and return a whole word.  
        if node.last: 
            x.word_list.append(word) 
  
        for a,n in node.children.items(): 
            x.suggestionsRec(n, word + a) 
  
    def printAutoSuggestions(x, key): 
          
        # Returns all the words in the trie whose common 
        # prefix is the given key thus listing out all  
        # the suggestions for autocomplete. 
        node = x.root 
        not_found = False
        temp_word = '' 
  
        for a in list(key): 
            if not node.children.get(a): 
                not_found = True
                break
  
            temp_word += a 
            node = node.children[a] 
  
        if not_found: 
            return 0
        elif node.last and not node.children: 
            return -1
  
        x.suggestionsRec(node, temp_word) 
  
        for s in x.word_list: 
            print(s) 
        return 1
  
# Driver Code 
key= input("Enter the incomplete word ") # key for autocomplete suggestions. 
status = ["Not found", "Found"] 
  
# creating trie object 
t = Trie() 
  
# creating the trie structure with the  
# given set of strings. 
t.formTrie(keys) 
  
# autocompleting the given key using  
# our trie structure. 
comp = t.printAutoSuggestions(key) 
  
if comp == -1: 
    print("No other strings found with this prefix\n") 
elif comp == 0: 
    print("No string found with this prefix\n") 
  
