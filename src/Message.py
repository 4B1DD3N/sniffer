from termcolor import colored


class Message:
    def __init__(self):
        pass

    def info(self, text):
        print colored(text, 'blue')

    def info_raw(self, text):
        return raw_input(colored(text, 'blue'))