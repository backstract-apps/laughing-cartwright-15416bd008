from sqlalchemy.orm import Session, aliased
from database import SessionLocal
from sqlalchemy import and_, or_
from typing import *
from fastapi import Request, UploadFile, HTTPException, status
import models, schemas
import boto3
import jwt
from datetime import datetime
import requests
import math
import random
import asyncio
from pathlib import Path


def convert_to_datetime(date_string):
    if date_string is None:
        return datetime.now()
    if not date_string.strip():
        return datetime.now()
    if "T" in date_string:
        try:
            return datetime.fromisoformat(date_string.replace("Z", "+00:00"))
        except ValueError:
            date_part = date_string.split("T")[0]
            try:
                return datetime.strptime(date_part, "%Y-%m-%d")
            except ValueError:
                return datetime.now()
    else:
        # Try to determine format based on first segment
        parts = date_string.split("-")
        if len(parts[0]) == 4:
            # Likely YYYY-MM-DD format
            try:
                return datetime.strptime(date_string, "%Y-%m-%d")
            except ValueError:
                return datetime.now()

        # Try DD-MM-YYYY format
        try:
            return datetime.strptime(date_string, "%d-%m-%Y")
        except ValueError:
            return datetime.now()

        # Fallback: try YYYY-MM-DD if not already tried
        if len(parts[0]) != 4:
            try:
                return datetime.strptime(date_string, "%Y-%m-%d")
            except ValueError:
                return datetime.now()

        return datetime.now()


async def get_log_entries(request: Request, db: Session):

    query = db.query(models.LogEntries)

    log_entries_all = query.all()
    log_entries_all = (
        [new_data.to_dict() for new_data in log_entries_all]
        if log_entries_all
        else log_entries_all
    )

    res = {
        "status": 200,
        "message": "This is the default message.",
        "data": {"log_entries_all": log_entries_all},
    }
    return res


async def post_recipes(
    request: Request,
    db: Session,
    raw_data: schemas.PostRecipes,
):
    user_id: Union[int, float] = raw_data.user_id
    title: str = raw_data.title
    total_calories: Union[int, float] = raw_data.total_calories
    macros_json: str = raw_data.macros_json
    created_at_dt: str = convert_to_datetime(raw_data.created_at_dt)

    record_to_be_added = {
        "title": title,
        "user_id": user_id,
        "macros_json": macros_json,
        "created_at_dt": created_at_dt,
        "total_calories": total_calories,
    }
    new_recipes = models.Recipes(**record_to_be_added)
    db.add(new_recipes)
    db.commit()
    # db.refresh(new_recipes)
    recipes_inserted_record = new_recipes.to_dict()

    res = {
        "status": 200,
        "message": "This is the default message.",
        "data": {"recipes_inserted_record": recipes_inserted_record},
    }
    return res


async def delete_recipes_id(request: Request, db: Session, id: Union[int, float]):

    query = db.query(models.Recipes)
    query = query.filter(and_(models.Recipes.id == id))

    record_to_delete = query.first()
    if record_to_delete:
        db.delete(record_to_delete)
        db.commit()
        recipes_deleted = record_to_delete.to_dict()
    else:
        recipes_deleted = record_to_delete

    res = {
        "status": 200,
        "message": "This is the default message.",
        "data": {"recipes_deleted": recipes_deleted},
    }
    return res


async def get_users_id(request: Request, db: Session, id: Union[int, float]):

    query = db.query(models.Users)
    query = query.filter(and_(models.Users.id == id))

    users_one = query.first()

    users_one = (
        (users_one.to_dict() if hasattr(users_one, "to_dict") else vars(users_one))
        if users_one
        else users_one
    )

    res = {
        "status": 200,
        "message": "This is the default message.",
        "data": {"users_one": users_one},
    }
    return res


