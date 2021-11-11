import os

# Class used to represent files
class File:
	def __init__(self, name, path):
		self.name = name
		self.path = path

# Generates list of `File` which are present in given directory and subdirectories
def all_files_in_dir_subdir(dir):
	dir_list = os.listdir(dir)

	dir_files = []

	for f in dir_list:
		file_path = dir + '/' + f

		if os.path.isfile(file_path):
			dir_files.append(File(f, file_path))
		else:
			subdir_files = all_files_in_dir_subdir(file_path)
			dir_files.extend(subdir_files)

	return dir_files

# Returns true if given string(x) is present in given File object(file)
def exist_in_file(file, x):
	f = open(file.path)
	s = f.read()
	f.close()
	return x in s

# Find all occurence of given string(x) exists in any file in given directory(dir)
def all_occ_in_dir(dir, x):
	file_list = all_files_in_dir_subdir(dir)
	containing_x = []
	for f in file_list:
		if exist_in_file(f, x):
			containing_x.append(f)

	print('Found '+x+' in '+str(len(containing_x))+' file(s):')
	for f in containing_x:
		print(f.name + ' | ' + f.path)

drc = input("Enter the directory ")
txt = input("Enter the text to search for: ")
all_occ_in_dir(drc, txt)