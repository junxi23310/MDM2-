import matplotlib.pyplot as plt
plt.close('all')
import pandas as pd 
import numpy as np
T = pd.read_csv('C:/Users/dell/Downloads/titanic (1).csv')
print(T.iloc[:8, :])
random_indices = np.random.randint(0, len(T), size=50)
random_sample = T.iloc[random_indices]

first = (T['Pclass'] == 1)
second = (T['Pclass'] == 2)
third = (T['Pclass'] == 3)
male = (T['Sex'] == "male")
female = (T['Sex'] == "female")
child = (T['Age'] < 18)
young = (T['Age'] >= 18) & (T['Age'] <= 40)
old = (T['Age'] > 40)

deceased = random_sample[random_sample['Survived'] == 0]
male_deceased = deceased[male]
male_child_deceased = male_deceased[child].shape[0]   # 儿童
male_young_deceased = male_deceased[young].shape[0]   # 青年
male_old_deceased = male_deceased[old].shape[0] 
# 年龄段和对应的遇难人数
age_groups = ['儿童', '青年', '老年']
death_counts = [male_child_deceased, male_young_deceased, male_old_deceased]

# 绘制柱状图
plt.bar(age_groups, death_counts, color=['blue', 'green', 'red'])
plt.xlabel('age')
plt.ylabel('people')
plt.title('nb')
plt.show()

