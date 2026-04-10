# Hermes Agent 中文安装向导

![中文界面](https://img.shields.io/badge/界面-中文-blue)
![一键安装](https://img.shields.io/badge/安装-一键-green)
![中文文档](https://img.shields.io/badge/文档-中文-orange)

## 🎯 项目简介

这是一个为 **中文用户** 专门优化的 Hermes Agent 安装向导，解决了原版英文向导看不懂的问题。

### 🌟 主要特点
- **全中文界面**：所有提示、选项、错误信息都是中文
- **一键安装**：复制一条命令即可开始安装
- **智能引导**：自动检测系统环境，提供合适的安装方案
- **安全可靠**：不修改系统核心文件，可随时卸载
- **完整文档**：包含详细的安装和使用说明

## 🚀 快速开始

### 最简单的安装方式（推荐新手）

```bash
# 复制这条命令到终端，按回车即可
curl -s https://raw.githubusercontent.com/horus-claw/hermes-agent-zh/main/chinese_setup_wizard.py | python3
```

### 如果上面的命令有问题，可以分两步操作

```bash
# 1. 先下载安装脚本
curl -o setup_zh.py https://raw.githubusercontent.com/horus-claw/hermes-agent-zh/main/chinese_setup_wizard.py

# 2. 再运行安装脚本
python3 setup_zh.py
```

## 📋 完整安装教程

### 第一步：准备环境

确保你的系统满足以下要求：
- **操作系统**：Ubuntu/Debian/CentOS/macOS/Windows(WSL2)
- **Python版本**：3.9 或更高（推荐 3.11）
- **内存**：至少 4GB
- **磁盘空间**：至少 2GB

检查Python版本：
```bash
python3 --version
```

如果版本低于3.9，需要先升级Python。

### 第二步：运行安装向导

运行上面提到的安装命令，你会看到：

```
🎭🤖 Hermes Agent 中文安装向导
============================================================
欢迎使用 Hermes Agent - 您的全能AI助手
本向导将帮助您完成安装和配置
所有提示均为中文，请按照指引操作
============================================================
```

### 第三步：按照向导提示操作

安装向导会依次询问：

1. **安装目录**（默认：`~/ai-assistant`）
   - 直接回车使用默认目录
   - 或输入自定义目录路径

2. **GitHub仓库地址**（默认：Hermes官方仓库）
   - 直接回车使用默认仓库
   - 或输入自定义仓库地址

3. **API密钥配置**
   - OpenRouter API密钥（推荐）
   - Anthropic API密钥（可选）
   - OpenAI API密钥（可选）
   - 至少需要配置一个有效的API密钥

4. **是否立即启动Hermes**
   - 输入 `y` 立即启动
   - 输入 `n` 稍后手动启动

### 第四步：安装完成

安装成功后，你会看到完整的使用说明：

```
============================================================
🚀 安装完成！使用说明
============================================================

📁 安装目录:
  Hermes代码: /home/你的用户名/ai-assistant/hermes-agent
  配置文件: ~/.hermes/

🚀 启动 Hermes Agent:
  cd /home/你的用户名/ai-assistant/hermes-agent
  source venv/bin/activate  # 激活虚拟环境
  python run_agent.py       # 启动Hermes

📝 常用命令:
  /help     - 查看帮助
  /skills   - 列出可用技能
  /model    - 切换AI模型
  /memory   - 管理记忆
  /exit     - 退出程序
```

## 🛠️ 安装后的操作

### 启动 Hermes Agent

```bash
# 进入安装目录
cd ~/ai-assistant/hermes-agent

# 激活Python虚拟环境（重要！）
source venv/bin/activate

# 启动Hermes
python run_agent.py
```

### 测试是否安装成功

启动后，输入一些简单的命令测试：

```
你好
/help
/skills
```

如果都能正常响应，说明安装成功。

## 📖 使用指南

### 基本操作

- **对话**：直接输入问题，Hermes会回答你
- **命令**：以 `/` 开头的特殊命令
- **技能**：使用预置的技能完成特定任务
- **记忆**：Hermes会记住你的偏好和习惯

### 常用命令列表

| 命令 | 说明 | 示例 |
|------|------|------|
| `/help` | 查看所有可用命令 | `/help` |
| `/skills` | 列出可用技能 | `/skills` |
| `/model` | 切换AI模型 | `/model claude-sonnet` |
| `/memory` | 管理记忆 | `/memory list` |
| `/todo` | 管理任务列表 | `/todo add 备份配置` |
| `/clear` | 清除屏幕 | `/clear` |
| `/exit` | 退出程序 | `/exit` |

### 实用技能

Hermes内置了许多实用技能：

- **服务器优化**：自动优化Linux服务器配置
- **代码开发**：帮助编写、调试、测试代码
- **系统管理**：管理进程、文件、网络等
- **文档处理**：处理PDF、Word、Excel等文档

使用技能的方法：
```
使用服务器优化技能
或
加载 github-pr-workflow 技能
```

## 🔧 故障排除

### 常见问题及解决方法

#### 问题1：安装脚本运行失败
**症状**：`python3: command not found` 或类似错误
**解决**：
```bash
# 安装Python3
sudo apt update
sudo apt install -y python3 python3-pip
```

#### 问题2：API密钥错误
**症状**：Hermes启动后立即退出，提示API密钥无效
**解决**：
1. 检查 `~/.hermes/.env` 文件中的API密钥格式
2. 确认API密钥有效且有余额
3. 确认网络可以访问API服务

#### 问题3：Python依赖安装失败
**症状**：`pip install` 失败，网络连接超时
**解决**：
```bash
# 使用国内镜像源
pip install -r requirements.txt -i https://pypi.tuna.tsinghua.edu.cn/simple
```

#### 问题4：虚拟环境问题
**症状**：`source venv/bin/activate` 失败
**解决**：
```bash
# 重新创建虚拟环境
cd ~/ai-assistant/hermes-agent
rm -rf venv
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

### 获取更多帮助

如果遇到本文未涵盖的问题：

1. **查看详细日志**：
   ```bash
   python run_agent.py --verbose 2>&1 | tee error.log
   ```

2. **检查系统状态**：
   ```bash
   python3 --version
   pip list | grep hermes
   ls -la ~/.hermes/
   ```

3. **重置配置**（最后的手段）：
   ```bash
   # 备份当前配置
   cp -r ~/.hermes ~/.hermes.backup
   
   # 删除配置目录
   rm -rf ~/.hermes
   
   # 重新运行安装向导
   curl -s https://raw.githubusercontent.com/horus-claw/hermes-agent-zh/main/chinese_setup_wizard.py | python3
   ```

## 📁 文件结构说明

安装完成后，你的系统会有以下文件：

```
~/.hermes/                    # 配置目录（用户级）
├── .env                      # API密钥文件（重要！不要分享）
├── config.yaml               # 主配置文件
├── skills/                   # 技能目录（后续创建）
└── sessions/                 # 会话历史记录

~/ai-assistant/hermes-agent/  # 程序目录（安装时指定）
├── venv/                     # Python虚拟环境
├── run_agent.py              # 主程序文件
├── requirements.txt          # Python依赖列表
├── chinese_setup_wizard.py   # 中文安装向导
└── ...其他文件
```

## 🔄 更新和维护

### 更新 Hermes Agent

```bash
# 进入安装目录
cd ~/ai-assistant/hermes-agent

# 更新代码
git pull origin main

# 更新依赖
pip install -r requirements.txt --upgrade
```

### 备份配置

```bash
# 创建配置备份
tar -czf hermes-backup-$(date +%Y%m%d).tar.gz ~/.hermes/

# 备份文件会保存在当前目录
# 文件名格式：hermes-backup-20250410.tar.gz
```

### 恢复配置

```bash
# 解压备份文件
tar -xzf hermes-backup-20250410.tar.gz -C ~/

# 覆盖现有配置（注意这会丢失当前配置）
```

## 🤝 贡献指南

欢迎改进这个中文安装向导！

1. **Fork 本仓库**
2. **创建特性分支** (`git checkout -b feature/改进功能`)
3. **提交更改** (`git commit -m '添加某个功能'`)
4. **推送分支** (`git push origin feature/改进功能`)
5. **创建 Pull Request**

### 需要改进的地方
- 更多的错误处理提示
- 支持更多操作系统
- 优化安装流程
- 添加更多中文文档

## 📄 许可证

本项目基于 MIT 许可证开源。

## 🙏 致谢

- 感谢 Hermes Agent 原项目的所有开发者
- 感谢所有测试和使用本中文向导的用户
- 感谢提出宝贵建议的贡献者

---

**💖 希望这个中文安装向导能帮助更多中文用户轻松使用 Hermes Agent！**

**✨ 让技术不再有语言障碍！**
