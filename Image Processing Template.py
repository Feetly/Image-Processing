import cv2
import glob

def view(img, name_of_window="",ns=0,ws=0):
	if ws is 1 : cv2.namedWindow(name_of_window, cv2.WINDOW_FULLSCREEN)
	elif ws is 2 : cv2.namedWindow(name_of_window, cv2.WND_PROP_FULLSCREEN)
	else : cv2.namedWindow(name_of_window, cv2.WINDOW_NORMAL)
	cv2.imshow(name_of_window, img)
	cv2.waitKey(ns*1000)
	cv2.destroyAllWindows()

def rgb(img):
	return (cv2.cvtColor(img, cv2.COLOR_BGR2RGB),"RBG Image")

def edge(img,i1=100,i2=100):
	return (cv2.Canny(img,i1,i2),"Edged Image")
	
def grey(img):
	return (cv2.cvtColor(img, cv2.COLOR_BGR2GRAY),"Grey Image")

def thres(img,t=128,h=255,l=0):
	return (cv2.threshold(cv2.cvtColor(img, cv2.COLOR_BGR2GRAY), t, h, l)[1], "Threshold Image")

def crop(img,y,h,x,w):
	return (img[y:y+h, x:x+w],"Cropped Image")
		
def scale(img,p):
	return (cv2.resize(img, (int(img.shape[1] * p / 100), int(img.shape[0] * p / 100)), interpolation = cv2.INTER_AREA),"Scaled Image")
    
def rotate(img,angle=0):
	return (cv2.warpAffine(img, cv2.getRotationMatrix2D((img.shape[1] // 2, img.shape[0] // 2), angle, 1.0), (img.shape[1], img.shape[0])), "Rotated Image")

def blurr(img,be=50):
	return (cv2.GaussianBlur(img, (be, be), w), "Blurred Image")

def rect(img,tl=(0,0),br=(0,0),c=(0,0,0),th=10):
	return (cv2.rectangle(img, tl, br, c, th), "Rectangled Image",crop(img,tl[1],br[1]-tl[1],tl[0],br[0]-tl[0]))

def line(img,p1=(0,0),p2=(0,0),c=(0,0,0),th=10):
	return (cv2.line(img, p1, p2, c, th), "Lined Image")
	
def txt(img,txt="",blp=(0,0),font=cv2.FONT_HERSHEY_SIMPLEX,fs=10,c=(0,0,0),th=10):
	return (cv2.putText(img, txt, blp,font, fs, c,th),"Texted Image")

def face(img):
	i=1
	faces = cv2.CascadeClassifier('haarcascade_frontalface_default.xml').detectMultiScale(cv2.cvtColor(img, cv2.COLOR_BGR2GRAY),scaleFactor= 1.1,minNeighbors= 5,minSize=(10, 10))
	for (x, y, w, h) in faces:
		c=crop(img,y,h,x,w)
		view(c[0],"Look Carefully?",3,2)
		g = raw_input("Do u think just showed image was a Face? (y/n) : ")
		if g is "y" :
			r=rect(img, (x, y), (x+w, y+h), (255, 255, 0), 2)
			eyes = cv2.CascadeClassifier('haarcascade_eye.xml').detectMultiScale(cv2.cvtColor(c[0], cv2.COLOR_BGR2GRAY),1.1,3)
			for (ex,ey,ew,eh) in eyes:
				cpy=c[0]
				rect(cpy,(ex,ey),(ex+ew,ey+eh),(0,255,0),2)
				view(cpy,"Look Carefully?",3,2)
				v = raw_input("Do u think just showed image was a eye? (y/n) : ")
				if v is "y" :
					cpy=c[0]
					rect(c[0],(ex,ey),(ex+ew,ey+eh),(0,255,0),1)				
			cv2.imwrite("Cropped_"+str(i)+".jpg", c[0])
			i+=1
	return r


images = [cv2.imread(file) for file in glob.glob("path/to/files/*.png")]
img = images[0]

#view(img,"TXT")
#edges(img,100,200)
#rgb(img)
#grey(img)
#thres(img,150,200,10)
#crop(img,15,250,150,150)
#scale(img,75)
#rotate(img,90)
#blurr(img,be=50)
#line(img,(200,0),(400,200),(0,255,255),3)
#txt(img,"Hello",(0,300),cv2.FONT_HERSHEY_SIMPLEX,5,(0,255,255),5)
#r=rect(img,(200,0),(400,200),(0,255,255),3)
#view(r[0],r[1])
#view(r[2][0],r[2][1])
#f=face(img)
#view(f[0],"Finall",10,1)
#cv2.imwrite("Finally.jpg",f[0])
