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

# Get start and end numbers
start = int(sys.argv[1])
end = int(sys.argv[2]) + 1

# Set the variables to the appropriate folders
current_folder = self_path()
A = os.path.join(current_folder, 'Images', 'A')
B = os.path.join(current_folder, 'Images', 'B')
C = os.path.join(current_folder, 'Images', 'C')
D = os.path.join(current_folder, 'Images', 'D')

# Create gifs
def create_gifs(nstart, nend):
    os.system('cls' if os.name == 'nt' else 'clear')
    print("Completed 0 of " + str(end-1))
    for i in range(nstart,nend):
        imagename="IMG_"+'{0:04}'.format(i)+".jpg"
        gifname="IMG_"+'{0:04}'.format(i)+".gif"

        filenames = [os.path.join(A, imagename), 
                    os.path.join(B, imagename),
                    os.path.join(C, imagename),
                    os.path.join(D, imagename),
                    os.path.join(C, imagename),
                    os.path.join(B, imagename)]

        images = []
        for filename in filenames:
            images.append(imageio.imread(filename))
        imageio.mimsave(os.path.join(current_folder, 'Images', 'Gifs', gifname), images, duration = 0.2)
        os.system('cls' if os.name == 'nt' else 'clear')
        print("Completed " + str(i) + " of " + str(end-1))

create_gifs(start, end)

print("--- %s seconds ---" % (time.time() - start_time))
k = input("press enter to exit") 