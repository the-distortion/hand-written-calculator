import numpy as np
from PIL import Image

def imgToArr(img):
	img = img.convert(dither='1').resize((28,28),resample=Image.LANCZOS)
	c=0;
	pxl=[[0]*28 for _ in range(28)]
	for i in img.getdata():
		pxl[c//28][c%28]=int(sum(i)<200)
		c+=1
	pxl = np.array([pxl])
	return pxl