import os
import time
import zipfile

workSpace = "/Users/alphahinex/workspace"
backupRoot = "/Users/alphahinex/github/trunk/gitbackup/backup"
week = time.strftime("%w")
backupPath = os.path.join(backupRoot, week)

# clean zip file which is a week ago
delCommand = "rm -f " + os.path.join(backupRoot,week + ".zip")
os.system(delCommand)

# get all .git root path
firstLvs = os.listdir(workSpace)
srcDirs = []
for firstdir in firstLvs:
    if(os.path.isdir(os.path.join(workSpace,firstdir))):
        for secdir in os.listdir(os.path.join(workSpace,firstdir)):
            if(secdir.find('git')>0):
                if(os.path.isdir(os.path.join(workSpace,firstdir,secdir))):
                    srcDirs.append(firstdir)

# copy .git folder
for folder in srcDirs:
    copyCommand = "mkdir -p " + os.path.join(backupPath, folder) + " && "
    copyCommand += "cp -R " + os.path.join(workSpace,folder,".git") + " " + os.path.join(backupPath,folder,".git")
    os.system(copyCommand)

# zip the backup folder
filelist = []
for root, dirs, files in os.walk(backupPath):
    for name in files:
        filelist.append(os.path.join(root,name))

zf = zipfile.ZipFile(os.path.join(backupRoot,week+".zip"),"w",zipfile.zlib.DEFLATED)
for fileToZip in filelist:
    zf.write(fileToZip)
zf.close()

# clean temp folder
rdCommand = "rm -rf " + backupPath
os.system(rdCommand)