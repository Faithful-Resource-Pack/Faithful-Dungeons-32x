![header](https://i.imgur.com/8GKOO62.png)

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
![](https://i.imgur.com/ienKLnB.png)  
When you've installed the add-on, make sure it's enabled by ticking the box below in the Add-ons tab and checking if the add-on is present in the list. (if it's not, untick the box, find the add-on and enable it manually.)  
![](https://i.imgur.com/eEqly35.png)  
Now you can import the default model by going to File > Import, selecting Skeleton mesh (.psk) and navigating to the model.  
![](https://i.imgur.com/p8nQCBY.png)  
Now that you've imported the model you can scale, move and rotate your custom one to fit the default like so:  
![](https://i.imgur.com/V3U6CKk.png)  
**TIP:** You can use a present view (like topdown) by clicking any of these points on the top right corner  for more accurate positioning.  
![](https://i.imgur.com/YHsPzwZ.png)  
You don't have to be super precise though - just try to roughly match the position and size of the default model.  

When you're finished, delete the default model by selecting it, right clicking it and selecting Delete.  

### 7. Export your model as FBX
You can export your model into the FBX format by going to File > Export and then selecting FBX.  
![](https://i.imgur.com/kWZm481.png)  
In the widnow that pops up you can navigate to your desired file location. That's not all tough - we'll also need to change some settings in the tab on the right side. Set the scale in the Transform tab to 0.01 and then, in the Geometry tab, set Smoothing to Face.  
![](https://i.imgur.com/HGml35u.png)  
Next, look at the model's name in the default game files and name your model that.  
![](https://i.imgur.com/8fz2F8K.png)  
Finally, click the blue Export button to finish the process.  
![](https://i.imgur.com/hTgN7Gx.png)  
Congratulations! You've made it through the entire modelling process and now have a model that will function properly when put into a mod!  

This is the end of the tutorial for those of you that are making items like the apple health drop, which do not require a render. But if you're making a model of a weapon - or just need to make a render - get ready for the next part:  

## PART 2: RENDERING
### 0. Import your model
(if you've followed the tutorial up to this part, you can skip this step.)  

To import the model ripped from Minecraft: Dungeons we will need to install the Import Unreal Skeletal Mesh add-on for Blender. To do that, go to Edit > Preferences, then in the window that pops up go into the Add-ons tab, click the install button and navigate to where you saved the.py file.  
![](https://i.imgur.com/fCHtBF1.png)  
When you've installed the add-on, make sure it's enabled by ticking the box below in the Add-ons tab and checking if the add-on is present in the list. (if it's not, untick the box, find the add-on and enable it manually.)  
![](https://i.imgur.com/rYNtWu9.png)  
Now you can import the default model by going to File > Import, selecting Skeleton mesh (.psk) and navigating to the model.  
![](https://i.imgur.com/jsNQY8x.png)  

### 1. Set up a material (again)
First, check if the Use Nodes button in the red checkered circle tab is blue. If it's not, click on it to make it blue.  
![](https://i.imgur.com/EsZDtMy.png)  
Then switch to the Shader Editor using this menu up top:  
![](https://i.imgur.com/6iBFkoE.png)  
The tab should change into a node editor. Enlarge it so you can see it better and then make it look like this:  
![](https://i.imgur.com/LuvEBYN.png)  
**TIP:** You can add a node by pressing Shift + A, selecting Search and then typing the node's name. You can also zoom in and out using Ctrl + scroll.
TO connect two nodes together just click and drag from one point (as seen above) to another with your mouse.  
![](https://i.imgur.com/miyObJ1.png)  

**NOTE: The text version of this tutorial is not finished yet! You can find a finished image version of the tutorial ![here](https://cdn.discordapp.com/attachments/715508829458006077/749616847011446854/modelling_rendering_tutorial_2.png).**
