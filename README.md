# EventLync - Event Management Platform

A comprehensive event management platform built with Flask (backend) and React (frontend) that enables organizers to create events, sell tickets, and manage check-ins through QR codes.

## 🚀 Live Demo

- **Frontend**: https://eventlync.vercel.app
- **Backend API**: https://eventlync.onrender.com
- **API Documentation**: https://eventlync.onrender.com/api/docs/swagger.json

## 📋 Features

### 👤 User Management
- User registration and authentication
- Role-based access (User, Organizer, Admin)
- JWT token-based security
- Profile management

### 🎪 Event Management
- Create and manage events
- Event search and filtering
- Image uploads (Cloudinary integration)
- Event analytics and statistics

### 🎫 Tickets & Payments
- Multiple ticket types per event
- M-Pesa integration for payments
- Real-time payment status tracking
- Order management and history

### 📱 Check-in System
- QR code generation for tickets
- QR scanner for event check-ins
- Real-time check-in validation
- Check-in history and reporting

## 🏗️ Architecture

### Backend (Flask)
```
backend/
├── app/
│   ├── models/          # SQLAlchemy models
│   ├── routes/          # API endpoints
│   ├── schemas/         # Data validation
│   ├── utils/           # Utilities (M-Pesa, QR, Email)
│   └── config.py        # Configuration
├── migrations/          # Database migrations
└── requirements.txt     # Python dependencies
```

### Frontend (React)
```
frontend/
├── src/
│   ├── components/      # Reusable UI components
│   ├── context/         # React Context (Auth)
│   ├── pages/           # Page components
│   ├── services/        # API services
│   └── styles/          # CSS styles
├── public/              # Static assets
└── package.json         # Node dependencies
```

## 🔧 Tech Stack

### Backend
- **Flask** - Web framework
- **SQLAlchemy** - ORM
- **PostgreSQL** - Database
- **Flask-JWT-Extended** - Authentication
- **Flask-CORS** - Cross-origin requests
- **M-Pesa API** - Payment processing
- **Cloudinary** - Image hosting
- **SendGrid** - Email service

### Frontend
- **React 18** - UI framework
- **React Router** - Navigation
- **Axios** - HTTP client
- **TailwindCSS** - Styling
- **Lucide React** - Icons
- **html5-qrcode** - QR scanning

## 🚀 Quick Start

### Prerequisites
- Node.js 18+
- Python 3.8+
- PostgreSQL
- Git

### Backend Setup

```bash
cd backend

# Create virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Set environment variables
cp .env.example .env
# Edit .env with your credentials

# Initialize database
flask db init
flask db migrate
flask db upgrade

# Run development server
flask run
```

### Frontend Setup

```bash
cd frontend

# Install dependencies
npm install

# Start development server
npm run dev
```

## 🔑 Environment Variables

### Backend (.env)
```bash
# Database
DATABASE_URL=postgresql://...

# Security
SECRET_KEY=your_secret_key
JWT_SECRET_KEY=your_jwt_secret

# M-Pesa (Kenya payments)
MPESA_ENV=sandbox
MPESA_CONSUMER_KEY=your_consumer_key
MPESA_CONSUMER_SECRET=your_consumer_secret
MPESA_SHORT_CODE=your_short_code
MPESA_PASSKEY=your_passkey
MPESA_CALLBACK_URL=https://yourdomain.com/api/payments/mpesa/callback

# Email (SendGrid)
SENDGRID_API_KEY=your_sendgrid_key
MAIL_DEFAULT_SENDER=noreply@yourdomain.com

# Cloudinary (Image uploads)
CLOUDINARY_CLOUD_NAME=your_cloud_name
CLOUDINARY_API_KEY=your_api_key
CLOUDINARY_API_SECRET=your_api_secret

# Frontend
FRONTEND_URL=http://localhost:5173
CORS_ORIGINS=http://localhost:5173
```

## 📡 API Endpoints

### Authentication
```
POST /api/auth/register          # User registration
POST /api/auth/register-organizer # Organizer registration
POST /api/auth/login             # User login
GET  /api/auth/me                # Get current user
```

### Events
```
GET  /api/events                 # List events
POST /api/events                 # Create event
GET  /api/events/{id}            # Get event details
PUT  /api/events/{id}            # Update event
DELETE /api/events/{id}          # Delete event
GET  /api/events/{id}/stats      # Event statistics
```

### Tickets
```
GET  /api/events/{id}/tickets    # Get event tickets
POST /api/events/{id}/tickets    # Create ticket type
```

### Orders & Payments
```
POST /api/orders                 # Create order
GET  /api/orders/user            # User orders
GET  /api/orders/{id}            # Order details
POST /api/payments/mpesa/initiate # Start M-Pesa payment
GET  /api/payments/{id}          # Payment status
POST /api/payments/mpesa/callback # M-Pesa callback
```

### Check-in
```
POST /api/checkin/verify         # Verify QR code
POST /api/checkin/mark           # Mark as checked in
```

## 🧪 Testing

### Run API Tests
```bash
cd backend
python test_mpesa.py  # Test M-Pesa integration
```

### Manual Testing
1. Register as user or organizer
2. Create an event (organizer only)
3. Add ticket types to event
4. Purchase tickets with M-Pesa
5. Use QR codes for check-in

### Test Credentials
- **M-Pesa Sandbox**: Use phone `254708374149`
- **Test Amount**: KES 1 (minimum)

## 🚀 Deployment

### Backend (Render)
1. Connect GitHub repository
2. Set environment variables
3. Deploy automatically on push

### Frontend (Vercel)
1. Connect GitHub repository
2. Set environment variables
3. Deploy automatically on push

## 🤝 Team Tasks

### Developer 1: Authentication & User Management
- Backend auth routes (`auth.py`)
- User management (`users.py`)
- Frontend auth pages and AuthContext
- JWT configuration and security

### Developer 2: Events & Tickets Management
- Event CRUD operations (`events.py`)
- Ticket system (`tickets.py`)
- File uploads and Cloudinary integration
- Event analytics and statistics

### Developer 3: Orders & Payments
- Order processing (`orders.py`)
- M-Pesa integration (`payments.py`, `mpesa.py`)
- QR code generation and check-in system
- Email notifications

## 📞 Support

For questions or issues:
1. Check API documentation
2. Review existing issues
3. Create new issue with details

---

**Happy coding! 🎉**
