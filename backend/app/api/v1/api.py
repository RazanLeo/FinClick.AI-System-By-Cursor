"""
Main API router for FinClick.AI
"""

from fastapi import APIRouter
from app.api.v1.endpoints import auth, users, financial_analysis, files, admin

api_router = APIRouter()

# Include all endpoint routers
api_router.include_router(auth.router, prefix="/auth", tags=["authentication"])
api_router.include_router(users.router, prefix="/users", tags=["users"])
api_router.include_router(financial_analysis.router, prefix="/analysis", tags=["financial_analysis"])
api_router.include_router(files.router, prefix="/files", tags=["files"])
api_router.include_router(admin.router, prefix="/admin", tags=["admin"])
