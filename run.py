from first import startSql
import sys
print("started")

#query = sys.argv[1]
#### EMPLOYEE TABLE
# query = "name of employee whose id is 5"
# query = "name and id of employee whose id is 6"
# query = "name and city of employee whose id is 7"
# query = "name of employee whose city is chennai"
# query = "name of employee whose name of city is pune"
# query = 'count the number of employee whose name is akash'
# query = 'what is the number of employee whose name is chennai'
# query = 'count the number of employee whose salary greater than 50000'
# query = 'what is the name of employee whose mobile_no is 9568881238'
# query = "list name and mobile_no of employee whose city is pune and whose designation is SDE"
# query = "List the name and id of employees whose city is 'New Delhi' and nationality is American"
#
# #### STUDENT TABLE
# query = "list name of student whose id is 8"
# query = "what is name of student whose rank is 1"
# query = "list details of all student whose nationality is Indian"
# query = "what is the total number of student in class is XII"
# query = "count the number of student whose city is delhi"
# query = "what is the name and city of student whose rank is 1"
# query = "list city of student having rank less than 10"
# query = "what is the nationality and city of students whose marks equal to 100"
# query = "what is the name of student whose marks are not greater than 33"
# query = "what is the name of students whose marks are greater than 33"
# query = "list out name of students grouped by city"
# query = "list out name of students grouped by city and order by their rank"

### books
db = "db.sql"
# query = input("Enter Query\n")
query = "total number of customer who bought product with price greater than 5000"
# query = "list out name of books whose writer is 'Aakash Kumar'"
# query = "What is the name of the book having id as 17"
# query = "What is the genre of book whose name is 'Gone Girl'"
# query = "What is the genre of the book having name as 'Famous Five' "
# query = "Who is the writer of the book whose name is 'Revolution 2020' "
# query = "Count the total number of books having genre as Thriller"
# query = "What is the total number of books whose writer is 'Chetan Bhagat' "
# query = "Count the total number of books having pages greater than 300"
# query = "What is the total number of books having rating greater than 4"
# query = "Calculate the total number of copies_sold of books having the genre as Sci-Fi"
# query = "Count the total number of books whose writer is 'Paulo Coelho' having a rating greater than 4"



# db = input("Enter Path to SQL Dump\n")

#### movies query
# query = "List the names of movies that have rating as 5"
# query = "Count the number of movies having genre as Comedy"
# query = "Count the number of movies having release year as 2018"
# query = "What is the total number of movies whose rating greater than 3"
# query = "What is the name of the movie whose id is 8"
# query = "What is the genre of the movie having name as Tenet"
# query = "List director and release_year of movie whose name is 'World War Z'"
# query = "List the names of movies whose duration greater than 120 minutes."
# query = "What is the genre of the movie whose name is Game "
# query = "What is the duration of the movie whose name is 'Batman Begins'"
# query = "Count the number of movies whose director is 'Christopher Nolan'"
# query = "What is the release_year of the movie whose name is Interstellar"
# query = "List the names of the movies whose release_year is 2015 and rating greater than 4"

### Restaurants

# query = "What is the name of the restaurant whose id is 7"
# query = "What is the rating of the restaurant having name as 'BBQ Nation'"
# query = "What is the location of the restaurant whose name is 'Nazeer Foods'"
# query = "List the names of restaurants that have rating greater than 4"
# query = "List the names of restaurants having cuisine_type as Italian"
# query = "Count the number of restaurants having cuisine_type as Chinese"
# query = "List the names of restaurants that have location as 'South Delhi'"
# query = "Count the number of restaurants that have location as 'Central Delhi'"
# query = "Count the number of restaurants having daily_income greater than 10000"
# query = "Count the total number of restaurants that have average_cost less than 500"
# query = "Calculate the total daily_income of restaurants having rating equal to 5"
# query = "What is the total number of restaurants where home_delivery is available"
# query = "List the names of restaurants whose average_cost less than 1000 and rating greater than 3"
# query = "List the names of restaurants whose location is 'North Delhi' and where home_delivery is available"

### product customer

# query = "What is the name of the customer whose id is 18"
# query = "What is the address of the customer whose id is 34"
# query = "What is the phone_number of the customer whose id is 10"
# query = "Count the total number of customers that have address as Saket"
# query = "List the names of customers having bill_amount greater than 5000"
# query = "Count the total number of customers having payment_mode as Cash"
# query = "What is the name of the customer having phone_number as 9560013484"
# query = "Count the total number of customers who bought more than 20 items"X
# query = "Calculate the average bill_amount of customers having id less than 50"
# query = "List the payment_mode of customers having bill_amount greater than 3999"
# query = "Calculate the total bill_amount of the customers having address as Rohini"
# query = "Calculate the total items purchased by customers having payment_mode as UPI"
# query = "List the names of the customers having city as 'Malviya Nagar' and having bill_amount less than 3000"
# query = "What is the number of customers having payment_mode as 'Card' and bill_amount greater than 8000"


a = startSql(str(query), str(db))
# a = startSql(str(query), "./emp.sql")
# a = getSql_like(str(query), "./emp.sql")
print(a)
print("done")

# get all names from emp
