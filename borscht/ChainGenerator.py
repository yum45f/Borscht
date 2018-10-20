import MeCab
import json
import re
from collections import defaultdict


class ChainGenerator(object):
  """
  マルコフ連鎖に用いるチェーン(連鎖)を生成し、必要があれば JSON形式で出力・保存できるクラスです。

  Attributes
  ----------
  text : str
    チェーン生成の元になる文。
  tagger : MeCab.Tagger
    形態素解析に用いる Tagger オブジェクト。
  chain : dict
    マルコフ連鎖に用いるチェーンが格納された辞書型配列。
  """

  BEGIN = "BOS"
  END = "EOS"

  def __init__(self, text):
    """
    初期化メソッド

    Parameters
    ----------
    text : str
      チェーンを生成するための文章
    """

    self.text = text
    self.tagger = MeCab.Tagger()

    self.chain = self.generate_chain()


  def generate_chain(self):
    """
    マルコフ連鎖に用いるチェーンを生成します。

    Returns
    -------
    chain : dict
        マルコフ連載に用いるチェーン。
        key: 3階マルコフ用の3つ組 val: 出現回数
    """

    sentences = self.splitting_text(self.text)

    chain = defaultdict(int)

    for sentence in sentences:
      morphemes = self.morphological_analysis(sentence)
      triplets = self.generate_triplet_block(morphemes)

      for (triplet, n) in triplets.items():
        chain[triplet] += n

    return chain

  def splitting_text(self, text):
    """
    引数に渡された長めの文章を一文ずつに分割します。

    Parameters
    ----------
    text : str
      解析する文。

    Returns
    -------
    sentences : list of str
      分割された一文ずつのリスト。
    """

    text = re.sub(r"(。|．|\.|！|!|？|\?)", r"\1\n", text)
    sentences = text.splitlines()
    sentences = [sentence.strip() for sentence in sentences]

    for index, item in enumerate(sentences):
      if re.search(r"@|#", item):
        del sentences[index]

    return sentences



  def morphological_analysis(self, sentence):
    """
    引数に渡された一文の形態素解析をします。

    Parameters
    ----------
    sentence : str
      解析する文。

    Returns
    -------
    morphemes : list of str
      形態素で分割された結果のリスト。
    """

    tagger = self.tagger
    tagger.parse('')
    
    morphemes = []
    sentence = sentence
    node = self.tagger.parseToNode(sentence)
    while node:
        if node.posid != 0:
            morpheme = node.surface
            morphemes.append(morpheme)
        node = node.next
    return morphemes

  def generate_triplet_block(self, morphemes):
    """
    引数で渡された形態素の配列から、形態素毎の3つ組を生成し、
    出現回数など、チェーンの生成に必要な情報を合わせたブロックを返します。

    Parameters
    ----------
    morphemes : list of str
      形態素配列。3つ以上の形態素が含まれている場合のみ有効。

    Returns
    -------
    triplet_blocks : dict
      3つ組とその出現回数が格納されたブロックの辞書型配列。
      引数に渡された形態素の数自体が3つ以下の場合は空の辞書型配列が渡されます。
      key: 3つ組 (tuple) val: 出現回数 (int)
    """

    # 形態素の 3つ組が作れない場合 = 形態素の数自体が3つ以下の場合は実行しない
    if len(morphemes) < 3:
      return {}

    triplet_blocks = defaultdict(int)

    # BOS を追加
    triplet = (ChainGenerator.BEGIN , morphemes[0], morphemes[1])
    triplet_blocks[triplet] = 1

    for i in range(len(morphemes)-2):
      triplet = tuple(morphemes[i:i+3])
      triplet_blocks[triplet] += 1

    # EOS を追加
    triplet = (morphemes[-2], morphemes[-1], ChainGenerator.END)
    triplet_blocks[triplet] = 1

    return triplet_blocks

  def dump(self):
    chain_data = []
    try:
        with open('chain.json', 'r', encoding="utf8", errors='ignore') as f:
            chain_data = json.load(f)
    except FileNotFoundError:
      pass

    for (triplet, num) in self.chain.items():
      chain_data.append([triplet[0], triplet[1], triplet[2], num])

    with open('chain.json', 'w') as f:
      json.dump(chain_data, f, indent=4, ensure_ascii=False)

    with open('tweets.txt', 'w') as f:
      f.write("")
