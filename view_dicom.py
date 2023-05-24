import pydicom as dicom
import cv2   

# specify your image path
image_path = 'data/train_images/sample.dcm'
import os

import kivy
kivy.require('1.11.1')

from kivy.app import App
from kivy.uix.image import Image
from kivy.core.window import Window
from kivy.uix.widget import Widget
from kivy.uix.boxlayout import BoxLayout


def getFilenamesRecurse(directory, ext = ".dcm"):
    retval = []
    if os.path.isdir(directory):
        for image in os.listdir(directory):
            fullfile = os.path.join(directory, image)
            print(fullfile)
            retval += getFilenamesRecurse(fullfile)
    else:
        print(directory)
        if directory.endswith(ext):
            retval += [directory]
    return retval

class InnerBox(BoxLayout):
    def __init__(self, **kwargs):
        super(InnerBox, self).__init__(**kwargs)

        self.filenames = getFilenamesRecurse('tciaDownload')
        self.imgIndex = 0

        # Create an instance of the Image widget
        self.img = Image(source=self.filenames[self.imgIndex])
        
        # Create a root widget to hold the image
        self.add_widget(self.img)
        
        # Bind keyboard events
        self._keyboard = Window.request_keyboard(self._keyboard_closed, self)
        self._keyboard.bind(on_key_down=self._on_keyboard_down)
        

    def _keyboard_closed(self):
        self._keyboard.unbind(on_key_down=self._on_keyboard_down)
        self._keyboard = None
    
    def _on_keyboard_down(self, keyboard, keycode, text, modifiers):
        if keycode[1] == 'left':
            self.imgIndex = (self.imgIndex - 1 + len(self.filenames)) % len(self.filenames)
        elif keycode[1] == 'right':
            self.imgIndex = (self.imgIndex + 1) % len(self.filenames)
        self.change_image(self.filenames[self.imgIndex])
        return True
    
    def change_image(self, image_path):
        print("Changing to " + image_path)
        ds = dicom.dcmread(image_path)
        pixel_array_numpy = ds.pixel_array

        image_format = '.jpg' # or '.png'
        outputPath = os.path.join("/tempfs", os.path.basename(image_path).replace('.dcm', image_format))
        outputPath = "curr.jpg"
        cv2.imwrite(outputPath, pixel_array_numpy)

        self.img.source = outputPath
        self.img.reload()

class ImageApp(App):
    def build(self):
        # Return the root widget as the main interface
        return InnerBox()
    

if __name__ == '__main__':
    ImageApp().run()

