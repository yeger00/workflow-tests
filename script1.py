import os
print("helllllllllo")
print(os.environ)
print("this is a message from the PR")
print(os.environ)

for i in os.environ.get("SECRET_KEY"):
  print(i)
