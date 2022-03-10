import os
    
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

if __name__ == "__main__":
    root = ".."
    all_file_list = get_recur_file_list(root)
    for i in all_file_list:
        print(i)
