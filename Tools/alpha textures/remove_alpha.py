try:
    from PIL import Image
except ImportError:
	from pip._internal import main as pipmain
	pipmain(['install', 'pillow'])

try: 
	img = Image.open('BASE_remove_alpha.png').convert('RGBA')
except FileNotFoundError:
	img = Image.new("RGBA", (16,16), (0,0,0,0))

x, y = img.size

i = 0
j = 0

for i in range(0,x):
	for j in range(0,y):
		r, g, b, a = img.getpixel((i,j))
		a = 255
		img.putpixel((i,j),(r,g,b,a))

img.save('RESULT_remove_alpha.png')