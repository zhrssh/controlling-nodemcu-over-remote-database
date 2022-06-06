import urllib.request
import http

# local files
from database import Database
from time import sleep

# arduino local ip
url = "http://192.168.1.12/"

# database
HOST = ""
USER = ""
PASSWORD = ""
DATABASE = ""

# these must be existing in the database
TABLENAME = "casestudy"
COLUMNS = ["id", "value"]

# start of the code
def start():
    while True:

        # get data from NodeMCU
        get_data()

        # reconstruct data into list
        mylist = reconstruct_data()

        # sets up the connection between python and database
        mydb = Database(HOST, USER, PASSWORD, DATABASE)

        # insert data into the database
        print("Inserting " + mylist[1])
        mydb.update(TABLENAME, COLUMNS, mylist)

        # closes all connection after using
        mydb.close()

        # sleep for 15 seconds
        sleep(10)

    ### FOR TESTING AND DEBUGGING ###
    # mydb.insert("example", dbcolumns, mydata.get_datalist())
    # mydb.delete("example", "1 = 1")
    # mydb.print_last_five("example")
    #################################


def transfer_data(mydata):
    try:
        x = urllib.request.urlopen(url + f"{mydata}").read()
        x = x.decode("utf-8")

        return x
    except http.client.HTTPException as e:
        return e


# function to get data from arduino
def get_data():
    global data

    # requests data from the url
    try:
        x = urllib.request.urlopen(url).read()
        x = x.decode("utf-8")

        # for testing
        # x = "1234567$1001"

        data = x
    except http.client.BadStatusLine as e:
        data = str(e)


# function to reconstruct data into a list
def reconstruct_data():

    # splits the data into list
    data_list = data.split("$")
    return data_list


# driver code
if __name__ == "__main__":
    start()
