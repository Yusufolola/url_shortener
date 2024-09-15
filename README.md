
 URL Shortener

Introduction
The URL Shortener web app is designed to convert long, unwieldy URLs into shorter, more manageable versions. This project was built with FastAPI for the backend, PostgreSQL for the database, and deployed on Render. It allows users to generate custom-length shortened URLs and manage them through a user-friendly interface.

- **Deployed Site**: [URL Shortener App](https://url-shortener-4-2owt.onrender.com/)
- **Blog Article**: [Project Overview Blog](#) (Link to your blog post)
- **Author**: [Oyesanmi Yusuf](https://www.linkedin.com/in/oyesanmi-yusuf)

## Installation

### Requirements
- Python 3.8+
- FastAPI
- PostgreSQL
- SQLAlchemy
- Uvicorn
- Pydantic

### Steps to Install Locally

1. **Clone the repository**:
    ```bash
    git clone https://github.com/Yusufolola/url_shortener.git
    cd url_shortener
    ```

2. **Set up a virtual environment**:
    ```bash
    python3 -m venv env
    source env/bin/activate
    ```

3. **Install the dependencies**:
    ```bash
    pip install -r requirements.txt
    ```

4. **Set up PostgreSQL Database**:
    - Install and run PostgreSQL locally.
    - Create a new database, user, and password.
    - Update the `config.py` file with your database URL.

5. **Run the app locally**:
    ```bash
    uvicorn app.main:app --reload
    ```

6. **Access the app**:
    - Open your browser and navigate to `http://127.0.0.1:8000/`.

## Usage
Once the app is running, you can:
1. Generate shortened URLs by inputting the original URL.
2. Manage existing URLs by updating or deleting them via the management interface.
3. Use the shortened URLs to redirect to the original long URLs.

## Contributing
Contributions are welcome! If you have ideas or improvements for the project:
1. Fork the repository.
2. Create a new branch (`git checkout -b feature-branch`).
3. Make your changes.
4. Commit the changes (`git commit -m "Description of changes"`).
5. Push to the branch (`git push origin feature-branch`).
6. Create a pull request.

## Related Projects
If you find this project useful, here are some related projects:
- [FastAPI](https://github.com/tiangolo/fastapi)
- [Uvicorn](https://github.com/encode/uvicorn)
- [SQLAlchemy](https://github.com/sqlalchemy/sqlalchemy)

## License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

This `README.md` covers the essentials for potential users or contributors to understand the project and how to interact with it.
