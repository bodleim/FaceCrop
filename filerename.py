import os
import glob

target = "외질혜"
fpath = "./data/"+str(target)+"/\*.jpg"  #해당 폴더안에 jpg 확장자 모두 불러오기
for fpath in glob.glob(fpath):
    fpath_r = fpath.replace(str(target),'') #selfie (27).jpg => (27).jpg로 변경
    fpath_r = fpath_r.replace('_','')
    fpath_r = fpath_r.replace("\\","")
    fpath_r = fpath_r.replace("./data/", "./data/" +str(target)+ "/")
    print(fpath_r+"\n")
    os.rename(fpath, fpath_r)