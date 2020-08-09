# How to use this tool:  

## Requirements:  
- [Blender](https://www.blender.org/)  
- [Python 3.8+](https://www.python.org/)  
    - And Pillow module  
- [Unreal Engine 4](https://www.unrealengine.com/en-US/?sessionInvalidated=true) version 4.22.x  

## Step by step: Blender  
> Thanks for [@CCCode](https://github.com/EvenTorset) for creating this model  

- Open `LoadingSpinnerBlock.blend` with Blender  
- Drag the green bar at the bottom at the begining of the animation  
![](https://i.imgur.com/6keqELu.png)  

- Go to the `Shading` tab at the top of the screen  
![](https://i.imgur.com/CYRvplh.png)  

- Click on the blank face of the block in front of you (you get a green outline surrounding it)  
![](https://i.imgur.com/LLW8Opj.png)  

- In the bottom slide, in the Orange Area, click on the cross & import a new textures:  

    - A. ![](https://i.imgur.com/PF4KKid.png)  
    - B. ![](https://i.imgur.com/q6Jvh6N.png)  
    - C. ![](https://i.imgur.com/CeQdT5M.png)  

- Drag the green slider until a new face  
    - Remake previous step & this step until all face are done  
    - :warning: The second side of the animation got 2 orange tab: this is because the animation file use a non-euclidian cube, there is 2 textures for 1 face.  

> Optionnal: You can go to the `Texture Paint` tab & press the space bar to see your'e texture on the model.  

- Return to the `Layout` tab, and in the bottom right, change the output path
  ![](https://i.imgur.com/urGU7Qm.png)  

- Finally: at the top left, click on render, then render animation, all screenshot should be in where you set the output path.
  ![](https://i.imgur.com/ELPhW9D.png)  
  
## Step by step: Python  
### Install Pillow:  
As I said before, you will need the Pillow module, install it (if you doens't have already installed it).  
- Press `Windows` + `R` then type `cmd` then `enter`  
- Write this command: `pip install pillow` then press `enter`  
![](https://i.imgur.com/eyBaK1W.png)  

---

:heavy_check_mark: **If you already have Pillow installed, you can just double click the `Merge.py` script to get the `loader.png`.**  
:warning: **The script need to be in the same file as screenshots took by Blender**  

## Step by step: Unreal Engine 4  

- You need to put the `loader.png` file in this folder: `UE4Project\Content\UI\Materials\LoadingScreens\Misc`  
- Open your `Dungeons.uproject` from `UE4Project/`  
- Find the file in your project & open it:  
![](https://i.imgur.com/Adxzs2H.png)  

- Then you have to change settings on the right tab:  
    - Compression Settings → BC7  
    - Mip Gen Settings → NoMipmaps  
    - Texture Group → UI  
  ![](https://i.imgur.com/aYart0i.png)  

**Everything should be good, you now just have to package your files using the [dokucraft tool](https://github.com/Dokucraft/Dungeons-Mod-Kit)**