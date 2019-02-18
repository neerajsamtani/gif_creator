# READ ME
I wrote this script for a 'Creative Labs' Photoshoot. The photographers wanted to create stereoscopic 3D gifs for everyone in the 'Creative Labs' team and needed to automate this process because there were too many gifs to create manually. The script is written in Python and uses the imageio and visvis libraries. It generated 88 gifs within 3 minutes.

To use this script, you will have to install the following dependencies using `pip install`. If you don't already have `pip`, run these two commands:
```
$ curl https://bootstrap.pypa.io/get-pip.py -o get-pip.py
```
And then run
```
$ python get-pip.py
```

Once you install 'pip', we can install our dependencies. You might already have some of these, like `numpy`.

```
$ pip install imageio
$ pip install visvis
$ pip install numpy
$ pip install PyOpenGL
$ pip install PySide2
```

Next, clone the repository to get the following folder structure:
```
gif_creator
│   gif_creator.py
│   README.md 
│
└───Images
│   │
│   └───A
│       │   IMG_0001.JPG
│       │   IMG_0002.JPG
│       │   ... *Other images with the same naming convention*
│   └───B
│       │   IMG_0001.JPG
│       │   IMG_0002.JPG
│       │   ... *Other images with the same naming convention*
│   └───C
│       │   IMG_0001.JPG
│       │   IMG_0002.JPG
│       │   ... *Other images with the same naming convention*
│   └───D
│       │   IMG_0001.JPG
│       │   IMG_0002.JPG
│       │   ... *Other images with the same naming convention*
```

When you double click on the script, enter the starting and ending image names for which you want to create gifs. For example, if I had 70 images which were named IMG_0004.JPG, IMG_0005.JPG, .... IMG_0074.JPG , I would enter `4 74` when prompted in the command line and then hit *Enter*. A folder *Gifs* will appear under the *Images* folder with all the gifs in it.

That's it!
