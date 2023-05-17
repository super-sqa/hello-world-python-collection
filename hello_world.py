print("Hello world from GitHub")

print("I am a basic script leaving in github that just prints gibrish")

print("I just added a new line in the file")


import os

current_build = os.environ.get('BUILD_NUMBER', "Unable to find the build number variable")

print(f"The build number is: {current_build}")