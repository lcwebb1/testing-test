import pytest
import requests

url_ddg = "https://api.duckduckgo.com"

president_masterlist = {"Washington", "Adams", "Jefferson", "Madison", "Monroe",
                        "Jackson", "Buren", "Harrison", "Tyler", "Polk", "Taylor",
                        "Fillmore", "Pierce", "Buchanan", "Lincoln", "Johnson",
                        "Grant", "Hayes", "Garfield", "Arthur", "Cleveland", "Harrison",
                        "McKinley", "Roosevelt", "Taft", "Wilson", "Harding", "Coolidge",
                        "Hoover", "Truman", "Eisenhower", "Kennedy", "Johnson",
                        "Nixon", "Ford", "Carter", "Reagan", "Bush", "Clinton", "Obama",
                        "Trump", "Biden"}


def test_ddg0():

    resp = requests.get(url_ddg + "/?q=DuckDuckGo&format=json")

    rsp_data = resp.json()

    assert "DuckDuckGo" in rsp_data["Heading"]


# Tests for names of US presidents from set in related topics in ddg search result

def test_presidents():

    resp = requests.get(url_ddg + "/?q=presidents+of+the+united+states&format=json")

    rsp_data = resp.json()

    for x in president_masterlist:

        assert x in str(rsp_data["RelatedTopics"])
