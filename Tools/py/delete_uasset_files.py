import os

def GetFileList(PATH):

	fileList = os.listdir(PATH)
	files = list()

	for entry in fileList:
		fullPath = os.path.join(PATH, entry)

		# If entry is a sub-directory, then get list of files from it
		if os.path.isdir(fullPath):
			files = files + GetFileList(fullPath)
		else:
			files.append(fullPath)

	return files

os.system('chcp 65001')
os.system('cls')

print("--------------------------------------")
print(" Searching & Removing .uasset files")
print("--------------------------------------")

path  = '..\\UE4Project\\Content\\'
count = 0
files = GetFileList(path)

filesFiltered = [ file for file in files if file.endswith(".uasset") ]


for file in filesFiltered:
	os.remove(file)
	count += 1
	print("\x1b[1m \x1b[33m Removed :",file,"\x1b[0m")


print("--------------------------------------")

if count != 0:
	if count == 1:
		print("\x1b[1m \x1b[32m Successfully removed 1 .uasset file \x1b[0m")
	else:
		print("\x1b[1m \x1b[32m Successfully .uasset file(s) removed: ",count,"\x1b[0m")
else:
	print("\x1b[1m \x1b[31m No files were found \x1b[0m")	

print("--------------------------------------")
