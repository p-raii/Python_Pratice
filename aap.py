import matplotlib.pyplot as plt


a = [1, 2, 3, 4, 5]
b = [0, 0.6, 0.2, 15, 10, 8, 16, 21]
c = [4, 2, 6, 8, 3, 20, 13, 15]

# use fig whenever u want the
# output in a new window also
# specify the window size you
# want ans to be displayed
fig = plt.figure(figsize =(5, 10))

# creating multiple plots in a
# single plot
sub1 = plt.subplot(1, 2, 1)
sub2 = plt.subplot(1, 2, 2)
# sub3 = plt.subplot(2, 2, 3)
# sub4 = plt.subplot(2, 2, 4)

sub1.plot(a, '*b')

# sets how the display subplot
# x axis values advances by 1
# within the specified range
sub1.set_xticks(list(range(0, 10, 1)))
sub1.set_title('1st Rep')

sub2.plot(b, 'or')

# sets how the display subplot x axis
# values advances by 2 within the
# specified range
sub2.set_xticks(list(range(0, 10, 2)))
sub2.set_title('2nd Rep')


# without writing plt.show() no plot
# will be visible
plt.show()
