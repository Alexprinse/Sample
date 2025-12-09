from collections import deque
from typing import List
class Solution:
    def alienOrder(self, words: List[str]) -> str:
        # Initialize adjacency matrix for the directed graph
        # graph[i][j] = True means character i comes before character j
        graph = [[False] * 26 for _ in range(26)]

        # Track which characters appear in the words
        seen_chars = [False] * 26
        char_count = 0
        num_words = len(words)

        # Build the graph by comparing adjacent words
        for i in range(num_words - 1):
            # Mark all characters in current word as seen
            for char in words[i]:
                if char_count == 26:
                    break
                char_index = ord(char) - ord('a')
                if not seen_chars[char_index]:
                    char_count += 1
                    seen_chars[char_index] = True

            # Compare current word with next word to find ordering
            curr_word_len = len(words[i])
            for j in range(curr_word_len):
                # If current word is longer than next word and they match up to this point,
                # the ordering is invalid (e.g., "abc" cannot come before "ab")
                if j >= len(words[i + 1]):
                    return ''

                char1, char2 = words[i][j], words[i + 1][j]
                if char1 == char2:
                    continue

                # Found first different character - this gives us ordering information
                index1, index2 = ord(char1) - ord('a'), ord(char2) - ord('a')

                # Check for contradictory ordering (char2 already comes before char1)
                if graph[index2][index1]:
                    return ''

                # Add edge: char1 comes before char2
                graph[index1][index2] = True
                break

        # Mark characters in the last word as seen
        for char in words[num_words - 1]:
            if char_count == 26:
                break
            char_index = ord(char) - ord('a')
            if not seen_chars[char_index]:
                char_count += 1
                seen_chars[char_index] = True

        # Calculate in-degrees for topological sort
        in_degree = [0] * 26
        for i in range(26):
            for j in range(26):
                if i != j and seen_chars[i] and seen_chars[j] and graph[i][j]:
                    in_degree[j] += 1

        # Perform topological sort using Kahn's algorithm
        queue = deque()
        result = []

        # Add all characters with in-degree 0 to queue
        for i in range(26):
            if seen_chars[i] and in_degree[i] == 0:
                queue.append(i)

        # Process queue
        while queue:
            curr_char_index = queue.popleft()
            result.append(chr(curr_char_index + ord('a')))

            # Reduce in-degree for all neighbors
            for i in range(26):
                if seen_chars[i] and i != curr_char_index and graph[curr_char_index][i]:
                    in_degree[i] -= 1
                    if in_degree[i] == 0:
                        queue.append(i)

        # If we couldn't process all characters, there's a cycle
        return '' if len(result) < char_count else ''.join(result)
