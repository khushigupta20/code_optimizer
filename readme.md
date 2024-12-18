# **Code Optimizer**

This repository contains a FastAPI-based backend for optimizing Python code. The project provides an API endpoint that accepts unoptimized code as input and returns a more efficient, optimized version of the code. The repository is designed to help developers clean up and improve their code efficiently.

---

## **Features**
- **Code Optimization:** Accepts Python code and returns an optimized version with improved efficiency and readability.
- **FastAPI Framework:** Utilizes the lightweight and high-performance FastAPI framework for the backend.
- **Easy Integration:** Exposes a `/optimize` API endpoint that can be easily consumed using frontend or external tools.
- **Scalable Design:** Modular and extensible for further functionality additions.

---

## **Installation**

Follow these steps to set up the repository locally:

1. **Clone the Repository**:
   ```
   git clone https://github.com/khushigupta20/code_optimizer.git
   cd code_optimizer
   ```
   
2. **Create a Virtual Environment**:
   ```
   python -m venv venv
   source venv/bin/activate       # On Windows: venv\Scripts\activate
   ```

3. **Install Dependencies**:
   ```
   pip install -r requirements.txt
   ```
4. **Add Open API Key to environment variables**:
   Please add it to .env file: 
   ```
   OPENAI_API_KEY=
   ```
   
5. **Run the Application**:
   ```
   uvicorn main:app --reload
   ```

The application will be available at http://127.0.0.1:8000.
