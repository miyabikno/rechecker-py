# coding: utf-8

from __future__ import division
import ui
import clipboard
from console import hud_alert
from rechecker import ReChecker

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
	v.frame = (0, 0, 360, 400)
	v.present('sheet')
else:
	# iPhone
	v.present(orientations=['portrait'])

