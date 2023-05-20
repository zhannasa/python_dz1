k = int(input('Enter the number of chocolate slices: '))
n_chocolate_length = 6
m_chocolate_width = 2
if (k % 2 == 0 and k < n_chocolate_length * m_chocolate_width):
    print('Yes')
else:
    print('No')