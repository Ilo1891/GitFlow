def capital_letters(input_string):
  return input_string.upper()

def firstletters(sentence):
    '''
       Функция которая делает заглавные буквы в строке
       '''

    return ' '.join(word.capitalize() for word in sentence.split())