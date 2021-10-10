voting_data = [
    {"county":"Arapahoe", "registered_voters": 422829},
    {"county":"Denver", "registered_voters": 463353}, 
    {"county":"Jefferson", "registered_voters": 432438}
    ]

#row_index = 0
#for counties in voting_data:
#    print(f'{voting_data[row_index]["county"]} county has {voting_data[row_index]["registered_voters"]} voters.')

#    row_index = row_index + 1

for row_index in range(len(voting_data)):
    print(f'{row_index,voting_data[row_index]["county"]}')

Some_list = [4,1,2,6,9]

for a in Some_list:
    print(a)

for b in range(len(Some_list)):
    print(b,Some_list[b])
