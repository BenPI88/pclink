import os, string, random
print("PCLink\nBy github/benpi88\nAn easy way to link two systems for ssh.")
i = 0
id = ""
while not i == 10:
  i += 1
  id = id + string.ascii_uppercase[random.randint(0, len(string.ascii_uppercase) - 1)]
os.system(f"ssh-keygen -f pclink-{id}")
print("Ready for client to connect!")
os.system(f"nc -l {random.randint(1000, 9999)} -e pclink-{id}.pub")
