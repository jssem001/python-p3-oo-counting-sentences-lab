#!/usr/bin/env python3
import re

class MyString:
  def __init__(self, value=""):
    self.value = value
  
  def test_value_string(self):
      if not isinstance(self.value, str):
        print("The value must be a string.")
    
  def is_sentence(self):
    sentence = self.value.endswith(".")
    return sentence
  
  def is_question(self):
    question = self.value.endswith("?")
    return question
  
  def is_exclamation(self):
    exclamation = self.value.endswith("!")
    return exclamation
  
  def count_sentences(self):
      return len(re.findall(r'[.!?]+', self.value))


  

# sample = MyString("sample sentence! Let's see if this works. Will it work?")
# print(sample.count_sentences())

