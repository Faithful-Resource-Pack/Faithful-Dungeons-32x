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

print('────────────────────────────────────────────────')
print('  Blocks  :')
print('     - Total   : ' + str(totalBlocks))
print('     - Missing : ' + str(blocksCount))
print('     - Done    : ' + str(totalBlocks - blocksCount) + ' (' + str(math.floor((totalBlocks - blocksCount) * 100 / totalBlocks)) + '%)' )

print()

print('  Actors  :')
print('     - Total   : ' + str(totalActors))
print('     - Missing : ' + str(actorsCount))
print('     - Done    : ' + str(totalActors - actorsCount) + ' (' + str(math.floor((totalActors - actorsCount) * 100 / totalActors)) + '%)' )

print()

print('  Prefabs :')
print('     - Total   : ' + str(totalPrefabs))
print('     - Missing : ' + str(prefabsCount))
print('     - Done    : ' + str(totalPrefabs - prefabsCount) + ' (' + str(math.floor((totalPrefabs - prefabsCount) * 100 / totalPrefabs)) + '%)' )

print()

print('  Global  :')
print('     - Total   : ' + str(totalBlocks + totalActors + totalPrefabs))
print('     - Missing : ' + str(blocksCount + actorsCount + prefabsCount))
print('     - Done    : ' + str(totalBlocks + totalActors + totalPrefabs - blocksCount - actorsCount - prefabsCount) + ' (' + str(math.floor((totalBlocks + totalActors + totalPrefabs - blocksCount - actorsCount - prefabsCount) * 100 / (totalBlocks + totalActors + totalPrefabs))) + '%)' )
print('────────────────────────────────────────────────')
print()