# Startup E-commerce Python Website

This is a startup e-commerce website built using Python and Flask. It provides basic e-commerce functionality including product listing, user authentication, and shopping cart management.

## Features

- User registration and authentication
- Product listing and detail views
- Shopping cart functionality
- Basic checkout process

## Tech Stack

- Python 3.8+
- Flask 2.0.1
- SQLAlchemy (Flask-SQLAlchemy 2.5.1)
- Flask-Login 0.5.0
- SQLite database

## Project Structure

```
e-commerce-website/
│
├── app.py
├── models.py
├── routes.py
├── config.py
├── requirements.txt
│
├── templates/
│   ├── base.html
│   ├── index.html
│   ├── login.html
│   ├── register.html
│   ├── product_detail.html
│   └── cart.html
│
└── static/
    └── css/
        └── style.css
```

## Setup and Installation

1. Clone the repository:
   ```
   git clone https://github.com/JohnDev19/Start-up-E-commerce-Python-Website.git
   cd e-commerce-website
   ```

2. Create a virtual environment and activate it:
   ```
   python -m venv venv
   source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
   ```

3. Install the required dependencies:
   ```
   pip install -r requirements.txt
   ```

4. Set up the database:
   ```
   python
   >>> from app import db
   >>> db.create_all()
   >>> exit()
   ```

5. Run the application:
   ```
   python app.py
   ```

6. Open a web browser and navigate to `http://localhost:5000`

## Usage

- Register a new user account
- Browse products on the home page
- Click on a product to view its details
- Add products to your cart
- View and manage your cart

## Contributing

This is a startup project and contributions are welcome. Please feel free to submit a Pull Request.

## License

This project is open source and available under the [MIT License](LICENSE).

