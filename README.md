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

## input

![swablu, a small bird with clouds as wings](https://github.com/gnoejuan/PixelArtToPerler/blob/39c37a960685406c576ffa35531f888342c14354/swablu.png)

```shell
Mean horizontal size: 14.0, std dev: 0.0
Mean vertical size: 14.0, std dev: 0.0
Pixel size detected: 14x14
Output image saved as swablu_grid.png
Color palette image saved as swablu_palette.png
```

## output

![the same swablu image, but with a grid and scaled up](https://github.com/gnoejuan/PixelArtToPerler/blob/39c37a960685406c576ffa35531f888342c14354/swablu_grid.png)
![the unique colors detected](https://github.com/gnoejuan/PixelArtToPerler/blob/39c37a960685406c576ffa35531f888342c14354/swablu_palette.png)

# A bad image output

## input


<details>

<summary>A large example image</summary>
    
![A dangling puppet with a certain horror aspect](https://github.com/gnoejuan/PixelArtToPerler/blob/39c37a960685406c576ffa35531f888342c14354/a9e0d44235267d1.png)
    
</details>


```shell
Mean horizontal size: 13.493506493506494, std dev: 19.178331507011112
Mean vertical size: 12.655172413793103, std dev: 5.510340511845015
Pixel size detected: 13x13
Output image saved as spamton_grid.png
Color palette image saved as spamton_palette.png
```

<details>

<summary>2 large output images</summary>
    
![the same puppet, with the grid not lined up with the pixels.](https://github.com/gnoejuan/PixelArtToPerler/blob/39c37a960685406c576ffa35531f888342c14354/spamton_grid.png)

![the unique colors detected](https://github.com/gnoejuan/PixelArtToPerler/blob/39c37a960685406c576ffa35531f888342c14354/spamton_palette.png)
    
</details>
