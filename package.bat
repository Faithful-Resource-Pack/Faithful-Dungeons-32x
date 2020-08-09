@echo off
echo ------------------------------------------------------------
echo(
echo Applying settings...
echo(
echo ------------------------------------------------------------
SET "ddp=%~dp0"
SET "ddp=%ddp:~0,-1%"
SET /p editorPath= < Tools\user_settings\editor_directory.txt
SET /p packageOutput= < Tools\user_settings\package_output.txt

echo ------------------------------------------------------------
echo(
echo Building resource pack...
echo(
echo ------------------------------------------------------------
cd Tools
python py\copy_block_textures.py
cd..

echo ------------------------------------------------------------
echo(
echo Importing assets...
echo(
echo ------------------------------------------------------------
python Tools\py\generate_asset_import_settings.py
"%editorPath%\UE4Editor-Cmd.exe" "%ddp%\UE4Project\Dungeons.uproject" -run=ImportAssets -nosourcecontrol "-importsettings=%ddp%\Tools\tmp_import_settings.json"
del /s Tools\tmp_import_settings.json  >nul 2>&1

echo ------------------------------------------------------------
echo(
echo Cooking assets...
echo(
echo ------------------------------------------------------------
del /S Dungeons\*.uasset
del /S Dungeons\*.ubulk
del /S Dungeons\*.uexp
del /S Dungeons\*.umap
del /S Dungeons\*.ufont
"%editorPath%\UE4Editor-Cmd.exe" "%ddp%\UE4Project\Dungeons.uproject" -run=cook -targetplatform=WindowsNoEditor
robocopy /job:Tools\configs\copy_cooked_assets

echo ------------------------------------------------------------
echo(
echo Packing...
echo(
echo ------------------------------------------------------------
python Tools\py\u4pak.py pack "%packageOutput%" Dungeons -p

echo ------------------------------------------------------------
echo(
echo Packing is done. You can close this window now.
echo(
echo ------------------------------------------------------------

pause