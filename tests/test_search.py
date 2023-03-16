import time

import pytest

from pageObjects.SearchBravePage import SearchBing
from pageObjects.ResultBravePage import ResultBing


class TestSearch:
    @pytest.mark.parametrize('phrase', ['go', 'java', 'c#'])
    def test_basic_bing_search(self, browser, phrase):
        search_page = SearchBing(browser)
        result_page = ResultBing(browser)

        # Given the Brave home page is displayed
        search_page.load()
        # When the user search for "dragon"
        search_page.search(phrase)
        # Then the search result query is "dragon"
        assert phrase == result_page.search_input_value()
        # And the search result links pertain to "dragon"
        titles = result_page.result_link_titles()
        matches = [t for t in titles if phrase.lower() in t.lower()]
        assert len(matches) > 0
        # Then the search result title contains "dragon"
        assert phrase in result_page.title()
