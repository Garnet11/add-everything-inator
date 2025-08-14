![the add everything inator!](https://github.com/user-attachments/assets/6d8ab2b0-6092-41cd-a82c-14f5697f91e7)

Welcome to the Add Everything-inator Github page! This tool can mass-add projects to studios via searching them and then adding the project.
# How to use
Enter your scratch credentials:

<img width="1090" height="84" alt="image" src="https://github.com/user-attachments/assets/68cd847f-176f-4411-b37a-c1632794f4ac" />

Fill out the studio keyword, amount of studios, and project id:

<img width="1087" height="55" alt="image" src="https://github.com/user-attachments/assets/3ea48bf1-3db1-4f1c-a970-654e67017844" />

Type "y" or "n" for forbidden words file:

<img width="1061" height="13" alt="image" src="https://github.com/user-attachments/assets/84ef2b67-692a-49c7-a392-76a333d05c41" />

<h2>The Forbidden Words File</h2>
Forbidden words can help avoid studios that may appear in search results but are not actually related. Each time the script is going to add a project to a studio, it checks the title of the studio for any of the words.

If you type "y" you will be prompted to put a full path to the file..
<img width="1103" height="34" alt="image" src="https://github.com/user-attachments/assets/1b0fef05-28b4-437f-9997-89a035b79470" />
Forbidden words are usually a simple list inside a text file. Example:

```txt
fan club
fanclub
undertale
deltarune
namco
mario
sonic
zelda
lucario
stop
nyan
cat
dragon
pokemon
related
```

(This list can be useful if you're doing Add Everything studios.)
<h2>What the script does after everything has been filled out</h2>
The script will check if any of the studios that have been searched the project has already been added to, and it will attempt add the project to each studio in the search results (except for ones with forbidden words in the title of course)
