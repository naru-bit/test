import os
b=[]
for curDir, dirs, files in os.walk("./cal"):
    print('===================')
    print("現在のディレクトリ: " + curDir)
    print("内包するディレクトリ: " + ", ".join(dirs))
    print("内包するファイル: " + ", ".join(files))

b=os.walk("./cal")

print(b)