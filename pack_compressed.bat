@echo off
title [1/5] Applying settings...
echo ------------------------------------------------------------
echo(
echo [1/5] Applying settings...
echo(
echo ------------------------------------------------------------
SET "ddp=%~dp0"
SET "ddp=%ddp:~0,-1%"
SET /p editorPath= < Tools\user_settings\editor_directory.txt
SET /p packageOutput= < Tools\user_settings\package_output.txt

title [2/5] Building resource pack...
echo ------------------------------------------------------------
echo(
echo [2/5] Building resource pack...
echo(
echo ------------------------------------------------------------
cd Tools
python py\copy_block_textures.py
cd..

title [3/5] Importing assets...
echo ------------------------------------------------------------
echo(
echo [3/5] Importing assets...
echo(
echo ------------------------------------------------------------
python Tools\py\generate_asset_import_settings.py
"%editorPath%\UE4Editor-Cmd.exe" "%ddp%\UE4Project\Dungeons.uproject" -run=ImportAssets -nosourcecontrol "-importsettings=%ddp%\Tools\tmp_import_settings.json"
del /s Tools\tmp_import_settings.json  >nul 2>&1

title [4/5] Cooking assets...
echo ------------------------------------------------------------
echo(
echo [4/5]Cooking assets...
echo(
echo ------------------------------------------------------------
del /S Dungeons\*.uasset
del /S Dungeons\*.ubulk
del /S Dungeons\*.uexp
del /S Dungeons\*.umap
del /S Dungeons\*.ufont
"%editorPath%\UE4Editor-Cmd.exe" "%ddp%\UE4Project\Dungeons.uproject" -run=cook -targetplatform=WindowsNoEditor

robocopy /job:Tools\configs\copy_cooked_assets

robocopy /S Precooked Dungeons 

title [5/5] Packing...
echo ------------------------------------------------------------
echo(
echo [5/5] Packing...
echo(
echo ------------------------------------------------------------
python Tools\py\u4pak.py pack "1-ComplianceDungeons_beta.pak" Dungeons -z -p

echo ------------------------------------------------------------
echo(
echo Packing is done. You can close this window now.
echo(
echo ------------------------------------------------------------

pause