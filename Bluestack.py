def reverse_each_word(sentence):
    temp_var = ""
    reverse_str = ""
    for char in sentence:

        if ('a' <= char <= 'z') or ('A' <= char <= 'Z'):
            temp_var = char + temp_var

        else:
            reverse_str = reverse_str + temp_var + char
            temp_var = ""
            reverse_str = reverse_str + temp_var

    return reverse_str


def main():
    test_str = "String; 2be reversed..."
    assert reverse_each_word(test_str), 'gnirtS; eb2 desrever...'