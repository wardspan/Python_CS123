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