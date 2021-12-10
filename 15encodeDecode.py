#!/usr/bin/python
import base64

str = "string example!! ..."
str = base64.b64encode(str.encode('utf-8'))
print("Encoded Stirng: ", str)
str = base64.b64decode(str).decode('utf-8')
print("Decoded Stirng: ", str)
