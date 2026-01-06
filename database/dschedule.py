from .database import database
import time

sdb = database["dschedule"]

def add_schedule(chat_id: int, msg_id: int, msg_ids: list[int]):
    sdb.insert_one({"chat_id": chat_id, "msg_id": msg_id, "msg_ids": msg_ids, "time": time.time()})

def remove_schedule(chat_id: int, msg_id: int):
    sdb.delete_one({"chat_id": chat_id, "msg_id": msg_id})

def get_all_schedules():
    return sdb.find().to_list()