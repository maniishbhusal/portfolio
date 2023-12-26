# Portfolio Website
This is a portfolio website project developed using [Django](https://www.djangoproject.com/). 
The website showcases the portfolio of a web developer and includes features such as a home page, about page, portfolio page, blog page, and contact page.

# Features
* **Home Page**: Introduces the developer and highlights their skills and expertise.
* **About Page**: Provides detailed information about the developer's background, experience, and education.
* **Portfolio Page**: Displays a collection of projects the developer has worked on, including project images, descriptions, and links.
* **Blog Page**: Showcases a collection of blog articles written by the developer, including titles, excerpts, and publication dates.
* **Contact Page**: Allows visitors to get in touch with the developer by submitting a contact form.
* **User Authentication**: Users can sign up, log in, and log out. Logged-in users have the ability to post comments on blog articles.

### User Groups
To enhance the user management system, two additional groups have been introduced:
* **Manager Group**: Members of this group have the authority to delete and update any blog articles.
* **Editor Group**: Members of this group can update any blog articles but cannot delete them.

### Individual User Permissions
* **Current Logged-In User**: The user who is currently logged in has the ability to edit or delete their own blog posts.

  ## Installation

1. Clone the repository: `git clone https://github.com/manish-bhusal/portfolio.git`
2. Navigate to the project directory: `cd portfolio`
3. Create a virtual environment: `python3 -m venv env`
4. Activate the virtual environment: `source env/bin/activate`
5. Install the dependencies: `pip install -r requirements.txt`
6. Apply the database migrations: `python manage.py migrate`
7. Start the development server: `python manage.py runserver`


## Contributing

Contributions are welcome! If you find any bugs or have suggestions for improvements, please open an issue or submit a pull request.

## License

This project is licensed under the [MIT License](https://github.com/git/git-scm.com/blob/main/MIT-LICENSE.txt).
