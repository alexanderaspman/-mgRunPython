import sys
from script import main

if __name__ == "__main__":
    if len(sys.argv) > 1:
        # Run the Python script on command-line arguments
        main()
    else:
        print("Usage: python main.py <script_args>")