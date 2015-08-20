import os

workSpace = "/Users/alphahinex/workspace"
backupRoot = "/Users/alphahinex/github/trunk/gitbackup/backup"

# get all .git root path
firstLvs = os.listdir(workSpace)
srcDirs = []
for firstdir in firstLvs:
    if(os.path.isdir(os.path.join(workSpace,firstdir))):
        for secdir in os.listdir(os.path.join(workSpace,firstdir)):
            if(secdir.find('git')>0):
                if(os.path.isdir(os.path.join(workSpace,firstdir,secdir))):
                    srcDirs.append(firstdir)

# copy .git folder, and delete the old one before if needed
for folder in srcDirs:
    cmd = "mkdir -p " + os.path.join(backupRoot, folder) + " && "
    cmd += "cp -R " + os.path.join(workSpace,folder,".git") + " " + os.path.join(backupRoot,folder,".git") + " && "
    cmd += "rm -f " + os.path.join(backupRoot, folder + ".tar")
    os.system(cmd)

# tar the backup folder
for folder in srcDirs:
    cmd = "tar czf " + os.path.join(backupRoot, folder + ".tgz") + " " + os.path.join(backupRoot, folder)
    cmd += " && rm -rf " + os.path.join(backupRoot, folder)
    os.system(cmd)