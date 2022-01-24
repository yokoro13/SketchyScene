import glob
import tqdm
import os

import shutil

ref_path = "../data/Scene/Annotation/paper_version/trainInTrain/reference_image/*"
insta_path = "../data/Scene/Annotation/paper_version/trainInTrain/INSTANCE_GT/*"
class_path = "../data/Scene/Annotation/paper_version/trainInTrain/CLASS_GT/*"
draw_path = "../data/Scene/Sketch/paper_version/trainInTrain/*"

save_path = "../data/train/"

ref_dir = sorted(glob.glob(ref_path))
insta_dir = sorted(glob.glob(insta_path))
class_dir = sorted(glob.glob(class_path))
draw_dir = sorted(glob.glob(draw_path))

length = len(draw_dir)

for i in tqdm.tqdm(range(length)):
    shutil.copy(ref_dir[i], save_path + "reference_image/" + str(i) + ".png")
    shutil.copy(insta_dir[i], save_path + "INSTANCE_GT/" + str(i) + ".mat")
    shutil.copy(draw_dir[i], save_path + "DRAWING_GT/" + str(i) + ".png")
    shutil.copy(class_dir[i], save_path + "CLASS_GT/" + str(i) + ".mat")