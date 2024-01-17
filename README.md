# WAB

### Setting up the Django Backend
1. Clone the project and set up the virtual environment.
2. Install the required dependencies using `pip install -r requirements.txt`.
3. Create client key and secret key for GitHub.
4. Set the keys securely in the `settings.py` file.
5. Run the Django development server using `python manage.py runserver`.

### Running the `index.html` Page
1. Install the Live Server extension in VSCode for a smoother development experience.
2. Go to your GitHub account settings and create an OAuth key.
3. Use a secure homepage URL and callback URL format, such as:  
   `http://127.0.0.1: **{your_live_server_port}**/index.html`
4. Access the provided URL in your browser, ensuring you are logged out of any GitHub accounts.
5. Sign in with GitHub to test your application.

### Note:
- Pay attention to securing sensitive information, especially your client and secret keys.
- CRUD APIs are implemented in the `views.py` file.
