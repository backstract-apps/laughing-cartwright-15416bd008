from pydantic import BaseModel,Field,field_validator

import datetime

import uuid

from typing import Any, Dict, List,Optional,Tuple,Union

import re

class Users(BaseModel):
    email: Optional[str]=None
    password_hash: Optional[str]=None
    activity_level: Optional[str]=None
    created_at_dt: Optional[Any]=None


class ReadUsers(BaseModel):
    email: Optional[str]=None
    password_hash: Optional[str]=None
    activity_level: Optional[str]=None
    created_at_dt: Optional[Any]=None
    class Config:
        from_attributes = True


class FoodItems(BaseModel):
    name: Optional[str]=None
    serving_size_g: Optional[float]=None
    calories: Optional[Union[int, float]]=None
    macros_json: Optional[str]=None
    created_at_dt: Optional[Any]=None


class ReadFoodItems(BaseModel):
    name: Optional[str]=None
    serving_size_g: Optional[float]=None
    calories: Optional[Union[int, float]]=None
    macros_json: Optional[str]=None
    created_at_dt: Optional[Any]=None
    class Config:
        from_attributes = True


class Recipes(BaseModel):
    user_id: Optional[Union[int, float]]=None
    title: Optional[str]=None
    total_calories: Optional[Union[int, float]]=None
    macros_json: Optional[str]=None
    created_at_dt: Optional[Any]=None


class ReadRecipes(BaseModel):
    user_id: Optional[Union[int, float]]=None
    title: Optional[str]=None
    total_calories: Optional[Union[int, float]]=None
    macros_json: Optional[str]=None
    created_at_dt: Optional[Any]=None
    class Config:
        from_attributes = True


class LogEntries(BaseModel):
    user_id: Optional[Union[int, float]]=None
    meal_type: Optional[str]=None
    calories_logged: Optional[Union[int, float]]=None
    macros_json: Optional[str]=None
    created_at_dt: Optional[Any]=None


class ReadLogEntries(BaseModel):
    user_id: Optional[Union[int, float]]=None
    meal_type: Optional[str]=None
    calories_logged: Optional[Union[int, float]]=None
    macros_json: Optional[str]=None
    created_at_dt: Optional[Any]=None
    class Config:
        from_attributes = True


class UserMetrics(BaseModel):
    user_id: Optional[Union[int, float]]=None
    metric_type: Optional[str]=None
    metric_value: Optional[float]=None
    log_date_dt: Optional[Any]=None


class ReadUserMetrics(BaseModel):
    user_id: Optional[Union[int, float]]=None
    metric_type: Optional[str]=None
    metric_value: Optional[float]=None
    log_date_dt: Optional[Any]=None
    class Config:
        from_attributes = True




class PostRecipes(BaseModel):
    user_id: Optional[Union[int, float]]=None
    title: Optional[str]=None
    total_calories: Optional[Union[int, float]]=None
    macros_json: Optional[str]=None
    created_at_dt: Optional[str]=None

    class Config:
        from_attributes = True



class PutUsersId(BaseModel):
    id: Union[int, float] = Field(...)
    email: Optional[str]=None
    password_hash: Optional[str]=None
    activity_level: Optional[str]=None
    created_at_dt: Optional[str]=None

    class Config:
        from_attributes = True



class PutUserMetricsId(BaseModel):
    id: Union[int, float] = Field(...)
    user_id: Optional[Union[int, float]]=None
    metric_type: Optional[str]=None
    metric_value: Optional[Any]=None
    log_date_dt: Optional[str]=None

    class Config:
        from_attributes = True



class PostFoodItems(BaseModel):
    name: Optional[str]=None
    serving_size_g: Optional[Any]=None
    calories: Optional[Union[int, float]]=None
    macros_json: Optional[str]=None
    created_at_dt: Optional[str]=None

    class Config:
        from_attributes = True



