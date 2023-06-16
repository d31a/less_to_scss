# Script to change a less css file to SCSS
# To convert a folder of files create folders called 'input' and 'output' in the root directory 
# Last modified: 16 Jun 2023
# Author: Ben Bagley

import os
import re

# Define the input folder containing the LESS files
LESS_FOLDER = "input"

# Define the output folder for the SCSS files
OUTPUT_FOLDER = "output"

# Iterate over the files in the input folder
for filename in os.listdir(LESS_FOLDER):
    if filename.endswith(".less"):
        # Form the input and output file paths
        less_file = os.path.join(LESS_FOLDER, filename)
        scss_file = os.path.join(OUTPUT_FOLDER, "_" + re.sub(r"\.less$", ".scss", filename))

        # Read the LESS file
        with open(less_file, "r") as file:
            less_content = file.read()

        # Convert LESS variables to SCSS variables and replace underscores with hyphens
        # Add any elements to be replaced after line.replace("foo", "bar")
        lines = less_content.split("\n")
        scss_lines = []
        for line in lines:
            if '__' in line or re.search(r'keyframes|charset', line):
                scss_lines.append(line)
            else: 
              line = line.replace("@", "$")\
                    .replace("_", "-")\
                    .replace(".&", "&")\
                    .replace(".rotate", "@include rotate")\
                    .replace(".flex", "@include flex")\
                    .replace(".transition", "@include transition")
              scss_lines.append(line)
        scss_content = "\n".join(scss_lines)

        # Apply breakpoints conversion
        scss_content = scss_content.replace("$media $phone-wide-max", "@include bp_max(mlarge)")\
            .replace("$media $phone-max", "@include bp_max(smedium)")\
            .replace("$media $tablet-max", "@include bp_max(medium)")\
            .replace("$media $nine-sixty-max", "@include bp_max(large)")\
            .replace("$media $ten-twenty-four-max", "@include bp_max(xlarge)")\
            .replace("$media $desktop-max", "@include bp_max(xxlarge)")\
            .replace("$media $twelve-eighty-max", "@include bp_max(xxxlarge)")\
            .replace("$media $phone-wide", "@include bp(mlarge)")\
            .replace("$media $phone", "@include bp(smedium)")\
            .replace("$media $tablet", "@include bp(medium)")\
            .replace("$media $nine-sixty", "@include bp(large)")\
            .replace("$media $ten-twenty-four", "@include bp(xlarge)")\
            .replace("$media $desktop", "@include bp(xxlarge)")\
            .replace("$media $twelve-eighty", "@include bp(xxxlarge)")

        # Write the converted content with breakpoints applied to the output SCSS file
        with open(scss_file, "w") as file:
            file.write(scss_content)