#!/usr/bin/env python3
#Class MyString
#needs a value property
#value property verified its a string b4 assigning
#default value is empty string

class MyString:
  def __init__(self, name=""):
    self.name = name

  def get_name(self):
    return self._name
  
  def set_name(self, new_name):
    if type(new_name) == str:
      self._name = new_name
    print("The value must be a string.")

  #returns True if value ends with period else False
  def is_sentence(self):
    if self._name[-1] == ".":
      return True
    return False
  
  #ends with a question mark return True else False
  def is_question(self):
    if self._name[-1] == "?":
      return True
    return False
  
  def is_exclamation(self):
    if self._name[-1] == "!":
      return True
    return False
  
  #return the 
  def count_sentences(self):
    checker = ["?","!"]
    value = self._name
    for fullstop in checker:
      value = value.replace(fullstop, ".")
      
    print(value)

    # list_of_sentence = []
    # for broken_sentence in value.split("."):
    #   list_of_sentence.append(broken_sentence)
    number = 0
    list_of_sentence = [broken_sentence.strip() for broken_sentence in value.split(".")]
    for word_count in list_of_sentence:
      if word_count != "":
        number += 1
    return number
    



  name =property(get_name, set_name)


mystring = MyString()  
mystring.name = "This is a string! It has three sentences. Right?"
mystring.count_sentences()