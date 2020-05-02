import re


class StringUtil:
    def __init__(self):
        super().__init__()
        self.exclude_char = r'県外'

    def exclude_outside(self, full_with_str):
        if re.search(self.exclude_char, full_with_str):
            return False
        else:
            return True

    def is_duplicate_data(self, number_char):
        check = re.search(r',', number_char)
        if check is None:
            return False, number_char
        else:
            tmp = re.sub(r'県|内|例|目', '', number_char)
            return True, list(map(lambda x: '県内{}例目'.format(x), tmp.split(',')))