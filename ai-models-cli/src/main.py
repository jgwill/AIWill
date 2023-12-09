import argparse
import sys
from models import generative_ai, text_bison, gpt4, dalle_3
from utils import input_handler

def main():
    parser = argparse.ArgumentParser(description='AI Models CLI')
    parser.add_argument('--m', type=str, required=True, help='AI model to use. g:generative, s:summarize, d:dalle')
    parser.add_argument('--i', type=str, required=False, help='Input for the AI model')
    parser.add_argument('--t', type=str, default='string', choices=['string', 'f', 'p'], help='Type of the input')

    args = parser.parse_args()
    #print("args.i: ", args.i)
    #print("args.t: ", args.t)
    if args.t == 'string':
        input_data = input_handler.handle_string_input(args.i)
    elif args.t == 'f':
        input_data = input_handler.handle_file_input(args.i)
    elif args.t == 'p':
        input_data = input_handler.handle_pipe_input(sys.stdin)
    #print("input_data: ", input_data)
          
    if args.m == 'generative_ai' or args.m == 'generative-ai' or args.m == 'g':
        model = generative_ai.GenerativeAI()
        output = model.generate_text(input_data)
    elif args.m == 'text_bison' or args.m == 'text-bison' or args.m == 's' or args.m == 'summarize' or args.m == 'summary':
        model = text_bison.TextBison()
        output = model.summarize(input_data)
    elif args.m == 'gpt4':
        model = gpt4.GPT4()
        output = model.generate_text(input_data)
    elif args.m == 'dalle_3':
        model = dalle_3.DALLE3()
        output = model.generate_image(input_data)

    print(output)

if __name__ == '__main__':
    main()