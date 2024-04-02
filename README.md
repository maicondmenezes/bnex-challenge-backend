# Django REST Framework Backend for Product Management

## Table of Contents

- [About the Project](#about-the-project)
- [Getting Started](#getting-started)
- [Prerequisites](#prerequisites)
- [Installation](#installation)
- [Running the Tests](#running-the-tests)
- [API Usage](#api-usage)
- [Contributing](#contributing)

## About the Project <a name = "about-the-project"></a>

This backend project is developed with Django and Django REST Framework, focusing on managing a "Product" entity. It aims to provide a comprehensive set of APIs for creating, retrieving, updating, and deleting products, each characterized by a name, description, and value. The project follows best practices such as Clean Code, Clean Architecture, Domain-Driven Design (DDD), Test-Driven Development (TDD), design patterns, and Object-Oriented Programming (OOP). It also implements authentication and authorization aligned with RESTful recommendations and OWASP standards.

## Getting Started <a name = "getting-started"></a>

Follow these instructions to set up the project locally for development and testing purposes.

### Prerequisites <a name = "prerequisites"></a>

- Python 3.8 or higher
- Poetry for Python package management

### Installation <a name = "installation"></a>

1. **Clone the Repository**

    ```bash
    git clone https://github.com/maicondmenezes/bnex-challenge-backend.git
    cd bnex-challenge-backend
    ```

2. **Setup Environment**

    Initialize a new Poetry environment and install dependencies.

    ```bash
    poetry install
    ```

3. **Apply Database Migrations**

    Set up your database structure.

    ```bash
    task makemigrations && task migrate
    ```

4. **Create an Admin User (Optional)**

    To access the Django admin interface, create a superuser.

    ```bash
    task createsuperuser
    ```

5. **Run the Development Server**

    Start the Django development server.

    ```bash
    task runserver
    ```

    The API will be available at `http://localhost:8000`.

## Running the Tests <a name = "running-the-tests"></a>

To ensure the reliability and functionality of the API, run the provided test suite:

```bash
task test
```

## API Usage <a name = "api-usage"></a>

- **Create a Product**

  `POST /products/`
  
- **List Products**

  `GET /products/`
  
- **Retrieve a Single Product**

  `GET /products/{product_id}/`
  
- **Update a Product**

  `PUT /products/{product_id}/`
  
- **Partial Update of a Product**

  `PATCH /products/{product_id}/`
  
- **Delete a Product**

  `DELETE /products/{product_id}/`

Refer to the project's API documentation (if available) for detailed information on request and response formats.

## Contributing <a name = "contributing"></a>

Your contributions are always welcome! Please follow these steps to contribute:

1. Fork the project repository.
2. Create a new branch for your feature (`git checkout -b feature/AmazingFeature`).
3. Commit your changes (`git commit -am 'Add some AmazingFeature'`).
4. Push to the branch (`git push origin feature/AmazingFeature`).
5. Open a Pull Request.

---
