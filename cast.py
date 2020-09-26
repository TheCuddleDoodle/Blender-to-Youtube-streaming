import os,sys,time
from threading import Thread

#installing updates



def first():
	time.sleep(2)
	os.system("unzip new.zip")	
	os.system("blender -b new/file.blend -x 1 -o //render -a")

#checking the availibity of files

def run():
	
	frame_no=0
	while(frame_no>=99999):
			x=frame_no
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
			x+=1			sys.stdout.flush()


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
