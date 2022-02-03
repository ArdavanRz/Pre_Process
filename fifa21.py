import pandas as panda  # name the library for further usage
import  seaborn as seaborn
import matplotlib.pyplot as plt

panda.set_option('display.max_columns', None)  # Since our data is too large to fit the console, we force pandas to
# display all of the availabe columns

fifa21 = panda.read_csv('players.csv')  # we instantiate our csv and name it fifa21

print("select your desired command from 1 to 10")
command = input()

if command == "1" :
 print("displaying players.csv")
 print(fifa21.head())  # print the entire csv file


if command == "2" :
 panda.set_option('display.max_rows', None)
 print("displaying the count of missing values in each column")
 missing = fifa21.isna().sum()  # we make an instance of the isna function result and print
 print(missing)


if command == "3" :
    print("average weight for all the players :")
    avg = fifa21["Weight"].mean()
    print(avg)

    print("highest Weigh among all players :")
    max_weight = fifa21["Weight"].max()
    print(max_weight)

    print("lowest Weigh among all players :")
    min_weight = fifa21["Weight"].min()
    print(min_weight)

if command == "4" :
    print(" club members for each nation :")
    nation = fifa21["Nationality"].value_counts()
    print(nation)

    print(" the nation with the most members :")
    nation = fifa21["Nationality"].value_counts()
    highest = nation.index[0]
    print(highest)

    print(" the nation with the least members :")
    lowest = nation.index[-1]
    print(lowest)


if command == "5" :
    print("listing promising players :")
    panda.set_option('display.max_rows', None)
    star = fifa21.loc[(fifa21['Growth'] > 4) & (fifa21['Potential'] > 84) , ['Name','Potential','Growth']]
    print(star)


if command == "6" :
    print("now plotting promising players :")
    star = fifa21.loc[(fifa21['Growth'] > 4) & (fifa21['Potential'] > 84), ['Potential', 'Growth','BestPosition']]
    seaborn.lmplot(x='Potential', y='Growth', data=star, hue='BestPosition',fit_reg=False)
    plt.show()


if command == "7" :
    print("the club with the most promising players :")
    star = fifa21.loc[(fifa21['Growth'] > 4) & (fifa21['Potential'] > 84), ['Club']]
    star_count = star["Club"].value_counts()
    print(star_count)


if command == "8" :
    print("now listing chelsea's promising players' worth in Euros :")
    worth = fifa21.loc[(fifa21['Growth'] > 4) & (fifa21['Potential'] > 84) & (fifa21['Club'] == "Chelsea"), ['Name','ValueEUR']]
    print(worth)

    print("total worth :")
    total_worth = worth['ValueEUR'].sum()
    print(total_worth)


if command == "9" :
    print("listing players with contracts expired by 2021 and not present in a national team :")
    contract = fifa21.loc[(fifa21['ContractUntil'] == 2021) & (fifa21['NationalTeam'] == "Not in team"), ['Name']]
    print(contract)

    print("total players matching this criteria :")
    print(contract.size)


if command == "10" :
    print("info related to Mehdi taremi")
    mehdi = fifa21.loc[(fifa21['Name'] == "M. Taremi") , ['Club','Positions','ValueEUR']]
    print(mehdi)









