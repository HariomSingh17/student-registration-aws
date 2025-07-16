import pymysql
import json
import base64
from urllib.parse import parse_qs

def lambda_handler(event, context):
    try:
        # DEBUG: Log full event
        print("Full Event:", json.dumps(event))

        # Step 1: Decode base64 body if needed
        body = event.get('body', '')
        if event.get('isBase64Encoded', False):
            body = base64.b64decode(body).decode('utf-8')

        print("DECODED BODY:", body)

        # Step 2: Parse URL-encoded form data
        data = parse_qs(body)
        print("PARSED DATA:", data)

        # Step 3: Extract form values
        name = data.get('name', [''])[0]
        roll = data.get('roll', [''])[0]
        enroll = data.get('enroll', [''])[0]
        email = data.get('email', [''])[0]
        phone = data.get('phone', [''])[0]

        print(f"Extracted: {name=}, {roll=}, {enroll=}, {email=}, {phone=}")

        # Step 4: MySQL DB connection details
        host = 'first-somwar.cx6wg28ewz01.us-west-1.rds.amazonaws.com'
        user = 'admin'
        password = 'Pankaj0708'

        # Step 5: Create database if it doesn't exist
        server_conn = pymysql.connect(
            host=host,
            user=user,
            password=password,
            database='',
            cursorclass=pymysql.cursors.DictCursor
        )

        with server_conn:
            with server_conn.cursor() as cursor:
                cursor.execute("CREATE DATABASE IF NOT EXISTS studentdb;")
            server_conn.commit()

        # Step 6: Insert into studentdb.students
        db_conn = pymysql.connect(
            host=host,
            user=user,
            password=password,
            database='studentdb',
            cursorclass=pymysql.cursors.DictCursor
        )

        with db_conn:
            with db_conn.cursor() as cursor:
                cursor.execute("""
                    CREATE TABLE IF NOT EXISTS students (
                        id INT AUTO_INCREMENT PRIMARY KEY,
                        name VARCHAR(100) NOT NULL,
                        roll VARCHAR(50) NOT NULL,
                        enroll VARCHAR(50) NOT NULL,
                        email VARCHAR(100) NOT NULL,
                        phone VARCHAR(20) NOT NULL,
                        registered_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
                    );
                """)
                cursor.execute("""
                    INSERT INTO students (name, roll, enroll, email, phone)
                    VALUES (%s, %s, %s, %s, %s);
                """, (name, roll, enroll, email, phone))
            db_conn.commit()

        return {
            'statusCode': 200,
            'headers': {
                'Content-Type': 'application/json',
                'Access-Control-Allow-Origin': '*'
            },
            'body': json.dumps("✅ Registration successful!")
        }

    except Exception as e:
        print("❌ Error:", str(e))
        return {
            'statusCode': 500,
            'headers': {
                'Content-Type': 'application/json',
                'Access-Control-Allow-Origin': '*'
            },
            'body': json.dumps(f"❌ Error: {str(e)}")
        }
