def convert(s:str, nrows:int)->str:
    """A function that converts a word to a zigzag pattern of a given number \
        of rows and return the read of that patern

    Args:
        s (str): string to be transformed
        nrows (int): number of rows for zigzag

    Returns:
        str: string converted to zigzag style

    e.g:
       convert('ABCDE', 3)\n
       A E\n
       BD\n
       C\n
       -> AEBDC
    """
    # return the word if there is nothing to change
    if len(s) <= nrows or nrows == 1:
        return s
    # list for each line of the zigzag
    lines = [[] for i in range(nrows)]
    currRow = 0
    round = False
    word = ''
    # loop that travels through the string and form each zigzag line
    while s != '':
        lines[currRow].append(s[0])
        s = s.replace(s[0],'',1) # removing the char from the string
        if currRow < nrows-1 and not round:
            currRow += 1
        else:
            currRow -=1
            if currRow == 0:
                round = False
            elif round == False:
                round = True
    # forming the word with each line
    for line in lines:
        for c in line:
            word += c
    return word

print(convert('Pineapple', 4))