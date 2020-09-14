import os, sys

def countFilesRecursive(dirname):
	cnt = 0
	for file in os.listdir(dirname):
		fullpath = os.path.join(dirname, file)
		if os.path.isdir(fullpath):
			cnt = cnt + countFilesRecursive(fullpath)
		elif os.path.isfile(fullpath):
			cnt = cnt + 1
	return cnt

def main():
	dir_list = []
	if len(sys.argv) > 1:
		dir_list = sys.argv[1:]
	else: 
		dir_list = ["./"]

	for dir in dir_list:
		if os.path.isfile(dir):
			print("\"{}\" is not a directory!".format(dir))
			continue	
		dirname = "current"
		if dir not in ["./", "."]:
			dirname = dir
		print("Total {} files in {} directory".format(countFilesRecursive(dir), dirname))

if __name__ == '__main__':
	main()

