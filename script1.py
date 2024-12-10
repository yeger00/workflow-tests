import os
print("helllllllllo")
print(os.environ)

for i in os.environ.get("SECRET_KEY"):
  print(i)
