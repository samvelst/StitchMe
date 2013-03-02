# Samvel Stepanyan
# StitchMe - stitch two pictures together side by side

import sys
import Image

def load_images():
    try:
        image_name1 = sys.argv[1]
        image_name2 = sys.argv[2]
    
        image1 = Image.open(image_name1)
        image2 = Image.open(image_name2)

        return (image1, image2)

    except IOError, e:
        print e
        sys.exit()


def main():
    image1, image2 = load_images()

if __name__ == '__main__':
    main()
