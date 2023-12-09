from PIL import Image
#from dalle_pytorch import DALLE

class DALLE3:
    def __init__(self):
        self.goal = "image-generation" # DALLE.load_model('path_to_your_model')

    def generate_image(self, text):
        image_tensor = self.model.generate_images(text)
        image = Image.fromarray(image_tensor.numpy())
        return image