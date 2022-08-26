
import matplotlib.pyplot as plt

# data 

month_exp_labels = ["Home Rent" , 'Food','Phone/Internet Bill','bike','Other Utilities']
exp_value = [7000 ,6000 , 4000 , 3500 , 2000]

# plot pie chart 

plt.pie(exp_value , labels = month_exp_labels)
plt.show()
