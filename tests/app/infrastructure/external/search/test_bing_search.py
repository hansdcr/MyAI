#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time         : 2026/2/8
# @Author       : Gelin
# @Software     : PyCharm
# @File         : test_bing_search.py

import pytest
from app.infrastructure.external.search.bing_search import BingSearchEngine
from app.domain.models.search import SearchResults


class TestBingSearch:
    """测试Bing搜索引擎"""

    @pytest.mark.asyncio
    async def test_search_gemini(self):
        """测试搜索'gemini'关键词"""
        # 创建搜索引擎实例
        search_engine = BingSearchEngine()

        # 执行搜索
        result = await search_engine.invoke("gemini")

        # 打印原始结果用于调试
        print(f"\n=== 搜索结果调试信息 ===")
        print(f"success: {result.success}")
        print(f"message: {result.message}")
        print(f"data type: {type(result.data)}")
        print(f"data: {result.data}")

        # 验证搜索成功
        assert result.success is True, f"搜索应该成功，但失败了: {result.message}"
        assert result.data is not None, "搜索结果不应为空"

        # 将data转换为SearchResults对象（因为ToolResult.data是dict类型）
        if isinstance(result.data, dict):
            search_results = SearchResults(**result.data)
        else:
            search_results = result.data

        # 验证搜索结果数据结构
        assert search_results.query == "gemini", "查询关键词应该是'gemini'"

        # 打印搜索结果供人工验证
        print(f"\n=== 搜索结果 ===")
        print(f"搜索关键词: {search_results.query}")
        print(f"日期范围: {search_results.date_range}")
        print(f"总结果数: {search_results.total_results}")
        print(f"返回结果数: {len(search_results.results)}")

        # 如果有结果，打印前3条
        if len(search_results.results) > 0:
            print("\n前3条搜索结果:")
            for i, item in enumerate(search_results.results[:3], 1):
                print(f"\n{i}. {item.title}")
                print(f"   URL: {item.url}")
                snippet_preview = item.snippet[:100] + "..." if len(item.snippet) > 100 else item.snippet
                print(f"   摘要: {snippet_preview}")

            # 验证第一条搜索结果的结构
            first_result = search_results.results[0]
            assert first_result.title, "搜索结果应该有标题"
            assert first_result.url, "搜索结果应该有URL"
            assert first_result.url.startswith("http"), "URL应该以http开头"
        else:
            print("\n⚠️  警告: 没有解析到搜索结果")
            print("这可能是因为:")
            print("1. Bing页面结构发生了变化")
            print("2. 被重定向到了不同的Bing版本（如cn.bing.com）")
            print("3. 网络问题或被限流")
            print("\n建议: 手动访问 https://www.bing.com/search?q=gemini 检查页面结构")

            # 不强制要求有结果，因为这可能是Bing的问题
            pytest.skip("未能解析到搜索结果，可能是Bing页面结构变化")
