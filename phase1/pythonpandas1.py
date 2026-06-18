import pandas as pd

data = [100,110,104,202,200]

series = pd.Series(data,index=["a","b","c","d","e"])

#location by label
print(series.loc["a"])
#location by index
print(series.iloc[0])

#filter by values
print(series[series>=200])


calories = {"Day 1":1750,"Day2":2100,"Day3":1700}
series2 = pd.Series(calories)
print(series2)


pokemon = ["Bulbasaur","pikkacu"]
series3 = pd.Series(pokemon)
print(series3)




#DATA FRAMES tabular datastructure 2 dimesnsional

data1 = {"Name":["spongeBob","Batman","Modi ji"],"Age":[30,35,50]}

df = pd.DataFrame(data1,index=["Employee 1","Employee 2","Employee 3"])
print(df)
print(df.loc["Employee 1"])
# new column 
df["Job"] = ["Cook","N/A","cashier"]
# new row
new_row = pd.DataFrame([{"Name":"Sandy","Age":28,"Job":"Engineer"}],
                       index=["Employee 4"])
df = pd.concat([df,new_row])
print(df)


#import 
dataf = pd.read_csv("students.csv")
datajson = pd.read_json("user.json")
print(dataf)
print(datajson.to_string())


#selection by column
print(dataf["name"].to_string())


#selection by rows
# harsh is the row and height and weight are columns
print(dataf.loc["Harsh"],["height","Weight"])


# filtering = keeping the rows that match a condotion
tall = df[df["Height"]>=2]

heavy_pokemon = df[df["weight"]>100]
print(heavy_pokemon)

# can use or operator too in it
water_pokemon = df[(df["Type1"]=="Water") | (df["Type2"]=="Water")]
print(water_pokemon) 



## aggregate functions reduces a set of values into
#  a single sumamry value used to summarize and analyze
#  data often used with the groupby() function


#whole dataframe
print(df.mean(numeric_only=True))
print(df.sum(numeric_only=True))
print(df.min(numeric_only=True))
print(df.count())


#single column
print(df["Height"].mean())
print(df["Height"].sum())


# data cleaning = the process of fixing/removing incomplete,incorrect or irrevalant data.
#drop irrelevant columns
df = df.drop(columns=["Legendary"])

