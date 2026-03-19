import os
import sys
from django.core.wsgi import get_wsgi_application

# Add the project directory to the path so it can find transcriber_project
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "transcriber_project.settings")

app = get_wsgi_application()
application = app
