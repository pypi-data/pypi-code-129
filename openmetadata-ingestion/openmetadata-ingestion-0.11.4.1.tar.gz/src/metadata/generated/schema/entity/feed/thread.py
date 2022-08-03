# generated by datamodel-codegen:
#   filename:  schema/entity/feed/thread.json
#   timestamp: 2022-08-03T16:24:31+00:00

from __future__ import annotations

from enum import Enum
from typing import List, Optional

from pydantic import BaseModel, Extra, Field

from ...type import basic, entityReference, reaction


class TaskType(Enum):
    RequestDescription = 'RequestDescription'
    UpdateDescription = 'UpdateDescription'
    RequestTag = 'RequestTag'
    UpdateTag = 'UpdateTag'
    Generic = 'Generic'


class ThreadTaskStatus(Enum):
    Open = 'Open'
    Closed = 'Closed'


class ThreadType(Enum):
    Conversation = 'Conversation'
    Task = 'Task'
    Announcement = 'Announcement'


class TaskDetails(BaseModel):
    class Config:
        extra = Extra.forbid

    id: int = Field(..., description='Unique identifier that identifies the task.')
    type: TaskType
    assignees: entityReference.EntityReferenceList = Field(
        ..., description='List of users or teams the task is assigned to'
    )
    status: Optional[ThreadTaskStatus] = None
    closedBy: Optional[str] = Field(None, description='The user that closed the task.')
    closedAt: Optional[basic.Timestamp] = Field(
        None,
        description='Timestamp when the task was closed in Unix epoch time milliseconds.',
    )
    oldValue: Optional[str] = Field(
        None, description='The value of old object for which the task is created.'
    )
    suggestion: Optional[str] = Field(
        None,
        description='The suggestion object to replace the old value for which the task is created.',
    )
    newValue: Optional[str] = Field(
        None, description='The new value object that was accepted to complete the task.'
    )


class Post(BaseModel):
    class Config:
        extra = Extra.forbid

    id: basic.Uuid = Field(
        ..., description='Unique identifier that identifies the post.'
    )
    message: str = Field(
        ...,
        description='Message in markdown format. See markdown support for more details.',
    )
    postTs: Optional[basic.Timestamp] = Field(
        None, description='Timestamp of the post in Unix epoch time milliseconds.'
    )
    from_: str = Field(
        ..., alias='from', description='Name of the User posting the message.'
    )
    reactions: Optional[reaction.ReactionList] = Field(
        None, description='Reactions for the post.'
    )


class Thread(BaseModel):
    class Config:
        extra = Extra.forbid

    id: basic.Uuid = Field(
        ..., description='Unique identifier that identifies an entity instance.'
    )
    type: Optional[ThreadType] = None
    href: Optional[basic.Href] = Field(
        None, description='Link to the resource corresponding to this entity.'
    )
    threadTs: Optional[basic.Timestamp] = Field(
        None,
        description='Timestamp of the when the first post created the thread in Unix epoch time milliseconds.',
    )
    about: basic.EntityLink = Field(
        ...,
        description='Data asset about which this thread is created for with format <#E::{entities}::{entityName}::{field}::{fieldValue}.',
    )
    entityId: Optional[basic.Uuid] = Field(
        None, description='Entity Id of the entity that the thread belongs to.'
    )
    addressedTo: Optional[basic.EntityLink] = Field(
        None,
        description='User or team this thread is addressed to in format <#E::{entities}::{entityName}::{field}::{fieldValue}.',
    )
    createdBy: Optional[str] = Field(None, description='User who created the thread.')
    updatedAt: Optional[basic.Timestamp] = Field(
        None,
        description='Last update time corresponding to the new version of the entity in Unix epoch time milliseconds.',
    )
    updatedBy: Optional[str] = Field(None, description='User who made the update.')
    resolved: Optional[bool] = Field(
        False, description='When `true` indicates the thread has been resolved.'
    )
    message: str = Field(
        ..., description='The main message of the thread in markdown format.'
    )
    postsCount: Optional[int] = Field(
        0, description='The total count of posts in the thread.'
    )
    posts: Optional[List[Post]] = None
    reactions: Optional[reaction.ReactionList] = Field(
        None, description='Reactions for the thread.'
    )
    task: Optional[TaskDetails] = Field(
        None,
        description='Details about the task. This is only applicable if thread is of type task.',
    )
