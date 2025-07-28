### test_data.py

from tools import add_pet

# Add some test pets to the Pet Store tagged as aggressive dogs
for i in range(4):
  name = "test_dog_" + str(i + 1)
  tags = [{"id": 0, "name": "aggressive"}]
  res = add_pet.invoke({"name": name, "tags": tags})
  print(res)

# Add some test pets to the Pet Store tagged as sick cats
for i in range(2):
  name = "test_cat_" + str(i + 1)
  tags = [{"id": 0, "name": "sick"}]
  res = add_pet.invoke({"name": name, "tags": tags})
  print(res)

# Add one test pet to the Pet Store of type Tiger
name = "Tinto Tiger"
tags = [{"id": 0, "name": "tiger"}]
res = add_pet.invoke({"name": name, "tags": tags})
print(res)

# Add one test pet to the Pet Store of type macaw
name = "Scarlet Macaw"
tags = [{"id": 0, "name": "macaw"}]
res = add_pet.invoke({"name": name, "tags": tags})
print(res)
