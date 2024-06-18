import os
import random

def get_subdirectories(parent_directory):
    subdirectories = []
    for root, dirs, _ in os.walk(parent_directory):
        for dir in dirs:
            subdirectories.append(os.path.join(root, dir))
    return subdirectories

def get_file_paths(directories):
    file_paths = set()  # 重複を避けるためにセットを使用
    for directory in directories:
        for root, _, files in os.walk(directory):
            for file in files:
                file_paths.add(os.path.join(root, file))
    return list(file_paths)

def shuffle_file_paths(file_paths, seed):
    random.seed(seed)
    random.shuffle(file_paths)
    return file_paths

# 親ディレクトリを指定
parent_directory = './cal'  # ここを適切な親ディレクトリパスに変更してください

# サブディレクトリを自動取得してファイルパスを取得
subdirectories = get_subdirectories(parent_directory)
print(subdirectories)

subdirectories.append(parent_directory)  # 親ディレクトリ自体も含める場合
file_paths = get_file_paths(subdirectories)

# ファイルパスをソートして順序を一定にする
file_paths.sort()

# ランダムシードを指定して並び替え
seed = 42  # 任意のシード値を指定
shuffled_paths = shuffle_file_paths(file_paths, seed)

# 結果を表示
for path in shuffled_paths:
    print(path)