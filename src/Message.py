from termcolor import colored


class Message:
    config = None

    def __init__(self, config=None):
        if config is not None:
            self.config = config

    def config_empty(self):
        return len(self.config) == 0

    def config_next_command(self):
        command = self.config[0]

        del self.config[0]

        return command

    def info(self, text):
        print colored(text, 'green')

    def info_space(self, text):
        delimiter = '_' * len(text)
        print '\n%s\n%s\n%s\n' % (delimiter, text, delimiter)

    def info_raw(self, text):
        if not self.config_empty():
            command = self.config_next_command()
            self.info(colored(text, 'green') + command)
            return command
        else:
            return raw_input(colored(text, 'green'))
