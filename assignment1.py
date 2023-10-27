import os

haed_folder_path = "/Users/dgsw8th54/Desktop/study/data camp/DCC_고등부_데이터셋/train_resized"
haed_file_list = os.listdir(haed_folder_path)
haed_file_count = len(haed_file_list)
fst = 0
snd = 0
thr = 0
count = 0
for i in range(haed_file_count):
    try:
        folder_path =  "/Users/dgsw8th54/Desktop/study/data camp/DCC_고등부_데이터셋/train_resized/"+haed_file_list[i]
        file_list = os.listdir(folder_path)
        count += len(file_list)
        for j in range(len(file_list)):
            if file_list[j][-6:-4] == "01":
                fst += 1;
            elif file_list[j][-6:-4] == "02":
                snd += 1
            elif file_list[j][-6:-4] == "03":
                thr += 1
            else:
                print(file_list[j][-6:-4])
    except:
        print(haed_file_list[i])
print("전체 : %d, 01 : %d, 02 : %d, 03, %d" % (haed_file_count, fst, snd, thr))