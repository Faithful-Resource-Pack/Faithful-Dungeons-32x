# Copyright (c) 2020 DokucraftSaga
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

import os
import json

def scantree(path):
  for entry in os.scandir(path):
    if entry.is_dir(follow_symlinks=False):
      yield from scantree(entry.path)
    else:
      yield entry

cwd = os.getcwd().replace('\\', '/')

importGroups = []

for png in [f.path.replace('\\', '/') for f in scantree('UE4Project/Content') if f.name.endswith('.png') and not os.path.isfile(os.path.splitext(f.path)[0]+'.uasset')]:
  group = {
    'GroupName': os.path.basename(png),
    'Filenames': [ cwd + '/' + png ],
    'DestinationPath': os.path.dirname(png).replace('UE4Project/Content', '/Game'),
    'bReplaceExisting':'true',
    'bSkipReadOnly':'false',
    'FactoryName': 'TextureFactory', 
    'ImportSettings': {
      'CompressionSettings': 'TC_BC7',
      'LODGroup': 'TEXTUREGROUP_Pixels2D'
    }
  }

  print('Importing ' + png.replace('UE4Project/Content/', ''))

  # Load custom import settings, if any
  if os.path.isfile(os.path.splitext(png)[0]+'.json'):
    with open(os.path.splitext(png)[0]+'.json') as json_file:
      for key,value in json.load(json_file).items():
        group['ImportSettings'][key] = value

  importGroups.append(group)

for fbx in [f.path.replace('\\', '/') for f in scantree('UE4Project/Content') if f.name.endswith('.fbx') and not os.path.isfile(os.path.splitext(f.path)[0]+'.uasset')]:
  group = {
    'GroupName': os.path.basename(fbx),
    'Filenames': [ cwd + '/' + fbx ],
    'DestinationPath': os.path.dirname(fbx).replace('UE4Project/Content', '/Game'),
    'bReplaceExisting':'true',
    'bSkipReadOnly':'false',
    'FactoryName': 'FbxFactory',
    'ImportSettings': {
      'bImportTextures': False,
      'bImportMaterials': True
    }
  }

  print('Importing ' + fbx.replace('UE4Project/Content/', ''))

  # Load custom import settings, if any
  if os.path.isfile(os.path.splitext(fbx)[0]+'.json'):
    with open(os.path.splitext(fbx)[0]+'.json') as json_file:
      for key,value in json.load(json_file).items():
        group['ImportSettings'][key] = value

  importGroups.append(group)

settingsFile = open('Tools/tmp_import_settings.json', 'w')
settingsFile.write(json.dumps({ 'ImportGroups': importGroups }))
settingsFile.close()