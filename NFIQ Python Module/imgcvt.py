# from PIL import Image

# # Open the original image
# image = Image.open('fp1.jpg')

# # Convert to 8-bit grayscale
# gray_8bit = image.convert('L')

# # Save the converted image
# gray_8bit.save('output_8bit.png')


from PIL import Image

def convert_and_set_ppi(input_path, output_8bit_path, output_1bit_path, ppi=500, threshold=128):
    """
    Converts an image to 8-bit and 1-bit grayscale and sets its resolution to the specified PPI.

    Parameters:
    - input_path (str): Path to the input image.
    - output_8bit_path (str): Path to save the 8-bit grayscale image.
    - output_1bit_path (str): Path to save the 1-bit grayscale image.
    - ppi (int): Desired pixels per inch (default is 500).
    - threshold (int): Threshold for 1-bit conversion (default is 128).
    """
    # Open the original image
    image = Image.open(input_path)
    print(f"Original image mode: {image.mode}, size: {image.size}, info: {image.info}")

    # Convert to 8-bit grayscale
    gray_8bit = image.convert('L')
    print("Converted to 8-bit grayscale.")

    # Save the 8-bit grayscale image with 500 PPI
    gray_8bit.save(output_8bit_path, dpi=(ppi, ppi))
    print(f"Saved 8-bit grayscale image to {output_8bit_path} with {ppi} PPI.")

    # Convert to 1-bit grayscale using a fixed threshold
    gray_1bit = gray_8bit.point(lambda x: 0 if x < threshold else 255, '1')
    print("Converted to 1-bit grayscale.")

    # Save the 1-bit grayscale image with 500 PPI
    gray_1bit.save(output_1bit_path, dpi=(ppi, ppi))
    print(f"Saved 1-bit grayscale image to {output_1bit_path} with {ppi} PPI.")

# Example usage
if __name__ == "__main__":
    convert_and_set_ppi(
        input_path='newfp2_output_1bit_.png',
        output_8bit_path='newfp3_output_8bit_.png',
        output_1bit_path='newfp3_output_1bit_.png',
        ppi=500,
        threshold=128  # Adjust threshold as needed
    )
