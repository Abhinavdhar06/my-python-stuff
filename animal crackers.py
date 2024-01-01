def animal_crackers(text):
    words = text.split()
    
    return words[0][0].lower() == words[1][0].lower()

result = animal_crackers("caca cha")
print(result)


