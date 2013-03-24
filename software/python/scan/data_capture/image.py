import os
import cv2

class Image:
    """
    Class: Image
    Stores all the information relevant to one captured image from the
    environment. This includes the patterns projected on the object when the
    image was taken, the camera that took the image, and the image data itself,
    in matrix form.

    Properties:
    Patterns - list of <GeneratedPattern>s; light patterns projected on
    the object when the image was taken
    camera - The <Camera> that took the image
    data - ndarray The pixel data comprising the image
    """
    def __init__(self, data, camera, patterns):
        self.data = data
        self.camera = camera
        self.patterns = patterns

def load_from_directory(dir_name):
    """
    Function: load_from_directory
    Loads all of the image files in a directory and returns them as a list of <Image>s

    Parameters:
    string dir_name - The name of the directory

    Returns:
    A list of <Image>s read from the directory

    """
    # list of images to return
    images = []

    # try to add each item in the directory as an image
    for f in os.listdir(dir_name):
        data = cv2.imread(os.path.join(dir_name, f))

        # if data collected, add the Image
        if data != None:
            images.append(Image(data, None, None))

    # return the list of images
    return images