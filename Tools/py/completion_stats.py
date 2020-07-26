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
itemsCount = 0
mobsCount = 0
prefabsCount = 0
totalBlocks = None
totalItems = None
totalMobs = None
totalPrefabs = None
redundant_files_message_shown = False

os.system('chcp 65001')
os.system('cls')

with open('configs/block_textures.json') as json_file:
  textures = json.load(json_file)
  totalBlocks = len(textures)
  for filename,copies in textures.items():
    if not os.path.isfile(blockTexturesPath + filename):
      blocksCount += 1

with open('configs/items_list.json') as json_file:
  textures = json.load(json_file)
  totalItems = len(textures)
  for filename in textures:
    if not os.path.isfile(unrealTexturesPath + filename):
      itemsCount += 1

with open('configs/mobs_list.json') as json_file:
  textures = json.load(json_file)
  totalMobs = len(textures)
  for filename in textures:
    if not os.path.isfile(unrealTexturesPath + filename):
      mobsCount += 1

with open('configs/prefabs_list.json') as json_file:
  textures = json.load(json_file)
  totalPrefabs = len(textures)
  for filename in textures:
    if not os.path.isfile(unrealTexturesPath + filename):
      prefabsCount += 1

print('\x1b[1m')
print('────────────────────────────────────────────────')
print('  Blocks  :')
print('     - Total    : ' + str(totalBlocks))
print('     -\x1b[31m Missing \x1b[37m : ' + str(blocksCount))
print('     -\x1b[32m Done    \x1b[37m : ' + str(totalBlocks - blocksCount) + ' (' + str(math.floor((totalBlocks - blocksCount) * 100 / totalBlocks)) + '%)' )

print()

print('  Items   :')
print('     - Total    : ' + str(totalItems))
print('     -\x1b[31m Missing \x1b[37m : ' + str(itemsCount))
print('     -\x1b[32m Done    \x1b[37m : ' + str(totalItems - itemsCount) + ' (' + str(math.floor((totalItems - itemsCount) * 100 / totalItems)) + '%)' )

print()

print('  Mobs    :')
print('     - Total    : ' + str(totalMobs))
print('     -\x1b[31m Missing \x1b[37m : ' + str(mobsCount))
print('     -\x1b[32m Done    \x1b[37m : ' + str(totalMobs - mobsCount) + ' (' + str(math.floor((totalMobs - mobsCount) * 100 / totalMobs)) + '%)' )

print()

print('  Prefabs :')
print('     - Total    : ' + str(totalPrefabs))
print('     -\x1b[31m Missing \x1b[37m : ' + str(prefabsCount))
print('     -\x1b[32m Done    \x1b[37m : ' + str(totalPrefabs - prefabsCount) + ' (' + str(math.floor((totalPrefabs - prefabsCount) * 100 / totalPrefabs)) + '%)' )

print()

print('  Global  :')
print('     - Total    : ' + str(totalBlocks + totalItems + totalMobs + totalPrefabs))
print('     -\x1b[31m Missing \x1b[37m : ' + str(blocksCount + itemsCount + mobsCount + prefabsCount))
print('     -\x1b[32m Done    \x1b[37m : ' + str(totalBlocks + totalItems + totalMobs + totalPrefabs - blocksCount - itemsCount - mobsCount - prefabsCount) + ' (' + str(math.floor((totalBlocks + totalItems + totalMobs + totalPrefabs - blocksCount - itemsCount - mobsCount - prefabsCount) * 100 / (totalBlocks + totalItems + totalMobs + totalPrefabs))) + '%)' )
print('────────────────────────────────────────────────')
print()