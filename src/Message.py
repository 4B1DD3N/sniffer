from termcolor import colored


class Message:
    def __init__(self):
        pass

    def info(self, text):
        print colored(text, 'green')

    def info_raw(self, text):
        return raw_input(colored(text, 'green'))
