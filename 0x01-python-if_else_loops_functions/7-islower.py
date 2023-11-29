#!/usr/bin/python3

def islower(c):
	char = ord(c)
	if char > 64 and char < 91:
		return False

	elif char > 96 and char < 123:
		return True

	return False
