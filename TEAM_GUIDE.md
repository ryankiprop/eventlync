# EventLync Team Documentation

## 🎯 Project Overview

**EventLync** is a comprehensive event management platform that allows organizers to create events, sell tickets via M-Pesa, and manage check-ins through QR codes.

## 👥 Team Structure & Tasks

### **👤 Developer 1: Authentication & User Management**
**Role**: Handle user registration, login, JWT tokens, and user management

#### **Backend Tasks** ⏱️ **~8-10 hours**
- **`RegisterResource.post()`** - User registration with email validation (`backend/app/routes/auth.py`)
- **`LoginResource.post()`** - Login with JWT token generation
- **`MeResource.get()`** - Get current user profile
- **`RegisterOrganizerResource.post()`** - Special organizer registration
- **`UsersListResource.get()`** - List all users (admin only) (`backend/app/routes/users.py`)
- **`UserRoleResource.put()`** - Change user roles (admin/organizer/user)
- **User CRUD operations** - Full user management
- **JWT configuration** - `JWT_SECRET_KEY` and token settings in `config.py`
- **Password hashing** - bcrypt integration in `utils/auth.py`
- **User model** - SQLAlchemy model with roles (`backend/app/models/user.py`)

#### **Frontend Tasks** ⏱️ **~6-8 hours**
- **Login/Register pages** - `frontend/src/pages/auth/Login.jsx`, `Register.jsx`
- **Organizer registration** - `frontend/src/pages/auth/RegisterOrganizer.jsx`
- **AuthContext** - `frontend/src/context/AuthContext.jsx`
```javascript
// Key functions to implement:
const login = async (values) => { /* API call + token storage */ }
const register = async (values) => { /* User registration */ }
const registerOrganizer = async (values) => { /* Organizer registration */ }
const logout = () => { /* Clear tokens + redirect */ }
```
- **Protected routes** - Route guards for authenticated pages
- **Role-based access control** - Admin/organizer/user permissions
- **Auth state persistence** - localStorage management
- **User profile page** - Account settings and information

---

### **👤 Developer 2: Events & Tickets Management**
**Role**: Event CRUD, ticket management, file uploads, and event analytics

#### **Backend Tasks** ⏱️ **~10-12 hours**
- **`EventsListResource.get()`** - List events with search/filtering (`backend/app/routes/events.py`)
- **`EventsListResource.post()`** - Create new events
- **`EventResource.get()`** - Get single event details
- **`EventResource.put()`** - Update event information
- **`EventResource.delete()`** - Delete events with cascade cleanup
- **`EventStatsResource.get()`** - Event analytics (tickets sold, revenue)
- **Event search** - Query parameters for filtering
- **Pagination** - `get_pagination_params()` utility
- **Authorization** - Role-based event access control

- **Ticket system** (`backend/app/routes/tickets.py`)
- **`EventTicketsResource.get()`** - List ticket types for event
- **`EventTicketsResource.post()`** - Create new ticket types
- **Ticket availability** - Quantity management and validation
- **Price handling** - Currency and pricing logic

- **File uploads** (`backend/app/routes/uploads.py`)
- **`ImageUploadResource.post()`** - Handle image uploads
- **Cloudinary integration** - `CLOUDINARY_*` variables in `config.py`
- **File validation** - Size, type, and security checks

- **Database models**
- **Event model** - `backend/app/models/event.py`
- **TicketType model** - `backend/app/models/ticket.py`
- **Relationships** - Foreign keys and constraints

#### **Frontend Tasks** ⏱️ **~8-10 hours**
- **Event pages** - `frontend/src/pages/public/Events.jsx`, `EventDetails.jsx`
- **Event creation** - `frontend/src/pages/organizer/CreateEvent.jsx`
- **Event management** - `frontend/src/pages/organizer/EditEvent.jsx`, `MyEvents.jsx`
- **Search & filtering** - Event discovery interface
- **Ticket management** - `frontend/src/components/events/TicketManager.jsx`
- **Ticket selection** - `frontend/src/components/events/TicketSelector.jsx`
- **Image uploads** - File upload components with preview
- **Cloudinary integration** - Frontend API calls
- **Event analytics** - Dashboard with charts and statistics
- **Responsive design** - Mobile-friendly event pages

---

### **👤 Developer 3: Orders & Payments**
**Role**: Order processing, M-Pesa integration, QR codes, and check-in system

#### **Backend Tasks** ⏱️ **~12-15 hours**
- **Order system** (`backend/app/routes/orders.py`)
- **`OrdersResource.post()`** - Create orders (free mode)
- **`UserOrdersResource.get()`** - User's order history
- **`OrderDetailResource.get()`** - Individual order details
- **`EventOrdersResource.get()`** - Organizer's event orders
- **`VerifyCheckinResource.post()`** - QR code verification
- **`MarkCheckinResource.post()`** - Check-in processing
- **Order validation** - Ticket availability and business rules
- **QR code generation** - Unique codes for each ticket
- **Email notifications** - Order confirmations

