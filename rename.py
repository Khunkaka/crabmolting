import os

for count, filename in enumerate(os.listdir("crab_image")):
    dist = "CB" + str(count) + ".jpg"
    os.rename('crab_image/' + filename, 'crab_image/' + dist)