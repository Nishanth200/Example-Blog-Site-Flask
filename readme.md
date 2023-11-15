# Flask Blog

This is a simple Flask blog application that retrieves blog data from an external API and displays it on different pages. The blog content is sourced from [npoint.io](https://npoint.io/6436b195c044c6b335c9).

## Features

- **Home Page:** Displays a list of blog posts retrieved from the API.
- **About Page:** Provides information about the blog or the author.
- **Contact Page:** A simple contact page.
- **Post Page:** Displays a specific blog post based on the post number in the URL.

## Routes

- `/`: Home page displaying a list of blog posts.
- `/about`: About page.
- `/contact`: Contact page.
- `/post/<nb>`: Individual post page based on the post number.

## Dependencies

- [Flask](https://palletsprojects.com/p/flask/)
- [Requests](https://docs.python-requests.org/en/latest/)


## Setup

1. Clone the repository:

   ```bash
   git clone https://github.com/your-username/flask-blog.git
2. Install dependencies:

   ```bash
    pip install Flask requests
3. Run the application:
    ```bash
   python app.py
