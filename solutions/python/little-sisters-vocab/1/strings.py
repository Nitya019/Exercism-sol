"""Functions for creating, transforming, and adding prefixes to strings."""


def add_prefix_un(word):
    """Take the given word and add the 'un' prefix.

    Parameters:
        word (str): The root word.

    Returns:
        str: Root word prepended with 'un'.
    """

    return "un"+word


def make_word_groups(vocab_words):

    prefix = vocab_words[0]

    words = [prefix]

    for word in vocab_words[1:]:
        words.append(prefix + word)

    return " :: ".join(words)
    

def remove_suffix_ness(word):
    """Remove the suffix from the word while keeping spelling in mind.

    Parameters:
        word (str): Word to remove suffix from.

    Returns:
        str: Word with suffix removed & spelling adjusted.

    Examples:
        >>> remove_suffix_ness('heaviness')
        'heavy'

        >>> remove_suffix_ness('sadness')
        'sad'

    """
    
    remove = word[:-4]
    if remove[-1] == "i":
        return remove.replace("i","y")
    else:
        return remove

def adjective_to_verb(sentence, index):
    """Change the adjective within the sentence to a verb.

    Parameters:
        sentence (str): The word used in a sentence as an adjective.
        index (int): Index of the adjective to remove and transform.

    Returns:
        str: The extracted adjective in verb form.

    Examples:
        >>> adjective_to_verb('It got dark as the sun set.', 2)
        'darken'

        >>> adjective_to_verb('The ink stains her fingers black.', -1)
        'blacken'

    """

    adjective = sentence.split()[index]
    if adjective.endswith("."):
      return adjective[:-1]+"en"
    else:
      return adjective+"en"
