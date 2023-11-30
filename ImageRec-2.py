## Image Recognition for Chubb (1/3)
# Use OpenAI Vision Transformer LLM
# By Cornell Engineering Management Group
# Ivanakbar Purwamaska; Connor O'Brien; Jonathan Nikolaidis; Christine Lambert; Hannah Culhane

## To run, type cd C:\Users\ivanpc\code\ChubbImage
# Then, type this in the PowerShell Terminal (below): python ImageRec-1.py
# To test this on other images, change the file path

## Setup
#region
# install pytorch
# install transformers

## Add PATH
import sys
sys.path.append('C:\\Users\\ivanpc\\AppData\\Local\\Packages\\PythonSoftwareFoundation.Python.3.11_qbz5n2kfra8p0\\LocalCache\\local-packages\\Python311\\site-packages')
sys.path.append('C:\\Users\\ivanpc\\AppData\\Local\\Packages\\PythonSoftwareFoundation.Python.3.11_qbz5n2kfra8p0\\LocalCache\\local-packages\\Python311\\Scripts')
sys.path.append('C:\\Users\\ivanpc\\source\\repos')
#endregion

## Supress Error
#region
import os
import sys
stderr = sys.stderr
sys.stderr = open(os.devnull, 'w')
#endregion

## Cat Image
#region
"""
from PIL import Image
import requests

from transformers import CLIPProcessor, CLIPModel

model = CLIPModel.from_pretrained("openai/clip-vit-large-patch14")
processor = CLIPProcessor.from_pretrained("openai/clip-vit-large-patch14")

url = "http://images.cocodataset.org/val2017/000000039769.jpg"
image = Image.open(requests.get(url, stream=True).raw)

categories = ["a photo of a cat", "a photo of a dog"]

inputs = processor(text=categories, images=image, return_tensors="pt", padding=True)

outputs = model(**inputs)
logits_per_image = outputs.logits_per_image # this is the image-text similarity score
probs = logits_per_image.softmax(dim=1) # we can take the softmax to get the label probabilities

probabilities = (probs[0] * 100).tolist()

#Print Output
print("")
for i, (category, probability) in enumerate(zip(categories, probabilities)):
    print(f"category {i + 1} ({category}): probability ({probability:.2f}%)")
print("")
"""

#endregion

## Dynamic File Path
#region
if len(sys.argv) < 2:
    sys.exit(1)

file_path = sys.argv[1]  # Use the provided argument for the file path
#endregion

## Phone Image
#region

from PIL import Image
import requests

from transformers import CLIPProcessor, CLIPModel

model = CLIPModel.from_pretrained("openai/clip-vit-large-patch14")
processor = CLIPProcessor.from_pretrained("openai/clip-vit-large-patch14")

image = Image.open(file_path)

phone_categories = ["contain a phone", "not contain a phone"]
crack_categories = ["a phone with a crack damage", "a phone with NO crack damage"]
type_categories = ["an iPhone", "an Android phone"]

#Process and predict phone or not phone
inputs_phone = processor(text=phone_categories, images=image, return_tensors="pt", padding=True)
outputs_phone = model(**inputs_phone)
probs_phone = outputs_phone.logits_per_image.softmax(dim=1)
probabilities_phone = (probs_phone[0] * 100).tolist()

#Process and predict crack damage
inputs_crack = processor(text=crack_categories, images=image, return_tensors="pt", padding=True)
outputs_crack = model(**inputs_crack)
probs_crack = outputs_crack.logits_per_image.softmax(dim=1)
probabilities_crack = (probs_crack[0] * 100).tolist()

#Process and predict phone type
inputs_type = processor(text=type_categories, images=image, return_tensors="pt", padding=True)
outputs_type = model(**inputs_type)
probs_type = outputs_type.logits_per_image.softmax(dim=1)
probabilities_type = (probs_type[0] * 100).tolist()

#Print Output
print("---")
print("Image Analyzed:", file_path)
print("")
print(">IMAGE RECOGNITION ANALYSIS:")    
for i, (category, probability) in enumerate(zip(phone_categories, probabilities_crack)):
    print(f"Does the image {category}? Probability {probability:.2f}%")
for i, (category, probability) in enumerate(zip(crack_categories, probabilities_crack)):
    print(f"Is the image {category}? Probability {probability:.2f}%")
for i, (category, probability) in enumerate(zip(type_categories, probabilities_type)):
    print(f"Is the image {category}? Probability {probability:.2f}%")
print("")
#endregion