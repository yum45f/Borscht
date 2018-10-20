import random
import json

class TextGenerator(object):
  """
  Chainに基づいて文章を生成するクラスです。

  Attributes
  ----------
  chain : list
    マルコフ連鎖に用いるチェーンが格納された配列。
  """

  def __init__(self, chain_json_filepath):
    """
    初期化メソッド

    Parameters
    ----------
    chain_json_filepath : str
      チェーンデータが書かれている JSONファイルのパス。
    """
    self.chain = self.get_chain_data(chain_json_filepath)

  def get_chain_data(self, filepath):
    """
    チェーン情報を JSONファイルから取得します。

    Returns
    -------
    chain : list
      チェーンが格納された配列。
    """

    chain = []
    with open(filepath, 'r') as f:
      for raw in json.load(f):
        chain.append({'prefix1': raw[0], 'prefix2': raw[1], 'suffix': raw[2], 'freq': raw[3]})

    return chain

  def generate(self):
    """
    ランダムに一文を生成します。
    """

    morphemes = []

    first_triplet =  self.get_first_triplet()

    morphemes.append(first_triplet['prefix2'])
    morphemes.append(first_triplet['suffix'])

    while morphemes[-1] != "EOS":
      prefix1 = morphemes[-2]
      prefix2 = morphemes[-1]
      triplet = self.get_triplet(prefix1, prefix2)
      morphemes.append(triplet[2])


    result = "".join(morphemes[:-1])

    return result


  def get_triplet(self, prefix1, prefix2):
    """
    refix1とprefix2からsuffixをランダムに取得します。

    Parameters
    ----------
    prefix1 : str
      1つ目のprefix
    prefix2 : str
      2つ目のprefix
    """

    chain = []

    for triplet_block in self.chain:
      if triplet_block['prefix1'] == prefix1:
        chain.append(triplet_block)
      elif triplet_block['prefix2'] == prefix2:
        chain.append(triplet_block)

    triplet = self.get_probable_triplet(chain)

    return (triplet["prefix1"], triplet["prefix2"], triplet["suffix"])

  def get_first_triplet(self):
    """
    文章のはじまりの3つ組をランダムに取得します。

    Returns
    -------
    triplet : tuple
      文章のはじまりの3つ組が格納されたタプル。
    """

    chain = []

    for triplet_block in self.chain:
      if triplet_block['prefix1'] == "BOS":
        chain.append(triplet_block)


    triplet = self.get_probable_triplet(chain)

    return triplet


  def search_chain(self, *queries):
    """
    引数から指定された条件に合致するものをチェーンから取得します。

    Parameters
    ----------
    queries : tuple or list
      チェーンの検索条件。

    Returns
    -------
    result : list
      取得したチェーン情報の配列。
    """



  def get_probable_triplet(self, triplet_blocks):
    """
    引数として渡された三つ組の配列の中から確率的に一つ選び返します。

    Parameters
    ----------
    triplet_blocks : list
      複数の "3つ組とそれに関する情報" が格納された配列。

    Returns
    ------
    triplet : dict
      確率的に選んだ 3つ組
    """

    probability = []

    for (index, triplet_block) in enumerate(triplet_blocks):
      for i in range(triplet_block['freq']):
        probability.append(index)

    triplet_block_index = random.choice(probability)

    return triplet_blocks[triplet_block_index]
