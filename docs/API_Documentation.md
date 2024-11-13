## Introduction
This document provides an overview of the API endpoints available for the Nexvya App. The API allows users to interact with the application to manage their interests, submit content, and access educational resources.

## Base URL
```
https://api.nexvya.in/v1
```

## Authentication
The API uses **OAuth 2.0** for authentication. To access protected endpoints, users must obtain an access token.

### Authentication Flow
1. **Login**: User sends a POST request to `/auth/login` with their credentials.
2. **Token Retrieval**: On successful login, the server returns an access token.
3. **Token Usage**: Include the access token in the `Authorization` header for subsequent requests.

### Example Request
```
POST /auth/login
Content-Type: application/json

{
  "email": "user@nexvya.in",
  "password": "your_password"
}
```

### Example Response
```json
{
  "access_token": "your_access_token",
  "token_type": "Bearer",
  "expires_in": 3600
}
```

## Endpoints

### 1. User Management

#### Register User
```
POST /users/register
```
**Request Body**
```json
{
  "username": "user123",
  "email": "user@example.com",
  "password": "your_password"
}
```

**Response**
```json
{
  "message": "User registered successfully",
  "user_id": "12345"
}
```

---

#### Get User Profile
```
GET /users/{user_id}
```
**Headers**
```
Authorization: Bearer your_access_token
```

**Response**
```json
{
  "user_id": "12345",
  "username": "user123",
  "email": "user@example.com",
  "interests": ["Machine Learning", "Web Development"]
}
```

### 2. Content Management

#### Submit Content
```
POST /content
```
**Headers**
```
Authorization: Bearer your_access_token
```

**Request Body**
```json
{
  "title": "Introduction to Machine Learning",
  "description": "A brief overview of machine learning concepts.",
  "content_type": "video",
  "url": "https://link-to-your-content.com"
}
```

**Response**
```json
{
  "message": "Content submitted successfully",
  "content_id": "67890"
}
```

---

#### Get Content by Interest
```
GET /content?interest={interest_name}
```

**Response**
```json
[
  {
    "content_id": "67890",
    "title": "Introduction to Machine Learning",
    "description": "A brief overview of machine learning concepts.",
    "url": "https://link-to-your-content.com"
  },
  ...
]
```

### 3. Feedback Management

#### Submit Feedback
```
POST /feedback
```
**Headers**
```
Authorization: Bearer your_access_token
```

**Request Body**
```json
{
  "user_id": "12345",
  "content_id": "67890",
  "feedback": "This content was very informative!"
}
```

**Response**
```json
{
  "message": "Feedback submitted successfully"
}
```

## Error Handling
The API returns standardized error responses to handle common issues.

### Example Error Response
```json
{
  "error": {
    "code": "INVALID_REQUEST",
    "message": "The request parameters are invalid."
  }
}
```

### Common Error Codes
- `400`: Bad Request
- `401`: Unauthorized
- `404`: Not Found
- `500`: Internal Server Error

## Rate Limiting
The API enforces rate limits to ensure fair usage. The limit is set to **100 requests per hour** per user.

## Support
For any questions or issues, please contact support at [**truecare@veritasya.in**](mailto:sonetspprt@gmail.com).

