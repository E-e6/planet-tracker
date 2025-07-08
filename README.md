# 🌌 Planet Tracker – A FastAPI App for Stargazers

**Planet Tracker** is a lightweight FastAPI-based web application that lets users check which planets are visible from Perth, Australia, at 8 PM local time. It calculates real-time planetary positions using NASA's DE421 ephemeris and Skyfield, and displays sunrise/sunset times using Astral.

---

## 🚀 Features

- 🪐 See which planets (Mercury, Venus, Mars, Jupiter, Saturn) are visible right now
- ☀️ Displays today's sunrise and sunset for Perth, WA
- 🌐 Built with Python, FastAPI, and Skyfield
- 📡 Backend-ready and deployable as a web app (Render, Railway, etc.)

---

## 📸 Demo

> _Coming Soon_ – Add screenshots or a link to a live version here after deployment.

---

## 🧠 How It Works

- Uses `astral` to get sun times
- Uses `skyfield` to calculate planet visibility above the horizon
- FastAPI displays the results at `http://localhost:8000`

---

## 🧪 Installation & Running Locally

1. **Clone the repository**

```bash
git clone https://github.com/YOUR-USERNAME/planet-tracker.git
cd planet-tracker
