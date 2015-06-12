# ex49 parser

class ParserError(Exception):
    pass

class Sentence(object):

    def __init__(self, subject, verb, obj):
        # remember we take ('noun','princess') tuples and convert them
        self.subject = subject[1]
        self.verb = verb[1]
        self.obj = obj[1]

""" 'peek' function peeks at a list of words and return what type of word
it is."""
def peek(word_list):
    if word_list:
	word = word_list[0]
	return word[0]
    else:
	return None

""" 'match' function confirms that the expected word is the right type, 
and returns the word.""" 
def match(word_list, expecting):
    if word_list:
	word = word_list.pop(0)

	if word[0] == expecting:
	    return word
	else:
	    return None
    else:
	return None

""" 'skip' function skips as any words of the type it finds."""
def skip(word_list, word_type):
    while peek(word_list) == word_type:
	match(word_list, word_type)

# 'parse_verb' function to handle parsing a verb.
def parse_verb(word_list):
    skip(word_list, 'stop')

    if peek(word_list) == 'verb':
	return match(word_list, 'verb')
    else:
	raise ParserError("Expected a verb next.")

# 'parse_object' function to handle parsing an object.
def parse_object(word_list):
    skip(word_list, 'stop')
    next_word = peek(word_list)

    if next_word == 'noun':
	return match(word_list, 'noun')
    elif next_word == 'direction':
	return match(word_list, 'direction')
    else:
	raise ParserError("Expected a noun or direction next.")

# 'parse_subject' function to handle parsing a subject
def parse_subject(word_list):
    skip(word_list, 'stop')
    next_word = peek(word_list)

    if next_word == 'noun':
	return match(word_list, 'noun')
    elif next_word == 'verb':
	return ('noun', 'player')
    else:
	raise ParserError("Expected a verb next.")


def parse_sentence(word_list):
    subj = parse_subject(word_list)
    verb = parse_verb(word_list)
    obj = parse_object(word_list)

    return Sentence(subj, verb, obj)
