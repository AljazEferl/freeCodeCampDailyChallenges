#09/29/2025

'''
Given a sentence, return the longest word in the sentence.

Ignore periods (.) when determining word length.
If multiple words are ties for the longest, return the first one that occurs.
'''

def get_longest_word(sentence):
   
    words = sentence.split()
    longest = words[0]
    for w in words: 
        if len(w) > len(longest):
            longest = w
   
    final = longest.replace(".", "")      
    return final

print(get_longest_word("coding is fun"))
print(get_longest_word("Coding challenges are fun and educational."))
print(get_longest_word("This sentence has multiple long words."))

'''
1. get_longest_word("coding is fun") should return "coding".
2. get_longest_word("Coding challenges are fun and educational.") should return "educational".
3. get_longest_word("This sentence has multiple long words.") should return "sentence".
'''