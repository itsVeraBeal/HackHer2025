# Basic Website with Python Backend

This project is a basic website that utilizes a Python backend with Flask and a frontend built with HTML, CSS, and JavaScript.

## Project Structure

```
basic-website
├── backend
│   ├── app.py
│   └── requirements.txt
├── frontend
│   ├── static
│   │   ├── css
│   │   │   └── styles.css
│   │   ├── js
│   │   │   └── scripts.js
│   └── templates
│       └── index.html
├── .gitignore
└── README.md
```

## Backend Setup

1. Navigate to the `backend` directory. use cd
2. Install the required dependencies listed in `requirements.txt` using pip:
   ```
   pip install -r requirements.txt
   ```
3. Run the application:
   ```
   python app.py
   ```

## Frontend Setup

The frontend files are located in the `frontend` directory. The main HTML file is `index.html`, which can be modified to change the content displayed on the website.

## Usage

Once the backend server is running, you can access the website by navigating to `http://localhost:5000` in your web browser.

## Contributing

Feel free to fork the repository and submit pull requests for any improvements or features you would like to add.

## License

This project is open-source and available under the MIT License.