import glob
import tqdm
import os

ref_path = "/"
insta_path = "/"
class_path = "/"
draw_path = "/"

save_path = "/"

ref_dir = glob.glob(ref_path)
insta_dir = glob.glob(insta_path)
class_dir = glob.glob(class_path)
draw_dir = glob.glob(draw_path)

length = len(draw_dir)

for i in tqdm.tqdm(range(length)):
    os.rename(ref_dir[i], save_path + "reference_image/" + str(i) + ".png")
    os.rename(insta_dir[i], save_path + "INSTANCE_GT/" + str(i) + ".mat")
    os.rename(draw_dir[i], save_path + "DRAWING_GT/" + str(i) + ".png")
    os.rename(class_dir[i], save_path + "CLASS_GT/" + str(i) + ".mat")