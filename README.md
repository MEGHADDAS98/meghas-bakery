# meghas-bakery
Megha's Bakery Management System

Overview

This project is a bakery management system designed to manage inventory, process orders, and handle user authentication. It provides APIs for interacting with various aspects of the bakery's operations, including managing ingredients, bakery items, inventory, orders, and user accounts.

Features
User Authentication: Users can register, log in, and authenticate using  tokens.
Ingredient Management: CRUD operations for managing ingredients used in bakery items.
Bakery Item Management: CRUD operations for managing bakery items, including their description, cost price, selling price, and associated ingredients.
Inventory Management: CRUD operations for managing inventory levels of bakery items.
Order Management: Users can place orders, view their order history, and manage their baskets.
Search Functionality: Users can search for bakery items based on their name or description.
Technologies Used
Django: Python-based web framework for building web applications.
Django REST Framework: Toolkit for building Web APIs using Django.

Installation

1.Clone the repository:

git clone https://github.com/MEGHADDAS98/meghas-bakery.git

2.Install dependencies:

pip install -r requirements.txt

3.Apply database migrations:

python manage.py migrate

4.Run the development server:

python manage.py runserver

Usage
Access the API endpoints using tools like Postman or cURL.
Register a user, obtain  tokens, and use them for authentication.
Use the provided endpoints for managing ingredients, bakery items, inventory, and orders.
