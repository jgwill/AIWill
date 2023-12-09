
import vertexai
from vertexai.language_models import TextGenerationModel
import os

project_id = os.getenv("GOOGLE_CLOUD_PROJECT")
location = os.getenv("GOOGLE_CLOUD_PROJECT_LOCATION")
credentials = os.getenv("GOOGLE_APPLICATION_CREDENTIALS")
textgeneration_model_name = os.getenv("GOOGLE_COULD_TEXTGENERATION_MODEL","text-bison@001")


class GenerativeAI:
    def __init__(self):
        self.goal = 'text-generation'

    def generate_text(self, input_text = "Give me ten interview questions for the role of software program manager.",
        temperature: float= 0.7,
        max_output_tokens: str= 256,
        top_p: float= 0.8,
        top_k: int=40
    ) -> str:
        """Ideation example with a Large Language Model"""
        
        model_name = "text-bison@001"
        

        vertexai.init(project=project_id, location=location)
        # TODO developer - override these parameters as needed:
        parameters = {
            "temperature": temperature,  # Temperature controls the degree of randomness in token selection.
            "max_output_tokens": max_output_tokens,  # Token limit determines the maximum amount of text output.
            "top_p": top_p,  # Tokens are selected from most probable to least until the sum of their probabilities equals the top_p value.
            "top_k": top_k,  # A top_k of 1 means the selected token is the most probable among all tokens.
        }

        model = TextGenerationModel.from_pretrained(model_name)
        response = model.predict(
            input_text,
            **parameters,
        )
        #print(f"{response.text}")

        return response.text

