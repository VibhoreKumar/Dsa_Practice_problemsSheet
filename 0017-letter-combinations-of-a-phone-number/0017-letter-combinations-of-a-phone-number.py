class Solution:
    def letterCombinations(self, digits: str) -> list[str]:
        if digits == "":
            return []

        mapping = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz"
        }

        result = [""]

        for digit in digits:
            new_result = []

            for old_string in result:
                for letter in mapping[digit]:
                    new_result.append(old_string + letter)

            result = new_result

        return result