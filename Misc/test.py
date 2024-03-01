ranks = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
ranks_string = ''.join(ranks)
print(ranks_string)
search_sequence = '45'
if search_sequence in ranks_string:
    print("Sequence found!")
else:
    print("Sequence not found.")


 elif (ranks[0],ranks[1]) or (ranks[1],ranks[0]) in ranks_string:


elif ranks[0] in '23456789' and ranks[1] in '23456789':
    if abs(int(ranks[0]) - int(ranks[1])) == 1 and suits[0] == suits[1]:
        bonus_points += 70
    elif abs(int(ranks[0]) - int(ranks[1])) == 1 and suits[0] != suits[1]:
        bonus_points += 50