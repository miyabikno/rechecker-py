import re
import sys


class ReChecker:
    # 初期設定
    def __init__(self, pattern, text):
        self.result = None
        self.pattern = pattern
        self.text = text

    # 正規表現のマッチ処理
    def check_match(self):
        try:
            # 正規表現チェック実行
            self.result = re.compile(self.pattern, flags=re.DOTALL).match(self.text)
        except:
            # パラメータ不正
            self.result = 'ng'

    # 結果をまとめる処理
    def summarize_result(self):
        output = '結果:一致しました\n'
        output += '入力したテキスト:%s\n' % self.text
        output += 'match[0]:%s\n' % self.result.group(0)
        for key, group in enumerate(self.result.groups()):
            # indexは1つずれる
            index = key + 1
            output += 'match[%s]:%s\n' % (index, group)
        return output


def main():
    # 引数のチェック
    if len(sys.argv) < 3:
        print('結果:引数が不足しています。')
        print('usage:python rechecker.py [pattern] [text]')
        exit()

    # 引数の受け取り
    checker = ReChecker(pattern=sys.argv[1], text=sys.argv[2])
    checker.check_match()

    # パラメータ不正
    if checker.result == 'ng':
        output = '結果:パターンの記述が不正です'
    # パラメータをまとめる
    elif checker.result is not None:
        output = checker.summarize_result()
    else:
        output = '結果:一致しませんでした'

    print(output)


if __name__ == "__main__":
    main()
