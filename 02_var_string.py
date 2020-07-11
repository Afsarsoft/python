# pyright: strict

# +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
# String manipulation
# +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
phrase: str = 'python is cool.'
print(f'String -> {phrase}')

phrase: str = 'python is cool.'
print(f'String -> {phrase.title()}')

# +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
scape_char: str = "Python is \"cool\"."
# scape_char: str = "Surush\"Cyrus\""
print(f'Scape character -> {scape_char}')

# +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
tab_char: str = '\tPython is cool'
print(f'Tab character -> {tab_char}')

# +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
new_line: str = 'Python is \ncool.'
print(f'New line -> {new_line}')

new_line = '\nPython \nis \ncool.'
print(f'New line -> {new_line}')

# +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
m_lines: str = """
   This is a sample for
   multilines
"""
print(f'Multi lines -> {m_lines}')
# +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

# +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
name: str = 'Python'
rest: str = 'is cool.'
print(f'Concatination -> {name} {rest}')

# +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
phrase: str = 'Python is cool.'
print(f'lower() -> {phrase} -> {phrase.lower()}')
print(f'upper() -> {phrase} -> {phrase.upper()}')
print(f'isupper() -> {phrase} -> {phrase.isupper()}')
print(f'upper().isupper() -> {phrase} -> {phrase.upper().isupper()}')
print(f'len() -> {phrase} -> {len(phrase)}')
print(f'[0] -> {phrase} -> {phrase[0]}')
print(f'[5] ->{phrase} -> {phrase[5]}')
print(f'[3:5] -> {phrase} -> {phrase[3:5]}')
print(f'[0:6] -> {phrase} -> {phrase[0:6]}')
print(f'[:] -> {phrase} -> {phrase[:]}')
print(f'[:5] -> {phrase} -> {phrase[:5]}')
print(f'[1:] -> {phrase} -> {phrase[1:]}')
print(f'[3:] -> {phrase} -> {phrase[3:]}')
print(f'[0:] -> {phrase} -> {phrase[0:]}')
print(f'[-1] -> {phrase} -> {phrase[-1]}')
print(f'[-5] -> {phrase} -> {phrase[-5]}')
print(f'[0:-7] -> {phrase} -> {phrase[0:-7]}')
print(f'[1:-1] -> {phrase} -> {phrase[1:-1]}')
print(f"count(o) -> {phrase} -> {phrase.count('o')}")
print(f"count(c) -> {phrase} -> {phrase.count('c')}")
print(f"find('u') -> {phrase} -> {phrase.find('u')}")  # if cannot find
print(f"find('n') -> {phrase} -> {phrase.find('n')}")
print(f"find('cool') -> {phrase} -> {phrase.find('cool')}")
print(f"index('h') -> {phrase} -> {phrase.index('h')}")
# errors out if cannot find->ValueError: substring not found
#print(f"index('u') ->{phrase} -> {phrase.index('u')}")
print(
    f"replace('cool', 'good') -> {phrase} -> {phrase.replace('cool', 'good')}")

# +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
num: int = 42
print(f'adding {num} using format or convert to a string {num}')

# +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
# Stripping Whitespace
greet: str = '     Hello Bob    '
print(f'lstrip() ->"{greet}:" {greet.lstrip()}')
print(f'rstrip() ->"{greet}:" {greet.rstrip()}')
print(f'strip()  ->"{greet}:" {greet.strip()}')

# +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
s1: str = 'A lot     of     spaces'
print(f'spliting "{s1}" using split() -> {s1.split()}')

s2: str = 'first;second;third'
print(f'spliting "{s2}" using split(";") -> {s2.split(";")}')

# +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

line: str = 'Please have a nice day'
line.startswith('Please')
line.startswith('P')
line.startswith('p')
print(f'"{line}" has line.startswith("Please")? {line.startswith("Please")}')
# +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
