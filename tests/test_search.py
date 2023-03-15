from pageObjects import SearchBingPage
from pageObjects import ResultBingPage


class TestSearch:
    def test_basic_bing_search(self, setup):
        self.driver = setup
        search_page = SearchBingPage(self.driver)
        result_page = ResultBingPage(self.driver)
        phrase = "panda"

        # Given the Bing home page is displayed
        search_page.load()
        # When the user search for "fenix"
        search_page.search(phrase)
        # Then the search result title contains "fenix"
        assert phrase in result_page.title()
        # And the search result query is "fenix"
        assert phrase == result_page.search_input_value()
        # And the search result links pertain to "fenix"
        titles = result_page.result_link_titles()
        matches = [t for t in titles if phrase.lower() in t.lower()]
        assert len(matches) > 0
