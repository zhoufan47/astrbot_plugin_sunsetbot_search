# <div align="center">🌇SunsetBotSearch</div>

<div align="center"><em>SunsetBot数据查询插件</em></div>

<br>
<div align="center">
  <a href="#-更新日志"><img src="https://img.shields.io/badge/VERSION-v1.0.0-E91E63?style=for-the-badge" alt="Version"></a>
  <a href="https://github.com/GEMILUXVII/astrbot_plugin_jm_cosmos/blob/main/LICENSE"><img src="https://img.shields.io/badge/license-AGPL--3.0-009688?style=for-the-badge" alt="License"></a>
  <a href="https://www.python.org/"><img src="https://img.shields.io/badge/PYTHON-3.10+-3776AB?style=for-the-badge&logo=python&logoColor=white" alt="Python"></a>
  <a href="https://github.com/AstrBotDevs/AstrBot"><img src="https://img.shields.io/badge/AstrBot-Compatible-00BFA5?style=for-the-badge&logo=robot&logoColor=white" alt="AstrBot Compatible"></a>
</div>

<div align="center">
  <a href="https://github.com/botuniverse/onebot-11"><img src="https://img.shields.io/badge/OneBotv11-AIOCQHTTP-FF5722?style=for-the-badge&logo=qq&logoColor=white" alt="OneBot v11 Support"></a>
  <a href="https://github.com/GEMILUXVII/astrbot_plugin_jm_cosmos"><img src="https://img.shields.io/badge/UPDATED-2025.06.01-2196F3?style=for-the-badge" alt="Updated"></a>
</div>

## 📝 介绍

SunsetBotSearch 是一个基于 AstrBot 开发的 sunsetBot数据查询插件，通过sunsetbot.top网站获取相关数据发送至聊天平台

## ✨ 功能特性

### 核心功能

- 查询当日/明日的朝霞晚霞火烧云数据

## 🚀 安装方法

1. **下载插件**: 下载本插件到 AstrBot 的插件目录
2. **安装依赖**: 在终端中执行以下命令:
   ```bash
   pip install -r requirements.txt
   ```
3. **重启 AstrBot**: 确保插件被加载


## 📋 命令列表

### 基础命令

- `/sunrise 地区简称` - 查询该地区的当日日出信息
- `/sunset 地区简称` - 查询该地区的当日日落信息
- `/sunrise2 地区简称` - 查询该地区的明日日出信息
- `/sunset2 地区简称` - 查询该地区的明日日落信息

## 💡 使用示例

### 查询上海市今日日落信息

```
/sunset 上海市
```

### 查询北京市朝阳区明日日出信息

```
/sunrise2 北京-朝阳区
```


## ❓ 常见问题

### 提示：API 服务返回错误: not_found (城市: XX)

**可能原因:**

城市/地区输入错误，或该地区未收录入地区数据库

**解决方法:**
访问https://sunsetbot.top/，在首页的地区查询框中查询实际可用地址

## ⚠️ 注意事项

- 本插件仅供学习交流使用
- 请勿将下载的内容用于商业用途
- 大量请求可能导致 IP 被封禁
- 请遵守当地法律法规

## 📝 更新日志
#### **v1.0.0** (2025-07-28)

- 初始版本发布

## 📜 许可协议

本插件采用 [GNU Affero General Public License v3.0 (AGPL-3.0)](https://www.gnu.org/licenses/agpl-3.0.html) 许可证。

## 🙏 致谢

本项目基于或参考了以下开源项目:

- [AstrBot](https://github.com/Soulter/AstrBot) - 机器人框架

