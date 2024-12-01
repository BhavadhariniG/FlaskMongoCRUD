# FlaskMongoCRUD
This Flask-based web application allows users to submit, view, and manage personal details like Name, Email ID, Mobile number, and Place. The application interacts with a MongoDB database to store and retrieve user submissions. The app is divided into several key routes and uses templates for a seamless user experience. Below is an explanation and analysis of the application.
# Features
1. Home Page:

A welcoming page with navigation options to explore the website.

2. Add User Details:

Users can add their information (Name, Email ID, Mobile number, and Place) using a form.
Data is saved to a MongoDB collection.

3. how Details:

Displays the submitted user details in a table format.
Data is dynamically fetched from MongoDB.

4. Submit Confirmation:

After adding details, users are redirected to a submission confirmation page with navigation links to other sections.

5. Modular Templates:

Uses Jinja2 templating to provide a consistent layout across pages.
Includes a navigation bar and footer shared across all pages.

# Route Analysis
1. /home

Serves as the main page.
Rendered using home.html, which is extended from base.html.

2. /submit

A simple confirmation page displayed after form submission.

3. /show

Fetches all records from the MongoDB collection submission_list using students.find().
Displays the data in a styled table.

4. /Add

Handles both GET and POST requests.
GET: Renders a form for input.
POST: Collects form data, structures it as a dictionary, and inserts it into MongoDB using insert_one.

# Code Breakdown
1. Flask Setup

The app is initialized with Flask and connected to MongoDB via MongoClient.

2. Database Configuration

MongoDB is used locally (localhost:27017).
The database is local, and the collection is submission_list.

3. Template Design

HTML templates leverage Jinja2 for dynamic content.
A base template (base.html) provides a consistent structure with a navigation bar and footer.

4. CSS Styling

Basic inline CSS styles for headers, buttons, forms, and tables.

# Result Analysis
1. Form Submission

Form validation ensures mandatory fields are filled before submission.
On successful submission, data is correctly inserted into MongoDB.

2. Data Retrieval

Records are dynamically displayed in a styled table, allowing users to see all submissions in an organized way.

3. Navigation

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

