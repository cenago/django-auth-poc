
# Django API with JWT Authentication

A lightweight Django backend featuring user authentication powered by JSON Web Tokens (JWT) using Django REST Framework and Simple JWT.

---

## 🚀 Features
- **Root Endpoint**: Clean greeting endpoint.
- **JWT Token Generation**: Secure user login and token issuance (`access` and `refresh` tokens).
- **Token Refreshing**: Seamless token lifetime extension.
- **Protected Routes**: Secure endpoints guarded by token verification.

---

## 🛠️ Installation & Setup

### 1. Clone & Navigate
```bash
cd your-project-directory

```

2. Install Dependencies
Ensure you have Python installed, then install the required packages:

```bash
pip install django djangorestframework djangorestframework-simplejwt
```

3. Database Migrations & Superuser
Run the migrations and create an admin user to test authentication:
```bash
python manage.py migrate
python manage.py createsuperuser
```
4. Run the Server
Start your local development server:
```bash
python manage.py runserver
```
The server will be available at http://127.0.0.1:8000/.🛣️ 

API EndpointsEndpointMethodDescriptionAuth Required

/   GET 

Home/Index greetingNo

/api/token/ POST 

Submit credentials to receive Access & Refresh tokensNo

/api/token/refresh/ POST


/api/protected/	GET

and run below commands to create the token and test.

below are PowerShell commands.



``` $body = @{ username="admin"; password="admin" } | ConvertTo-Json```

---

```$response = Invoke-RestMethod -Method Post -Uri "http://127.0.0.1:8000/api/token/" -Body $body -ContentType "application/json"```

---

``` Invoke-RestMethod -Method Get -Uri "http://127.0.0.1:8000/api/protected/" -Headers $headers```

'''
---------
