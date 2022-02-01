
import pandas

data=pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")

gray_squirrel=data[data["Primary Fur Color"]=="Gray"]
red_squirrel=data[data["Primary Fur Color"]=="Cinnamon"]
black_squirrel=data[data["Primary Fur Color"]=="Black"]

print(len(gray_squirrel))
print(len(red_squirrel))
print(len(black_squirrel))

dict_count={
    "Fur Color":["Gray","Cinnamon","Black"],
    "Count":[len(gray_squirrel),len(red_squirrel),len(black_squirrel)]
    }

df=pandas.DataFrame(dict_count)
df.to_csv("Color_count.csv")
