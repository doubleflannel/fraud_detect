# Image-Based Claim Analysis System

## Overview
This suite of scripts is designed for analyzing image-based claims, potentially for fraud detection in a company. It assesses various attributes of images, checks for modifications, and verifies their originality by utilizing a combination of image recognition, metadata analysis, and reverse image searching.

## Components

### 1. Image Recognition (`ImageRec-2.py`)
Utilizes AI models (specifically OpenAI's Vision Transformer) to identify specific features in images, such as the presence of a phone, crack damage, and the type of phone (iPhone or Android).

### 2. Image Alteration Analysis (`ImageAlter-2.py`)
Analyzes image metadata to detect any alterations. It examines the creation and modification dates, as well as AI-generated tags in the image's metadata.

### 3. Reverse Image Search (`ImageSearch-2.py`)
Performs online searches using the TinEye API to find similar images and assess the originality of the processed image.

### 4. Script Orchestrator (`RunPythonScriptRecursivelyOnAllFilesInCurrentWorkingDirectory.ps1`)
Automates the execution of the above Python scripts for batch processing of images. It compiles the results of individual scripts into a comprehensive CSV file.

## Workflow

1. **Batch Processing**: The PowerShell script searches for all image files in the current directory and subdirectories for processing.
2. **Image Recognition**: Determines various attributes like crack damage, phone type, etc.
3. **Image Alteration Analysis**: Assesses if the image has been altered based on metadata.
4. **Reverse Image Search**: Checks for the originality of the image by searching for similar images online.
5. **Result Compilation**: Aggregates the results from each script and exports them to a CSV file for review.

## Usage

- The system is designed to be executed in a directory containing image files. 
- It automatically processes all images in the directory and its subdirectories.

## System Requirements

- Python installation with required libraries (`pytorch`, `transformers`, `pytineye`, `exiftool`, etc.).
- PowerShell for running the orchestrator script.

## Potential Improvements

- The system assumes consistent output formats from each Python script. Any format changes may require adjustments in the PowerShell script.
- Error handling and exception management could be improved for robustness.

## Conclusion

Ideal for insurance companies or other entities dealing with numerous image-based claims, this system helps automate the assessment process and flag potential fraud cases.