async def put_users_id(
    request: Request,
    db: Session,
    raw_data: schemas.PutUsersId,
):
    id: Union[int, float] = raw_data.id
    email: str = raw_data.email
    password_hash: str = raw_data.password_hash
    activity_level: str = raw_data.activity_level
    created_at_dt: str = convert_to_datetime(raw_data.created_at_dt)

    query = db.query(models.Users)
    query = query.filter(and_(models.Users.id == id))
    users_edited_record = query.first()

    if users_edited_record:
        for key, value in {
            "id": id,
            "email": email,
            "created_at_dt": created_at_dt,
            "password_hash": password_hash,
            "activity_level": activity_level,
        }.items():
            setattr(users_edited_record, key, value)

        db.commit()

        # db.refresh(users_edited_record)

        users_edited_record = (
            users_edited_record.to_dict()
            if hasattr(users_edited_record, "to_dict")
            else vars(users_edited_record)
        )

    res = {
        "status": 200,
        "message": "This is the default message.",
        "data": {"users_edited_record": users_edited_record},
    }
    return res


async def delete_users_id(request: Request, db: Session, id: Union[int, float]):

    query = db.query(models.Users)
    query = query.filter(and_(models.Users.id == id))

    record_to_delete = query.first()
    if record_to_delete:
        db.delete(record_to_delete)
        db.commit()
        users_deleted = record_to_delete.to_dict()
    else:
        users_deleted = record_to_delete

    res = {
        "status": 200,
        "message": "This is the default message.",
        "data": {"users_deleted": users_deleted},
    }
    return res


async def get_user_metrics_id(request: Request, db: Session, id: Union[int, float]):

    query = db.query(models.UserMetrics)
    query = query.filter(and_(models.UserMetrics.id == id))

    user_metrics_one = query.first()

    user_metrics_one = (
        (
            user_metrics_one.to_dict()
            if hasattr(user_metrics_one, "to_dict")
            else vars(user_metrics_one)
        )
        if user_metrics_one
        else user_metrics_one
    )

    res = {
        "status": 200,
        "message": "This is the default message.",
        "data": {"user_metrics_one": user_metrics_one},
    }
    return res


async def put_user_metrics_id(
    request: Request,
    db: Session,
    raw_data: schemas.PutUserMetricsId,
):
    id: Union[int, float] = raw_data.id
    user_id: Union[int, float] = raw_data.user_id
    metric_type: str = raw_data.metric_type
    metric_value: float = raw_data.metric_value
    log_date_dt: str = convert_to_datetime(raw_data.log_date_dt)

    query = db.query(models.UserMetrics)
    query = query.filter(and_(models.UserMetrics.id == id))
    user_metrics_edited_record = query.first()

    if user_metrics_edited_record:
        for key, value in {
            "id": id,
            "user_id": user_id,
            "log_date_dt": log_date_dt,
            "metric_type": metric_type,
            "metric_value": metric_value,
        }.items():
            setattr(user_metrics_edited_record, key, value)

        db.commit()

        # db.refresh(user_metrics_edited_record)

        user_metrics_edited_record = (
            user_metrics_edited_record.to_dict()
            if hasattr(user_metrics_edited_record, "to_dict")
            else vars(user_metrics_edited_record)
        )

    res = {
        "status": 200,
        "message": "This is the default message.",
        "data": {"user_metrics_edited_record": user_metrics_edited_record},
    }
    return res


async def post_food_items(
    request: Request,
    db: Session,
    raw_data: schemas.PostFoodItems,
):
    name: str = raw_data.name
    serving_size_g: float = raw_data.serving_size_g
    calories: Union[int, float] = raw_data.calories
    macros_json: str = raw_data.macros_json
    created_at_dt: str = convert_to_datetime(raw_data.created_at_dt)

    record_to_be_added = {
        "name": name,
        "calories": calories,
        "macros_json": macros_json,
        "created_at_dt": created_at_dt,
        "serving_size_g": serving_size_g,
    }
    new_food_items = models.FoodItems(**record_to_be_added)
    db.add(new_food_items)
    db.commit()
    # db.refresh(new_food_items)
    food_items_inserted_record = new_food_items.to_dict()

    res = {
        "status": 200,
        "message": "This is the default message.",
        "data": {"food_items_inserted_record": food_items_inserted_record},
    }
    return res


