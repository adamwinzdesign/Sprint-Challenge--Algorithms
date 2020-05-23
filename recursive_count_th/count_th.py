'''
Your function should take in a single parameter (a string `word`)
Your function should return a count of how many occurences of ***"th"*** occur within `word`. Case matters.
Your function must utilize recursion. It cannot contain any loops.
'''

# recursively split the word and check for 'th'

def count_th(word):
    
    if(len(word) < 2):
        return 0

    elif(word[0] + word[1] == 'th'):
        return 1 + count_th(word[2:])

    return count_th(word[1:])
