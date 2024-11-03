from typing import List

MAX_LEN = 3


def suggestedProducts(products: List[str], searchWord: str) -> List[List[str]]:

    trieRoot = {}

    def add_word_to_trie(word):

        curr = trieRoot

        for char in word:

            if char not in curr:
                curr[char] = {}

            curr = curr[char]

        curr["*"] = word

    for product in products:

        add_word_to_trie(product)

    def dfs(node, res):
        if len(res) == MAX_LEN:
            return

        if node.get("*"):
            res.append(node["*"])

        for k in range(ord("a"), ord("z") + 1):

            if chr(k) in node:
                dfs(node[chr(k)], res)

    def find_prefix(prefix):
        curr = trieRoot

        for char in prefix:
            if char not in curr:
                return False

            curr = curr[char]

        return curr

    char_list = []

    query_res = []

    for i in range(len(searchWord)):

        search_res = []

        char_list.append(searchWord[i])

        prefix_node = find_prefix(char_list)

        if prefix_node:
            dfs(prefix_node, search_res)

        query_res.append(search_res)

    return query_res

if __name__ == "__main__":

    products = ["mobile", "mouse", "moneypot", "monitor", "mousepad"]
    searchWord = "mouse"

    result = suggestedProducts(products, searchWord)
    print(result)
