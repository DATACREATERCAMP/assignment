import os

current_path = os.getcwd()
print('currentPath -', current_path)

TRAIN_PATH = "train_resized/"
VALID_PATH = "valid_resized/"

MAX = 3

def countData(path):
    global current_path

    idxLst = [0 for _ in range(MAX)]
    cnt = 0
    path = os.path.join(current_path, path)


    if not os.path.exists(path):
        print('Folder does not exist')
        return
        
    folder_list = os.listdir(path)

    for folder in folder_list:
        try:
            folder_path =  os.path.join(path, folder)
            file_list = os.listdir(folder_path)
            for file in file_list:
                try:
                    fileName, ext = os.path.splitext(file)
                    fileIdx = fileName[-2:]
                    cnt += 1
                    idxLst[int(fileIdx) - 1] += 1
                except Exception as e:
                    print(e)
        except Exception as e:
            print(e)
    print('-----------------------')
    print('path -', path)

    for (idx, i) in enumerate(idxLst):
        print(f'{idx + 1} - {i}')
    print('-----------------------')


countData(TRAIN_PATH)
countData(VALID_PATH)
