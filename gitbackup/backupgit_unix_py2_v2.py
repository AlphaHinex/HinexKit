import os
import sys

workSpace = "/Users/alphahinex/workspace"
backupRoot = "/Users/alphahinex/github/trunk/gitbackup/backup"

def main(args):
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

    # tar the backup folder with encryption, and could use this command to untar
    # dd if=${file} | openssl des3 -d -k ${password} | tar zxf -
    for folder in srcDirs:
        cmd = "tar -zcvf - " + os.path.join(backupRoot, folder) + "|openssl des3 -salt -k " + args[1] + "|dd of=" + os.path.join(backupRoot, folder + ".tar")
        cmd += " && rm -rf " + os.path.join(backupRoot, folder)
        os.system(cmd)

if __name__ == '__main__':
    main(sys.argv)