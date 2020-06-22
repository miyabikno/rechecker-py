# rechecker-py
Pythonで作る正規表現チェッカーです。

## 使い方

### 直接実行する
引数に「正規表現のパターン」と「マッチするテキスト」を取ります。
pyhton python rechecker.py [pattern] [text]

◆実行例
pyhton python rechecker.py '^aaaa$' 'aaaa'

◆出力結果
結果:一致しました
入力したテキスト:aaaa
match[0]:aaaa

### モジュールを読み込む場合

from rechecker import ReChecker
checker = ReChecker('^aaaa$', 'aaaa')
checker.check_match()
checker.summarize_result()
```
from rechecker import ReChecker
checker = ReChecker('^aaaa$', 'aaaa')
checker.check_match()
checker.summarize_result()
```

## ブログでWeb版を公開中

[正規表現チェッカー for Python](https://miyabikno-jobs.com/tool-python-rechecker/)