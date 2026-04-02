class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        
        wordSet = set(wordList)
        the_alphabets = 'abcdefghijklmnopqrstuvwxyz'
        if endWord not in wordList:
            return 0
        
        queue = deque([(beginWord, 1)])

        while queue:
            word , steps = queue.popleft()
            if word == endWord:
                return steps
            for i in range(len(word)):
                for c in the_alphabets:
                    nextWord = word[:i] + c + word[i+1:]
                    if nextWord in wordSet:
                        queue.append((nextWord, steps + 1))
                        wordSet.remove(nextWord)
        return 0
