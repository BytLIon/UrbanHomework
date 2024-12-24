def all_variants(text):

    for x in range(len(text)):
        for r in range(len(text) - x):
            yield text[x:r + x + 1]


if __name__ == '__main__':
    a = all_variants("abc")
    for i in a:
        print(i)