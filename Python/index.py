import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load data
df = pd.read_csv('data.csv')

#1. Bar Chart: Number of students per course
plt.figure(figsize=(6,4))
df['Course'].value_counts().plot(kind='bar', color='skyblue')
plt.title('Number of Students per Course')
plt.xlabel('Course')
plt.ylabel('Count')
plt.tight_layout()
plt.savefig('bar_chart.png')
plt.close()

# 2. Line Chart: Age distribution by Student_ID
plt.figure(figsize=(6,4))
plt.plot(df['Student_ID'], df['Age'], marker='o')
plt.title('Student Age by Student ID')
plt.xlabel('Student ID')
plt.ylabel('Age')
plt.tight_layout()
plt.savefig('line_chart.png')
plt.close()

# 3. Pie Chart: Gender distribution
plt.figure(figsize=(5,5))
gender_counts = df['Gender'].value_counts()
plt.pie(gender_counts, labels=gender_counts.index, autopct='%1.1f%%', colors=['#ff9999','#66b3ff'])
plt.title('Gender Distribution')
plt.tight_layout()
plt.savefig('pie_chart.png')
plt.close()

# 4. Histogram: Age distribution
plt.figure(figsize=(6,4))
plt.hist(df['Age'], bins=5, color='lightgreen', edgecolor='black')
plt.title('Age Distribution')
plt.xlabel('Age')
plt.ylabel('Frequency')
plt.tight_layout()
plt.savefig('histogram.png')
plt.close()

# 5. Scatter Plot: Age vs Student_ID
plt.figure(figsize=(6,4))
plt.scatter(df['Student_ID'], df['Age'], c='purple')
plt.title('Age vs Student ID')
plt.xlabel('Student ID')
plt.ylabel('Age')
plt.tight_layout()
plt.savefig('scatter_plot.png')
plt.close()

# 6. Box Plot: Age by Gender
plt.figure(figsize=(6,4))
sns.boxplot(x='Gender', y='Age', data=df, palette='pastel')
plt.title('Age Distribution by Gender')
plt.tight_layout()
plt.savefig('box_plot.png')
plt.close()

# 7. Area Chart: Cumulative count of students by age
plt.figure(figsize=(6,4))
df_sorted = df.sort_values('Age')
cum_counts = df_sorted['Age'].value_counts().sort_index().cumsum()
plt.fill_between(cum_counts.index, cum_counts.values, color='orange', alpha=0.5)
plt.title('Cumulative Number of Students by Age')
plt.xlabel('Age')
plt.ylabel('Cumulative Count')
plt.tight_layout()
plt.savefig('area_chart.png')
plt.close()

# 8. Heatmap: Count of students by Course and Exam Center
plt.figure(figsize=(7,5))
pivot = pd.pivot_table(df, index='Course', columns='Exam_Center', values='Student_ID', aggfunc='count', fill_value=0)
sns.heatmap(pivot, annot=True, cmap='YlGnBu')
plt.title('Students by Course and Exam Center')
plt.tight_layout()
plt.savefig('heatmap.png')
plt.close()

# 9. Bubble Chart: Age vs Student_ID, bubble size by Penalty severity
penalty_map = {'None': 10, 'Warning': 30, 'Zero marks': 50, 'Exam cancelled': 70, 'One-semester suspension': 90, 'One-year suspension': 110, 'Expulsion': 130}
bubble_size = df['Penalty'].map(penalty_map).fillna(10)
plt.figure(figsize=(6,4))
plt.scatter(df['Student_ID'], df['Age'], s=bubble_size, alpha=0.5, c='red', edgecolors='w', linewidth=0.5)
plt.title('Bubble Chart: Age vs Student ID (Bubble = Penalty Severity)')
plt.xlabel('Student ID')
plt.ylabel('Age')
plt.tight_layout()
plt.savefig('bubble_chart.png')
plt.close()