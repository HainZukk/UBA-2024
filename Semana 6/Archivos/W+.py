archive = open("w+.txt" , "w+")
lines = archive.readlines()
print(lines)

archive.write("Pene\n")
archive.write("Fumanchu\n")
archive.write("Mamahuevo")
archive.close()
