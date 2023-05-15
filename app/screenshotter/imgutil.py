from PIL import Image

def pad_square(image: Image.Image, fill_color) -> Image.Image:
    """Pads an image to be square.
    """
    side = max(image.size) # square side is the longest dimension
    box = ((side - image.size[0]) // 2, (side - image.size[1]) // 2)
    res = Image.new(image.mode, (side, side), fill_color)
    res.paste(image, box)
    return res