file= open("E:\\myFile.txt",mode="a")
file.write("\nchecking ,OK")
file= open("E:\\myFile.txt",mode="r")
print(file.read())
file= open("E:\\myFile.txt",mode="w")
file.write("\nThis is wriiting comment!!!")
file= open("E:\\myFile.txt",mode="r")
print(file.read())

