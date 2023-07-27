from collections import defaultdict


class Solution(object):
    def groupAnagrams(self, strs):
        # Create a hashmap to store the anagrams
        anagram_map = defaultdict(list)
        # Iterate through each string in the input array
        for word in strs:
            # Sort the word to use it as a key in the hashmap
            sorted_word = ''.join(sorted(word))

            # Add the word to the list of anagrams for the sorted word
            anagram_map[sorted_word].append(word)

        # Return the grouped anagrams as a list
        return list(anagram_map.values())


strs = ["eat", "tea", "tan", "ate", "nat", "bat"]
Sol = Solution()
print(Sol.groupAnagrams(strs))
