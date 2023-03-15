import time

from pageObjects.SearchBravePage import SearchBing
from pageObjects.ResultBravePage import ResultBing


class TestSearch:
    def test_basic_bing_search(self, setup):
        self.driver = setup
        search_page = SearchBing(self.driver)
        result_page = ResultBing(self.driver)
        phrase = "dragon"

        # Given the Bing home page is displayed
        search_page.load()
        # When the user search for "dragon"
        search_page.search(phrase)
        # Then the search result title contains "dragon"
        time.sleep(5)
        assert phrase in result_page.title()
        # And the search result query is "dragon"
        assert phrase == result_page.search_input_value()
        # And the search result links pertain to "dragon"
        titles = result_page.result_link_titles()
        matches = [t for t in titles if phrase.lower() in t.lower()]
        assert len(matches) > 0
