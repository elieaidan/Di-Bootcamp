sample_dict = {
  "name": "Kelly",
  "age":25,
  "salary": 8000,
  "city": "New york"

}
keys_to_remove = ["name", "salary"]

for keys in keys_to_remove:
    del sample_dict[keys]


print(sample_dict)