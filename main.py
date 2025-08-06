# -----------------------------------------------------------------------------
# AstrBot SunsetWhere Sunset/Sunrise Information Plugin
#
# 文件名: main.py
# 功  能: 从 sunsetbot.top API 获取日出/日落等天文事件信息
# 作  者: [请在此处填写你的名字]
# 版  本: 1.0
# 依  赖: aiohttp (请确保已通过 pip install aiohttp 安装)
# 变更(v1.0):
# -----------------------------------------------------------------------------

import random
from urllib.parse import urlencode

import aiohttp

from astrbot.api import logger
# 导入 AstrBot 核心 API
from astrbot.api.event import filter, AstrMessageEvent
from astrbot.api.star import Context, Star, register


# 使用 @register 装饰器向 AstrBot 核心注册插件
@register("sunset_info", "棒棒糖", "查询日出日落信息的插件", "1.0.1")
class SunsetPlugin(Star):
    """
    一个用于从 sunsetbot.top 获取日出日落等天文事件信息的插件。
    """

    # --- 命令配置中心 ---
    COMMAND_CONFIG = {
        "sunrise": {"event_type": "rise_1", "display_name": "日出"},
        "sunset": {"event_type": "set_1", "display_name": "日落"},
        "sunrise2": {"event_type": "rise_2", "display_name": "明日日出"},
        "sunset2": {"event_type": "set_2", "display_name": "明日日落"},
    }

    def __init__(self, context: Context):
        super().__init__(context)
        self.http_session = aiohttp.ClientSession(trust_env=False)
        logger.info("插件 [sunset_info] 已初始化。")

    async def _query_api(self, city: str,model:str, event_type: str) -> dict:
        """
        内部函数，用于请求 sunsetbot.top API。
        """
        base_url = "https://sunsetbot.top/"
        encoded_city = city
        event_date_param = "None"

        params = {
            "query_id": str(random.randint(100000, 999999)),
            "intend": "select_city",
            "query_city": encoded_city,
            "event_date": event_date_param,
            "event": event_type,
            "times": "None",
            "model": model
        }

        full_url = f"{base_url}?{urlencode(params)}"
        logger.info(f"插件 [sunset_info] 正在访问 URL: {full_url}")

        async with self.http_session.get(base_url, params=params) as response:
            response.raise_for_status()
            return await response.json()

    async def _process_command(self, event: AstrMessageEvent,city: str,model:str, command_name: str):
        """
        一个通用的核心逻辑处理器，被所有具体的命令处理器调用。
        这是一个异步生成器。
        """
        config = self.COMMAND_CONFIG.get(command_name)
        if not config:
            logger.warning(f"收到了一个未配置的命令: {command_name}")
            return

        try:
            data = await self._query_api(city,model, config["event_type"])
            if data.get("status") == "ok":
                city_name = data.get("display_city_name", city)
                display_times_name = data.get("display_times_name")
                display_times_str = data.get("display_times_str")
                event_name = config["display_name"]
                event_time_str = data.get("tb_event_time", "未知时间")
                quality = data.get("tb_quality", "未知")
                aod = data.get("tb_aod", "未知")
                model = data.get("display_model", "未知")
                reply_message = (
                    f"🌇 {city_name} {event_name}预报\n"
                    f"--------------------\n"
                    f"📊 测算场次: {display_times_name} - {display_times_str}\n"
                    f"📅 预计时间: {event_time_str}\n"
                    f"✨ 鲜艳度: {quality}\n"
                    f"🌫 气溶胶: {aod}\n"
                    f"--------------------\n"
                    f"💿模型: {model}\n"
                    f"🌏数据来源：sunsetbot.top"
                )
                yield event.plain_result(reply_message)
            else:
                error_msg = f"API 服务返回错误: {data.get('status', '未知状态')}"
                yield event.plain_result(error_msg + f" (城市: {city})")

        except aiohttp.ClientResponseError as e:
            logger.error(f"插件 [sunset_info] 请求API时服务器返回错误: {e.status} {e.message}")
            yield event.plain_result(f"请求失败，服务器返回错误码：{e.status}")
        except Exception as e:
            logger.error(f"插件 [sunset_info] 处理命令 '{command_name}' 时发生未知错误: {e}", exc_info=True)
            yield event.plain_result("插件处理时发生未知错误，请联系管理员查看后台日志。")

    # --- 独立的命令处理器 ---
    # 每个处理器对应一个命令，然后调用核心逻辑函数

    @filter.command("今天日出")
    async def handle_sunrise(self, event: AstrMessageEvent, city: str):
        # 修正：使用 async for 来迭代并产生异步生成器的结果
        async for result in self._process_command(event,city,"GFS", "sunrise"):
            yield result
        async for result in self._process_command(event,city,"EC", "sunrise"):
            yield result

    @filter.command("今天日落")
    async def handle_sunset(self, event: AstrMessageEvent, city: str):
        async for result in self._process_command(event,city,"GFS", "sunset"):
            yield result
        async for result in self._process_command(event, city,"EC", "sunset"):
            yield result

    @filter.command("明天日出")
    async def handle_sunrise2(self, event: AstrMessageEvent, city: str):
        async for result in self._process_command(event,city,"GFS", "sunrise2"):
            yield result
        async for result in self._process_command(event,city,"EC", "sunrise2"):
            yield result

    @filter.command("明天日落")
    async def handle_sunset2(self, event: AstrMessageEvent, city: str):
        async for result in self._process_command(event,city,"GFS", "sunset2"):
            yield result
        async for result in self._process_command(event,city, "EC", "sunset2"):
            yield result

    async def terminate(self):
        """
        清理函数，用于关闭 aiohttp 客户端会话，释放资源。
        """
        if self.http_session and not self.http_session.closed:
            await self.http_session.close()
            logger.info("插件 [sunset_info] 已终止。")
