import os
print("helllllllllo4")
print(os.environ)

for i in os.environ.get("SECRET_KEY"):
  print(i)
