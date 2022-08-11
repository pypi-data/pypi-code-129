import logging

class BracketFormatter (logging.Formatter):

    blue = '\x1b[38;5;39m'
    yellow = '\x1b[38;5;226m'
    red = '\x1b[38;5;196m'
    bold_red = '\x1b[31;1m'
    reset = '\x1b[0m'

    def __init__(self):
        super().__init__()
        self.fmt = '%(message)s'
        self.FORMATS = {
            logging.DEBUG: '[.] ' + self.fmt,
            logging.INFO: '[' + self.blue + '+' + self.reset + '] ' + self.fmt,
            logging.WARNING: '[' + self.yellow + '!' + self.reset + '] ' + self.fmt,
            logging.ERROR: '[' + self.red + '*' + self.reset + '] ' + self.fmt,
            logging.CRITICAL: self.bold_red + '[*] ' + self.fmt + self.reset
        }

    def format(self, record):
        log_fmt = self.FORMATS.get(record.levelno)
        formatter = logging.Formatter(log_fmt)
        return formatter.format(record)

