# Dominant Color Extractor

A lightweight CLI tool to extract the dominant color(s) from an image using KMeans clustering on RGB pixels. It identifies top N colors sorted by pixel frequency, outputs in RGB or HEX format with percentages, and handles edge cases gracefully for reliable use.

## Installation

1. Clone the repository:
   ```bash
   git clone <your-repo-url>
   cd dominant-color-extractor
   ```

2. Install Python dependencies:
   ```bash
   pip install Pillow numpy scikit-learn
   ```

## Usage

Run from the project root:

```bash
python src/main.py image.jpg
```
Extracts the single dominant color in RGB format (e.g., `(255, 0, 0) (45.2%)`).

```bash
python src/main.py image.jpg --num-colors 5 --format hex
```
Extracts top 5 colors in HEX format (e.g., `#FF0000 (45.2%)`).

```bash
python src/main.py --help
```
Shows full help:

```
usage: main.py [-h] [--num-colors NUM_COLORS] [--format {rgb,hex}] image

CLI tool to extract dominant color(s) from images via KMeans clustering on RGB
pixels.

positional arguments:
  image                 Path to the input image file

options:
  -h, --help            show this help message and exit
  --num-colors NUM_COLORS, -n NUM_COLORS
                        Number of dominant colors to extract (default: 1)
  --format {rgb,hex}, -f {rgb,hex}
                        Output format: 'rgb' or 'hex' (default: rgb)
```

Errors and warnings are printed to stderr (e.g., file not found, invalid image).

## Features

- KMeans clustering (scikit-learn) on image pixels for accurate dominant colors
- Configurable number of colors (`--num-colors`, default: 1), auto-caps to pixel count
- Output formats: RGB or HEX, with pixel count percentages
- Colors sorted by descending frequency
- Robust error handling: invalid files/images, empty pixels, invalid args
- Reproducible results (`random_state=42`)
- Clean argparse interface with helpful messages

## Dependencies

- Python 3.6+ (argparse is stdlib)
- [Pillow](https://pillow.readthedocs.io/)
- [NumPy](https://numpy.org/)
- [scikit-learn](https://scikit-learn.org/)

## License

MIT