# a. Choose a dataset, you can use Seaborn [example datasets]. Create a cheat sheet for yourself containing all plot types discussed in the lecture. Provide the following info:

#         - Plot type

#         - Use cases (categorical data, distribution, etc.)

#         - Example on the dataset

import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

exercise = sns.load_dataset('exercise')

# Scatter Plot

sns.scatterplot(data=exercise, x='pulse', y='time', hue='diet')
plt.title('Scatter Plot: Pulse vs Time by Diet')
plt.show()

# Plot regplot
# sns.regplot(data=exercise, x='time', y='pulse')
# plt.title('Regression Plot: Time vs Pulse')
# plt.xlabel('Time (minutes)')
# plt.ylabel('Pulse')
# plt.show()

# Plot strip plot
sns.stripplot(data=exercise, x='kind', y='pulse', jitter=True)
plt.title('Strip Plot: Pulse Distribution by Kind of Exercise')
plt.xlabel('Kind of Exercise')
plt.ylabel('Pulse')
plt.show()

# Plot swarm plot
sns.swarmplot(data=exercise, x='kind', y='pulse')
plt.title('Swarm Plot: Pulse Distribution by Kind of Exercise')
plt.xlabel('Kind of Exercise')
plt.ylabel('Pulse')
plt.show()

# Line Plot
sns.lineplot(data=exercise, x='time', y='pulse', hue='diet')
plt.title('Line Plot: Time vs Pulse by Diet')
plt.show()

# Bar Plot
sns.barplot(data=exercise, x='diet', y='pulse', estimator=sum)
plt.title('Bar Plot: Total Pulse by Diet')
plt.show()

# Histogram
sns.histplot(data=exercise, x='pulse', bins=20, kde=True)
plt.title('Histogram: Distribution of Pulse')
plt.show()

# Box Plot
sns.boxplot(data=exercise, x='diet', y='pulse')
plt.title('Box Plot: Pulse by Diet')
plt.show()

# Violin Plot
sns.violinplot(data=exercise, x='diet', y='pulse')
plt.title('Violin Plot: Pulse by Diet')
plt.show()

# Pair Plot
sns.pairplot(exercise, hue='diet')
plt.title('Pair Plot: Pairwise Relationships in Exercise Dataset')
plt.show()

# Heatmap
exercise['time'] = exercise['time'].str.replace(' min', '').astype(int)
exercise_encoded = pd.get_dummies(exercise, columns=['diet', 'kind'])
correlation_matrix = exercise_encoded.corr()
sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm')
plt.title('Heatmap: Correlation Matrix of Exercise Dataset')
plt.show()

# Count Plot
sns.countplot(data=exercise, x='diet')
plt.title('Count Plot: Number of Observations per Diet')
plt.show()

# Boxen Plot
sns.boxenplot(data=exercise, x='diet', y='pulse')
plt.title('Boxen Plot: Pulse by Diet')
plt.show()
