def read_string_and_reverse(input_string):
    words = str(input_string).split(' ')
    reversed_words = [word[::-1] for word in words]
    return " ".join(reversed_words)


if __name__ == '__main__':
    print(read_string_and_reverse(input()))
