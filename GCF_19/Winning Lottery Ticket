import random

chosen_lott_num = [34, 29, 13, 8, 42, 55, 16]

random_lott_num = []
while len(random_lott_num) < 7:
    new_num = random.randint(1, 60)
    if new_num not in random_lott_num:
        random_lott_num.append(new_num)

count = 0

for num in random_lott_num:
    if num in chosen_lott_num:
        count += 1

print('You\'re chosedn lottery numbers: {}'.format(chosen_lott_num))
print('The winning lottery numbers: {}'.format(random_lott_num))


if count == 7:
    print('Congradulations!!! \'You\'ve won the grand prize of £ 1,000,000!!' )
elif count == 6:
    print('Congratulations!!!! You\'ve won £10,000!!!!')
elif count == 5:
    print('Congratulations!!! You\'ve won £100!!!')
elif count == 4:
    print('Congratulations!! You\'ve won £40!!')
elif count == 3:
    print('Congratulations! You\'ve won £20!')
else:
    print('Unfortunately, you\'ve not won a prize this time round. Better luck next time! ')
