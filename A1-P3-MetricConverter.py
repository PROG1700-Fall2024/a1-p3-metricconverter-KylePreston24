#Program 3 – Imperial to Metric Conversion
#Write a console program that converts a weight given in tons (imperial), stones, pounds, and ounces 
# to the metric equivalent in metric tons, kilograms, and grams.

"""
Student Name: Kyle Preston
Program: Program 3 – Imperial to Metric Conversion


"""



def main():
    # YOUR CODE STARTS HERE, each line must be indented (one tab)


       #Variables for all imperial and metric values

    tons = float(0) 
    stone = float(0)
    pounds = float(0)
    ounces = float(0)
    grams = float(0)
    kilos = float(0)
    metricTons = float(0)
    totalOunces = float(0)
    totalKilos = float(0)
    
    #Input  for all our imperial values tons/stone/pounds/ounces    

    tons = input("Enter the number of tons: ")

    stone = input("Enter the number of stone: ")  

    pounds = input("Enter the number of pounds: ")

    ounces = input("Enter the number of ounces: ")


    # Calcultions  Total ounces-

    totalOunces = 35840 * float(tons) + 224 * float(stone) + 16 * float(pounds) + float(ounces)

    # Total Kilos from ounces conversion

    totalKilos = totalOunces / 35.274

    # Metric ton from total kilos conversion 

    metricTons = int(totalKilos/1000)

    #kilo Calculation

    kilos = int(totalKilos - metricTons * 1000)


    # Grams calculation

    grams = (totalKilos - (metricTons * 1000) - int(kilos)) * 1000

    #PRINT STATEMENT will show all values in metric form with grams having one decimal 

    print("The metric weight is {0} metric tons, {1} kilos, and {2:.1f} grams.".format(metricTons, kilos, grams))



    # YOUR CODE ENDS HERE

main()