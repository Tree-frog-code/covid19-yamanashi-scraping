import re


class TextParser:
    def __init__(self):
        self.pattern = r'年代|性別|退院|居住地'

    def text2dict(self, target_number: str, text_file_path: str) -> dict:
        book_mark = re.sub(r'県内', '', target_number)
        data_dict = {}

        with open(text_file_path, 'rt', encoding='utf-8') as input_file:
            read_flg = True
            texts = [s.strip() for s in input_file.readlines()]
            for text in texts:
                # numberで返される'n例目'以降の文字列を読み込む
                if read_flg:
                    check = re.search(book_mark, text)
                    # print("book_mark:{} check:{} text:{}".format(
                    #     book_mark, check, text))
                    if check is None:
                        continue
                    else:
                        # テキスト情報として'n-1,n例目'と記載されている部分を除外する
                        tmp_check = text[check.start()-1]
                        # print(tmp_check)
                        if re.match(r',|、|､', tmp_check) is None:
                            read_flg = False
                if text != '':
                    # 事前に':'を削除する
                    text = re.sub(r':|︓', '', text)
                    m = re.search(self.pattern, text)
                    # print(text)
                    if m is not None:
                        key = m.group()
                        value = text[m.end():]
                        # 年代の表記ゆれの統一（歳代→代）
                        if key == '年代':
                            value = re.sub(r'歳', '', value)
                        # keyが存在しない場合のみ代入する
                        if key not in data_dict:
                            data_dict[key] = value
                        continue
        return data_dict
