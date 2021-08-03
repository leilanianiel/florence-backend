# FlorenceBackend

Backend Florence Fridge App

Florence FridgeApp can assist in making our lives easier and more efficient. This app would minimize the amount of food waste in everyday homes. Similar to smart fridges; Florence would keep an inventory of the food that is stored in your fridge. The app would keep baseline expiration dates of foods and also be able to add inventory, sort by food item and more. When food is closest to expiring it would be pushed to the top of the list. With the inventory being stored, Florence would suggest recipes based on categories and keywords, and would always suggest recipes close to expiration food first. This would be an affordable alternative to a smart fridge and would help everyday user take the stress out of cooking and food waste.



# Create a virtual environment:

$ python3 -m venv venv
$ source venv/bin/activate
(venv) $ # You're in activated virtual environment!
Install dependencies (we've already gathered them all into a requirements.txt file):

(venv) $ pip install -r requirements.txt
Setting Up Development and Test Databases
Create a database:

A development database named video_store_api_development
[OPTIONAL] A test database named video_store_api_test
There are no Pytest tests for this project. If you choose to write your own using the tests from Task List as a model, we recommend you also use a testing database
Creating a .env File
Create a file named .env.

Create two environment variables that will hold your database URLs.

SQLALCHEMY_DATABASE_URI to hold the path to your development database
[OPTIONAL] SQLALCHEMY_TEST_DATABASE_URI to hold the path to your development database
Your .env may look like this:

SQLALCHEMY_DATABASE_URI=postgresql+psycopg2://postgres:postgres@localhost:5432/task_list_api_development
SQLALCHEMY_TEST_DATABASE_URI=postgresql+psycopg2://postgres:postgres@localhost:5432/task_list_api_test
Run $ flask db init
Run $ flask db init.

After you make your first model in Wave 1, run the other commands flask db migrate and flask db upgrade.

Run $ flask run or $ FLASK_ENV=development flask run
Check that your Flask server can run with $ flask run.

We can run the Flask server specifying that we're working in the development environment. This enables hot-reloading, which is a feature that refreshes the Flask server every time there is a detected change.

$ FLASK_ENV=development flask run
It is highly recommended to run the Flask servers with this command.
