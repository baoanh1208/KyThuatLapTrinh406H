def open_help(self):
    file_help = "HELP.pdf"
    current_path = os.getcwd()
    file_help = f"{current_path}/../assets/{file_help}"
    webbrowser.open_new(file_help)