from database import connect_database
from schedule import organize_lessons, schedule_class
from utils import authenticate_user, send_notification

def main():
    # Establish database connection
    db_connection = connect_database()

    # User authentication
    user = authenticate_user()

    # Organize and schedule classes
    organize_lessons(db_connection, user)
    schedule_class(db_connection, user)

    # Send any necessary notifications
    send_notification(user)

if __name__ == "__main__":
    main()
