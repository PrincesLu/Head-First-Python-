import random

random_lott_num = []

chosen_lott_num = []

while len(random_lott_num) < 7:
    new_num = random.randint(1,60)

    if new_num not in random_lott_num:
        random_lott_num.append(new_num)

while len(chosen_lott_num) < 7:
    num_choice = int(input('What number between 1 and 59 inclusive would you like to choose? '))

    if num_choice in chosen_lott_num:
        print('Please choose a number you have\'t already chosen. ')

    while num_choice < 1 or num_choice > 59:
        num_choice = int(input('Please choose a number between 1 and 59 inclusive: '))
        if num_choice in chosen_lott_num:
            print('Please choose a number you have\'t already chosesn. ')
    if num_choice not in chosen_lott_num:
        chosen_lott_num.append(num_choice)

count = 0

for num in random_lott_num:
    if num in chosen_lott_num:
        count +=1
print('You\'re chosen lottery numbers: {}\n'.format(chosen_lott_num))
print('The winning lottery numbers: {}\n'.format(random_lott_num))

if count == 7:
    print('Congratulations!!!!! You\'ve won the grand prize of £1,000,000!!!!!')
elif count == 6:
    print('Congratulations!!!! You\'ve won £10,000!!!!')
elif count == 5:
    print('Congratulations!!! You\'ve won £100!!!')
elif count == 4:
    print('Congratulations!! You\'ve won £40!!')
elif count == 3:
    print('Congratulations! You\'ve won £20!')
else:
    print('Unfortunately, you\'ve not won a prize this time round. Better luck next time!')
