"""
layer0 : image without transparency
layer1 : image with alpha channel (transparency)
"""

try:
    from PIL import Image
except ImportError:
	print("You need to install pillow, use those commands:\n> python3 -m pip install --upgrade pip\n> ython3 -m pip install --upgrade Pillow")
	print("Follow this tutorial if you don't know how to use commands: https://www.youtube.com/watch?v=Jey1GH8CERI")

try: 
	layer0 = Image.open('BASE_merge_alpha_layer0.png').convert('RGBA')
	layer1 = Image.open('BASE_merge_alpha_layer1.png').convert('RGBA')
except FileNotFoundError:
	layer0 = Image.new("RGBA", (16,16), (0,0,0,0))
	layer1 = Image.new("RGBA", (16,16), (0,0,0,0))

x0, y0 = layer0.size
x1, y1 = layer1.size

result = Image.new("RGBA", (x0,y0), (0,0,0,0))

if (x0 != x1 or y0 != y1): 
	print("You need to use images with same size")
else:
	for i in range(0,x0):
		for j in range(0,y0):
			r0, g0, b0, a0 = layer0.getpixel((i,j))
			r1, g1, b1, a1 = layer1.getpixel((i,j))

			a1 = 0

			# first opaque texture
			result.putpixel((i,j), (r0,g0,b0,a0))
			# then transparent texture
			result.putpixel((i,j), (r1,g1,b1,a0))

	result.save('RESULT_merge_alpha.png')