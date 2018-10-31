"""Main executable for cmm(c-minus-minus) compiler."""

import argparse
import pathlib
import platform
import subprocess
import sys
from pprint import pprint

import cmm_compiler.lexer as lexer

from cmm_compiler.errors import error_collector, CompilerError
from cmm_compiler.parser.parser import parse


def main():
    """Run the main compiler script."""
    arguments = get_arguments()

    objs = []
    for file in arguments.files:
        print("Result of file: " + file.split('/')[-1])
        objs.append(process_file(file, arguments))

    error_collector.show()


def process_file(file, args):
    """Process single file into object file and return the object file name."""
    if file[-2:] == ".c":
        return process_cmm_file(file, args)
    else:
        err = f"unknown file type: '{file}', only .c file as C-like cmm(c-minus-minus) files are supported."
        error_collector.add(CompilerError(err))
        return None


def process_cmm_file(file, args):
    """Does Lexical analyses and parse from a C-like cmm(c-minus-minus) file."""
    code = read_file(file)
    if not error_collector.ok():
        return None

    token_list = lexer.tokenize(code, file)
    if not error_collector.ok():
        return None
    
    pprint([{i: o} for i, o in enumerate(token_list)])

    # If parse() can salvage the input into a parse tree, it may emit an
    # ast_root even when there are errors saved to the error_collector. In this
    # case, we still want to continue the compiler stages.
    ast_root = parse(token_list)
    if not ast_root:
        return None


def get_arguments():
    """Get the command-line arguments.

    This function sets up the argument parser. Returns a tuple containing
    a list of the file names provided on command line.
    """
    desc = """Lexical analyses and parser for C-like cmm(c-minus-minus) files."""
    parser = argparse.ArgumentParser(
        description=desc, usage="main.py [-h] files...")

    # Files to compile
    parser.add_argument("files", metavar="files", nargs="+")

    return parser.parse_args()


def read_file(file):
    """Return the contents of the given file."""
    try:
        with open(file) as c_file:
            return c_file.read()
    except IOError as e:
        description = f"could not read file: '{file}'"
        error_collector.add(CompilerError(description))


if __name__ == "__main__":
    sys.exit(main())