class PutFoodItemsId(BaseModel):
    id: Union[int, float] = Field(...)
    name: Optional[str]=None
    serving_size_g: Optional[Any]=None
    calories: Optional[Union[int, float]]=None
    macros_json: Optional[str]=None
    created_at_dt: Optional[str]=None

    class Config:
        from_attributes = True



class PostLogEntries(BaseModel):
    user_id: Optional[Union[int, float]]=None
    meal_type: Optional[str]=None
    calories_logged: Optional[Union[int, float]]=None
    macros_json: Optional[str]=None
    created_at_dt: Optional[str]=None

    class Config:
        from_attributes = True



class PutLogEntriesId(BaseModel):
    id: Union[int, float] = Field(...)
    user_id: Optional[Union[int, float]]=None
    meal_type: Optional[str]=None
    calories_logged: Optional[Union[int, float]]=None
    macros_json: Optional[str]=None
    created_at_dt: Optional[str]=None

    class Config:
        from_attributes = True



class PutRecipesId(BaseModel):
    id: Union[int, float] = Field(...)
    user_id: Optional[Union[int, float]]=None
    title: Optional[str]=None
    total_calories: Optional[Union[int, float]]=None
    macros_json: Optional[str]=None
    created_at_dt: Optional[str]=None

    class Config:
        from_attributes = True



class PostUsers(BaseModel):
    email: Optional[str]=None
    password_hash: Optional[str]=None
    activity_level: Optional[str]=None
    created_at_dt: Optional[str]=None

    class Config:
        from_attributes = True



class PostUserMetrics(BaseModel):
    user_id: Optional[Union[int, float]]=None
    metric_type: Optional[str]=None
    metric_value: Optional[Any]=None
    log_date_dt: Optional[str]=None

    class Config:
        from_attributes = True



# Query Parameter Validation Schemas

class DeleteRecipesIdQueryParams(BaseModel):
    """Query parameter validation for delete_recipes_id"""
    id: int = Field(..., ge=1, description="Id")

    class Config:
        populate_by_name = True


class GetUsersIdQueryParams(BaseModel):
    """Query parameter validation for get_users_id"""
    id: int = Field(..., ge=1, description="Id")

    class Config:
        populate_by_name = True


class DeleteUsersIdQueryParams(BaseModel):
    """Query parameter validation for delete_users_id"""
    id: int = Field(..., ge=1, description="Id")

    class Config:
        populate_by_name = True


class GetUserMetricsIdQueryParams(BaseModel):
    """Query parameter validation for get_user_metrics_id"""
    id: int = Field(..., ge=1, description="Id")

    class Config:
        populate_by_name = True


class DeleteLogEntriesIdQueryParams(BaseModel):
    """Query parameter validation for delete_log_entries_id"""
    id: int = Field(..., ge=1, description="Id")

    class Config:
        populate_by_name = True


class DeleteUserMetricsIdQueryParams(BaseModel):
    """Query parameter validation for delete_user_metrics_id"""
    id: int = Field(..., ge=1, description="Id")

    class Config:
        populate_by_name = True


class GetRecipesIdQueryParams(BaseModel):
    """Query parameter validation for get_recipes_id"""
    id: int = Field(..., ge=1, description="Id")

    class Config:
        populate_by_name = True


class GetLogEntriesIdQueryParams(BaseModel):
    """Query parameter validation for get_log_entries_id"""
    id: int = Field(..., ge=1, description="Id")

    class Config:
        populate_by_name = True


class GetFoodItemsIdQueryParams(BaseModel):
    """Query parameter validation for get_food_items_id"""
    id: int = Field(..., ge=1, description="Id")

    class Config:
        populate_by_name = True


class DeleteFoodItemsIdQueryParams(BaseModel):
    """Query parameter validation for delete_food_items_id"""
    id: int = Field(..., ge=1, description="Id")

    class Config:
        populate_by_name = True
