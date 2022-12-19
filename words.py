def to_upper(words, starts):
    for word in words:
        for letter in starts:
            if word.startswith(letter):
               print(word.upper())


to_upper(["hello", "hi", 'envelope'],["h"])