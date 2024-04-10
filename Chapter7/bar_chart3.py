import matplotlib.pyplot as plt

def main():
    left_edges = [0, 10, 20, 30, 40, 50]
    heights = [100, 200, 300, 400, 500, 600]
    bar_width = 10
    
    plt.bar(left_edges, heights, bar_width, color=('r', 'g', 'b', 'y', 'm', 'c'))
    
    plt.title('Sales by Year')
    
    plt.xlabel('Year')
    plt.ylabel('Sales')
    
    plt.xticks([5, 15, 25, 35, 45, 55], ['2016', '2017', '2018', '2019', '2020', '2021'])   
    plt.yticks([0, 100, 200, 300, 400, 500], ['$0m', '$1m', '$2m', '$3m', '$4m', '$5m'])
    
    plt.grid(False)
    plt.show()

if __name__ == '__main__':
    main()