# Python DogAPI

This library wraps [dog.ceo's DogAPI](https://dog.ceo/dog-api/)

## Functions

1. `list()` 
    - Returns an array of all the dog images from all the breeds
1. `list_images(breed[, subbreed])`
    - Returns an array of all the images from the breed,
    - if you also provide a subbredd (in addition to the breed) the list will only include images from that subbreed.
1. `random([breed][, subbreed])` 
    - Returns a random dog image from all the breeds if no parameters are passed.  
    - If a breed is provided it will return an array of all the images from the breed, 
    - and if you pass a subbreed (as well as a breed) it will return an array of all the images from the subbreed. 

## Usage

1. Create a dogapi object: `dogapi = DogAPI()`
1. Call a function: 
    1. `dogapi.list()`
    1. `dogapi.list_images()`
    1. `dogapi.list_images("cairn")`
    1. `dogapi.random()`
    1. `dogapi.random("boxer")`


## Simple Example Program

    from pprint import pprint
    from random import choice
    import DogAPI

    dogapi = DogAPI()
    breeds = dogapi.list()['message']
    pprint(dogapi.random(choice(breeds)))
    pprint(dogapi.list_images(choice(breeds)))
    pprint(dogapi.random())
