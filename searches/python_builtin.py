"""
This is the builtin python search.
"""
from searches.search import Search

class BuiltinSearch(Search):

    def load_data(self, filename):
        with open(filename, "r") as readfile:
            self.data = readfile.read()

    def search(self, term):
        return self.data.find(term)
