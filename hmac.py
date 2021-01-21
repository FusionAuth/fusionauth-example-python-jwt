import jwt

key = "hello pythonistas! #$! PYTHON it up"
encoded = jwt.encode({"some": "payload"}, key, algorithm="HS256")

print(encoded)

print jwt.decode(encoded, key, algorithms="HS256")
