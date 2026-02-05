#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date     : 2026/01/31
# @Author   : Gelin
# @File     : app_config.py

import logging

logger = logging.getLogger(__name__)

from pydantic import BaseModel, ConfigDict, HttpUrl, Field


class LLMConfig(BaseModel):
    """ 语言模型配置 """
    base_url: HttpUrl = "https://api.deepseek.com"  # 基础URL地址
    api_key: str = ""  # API密钥
    model_name: str = "deepseek-reasoner"  # 推理模型如果传递了tools底层会自动切换deepseek-chat
    temperature: float = Field(default=0.7)  # 温度
    max_tokens: int = Field(8192, ge=0)  # 最大输出token数, 值要大于等于0

class AgentConfig(BaseModel):
    """Agent通用配置"""
    max_iterations: int = Field(default=100,gt=0,lt=1000) #最大迭代次数
    max_retries: int = Field(default=3,gt=1,lt=10) # LLM/工具的最大重试次数
    max_search_results: int = Field(default=10,gt=1,lt=30) #最大搜索结果返回数据条目


class AppConfig(BaseModel):
    """ 应用配置信息，包含Agent配置、LLM提供商、A2A网络、MCP服务配置等"""
    llm_config: LLMConfig  # 语言模型配置
    agent_config: AgentConfig # agent通用配置

    # Pydantic配置，允许传递额外字段初始化
    model_config = ConfigDict(extra="allow")
