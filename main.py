import os, pygame
from pygame.locals import *
from PIL import Image
import tkinter as tk
import tkinter.messagebox as mb
from cursors import *
from img_process import *
import tensorflow as tf

def main():
	global calculation,white,black,screen
	flag = 1;count=1
	while flag:
		try:
			for ev in pygame.event.get():
				if ev.type == QUIT:flag = 0;break
				# clock.tick(200)

				px, py = pygame.mouse.get_pos()
				if pygame.mouse.get_pressed() == (1,0,0):
					pygame.draw.ellipse(screen, black, (px,py,18,18))
				elif pygame.mouse.get_pressed() == (0,0,1):
					screen.fill(white)

				if ev.type == pygame.KEYDOWN:
					if ev.key == pygame.K_PLUS or ev.key == pygame.K_KP_PLUS:
						print('+')
						pygame.image.save(screen, f"screenshot{count}.jpg")
						calculation.append(Image.open(f"screenshot{count}.jpg"))
						calculation.append('+')
						count+=1
						screen.fill(white)
						print(calculation)
					elif ev.key == pygame.K_MINUS or ev.key == pygame.K_KP_MINUS:
						print('-')
						pygame.image.save(screen, f"screenshot{count}.jpg")
						calculation.append(Image.open(f"screenshot{count}.jpg"))
						calculation.append('-')
						count+=1
						screen.fill(white)
						print(calculation)
					elif ev.key == pygame.K_ASTERISK or ev.key == pygame.K_KP_MULTIPLY:
						print('*')
						pygame.image.save(screen, f"screenshot{count}.jpg")
						calculation.append(Image.open(f"screenshot{count}.jpg"))
						calculation.append('*')
						count+=1
						screen.fill(white)
						print(calculation)
					elif ev.key == pygame.K_SLASH or ev.key == pygame.K_KP_DIVIDE:
						print('/')
						pygame.image.save(screen, f"screenshot{count}.jpg")
						calculation.append(Image.open(f"screenshot{count}.jpg"))
						calculation.append('/')
						count+=1
						screen.fill(white)
						print(calculation)
					elif ev.key == pygame.K_SPACE:
						pygame.image.save(screen, f"screenshot{count}.jpg")
						screen.fill(white)
						try:
							calculation.append(Image.open(f"screenshot{count}.jpg"))
						except Exception as x:pr(x,'lol46')
						count+=1
					elif ev.key == pygame.K_RETURN or pygame.K_KP_ENTER:
						pygame.image.save(screen, f"screenshot{count}.jpg")
						calculation.append(Image.open(f"screenshot{count}.jpg"))
						predict();
						flag = 0; break;
					else:print(ev.key)
				pygame.display.update()

		except Exception as ex:
			print(ex,'lol49');break
	pygame.quit()
	del calculation
	while count>0:
		os.remove(f"screenshot{count}.jpg")
		count-=1

def predict():
	global model
	print("Enter")
	st = []
	for i in calculation:
		if str(type(i))=="<class 'str'>":st.append(i)
		else:
			st.append(str( np.argmax(model.predict(imgToArr(i))) ))
	if not st[-1].isdigit(): st.append('0')
	st="".join(st)
	print(st)
	tk.Tk().withdraw()
	exec(f'print(mb.showinfo("Answer:","{st} = "+str("%.5f"%({st}))))')

tk.Tk().withdraw()
print(mb.showinfo('Instructions','      Welcome to Soham\'s Hand-written Calculator!\t\n\n1. Use your left-mouse to draw and right-mouse to undo\n2. Press SPACE to confirm drawing and draw next digits\n3. Press the operation keys (+-*/) after drawing the digits of the number\n4. Press ENTER to end, and show the result..yaay!!'))
calculation=[]
model = tf.keras.models.load_model('model.h5')
white = (255,255,255); black = (0,0,0)
pygame.init()
screen = pygame.display.set_mode((280,280))
pygame.display.set_caption("Drawing Pad")
setCursor()
screen.fill(white)
# clock = pygame.time.Clock()
main()