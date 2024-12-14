# IMDB Clone - REST API

This project is a REST API-based IMDB clone, built using **Django** and **Django REST Framework (DRF)**. It mimics core functionalities of IMDB, allowing users to interact with movies, streaming platforms, and reviews, while also providing a secure user authentication system using **Token Authentication**.

---

## Features

### 1. **Streaming Platforms**
- **View All Platforms**: Retrieve a list of all available streaming platforms.
- **Detailed Platform View**: Fetch detailed information about a specific platform by its ID.

   **Endpoints**:
   - `GET /stream/` - List all streaming platforms.
   - `GET /stream/<int:pk>/` - Get details of a specific platform.

---

### 2. **Watchlist**
- **View Watchlist**: Access all movies and shows available in the watchlist.
- **Detailed Movie/Show View**: Fetch details for a specific movie or show.

   **Endpoints**:
   - `GET /list/` - List all movies/shows in the watchlist.
   - `GET /<int:pk>/` - View details of a specific movie/show.

---

### 3. **Reviews**
- **Create Reviews**: Add a new review for a movie/show.
- **View All Reviews**: Fetch all reviews for a specific movie/show.
- **Detailed Review**: Access detailed information about a specific review.

   **Endpoints**:
   - `POST /<int:pk>/review-create/` - Create a new review for a movie/show.
   - `GET /<int:pk>/review/` - List all reviews for a specific movie/show.
   - `GET /review/<int:pk>/` - Retrieve a specific review.

---

### 4. **User Authentication (Token-Based)**
- **Login**: Authenticate users and generate a token for secure access.
- **Register**: Create a new user account.
- **Logout**: Invalidate the user token to log out securely.

   **Endpoints**:
   - `POST /account/login/` - Log in and obtain an authentication token.
   - `POST /account/register/` - Register a new user.
   - `POST /account/logout/` - Log out and invalidate the token.

---

## Project Structure

### **Main Project (`urls.py`)**
- `admin/` - Admin panel for managing database models.
- `movie/` - Includes all URLs related to movies and watchlists (`movie_list` app).
- `account/` - Includes user-related operations (`user_app`).

### **Apps**
- **movie_list** - Handles watchlists, streaming platforms, and reviews.
- **user_app** - Manages user accounts, authentication, and permissions.

---

## Authentication

This project uses **Token-Based Authentication** powered by Django REST Framework. Each user receives a unique token upon login, which is required for accessing secure API endpoints. Tokens ensure that all user actions are authenticated and authorized.

---

## Overview

This project is a scalable backend solution for building an IMDB-like system, providing a robust and secure API for integration with frontend applications.
