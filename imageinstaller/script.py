import logging
from imgCreate import script 
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)
script: imgCreate() = imgCreate
def main():
    # Your script's logic here...
    print("Hello, world!")
    script()