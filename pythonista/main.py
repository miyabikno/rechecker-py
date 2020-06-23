# coding: utf-8

from __future__ import division
import ui
import clipboard
from console import hud_alert
import re


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


def check_re_match(sender):
	'@type sender: ui.Button'
	# Get the button's title for the following logic:
	name = sender.name
	
	if name == 'check':
		pattern = sender.superview['pattern'].text
		check_text = sender.superview['text'].text
		
		result = sender.superview['result']
		
		checker = ReChecker(pattern, check_text)
		checker.check_match()

		# パラメータ不正
		if checker.result == 'ng':
			output = '結果:パターンの記述が不正です'
		# パラメータをまとめる
		elif checker.result is not None:
			output = checker.summarize_result()
		else:
			output = '結果:一致しませんでした'
		
		result.text = output
		
def append_symbol(sender):
	pattern = sender.superview['pattern'].text
	t = sender.title
	sender.superview['pattern'].text = pattern + t

def copy_action(sender):
	'@type sender: ui.Button'
	pattern = sender.superview['pattern'].text
	
	clipboard.set(pattern)
	hud_alert('コピーしました')


v = ui.load_view('rechecker')

if min(ui.get_screen_size()) >= 768:
	# iPad
	v.frame = (0, 0, 430, 700)
	v.present('sheet')
else:
	# iPhone
	v.present(orientations=['portrait'])

