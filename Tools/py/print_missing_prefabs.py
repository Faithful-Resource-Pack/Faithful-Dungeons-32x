import os
import json
import math

texturesPath = '../UE4Project/Content/'

def scantree(path):
  for entry in os.scandir(path):
    if entry.is_dir(follow_symlinks=False):
      yield from scantree(entry.path)
    else:
      yield entry

count = 0
redundant_files_message_shown = False

with open('configs/prefabs_list.json') as json_file:
  textures = json.load(json_file)
  for filename in textures:
    if os.path.isfile(texturesPath + filename):
      print('Done:    ' + filename)
    if not os.path.isfile(texturesPath + filename):
      count += 1
      print('Missing: ' + filename)

  total = len(textures)
  print()
  print('----------------------------------------')
  print('  Total missing: ' + str(count))
  print('  Total done:    ' + str(total - count))
  print('  Complete:      ' + str(math.floor((total - count) * 100 / total)) + '%')
  print('----------------------------------------')

print()