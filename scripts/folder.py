import os

def folder_count(path, map = {}):
  count = 0
  for f in os.listdir(path):
    child = os.path.join(path, f)
    if os.path.isdir(child):
      child_count = folder_count(child, map)
      count += child_count + 1 # unless include self
  map[path] = count
  return count

path = "/Users/huyho/Documents/progressor/scripts/input/superagent"
map = {}
print(folder_count(path, map))

