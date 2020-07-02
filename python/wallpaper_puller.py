import os
from shutil import copy

folder_path = "C:\\Users\\Admin\\AppData\\Local\\Packages\\Microsoft.Windows.ContentDeliveryManager_cw5n1h2txyewy\\LocalState\\Assets"
target_path = "./"
size_threshold = 200000 
# Copy anything over 200 Kb

print("Starting Program...")

files_list = os.listdir(folder_path)
print("Fetching files from folder path")

if len(files_list) == 0:
    raise Exception("Nothing inside the folder path")

pairs = []
for name in files_list:
    location = os.path.join(folder_path, name)
    pairs.append((os.path.getsize(location), name))

pairs.sort(key=lambda s: s[0], reverse=True)

# Copy the file and append ".jpg" to the end
for pair in pairs:
    if pair[0] > size_threshold:
        print("Copying", pair[1])
        destination = os.path.join(target_path, pair[1] + ".jpg")
        source = os.path.join(folder_path, pair[1])
        copy(source, destination)
    else:
        break

print("Done.")