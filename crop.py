import sys
from PIL import Image

try:
    from rembg import remove
    print("rembg imported")
except ImportError:
    print("rembg not installed")
    sys.exit(1)

img_path = "cover.png"
img = Image.open(img_path)
w, h = img.size

# The character is at the bottom. We crop the bottom half or something.
# Let's crop the bottom half first just in case.
# Actually, the user says "at the bottom".
# Let's crop the bottom 50% and horizontally center or full width.
bottom_half = img.crop((0, int(h*0.4), w, h))

# Remove background
output = remove(bottom_half)

# Save the output
output.save("character_extracted.png")
print("Saved character_extracted.png")
