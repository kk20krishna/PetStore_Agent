from tools import add_pet

Add some test pets to the Pet Store
for i in range(4):
  name = "test_dog_" + str(i + 1)
  tags = [{"id": 0, "name": "aggressive"}]
  res = add_pet.invoke({"name": name, "tags": tags})
  print(res)

# Add some test pets to the Pet Store
# for i in range(2):
#   name = "test_cat_" + str(i + 1)
#   tags = [{"id": 0, "name": "sick"}]
#   res = add_pet.invoke({"name": name, "tags": tags})
#   print(res)
