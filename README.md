# Pay-Calculator-Python
This is a simple pay calculator that utilises inputted information to create an estimated pay through its calculations. 

Late hours are payed at 1.5x
Weekend hours are payed at 2x.
Overtime hours are payed at 2x

The system makes sure to consider for breaks that may be taken and deducts the pay is regards to the pay-to-minute ratio. Float() was used opposed to int() as it allowed for decimals to be used in the inputs of both the hours worked and the pay as these numbers are rarely whole numbers.

There is also tax included on any pay that is over $350 in week and is taxed at a 16% rate. This may cause results to differ due to the varying tax rates.
