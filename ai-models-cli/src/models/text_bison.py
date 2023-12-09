#from transformers import pipeline

import vertexai
from vertexai.language_models import TextGenerationModel
import os

project_id = os.getenv("GOOGLE_CLOUD_PROJECT")
location = os.getenv("GOOGLE_CLOUD_PROJECT_LOCATION")
credentials = os.getenv("GOOGLE_APPLICATION_CREDENTIALS")
textgeneration_model_name = os.getenv("GOOGLE_COULD_TEXTGENERATION_MODEL","text-bison@001")


class TextBison:
    def __init__(self):
        self.goal = "summarizer"# = pipeline('summarization')

    # def summarize(self, text):
    #     return self.summarizer(text)[0]['summary_text']
    
    def summarize(self,text_to_summarize,
                  temperature: float= 0.7,
                  max_output_tokens: str= 256,
                  top_p: float= 0.95,
                  top_k: int=40
                  ) -> str:
        """Summarization Example with a Large Language Model"""

        vertexai.init(project=project_id, location=location, credentials=credentials)
        # TODO developer - override these parameters as needed:
        parameters = {
            "temperature": temperature,  # Temperature controls the degree of randomness in token selection.
            "max_output_tokens": max_output_tokens,  # Token limit determines the maximum amount of text output.
            "top_p": top_p,  # Tokens are selected from most probable to least until the sum of their probabilities equals the top_p value.
            "top_k": top_k,  # A top_k of 1 means the selected token is the most probable among all tokens.
        }

        model = TextGenerationModel.from_pretrained(textgeneration_model_name)
        

        response = model.predict(
            text_to_summarize,
            **parameters,
        )
        #print(f"{response.text}")

        return response.text

