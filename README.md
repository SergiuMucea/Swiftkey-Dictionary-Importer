# Swiftkey Dictionary Importer

The purpose of this project is to automate the integration of the Microsoft SwiftKey keyboard dictionary into a compatible file with Google Gboard dictionary.<br>
At the moment, there is no compatibility between the two platforms and Gboard will give errors if other methods such as a copy-paste from a notepad or an excel file is tried.<br>

## Main functionalities and steps to use

1. Download the Microsoft SwiftKey dictionary and extract the **sync_words.json** file from the .zip file.
2. In the Gboard app on your phone, if there are no words in your existing dictionary, add a couple of words just to get it working and then export the dictionary to your computer.
3. Either/or:
    1. (Either) Copy and paste the code from main.py to your interpreter and run it.
    2. (Or) Download the .exe file containing the code and run it
4. You will get two pop-up screens for selecting the files to be processed:
    1. Select the Gboard dictionary first
    2. Select the Microsoft dictionary .json file second.
5. Take the .txt file and put it on your phone/drive and upload the dictionary in the Google Gboard

For example purposes, a Gboard and a Swiftkey dictionary file have been added in the docs folder.

### Important notice!

It is important to be aware of the fact that importing a large number of words in Gboard may actually disturb the typing experience rather than improve it.<br>
It could potentially lead to some issues, like cluttering suggestions or making it harder to find commonly used words.<br>
If you *do* decide to import all Microsoft SwiftKey words, then make sure to test if it is worth it.<br>
If it does not bring any value to your experience, then probably it is best to *delete learned words and data* from the Gboard settings and leave Google learn your typing habbits by itself :wink: