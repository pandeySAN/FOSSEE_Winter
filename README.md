# 🧪 Chemical Equipment Visualizer

A full-stack tool to upload, analyze, and visualize chemical equipment datasets from CSV files. Built using **Django REST Framework**, **React**, and **Chart.js**.

---

## 🚀 Features

### 🔼 CSV Upload

Upload CSV files containing:

```
Equipment, Type, Flowrate, Pressure, Temperature
```

### 📊 Automatic Data Analysis

Backend calculates:

* Total number of equipment
* Average flowrate
* Average pressure
* Average temperature
* Type distribution (Pump, Valve, Reactor, etc.)

### 📈 Visualizations

React frontend displays:

* Summary metrics
* Bar chart showing equipment type distribution

### 📜 History Tracking

* Stores last **5 uploaded datasets**
* View all previous summaries on **History Page**

---

## 🏗️ Tech Stack

### Backend

* Django 5.x
* Django REST Framework
* Pandas
* SQLite

### Frontend

* React.js
* Axios
* Chart.js + react-chartjs-2
* React Router DOM

---

## 📂 Project Structure

```
chemical-equipment-visualizer/
│
├── backend/
│   ├── equipment_api/      # Django project settings
│   ├── api/                # CSV upload + history API
│   └── db.sqlite3
│
└── web-frontend/
    ├── src/
    │   ├── components/
    │   │   ├── UploadCSV.js
    │   │   ├── Summary.js
    │   │   ├── Charts.js
    │   │   └── History.js
    │   └── App.js
```

---

## ⚙️ Backend Setup

### 1️⃣ Create Virtual Environment

```
python -m venv venv
venv\\Scripts\\activate
```

### 2️⃣ Install Dependencies

```
pip install django djangorestframework pandas
```

### 3️⃣ Apply Migrations

```
python manage.py makemigrations
python manage.py migrate
```

### 4️⃣ Run Server

```
python manage.py runserver
```

Backend runs on:

```
http://127.0.0.1:8000
```

---

## 🖥️ Frontend Setup

### 1️⃣ Install Dependencies

```
npm install
```

### 2️⃣ Start React App

```
npm start
```

Frontend runs on:

```
http://localhost:3000
```

---

## 🔌 API Endpoints

### 📤 Upload CSV

`POST /api/upload/`

**Response:**

```json
{
  "total_equipment": 15,
  "average_flowrate": 119.8,
  "average_pressure": 6.10,
  "average_temperature": 117.46,
  "type_distribution": {
    "Pump": 4,
    "Valve": 3,
    "Reactor": 2
  }
}
```

### 📜 Get History

`GET /api/history/`

Returns last 5 uploaded datasets.

---

## 🛢 Database Model

```python
class Dataset(models.Model):
    file_name = models.CharField(max_length=255)
    summary_json = models.TextField()
    uploaded_at = models.DateTimeField(auto_now_add=True)
```

---

## 📎 Sample CSV Format

```
Equipment,Type,Flowrate,Pressure,Temperature
EQ101,Pump,120,5.8,110
EQ102,Valve,100,6.5,115
EQ103,HeatExchanger,140,6.0,119
```

---

## ✔️ Project Status

* Fully working CSV → Summary → Charts pipeline
* History tracking implemented
* Desktop version built with PyQt5 (optional)

---

## 👨‍💻 Author

**Sanchit Pandey**
