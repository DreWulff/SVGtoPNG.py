import os
os.environ["PATH"] += r";C:\Program Files\GTK3-Runtime Win64\bin"

import cairosvg

def convert_svg_to_png(name: str, width: int=None) -> None:
    """
    Converts an SVG file to a PNG file with the specified dimensions.

    Parameters:
        svg_file: Name to the input SVG file.
        png_file: Name to save the output PNG file.
        width: Desired width of the PNG (optional).
    """
    svg_name = name + ".svg"
    png_name = name + ".png"

    # Read the SVG content
    with open(os.path.dirname(os.path.abspath(__file__)) + "\\" + svg_name, 'rb') as svg:
        svg_content = svg.read()
    
    # Convert to PNG
    cairosvg.svg2png(
        bytestring=svg_content,
        write_to=os.path.dirname(os.path.abspath(__file__)) + "\\" + png_name,
        output_width=width,
        output_height=width
    )
    print(f"PNG saved to {png_name}")

# Example usage
name = input("Name of .svg file to convert: ")
size = input("Size of output (square of NxN pixels): ")
convert_svg_to_png(name, width=int(size))