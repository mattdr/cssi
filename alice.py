#! /usr/bin/python
#
# A program to analyze the text of Alice in Wonderland and do
# interesting things with the data.

import string

def GetWordCounts(text_string):
    text_string = text_string.lower()
    text_string = text_string.replace("--", " ")
    words_list = text_string.split()
    words_dict = {}
    for word_string in words_list:
        word_string = word_string.strip(string.punctuation)
        if word_string in words_dict:
            words_dict[word_string] += 1
        else:
            words_dict[word_string] = 1
    return words_dict

def TopWords(words_dict):
    sorted_words_list = sorted(words_dict.keys(),
                               key=words_dict.get,
                               reverse=True)

    print ""
    print "Most common"
    for word_string in sorted_words_list[:10]:
        print word_string, "occurs",
        print words_dict[word_string], "times"

    print ""
    print "Least common"
    for word_string in sorted_words_list[-10:]:
        print word_string, "occurs",
        print words_dict[word_string], "times"


def main():
    # Open the file, read it into memory as a single string.
    with open('alice_in_wonderland.txt') as alice_file:
        alice_text = alice_file.read()

    words_count_dict = GetWordCounts(alice_text)
    unique_words = len(words_count_dict)

    print 'Unique words:', unique_words
    TopWords(words_count_dict)

if __name__ == '__main__':
    main()
