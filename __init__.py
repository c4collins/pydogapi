from urllib import request as urlrequest, parse as urlparse
import json


class DogAPI(object):
    base_domain = "https://dog.ceo/"
    api_route = "/api/"

    def list(self):
        return self._api_request("breeds/list")

    def list_images(self, breed, subbreed=None):
        if subbreed is None:
            return self._api_request("breed/{}/images".format(breed))
        else:
            return self._api_request("breed/{}/{}/images".format(breed, subbreed))

    def random(self, breed=None, subbreed=None):
        if breed is None:
            return self._api_request("breeds/image/random".format(breed))
        if subbreed is None:
            return self._api_request("breed/{}/images/random".format(breed))
        else:
            return self._api_request("breed/{}/{}/images/random".format(breed, subbreed))

    def _build_url(self, endpoint=""):
        api = urlparse.urljoin(self.base_domain, self.api_route)
        return urlparse.urljoin(api, endpoint)

    def _api_request(self, endpoint):
        # print(self._build_url(endpoint)) # Useful for debugging, but not enough to implement a logger
        return json.loads(urlrequest.urlopen(
            self._build_url(endpoint)
        ).read().decode("utf-8"))

if __name__ == "__main__":
    from pprint import pprint
    from random import choice

    dogapi = DogAPI()
    breeds = dogapi.list()['message']
    pprint(dogapi.random(choice(breeds)))
    pprint(dogapi.list_images(choice(breeds)))
    pprint(dogapi.random())
