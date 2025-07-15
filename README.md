# 📌 Student Registration Portal (Serverless on AWS)

A modern, responsive student registration form hosted on Amazon S3, using AWS Lambda and API Gateway to securely store student details into a MySQL database.

![Architecture Diagram](docs/architecture_diagram.png)

## ✨ Features
✅ Responsive and animated HTML registration form  
✅ Serverless architecture with AWS Lambda & API Gateway  
✅ Data stored securely in MySQL database  
✅ Hosted on Amazon S3 for high availability  
✅ Modern UI design with subtle animations

## 🛠 Technologies Used
- **Frontend**: HTML5, CSS3, Google Fonts, subtle animations  
- **Backend**: AWS Lambda (Node.js/Python)  
- **API**: AWS API Gateway (HTTP POST integration)  
- **Database**: Amazon RDS MySQL  
- **Storage**: Amazon S3 (for hosting the form)  
- **Monitoring**: Amazon CloudWatch Logs

## ⚙️ Project Architecture

```text
[HTML Form on S3]
       │
       ▼
[API Gateway (POST)]
       │
       ▼
[AWS Lambda Function]
       │
       ▼
[MySQL Database]
```

## 🚀 Setup & Deployment
(Instructions on creating DB, Lambda, API Gateway, hosting form on S3, etc.)

## 🖼 Screenshots

| Step | Screenshot |
|-----|-------------|
| Database Table | ![DB Screenshot](docs/screenshots/db.png) |
| Hosted Form | ![Form Screenshot](docs/screenshots/form.png) |
| Lambda Function | ![Lambda Screenshot](docs/screenshots/lambda.png) |
| API Gateway | ![API Gateway Screenshot](docs/screenshots/api_gateway.png) |
| S3 Bucket | ![S3 Screenshot](docs/screenshots/s3.png) |

## 🔄 How It Works
1. User submits form → API Gateway → Lambda → DB.

## 🧩 Future Improvements
- Add validation, captcha, email notifications, etc.

## ✍️ Author
- Hariom Singh ([GitHub](https://github.com/HariomSingh17))
