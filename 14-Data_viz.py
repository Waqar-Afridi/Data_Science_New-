import seaborn as sns
import matplotlib.pyplot as plt
sns.set_theme(style="ticks", color_codes=True)
titanic=sns.load_dataset("titanic")
print(titanic)

# sns.countplot(x="sex",data=titanic)
# plt.show()

# sns.countplot(x="sex",hue="class",data=titanic)
# plt.show()

p=sns.countplot(x="sex",hue="class",data=titanic)
p.set_title("plot for basic count plot")
plt.show()
# to edit this file we pull it
# to to update file in github we need to commmit again 
