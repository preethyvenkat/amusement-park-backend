# 🎢 Amusement Park Backend – Ride & Guest Microservices

This project contains two microservices designed to power the backend of an amusement park system: **Ride Service** and **Guest Management Service**.

---

## 📦 Microservices Overview

### 🚀 Ride Service

Manages all ride-related data and operations.

**Features:**
- Create, update, delete ride info
- Check ride status (available, maintenance)
- Track ride queue and wait times

**Endpoints:**
```http
GET    /api/rides              # List all rides
GET    /api/rides/{id}         # Get ride details
POST   /api/rides              # Add a new ride
PUT    /api/rides/{id}         # Update ride
DELETE /api/rides/{id}         # Delete ride
GET    /api/rides/{id}/status  # Get live ride status
POST   /api/rides/{id}/queue   # Add guest to queue
