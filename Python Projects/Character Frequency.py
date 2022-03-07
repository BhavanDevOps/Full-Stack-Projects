def print_character_count(line):
    line=line.lower()
    unique_character=set(line)
    unique_character.discard(" ")
    for character in sorted(unique_character):
        print("{}: {}".format(character,line.count(character)))
        
line=input()
print_character_count(line)