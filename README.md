# bTechProject

### How to Run
python2 run.py

It will ask for query, give your query
It will ask for sql dump path, give your sql dump file path

e.g. query = "Give name of all employee whose cityName is pune"
     sql dump = "emp.sql"
     
output = SELECT employee.name FROM employee INNER JOIN city ON employee.cityId = city.id WHERE city.cityName = 'pune';
