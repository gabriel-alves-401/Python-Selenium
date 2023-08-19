"""
* Selenium Mask purpose is modify the document of chromedriver to change the cdc parameter
* Sites read the cdc parameter to figure that you're a robot
@author Gabriel Alves
"""

import io
import os
import random
import re
import string

path = os.path.abspath("C:/dev/libraries/chromedriver.exe")
replacement = "aja_" + ''.join(random.choice(string.ascii_lowercase) for _ in range(22))
replacement = replacement.encode()


def alterate(path_file, replacement_str):
    with io.open(path_file, "r+b") as fh:
        for line in iter(lambda: fh.readline(), b""):
            if b"cdc_" in line:
                fh.seek(-len(line), 1)
                newline = re.sub(b"cdc_.{22}", replacement_str, line)
                fh.write(newline)
                print(f"\033[93m[*]\033[0m Linha encontrada e alterada com sucesso: {line}")


if __name__ == '__main__':
    while alterate(path, replacement):
        pass
