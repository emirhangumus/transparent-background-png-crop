# PNG Transparent Background Cropping Script with Customizable Transparency Threshold

This Python script allows you to crop PNG images by removing fully transparent pixels around the edges. The transparency threshold can be customized, allowing you to define which pixels are considered "non-transparent" based on their alpha channel value. It uses the `Pillow` library for image processing and is executed via the command line.

## Features

- Automatically crops the transparent areas from the edges of PNG images.
- Customizable minimum transparency threshold to define "non-transparent" pixels.
- Command-line interface for flexible usage.

## Prerequisites

Ensure that you have Python and the necessary libraries installed before running the script.

### Install Pillow

You can install the required `Pillow` library with pip:

```bash
pip install Pillow
```

## Usage

To use the script, run the following command in your terminal:

```bash
python png_transparent_crop.py input_image.png output_image.png --min_transparency 128
```

Replace `input_image.png` with the path to your input PNG image and `output_image.png` with the desired output file name. The `--min_transparency` flag allows you to specify the minimum alpha channel value for a pixel to be considered non-transparent. The default value is 0, meaning all transparent pixels will be cropped.

## Example

Here's an example of how the script can be used:

```bash
python png_transparent_crop.py example.png cropped_example.png --min_transparency 2
```

This command will crop the image `example.png` by removing fully transparent pixels with an alpha channel value less than 2. The resulting cropped image will be saved as `cropped_example.png`.

## License

This script is licensed under the MIT License. See the [LICENSE](LICENSE) file for more information.

## Acknowledgements

- [Pillow](https://python-pillow.org/) - The friendly PIL fork by Alex Clark and Contributors
