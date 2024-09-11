import os
import webbrowser
from django.core.management import execute_from_command_line

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'ConsultClient.settings')

def run_server():
    execute_from_command_line(["manage.py", "runserver"])


    if __name__ == "__main__":
        run_server()