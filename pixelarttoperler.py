import cv2
import numpy as np

def find_pixel_size(image):
    h, w, _ = image.shape
    horizontal_count = 1
    vertical_count = 1
    horizontal_sizes = []
    vertical_sizes = []

    horizontal_gap = 0
    vertical_gap = 0

    for i in range(1, w):
        if np.any(image[:, i, :] != image[:, i - 1, :]):
            horizontal_count += 1
            if horizontal_gap > 0:
                horizontal_sizes.append(horizontal_gap)
                horizontal_gap = 0
        else:
            horizontal_gap += 1

    for i in range(1, h):
        if np.any(image[i, :, :] != image[i - 1, :, :]):
            vertical_count += 1
            if vertical_gap > 0:
                vertical_sizes.append(vertical_gap)
                vertical_gap = 0
        else:
            vertical_gap += 1

    mean_horizontal_size = np.mean(horizontal_sizes)
    std_horizontal_size = np.std(horizontal_sizes)
    mean_vertical_size = np.mean(vertical_sizes)
    std_vertical_size = np.std(vertical_sizes)

    pixel_size = min(w // horizontal_count, h // vertical_count)

    print(f"Mean horizontal size: {mean_horizontal_size}, std dev: {std_horizontal_size}")
    print(f"Mean vertical size: {mean_vertical_size}, std dev: {std_vertical_size}")

    return pixel_size


def insert_grid(image, pixel_size, grid_color=(25, 25, 25), thickness=2):
    h, w, _ = image.shape
    new_w = w + (w // pixel_size) * thickness
    new_h = h + (h // pixel_size) * thickness
    new_image = np.zeros((new_h, new_w, 3), dtype=np.uint8)

    for y in range(h):
        for x in range(w):
            new_x = x + x // pixel_size * thickness
            new_y = y + y // pixel_size * thickness

            new_image[new_y:new_y+1, new_x:new_x+1] = image[y, x]

            if (x + 1) % pixel_size == 0 and x + 1 < w:
                new_image[new_y:new_y+1, new_x+1:new_x+1+thickness] = grid_color

            if (y + 1) % pixel_size == 0 and y + 1 < h:
                new_image[new_y+1:new_y+1+thickness, new_x:new_x+1] = grid_color

    return new_image


def scale_pixel_art(image, min_size_pixels):
    h, w, _ = image.shape

    if h >= min_size_pixels and w >= min_size_pixels:
        return image

    scale_factor = max(min_size_pixels / h, min_size_pixels / w)
    scale_factor = int(np.ceil(scale_factor))

    new_h = h * scale_factor
    new_w = w * scale_factor

    scaled_image = np.zeros((new_h, new_w, 3), dtype=np.uint8)

    for y in range(h):
        for x in range(w):
            color = image[y, x]
            scaled_image[y * scale_factor:(y + 1) * scale_factor, x * scale_factor:(x + 1) * scale_factor] = color

    return scaled_image

def create_color_palette(image, square_size_inches=3, ppi=100, grid_color=(255, 255, 255), outline_thickness=2, max_colors_per_row=4, row_space_inches=0.5):
    unique_colors = np.unique(image.reshape(-1, image.shape[-1]), axis=0)
    unique_colors = [tuple(color) for color in unique_colors.tolist()]

    if grid_color in unique_colors:
        unique_colors.remove(grid_color)

    square_size_pixels = square_size_inches * ppi
    margin_pixels = square_size_pixels // 4
    count_space_pixels = square_size_pixels // 2
    row_space_pixels = int(row_space_inches * ppi)
    num_rows = int(np.ceil(len(unique_colors) / max_colors_per_row))

    canvas_width = (square_size_pixels + margin_pixels * 2) * max_colors_per_row + count_space_pixels * (max_colors_per_row - 1)
    canvas_height = (square_size_pixels + margin_pixels * 2 + row_space_pixels) * num_rows - row_space_pixels
    max_empty_space = int(canvas_height * 0.1)
    canvas_height = min(canvas_height + max_empty_space, canvas_height * 2)

    palette_image = np.ones((canvas_height, canvas_width, 3), dtype=np.uint8) * 255

    for idx, color in enumerate(unique_colors):
        row = idx // max_colors_per_row
        col = idx % max_colors_per_row

        x_start = (square_size_pixels + margin_pixels * 2 + count_space_pixels) * col + margin_pixels
        y_start = margin_pixels + row * (square_size_pixels + margin_pixels * 2 + row_space_pixels)

        palette_image[y_start:y_start + square_size_pixels, x_start:x_start + square_size_pixels] = color

        # Invert color of the border pixels for negative outline
        palette_image[y_start:y_start + outline_thickness, x_start:x_start + square_size_pixels] = 255 - palette_image[y_start:y_start + outline_thickness, x_start:x_start + square_size_pixels]
        palette_image[y_start + square_size_pixels - outline_thickness:y_start + square_size_pixels, x_start:x_start + square_size_pixels] = 255 - palette_image[y_start + square_size_pixels - outline_thickness:y_start + square_size_pixels, x_start:x_start + square_size_pixels]
        palette_image[y_start:y_start + square_size_pixels, x_start:x_start + outline_thickness] = 255 - palette_image[y_start:y_start + square_size_pixels, x_start:x_start + outline_thickness]
        palette_image[y_start:y_start + square_size_pixels, x_start + square_size_pixels - outline_thickness:x_start + square_size_pixels] = 255 - palette_image[y_start:y_start + square_size_pixels, x_start + square_size_pixels - outline_thickness:x_start + square_size_pixels]

    return palette_image

def main():
    input_image_path = "swablu.png"
    output_image_path = "swablu_grid.png"
    color_palette_path = "swablu_palette.png"
    # input_image_path = "C:\\Users\\gnoej\\Downloads\\a9e0d44235267d1.png"
    # output_image_path = "spamton_grid.png"
    # color_palette_path = "spamton_palette.png"
    min_size_pixels = 576

    image = cv2.imread(input_image_path)

    scaled_image = scale_pixel_art(image, min_size_pixels)

    pixel_size = find_pixel_size(scaled_image)
    
    grid_image = insert_grid(scaled_image, pixel_size)

    cv2.imwrite(output_image_path, grid_image)

    color_palette_image = create_color_palette(grid_image)
    cv2.imwrite(color_palette_path, color_palette_image)

    print(f"Pixel size detected: {pixel_size}x{pixel_size}")
    print(f"Output image saved as {output_image_path}")
    print(f"Color palette image saved as {color_palette_path}")

if __name__ == "__main__":
    main()
