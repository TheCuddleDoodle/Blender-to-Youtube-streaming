import os,sys,time
from threading import Thread

#installing updates



def first():
	time.sleep(2)
	os.system("unzip new.zip")	
	os.system("blender -b new/file.blend -x 1 -o //render -a")

#checking the availibity of files

def run():
	
	
	for x in range(1,9):
			if os.path.isfile("new/render000"+str(x)+".png"):
				os.system("cat new/render000"+str(x)+".png"+" "+">>"+" "+"image")
			else:
				t="xyz"
				while ( t != "True"):
					if os.path.isfile("new/render000"+str(x)+".png"):
						os.system("cat new/render000"+str(x)+".png"+" "+">>"+" "+"image")
						t="True"
					else:				
						time.sleep(2)
						sys.stdout.flush()

	for x in range(10,100):
			if os.path.isfile("new/render00"+str(x)+".png"):
				os.system("cat new/render00"+str(x)+".png"+" "+">>"+" "+"image")
			else:
				t="xyz"
				while ( t != "True"):
					if os.path.isfile("new/render00"+str(x)+".png"):
						os.system("cat new/render00"+str(x)+".png"+" "+">>"+" "+"image")
						t="True"
					else:				
						time.sleep(2)
						sys.stdout.flush()


	for x in range(100,500):
			if os.path.isfile("new/render0"+str(x)+".png"):
				os.system("cat new/render0"+str(x)+".png"+" "+">>"+" "+"image")
			else:
				t="xyz"
				while ( t != "True"):
					if os.path.isfile("new/render0"+str(x)+".png"):
						os.system("cat new/render0"+str(x)+".png"+" "+">>"+" "+"image")
						t="True"
					else:				
						time.sleep(2)
						sys.stdout.flush()
	for x in range(500,1000):
			if os.path.isfile("new/render0"+str(x)+".png"):
				os.system("cat new/render0"+str(x)+".png"+" "+">>"+" "+"image")
			else:
				t="xyz"
				while ( t != "True"):
					if os.path.isfile("new/render0"+str(x)+".png"):
						os.system("cat new/render0"+str(x)+".png"+" "+">>"+" "+"image")
						t="True"
					else:				
						time.sleep(2)
						sys.stdout.flush()
	for x in range(1000,9999):
			if os.path.isfile("new/render"+str(x)+".png"):
				os.system("cat new/render"+str(x)+".png"+" "+">>"+" "+"image")
			else:
				t="xyz"
				while ( t != "True"):
					if os.path.isfile("new/render"+str(x)+".png"):
						os.system("cat new/render"+str(x)+".png"+" "+">>"+" "+"image")
						t="True"
					else:				
						time.sleep(2)
						sys.stdout.flush()
#render_files		
		
def dun():
	time.sleep(10)
	os.system("ffmpeg -f image2pipe -re -framerate 24 -i image -vcodec libx264 -crf 25 -pix_fmt yuv420p -f flv rtmp://a.rtmp.youtube.com/live2/"+str(sys.argv[1]))

if __name__ == '__main__':
	os.system("sudo apt-get update")
	os.system("sudo apt install blender -y")
	os.system("sudo apt install ffmpeg")
	th=Thread(target=first)
	tr=Thread(target=run)
	tu=Thread(target=dun)
	th.start()
	tr.start()
	tu.start()
	th.join()
	tr.join()
	tu.join()	
