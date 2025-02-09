# Django CRM System

A robust Customer Relationship Management (CRM) system built with Django, featuring user authentication, record management, and a clean Bootstrap interface.

## Features

- **User Authentication**

  - Secure login and registration
  - Password validation and protection
  - User-specific record management

- **Record Management**

  - Create, read, update, and delete (CRUD) customer records
  - Each record includes contact and address information
  - Records are associated with the creating user
  - Searchable and filterable admin interface

- **User Interface**
  - Clean, responsive Bootstrap design
  - Interactive data tables
  - Flash messages for user feedback
  - Mobile-friendly layout

## Technology Stack

- Python 3.13
- Django
- MySQL
- Bootstrap 5
- Python-dotenv for environment management

## Installation

1. Clone the repository:

## Usage

1. Access the application at `http://localhost:8000`
2. Register a new user account or login with existing credentials
3. Add, view, update, or delete customer records
4. Access the admin interface at `http://localhost:8000/admin`

## Project Structure

- `app_one/`: Main application directory

  - `models.py`: Database models for customer records
  - `views.py`: View functions for handling requests
  - `forms.py`: Form definitions for data input
  - `urls.py`: URL routing configurations

- `templates/`: HTML templates
  - Base template with Bootstrap integration
  - Separate templates for each major function

## Security Features

- CSRF protection
- Password hashing
- User authentication
- Form validation
- Environment variable management

## Database Schema

The main `Record` model includes:

- User association (ForeignKey)
- Contact information (name, email, phone)
- Address details (address, city, state, zipcode)
- Timestamps
- Indexed fields for optimized queries

## Contributing

1. Fork the repository
2. Create a feature branch
3. Commit your changes
4. Push to the branch
5. Create a Pull Request

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Acknowledgments

- Django Framework
- Bootstrap for UI components
- MySQL for database management