async def put_food_items_id(
    request: Request,
    db: Session,
    raw_data: schemas.PutFoodItemsId,
):
    id: Union[int, float] = raw_data.id
    name: str = raw_data.name
    serving_size_g: float = raw_data.serving_size_g
    calories: Union[int, float] = raw_data.calories
    macros_json: str = raw_data.macros_json
    created_at_dt: str = convert_to_datetime(raw_data.created_at_dt)

    query = db.query(models.FoodItems)
    query = query.filter(and_(models.FoodItems.id == id))
    food_items_edited_record = query.first()

    if food_items_edited_record:
        for key, value in {
            "id": id,
            "name": name,
            "calories": calories,
            "macros_json": macros_json,
            "created_at_dt": created_at_dt,
            "serving_size_g": serving_size_g,
        }.items():
            setattr(food_items_edited_record, key, value)

        db.commit()

        # db.refresh(food_items_edited_record)

        food_items_edited_record = (
            food_items_edited_record.to_dict()
            if hasattr(food_items_edited_record, "to_dict")
            else vars(food_items_edited_record)
        )

    res = {
        "status": 200,
        "message": "This is the default message.",
        "data": {"food_items_edited_record": food_items_edited_record},
    }
    return res


async def post_log_entries(
    request: Request,
    db: Session,
    raw_data: schemas.PostLogEntries,
):
    user_id: Union[int, float] = raw_data.user_id
    meal_type: str = raw_data.meal_type
    calories_logged: Union[int, float] = raw_data.calories_logged
    macros_json: str = raw_data.macros_json
    created_at_dt: str = convert_to_datetime(raw_data.created_at_dt)

    record_to_be_added = {
        "user_id": user_id,
        "meal_type": meal_type,
        "macros_json": macros_json,
        "created_at_dt": created_at_dt,
        "calories_logged": calories_logged,
    }
    new_log_entries = models.LogEntries(**record_to_be_added)
    db.add(new_log_entries)
    db.commit()
    # db.refresh(new_log_entries)
    log_entries_inserted_record = new_log_entries.to_dict()

    res = {
        "status": 200,
        "message": "This is the default message.",
        "data": {"log_entries_inserted_record": log_entries_inserted_record},
    }
    return res


async def put_log_entries_id(
    request: Request,
    db: Session,
    raw_data: schemas.PutLogEntriesId,
):
    id: Union[int, float] = raw_data.id
    user_id: Union[int, float] = raw_data.user_id
    meal_type: str = raw_data.meal_type
    calories_logged: Union[int, float] = raw_data.calories_logged
    macros_json: str = raw_data.macros_json
    created_at_dt: str = convert_to_datetime(raw_data.created_at_dt)

    query = db.query(models.LogEntries)
    query = query.filter(and_(models.LogEntries.id == id))
    log_entries_edited_record = query.first()

    if log_entries_edited_record:
        for key, value in {
            "id": id,
            "user_id": user_id,
            "meal_type": meal_type,
            "macros_json": macros_json,
            "created_at_dt": created_at_dt,
            "calories_logged": calories_logged,
        }.items():
            setattr(log_entries_edited_record, key, value)

        db.commit()

        # db.refresh(log_entries_edited_record)

        log_entries_edited_record = (
            log_entries_edited_record.to_dict()
            if hasattr(log_entries_edited_record, "to_dict")
            else vars(log_entries_edited_record)
        )

    res = {
        "status": 200,
        "message": "This is the default message.",
        "data": {"log_entries_edited_record": log_entries_edited_record},
    }
    return res


