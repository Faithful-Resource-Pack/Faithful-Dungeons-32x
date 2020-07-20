# Faithful Dungeons
![Header](https://raw.githubusercontent.com/Faithful-Dungeons/Website/master/image/banner/banner.png)
> Welcome to the official Faithful Dungeons repository! Here you can see our progress on the Faithful 32x recource pack for Minecraft Dungeons!

## Info
- All recently made textures will be uploaded here.
- The mod making tool this repository features was made by the [Dokucraft Team](https://github.com/Dokucraft).
- If you find any Issues, please report them [here](https://github.com/Faithful-Dungeons/Resource-Pack/issues). 
- All textures are made from this [.zip](https://www.mediafire.com/file/38edw7s7rrf9lji/Content.zip/file) file made by [RobertR11](https://github.com/RobertRR11).
- This GitHub is structured in the same way as the Dokucraft [Tool](https://github.com/Dokucraft/Dungeons-Mod-Kit) provides.
- If you're new to this project, check out [this flowchart](https://cdn.discordapp.com/attachments/716484045118373979/722080330860986429/Untitled_Diagram.png) about making and submitting textures.


## How to compile:
> You can compile our Resource Pack by yourself, **according to our Licence, you can't distribute it or sell it.**

### Prerequisites:
- [Python 3.8+](https://www.microsoft.com/en-us/p/python-38/9mssztt1n39l?activetab=pivot:overviewtab)
- Unreal Engine 4.22 (available on the Epic Game Store)

### Setup:
Edit the text files in the `Tools/settings` folder to configure the tools:

| File | Description |
| -------- | -------- |
| editor_directory.txt     | This contains the path to the folder where the Unreal Editor executables are.     |
| package_output.txt     | This contains the path to the .pak file that the package.bat tool creates.     |
| quickbms_export_dir.txt     | This contains the path to the folder where you have exported the game files using QuickBMS. This is only needed for the `Tools/copy_missing_blocks.bat` tool.     |

Setting the package_output path to a file in your ~mods folder is recommended to make testing the mod easy.

> A more detailed documentation can be found [here](https://github.com/Dokucraft/Dungeons-Mod-Kit)

Then you need to execute those files: 
- 1st : build_resource_packs.bat
- 2nd : import_assets.bat
- 3rd : cook_assets.bat
- at the end : package.bat

Then you get the `.pak` exported where you set your path in `package_output.txt`

## Links
- Faithful Website: https://faithful.team/
- Faithful Dungeons Website: https://faithful-dungeons.github.io/Website/
- Discord: https://discord.gg/pwnGtXs
- Dungeons Discord: https://discord.gg/eeVpygu

## Have a question?
You can find some questions and answers in the [FAQ Wiki page](https://github.com/Faithful-Dungeons/Resource-Pack/wiki/FAQ). If your question isn't there then you can join our [Discord server](https://discord.gg/eeVpygu) and ask your question there!
