from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from dotenv import load_dotenv
import os
from code_optimizer import optimizeCode
from pydantic import BaseModel


# Load environment variables from the .env file
load_dotenv()

# Create a FastAPI application
app = FastAPI()

templates = Jinja2Templates(directory="templates")

# Define a route at the root web address ("/")
@app.get("/")
def read_root(request:Request):
	return templates.TemplateResponse(request=request,name="home.html")



class OptimizeRequest(BaseModel):
    code: str
	
@app.post("/optimize")
def handle_optimize_request(optimizeRequest: OptimizeRequest):
	return optimizeCode(optimizeRequest.code)