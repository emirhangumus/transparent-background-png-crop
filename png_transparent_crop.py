import argparse
from PIL import Image

def find_non_transparent_edges(image, MIN_TRANSPARENCY):
    """Finds the first non-transparent pixel from all 4 edges of the image."""
    pixels = image.load()
    width, height = image.size

    # Initialize coordinates for cropping
    left, top, right, bottom = 0, 0, width, height

    # Find the left edge (from left to right)
    for x in range(width):
        for y in range(height):
            if pixels[x, y][3] > MIN_TRANSPARENCY:
                left = x
                break
        if left != 0:
            break

    # Find the right edge (from right to left)
    for x in range(width - 1, -1, -1):
        for y in range(height):
            if pixels[x, y][3] > MIN_TRANSPARENCY:
                right = x + 1
                break
        if right != width:
            break

    # Find the top edge (from top to bottom)
    for y in range(height):
        for x in range(width):
            if pixels[x, y][3] > MIN_TRANSPARENCY:
                top = y
                break
        if top != 0:
            break

    # Find the bottom edge (from bottom to top)
    for y in range(height - 1, -1, -1):
        for x in range(width):
            if pixels[x, y][3] > MIN_TRANSPARENCY:
                bottom = y + 1
                break
        if bottom != height:
            break

    return left, top, right, bottom

def crop_transparent_background(input_path, output_path, MIN_TRANSPARENCY):
    image = Image.open(input_path).convert("RGBA")

    left, top, right, bottom = find_non_transparent_edges(image, MIN_TRANSPARENCY)
    cropped_image = image.crop((left, top, right, bottom))

    # Save the cropped image
    cropped_image.save(output_path)
    print(f"Image cropped and saved to {output_path}")

def main():
    parser = argparse.ArgumentParser(description="Crop PNG image by removing transparent background.")
    
    parser.add_argument("input_file", help="Path to the input PNG file")
    parser.add_argument("output_file", help="Path to save the cropped PNG file")
    # create a optional argument to set the minimum transparency
    parser.add_argument("--min_transparency", type=int, default=0, help="Minimum transparency value to consider a pixel as non-transparent (0-255)")

    args = parser.parse_args()

    crop_transparent_background(args.input_file, args.output_file, args.min_transparency)

if __name__ == "__main__":
    main()
