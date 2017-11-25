def balanced(braces):
        braced = 0
        for brace in braces:

            if brace == '{': braced += 1
            if brace == '}':
                braced -= 1
                if braced < 0: return False
        return braced == 0




n = 2
counter = 0
braces = (['{','}','[',']','(',')'],['{','[','}',']'])
while (counter < n):
    if (balanced(braces[counter])):
        print('YES')
    else:
        print('NO')

    counter = counter + 1


