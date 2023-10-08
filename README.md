# Introduction

A command-line calculator to help with your personal financial planning.

As of 3/18/2020, the application can be used via a basic Python IDE or the Linux command line.

This application is able to calculate and provide insights into your current personal financial situation, as well as give you valuable insights into a given financial scenario.

This application will keep a record of all queries both in a SQLite database and a CSV file. Both csv and SQL database files will allow you to analyze your queries in your chosen application. The idea is to give you tools to create various financial scenarios for yourself so that you will be able to plan ahead for a given situation.

When running the application, simply follow the program's instructions to enter a full query. The application will then show you all of your relevant data for the information entered.

# NEWS:

* 8/9/2020: The CSV file will eventually be replaced by the SQL database. There is currently no date for this change
* 7/2/2023: This open-source version will contain no data pipeline functionality to move `.csv` information to a Postgresql server. This process will need to be developed by the user.

# Additional Details

*DISCLAIMER:*

Please remember to back up your data. This application and its creators will not be held responsible for data that is accidentally erased by either the user or the user's computer. Please make sure to maintain your `FC_Log.csv` file in a safe location. This file has been added to the `.gitignore` file to prevent accidental upload to the public repo.

*Application Data Process*

REMEMBER: All data is stored directly in the file path where this application is located.

1. User enters requested data into the application
2. The application creates a new CSV file if it does not exist
3. The current query is logged into the CSV file
4. Create new SQLite database if it does not exist
5. Query is logged to the database
6. Application must be restarted to begin a new query
