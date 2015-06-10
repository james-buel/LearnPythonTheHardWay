def convert_number(s):
    try:
        return int(s)
    except ValueError:
        return None

def scan(input):
    """
    Takes an input string, and for each word in the sentence,
    append to a list of tuples like ('<TYPE>', '<WORD>')
    """
    directions = ['north', 'south', 'east', 'west', \
    'down', 'up', 'left', 'right', 'back']
    verbs = ['go', 'stop', 'kill', 'eat']
    stop_words = ['the', 'in', 'of', 'from', 'at', 'it']
    nouns = ['door', 'bear', 'princess', 'cabinet']
    
    output = []
    words = input.strip().split()
    
    for word in words: 
        word_l = word.lower() #lower case for comparison
        if word_l in directions:
            output.append(('direction', word))
        elif word_l in verbs:
            output.append(('verb', word))
        elif word_l in stop_words:
            output.append(('stop', word))
        elif word_l in nouns:
            output.append(('noun', word))
        else: #at this point, it is either a number, or an error
            number = convert_number(word_l)
            if number: #if conversion worked
                output.append(('number', number))
            else:
                output.append(('error', word))
    return output