#!/usr/bin/python3

def text_indentation(text):

    char_det = ['.', '?', ':']
    i = 0
    output_str = ""

    try:
        if not isinstance(text, str):
            raise TypeError("text must be a string")

    except TypeError as e:
        print(e)

    while i < len(text):
        output_str += text[i]
        if text[i] in char_det:
            output_str += "\n\n"
            if text[i + 1] == " ":
                i += 1
        i += 1

    print(output_str, end="")
