#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date     : 2026/01/28
# @Author   : Gelin
# @File     : main.py

from fastapi import FastAPI
from core.config import get_settings


settings = get_settings()
print(settings)


app = FastAPI()

