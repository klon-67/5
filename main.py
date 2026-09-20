import os

for root, dirs, files in os.walk('.'):
    for directory in dirs:
        print(os.path.join(root, directory))
    for file in files:
        print(os.path.join(root, file))
