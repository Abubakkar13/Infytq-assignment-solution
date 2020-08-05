'''
Assume that a poem is given. Write the regular expressions for the following:

Print how many times the letter 'v' appears in the poem.

Remove all the newlines from the poem and print the poem in a single line.
If a word has 'ch' or 'co', replace it with 'Ch' or 'Co'.

If the pattern has characters 'ai' or 'hi', replace the next three characters
with *\*.

Test your code by using the given sample inputs.
Verify your code by using the 2nd sample input(highlighted) given below:

'''

#PF-Assgn-53
#This verification is based on string match.
import re
poem='''
If I can stop one heart from breaking,
I shall not live in vain;
If I can ease one life the aching,
Or cool one pain,
Or help one fainting robin
Unto his nest again,
I shall not live in vain.
'''

#Note: Triple quotes can be used to enclose Strings which has lines of text.

#Write your logic here for question 1
print(poem.count('v'))

print()
print(re.sub(r"\n", r" ", poem))

print()
print(re.sub(r"c(h|o)", r"C\1", poem))
#Write your regular expression 

print()
print(re.sub(r"(ai|hi).{3}", r"\1*\*", poem))
#Write your regular expression here for question 4)
