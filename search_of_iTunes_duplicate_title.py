import glob
import os
import pandas as pd
from mutagen.id3 import ID3, TIT2

#検索にかける拡張子のリスト
EXT_LIST = [".mp3", ".m4a", ".wav"]
#ファイル精査を行うフォルダのパス
ORIGIN_PATH = "/Users/april_fool/Music/iTunes/iTunes Media/"
#曲名を収納するリスト
music_df = pd.DataFrame(columns=['Name', 'Album', 'Artist'])


""" データフレームを用いて同一のファイル名・拡張子を有する曲をprintする """
def search_duplicate_music(music_df):
    title_list = music_df["Name"].values.tolist()
    dupl_tf_list = music_df.duplicated(subset='Name').values.tolist()
    true_list = [i for i, x in enumerate(dupl_tf_list) if x == True]
    dupl_title_list = sorted(set([title_list[n] for n in true_list]))

    for title in dupl_title_list:
        print(music_df[music_df["Name"] == title])
        print('\n----------------------\n')
    return 0


""" データフレームを作るだけ 
    なお、生成時にはiTunesのフォルダ生成機能が ~/Artist/Album/Music_title.mp4 となる仕様を用いています。 """
def build_df():
    music_df = pd.DataFrame(columns=['Name', 'Album', 'Artist'])
    for filename in glob.glob(ORIGIN_PATH+"**", recursive=True):
        if os.path.splitext(filename)[1] in EXT_LIST:
            data = filename.split("/")
            music_df = music_df.append({'Name':data[-1], 'Album':data[-2], 'Artist':data[-3]}, ignore_index=True)
    print(len(music_df), "個の曲を感知。\n")
    return music_df


""" 全てのファイルの所得、ファイルの端子の分別 """
def search_extension(EXT_LIST):
    new_ext_list = []
    for filename in glob.glob(ORIGIN_PATH+"**", recursive=True):
        if os.path.isfile(filename):
            if not (os.path.splitext(filename)[1] in EXT_LIST) and (os.path.splitext(filename)[1] in new_ext_list):
                new_ext_list.append(os.path.splitext(filename)[1])
    print("EXT_LISTに含まれていない拡張子は", new_ext_list, "の通りとなります。")
    print("ちなみに、EXT_LISTは", new_ext_list, "の通りとなります。")
    print("いかがでしたか？")


if __name__ == '__main__':
    print(ORIGIN_PATH, " 直下のファイルを全精査します...\n")
    
    #拡張子について調べたいなら。
    #search_extension(EXT_LIST)
    
    music_df = build_df()
    dupl_df = search_duplicate_music(music_df)


""" 参考サイト
Pythonでmp3などのID3タグを編集するmutagenの使い方
    https://note.nkmk.me/python-mutagen-mp3-id3/
        孫引き - タグIDについての公式ドキュメント
            https://id3.org/id3v2.4.0-frames
Pythonで条件を満たすパスの一覧を再帰的に取得するglobの使い方
    https://note.nkmk.me/python-glob-usage/
ID3 - Mutagen
    https://mutagen.readthedocs.io/en/latest/api/id3.html
【Python】文字コードについてまとめる
    https://qiita.com/chii-08/items/c7032c5b0bc5f8ea9156
Pythonリファレンス - 標準エンコーディング
    http://docs.daemon.ac/python/Python-Docs-2.5/lib/standard-encodings.html

https://code-examples.net/ja/q/63ca69

食べてたもの。
    https://www.meiji.co.jp/sweets/candy_gum/hilemon/
"""




""" 以下は残骸 """




""" リストが空なら文字列'null'を返し、タグがあるならUTFに変換したタグを返す """
"""
def judge_null_list(get_list):
    if get_list == []:
        return 'null'
    else:
        if 'UTF8'   in str(get_list):
            return #str(get_list[0])
        if 'UTF16'  in str(get_list):
            return #str(get_list[0])
        if 'LATIN1' in str(get_list):
            #print(get_list)
            return bytes(str(get_list[0]),'iso-8859-1')#.decode('utf-16', 'replace')
        print(get_list)
        print("だめです。")
"""

""" 全てのファイルの所得、必要な情報を抜き出し music_df に格納 """
"""
def old_file_wo_list_ni_butikomuyatu():
    for filename in glob.glob(ORIGIN_PATH+"**", recursive=True):
        if os.path.splitext(filename)[1] in EXT_LIST:
            #print(filename)
            tags = ID3(filename)
            #print(tags.pprint())
            #TIT2
                #TPE1
            #TALB
            #TCON
            print(judge_null_list(tags.getall('TIT2')))
            #s_blank.split()
            #music_df = music_df.append({'Name':tags["title"], 'Artist':tags["artist"], 'Album':tags["album"]}, ignore_index=True)
#tags = ID3("/Users/april_fool/Music/iTunes/iTunes Media/Media.localized/Music/茶太/空/03 神様 -カイロス-.m4a")
#music_df = music_df.append({'Name':tags["title"], 'Artist':tags["artist"], 'Album':tags["album"]}, ignore_index=True)
print(music_df)
"""