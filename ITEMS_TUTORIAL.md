![header](https://raw.githubusercontent.com/Faithful-Dungeons/Resource-Pack/master/UE4Project/Content/UI/Materials/Menu/logo_mainscreen.png)
# MAKE AND RENDER ITEMS AND EQUIPMENT: THE GUIDE
> For complete 3D Modeling Rookies
> Made by Pomik108 & Adapted to Markdown by Juknum

When making a mod for Minecraft: Dungeons, it is important to know that most weapons, melee and ranged, are not like items in Java or Bedrock Edition - their model is not generated from their texture, but rather it's made to fit it. This tutorial will show you how to make and render models for your own, custom item textures. Never worked with any 3D modelling software of any kind? Not to worry, this tutorial will show you exactly what to do, without any need for previous 3D modelling knowledge! Let's get started:

### You will need:
- [Blockbench 3.6.6+](https://blockbench.net/)
- [Blender 2.80+](https://www.blender.org/)
- Import Unreal Skeletal Mesh add-on for Blender (download below)
- Minecraft: Dungeons default game files

## PART 0: CONTROLS AND HOTKEYS
### Blockbench:
![](https://i.imgur.com/rlI2rPa.png)
### Blender:
![](https://i.imgur.com/blQ0Ph4.png)
> If you are on Mac: use `Cmd` instead of `Ctrl`

### * What if I don't have a 3rd button mouse/numpad?
> you can skip this part if you've got a normal keyboard & mouse.

That's no problem! Blender allows you to emulate both of these, allowing you to access the controls you need.
Here's how to do it:

1. Go to Edit tab up top, then select Preferences. A window should pop up.
![](https://i.imgur.com/Yp9oT3f.png)

2. In that window, go to the Input tab and check the `Emulate 3 Button Mouse` and `Emulate Numpad` boxes. ![](https://i.imgur.com/dpFHbYI.png) 
By default, `alt`+`LMB` will be registered as `MMB`. If you emulate the numpad, you can access the numpad hotkeys by pressing numbers in the top row of the keyboard (do NOT press shift!). The emulation will overide some existing hotkeys placed on the numerical row, but we don't need them anyway, so don't worry about that.

Additionally, if you've got an Apple Magic Mouse, on top of having to emulate a 3 button mouse the view controls are a bit different:  
![](https://i.imgur.com/1EcYFCb.png)
> All other controls are the same.

## PART 1: MODELLING
### 1. Prepare a texture
When you're finished making a texture for your item, it should look something like this:
![](https://i.imgur.com/n483Ej8.png)  
This is the texture that you want to use in your mod. For our purposes we'll need another, slightly modified texture. Make a copy of your texture and modify that. For your texture to work properly with Blockbench, you need to get rid of all the parts that you do not want to be included in the model. In this case we need to remove the palette thingy, but depending on the texture you might also need to make the background transparent etc.  
This is how your texture should look before importing to Blockbench:
![](https://i.imgur.com/EybsujV.png)

Now with that out of the way, let's get to modelling itself!

### 2. Extrude texture in Blockbench
Upon opening Blockbench you should get to this screen:
![](https://i.imgur.com/t8M7XQy.png)  
Make a new generic model and name it whatever you want. **DO NOT** change the texture dimensions in the window that pops up, it will break things!  
![](https://i.imgur.com/ULuju9i.png)  
Before importing the texture, make sure that your snapping grid resolution is 16x16. You can do that by going to `File > Settings...` and then the Snapping tab.  
![](https://i.imgur.com/NWghNeM.png)  
Now go to `File > Import` and select `Extrude Texture`. **Do not** change anything in the window that pops up. You should get something like this:  
![](https://i.imgur.com/AppS5Vx.png)  
Now move the model so that it's centered on the grid.  
![](https://i.imgur.com/AGxImrR.png)  
Finally, right click on the texture under the Textures tab, and then change the file to your original, unmodified texture.
![](https://i.imgur.com/a7CYSMu.png)  
If you done that correctly, you shouldn't see a visual change.

### 3. Export the model as OBJ
You can do that by going to `File > Export` and then selecting `Export OBJ Model`.
![](https://i.imgur.com/0ZdKX3R.png)  
Save the OBJ file somewhere you can find it - you'll need it in the next step:

### 4. Import the model into Blender
> Time to get our hands dirty in Blender!

Upon opening you should see small window pop up - don't change anything in there, just clicl away so the window disappears.  
Next, delete the default cube by selecting it, right clicking and selecting `Delete`.  
Now you can import your OBJ model by going to `File > Import`, selecting `Wavefront (.obj)` and then navigating to your model.  
![](https://i.imgur.com/yLpIWJH.png)  
You might notice that your model doesn't show any textures - that is completely normal, it's just blender's default view mode. Switch to Material mode (top right) to see the texture.  
![](https://i.imgur.com/aELslBc.png)  
Your model should then look something like this:  
![](https://i.imgur.com/q63Qjlh.png)  
Additionally, you can box select all the part of your model, shift-click on one of them and press `Ctrl` + `J` to merge all parts into one like so:  
![](https://i.imgur.com/d6emann.png)  
This will make it easier to edit the model all at once.
We don't want the textures this blurry though! To fix that you'll need to   

### 5. Set up a material
You can edit your material by clicking on the red checkered circle in the tab on the right:  
![](https://i.imgur.com/12i2rgD.png)  
First you need to name your material correctly. Go to the location of the default texture in the Dungeons game files (assuming you've extracted them); you should see a bunch of files besides the texture. Locate the one with the .mat extension and copy its name (without the extension).  
![](https://i.imgur.com/t2I7hre.png)  
Next, copy the name into this field at the top of the Material Properties tab, and press Enter.  
![](https://i.imgur.com/Pas2EG4.png)  
Now you can fix the texture filtering by going into this dropdown menu and selecting Closest.  
![](https://i.imgur.com/vtITG8N.png)  
If you've done everything correctly, your model should look roughly like this:  
![](https://i.imgur.com/ov1P1PW.png)  
### 6. Position and scale your model
Now it's time to position your model to fit the default scale and placement. To do that we're going to use the default item model.  
For importing Unreal skeletal meshes into Blender we're gonna need the Import Unreal Skeletal Mesh add-on. To install it, go to `Edit > Preferences`, then in the window that pops up go into the Add-ons tab, click the Install button and navigate to where you saved the .py file 