async def delete_log_entries_id(request: Request, db: Session, id: Union[int, float]):

    query = db.query(models.LogEntries)
    query = query.filter(and_(models.LogEntries.id == id))

    record_to_delete = query.first()
    if record_to_delete:
        db.delete(record_to_delete)
        db.commit()
        log_entries_deleted = record_to_delete.to_dict()
    else:
        log_entries_deleted = record_to_delete

    res = {
        "status": 200,
        "message": "This is the default message.",
        "data": {"log_entries_deleted": log_entries_deleted},
    }
    return res


async def put_recipes_id(
    request: Request,
    db: Session,
    raw_data: schemas.PutRecipesId,
):
    id: Union[int, float] = raw_data.id
    user_id: Union[int, float] = raw_data.user_id
    title: str = raw_data.title
    total_calories: Union[int, float] = raw_data.total_calories
    macros_json: str = raw_data.macros_json
    created_at_dt: str = convert_to_datetime(raw_data.created_at_dt)

    query = db.query(models.Recipes)
    query = query.filter(and_(models.Recipes.id == id))
    recipes_edited_record = query.first()

    if recipes_edited_record:
        for key, value in {
            "id": id,
            "title": title,
            "user_id": user_id,
            "macros_json": macros_json,
            "created_at_dt": created_at_dt,
            "total_calories": total_calories,
        }.items():
            setattr(recipes_edited_record, key, value)

        db.commit()

        # db.refresh(recipes_edited_record)

        recipes_edited_record = (
            recipes_edited_record.to_dict()
            if hasattr(recipes_edited_record, "to_dict")
            else vars(recipes_edited_record)
        )

    res = {
        "status": 200,
        "message": "This is the default message.",
        "data": {"recipes_edited_record": recipes_edited_record},
    }
    return res


async def delete_user_metrics_id(request: Request, db: Session, id: Union[int, float]):

    query = db.query(models.UserMetrics)
    query = query.filter(and_(models.UserMetrics.id == id))

    record_to_delete = query.first()
    if record_to_delete:
        db.delete(record_to_delete)
        db.commit()
        user_metrics_deleted = record_to_delete.to_dict()
    else:
        user_metrics_deleted = record_to_delete

    res = {
        "status": 200,
        "message": "This is the default message.",
        "data": {"user_metrics_deleted": user_metrics_deleted},
    }
    return res


async def post_users(
    request: Request,
    db: Session,
    raw_data: schemas.PostUsers,
):
    email: str = raw_data.email
    password_hash: str = raw_data.password_hash
    activity_level: str = raw_data.activity_level
    created_at_dt: str = convert_to_datetime(raw_data.created_at_dt)

    record_to_be_added = {
        "email": email,
        "created_at_dt": created_at_dt,
        "password_hash": password_hash,
        "activity_level": activity_level,
    }
    new_users = models.Users(**record_to_be_added)
    db.add(new_users)
    db.commit()
    # db.refresh(new_users)
    users_inserted_record = new_users.to_dict()

    res = {
        "status": 200,
        "message": "This is the default message.",
        "data": {"users_inserted_record": users_inserted_record},
    }
    return res


async def get_recipes_id(request: Request, db: Session, id: Union[int, float]):

    query = db.query(models.Recipes)
    query = query.filter(and_(models.Recipes.id == id))

    recipes_one = query.first()

    recipes_one = (
        (
            recipes_one.to_dict()
            if hasattr(recipes_one, "to_dict")
            else vars(recipes_one)
        )
        if recipes_one
        else recipes_one
    )

    res = {
        "status": 200,
        "message": "This is the default message.",
        "data": {"recipes_one": recipes_one},
    }
    return res


