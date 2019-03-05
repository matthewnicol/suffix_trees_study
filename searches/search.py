"""
This is the builtin python search.
"""
import time
import os
import sys
from pympler import asizeof

class bcolors:
    """ Print pretty things to the terminal
    """
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
    HIGHLIGHT = '\x1b[6;30;42m'
    HIGHLIGHT2 = '\33[45m'
    BLACKBG = '\033[40m'


class Search:
    """ 
    Base class that we will inherit from to implement a search
    Override functions:
        load_data
        search
    """
    def __init__(self, filename, *search_terms, output=True):
        self.output = output
        self.filename = filename
        self.searches = {}
        self.output_header()
        self._start_timing()
        self.load_data(f'./data/{filename}')
        self.load_time = self._stop_timing()
        self.output_loading_time()

        for search_term in search_terms:
            self._start_timing()
            search_pos = self.search(search_term)
            search_time = self._stop_timing()
            self.searches[search_term] = search_pos, search_time
            self.output_search_time(search_term, search_pos, search_time)

    def output_header(self):
        """ What kind of search is this? What is the filename? How big is it
        """
        if self.output:
            size = os.path.getsize(f'./data/{self.filename}')
            print(f'\n'
                  f'{bcolors.HIGHLIGHT2} {bcolors.BOLD}{self.__class__.__name__} {bcolors.ENDC} '
                  f'{bcolors.HIGHLIGHT} {self.filename} {bcolors.ENDC} '
                  f'{bcolors.HIGHLIGHT2} File Size: {size >> 20}MB {bcolors.ENDC} ')

    def output_loading_time(self):
        """ How long did it take us to load data into structures?
        """
        if self.output:
            print(
                    bcolors.FAIL, 
                    "{:.4f}".format(self.load_time), 
                    bcolors.ENDC, 
                    f'{bcolors.UNDERLINE}Load In File{bcolors.ENDC}', 
                    bcolors.HIGHLIGHT2,
                    f'In Memory: {asizeof.asizeof(self) >> 20}MB',
                    bcolors.ENDC
            )

    def output_search_time(self, search_term, search_pos, search_time):
        """ How long did it take us to search for 'search_term'
        """
        if self.output:
            print(
                bcolors.FAIL,
                "{:.4f}".format(search_time),
                bcolors.ENDC,
                f"{bcolors.UNDERLINE}Search{bcolors.ENDC} "
                    f"{bcolors.HIGHLIGHT}'{search_term[:30]}"
                    f"{'...' if len(search_term) > 29 else ''}'{bcolors.ENDC}",
                bcolors.BOLD,
                f'(Char: {search_pos})',
                bcolors.ENDC
            )

    def _start_timing(self):
        """ Log current time
        """
        self.checkpoint = time.time()

    def _stop_timing(self, tab=True):
        """ How long has passed since we started timing?
        """
        now = time.time()
        return round(now-self.checkpoint,4)


    def load_data(self, filename):
        """ Override me
        """
        raise NotImplemented()

    def search(self, term):
        """ Override me
        """
        raise NotImplemented()
