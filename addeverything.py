import scratchattach as sa
import re
from time import sleep
import warnings
warnings.filterwarnings('ignore', category=sa.LoginDataWarning)
print("Welcome to the Add Everything-inator! Bugs, suggestions or reviews can be posted on the Github: https://github.com/Garnet11/add-everything-inator or on my Scratch account: https://scratch.mit.edu/users/GarnetonScratch/")
while True:
    username = input("Scratch username: ")
    password = input("Scratch password: ")
    try:
        session = sa.login(username, password)
        break
    except:
        print("Error! Login failed. Please check your username or password!")
searching = input("Studio keyword: ")
amount = int(input("Amount of studios: "))
projectid = input("Project ID: ")
forbiddenwords = []
while True:
    yesorno = input("Would you like to use a forbidden words file? (This is useful for avoiding studios unrelated to your project) (y/n): ")
    if yesorno == "y":
        while True:
            filepath = input("Full path to forbidden words file: ")
            try:
                with open(filepath, "r") as forbiddenwords:
                    forbiddenwords = forbiddenwords.read().splitlines()
                print("Successfully added forbidden words.")
                break
            except:
                print("Error! Could not find file.")                    
        break
    elif yesorno == "n":
        pass
        break
    else:
        pass
adds = 0
fails = 0
try:
    project = session.connect_project(projectid)
except:
    print("Error! We could not get your project. Please check the ID!")
    input()
    exit()
print("Getting studios...", end="")
studios = session.search_studios(query=searching, mode="popular", language="en", limit=amount)
pstudios = project.studios(limit=300)
print("Done!")
count = 0
for i in studios:
    for e in pstudios:
        if e.id == i.id:
            del studios[count]
            print(f"Omitted studio {i.id} in studios to be added because it already exists inside the projects added studios.")
    count += 1
print("Adding projects...")
for i in studios:
    try:
        hasword = False
        for e in forbiddenwords:
            if re.search(e, i.title, re.IGNORECASE) != None:
                hasword = True
        if hasword == False:
            i = session.connect_studio(str(i.id))
            i.add_project(projectid)
            adds += 1
            print(f"Added project to studio '{i.title}' ({i.id}) ({adds}/{len(studios)} added)")
        else:
            fails += 1
            print(f"Could not add project to studio '{i.title}' ({i.id}) because it had forbidden words. ({adds}/{len(studios)} added)")
    except:
        fails += 1
        print(f"Failed to add project to studio '{i.title}' ({i.id}) ({adds}/{len(studios)} added)")
    sleep(0.1)
print(f"Operation complete! Successfully added the project '{project.title}' to {adds} studios, failed to add to {fails} studios.")
input()

