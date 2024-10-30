# Import necessary libraries
import seaborn as sns
import matplotlib.pyplot as plt

# Load the Iris dataset
data = sns.load_dataset("iris")

# Set the figure size
plt.figure(figsize=(10, 6))

# Create a box plot for petal length by species
sns.boxplot(data=data, x="species", y="petal_length", palette="Set2")

# Add titles and labels
plt.title("Box Plot of Petal Length by Species")
plt.xlabel("Species")
plt.ylabel("Petal Length (cm)")

# Save the plot 
plt.savefig("boxplot.png")  

# Show the plot
plt.show()
