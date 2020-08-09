'''
*	Script made by Juknum, Pilow is required
* 	info : this script is maybe not right optimized but it works 
'''

try:
    from PIL import Image
except ImportError:
	from pip._internal import main as pipmain
	pipmain(['install', 'pillow'])
	
import os

array = [ 
	'0001.png', '0002.png', '0003.png', '0004.png', '0005.png', '0006.png', '0007.png', '0008.png',
	'0009.png', '0010.png', '0011.png', '0012.png', '0013.png', '0014.png', '0015.png', '0016.png',
	'0017.png', '0018.png', '0019.png', '0020.png', '0021.png', '0022.png', '0023.png', '0024.png', 
	'0025.png', '0026.png', '0027.png', '0028.png', '0029.png', '0030.png', '0031.png', '0032.png', 
	'0033.png', '0034.png', '0035.png', '0036.png', '0037.png', '0038.png', '0039.png', '0040.png',
	'0041.png', '0042.png', '0043.png', '0044.png', '0045.png', '0046.png', '0047.png', '0048.png',
	'0049.png', '0050.png', '0051.png', '0052.png', '0053.png', '0054.png', '0055.png', '0056.png', 
	'0057.png', '0058.png', '0059.png'
]

def MergeCol(img1, img2):

	dst = Image.new('RGBA', (img1.width + img2.width, img1.height) )
	dst.paste(img1, (0,0))
	dst.paste(img2, (img1.width, 0))

	return dst

def MergeRow(img1, img2):
	dst = Image.new('RGBA', (img1.width, img1.height + img2.height) )
	dst.paste(img1, (0,0))
	dst.paste(img2, (0, img1.height))

	return dst

row = 0
col = 0
arrayIterater = 0
colIterater   = 0

while row != 8:
	while col != 7:
		
		if (col + 8*row) < 58:

			if col == 0 :
				img1 = Image.open(array[col + 8*row ])
				img2 = Image.open(array[col + 8*row +1])
			else:
				img1 = Image.open("tmp" + str(row) + ".png")
				img2 = Image.open(array[col + 8*row + 1])

			MergeCol(img1, img2).save("tmp" + str(row) + ".png")
		col += 1

	if row == 1:
		img1 = Image.open("tmp0.png")
		img2 = Image.open("tmp1.png")
		MergeRow(img1, img2).save("tmpA.png")
	elif row > 1:
		img1 = Image.open("tmpA.png")
		img2 = Image.open("tmp" + str(row) + ".png")
		MergeRow(img1, img2).save("tmpA.png")
	
	row += 1
	col = 0

img = Image.open("tmpA.png")
final = Image.new('RGBA', (2048,2048))
final.paste(img, (0,0))
final.save("loader.png")

for i in range(0,8):
	os.remove("tmp" + str(i) + ".png")
os.remove("tmpA.png")

print("Done")