import random
import string


class URLShortener():
    def __init__(self, incoming_url):
        self.incoming_url = incoming_url

    def shorten(self, char_length=6):
        letters_and_nums = string.ascii_letters + string.digits

        final = ["".join(random.choice(letters_and_nums))
                 for i in range(char_length)]

        print("".join(final))


