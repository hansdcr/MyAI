#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time         :   2026/2/4
# @Author       :   Gelin
# @Software     :   PyCharm
# @File         :   tool_result.py
from typing import Optional,TypeVar, Generic

from pydantic import BaseModel

T = TypeVar("T")

class ToolResult(BaseModel,Generic[T]):
    """工具结果Domain模型"""

    success: bool = True # 是否成功调用
    message: Optional[str] = "" # 额外的信息提示
    data: Optional[dict] = None # 工具的执行结果/数据

