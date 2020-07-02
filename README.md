# Windows-Rotating-Wallpaper-Puller
Pulls the rotating wallpapers on your login screen (which change periodically) as .jpg files to a destination folder of your choice. I wrote this program because I wanted to keep these wallpapers for personal use, such as for my desktop wallpaper (or whatever other purpose), and I was tired of manually pulling and renaming them.

### Usage
Currently, the program is written in Python (v3.82) for Windows 10, so a pre-requisite would be to install that version of Python, or a higher one. The program itself is a little bit crude - more user interactivity would be a future step (such as specifying target and asset folder paths as command line arguments).

#### Python Version
The current method to change target and asset folder paths is by manually changing the variables in the program (```target_path``` and ```folder_path``` respectively). Ensure ```folder_path``` points to the user's assets folder. This can be found at ```C: > Users > [your username] > AppData > Local > Packages > Microsoft.Windows.ContentDeliveryManager_cw5n1h2txyewy > LocalState > Assets```, replacing ```[your username]``` with the current user's login name.


```target_path``` can point to anywhere, as long as it is a folder. This indicates where the program should copy the wallpaper files to.

### Things to improve on
1. For now, this is written in Python. I'd like to get a batch script version of this working, so that Windows users don't have to install anything

2. As mentioned above, user convenience and interactivity is admittedly lacking. Ways to improve on this are making command line arguments the way to specify destination and asset folders, along with automatically finding the assets folder for the user. Default values for these variables would also help (such as a pre-made 'targets' folder)

3. Error checking is spotty - things such as copying over files which already exist aren't handled, along with checking if folder_path points to the real assets folder (which could be bad since it would copy over files completely unrelated).
