# AI Models CLI

This project provides a command line interface to use various types of AI models such as generative AI for text creation, TextBison or GPT-4 for text summarization, and DALL-E-3 for image generation. It supports input from pipe, string or input files.

![Alt text](image.png)

## Installation

To install the project, you need to have Python 3.6 or higher installed on your machine. Then, you can install the project and its dependencies using the following command:

```bash
pip install -r requirements.txt
```

## Usage

You can use the command line interface as follows:

```bash
python src/main.py --model generative_ai --input "Hello, world!"
```

This will use the generative AI model to create text based on the input "Hello, world!".

You can also use the `--input-file` option to specify an input file:

```bash
python src/main.py --model generative_ai --input-file input.txt
```

This will read the input from the file `input.txt`.

If you want to use input from a pipe, you can do so as follows:

```bash
echo "Hello, world!" | python src/main.py --model generative_ai
```

This will use the input from the pipe.

The available models are `generative_ai`, `text_bison`, `gpt4`, and `dalle_3`.

## Testing

You can run the unit tests using the following command:

```bash
python -m unittest tests/test_models.py
```

## Contributing

If you want to contribute to this project, please feel free to submit a pull request. If you find a bug or have a suggestion for improvement, please open an issue.

## License

This project is licensed under the MIT License. See the LICENSE file for details.