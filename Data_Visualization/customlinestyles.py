import matplotlib.pyplot as plt

x = [1, 2, 3, 4, 5]
y = [2, 3, 5, 7, 11]

plt.plot(x, y, color='purple', linestyle='--', marker='o', markersize=8)
plt.title('Custom Line Styles')
plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.grid(True)  
plt.show()