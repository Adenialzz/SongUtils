import os
import os.path as osp
import shutil
import random
from tqdm import tqdm
    
def get_recur_file_list(root):
    def recur(path):
        filesList = os.listdir(path)
        for fileName in filesList:
            fileAbsPath = os.path.join(path, fileName)
            if os.path.isdir(fileAbsPath):
                recur(fileAbsPath)
            else:
                all_file_list.append(fileAbsPath)
    all_file_list = []
    recur(root)
    return all_file_list



def split_files(all_files_dir, output_dir, num_per_group, shuffle=False):
    files_list = os.listdir(all_files_dir)
    if shuffle:
        random.shuffle(files_list)
    split_folder_index = 0
    for i, image in tqdm(enumerate(files_list), total=len(files_list)):
        if i % num_per_group == 0:
            split_folder_index += 1
            currDir = osp.join(output_dir, str(split_folder_index))
        if not osp.isdir(currDir):
            os.mkdir(currDir)
        shutil.copyfile(osp.join(all_files_dir, image), osp.join(currDir, image))

if __name__ == "__main__":
    root = ".."
    all_file_list = get_recur_file_list(root)
    for i in all_file_list:
        print(i)
