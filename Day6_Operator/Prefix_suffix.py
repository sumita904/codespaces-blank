#File extensions-- removesuffix()
message='python_notes.txt'
print(message.removesuffix('.txt'))

# removeprefix()
nostarch_url='https://nostarch.com'
print(nostarch_url.removeprefix('https://'))

""" three stripping functions- lstrip(),rstrip(),strip()
strip() method - removes whitespace from both side
rstrip() method - removes whitespace from right side
lstrip() method- removes whitespace from left side
"""

message = '  Python  '
print(message.strip())
print(message.rstrip())
print(message.lstrip())



