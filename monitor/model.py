# Copyright 2020 Fu Hanxi

# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License iy
# s distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import datetime

from peewee import *

DB = DatabaseProxy()


class BaseModel(Model):
    class Meta:
        database = DB


class User(BaseModel):
    id = AutoField()
    name = CharField(unique=True)

    def __str__(self):
        return f'User <{self.name}>'


class Message(BaseModel):
    user = ForeignKeyField(User, on_delete='CASCADE')
    text = CharField(null=False)
    created_at = DateTimeField(default=datetime.datetime.now(tz=datetime.timezone.utc))

    def __str__(self):
        return f'Message <{self.text}>'


class Record(BaseModel):
    id = AutoField()
    name = CharField(null=False)
    date = DateField(default=datetime.datetime.utcnow().date())
    counter = IntegerField(default=0)

    def __str__(self):
        return f'Record {self.date} <{self.name}> [{self.counter}]'


models = [
    User,
    Message,
    Record,
]


def create_tables():
    with DB.atomic():
        tables_to_create = list(filter(lambda m: not m.table_exists(), models))
        DB.create_tables(tables_to_create)
