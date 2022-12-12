import re
import numpy as np


def gettagssequence(tagged_file):
    """ Read the contents of alice_tags.txt and store it in a list
of strings, where each string is the sequence of lower cased tags (after removing the <SEP>
special character) for one sentence"""
    # Read the content of alice_tags.txt and store it in a list of strings
    contents = open(tagged_file).read()  # read the file
    contents = re.sub(r'([\w]*)\<SEP\>', r"\1", contents, 0, re.MULTILINE) # remove <SEP>
    #contents = re.sub(r'\<SEP\>', r"", contents, 0, re.MULTILINE)
    contents = contents.lower() # lower case

    tags_sequences = contents.split("\n") # split the lines

    # Return the list of strings
    return tags_sequences


def getwordssequence(words_file):
    """Reads the contents of alice_words.txt, and stores them in
  a list of lists, where each inner list contains one word per line, lower cased. The separation
  between words is given by the special token <SEP>"""
    # Read the content of alice_words.txt using regex and store in the list of lists
    contents = open(words_file).read()

    lines = contents.split("\n")

    word_sequences = []

    for line in lines:

        arr = []

        for match in re.finditer(r"([\w$&+,:;=?@#|'.^*()%!\[\]<>\.-]*?)(?:\<SEP\>|\n|$)", line):
            group = match.group(1)
            if group:
                arr.append(group.lower())

        word_sequences.append(arr)

    # Return the list of lists of words
    return word_sequences


def find_positions(tags_sequences):
    """First, write a regular expression that captures the following requirement: a noun phrase is a sequence
of one or more nouns (which are denoted with the letter N) preceded by zero, one or more adjectives
(which are denoted with the letter J). (remember to handle changes in capitalization)
Then, use this regular expression to produce a list of lists of tuples, where each inner tuple contains
the start and end position (note that end position is non inclusive) of each noun phrase your regex
found. For example, for the third sentence, the corresponding list of tuples could be [(2, 3), (4, 5
)], because it found two different noun phrases (in the form of tuples)"""
    # regex = r"(?:[Jj][\w$&+,:;=?@#|'.^*()%!\[\]<>\.-]*?)*[Nn][\w$&+,:;=?@#|'.^*()%!\[\]<>\.-]*?"
    regex = r"(?:[Jj][\w$&+,:;=?@#|'.^*()%!\[\]<>\.-]*?(?:|\n|$))*[Nn][\w$&+,:;=?@#|'.^*()%!\[\]<>\.-]*?(?:|\n|$)"

    positions = []
    # Find the positions of the noun phrases
    for sequence in tags_sequences:
        matches = re.finditer(regex, sequence)
        positions.append([(match.start(), match.end()) for match in matches])
    return positions


def find_noun_phrases(input_word, matches_list, words_sequences):
    """With the matches_list produced in step 2, you can now query your list of sentences contained in
words_sequences for any noun phrase. In this final part, you implement a function find_noun_phrase
(input_word, matches_list, words_sequences) that takes as input one input word (a string), and
the variables matches_list and words_sequences, and prints all noun phrases containing that word
as well as the sentence number (starting counting from one, and not by zero, which would be the
default in Python) in which they appear, formatted like this: sentence_id:noun_phrase.
"""
    # Find the noun phrases containing the input word
    for i in range(len(matches_list)):
        for match in matches_list[i]:
            if input_word in words_sequences[i][match[0]:match[1]]:
                print(str(i + 1) + ":" +
                      " ".join(words_sequences[i][match[0]:match[1]]))


# To test your functions above, run the code below and compare your results with the example outputs below.
# Q3 Test Cases
if __name__ == '__main__':
    testcases = {'a': [1, 3],
                 'b': [(np.random.rand(3, 2), np.ones((3, 2)))],
                 'c': [(np.random.rand(3, 2), np.ones((3, 1)))]}
    print('\n-- Q3a testcases --')
    t = gettagssequence('alice_tags.txt')
    w = getwordssequence('alice_words.txt')
    for args in testcases['a']:
        print('words_sequences[:{}]:'.format(args), w[:args])
        print('tag_sequences[:{}]:'.format(args), t[:args])
    print(len(w[0]), len(t[0]))
    print('-----------')
    print('\n-- Q3b testcases --')
    m = find_positions(t)
    print(m[3])  # third sentence
    print('-----------')
    print('\n-- Q3c testcases --')
    find_noun_phrases('disappointment', m, w)
    print('-----------')


# Example Test Outputs
# -- Q3a testcases --
# words_sequences[:1]: [['[', 'alice', "'", 's', 'adventures', 'in', 'wonderland', 'by', 'lewis', 'carroll', '1865', ']']]
# tag_sequences[:1]: ['jnpnnininncn']
# words_sequences[:3]: [['[', 'alice', "'", 's', 'adventures', 'in', 'wonderland', 'by', 'lewis', 'carroll', '1865', ']'], ['chapter', 'i', '.'], ['down', 'the', 'rabbit', '-', 'hole']]
# tag_sequences[:3]: ['jnpnnininncn', 'np.', 'idn:n']
# 12 12
# -----------
#
# -- Q3b testcases --
#[(2, 3), (4, 5)]
# -----------
#
# -- Q3c testcases --
# 14:great disappointment
# -----------
