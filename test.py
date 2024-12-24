import sys
# Functions in sys Module
# sys.argv
# sys.argv is a list in Python that contains command-line arguments passed to a script.
# sys.argv[0]: The name of the script file.
# sys.argv[1], sys.argv[2], etc.: These are the additional arguments provided when running the script.

print("Hello, my name is", sys.argv[1])
#so to avoid indexerror we can use the try and except method or a conditional statement
