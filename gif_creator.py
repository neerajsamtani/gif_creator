import os
import sys
import imageio
import visvis as vv
import time
start_time = time.time()

# Return the folder in which the script is stored
def self_path():
    path = os.path.dirname(sys.argv[0])
    if not path:
        path = '.'
    return path

# Set the variables to the approproate folders
current_folder = self_path()
A = os.path.join(current_folder, 'Images', 'A')
B = os.path.join(current_folder, 'Images', 'B')
C = os.path.join(current_folder, 'Images', 'C')
D = os.path.join(current_folder, 'Images', 'D')

# If an argument is not specified, assume the name of the image is "IMG_0001.jpg"
if(len(sys.argv) > 1):
	imagename = sys.argv[1] + ".jpg"
	gifname = sys.argv[1] + ".gif"
else:
	imagename = "IMG_0001.jpg"
	gifname = "IMG_0001.gif"

filenames = [os.path.join(A, imagename), 
			os.path.join(B, imagename),
			os.path.join(C, imagename),
			os.path.join(D, imagename),
			os.path.join(C, imagename),
			os.path.join(B, imagename),
			os.path.join(A, imagename)]

images = []
for filename in filenames:
    images.append(imageio.imread(filename))
imageio.mimsave(os.path.join(current_folder, 'Images', 'Gifs', gifname), images, duration = 0.2)

print("--- %s seconds ---" % (time.time() - start_time))
k = input("press enter to exit") 