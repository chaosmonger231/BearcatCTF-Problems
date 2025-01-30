from PIL import Image

image_names = [
    "A_0_0.png", "A_0_1.png", "A_0_2.png", "A_0_3.png",
    "B_1_0.png", "B_1_1.png", "B_1_2.png", "B_1_3.png",
    "C_2_0.png", "C_2_1.png", "C_2_2.png", "C_2_3.png"
]

images = [Image.open(name) for name in image_names]

img_width, img_height = images[0].size

# Define grid dimensions

columns = 4
rows = 3

full_image = Image.new("RGB", (columns * img_width, rows * img_height))

for idx, image in enumerate(images):
    x = (idx % columns) * img_width
    y = (idx // columns) * img_height
    full_image.paste(image, (x,y))

full_image.show()
full_image.save("Target.png")
