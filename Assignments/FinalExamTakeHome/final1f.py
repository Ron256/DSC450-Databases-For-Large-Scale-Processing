# Ronaldlee Ejalu
# DSC 450
# Final Take home exam
# plotting the resulting runtime (# of tweets versus run times)
# using matplotlib for 1-a, 1-c, 1-d, and 1-e
# 1f
import pandas as pd
import matplotlib.pyplot as plt
import os

os.chdir('C:/Users/rejalu1/OneDrive - Henry Ford Health System/DSC450/Assignments/FinalExamTakeHome')

# deriving the data structures for the runtimes of the number of tweets for the 
# questions 1a, 1c, 1d, and 1e
dataForA = [(500, 1016.9364602565765), (50, 288.94251561164856)]
dataForC = [(500, 3012.9960594177246), (50, 279.7146816253662)]
dataForD = [(500, 172.24891209602356), (50, 14.039840698242188)]
dataForE = [(500, 173.3715558052063), (50, 8.637104034423828)]

# derive the different data frames
dfRunTimeA = pd.DataFrame(dataForA, columns=['NumberOfTweets', 'RunTimeinSecs'])
dfRunTimeC = pd.DataFrame(dataForC, columns=['NumberOfTweets', 'RunTimeinSecs'])
dfRunTimeD = pd.DataFrame(dataForD, columns=['NumberOfTweets', 'RunTimeinSecs'])
dfRunTimeE = pd.DataFrame(dataForE, columns=['NumberOfTweets', 'RunTimeinSecs'])
print(dfRunTimeE)

fig = plt.figure()                                          # create a blank figure

# add a varierty of sub plots to it,
# the first two parameters describe the size of the grid
# that corresponds to the sub figures being added.
# 2 by 2 means we have a grid of four different sub plots
# and we are going to use that to compare and contrast the styles of the different figures. 
# the last parameter refers to which of the sub plots we are adding to.
# so one refers to the top left of the first out of the four subplots in the figure

sp = fig.add_subplot(2, 2, 1)                                    # Add a grid of 4 subplots
fig.set_size_inches(15, 15)                                      # set the figure size in inches. 

sp.plot(dfRunTimeA['NumberOfTweets'], dfRunTimeA['RunTimeinSecs'], '--')
sp.set_ylim(bottom=0)
sp.set_title("# of Tweets versus runtime for 1a", fontsize = 12)
sp.set_xlabel('NumberOfTweets (in thousands)', fontsize = 12)
sp.set_ylabel('Run Time in Seconds', fontsize = 12)


# creating a nother sub plot and we are using a 2 by 2 grid.
# in this case we are adding the secondor  top-right subplot to the figure 
# you can use different grading within the same figure but that does potentially 
# create overlay which you may or may not want to have in practice. 
# just note that is it possible but we will keep consistent grading into two-by-two
sp2 = fig.add_subplot(2, 2, 2) # so this addes the second sub plot to the top right
sp2.plot(dfRunTimeC['NumberOfTweets'], dfRunTimeC['RunTimeinSecs'], '-')
sp2.set_ylim(bottom=0)
sp2.set_title("# of Tweets versus runtime for 1c", fontsize = 12)                               # add the title to the plot                         
sp2.set_xlabel('NumberOfTweets (in thousands)', fontsize = 12)                                  # adding the x-axis label                     
sp2.set_ylabel('Run Time in Seconds', fontsize = 12)                                            # adding y-axis label

# next we add a third subplot and we are adding in the botton left, through the subplot
sp3 = fig.add_subplot(2, 2, 3) 
sp3.plot(dfRunTimeD['NumberOfTweets'], dfRunTimeD['RunTimeinSecs'],'-.') 
sp3.set_ylim(bottom=0)
sp3.set_title("# of Tweets versus runtime for 1d", fontsize = 12)                               # add the title to the plot                         
sp3.set_xlabel('NumberOfTweets (in thousands)', fontsize = 12)                                  # adding the x-axis label                     
sp3.set_ylabel('Run Time in Seconds', fontsize = 12)                                            # adding y-axis label
# sp3.set_ylim([15, 180])

# lets continue with fourth subplot
# Again, two by two adding to the fourth location over here
sp4 = fig.add_subplot(2, 2, 4)
sp4.plot(dfRunTimeE['NumberOfTweets'], dfRunTimeE['RunTimeinSecs']) 
sp4.set_ylim(bottom=0)
sp4.set_title("# of Tweets versus runtime for 1e", fontsize = 12)                               # add the title to the plot                         
sp4.set_xlabel('NumberOfTweets (in thousands)', fontsize = 12)                                  # adding the x-axis label                     
sp4.set_ylabel('Run Time in Seconds', fontsize = 12)                                            # adding y-axis label
#fig
fig.savefig('1e.pdf', bbox_inches='tight')                                  # save the file in pdf




