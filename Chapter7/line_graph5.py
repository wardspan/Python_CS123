# This program displays a simple line graph.
import matplotlib.pyplot as plt

def main():
    x_coords = [0, 1, 2, 3 ,4]
    y_coords = [0, 3, 1, 5, 2]
    
    plt.plot(x_coords, y_coords, marker='o')
    plt.title('Sample Line Graph')
    plt.xlabel('X-axis label')
    plt.ylabel('Y-axis label')
    
    plt.xticks([0, 1, 2, 3, 4], ['A', 'B', 'C', 'D', 'E'])
    plt.yticks([0, 1, 2, 3, 4, 5], ['0', '1', '2', '3', '4', '5'])
    
    plt.grid(True)
    
    plt.show()
    
    
if __name__ == '__main__':
    main()
    