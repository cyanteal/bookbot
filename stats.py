def word_count(text):
    words = text.split()
    count = len(words)
    return count

def character_count(text):
    character_count = {}
    character_list = []

    for character in text:
        character = str.lower(character)
        character_list.append(character)
    
    for character in character_list:
        if character not in character_count:
            character_count[character] = 0
        if character in character_count:
            character_count[character] += 1
    
    return character_count

def sorting(characters):
    sorted_count_list = []

    for char in characters:
        char_count = {}
        count = characters[char]
        char_count["char"] = char
        char_count["num"] = count
        sorted_count_list.append(char_count)

    return sorted_count_list

def sort_on(characters):
    return characters["num"]


