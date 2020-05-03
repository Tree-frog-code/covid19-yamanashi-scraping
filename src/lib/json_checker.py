
import json


class JsonChecker:
    def __init__(self):
        pass

    def read_json(self, path):
        with open(path, 'r', encoding='utf-8') as f:
            data = json.load(f)
        return data

    def exclude_date_key(self, obj):
        return_obj = {}
        for key in obj.keys():
            print(key)
            if key != 'lastUpdate' and key != 'date':
                if isinstance(obj[key], dict):
                    tmp = self.exclude_date_key(obj[key])
                else:
                    tmp = obj[key]
                return_obj[key] = tmp
        return return_obj

    def check_list_count(self, input1, input2, key):
        return len(input1[key]['data']) == len(input2[key]['data'])

    def check_nonzero_max(self, before, after, key):
        before_nonzero = list(
            filter(lambda x: x['小計'] != 0, before[key]['data']))
        after_nonzero = list(
            filter(lambda x: x['小計'] != 0, after[key]['data']))
        before_max = max(before_nonzero, key=lambda x: x['日付'])
        after_max = max(after_nonzero, key=lambda x: x['日付'])

        return before_max['日付'] == after_max['日付'] and before_max['小計'] == after_max['小計']
