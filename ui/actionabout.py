def open_about(self):
    file_about = "ABOUT.pdf"
    current_path = os.getcwd()
    file_about = f"{current_path}/../assets/{file_about}"
    webbrowser.open_new(file_about)