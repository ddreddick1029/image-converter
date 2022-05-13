from PIL import Image
import glob

# Thanks to SO user "dm2013" & GitHub user "amrrs"
for file in glob.glob("*.png"):
    open_image = Image.open(file)
    rgb_oi = open_image.convert('RGB')
    rgb_oi.save(file.replace("png", "jpg", quality=100))
