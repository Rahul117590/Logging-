import os 
# print(dir(os))   # get all the opeation method name in list formm
print(os.getcwd()) # help to find the location of the file in the python



# File and Directory Management:
#os.mkdir("newFolder") # used to create new folder in you worklocation
#os.makedirs("one/two")# used to create subfolder like one and two in the folder of one
#os.rmdir("newfolder") # it help to delete the folder
# os.removedirs("one/two")# it used to delete the subfolder with one move [recursive delete]
# print(os.listdir('.')) # it give the detail of all sub file and folder
# var=os.walk(os.getcwd()) # it gives all the file and subfolder detail in the python current location or as u want location
# print(var)

# for value in var:
#     print(value)


# stats=os.stat("start.ipynb") # it give the all file details like when file is created size everything
# print(stats) 
# print(stats.st_size)



# path Manipulation
