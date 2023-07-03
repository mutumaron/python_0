#list data stucture,it is ordered and changeble
cars=["Toyota","Mazda","Volkswagen","Nissan","Suzuki"]
cars[1]="Range"
cars.append("Subaru")
cars.insert(2, "Audi")
cars.pop()
cars.sort()
cars.reverse()
print(cars)

#this is a tuple,its unchangable

fruits=("Mango","Apple","Pineapple","Orange")
#fruits[1]="Banana"
#fruits.pop()
#fruits.count()

for i in fruits:
     print(i)


#sets data structures .unordered

country={"Kenya","Uganda","France","Rwanda","Mali","Malawi","Russia"}
print(country)


#dictionaries

matunda={
    "Amount":40,
    "Jina":"Ndizi",
    "Rangi":"Yellow"
}
matunda["Size"]="Large"
matunda.pop("Size")
print(matunda)

