#!/usr/bin/env python3
import sys

class MyString:
    def __init__(self, value=""):
        """
        Initialize MyString, ensuring value is a string.
        """
        if not isinstance(value, str):
            raise TypeError(" The initial value must be a string")
        self._value = value

    @property
    def value(self):
        return self._value
    
    @value.setter
    def value(self, new_value):
        if not isinstance(new_value, str):
          
            print("The value must be a string.") 
        else:
            self._value = new_value
    
    def is_sentence(self):
        """
        Returns True if the value ends in a period (.).
        """
        return self._value.endswith('.')
    
    def is_question(self):
        """
        Returns True if the value ends in a question mark (?).
        """
        return self._value.endswith('?')
    
    def is_exclamation(self):
        """
        Returns True if the value ends in an exclamation mark (!).
        """
        return self._value.endswith('!')
    
    def count_sentences(self):
        """
        Counts the number of "sentences" defined as segments ending in a period (.), question mark (?), or exclamation mark (!).
        """
        text = self._value.strip()
        if not text:
            return 0
        
        # 1. Pad the punctuation with a space to handle cases where 
        # punctuation is immediately followed by a non-space character (e.g., in a complex contraction)
        # and to simplify splitting.
        temp_text = text.replace('!', ' !').replace('?', ' ?').replace('.', ' .')
        
        # 2. Split the string by spaces to get words and punctuation marks separately
        words_and_marks = temp_text.split()
        
        sentence_count = 0
        
        # 3. Iterate through the fragments and count sentence enders
        for fragment in words_and_marks:
            # Check if the fragment is one of the sentence-ending punctuation marks
            if fragment in ['.', '?', '!']:
                # This ensures we count a 'sentence' only once per ending group.
                if sentence_count == 0 or words_and_marks[words_and_marks.index(fragment) - 1] not in ['.', '?', '!']:
                    sentence_count += 1

        # 1. Replace all delimiters with a single, unique character that won't appear in the text (e.g., '@')
        normalized_text = self._value.replace('!', '@').replace('?', '@').replace('.', '@')
        
        # 2. Split by the unique character. This list will contain potential sentence fragments.
        fragments = normalized_text.split('@')
        
        # 3. Count non-empty fragments as sentences
        count = 0
        for fragment in fragments:
            if fragment.strip():
                count += 1
                
        # Handle the edge case where text ends without punctuation but contains text (e.g., "Hello world")

        return count
