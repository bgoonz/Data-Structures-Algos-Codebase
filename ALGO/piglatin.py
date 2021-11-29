# A Pig Latin translator will move the first letter of a word to the last and append "ay" to the word
pyg = 'ay'
# input a word
original = raw_input('Enter a word:')
# if input is a string and is alphabet only
if len(original) > 0 and original.isalpha():
  word = original.lower()
  first = word[0]
  # formated, concatenate word and first letter with "ay"
  new_word = word + first + pyg
  # slice the input word after the first letter
  new_word = new_word[1:]
  print new_word
  