async def get_recipes(request: Request, db: Session):

    query = db.query(models.Recipes)

    recipes_all = query.all()
    recipes_all = (
        [new_data.to_dict() for new_data in recipes_all] if recipes_all else recipes_all
    )

    res = {
        "status": 200,
        "message": "This is the default message.",
        "data": {"recipes_all": recipes_all},
    }
    return res


async def get_users(request: Request, db: Session):

    query = db.query(models.Users)

    users_all = query.all()
    users_all = (
        [new_data.to_dict() for new_data in users_all] if users_all else users_all
    )

    res = {
        "status": 200,
        "message": "This is the default message.",
        "data": {"users_all": users_all},
    }
    return res


async def get_user_metrics(request: Request, db: Session):

    query = db.query(models.UserMetrics)

    user_metrics_all = query.all()
    user_metrics_all = (
        [new_data.to_dict() for new_data in user_metrics_all]
        if user_metrics_all
        else user_metrics_all
    )

    res = {
        "status": 200,
        "message": "This is the default message.",
        "data": {"user_metrics_all": user_metrics_all},
    }
    return res


async def get_food_items(request: Request, db: Session):

    query = db.query(models.FoodItems)

    food_items_all = query.all()
    food_items_all = (
        [new_data.to_dict() for new_data in food_items_all]
        if food_items_all
        else food_items_all
    )

    res = {
        "status": 200,
        "message": "This is the default message.",
        "data": {"food_items_all": food_items_all},
    }
    return res


async def get_log_entries_id(request: Request, db: Session, id: Union[int, float]):

    query = db.query(models.LogEntries)
    query = query.filter(and_(models.LogEntries.id == id))

    log_entries_one = query.first()

    log_entries_one = (
        (
            log_entries_one.to_dict()
            if hasattr(log_entries_one, "to_dict")
            else vars(log_entries_one)
        )
        if log_entries_one
        else log_entries_one
    )

    res = {
        "status": 200,
        "message": "This is the default message.",
        "data": {"log_entries_one": log_entries_one},
    }
    return res


async def get_food_items_id(request: Request, db: Session, id: Union[int, float]):

    query = db.query(models.FoodItems)
    query = query.filter(and_(models.FoodItems.id == id))

    food_items_one = query.first()

    food_items_one = (
        (
            food_items_one.to_dict()
            if hasattr(food_items_one, "to_dict")
            else vars(food_items_one)
        )
        if food_items_one
        else food_items_one
    )

    res = {
        "status": 200,
        "message": "This is the default message.",
        "data": {"food_items_one": food_items_one},
    }
    return res


async def post_user_metrics(
    request: Request,
    db: Session,
    raw_data: schemas.PostUserMetrics,
):
    user_id: Union[int, float] = raw_data.user_id
    metric_type: str = raw_data.metric_type
    metric_value: float = raw_data.metric_value
    log_date_dt: str = convert_to_datetime(raw_data.log_date_dt)

    record_to_be_added = {
        "user_id": user_id,
        "log_date_dt": log_date_dt,
        "metric_type": metric_type,
        "metric_value": metric_value,
    }
    new_user_metrics = models.UserMetrics(**record_to_be_added)
    db.add(new_user_metrics)
    db.commit()
    # db.refresh(new_user_metrics)
    user_metrics_inserted_record = new_user_metrics.to_dict()

    res = {
        "status": 200,
        "message": "This is the default message.",
        "data": {"user_metrics_inserted_record": user_metrics_inserted_record},
    }
    return res


async def delete_food_items_id(request: Request, db: Session, id: Union[int, float]):

    query = db.query(models.FoodItems)
    query = query.filter(and_(models.FoodItems.id == id))

    record_to_delete = query.first()
    if record_to_delete:
        db.delete(record_to_delete)
        db.commit()
        food_items_deleted = record_to_delete.to_dict()
    else:
        food_items_deleted = record_to_delete

    res = {
        "status": 200,
        "message": "This is the default message.",
        "data": {"food_items_deleted": food_items_deleted},
    }
    return res
