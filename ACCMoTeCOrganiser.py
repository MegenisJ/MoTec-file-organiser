import shutil, os
from os import listdir
from os.path import isfile, join
#reading all the files in the folder and creating a list of them
mypath = os.getcwd()+"/MoTeC/"
onlyfiles = [f for f in listdir(mypath) if isfile(join(mypath, f))]
#creating a dictionary of tracks with the current cars that the telemetry data exists for
tracklist = {}
for i in onlyfiles:
    #dumb janky ineffecient if statement just to stop an error
    if "-" in i:
        x = i.split('-')
        if x[0]  not in tracklist:
            tracklist[x[0]] = []
        if x[1] not in tracklist.get(x[0]):
            tracklist[x[0]].append(x[1])

#creating a list of file paths
paths = []
for i in tracklist:
    for x in tracklist[i]:
        paths.append(mypath + i+ "/"+x )

#creating the files
for path in paths:
    try:
        os.makedirs(path)
    except OSError:
        print ("Creation of the directory %s failed" % path)
    else:
        print ("Directory Created: %s " % path)
#copying motec files into the correct place
print("Moving files... program will close when operation is complete")
print("This will take some time if there are lots of files to move")
for i in onlyfiles:
    #dumb janky ineffecient if statement just to stop an error
    if "-" in i:
        x = i.split('-')
        src = (mypath + "/" + i)
        dst = (mypath  +x[0] +"/"+ x[1] +"/"+ i)
        #shutil.copyfile(src, dst)
        #use move for the final working version
        shutil.move(src, dst)
