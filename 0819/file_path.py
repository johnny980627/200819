import os.path
if os.path.isfile("yee.txt"):
    print("存在")
    file = open("yee.txt","a")
    file.write("檔案存在")
else:
    print("不存在")
    file = open("yee.txt","w")
    file.write("新創建檔案")
file.close()
