wallet = "$300"

items_purchase = {
  "Water": "$1",
  "Bread": "$3",
  "TV": "$1,000",
  "Fertilizer": "$20"
}

# ➞ ["Bread", "Fertilizer", "Water"]

for key in items_purchase:

    item: str = items_purchase[key]

    item_list: list = list(item)

    del item_list[0] # remove $ sign

    item: str = "".join(item_list) # connect all the numbers together
    
    item: str = item.replace(',', '') # replace ',' (comma) with empty space

    item: int = int(item) # convert into a number

    items_purchase[key] = item

print(items_purchase)




