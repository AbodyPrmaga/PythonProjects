def cleanworld(word):

    if len(word) == 1:
        return word
    
    if word[0] == word[1]:

        return cleanworld(word[1:])

    return word[0] + cleanworld(word[1:])


print(cleanworld("wwwwwoooooorrrrrllllddd"))