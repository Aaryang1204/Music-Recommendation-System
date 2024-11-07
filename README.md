**MUSIC RECOMMENDATION SYSTEM**

This project is a **Music Recommendation System** built using Python and MySQL, designed to provide song recommendations based on user mood and song history. It supports both **admin** and **user roles** with distinct features for each.

### Key Features

#### 1. **Admin Portal**
   - **User Management**: Admin can view user information, delete user profiles, and remove song history.
   - **Song Management**: Admin can add new songs, delete existing ones, and view the entire song library, allowing control over the content available to users.

#### 2. **User Portal**
   - **Signup and Login**: New users can register, and returning users can log in using their ID and password. There is also a "Forgot Password" option where users can reset their password using their name and phone number.
   - **Mood-Based Recommendation**: Users can select a mood (e.g., Happy, Sad, Party, Motivated, Romantic, Calm) to receive song recommendations tailored to that emotion.
   - **Song Library**: Users can select up to five songs from the available library to form a preference history. This history is used for future recommendations.
   - **Personalized Recommendations**: Based on previous song selections, the system recommends songs matching the most common mood in a user’s listening history.
   - **Feedback System**: Users can provide feedback on recommendations, allowing the system to understand user satisfaction.

### Core Functions

- **User ID and Song ID Generation**: Functions to create unique IDs for users and songs.
- **Recommendation Engine**: The system provides song recommendations based on either the user's mood or their listening history.
- **Database Management**: MySQL is used to store and manage user data, song information, and user feedback.

This project provides a foundational recommendation system with a user-friendly interface and robust admin control, combining mood-based suggestions with personalized song history tracking to enhance the user experience.


**PREREQUISITES**

Before running this project, ensure you have the following installed:

Python (version 3.6 or higher)

MySQL Database

Make sure MySQL Server is installed and running. You’ll need a MySQL user with privileges to create databases and tables.
Recommended to use MySQL Workbench or any other MySQL client to manage the database visually.


MySQL Connector for Python

Required to connect Python with MySQL. Install using:
pip install mysql-connector-python
Setup Database and Tables

Create a database named msr (Music Recommendation System).

Create the following tables in the msr database:

user_info: Stores user ID, name, mobile number, and password.
song_data: Stores song information such as song ID, name, artist, and genre.
feedback: Records user feedback.
Example SQL commands to set up tables:

CREATE DATABASE msr;

USE msr;

CREATE TABLE user_info (
    user_id VARCHAR(20) PRIMARY KEY,
    user_name VARCHAR(50),
    user_mob BIGINT,
    user_pass VARCHAR(20)
);

CREATE TABLE song_data (
    song_name VARCHAR(100),
    song_artist VARCHAR(50),
    song_genre VARCHAR(20),
    song_id VARCHAR(20) PRIMARY KEY
);

CREATE TABLE feedback (
    user_id VARCHAR(20),
    feedback CHAR(1)
);
Random Library

The random library is a built-in Python library used for generating unique user and song IDs.
