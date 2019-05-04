Borscht
====
**The Python Module of The Japanese sentence generator by Markov chain.**


## Description
The Python Module of The Japanese sentence generator by Markov chain.

Do you want to generate text by Markov chain?
It's quite easy! Just copy the example below.

## Requirement
If you want to run this module, please install these:

- Python 3.x
- MeCab - <http://taku910.github.io/mecab/>
- mecab-python3 (Python Module)

**Recommendation:**
We recommend that you use this MeCab dictionary, `mecab-ipadic-NEologd`

> **If you want detailed information about how to install MeCab and `mecab-ipadic-NEologd`,
please see this post. (written in Japanese):
<https://qiita.com/taroc/items/b9afd914432da08dafc8>**


## Example Usage

```python
# Import borscht.
import borscht as bor

# Text used for chain generation of Markov chain
text = """
　親譲りの無鉄砲で小供の時から損ばかりしている。小学校に居る時分学校の二階から飛び降りて一週間ほど腰を抜かした事がある。
なぜそんな無闇をしたと聞く人があるかも知れぬ。別段深い理由でもない。
新築の二階から首を出していたら、同級生の一人が冗談に、いくら威張っても、そこから飛び降りる事は出来まい。弱虫やーい。と囃したからである。
小使に負ぶさって帰って来た時、おやじが大きな眼をして二階ぐらいから飛び降りて腰を抜かす奴があるかと云ったから、この次は抜かさずに飛んで見せますと答えた。
　親類のものから西洋製のナイフを貰って奇麗な刃を日に翳して、友達に見せていたら、一人が光る事は光るが切れそうもないと云った。
切れぬ事があるか、何でも切ってみせると受け合った。そんなら君の指を切ってみろと注文したから、何だ指ぐらいこの通りだと右の手の親指の甲をはすに切り込んだ。
幸ナイフが小さいのと、親指の骨が堅かったので、今だに親指は手に付いている。しかし創痕は死ぬまで消えぬ。
　庭を東へ二十歩に行き尽すと、南上がりにいささかばかりの菜園があって、真中に栗の木が一本立っている。
これは命より大事な栗だ。実の熟する時分は起き抜けに背戸を出て落ちた奴を拾ってきて、学校で食う。
菜園の西側が山城屋という質屋の庭続きで、この質屋に勘太郎という十三四の倅が居た。
勘太郎は無論弱虫である。弱虫の癖に四つ目垣を乗りこえて、栗を盗みにくる。ある日の夕方折戸の蔭に隠れて、とうとう勘太郎を捕まえてやった。
その時勘太郎は逃げ路を失って、一生懸命に飛びかかってきた。向うは二つばかり年上である。
弱虫だが力は強い。鉢の開いた頭を、こっちの胸へ宛ててぐいぐい押した拍子に、勘太郎の頭がすべって、おれの袷の袖の中にはいった。
邪魔になって手が使えぬから、無暗に手を振ったら、袖の中にある勘太郎の頭が、右左へぐらぐら靡いた。
しまいに苦しがって袖の中から、おれの二の腕へ食い付いた。痛かったから勘太郎を垣根へ押しつけておいて、足搦をかけて向うへ倒してやった。
山城屋の地面は菜園より六尺がた低い。勘太郎は四つ目垣を半分崩して、自分の領分へ真逆様に落ちて、ぐうと云った。
勘太郎が落ちるときに、おれの袷の片袖がもげて、急に手が自由になった。その晩母が山城屋に詫びに行ったついでに袷の片袖も取り返して来た。
　この外いたずらは大分やった。大工の兼公と肴屋の角をつれて、茂作の人参畠をあらした事がある。人参の芽が出揃わぬ処へ藁が一面に敷いてあったから、
その上で三人が半日相撲をとりつづけに取ったら、人参がみんな踏みつぶされてしまった。古川の持っている田圃の井戸を埋めて尻を持ち込まれた事もある。
太い孟宗の節を抜いて、深く埋めた中から水が湧き出て、そこいらの稲にみずがかかる仕掛であった。
その時分はどんな仕掛か知らぬから、石や棒ちぎれをぎゅうぎゅう井戸の中へ挿し込んで、水が出なくなったのを見届けて、うちへ帰って飯を食っていたら、
古川が真赤になって怒鳴り込んで来た。たしか罰金を出して済んだようである。
"""
# 夏目漱石 「坊っちゃん」より

cg = bor.ChainGenerator(text) # Generate instance of class that generates chains
cg.dump("./chain.json") # Dump json file written about chains' info.
tg = bor.TextGenerator("./chain.json")
# Generate instance of class that generates sentence.

for i in range(10):
  sentence = tg.generate() # Generate sentence
  print(tg.generate())
```

## Installation
It's quite simple using pip command:

```bash
$ pip install borscht
```

## Contribution

1. Fork it (<https://github.com/yu-san-19/Borscht>)
2. Create your feature branch (`git checkout -b feature/<your-new-feature>`)
3. Commit your changes (`git commit -am 'Add some feature'`)
4. Push to the branch (`git push origin feature/<your-new-feature>`)
5. Create new Pull Request

## License

This repository licensed under the [Apache License, Version 2.0](https://github.com/yu-san-19/Borscht/blob/master/LICENSE).
Please see the [LICENSE](https://github.com/yu-san-19/Borscht/blob/master/LICENSE) file.

## Author

[YuSan19](https://github.com/yu-san-19) and other Contributors.
