import pytest

import assignment0
from assignment0 import main


def test_download_sanity():
    assert main.download() is not None


def test_download_size():
    assert len(main.download()) == 135131
christangrant@testinstance:/hw1/cs5293sp19-assignment0$ cat tests/test_random.py 
import pytest

import assignment0
from assignment0 import main


def test_extract_request():
    text = main.download()
    promises = main.extract_requests(text)
    assert len(promises) == 174


title0 = "Propose a Constitutional Amendment to impose term limits on all members of Congress"
def test_extract_titles():
    text = main.download()
    promises = main.extract_requests(text)
    titles = main.extract_titles(promises) 

    assert titles[0] == title0


def test_random_title():
    text = main.download()
    promises = main.extract_requests(text)
    titles = main.extract_titles(promises) 
    randomtitle = main.random_title(titles)

    assert type(randomtitle) == str
    assert len(randomtitle) > 0
