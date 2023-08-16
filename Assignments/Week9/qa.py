import matplotlib.pyplot as plt
from numpy.random import randn

fig = plt.figure()                                  # the initial figure is going to be blank

# add a varierty of sub plots to it,
# the first two parameters describe the size of the grid
# that corresponds to the sub figures being added.
# 2 by 2 means we have a grid of four different sub plots
# and we are going to use that to compare and contrast the styles of the different figures. 
# the last parameter refers to which of the sub plots we are adding to.
# so one refers to the top left of the first out of the four subplots in the figure
sp1 = fig.add_subplot(2, 2, 1)


# generate some random numbers
y = randn(30)
# print(y)

# Note that we are creating multiple sub plots
# for the time being we are only filling in one of the four elements on the grid
# therefore we only see a signle plot
sp1.plot(y)
fig.set_size_inches(15, 10)
fig.show()