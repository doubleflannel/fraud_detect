## Image Alter Examiner for Chubb (2/3)
# Use Exiftool.exe
# By Cornell Engineering Management Group
# Ivanakbar Purwamaska; Connor O'Brien; Jonathan Nikolaidis; Christine Lambert; Hannah Culhane"""

## To run, type cd C:\Users\ivanpc\code\ChubbImage
# To run, type this in the PowerShell Terminal (below): python ImageAlter-1.py
# To test this on other images, change the file path

## Setup
#region
# install datetime
# install pyexiftool

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
from exiftool import ExifToolHelper
from datetime import datetime

def format_date1(date_str):
    dt = datetime.strptime(date_str, '%Y:%m:%d %H:%M:%S%z')
    date_formatted = dt.strftime('%B %d, %Y')
    time_formatted = dt.strftime('%I:%M%p')    
    tz_offset = date_str[-6:]
    return f"{date_formatted}; {time_formatted}"

def format_date2(date_str):
    dt = datetime.strptime(date_str, '%Y:%m:%d %H:%M:%S')
    date_formatted = dt.strftime('%B %d, %Y')
    time_formatted = dt.strftime('%I:%M%p')    
    return f"{date_formatted}; {time_formatted}"

def string_to_timestamp(date_str):
    try:
        dt = datetime.strptime(date_str, '%B %d, %Y; %I:%M%p')
        timestamp = int(dt.timestamp())
        return timestamp
    except ValueError:
        return None

def extract_metadata(file_path, keys_of_interest):
    metadata = {}
    with ExifToolHelper() as et:
        for d in et.get_metadata(file_path):
            for k, v in d.items():
                if k in keys_of_interest:
                    metadata[k] = v
    return metadata

def main(file_path):
    keys = ["File:FileName", "File:Directory", "EXIF:DateTimeOriginal", "File:FileModifyDate", "XMP:Credit", "IPTC:Credit"]
    metadata = extract_metadata(file_path, keys)
    
    is_time_modified = False
    is_ai_generated_xmp = "AI-Generated" in metadata.get('XMP:Credit', "")
    is_ai_generated_iptc = "AI-Generated" in metadata.get('IPTC:Credit', "")
    
    if 'EXIF:DateTimeOriginal' in metadata and 'File:FileModifyDate' in metadata:
        created_timestamp = string_to_timestamp(format_date2(metadata['EXIF:DateTimeOriginal']))
        modified_timestamp = string_to_timestamp(format_date1(metadata['File:FileModifyDate']))
        if created_timestamp and modified_timestamp:
            difference_in_seconds = modified_timestamp - created_timestamp
            if difference_in_seconds > 3*60:
                is_time_modified = True
    
    print(">IMAGE ALTERATION ANALYSIS RESULT:")    
#    print(f"Image Analyzed:", file_path)
    if is_time_modified or is_ai_generated_xmp or is_ai_generated_iptc:
        print("The image HAS been modified, based on metadata")
    else:
        print("The image HAS NOT been modified, based on metadata")
    if 'XMP:Credit' in metadata:
        print(f"XMP Credit: {metadata['XMP:Credit']}")
    if 'IPTC:Credit' in metadata:
        print(f"IPTC Credit: {metadata['IPTC:Credit']}")
    if 'EXIF:DateTimeOriginal' in metadata:
        print(f"{format_date2(metadata['EXIF:DateTimeOriginal'])} (Date Created)")
    if 'File:FileModifyDate' in metadata:
        print(f"{format_date1(metadata['File:FileModifyDate'])} (Date Written/Re-Written)")
    print("")

main(file_path)
#endregion