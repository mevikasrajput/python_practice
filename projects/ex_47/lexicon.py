def match(word_list, excepting):
    if word_list:
        word = word_list.pop(0)

        if word[0] == excepting:
            return word
        else:
            return None

    else:
        return None

def skip(word_list, word_type):
    while peek(word_list) == word_type:
        match(word_list, word_type)


class ParserError(Exception):
    pass

class subject(object):
    def __init__(self, subject, obj, verb):
        self.subject = subject[1]
        self.object = obj[1]
        self.verb = verb[1]


def peek(word_list):
    if word_list:
        word = word_list(0)
        return word(0)
    else:
        return None


def match(word_list, excepting):
    if word_list:
        word = word_list.pop(0)

        if word[0] == excepting:
            return word
        else:
            return None
    else:
        return None

def skip(word_list, word_type):
    while peek(word_list) == word_type:
        match(word_list, word_type)

def parse_word(word_list):
    skip(word_list, 'stop')

    if peek(word_list) == 'verb':
        match(word_list, 'verb')
    else:
        raise ParserError ("ecpected a verb next")

def parse_object(word_list):
    skip(word_list, 'stop')
    next = peek(word_list)

    if next == 'noun':
        return match(word_list, 'noun')

    if next == 'direction':
        return match(word_list, 'direction')
    
    else:
        raise ParserError ("Expected a noun or direction next")

def parse_sub(word_list):
    verb = parse_verb(word_list)
    obj = parse_obj(word_list)

    return sentence(sub, verb, obj)

def parse_sentence(word_list):
    skip(word_list, 'stop')

    start = peek(word_list)
    
    if start == 'noun':
        subj = match(word_list, 'noun')
        return parse_sub(word_list, subj)
    elif start == 'verb':
        return parse_sub(word_list,('noun', 'player'))
    else:
        raise ParserError("must start subj, obj not verb")






