# pyright: strict
from typing import List

# +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++


def emoji_converter(message: str) -> str:
    words: List[str] = message.split(' ')
    emojis = {
        ":)": "😀",
        ":(": "😌"
    }

    output: str = ""
    word: str = ''
    for word in words:
        output += emojis.get(word, word) + " "

    return(output)


message: str = str(input(">"))
result: str = emoji_converter(message)
print(result)
# +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
