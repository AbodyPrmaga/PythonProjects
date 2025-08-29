import re

url = "https://manapps.eg/articale/Abdelrahman/Q7ff6f6f1b3g52p3O6m5"

search = re.search(r"(https?)://([a-z]{0,20})\.([a-z]{0,10})/([a-zA-z]{0,15})/([A-z]{0,15})/(\w+)",url)


print("Protocol :",f"{search.group(0)}")
print("Domain Name :",f"{search.group(1)}")
print("Sub Domain Name :",f"{search.group(2)}")
print("Section Name :",f"{search.group(3)}")
print("Writer :",f"{search.group(4)}")
print("Id articale :",f"{search.group(5)}")