@echo on
SET "ddp=%~dp0"
SET "ddp=%ddp:~0,-1%"
SET /p editorPath= < Tools\settings\editor_directory.txt
SET /p packageOutput= < Tools\settings\package_output.txt

REM Building Resource Pack...
cd Tools
python copy_block_textures.py
cd..

REM Importing assets...
@echo off
python Tools\generate_asset_import_settings.py
"%editorPath%\UE4Editor-Cmd.exe" "%ddp%\UE4Project\Dungeons.uproject" -run=ImportAssets -nosourcecontrol "-importsettings=%ddp%\Tools\tmp_import_settings.json"
del /s Tools\tmp_import_settings.json  >nul 2>&1
@echo on

@REM Cooking assets...
del /S Dungeons\*.uasset
del /S Dungeons\*.ubulk
del /S Dungeons\*.uexp
del /S Dungeons\*.umap
del /S Dungeons\*.ufont
"%editorPath%\UE4Editor-Cmd.exe" "%ddp%\UE4Project\Dungeons.uproject" -run=cook -targetplatform=WindowsNoEditor
robocopy /job:Tools\copy_cooked_assets

REM	Packing...
python Tools\u4pak.py pack "%packageOutput%" Dungeons -p