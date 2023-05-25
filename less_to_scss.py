# Script to convert less variables to scss variables. 
# Modify the LESS_FILE variable with input file and OUTPUT_FILE with the desired output. 

# Find a fix so that only _ is replaced when not part of a variable. Could cause issues. 

# Define the LESS file you want to convert
LESS_FILE = "main.less"

SCSS_FILE = "output.scss"

# Read the LESS file
with open(LESS_FILE, "r") as less_file:
    less_content = less_file.read()

# Convert LESS variables to SCSS variables and replace underscores with hyphens
scss_content = less_content.replace("@", "$").replace("_", "-")


# Write the converted content to the output SCSS file
with open(SCSS_FILE, "w") as scss_file:
    scss_file.write(scss_content)

INPUT_FILE = "output.scss"

# Define the output SCSS file
OUTPUT_FILE = "_main.scss"

# Read the input file
with open(INPUT_FILE, "r") as input_file:
    input_content = input_file.read()

# Convert breakpoints (modify if needed)

output_content = input_content.replace("$media $phone-wide-max", "@include bp_max(mlarge)").replace("$media $phone-max", "@include bp_max(medium)").replace("$media $tablet-max", "@include bp_max(medium)").replace("$media $nine-sixty-max", "@include bp_max(large)").replace("$media $ten-twenty-four-max", "@include bp_max(xlarge)").replace("$media $desktop-max", "@include bp_max(xxlarge)").replace("$media $sixteen-max", "@include bp_max(xxxlarge)").replace("$media $phone-wide", "@include bp(mlarge)").replace("$media $phone", "@include bp(medium)").replace("$media $tablet", "@include bp(medium)").replace("$media $nine-sixty", "@include bp(large)").replace("$media $ten-twenty-four", "@include bp(xlarge)").replace("$media $desktop", "@include bp(xxlarge)").replace("$media $sixteen", "@include bp(xxxlarge)")
   
# Write the converted content to the output SCSS file
with open(OUTPUT_FILE, "w") as output_file:
    output_file.write(output_content)                  
