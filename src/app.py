"""
High School Management System API

A super simple FastAPI application that allows students to view and sign up
for extracurricular activities at Mergington High School.
"""

from fastapi import FastAPI, HTTPException
from fastapi.staticfiles import StaticFiles
from fastapi.responses import RedirectResponse
import os
from pathlib import Path

app = FastAPI(title="Mergington High School API",
              description="API for viewing and signing up for extracurricular activities")

# Mount the static files directory
current_dir = Path(__file__).parent
app.mount("/static", StaticFiles(directory=os.path.join(Path(__file__).parent,
          "static")), name="static")

# In-memory activity database
activities = {
    "Chess Club": {
        "description": "Learn strategies and compete in chess tournaments",
        "schedule": "Fridays, 3:30 PM - 5:00 PM",
        "max_participants": 12,
        "participants": ["michael@mergington.edu", "daniel@mergington.edu"]
    },
    "Programming Class": {
        "description": "Learn programming fundamentals and build software projects",
        "schedule": "Tuesdays and Thursdays, 3:30 PM - 4:30 PM",
        "max_participants": 20,
        "participants": ["emma@mergington.edu", "sophia@mergington.edu"]
    },
    "Gym Class": {
        "description": "Physical education and sports activities",
        "schedule": "Mondays, Wednesdays, Fridays, 2:00 PM - 3:00 PM",
        "max_participants": 30,
        "participants": ["john@mergington.edu", "olivia@mergington.edu"]
    }
}


@app.get("/")
def root():
    return RedirectResponse(url="/static/index.html")


@app.get("/activities")
def get_activities():
    return activities


# Ecuador provinces with capitals and 2026 population estimates
ecuador_provinces = [
    {"province": "Azuay", "capital": "Cuenca", "region": "Sierra", "population_2026": 903421},
    {"province": "Bolívar", "capital": "Guaranda", "region": "Sierra", "population_2026": 211574},
    {"province": "Cañar", "capital": "Azogues", "region": "Sierra", "population_2026": 268955},
    {"province": "Carchi", "capital": "Tulcán", "region": "Sierra", "population_2026": 187122},
    {"province": "Chimborazo", "capital": "Riobamba", "region": "Sierra", "population_2026": 534968},
    {"province": "Cotopaxi", "capital": "Latacunga", "region": "Sierra", "population_2026": 483610},
    {"province": "El Oro", "capital": "Machala", "region": "Costa", "population_2026": 725848},
    {"province": "Esmeraldas", "capital": "Esmeraldas", "region": "Costa", "population_2026": 614322},
    {"province": "Galápagos", "capital": "Puerto Baquerizo Moreno", "region": "Insular", "population_2026": 36270},
    {"province": "Guayas", "capital": "Guayaquil", "region": "Costa", "population_2026": 4228180},
    {"province": "Imbabura", "capital": "Ibarra", "region": "Sierra", "population_2026": 478234},
    {"province": "Loja", "capital": "Loja", "region": "Sierra", "population_2026": 514301},
    {"province": "Los Ríos", "capital": "Babahoyo", "region": "Costa", "population_2026": 878651},
    {"province": "Manabí", "capital": "Portoviejo", "region": "Costa", "population_2026": 1578940},
    {"province": "Morona Santiago", "capital": "Macas", "region": "Amazonia", "population_2026": 193470},
    {"province": "Napo", "capital": "Tena", "region": "Amazonia", "population_2026": 132844},
    {"province": "Orellana", "capital": "Puerto Francisco de Orellana", "region": "Amazonia", "population_2026": 147568},
    {"province": "Pastaza", "capital": "Puyo", "region": "Amazonia", "population_2026": 133905},
    {"province": "Pichincha", "capital": "Quito", "region": "Sierra", "population_2026": 3228450},
    {"province": "Santa Elena", "capital": "Santa Elena", "region": "Costa", "population_2026": 374762},
    {"province": "Santo Domingo de los Tsáchilas", "capital": "Santo Domingo", "region": "Sierra", "population_2026": 495810},
    {"province": "Sucumbíos", "capital": "Nueva Loja", "region": "Amazonia", "population_2026": 218537},
    {"province": "Tungurahua", "capital": "Ambato", "region": "Sierra", "population_2026": 584045},
    {"province": "Zamora Chinchipe", "capital": "Zamora", "region": "Amazonia", "population_2026": 122389},
]


@app.get("/provinces")
def get_provinces():
    """Return Ecuador provinces with capitals and 2026 population estimates"""
    return ecuador_provinces


@app.post("/activities/{activity_name}/signup")
def signup_for_activity(activity_name: str, email: str):
    """Sign up a student for an activity"""
    # Validate activity exists
    if activity_name not in activities:
        raise HTTPException(status_code=404, detail="Activity not found")

    # Get the specific activity
    activity = activities[activity_name]

    # Add student
    activity["participants"].append(email)
    return {"message": f"Signed up {email} for {activity_name}"}