- **M-Pesa integration** (`backend/app/routes/payments.py`)
- **`MpesaInitiateResource.post()`** - Start M-Pesa payment
- **`PaymentStatusResource.get()`** - Check payment status
- **`MpesaCallbackResource.post()`** - Handle M-Pesa callbacks
- **Payment tracking** - Status updates and error handling

- **M-Pesa utilities** (`backend/app/utils/mpesa.py`)
- **`initiate_stk_push()`** - STK push API calls
- **`get_access_token()`** - Authentication with M-Pesa
- **Password generation** - Timestamp and hash functions
- **Error logging** - Comprehensive debugging info

- **QR system** (`backend/app/utils/qrcode_util.py`)
- **`generate_ticket_qr()`** - QR code creation
- **Unique ID generation** - Secure ticket identifiers
- **QR validation** - Check-in verification logic

- **Email integration** (`backend/app/utils/email.py`)
- **`send_order_confirmation()`** - Email templates
- **SendGrid setup** - API integration and configuration

- **Database models**
- **Order model** - `backend/app/models/order.py`
- **OrderItem model** - Individual ticket purchases
- **Payment model** - Transaction tracking

#### **Frontend Tasks** ⏱️ **~8-10 hours**
- **Payment system** - `frontend/src/services/payments.js`
```javascript
export const initiateMpesa = async (payload) => { /* Start payment */ }
export const getPayment = async (paymentId) => { /* Check status */ }
```
- **Order management** - `frontend/src/pages/user/Orders.jsx`
- **Order confirmation** - Post-purchase pages
- **Payment status** - Real-time polling and updates
- **Phone validation** - Kenya number format checking

- **QR check-in system**
- **QR scanner** - html5-qrcode integration
- **Check-in interface** - Organizer tools
- **Validation feedback** - Success/error messages
- **Check-in history** - Reporting and analytics

- **UI components**
- **Payment forms** - Secure input handling
- **Status indicators** - Loading states and progress
- **Error handling** - User-friendly error messages
- **Responsive design** - Mobile payment experience

---

## 🔗 Integration Points

### **Auth ↔ Events**
- JWT tokens for API authentication
- Role-based permissions (organizer/admin)
- User ownership validation
- Protected routes and API endpoints

### **Events ↔ Orders**
- Event ID validation in orders
- Ticket availability checks
- Price calculations and totals
- Event-specific order constraints

### **Orders ↔ Payments**
- Order creation triggers payment flow
- Payment callbacks update order status
- QR codes link orders to check-in
- Email notifications for completed orders

---

## 🧪 Testing Strategy

### **Unit Tests**
- Individual function/component testing
- Mock external services (M-Pesa, email)
- Validation and error handling

### **Integration Tests**
- End-to-end payment flows
- Event creation → ticket purchase → check-in
- Authentication → authorization checks

### **API Testing**
- Postman/Newman collections
- Automated API tests
- Contract testing between services

### **Manual Testing**
- User registration and login flows
- Event creation and management
- Ticket purchasing with M-Pesa
- QR code check-in process

---

## 🚀 Development Workflow

### **Daily Standups**
- What was completed yesterday
- What will be worked on today
- Any blockers or issues

### **Code Reviews**
- Pull request reviews for all changes
- Cross-team knowledge sharing
- Code quality and consistency

### **Integration Testing**
- Regular integration of all three areas
- End-to-end testing of complete flows
- Performance and security testing

---

## 📈 Success Metrics

### **Functional Requirements**
- ✅ User registration and authentication
- ✅ Event creation and management
- ✅ Ticket purchasing with M-Pesa
- ✅ QR code check-in system
- ✅ Role-based access control

### **Technical Requirements**
- ✅ Secure JWT authentication
- ✅ Real-time payment processing
- ✅ Responsive mobile design
- ✅ Comprehensive error handling
- ✅ Performance optimization

### **Quality Assurance**
- ✅ 90%+ test coverage
- ✅ No critical security vulnerabilities
- ✅ Mobile-responsive design
- ✅ Cross-browser compatibility
- ✅ Accessibility compliance

---

## 🎯 Final Deliverables

1. **Fully functional EventLync platform**
2. **Comprehensive documentation**
3. **Test suites and automation**
4. **Deployment configurations**
5. **User acceptance testing**

## 📞 Communication

- **Daily standups** via [platform]
- **Code reviews** via GitHub
- **Issues and bugs** via GitHub Issues
- **Documentation** via this README

---

**Let's build an amazing event management platform! 🚀**
