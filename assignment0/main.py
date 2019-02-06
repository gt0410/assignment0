import json
import random
import urllib.request

from typing import List, Dict, Any

url = "https://raw.githubusercontent.com/TrumpTracker/trumptracker.github.io/master/_data/data.json"


def download():
    """ This function downloads the json data from the url."""
    # TODO add code here
    r  = urllib.request.urlopen(url)
    s = r.read().decode('utf-8')
    return s


def extract_requests(text: str) -> List[Dict[str, Any]]:
    """
        This function turns the json data into a dict object and
        extracts and returns the array of promises.
    """
    # TODO add code here
   # json_data = download()
    dict_obj = json.loads(text)
    prom = dict_obj["promises"]
#    prom = np.array(dict_obj['promises'])
    return prom


def extract_titles(promises: List[Dict[str, Any]]) -> List[str]:
    """ Make a new array with just the titles. """
    # TODO add code here
   # promises = extract_requests()
    t = []
    for val in promises:
        f = val["title"]
        t.append(f)

    return t


def random_title(titles: List[str]) -> str:
    """ This function takes list of titles and returns one string at random. """
    # TODO add code here
   # titles = extract_titles()
    rand_title = random.choice(titles)
    #print(rand_title)
    return rand_title

#json_data = download()
#promises = extract_requests(json_data)
#titles = extract_titles(promises)
#random_title(titles)

              

