
import pandas as pd

data = pd.read_csv("data25.csv", delimiter=";",
                   names=['Label', 'Size'])
print(data)

def job():

    try:

        Enter_1 = str(input("Enter сolumn name"))
        Enter_2 = int(input("Enter cell number"))

        print(data.at [Enter_2, Enter_1])

    except ValueError:
        print("Oops! You were hurt as a child")

    except NameError:
        print("Oops! You were hurt as a child")

    except TypeError:
        print("Oops! You were hurt as a child")

    except KeyError:
        print("Oops! You were hurt as a child")


job()






