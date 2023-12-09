import unittest
from src.models import generative_ai, text_bison, gpt4, dalle_3

class TestModels(unittest.TestCase):

    def setUp(self):
        self.generative_ai = generative_ai.GenerativeAI()
        self.text_bison = text_bison.TextBison()
        self.gpt4 = gpt4.GPT4()
        self.dalle_3 = dalle_3.DALLE3()

    def test_generative_ai(self):
        input_text = "Hello, world!"
        output_text = self.generative_ai.generate_text(input_text)
        self.assertIsInstance(output_text, str)

    def test_text_bison(self):
        input_text = "Hello, world! This is a test of the TextBison model."
        output_text = self.text_bison.summarize(input_text)
        self.assertIsInstance(output_text, str)

    def test_gpt4(self):
        input_text = "Hello, world!"
        output_text = self.gpt4.generate_text(input_text)
        self.assertIsInstance(output_text, str)

    def test_dalle_3(self):
        input_text = "A beautiful sunset over the ocean."
        output_image = self.dalle_3.generate_image(input_text)
        self.assertIsInstance(output_image, Image.Image)

if __name__ == '__main__':
    unittest.main()