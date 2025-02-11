# Taskify - Full-Stack Task Management Application

Taskify is a full-stack task management application built with **FastAPI (Python)** for the backend, **Next.js (React, TypeScript, Tailwind CSS)** for the frontend, and **PostgreSQL** as the database. It follows **DevSecOps best practices**, including CI/CD pipelines, security scanning, and automated deployments.

---

## 🌟 Features
- ✅ **Task Management** - Create, update, and delete tasks
- 🔒 **Secure Authentication** - JWT-based authentication
- 🚀 **FastAPI Backend** - High-performance API with PostgreSQL
- 🎨 **Next.js Frontend** - Modern UI with Tailwind CSS
- 📡 **WebSockets (Planned)** - Real-time task updates
- 📦 **Node.js Services (Planned)** - Background workers for async processing
- 🛠 **CI/CD Pipeline** - Automated testing and deployments with GitHub Actions
- 🔍 **DevSecOps Security** - OWASP ZAP scanning, Bandit, and ESLint

---

## ⚙️ Tech Stack
| Component  | Technology |
|------------|-------------|
| **Frontend**  | Next.js (React, TypeScript, Tailwind) |
| **Backend**  | FastAPI (Python), SQLAlchemy |
| **Database**  | PostgreSQL |
| **Authentication**  | JWT (Python-Jose) & bcrypt |
| **CI/CD**  | GitHub Actions |
| **Security**  | Bandit, OWASP ZAP, ESLint |
| **Deployment**  | Backend - Fasthosts (VPS), Frontend - Netlify |

---

## 📂 Project Structure
```
Taskify/
│── backend/   # FastAPI Backend
│   ├── src/   # Source code
│   ├── tests/ # Backend tests
│   ├── venv/  # Virtual environment (ignored)
│── frontend/  # Next.js Frontend
│   ├── src/   # Components & pages
│   ├── public/ # Static assets
│── node-services/ # Node.js workers (planned)
│── .github/   # CI/CD Workflows
│── docker/    # Docker configuration
│── README.md  # Project documentation
```

---

## 🚀 Setup Instructions

### **1️⃣ Clone the Repository**
```sh
git clone https://github.com/your-username/Taskify.git
cd Taskify
```

### **2️⃣ Backend Setup**
```sh
cd backend
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
uvicorn main:app --host 127.0.0.1 --port 8000 --reload
```

### **3️⃣ Frontend Setup**
```sh
cd frontend
npm install
npm run dev
```

### **4️⃣ Database Setup**
Ensure PostgreSQL is running and create the database:
```sh
sudo -u postgres psql
CREATE DATABASE taskify;
CREATE USER taskify_user WITH PASSWORD 'password';
GRANT ALL PRIVILEGES ON DATABASE taskify TO taskify_user;
\q
```

### **5️⃣ Deploy Backend on Fasthosts**
```sh
ssh user@your-fasthosts-server-ip
cd Taskify/backend
source venv/bin/activate
uvicorn main:app --host 0.0.0.0 --port 8000 --reload
```

### **6️⃣ Deploy Frontend on Netlify**
1. **Login to Netlify**
2. **Connect GitHub Repo**
3. **Set Environment Variables**
4. **Deploy**

---

## 🛠 Future Improvements
- 🔄 **WebSockets** for real-time task updates
- 📧 **Email Notifications**
- 📱 **Mobile-Friendly UI**
- 🔒 **OAuth2 Authentication (Google, GitHub)**
- 📊 **Task Analytics Dashboard**

---

## 🤝 Contributing
1. **Fork the repository**
2. **Create a new branch** (`feature/your-feature`)
3. **Commit changes** (`git commit -m "Added new feature"`)
4. **Push to GitHub** (`git push origin feature/your-feature`)
5. **Create a Pull Request**

---

## 📝 License
This project is licensed under the **MIT License**.

---

## 💌 Contact
- **GitHub**: [RyanLL02](https://github.com/RyanLL02)
- **Email**: ryanllewellyn02@gmail.com

