def reverse_each_word(sentence):
    """
    This will only change/replaces position of
    the alpha char not the special char
    """
    temp_var = ""
    reverse_str = ""
    for char in sentence:

        if ('a' <= char <= 'z') or ('A' <= char <= 'Z'):
            temp_var = char + temp_var  # temp_var will contain the special char

        else:
            reverse_str = reverse_str + temp_var + char
            temp_var = ""
            reverse_str = reverse_str + temp_var  # reverse_str will contain all char including special

    return reverse_str


def main():
    test_str = "String; 2be reversed..."
    getresult = reverse_each_word(test_str)
    assert getresult, 'gnirtS; eb2 desrever...'
    return 0


if __name__ == '__main__':
    main()
