#!/usr/bin/python3

def uppercase(str):
	for i in range(len(str)):
		letter = str[i]
		if ord(letter) >= 97 or ord(letter) <= 122:
			letter = ord(letter) - 32
			str_final[i] = chr(letter)

	return str_final[i]
