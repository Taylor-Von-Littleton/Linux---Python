#!/usr/bin/python3
import sys
import os
import pandas as pd

def get_directory_size(path):
  total = 0
  for entry in os.scandir(path): #os.scandir returns a list of files and directories, including sybolic links.
    try:
      if entry.is_dir(follow_symlinks=False):
        total += get_directory_size(entry.path) #goes through directory recursively (entry.path) is full name to the given directory on the given disk
      else:
        total += entry.stat(follow_symlinks=False).st_size
    except Exception as e:
        print("Exception: ", e)
        total+=0
  return total

#__name__ used to identify the code for the standalone script.
if __name__ == '__main__': # if this module is imported from another module it will not execute. It must act as a standalone program as it has been on the first 2 practice executions
  path = '/home'
  print("total arguments passed: ", len(sys.argv))

  directory = sys.argv[1] if len(sys.argv) >= 2 else path

  usage = []
  paths = []

  for entry in os.scandir(directory):
    print(entry.path)
    if(entry.is_dir(follow_symlinks=False)): #if entry is directory and not a symbolic link print the below message 
      total = get_directory_size(entry.path)
      print (total)
      paths.append(entry.path)
      usage.append(total)
    usage_dict = {'directory' : paths, 'usage' : usage}
    df = pd.DataFrame(usage_dict)
    print (df)
    df.to_csv("disk_home_usage.csv") #Name of newly generated csv file and function used to generate csv file.
      #print(entry.path + " is a directory")
      #print(get_directory_size(entry.path))
