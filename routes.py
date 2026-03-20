from fastapi import APIRouter, Request, Depends, HTTPException, UploadFile,Query, Form
from sqlalchemy.orm import Session
from typing import List,Annotated
import service, models, schemas
from fastapi import Query
from database import SessionLocal
from middleware.application_middleware import default_dependency


router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.get('/log_entries/')
async def get_log_entries(request: Request, db: Session = Depends(get_db), protected_deps_1: dict = Depends(default_dependency)):
    try:
        return await service.get_log_entries(request, db)
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(500, str(e))

@router.post('/recipes/')
async def post_recipes(request: Request, raw_data: schemas.PostRecipes, db: Session = Depends(get_db), protected_deps_1: dict = Depends(default_dependency)):
    try:
        return await service.post_recipes(request, db, raw_data)
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(500, str(e))

@router.delete('/recipes/id/')
async def delete_recipes_id(request: Request, query: schemas.DeleteRecipesIdQueryParams = Depends(), db: Session = Depends(get_db), protected_deps_1: dict = Depends(default_dependency)):
    try:
        return await service.delete_recipes_id(request, db, query.id)
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(500, str(e))

@router.get('/users/id/')
async def get_users_id(request: Request, query: schemas.GetUsersIdQueryParams = Depends(), db: Session = Depends(get_db), protected_deps_1: dict = Depends(default_dependency)):
    try:
        return await service.get_users_id(request, db, query.id)
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(500, str(e))

@router.put('/users/id/')
async def put_users_id(request: Request, raw_data: schemas.PutUsersId, db: Session = Depends(get_db), protected_deps_1: dict = Depends(default_dependency)):
    try:
        return await service.put_users_id(request, db, raw_data)
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(500, str(e))

@router.delete('/users/id/')
async def delete_users_id(request: Request, query: schemas.DeleteUsersIdQueryParams = Depends(), db: Session = Depends(get_db), protected_deps_1: dict = Depends(default_dependency)):
    try:
        return await service.delete_users_id(request, db, query.id)
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(500, str(e))

@router.get('/user_metrics/id/')
async def get_user_metrics_id(request: Request, query: schemas.GetUserMetricsIdQueryParams = Depends(), db: Session = Depends(get_db), protected_deps_1: dict = Depends(default_dependency)):
    try:
        return await service.get_user_metrics_id(request, db, query.id)
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(500, str(e))

@router.put('/user_metrics/id/')
async def put_user_metrics_id(request: Request, raw_data: schemas.PutUserMetricsId, db: Session = Depends(get_db), protected_deps_1: dict = Depends(default_dependency)):
    try:
        return await service.put_user_metrics_id(request, db, raw_data)
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(500, str(e))

@router.post('/food_items/')
async def post_food_items(request: Request, raw_data: schemas.PostFoodItems, db: Session = Depends(get_db), protected_deps_1: dict = Depends(default_dependency)):
    try:
        return await service.post_food_items(request, db, raw_data)
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(500, str(e))

@router.put('/food_items/id/')
async def put_food_items_id(request: Request, raw_data: schemas.PutFoodItemsId, db: Session = Depends(get_db), protected_deps_1: dict = Depends(default_dependency)):
    try:
        return await service.put_food_items_id(request, db, raw_data)
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(500, str(e))

@router.post('/log_entries/')
async def post_log_entries(request: Request, raw_data: schemas.PostLogEntries, db: Session = Depends(get_db), protected_deps_1: dict = Depends(default_dependency)):
    try:
        return await service.post_log_entries(request, db, raw_data)
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(500, str(e))

@router.put('/log_entries/id/')
async def put_log_entries_id(request: Request, raw_data: schemas.PutLogEntriesId, db: Session = Depends(get_db), protected_deps_1: dict = Depends(default_dependency)):
    try:
        return await service.put_log_entries_id(request, db, raw_data)
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(500, str(e))

@router.delete('/log_entries/id/')
async def delete_log_entries_id(request: Request, query: schemas.DeleteLogEntriesIdQueryParams = Depends(), db: Session = Depends(get_db), protected_deps_1: dict = Depends(default_dependency)):
    try:
        return await service.delete_log_entries_id(request, db, query.id)
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(500, str(e))

@router.put('/recipes/id/')
async def put_recipes_id(request: Request, raw_data: schemas.PutRecipesId, db: Session = Depends(get_db), protected_deps_1: dict = Depends(default_dependency)):
    try:
        return await service.put_recipes_id(request, db, raw_data)
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(500, str(e))

@router.delete('/user_metrics/id/')
async def delete_user_metrics_id(request: Request, query: schemas.DeleteUserMetricsIdQueryParams = Depends(), db: Session = Depends(get_db), protected_deps_1: dict = Depends(default_dependency)):
    try:
        return await service.delete_user_metrics_id(request, db, query.id)
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(500, str(e))

@router.post('/users/')
async def post_users(request: Request, raw_data: schemas.PostUsers, db: Session = Depends(get_db), protected_deps_1: dict = Depends(default_dependency)):
    try:
        return await service.post_users(request, db, raw_data)
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(500, str(e))

@router.get('/recipes/id/')
async def get_recipes_id(request: Request, query: schemas.GetRecipesIdQueryParams = Depends(), db: Session = Depends(get_db), protected_deps_1: dict = Depends(default_dependency)):
    try:
        return await service.get_recipes_id(request, db, query.id)
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(500, str(e))

@router.get('/recipes/')
async def get_recipes(request: Request, db: Session = Depends(get_db), protected_deps_1: dict = Depends(default_dependency)):
    try:
        return await service.get_recipes(request, db)
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(500, str(e))

@router.get('/users/')
async def get_users(request: Request, db: Session = Depends(get_db), protected_deps_1: dict = Depends(default_dependency)):
    try:
        return await service.get_users(request, db)
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(500, str(e))

@router.get('/user_metrics/')
async def get_user_metrics(request: Request, db: Session = Depends(get_db), protected_deps_1: dict = Depends(default_dependency)):
    try:
        return await service.get_user_metrics(request, db)
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(500, str(e))

@router.get('/food_items/')
async def get_food_items(request: Request, db: Session = Depends(get_db), protected_deps_1: dict = Depends(default_dependency)):
    try:
        return await service.get_food_items(request, db)
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(500, str(e))

@router.get('/log_entries/id/')
async def get_log_entries_id(request: Request, query: schemas.GetLogEntriesIdQueryParams = Depends(), db: Session = Depends(get_db), protected_deps_1: dict = Depends(default_dependency)):
    try:
        return await service.get_log_entries_id(request, db, query.id)
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(500, str(e))

@router.get('/food_items/id/')
async def get_food_items_id(request: Request, query: schemas.GetFoodItemsIdQueryParams = Depends(), db: Session = Depends(get_db), protected_deps_1: dict = Depends(default_dependency)):
    try:
        return await service.get_food_items_id(request, db, query.id)
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(500, str(e))

@router.post('/user_metrics/')
async def post_user_metrics(request: Request, raw_data: schemas.PostUserMetrics, db: Session = Depends(get_db), protected_deps_1: dict = Depends(default_dependency)):
    try:
        return await service.post_user_metrics(request, db, raw_data)
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(500, str(e))

@router.delete('/food_items/id/')
async def delete_food_items_id(request: Request, query: schemas.DeleteFoodItemsIdQueryParams = Depends(), db: Session = Depends(get_db), protected_deps_1: dict = Depends(default_dependency)):
    try:
        return await service.delete_food_items_id(request, db, query.id)
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(500, str(e))

