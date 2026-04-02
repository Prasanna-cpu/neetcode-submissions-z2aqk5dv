class Solution:
    def letterCombinations(self, digits: str) -> List[str]:

        if not digits:
            return []
            
        
        result = []

        phone_map = {
            "2" : 'abc',
            "3" : 'def', 
            "4" : 'ghi',
            "5" : 'jkl',
            "6" : 'mno',
            "7" : 'pqrs',
            "8" : 'tuv',
            "9" : 'wxyz'
        }

        def backtrack(start, path):
            if start == len(digits):
                result.append(path)
                return

            possible_letters = phone_map[digits[start]]
            for letter in possible_letters:
                backtrack(start + 1 , path + letter)

        backtrack(0,"")
        return result
        