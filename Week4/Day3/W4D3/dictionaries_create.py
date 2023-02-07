a_dict: dict = {}

print(type(a_dict))

# The key has to be NOT MUTABLE -> str, int
# b_dict = {[1,2,3]: "value"}

# print(b_dict)


c_dict = {1: "A", 2: "B"}

print(c_dict[1])

d_dict = {1: [1,2,3], 2: "Hello"}

info = {
    "Yossi": {"first_name": "yossi", "last_name": "eik", "age": 31},
    "David": {"first_name": "david", "last_name": "roz", "age": 28}
}

print(info["David"]["age"])



# keys and values
personal_info1 = {"name": "Yossi", "City": "TLV"}
personal_info2 = {"name": "Shon", "City": "AFULA"}
personal_info3 = {"name": "David", "City": "JERUSALEM"}
personal_info4 = {"name": "Lea", "City": "KS"}
personal_info5 = {"name": "Noa", "City": "Netanya"}
personal_info6 = {"name": "Noa"}


# print(personal_info2["City"] == "JERUSALEM")


# keys
print(personal_info1.keys())
search_for = "City"
print(search_for in personal_info6.keys())
city_value = personal_info5.get("City", None)

print(city_value)

# values

dict_values = personal_info3.values()
print(dict_values)


# looping through keys
for key in personal_info1:
    print("KEY:", key)

# looping throug values
for value in personal_info1.values():
    print("VALUE:", value)

# looping through keys + values
for key, value in personal_info1.items():
    print(f"{key}: {value}")


# UPDATING
personal_info6 = {"name": "Noa"}
 
# Add a new key and value
personal_info6["City"] = "New York"

print(personal_info6)

personal_info6["NAME"] = personal_info6["name"]

del personal_info6["name"]

print(personal_info6)

personal_info6["NAME"] = "Lea"

print(personal_info6)

