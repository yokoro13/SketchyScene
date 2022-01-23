import glob
import tqdm

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
    os.rename(ref_dir[i], save + "reference_image/" + str(i) + ".png")
    os.rename(insta_dir[i], save + "INSTANCE_GT/" + str(i) + ".mat")
    os.rename(draw_dir[i], save + "DRAWING_GT/" + str(i) + ".png")
    os.rename(class_dir[i], save + "CLASS_GT/" + str(i) + ".mat")