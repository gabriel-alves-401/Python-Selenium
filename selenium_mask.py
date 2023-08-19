"""
* The purpose of Selenium Mask is to modify the chromedriver binary file to change the cdc parameter.
* Many websites use the cdc parameter to detect automated robot-like behavior.
* This script helps to obfuscate the cdc parameter to avoid such detection.
* This script follows the PEP-8 style guide for Python code.
* @author Gabriel Alves
"""

import io
import os
import random
import re
import string

# Specify the path to the chromedriver binary file
path = os.path.abspath("C:/dev/libraries/chromedriver.exe")

# Generate a random replacement string for the cdc parameter
replacement = "aja_" + ''.join(random.choice(string.ascii_lowercase) for _ in range(22))
replacement = replacement.encode()


def alterate(file_path: str, replacement_str: bytes) -> None:
    """
    Modify the chromedriver binary to replace occurrences of cdc parameter.
    
    :param file_path: Path to the chromedriver binary file.
    :param replacement_str: The replacement string for the cdc parameter.
    """
    with io.open(file_path, "r+b") as fh:
        for line in iter(lambda: fh.readline(), b""):
            if b"cdc_" in line:
                fh.seek(-len(line), 1)
                # Replace the cdc parameter with the generated replacement string
                newline = re.sub(b"cdc_.{22}", replacement_str, line)
                fh.write(newline)
                print(f"\033[93m[*]\033[0m Line found and successfully modified: {line}")


if __name__ == '__main__':
    # Continuously modify the chromedriver binary until no more occurrences are found
    while alterate(path, replacement):
        pass
