#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date     : 2026/01/28
# @Author   : Gelin
# @File     : status_routes.py

import logging
from fastapi import APIRouter
from app.interfaces.schemas import Response

logger = logging.getLogger(__name__)
router = APIRouter(prefix="/status",tags=["状态模块"])


@router.get(
    path="", # 空代表/status
    response_model=Response,
    summary="系统健康检查",
    description="检查系统postgres redis fastapi等组件的健康信息"
)
async def get_status()->Response:
    """ 检查系统postgres redis fastapi等组件的健康信息 """
    # todo: 等待postgres redis cos等接入后补全代码
    
    return Response.success()
