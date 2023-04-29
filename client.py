import os, sys, socket
if len(sys.argv) == 0 or len(sys.argv) == 1:
  print("Please specify the instance the host is using with the following command:\npython3 client.py <ip> <port>")
elif len(sys.argv) == 2:
  i = 0
  id = ""
  while not i == 10:
    i += 1
    id = id + string.ascii_uppercase[random.randint(0, len(string.ascii_uppercase) - 1)]
  os.system(f"nc {sys.argv[0]} {sys.argv[1]} -v -o pclink-{id}")
  os.system(f"ssh-copy-id -i pclink-{id} {os.getlogin()}@{socket.gethostname()}")
else:
  print("Too many arguments!")
