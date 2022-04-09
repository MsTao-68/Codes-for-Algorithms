# !usr/bin/Python
# Project: Build Trie Tree Data Structure
# Author: Shengmin(Tracy) Tao
# Date: 2022/04/09

class Trie:

    def __init__(self):
        self.children = [None] * 26  # init 26 chars
        self.isEnd = False  # init not isEnd

    def searchPrefix(self, prefix: str) -> "Trie":
        '''
        :param self: class
        :param prefix: prefix String
        function traverse prefix to create node.children array
        return: current node
        '''
        node = self
        for ch in prefix:
            ch = ord(ch) - ord("a")  # ch index
            if not node.children[ch]:  # ch not in node.children array
                return None
            node = node.children[ch]  # modify node.children array, add ch
        return node

    def insert(self, word: str) -> None:
        '''
        :param self: class
        :param word: String for create the trie tree
        function: insert words into trie tree
        return None
        '''
        node = self
        for ch in word:  # traverse the word to get char
            ch = ord(ch) - ord('a')  # ch index
            if not node.children[ch]:  # if this char in words not in children array
                node.children[ch] = Trie()  # create a node for this char
            node = node.children[ch]  # if this char exist, visit the node of this ch by index
        node.isEnd = True  # add Flag , represent the last char in prefix

    def search(self, word: str) -> bool:
        '''
        :param self: class
        :param word: String to search in trie tree
        funtion lookup the word in trie tree
        return bool: whether last char node is null and if the last char node.isEnd = Tree
        '''
        node = self.searchPrefix(word)  # search the prefix of the word, return the node of the last char in word
        return node is not None and node.isEnd

    def startsWith(self, prefix: str) -> bool:
        '''
        :param self: class
        :param prefix: prefix to search
        return bool: whether last char node is null and if the last char node.isEnd = Tree
        '''
        return self.searchPrefix(prefix) is not None
