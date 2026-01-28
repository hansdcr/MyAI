#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date     : 2026/01/28
# @Author   : Gelin
# @File     : main.py

import logging
from fastapi import FastAPI
from core.config import get_settings
from app.infrastructure.logging import setup_logging

# 1、加载配置信息
settings = get_settings()

# 2、初始化日志系统
setup_logging()
logger = logging.getLogger()


logger.info("测试..")

app = FastAPI()

