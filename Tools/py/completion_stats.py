import os
import json
import math

blockTexturesPath = '../Block Textures/'
unrealTexturesPath = '../UE4Project/Content/'

def scantree(path):
  for entry in os.scandir(path):
    if entry.is_dir(follow_symlinks=False):
      yield from scantree(entry.path)
    else:
      yield entry

blocksCount = 0
actorsCount = 0
prefabsCount = 0
totalBlocks = None
totalActors = None
totalPrefabs = None
redundant_files_message_shown = False

with open('configs/block_textures.json') as json_file:
  textures = json.load(json_file)
  totalBlocks = len(textures)
  for filename,copies in textures.items():
    if not os.path.isfile(blockTexturesPath + filename):
      blocksCount += 1

with open('configs/actors_list.json') as json_file:
  textures = json.load(json_file)
  totalActors = len(textures)
  for filename in textures:
    if not os.path.isfile(unrealTexturesPath + filename):
      actorsCount += 1

with open('configs/prefabs_list.json') as json_file:
  textures = json.load(json_file)
  totalPrefabs = len(textures)
  for filename in textures:
    if not os.path.isfile(unrealTexturesPath + filename):
      prefabsCount += 1

print()
print('------------------------------------------------')
print('  Total blocks:     ' + str(totalBlocks))
print('  Missing blocks:   ' + str(blocksCount))
print('  Blocks done:      ' + str(totalBlocks - blocksCount))
print('  Complete blocks:  ' + str(math.floor((totalBlocks - blocksCount) * 100 / totalBlocks)) + '%')
print()
print('  Total actors:     ' + str(totalActors))
print('  Missing actors:   ' + str(actorsCount))
print('  Actors done:      ' + str(totalActors - actorsCount))
print('  Complete actors:  ' + str(math.floor((totalActors - actorsCount) * 100 / totalActors)) + '%')
print()
print('  Total prefabs:    ' + str(totalPrefabs))
print('  Missing prefabs:  ' + str(prefabsCount))
print('  Prefabs done:     ' + str(totalPrefabs - prefabsCount))
print('  Complete prefabs: ' + str(math.floor((totalPrefabs - prefabsCount) * 100 / totalPrefabs)) + '%')
print()
print('  Total textures:   ' + str(totalBlocks + totalActors + totalPrefabs))
print('  Total missing:    ' + str(blocksCount + actorsCount + prefabsCount))
print('  Total done:       ' + str(totalBlocks + totalActors + totalPrefabs - blocksCount - actorsCount - prefabsCount))
print('  Complete:         ' + str(math.floor((totalBlocks + totalActors + totalPrefabs - blocksCount - actorsCount - prefabsCount) * 100 / (totalBlocks + totalActors + totalPrefabs))) + '%')
print('------------------------------------------------')
print()