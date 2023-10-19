import argparse
from PIL import Image


def convert_webp_to_png(input_path, output_path):
    with Image.open(input_path) as im:
        im.save(output_path, 'PNG')
    print(f"File converted and saved at {output_path}")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description='Convert WEBP files to PNG format.')
    parser.add_argument('input_path', type=str,
                        help='Path to the WEBP file to be converted.')
    parser.add_argument('output_path', type=str,
                        help='Path to save the converted PNG file.')

    args = parser.parse_args()

    convert_webp_to_png(args.input_path, args.output_path)
