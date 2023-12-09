import sys
import argparse

# def handle_pipe_input():
#     if not sys.stdin.isatty():
#         piped_input = sys.stdin.read()
#         return piped_input
#     else:
#         return None
def handle_pipe_input(input_stream):
    if not input_stream.isatty():
        piped_input = input_stream.read()
        return piped_input
    else:
        return None
def handle_string_input(input_string):
    if input_string:
        return input_string
    else:
        return None

def handle_file_input(input_file):
    if input_file:
        with open(input_file, 'r') as file:
            file_input = file.read()
        return file_input
    else:
        return None

def handle_input(args):
    parser = argparse.ArgumentParser()
    parser.add_argument('--input', help='Input for the AI model')
    parser.add_argument('--file', help='Input file for the AI model')
    args = parser.parse_args()

    if args.input:
        return handle_string_input(args.input)
    elif args.file:
        return handle_file_input(args.file)
    else:
        return handle_pipe_input()