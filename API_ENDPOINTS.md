# API Endpoints

Base URL: `/api`

## Auth
- POST `/auth/register`
- POST `/auth/login`
- GET `/auth/me` (JWT)

## Events
- GET `/events` (q, page, per_page)
- POST `/events` (JWT organizer/admin)
- GET `/events/:id`
- PUT `/events/:id` (JWT owner/admin)
- DELETE `/events/:id` (JWT owner/admin)

## Tickets
- GET `/events/:id/tickets`
- POST `/events/:id/tickets` (JWT owner/admin)

## Orders
- POST `/orders` (JWT)
- GET `/orders/user` (JWT)
- GET `/orders/:id` (JWT owner/admin)

## Dashboard
- GET `/dashboard/organizer` (JWT organizer/admin)
- GET `/dashboard/admin` (JWT admin)
