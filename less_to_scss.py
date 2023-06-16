# Script to change a less css file to SCSS
# Last modified: 16 Jun 2023
# Author: Ben Bagley

import re

# Define the LESS file you want to convert
LESS_FILE = "input/pages.less"
SCSS_FILE = "output.scss"

# Read the LESS file
with open(LESS_FILE, "r") as less_file:
    less_content = less_file.read()

# Convert LESS variables to SCSS variables and replace underscores with hyphens
lines = less_content.split("\n")
scss_lines = []
for line in lines: 
    if '__' in line or re.search(r'keyframes|charset', line): # include any keywords or chars that need to be ignored 
        scss_lines.append(line)
    else:
        line = line.replace("@", "$").replace("_", "-")
        scss_lines.append(line)
scss_content = "\n".join(scss_lines)

# Write the converted content to the output SCSS file
with open(SCSS_FILE, "w") as scss_file:
    scss_file.write(scss_content)

INPUT_FILE = "output.scss"

# Define the output SCSS file
OUTPUT_FILE = "output/_pages.scss"

# Read the input file
with open(INPUT_FILE, "r") as input_file:
    input_content = input_file.read()

# Convert breakpoints (modify if needed)
output_content = input_content.replace("$media $phone-wide-max", "@include bp_max(mlarge)")\
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

# Write the converted content to the output SCSS file
with open(OUTPUT_FILE, "w") as output_file:
    output_file.write(output_content)
