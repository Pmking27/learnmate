# LearnMate

LearnMate is a web application created using Django, aimed at providing a platform for users to learn and share educational resources. It allows users to create an account, browse through various educational materials, and interact with other learners through comments and discussions.

## Features

- User registration and authentication system
- User profiles with customizable information
- Browse and search for educational resources
- Upload and share educational materials
- Commenting and discussion system
- User-friendly interface and intuitive navigation

## Installation

To run the LearnMate application locally, follow these steps:

1. Clone the repository:

```
git clone https://github.com/Pmking27/learnmate.git
```

2. Navigate to the project directory:

```
cd learnmate
```

3. Create a virtual environment:

```
python3 -m venv venv
```

4. Activate the virtual environment:

   - For Windows:

   ```
   venv\Scripts\activate
   ```

   - For macOS and Linux:

   ```
   source venv/bin/activate
   ```

5. Install the required dependencies:

```
pip install -r requirements.txt
```

6. Set up the database:

```
python manage.py migrate
```

7. Start the development server:

```
python manage.py runserver
```

8. Open your web browser and navigate to [http://localhost:8000/](http://localhost:8000/) to access the LearnMate application.

## Configuration

LearnMate uses a configuration file `settings.py` to manage various settings. You can modify the settings to suit your requirements.

Some of the important settings include:

- `SECRET_KEY`: The secret key used for securing the application. It is recommended to keep this key secret and not share it publicly.
- `DATABASES`: Configuration related to the database used by the application. You can update this configuration to connect to your preferred database.
- `MEDIA_ROOT`: The directory where user-uploaded files will be stored.
- `EMAIL_BACKEND`: The email backend configuration for sending emails. Update this configuration to use your preferred email service.

## Contributing

Contributions to LearnMate are welcome! If you encounter any issues or have ideas for improvements, please open an issue or submit a pull request on the GitHub repository.

## License

LearnMate is licensed under the [MIT License](LICENSE).

## Acknowledgments

- This project was inspired by the need for a centralized platform for educational resources.
- Special thanks to the Django community for creating a powerful and flexible web framework.
- Thanks to all the contributors who have helped improve LearnMate.

## Contact

If you have any questions, suggestions, or feedback, you can reach out to the project maintainer:

- Project Maintainer: [Prathamesh Mandavkar](mailto:prathamesh2702m@gmail.com)

Please provide detailed information to help with your inquiry or feedback.

---

Thank you for your interest in LearnMate! We hope you find it useful for your educational journey.
```
