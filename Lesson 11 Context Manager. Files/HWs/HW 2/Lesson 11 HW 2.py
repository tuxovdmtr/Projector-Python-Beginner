# Create a file with some content. As example, you can take this one:
# “Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum”.
# Create a second file and copy the content of the first file to the second file in upper case.

with open("Lesson 11 Context Manager. Files\HWs\HW 2\content.txt", "r") as input_content, open("result.txt", "w") as output_content:
    input_text = input_content.read()
    output_content.write(input_text.upper())