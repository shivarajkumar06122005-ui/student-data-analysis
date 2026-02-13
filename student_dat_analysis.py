import pandas as pd
import matplotlib.pyplot as plt

data = {
    "Name": ["A", "B", "C", "D"],
    "Math": [85, 78, 92, 70],
    "Science": [90, 75, 88, 65]
}

df = pd.DataFrame(data)
# total marks for each student
df["Total"] = df["Math"] + df["Science"]
print(df) 
# Average marks for each students
df["Average"] = df["Total"] / 2
print(df)
# topper of the class
topper = df.loc[df["Total"].idxmax()]
print("Topper of the class:")
print(topper)

df["Rank"] = df ["Total"].rank(ascending=False).astype(int)
print(df)
# Add line to chart comparsion

plt.figure()

plt.plot(df["Name"], df["Math"], marker='o')
plt.plot(df["Name"], df["Science"], marker='o')

plt.title("Subject-wise Comparison")
plt.xlabel("Students")
plt.ylabel("Marks")
plt.legend(["Math", "Science"])

plt.show()


plt.figure()

bars = plt.bar(df["Name"], df["Total"])

# Add value labels on top
for bar in bars:
    y = bar.get_height()
    plt.text(bar.get_x() + bar.get_width()/2, y, str(y), 
             ha='center', va='bottom')

plt.title("Total Marks of Students")
plt.xlabel("Students")
plt.ylabel("Total Marks")

plt.show()


print(df)
