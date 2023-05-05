# PixelArtToPerler
A simple python script to generate a grid over pixel art and the unique colors found within the image to help plan perler beard art.

Should also "upscale" to a readable size. 

Generally, there are a minimum of three variables to update, found in the main block near the bottom.

```python
def main():
    input_image_path = "swablu.png"
    output_image_path = "swablu_grid.png"
    color_palette_path = "swablu_palette.png"
```

The script will also check the standard deviation of the height and width. From my observations, a standard deviation other than 0, means this script won't work.

# A good image output

```shell
Mean horizontal size: 14.0, std dev: 0.0
Mean vertical size: 14.0, std dev: 0.0
Pixel size detected: 14x14
Output image saved as swablu_grid.png
Color palette image saved as swablu_palette.png
```

# A bad image output

```shell
Mean horizontal size: 13.493506493506494, std dev: 19.178331507011112
Mean vertical size: 12.655172413793103, std dev: 5.510340511845015
Pixel size detected: 13x13
Output image saved as spamton_grid.png
Color palette image saved as spamton_palette.png
```
