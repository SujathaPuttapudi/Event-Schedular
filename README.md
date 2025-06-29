1.PROJECT TITLE 


# 📅 Event Scheduler Backend using Python & Flask

This is a simple backend project that helps users schedule, view, update, and delete events using REST APIs built with Flask. Events are stored in a local JSON file to maintain persistence.

---

## 🚀 Features

- 📌 Add new events with title, description, start time, and end time
- 📋 View all scheduled events (sorted by start time)
- ✏️ Update an existing event
- ❌ Delete events by ID
- 💾 Save and load data using `events.json`
- 🧪 Basic unit tests with Pytest
- 🔎 (Optional) Search events by title/description
- ⏰ (Optional) Show reminders for events due in the next hour

---

## 🧰 Tech Stack

- **Python 3.11**
- **Flask** (Web framework)
- **JSON** (Data storage)
- **Postman** (API testing)
- **Git & GitHub**

---

## ⚙️ Installation & Setup

### ✅ Step-by-Step Guide

1. **Clone the Repository**  
   git clone https://github.com/SujathaPuttapudi/Event-Schedular.git
   cd Event-Schedular 
2. **Create and Activate Virtual Environment**
    python -m venv venv
    .\venv\Scripts\activate 
3. **Install Required Packages**
    pip install flask
4. **Start the Flask Server**
    python app.py

## 🌐 API ENDPOINTS


| Method | Endpoint       | Description           |
| ------ | -------------- | --------------------- |
| GET    | `/events`      | Get all events        |
| POST   | `/events`      | Add a new event       |
| PUT    | `/events/<id>` | Update an event by ID |
| DELETE | `/events/<id>` | Delete an event by ID |

## 🧪 SAMPLE API REQUEST & RESPONSE
### ➕ Add Event (POST /events)
**Request:**
{
  "title": "Team Meeting",
  "description": "Monthly sync-up",
  "start_time": "2025-06-30 10:00",
  "end_time": "2025-06-30 11:00"
}
**Response:**
{
  "message": "Event added successfully",
  "event_id": 1
}
 
## 📬 Testing with Postman

- Launch Postman
- Use URL: http://127.0.0.1:5000/events
- Choose method (GET, POST, PUT, DELETE)
- Add request body as raw JSON (for POST & PUT)
- Click Send

You can also **export the Postman collection** to submit with your code.


## 🧪 Unit Testing

Unit tests are written using `pytest` to ensure core functionality works as expected.

### ✅ What’s Tested:
- Adding an event
- Deleting an event
- Updating an event
- Listing all events

### 🧪 How to Run:
    pip install pytest
    pytest test_event_manager.py

### The test file is located in:
    test_event_manager.py


## 📂 Folder Structure

Event-Schedular/
├── app.py                 # Flask application entry point
├── event_manager.py       # Core logic for managing events
├── events.json            # JSON file for storing event data
├── requirements.txt       # Dependencies list
├── test_event_manager.py  # Pytest test cases
├── README.md              # Project documentation


## 🧪 Running Tests

1. Install `pytest` if not already installed:
   pip install pytest
2. Run the tests using:
    pytest test_event_manager.py
3. All test cases should pass without errors ✅


## 👤 Developer

- **Name:** Puttapudi Sujatha  
- **Email:** lakshmi26747@gmail.com  
- **Mobile:** 6304926747  
- **GitHub:** [SujathaPuttapudi](https://github.com/SujathaPuttapudi) 

## ✅ Project Status

- ✅ Core Features Implemented
- ✅ API Tested using Postman
- ✅ JSON Persistence Working
- ✅ Unit Tests Passed
- ✅ GitHub Repository Ready
- ✅ Submission Form Ready


## 📎 GitHub Repository

🔗 [https://github.com/SujathaPuttapudi/Event-Schedular](https://github.com/SujathaPuttapudi/Event-Schedular)











