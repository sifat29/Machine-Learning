import os
folder = r"E:/code python/New folder/muzzle_dataset"
# main_folder=os.walk(folder)
# print(main_folder)
# # for i in len(range(main_folder)):
# #     for j in len(range(main_folder[i])):
# #         print(main_folder[i][j])
# #          oldname = folder + filename   
# #     newname = folder + "Emp_" + str(count + 1) + ".jpg"
# #     os.rename(oldname, newname)
# for count, filename in enumerate(main_folder):
#     # print(os.path.join(folder,filename))
#     for idx, sub_file in enumerate([os.path.join(folder,filename)]):

#         #  for x, image_name in enumerate(os.listdir(folder + "/" + filename +"/"+ sub_file)):
#         #     dir = os.listdir(folder+"/"+filename+"/"+sub_file+"/")

#         #  os.rename(image_name,  "1" + image_name)

for root, subdirectories, files in os.walk(folder):
    for file in files:
        new_name = "1"+file
        os.rename(os.path.join(root,file), os.path.join(root,new_name))
    for dir in subdirectories:
        if(dir.startswith("0")):
            new_dir = "1"+dir
            os.rename(os.path.join(root,dir), os.path.join(root, new_dir))
    

