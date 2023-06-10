import pandas as pd

f = open("/home/shared_folder/2_0516/subject/length_info.txt", 'r')
df = pd.DataFrame()

length_info = []
for line in f.readlines():
    length_info.append(int(line.split("=")[1].strip()))

print(1)
df["length"] = length_info

df.to_csv("./df_length.csv", sep = ",")
