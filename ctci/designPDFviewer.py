def designerPdfViewer(h, word):
    max_height = 0
    for character in word:
        char_index = ord(character) - ord("a")
        max_height = max(max_height, h[char_index])
    return max_height


if __name__ == "__main__":
    h = "1 3 1 3 1 4 1 3 2 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5".split()

    word = "abc"

    print(designerPdfViewer(h, word))
