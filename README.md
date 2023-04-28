# A project that represents a complete app for online purchase of tickets for a movie session.
## How to run localy:
1. You have to create ```.env``` file in ```cinema_project``` directory to record all the data necessary for application that used in ```settings.py```

2. To use all the features of the application (Payment, sending emails etc.), you need to redefine the EMAIL and STRIPE parameters in the ```settings.py``` file.

3. Аfter all the steps, you can run the command ```docker-compose up -d --build``` and use this application.

 Application will be available at ```localhost:8000```

## Test data will be automatically migrated.
