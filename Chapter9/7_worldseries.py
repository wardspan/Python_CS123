# Write a program that reads WorldSeriesWinners.txt and creates a dictionary in which the keys 
# are the names of the teams, and each key’s associated value is the number of times the team 
# has won the World Series. The program should also create a dictionary in which the keys are 
# the years, and each key’s associated value is the name of the team that won that year.
# The program should prompt the user for a year in the range of 1903 through 2009. It should then 
# display the name of the team that won the World Series that year, and the number of times that
# team has won the World Series.

def read_world_series_winners():
    winners = {}
    years = {}

    with open('WorldSeriesWinners.txt', 'r') as file:
        for line in file:
            year, team = line.strip().split(',')
            winners[team] = winners.get(team, 0) + 1
            years[year] = team

    return winners, years

def main():
    winners, years = read_world_series_winners()

    year = int(input("Enter a year (1903-2009): "))
    if str(year) in years:
        team = years[str(year)]
        wins = winners[team]
        print(f"The {team} won the World Series in {year} and has won it {wins} times.")
    else:
        print("No data available for that year.")

if __name__ == '__main__':
    main()