## Image Reverse Searcher for Chubb (3/3)
# Use Tineye API
# By Cornell Engineering Management Group
# Ivanakbar Purwamaska; Connor O'Brien; Jonathan Nikolaidis; Christine Lambert; Hannah Culhane"""

## To run, type cd C:\Users\ivanpc\code\ChubbImage
# Then, type this in the PowerShell Terminal (below): python ImageSearch-1.py
# To test this on other images, change the file path

## Setup
#region
# install tineye

## Add PATH
import sys
sys.path.append('C:\\Users\\ivanpc\\AppData\\Local\\Packages\\PythonSoftwareFoundation.Python.3.11_qbz5n2kfra8p0\\LocalCache\\local-packages\\Python311\\site-packages')
sys.path.append('C:\\Users\\ivanpc\\AppData\\Local\\Packages\\PythonSoftwareFoundation.Python.3.11_qbz5n2kfra8p0\\LocalCache\\local-packages\\Python311\\Scripts')
sys.path.append('C:\\Users\\ivanpc\\source\\repos')
#endregion

## Dynamic File Path
#region
if len(sys.argv) < 2:
    sys.exit(1)

file_path = sys.argv[1]  # Use the provided argument for the file path
#endregion

## Phone Image
#region
from pytineye import TinEyeAPIRequest

api_key = ' dn_k5RyGYD-GL6dXiV61_mOzv^_rg8^65JUKgKvt'
api = TinEyeAPIRequest(
    'https://api.tineye.com/rest/',
    api_key
)

with open(file_path, 'rb') as fp:
    data = fp.read()
    response = api.search_data(
        data=data,
        limit=2
    )

#Print Output
import webbrowser
import pygetwindow as gw
import pyautogui

# webbrowser.open(f"file://{file_path}", new=2)  # Open local image in default viewer/browser

#print(f"Image Analyzed:", file_path)
print(">ONLINE REVERSE SEARCH ANALYSIS:")
if response.matches:
    print("The image is NOT original, matching images found online")
    for index, match in enumerate(response.matches, start=1):
        print(f"Mathing image {index}, similarity {round(match.score, 2)}%")
        print(f"Link: {match.image_url}")
#        webbrowser.open(match.image_url, new=2)  # Open each URL in a new window/tab
#        pyautogui.sleep(1)
#        window_title = gw.getActiveWindow().title
#        browser_window = gw.getWindowsWithTitle(window_title)[0]
#        browser_window.resizeTo(500, 500)  # Width, Height
#        browser_window.moveTo(100, 100)  # X, Y
else:
    print("The image is original, no matching images found online")
print("---")
print("")
#endregion