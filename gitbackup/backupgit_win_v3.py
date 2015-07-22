import os
import time
import zipfile

workSpace = "e:\\workspace"
backupRoot = "f:\\gitbackup"
week = time.strftime("%w")
backupPath = os.path.join(backupRoot, week)

# clean zip file which is a week ago
delCommand = "del " + os.path.join(backupRoot,week+".zip") + " /a/f"
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
        copyCommand = "xcopy " + os.path.join(workSpace,folder,".git") + " " + os.path.join(backupPath,folder,".git /E/Q/I/K")
        os.system(copyCommand)

# backup .git folder not in workspace
copyCommand = "xcopy e:\\additional\\.git " + os.path.join(backupPath,"additional\\.git") + " /E/Q/I/K"
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
rdCommand = "rd " + backupPath + " /s/q"
os.system(rdCommand)

# copy backup file to dropbox folder
cpCommand = "copy " + os.path.join(backupRoot, week+".zip") + " f:\\Dropbox\\private\\gitbackup.zip /Y"
os.system(cpCommand)

