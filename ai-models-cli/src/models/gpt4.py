#from transformers import GPT2LMHeadModel, GPT2Tokenizer

class GPT4:
    def __init__(self):
        self.goal = "gpt4"
        #self.tokenizer = GPT2Tokenizer.from_pretrained("gpt2")
        #self.model = GPT2LMHeadModel.from_pretrained("gpt2")

    def generate_text(self, input_text):
        inputs = self.tokenizer.encode(input_text, return_tensors='pt')
        outputs = self.model.generate(inputs, max_length=500, num_return_sequences=1, no_repeat_ngram_size=2)
        generated_text = self.tokenizer.decode(outputs[0], skip_special_tokens=True)
        return generated_text