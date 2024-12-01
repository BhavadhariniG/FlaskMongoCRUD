# FlaskMongoCRUD
This Flask-based web application allows users to submit, view, and manage personal details like Name, Email ID, Mobile number, and Place. The application interacts with a MongoDB database to store and retrieve user submissions. The app is divided into several key routes and uses templates for a seamless user experience. Below is an explanation and analysis of the application.
# Features
Home Page:
A welcoming page with navigation options to explore the website.

Add User Details:

Users can add their information (Name, Email ID, Mobile number, and Place) using a form.
Data is saved to a MongoDB collection.
Show Details:

Displays the submitted user details in a table format.
Data is dynamically fetched from MongoDB.
Submit Confirmation:

After adding details, users are redirected to a submission confirmation page with navigation links to other sections.
Modular Templates:

Uses Jinja2 templating to provide a consistent layout across pages.
Includes a navigation bar and footer shared across all pages.
# Route Analysis
/home

Serves as the main page.
Rendered using home.html, which is extended from base.html.
/submit

A simple confirmation page displayed after form submission.
/show

Fetches all records from the MongoDB collection submission_list using students.find().
Displays the data in a styled table.
/Add

Handles both GET and POST requests.
GET: Renders a form for input.
POST: Collects form data, structures it as a dictionary, and inserts it into MongoDB using insert_one.
# Code Breakdown
Flask Setup

The app is initialized with Flask and connected to MongoDB via MongoClient.
Database Configuration

MongoDB is used locally (localhost:27017).
The database is local, and the collection is submission_list.
Template Design

HTML templates leverage Jinja2 for dynamic content.
A base template (base.html) provides a consistent structure with a navigation bar and footer.
CSS Styling

Basic inline CSS styles for headers, buttons, forms, and tables.
# Result Analysis
Form Submission

Form validation ensures mandatory fields are filled before submission.
On successful submission, data is correctly inserted into MongoDB.
Data Retrieval

Records are dynamically displayed in a styled table, allowing users to see all submissions in an organized way.
Navigation

The navigation bar provides quick access to all key sections.
Links on the submission confirmation page ensure seamless user flow.
# How to Run
Clone the repository:
git clone <repository-url>

Navigate to the project directory:
cd project-directory

Install the required dependencies:
pip install flask pymongo

Run the application:
python app.py

Access the application in your browser at http://127.0.0.1:5000/home.
# Technologies Used
Backend: Flask
Database: MongoDB
Frontend: HTML, CSS, Jinja2 Templating
# Future Enhancements
Add input validation for mobile numbers and email IDs.
Implement update and delete functionality for submitted records.
Enhance the UI with Bootstrap or similar frameworks.
Introduce user authentication for secure submissions and access.

