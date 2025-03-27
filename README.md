# To-Do Application with Flet and SQLite3

This project is a simple to-do application built using Flet for the user interface and SQLite3 for the back-end database. The application allows users to create, read, update, and delete tasks. It also includes user authentication with JWT-based login and signup, Argon2 for password hashing, and Redis for caching.

## App Setup

1. Clone the repository:
   ```
   git clone https://github.com/githubnext/workspace-blank.git
   cd workspace-blank
   ```

2. Create a virtual environment and activate it:
   ```
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. Install the required dependencies:
   ```
   pip install -r requirements.txt
   ```

4. Run the application:
   ```
   python app.py
   ```

## User Authentication

The application uses JWT-based authentication for user login and signup. Passwords are hashed using Argon2, and Redis is used for caching.

### Signup
To sign up, provide a username and password. The password will be hashed and stored securely in the database.

### Login
To log in, provide the correct username and password. A JWT token will be generated and returned, which can be used for authenticated requests.

## Database Setup and CRUD Functions

The application uses SQLite3 as the database. The database is initialized with the necessary tables for storing user information and tasks.

### CRUD Functions
- **Create Task**: Add a new task to the database.
- **Read Task**: Retrieve tasks from the database.
- **Update Task**: Update an existing task in the database.
- **Delete Task**: Soft-delete a task from the database.

## Final Documentation

This section includes any additional notes and final documentation for the project.

### Notes
- The application may refresh when one of the CRUD functions is called. This is a known issue but does not affect the actual functionality.
- Ensure that the Redis server is running for caching to work properly.
