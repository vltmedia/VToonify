import os, glob, shutil
    
def imageSequencetoVideo(filepattern, outputPath, framerate = 12):
    # run ffmpeg to convert image sequence with filepattern to video at outputPath
    os.system(f'ffmpeg -y -r {framerate} -i %s -vcodec libx264 -pix_fmt yuv420p %s' % (filepattern, outputPath))
    
if __name__ == '__main__':
    
    path = r"F:\Projects\CodeDump\GenFX\src\helpers\vToon\output\isekai"
    imgpath = r"F:\Projects\CodeDump\GenFX\src\helpers\vToon\output\isekai\imgs\"
    videospath = r"F:\Projects\CodeDump\GenFX\src\helpers\vToon\output\isekai\videos\"
    imagefiles = glob.glob(os.path.join(path, "*.jpg"))
    videosfiles = glob.glob(os.path.join(path, "*.mp4"))
    
    # for file in imagefiles:
    #     shutil.move(file, imgpath)
        
    for file in videosfiles:
        shutil.move(file, os.path.join(imgpath,))
    
    
    # for indx in range(1,50):
    #     imageSequencetoVideo(os.path.abspath(f"{path}/Justin_vtoonify_%04d_{indx}_c_d.jpg"),os.path.abspath(f"{path}/Justin_vtoonify_{indx}_c_d.mp4"), 12 )
    
    
    