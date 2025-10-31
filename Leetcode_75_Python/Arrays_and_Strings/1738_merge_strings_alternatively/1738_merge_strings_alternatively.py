def mergeAlternately(self, word1: str, word2: str) -> str:
    # An array is more efficient
    final = []

    # A variable we can use to iterate through the string.
    max_length = max(len(word1), len(word2))

    for i in range(max_length):
        if i < len(word1):
            final.append(word1[i])

        if i < len(word2):
            final.append(word2[i])

    return "".join(final)
