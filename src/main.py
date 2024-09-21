from fastapi import FastAPI
from fastapi.exceptions import RequestValidationError

from src.exceptions.common import CustomException
from src.exceptions.validation import CustomValidationException
from src.middlewares.exception_handlers import (
    custom_exception_handler,
    custom_validation_exception_handler,
    validation_exception_handler,
)
from src.routes.schedule import router as schedule_router
from src.routes.user import router as user_router


app = FastAPI()

# Custom Exception Handler for Validation Errors
app.add_exception_handler(RequestValidationError, validation_exception_handler)
app.add_exception_handler(CustomValidationException, custom_validation_exception_handler)
app.add_exception_handler(CustomException, custom_exception_handler)

# Include the routes
app.include_router(schedule_router)
app.include_router(user_router)
