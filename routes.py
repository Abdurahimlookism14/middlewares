from fastapi import APIRouter

router = APIRouter()

@router.post("/register")
async def register(data: dict):
    level = data.get("level", "").lower()
    salary = 0

    if level == "jun":
        salary = 700
    elif level == "middle":
        salary = 1000
    elif level == "senior":
        salary = 2000

    return {"message": "Вы успешно зарегистрированы!", "level": level, "salary": salary}