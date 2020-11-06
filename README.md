<img src="https://i.imgur.com/9oNc1J2.png" alt="ComplianceDungeons" align="right" height="256px">
<div align="center">
  <h1>Compliance Dungeons</h1>
  <h3>Compliance 32x for Minecraft Dungeons</h3>

![RepoSize](https://img.shields.io/github/repo-size/Faithful-Dungeons/Resource-Pack)
![Issues](https://img.shields.io/github/issues/Faithful-Dungeons/Resource-Pack)
![PullRequests](https://img.shields.io/github/issues-pr/Faithful-Dungeons/Resource-Pack)
![Downloads](https://img.shields.io/github/downloads/Faithful-Dungeons/Resource-Pack/total)
</div>

## Info
- All recently made textures will be uploaded here.
- The mod making tool this repository features was made by the [Dokucraft Team](https://github.com/Dokucraft).
- If you find any Issues, please report them [here](https://github.com/Faithful-Dungeons/Resource-Pack/issues). 
- This GitHub is structured in the same way as the [Dokucraft Tool](https://github.com/Dokucraft/Dungeons-Mod-Kit) provides.
- If you're new to this project, check out [this flowchart](https://media.discordapp.net/attachments/716484045118373979/735067976918630430/texture_flowchart.png) about making and submitting textures.

## Contributors
[![](https://sourcerer.io/fame/RobertRR11/Faithful-Dungeons/Resource-Pack/images/0)](https://sourcerer.io/fame/RobertRR11/Faithful-Dungeons/Resource-Pack/links/0)[![](https://sourcerer.io/fame/RobertRR11/Faithful-Dungeons/Resource-Pack/images/1)](https://sourcerer.io/fame/RobertRR11/Faithful-Dungeons/Resource-Pack/links/1)[![](https://sourcerer.io/fame/RobertRR11/Faithful-Dungeons/Resource-Pack/images/2)](https://sourcerer.io/fame/RobertRR11/Faithful-Dungeons/Resource-Pack/links/2)[![](https://sourcerer.io/fame/RobertRR11/Faithful-Dungeons/Resource-Pack/images/3)](https://sourcerer.io/fame/RobertRR11/Faithful-Dungeons/Resource-Pack/links/3)[![](https://sourcerer.io/fame/RobertRR11/Faithful-Dungeons/Resource-Pack/images/4)](https://sourcerer.io/fame/RobertRR11/Faithful-Dungeons/Resource-Pack/links/4)[![](https://sourcerer.io/fame/RobertRR11/Faithful-Dungeons/Resource-Pack/images/5)](https://sourcerer.io/fame/RobertRR11/Faithful-Dungeons/Resource-Pack/links/5)[![](https://sourcerer.io/fame/RobertRR11/Faithful-Dungeons/Resource-Pack/images/6)](https://sourcerer.io/fame/RobertRR11/Faithful-Dungeons/Resource-Pack/links/6)[![](https://sourcerer.io/fame/RobertRR11/Faithful-Dungeons/Resource-Pack/images/7)](https://sourcerer.io/fame/RobertRR11/Faithful-Dungeons/Resource-Pack/links/7)

## How to compile:
> You can compile our Resource Pack by yourself, but **according to our Licence, you can't distribute it or sell it.**

### Prerequisites:
- [Python 3.8+](https://www.microsoft.com/en-us/p/python-38/9mssztt1n39l?activetab=pivot:overviewtab)
- Unreal Engine 4.22 (available on the Epic Game Store)

The tools will only run on Windows.

### Setup:
Edit the text files in the `Tools/user_settings` folder to configure the tools:

| File | Description |
| -------- | -------- |
| editor_directory.txt     | This contains the path to the folder where the Unreal Editor executables are.     |
| package_output.txt     | This contains the path to the .pak file that the package.bat tool creates.     |
| quickbms_export_dir.txt     | This contains the path to the folder where you have exported the game files using QuickBMS. This is only needed for the `Tools/copy_missing_blocks.bat` and `Tools/update_block_textures_config.bat` tools.     |

Setting the package_output path to a file in your ~mods folder is recommended to make testing the mod easy.

> A more detailed documentation can be found [here](https://github.com/Dokucraft/Dungeons-Mod-Kit)

If an update for the game comes out and you don't want to wait for the mod kit to update, you can use the `Tools/update_block_textures_config.bat` tool to update it yourself. It requires the QuickBMS exported files of the game, and [Pillow](https://pypi.org/project/Pillow/), so make sure that is installed before you run it. After it's done, the block textures config should be updated.

To build the pak you need to execute the package.bat file. This can take anywhere from 1 to 3 minutes depending on your hardware.

Then you get the `.pak` exported where you set your path in `package_output.txt`

## Links
- Compliance Dungeons Website: https://faithful-dungeons.github.io/Website/
- Compliance Discord: https://discord.gg/pwnGtXs
- Compliance Dungeons Discord: https://discord.gg/eeVpygu

## Have a question?
You can find some questions and answers in the [FAQ Wiki page](https://github.com/Compliance-Dungeons/Resource-Pack/wiki/FAQ). If your question isn't there then you can join our [Discord server](https://discord.gg/eeVpygu) and ask your question there!
