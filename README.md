Backend Configuration

1. Create virtual environment by running setup.sh in setup in backend folder.
  Command: sh setup.sh

2. Activate the virtualenv created in setup folder.
  Command: source venv/bin/activate

3. Install dependencies by running the below command.
  Command: pip install -r requirements.pip


4. Navigate back to the path where manage.py present and run the below command.
  Command: python manage.py runserver 0.0.0.0:8000

5. Please create the superuser by below command
  Command: python manage.py createsuperuser


Front End Configuration

1. Run npm install to install the dependencies.
  Command: npm Install

2. Run ng serve for running the application.
  Command: ng serve

3. Navigate to frontend/src/app/config.service.ts.

4. Change the backend url if needed.
