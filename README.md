# AbanTether

This is a simple cryptocurrency exchange  


## Features

- Create orders
- Retrieve orders by ID


## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/AliRasoulinejad/abantether.git
   ```
2. Navigate to the project directory:
    ```bash
    cd abantether
   ```
3. Install dependencies:
    ```bash
    poetry install
   ```
4. Run migrations:
    ```bash
    python manage.py migrate
   ```


## Usage
1. Run by command:
    ```bash
   python manage.py runserver
    ```
2. Run by docker-compose:
   ```bash
    make up
    ```
    also you can turn it off by
    ```bash
   make down
    ``` 


## Docs
You can use docs by this link: 
- [swagger](http://localhost:8000/docs/swagger/)
- [redoc](http://localhost:8000/docs/redoc/)


## Testing
Unfortunately, I had no time to write tests, but in future we can run tests by this command:
   ```bash 
   python manage.py test
   ```
