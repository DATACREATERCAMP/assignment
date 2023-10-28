import os

current_path = os.getcwd()
print('currentPath -', current_path)

TRAIN_PATH = "train_resized/"
VALID_PATH = "valid_resized/"

def countData(path):
    global current_path

    fst = 0
    snd = 0
    thr = 0
    cnt = 0
    path = os.path.join(current_path, path)

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
                    match fileIdx:
                        case "01": fst += 1
                        case "02": snd += 1
                        case "03": thr += 1
                except Exception as e:
                    print(e)
        except Exception as e:
            print(e)
    print('-----------------------')
    print('path -', path)

    print(f"result - {cnt}, 01 : {fst}, 02 : {snd}, 03, {thr}" % ())
    print('-----------------------')


countData(TRAIN_PATH)
countData(VALID_PATH)
