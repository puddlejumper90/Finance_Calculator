A command-line calculator to help with your personal financial planning.

As of 3/18/2020, the application can be used via a basic python IDE or the Linux command line.

This application is able to calculate and provide insights into your current personal financial situation, as well as give you valuable insights on a given financial scenario.

This application will keep a record all queries both in a SQLite database and a CSV file. Both csv and SQL database files will allow you to analyze your queries in your chosen application. The idea is to give you tools to create various financial scenarios for yourself so that you will be able to plan ahead for a given situation.

When running the application, simply follow the program's instructions to enter a full query. The application will then show you all of your relevant data for the information entered.

NEWS:

8/9/2020: The CSV file will eventually be replaced by the SQL database. There is currently no date for this change


*DISCLAIMER:*

Please remember to backup your data. This application and its creators will not be held responsible for data that is accidentally erased by either the user or the user's computer.

*Application Data Process*

REMEMBER: All data is stored directly to the file path where this application is located.

1. User enters requested data into the application
2. The application creates a new CSV file if it does not exists
3. Current query is logged into the CSV file
4. Creates new sqlite database if it does not exist
5. Query is logged to the database
6. Application must be restarted to begin new query
