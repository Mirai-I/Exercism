import re
def parse(markdown):
    markdown = re.sub(r'__([^\n]+?)__', r'<strong>\1</strong>',markdown)
# +? -> できるだけ最小でmatchしたものを返す
# \1 -> 参照する方法らしい　re.sub() の repl 引数へ渡される文字列中
    markdown = re.sub(r'_([^\n]+?)_', r'<em>\1</em>',markdown)
# これは全くわからない
    markdown = re.sub(r'^\* (.*?$)', r'<li>\1</li>', markdown, flags=re.M)
# 改行後の*についての変換かと，
# .*? -> なるべく少ない文字をマッチする
# $ -> 文字列の最後
    markdown = re.sub(r'(<li>.*</li>)', r'<ul>\1</ul>', markdown, flags=re.S)
# re.S -> "."を改行含むあらゆる文字にマッチさせる
    for i in range(6, 0, -1):
        markdown = re.sub(r'^{} (.*?$)'.format('#' * i), r'<h{0}>\1</h{0}>'.format(i), markdown, flags=re.M)

# ？！->正規表現が文字列の現在位置にマッチ しなかった 場合に成功
    markdown = re.sub(r'^(?!<[hlu])(.*?$)', r'<p>\1</p>', markdown, flags=re.M)

    markdown = re.sub(r'\n', '', markdown)

    return markdown
