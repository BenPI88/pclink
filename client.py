import os, sys
if len(sys.argv) == 0 or len(sys.argv) == 1:
  print("Please specify the instance the host is using with the following command:\npython3 client.py <ip> <port>")
elif len(sys.argv) == 2:
  os.system(f"nc {sys.argv[0]} {sys.argv[1]} -v -o pclink")
else:
  print("Too many arguments!")
