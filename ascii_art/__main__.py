import argparse
from PIL import Image
from . import image_to_ascii


def save(path, ascii):
    """
    Saves ascii text into text file
    :param: path - path where to save file
    :param: ascii - ascii text
    """
    with open(path, 'w', encoding='utf-8') as file:
        file.write(ascii)
        file.close()


def main() -> int:
    """ASCII art generator with multiple customization parameters"""
    parser = argparse.ArgumentParser(description="Convert your favorite image into ASCII art")
    parser.add_argument("input", type=str, help="Path to image from which ASCII art will be generated")
    parser.add_argument("--width", type=int, help="Character width of ASCII art")
    parser.add_argument("--height", type=int, help="Character height of ASCII art")
    parser.add_argument(
        "--chars", type=str, default=" .',:;+*?%S#@", help="String containing characters to be seen in ASCII art"
    )
    parser.add_argument("--font", type=str, help="Font for calculating the character weights")
    parser.add_argument("--save", type=str, help="Save ascii output text, near input file (if output file not specified)", default='default', nargs='?')
    parser.add_argument("--invert", action="store_true", help="Whether the ASCII output color is inverted")
    parser.add_argument(
        "--normalize", action="store_true", help="Whether the weights of the provided ASCII characters are normalized"
    )

    args = parser.parse_args()

    image = Image.open(args.input)

    # Generate ASCII art from image
    ascii_art = image_to_ascii(image, args.width, args.height, args.chars, args.font, args.invert, args.normalize)

    # Save file if specified
    if args.save == 'default': pass
    elif args.save:
        save(args.save, ascii_art)
    else:
        args.save = image.filename[:image.filename.rfind('.'):] + '.txt'
        save(args.save, ascii_art)

    # Output to stdout
    print(ascii_art)

    return 0


if __name__ == "__main__":
    exit(main())
