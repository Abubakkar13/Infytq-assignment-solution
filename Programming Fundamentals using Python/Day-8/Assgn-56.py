'''
Write a python program that accepts a text and displays a string which contains the word with the largest frequency in the text and the frequency itself separated by a space.

 Rules:
   1. The word should have the largest frequency.
   2. In case multiple words have the same frequency, then choose the word that has the maximum length.
 Assumptions:
    The text has no special characters other than space.
    The text would begin with a word and there will be only a single space between the words.
Perform case insensitive string comparisons wherever necessary.
'''
#PF-Assgn-56

def max_frequency_word_counter(data):
    word_set = set(data.lower().split())
    temp_dict = dict()
    for word in word_set:
        frequency = data.lower().split().count(word)
        if str(frequency) in temp_dict.keys():
            if len(word) > len(temp_dict[str(frequency)]):
                temp_dict[str(frequency)] = word
        else:
            temp_dict.update({str(frequency):word})
    maximum = 0
    for count in temp_dict.keys():
        if int(count) > maximum:
            maximum = int(count)
    word, frequency = temp_dict[str(maximum)], maximum
    print(word, frequency)

    #start writing your code here
    #Populate the variables: word and frequency


    # Use the below given print statements to display the output
    # Also, do not modify them for verification to work
    #print(word,frequency)


#Provide different values for data and test your program.
data="Rain on the green grass and Rain on the tree"
max_frequency_word_counter(data)
