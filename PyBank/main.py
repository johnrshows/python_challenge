#dependencies

import os
import csv 

#path

csvpath = os.path.join('/Users/johnshows/Desktop/class/python_challenge/PyBank/Resources/budget_data.csv')

#variables

with open(csvpath, newline='') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    print(csvreader)
    csv_header = next(csvreader)
    month = []
    revenue = []
    revenue_change = []
    monthly_change = []
    
    print(f'Header: {csv_header}')               

#Month count      
    
    for row in csvreader:
        month.append(row[0])
        revenue.append(row[1])
    print(len(month))

 #Revenue count
    
    revenue_int = map(int,revenue)
    total_revenue = (sum(revenue_int))
    print(total_revenue)

 #Average change
    
    i = 0
    for i in range(len(revenue) - 1):
        profit_loss = int(revenue[i+1]) - int(revenue[i])
        revenue_change.append(profit_loss)
    Total = sum(revenue_change)
    monthly_change = Total / len(revenue_change)
    print(monthly_change)
    
    
#Greatest Increase
    
    profit_increase = max(revenue_change)
    print(profit_increase)
    k = revenue_change.index(profit_increase)
    month_increase = month[k+1]
    
#Greatest Decrease
    
    profit_decrease = min(revenue_change)
    print(profit_decrease)
    j = revenue_change.index(profit_decrease)
    month_decrease = month[j+1]


#output

output_path = os.path.join ("/Users/johnshows/Desktop/class/python_challenge/PyBank/Analysis","analysis.txt")

with open (output_path,'w') as txtfile:

    txtfile.write(f'Financial Analysis'+'\n')
    txtfile.write(f'----------------------------'+'\n')


    txtfile.write('Total number of months: ' + str(len(month)) +'\n')

    txtfile.write('Total Revenue in period: $ ' + str(total_revenue)+'\n')
        
    txtfile.write('Average monthly change in Revenue : $' + str(monthly_change)+'\n')

    txtfile.write(f'Greatest Increase in Profits: {month_increase} (${profit_increase})'+'\n')

    txtfile.write(f'Greatest Decrease in Profits: {month_decrease} (${profit_decrease})'+'\n')


