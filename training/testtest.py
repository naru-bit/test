import os
import random

def get_file_paths(parent_directory):
    file_paths = []
    for root, dir, files in os.walk(parent_directory):
        for file in files:
            file_paths.append(os.path.join(root, dir,file))
    return file_paths


def shuffle_file_paths(file_paths, seed):
    random.seed(seed)
    random.shuffle(file_paths)
    return file_paths

# 親ディレクトリを指定
parent_directory = './cal'  # ここを適切な親ディレクトリパスに変更してください




# ファイルパスを取得
file_paths = get_file_paths(parent_directory)

# ファイルパスをソートして順序を一定にする
file_paths.sort()

# ランダムシードを指定して並び替え
seed = 42  # 任意のシード値を指定
shuffled_paths = shuffle_file_paths(file_paths, seed)

# 結果を表示
for path in shuffled_paths:
    print(path)



