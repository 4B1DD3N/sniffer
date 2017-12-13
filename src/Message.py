from termcolor import colored


class Message:
    def __init__(self):
        pass

    def info(self, text):
        print colored(text, 'green')

    def info_space(self, text):
        delimiter = '_' * len(text)
        print '\n%s\n%s\n%s\n' % (delimiter, text, delimiter)

    def info_raw(self, text):
        return raw_input(colored(text, 'green'))
