from dictionary.word_frequency import WordFrequency
from dictionary.base_dictionary import BaseDictionary
import bisect


# ------------------------------------------------------------------------
# This class is required TO BE IMPLEMENTED
# Array-based dictionary implementation
#
# __author__ = 'Son Hoang Dau'
# __copyright__ = 'Copyright 2022, RMIT University'
# ------------------------------------------------------------------------

class ArrayDictionary(BaseDictionary):

    def __init__(self):
        self.dictionary_data = []
        pass


    def build_dictionary(self, words_frequencies: [WordFrequency]):
        """
        construct the data structure to store nodes
        @param words_frequencies: list of (word, frequency) to be stored
        """

        # TO BE IMPLEMENTED
        self.dictionary_data = words_frequencies


    def search(self, word: str) -> int:
        """
        search for a word
        @param word: the word to be searched
        @return: frequency > 0 if found and 0 if NOT found
        """
        # TO BE IMPLEMENTED
        for entry in self.dictionary_data:
            if entry.word == word:
                return entry.frequency

        return 0

    def add_word_frequency(self, word_frequency: WordFrequency) -> bool:
        """
        add a word and its frequency to the dictionary
        @param word_frequency: (word, frequency) to be added
        :return: True whether succeeded, False when word is already in the dictionary
        """
        # TO BE IMPLEMENTED
        if not any(entry.word == word_frequency.word for entry in self.dictionary_data):
            self.dictionary_data.append(word_frequency)
            return True

        return False

    def delete_word(self, word: str) -> bool:
        """
        delete a word from the dictionary
        @param word: word to be deleted
        @return: whether succeeded, e.g. return False when point not found
        """
        # find the position of 'word' in the list, if exists, will be at idx-1
        # TO BE IMPLEMENTED
        for entry in self.dictionary_data:
            if entry.word == word:
                self.dictionary_data.remove(entry)
                return True

        return False


    def autocomplete(self, prefix_word: str) -> [WordFrequency]:
        """
        return a list of 3 most-frequent words in the dictionary that have 'prefix_word' as a prefix
        @param prefix_word: word to be autocompleted
        @return: a list (could be empty) of (at most) 3 most-frequent words with prefix 'prefix_word'
        """
        matching_words = [entry for entry in self.dictionary_data if entry.word.startswith(prefix_word)]
        matching_words.sort(key=lambda entry: entry.frequency, reverse=True)
        return matching_words[:3]
