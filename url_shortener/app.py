import random
import string


class URLShortener():
    def __init__(self, url):
        self.url = url

    def shorten(self, num_length=3, char_length=3):
        letters = string.ascii_letters
        nums = string.digits

        letter_chars = ["".join(random.choice(letters))
                        for i in range(char_length)]
        num_chars = ["".join(random.choice(nums)) for i in range(num_length)]

        print(letter_chars + num_chars)


url = URLShortener(
    "https://www.freecodecamp.org/learn/coding-interview-prep/take-home-projects/build-a-roguelike-dungeon-crawler-game")

url.shorten()
