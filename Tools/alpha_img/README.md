# How it works: 

- Pillow is required to use those programs!

```py
 python3 -m pip install --upgrade pip
 python3 -m pip install --upgrade Pillow
```

> Follow this tutorial if you don't know how to use commands: [YouTube Link](https://www.youtube.com/watch?v=Jey1GH8CERI)

## remove_alpha.py:
![header](https://i.imgur.com/tD2wjr8.png){:height="50%" width="50%"}
> From Alpha to Opaque

Set transparent pixel to 0 (make them opaque)
- Use `BASE_remove_alpha.png` as base
- Give`RESULT_remove_alpha.png`

## get_alpha.py:
![header](https://i.imgur.com/BVkyAEG.png){:height="50%" width="50%"}

> From Opaque to Alpha

Set **all** pixels transparents,
- Use `BASE_get_alpha.png` as base
- Give`RESULT_remove_alpha.png`

## merge_alpha_layers.py:
![header](https://i.imgur.com/UluBq4C.png){:height="50%" width="50%"}

> Merge easily both types

With this one, you can set "masks", one with opaque pixels, one with transparents pixels.
- Use `BASE_merge_alpha_layer0.png` as base for solid pixels.
- Use `BASE_merge_alpha_layer1.png` as base for transparent pixels.
- Give`RESULT_merge_alpha.png` as a fusion of them.
