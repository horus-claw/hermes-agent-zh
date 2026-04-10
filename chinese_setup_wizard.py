#!/usr/bin/env python3
"""
Hermes Agent 中文安装向导
专为中文用户设计，解决英文向导问题
"""

import os
import sys
import subprocess
from pathlib import Path

def print_banner():
    """显示中文欢迎横幅"""
    print("\n" + "="*60)
    print("🎭🤖 Hermes Agent 中文安装向导")
    print("="*60)
    print("欢迎使用 Hermes Agent - 您的全能AI助手")
    print("本向导将帮助您完成安装和配置")
    print("所有提示均为中文，请按照指引操作")
    print("="*60 + "\n")

def check_requirements():
    """检查系统要求"""
    print("🔍 检查系统要求...")
    
    requirements = [
        ("Python 3.9+", check_python_version),
        ("Git", check_git),
        ("pip", check_pip),
        ("磁盘空间", check_disk_space),
    ]
    
    all_ok = True
    for name, check_func in requirements:
        try:
            if check_func():
                print(f"  ✅ {name}")
            else:
                print(f"  ❌ {name} - 不符合要求")
                all_ok = False
        except Exception as e:
            print(f"  ⚠️ {name} - 检查失败: {e}")
            all_ok = False
    
    return all_ok

def check_python_version():
    """检查Python版本"""
    import sys
    return sys.version_info >= (3, 9)

def check_git():
    """检查Git是否安装"""
    try:
        subprocess.run(["git", "--version"], capture_output=True, check=True)
        return True
    except:
        return False

def check_pip():
    """检查pip是否安装"""
    try:
        subprocess.run(["pip", "--version"], capture_output=True, check=True)
        return True
    except:
        return False

def check_disk_space():
    """检查磁盘空间（简化版）"""
    # 简化检查，假设至少有1GB空间
    try:
        import shutil
        total, used, free = shutil.disk_usage("/")
        return free > 1_000_000_000  # 1GB
    except:
        return True  # 如果检查失败，假设空间足够

def install_dependencies():
    """安装系统依赖"""
    print("\n📦 安装系统依赖...")
    
    system = detect_system()
    
    if system == "ubuntu" or system == "debian":
        commands = [
            ["apt", "update"],
            ["apt", "install", "-y", "python3", "python3-pip", "python3-venv", "git", "curl"],
        ]
    elif system == "centos" or system == "rhel":
        commands = [
            ["yum", "install", "-y", "python3", "python3-pip", "git", "curl"],
        ]
    elif system == "macos":
        print("  请确保已安装 Homebrew")
        commands = [
            ["brew", "install", "python@3.11", "git"],
        ]
    else:
        print(f"  ⚠️ 未知系统类型: {system}")
        print("  请手动安装: Python 3.9+, Git, pip")
        return False
    
    for cmd in commands:
        print(f"  运行: {' '.join(cmd)}")
        try:
            subprocess.run(cmd, check=True)
        except subprocess.CalledProcessError as e:
            print(f"  ❌ 命令执行失败: {e}")
            return False
    
    print("  ✅ 依赖安装完成")
    return True

def detect_system():
    """检测操作系统类型"""
    import platform
    
    system = platform.system().lower()
    if system == "linux":
        # 尝试检测Linux发行版
        try:
            with open("/etc/os-release", "r") as f:
                content = f.read().lower()
                if "ubuntu" in content or "debian" in content:
                    return "ubuntu"
                elif "centos" in content or "rhel" in content:
                    return "centos"
        except:
            pass
        return "linux"
    elif system == "darwin":
        return "macos"
    elif system == "windows":
        return "windows"
    else:
        return "unknown"

def clone_repository():
    """克隆Hermes仓库"""
    print("\n📥 下载Hermes Agent代码...")
    
    install_dir = input("  请输入安装目录 [默认: ~/ai-assistant]: ").strip()
    if not install_dir:
        install_dir = "~/ai-assistant"
    
    # 展开~到用户目录
    install_dir = os.path.expanduser(install_dir)
    
    repo_url = input("  请输入GitHub仓库URL [默认: https://github.com/你的用户名/hermes-agent.git]: ").strip()
    if not repo_url:
        repo_url = "https://github.com/你的用户名/hermes-agent.git"
    
    try:
        # 创建目录
        Path(install_dir).mkdir(parents=True, exist_ok=True)
        
        # 克隆仓库
        cmd = ["git", "clone", repo_url, f"{install_dir}/hermes-agent"]
        print(f"  运行: {' '.join(cmd)}")
        subprocess.run(cmd, check=True, cwd=install_dir)
        
        print(f"  ✅ 代码下载完成到: {install_dir}/hermes-agent")
        return install_dir
    except Exception as e:
        print(f"  ❌ 下载失败: {e}")
        return None

def setup_virtual_env(install_dir):
    """设置Python虚拟环境"""
    print("\n🐍 设置Python虚拟环境...")
    
    venv_path = f"{install_dir}/hermes-agent/venv"
    
    if os.path.exists(venv_path):
        choice = input(f"  虚拟环境已存在，是否重新创建? [y/N]: ").strip().lower()
        if choice == 'y':
            import shutil
            shutil.rmtree(venv_path)
        else:
            print("  使用现有虚拟环境")
            return True
    
    try:
        cmd = ["python3", "-m", "venv", "venv"]
        print(f"  运行: {' '.join(cmd)}")
        subprocess.run(cmd, check=True, cwd=f"{install_dir}/hermes-agent")
        
        print("  ✅ 虚拟环境创建完成")
        return True
    except Exception as e:
        print(f"  ❌ 创建虚拟环境失败: {e}")
        return False

def install_python_packages(install_dir):
    """安装Python依赖包"""
    print("\n📦 安装Python依赖包...")
    
    # 激活虚拟环境并安装
    try:
        # 使用虚拟环境的pip
        pip_path = f"{install_dir}/hermes-agent/venv/bin/pip"
        
        cmd = [pip_path, "install", "-r", "requirements.txt"]
        print(f"  运行: {' '.join(cmd)}")
        result = subprocess.run(cmd, capture_output=True, text=True, cwd=f"{install_dir}/hermes-agent")
        
        if result.returncode == 0:
            print("  ✅ 依赖包安装完成")
            return True
        else:
            print(f"  ❌ 安装失败")
            print(f"  错误输出: {result.stderr}")
            return False
    except Exception as e:
        print(f"  ❌ 安装失败: {e}")
        return False

def setup_configuration():
    """设置配置文件"""
    print("\n⚙️ 设置配置文件...")
    
    hermes_home = os.path.expanduser("~/.hermes")
    Path(hermes_home).mkdir(parents=True, exist_ok=True)
    
    print("  需要配置以下API密钥:")
    print("  1. OpenRouter API密钥 (推荐)")
    print("  2. Anthropic API密钥")
    print("  3. OpenAI API密钥")
    print("  至少需要配置一个API密钥")
    
    config = {}
    
    openrouter_key = input("  请输入OpenRouter API密钥 (可选，直接回车跳过): ").strip()
    if openrouter_key:
        config["OPENROUTER_API_KEY"] = openrouter_key
    
    anthropic_key = input("  请输入Anthropic API密钥 (可选，直接回车跳过): ").strip()
    if anthropic_key:
        config["ANTHROPIC_API_KEY"] = anthropic_key
    
    openai_key = input("  请输入OpenAI API密钥 (可选，直接回车跳过): ").strip()
    if openai_key:
        config["OPENAI_API_KEY"] = openai_key
    
    # 创建.env文件
    env_content = "# Hermes Agent API密钥配置\n"
    for key, value in config.items():
        env_content += f"{key}={value}\n"
    
    env_file = f"{hermes_home}/.env"
    with open(env_file, "w") as f:
        f.write(env_content)
    
    print(f"  ✅ API密钥保存到: {env_file}")
    print("  ⚠️ 请妥善保管此文件，不要分享给他人")
    
    # 创建config.yaml
    config_template = f"""# Hermes Agent 配置文件
# 中文注释版

agent:
  # AI模型设置
  model: "anthropic/claude-sonnet-4"  # 默认模型
  provider: "openrouter"              # API提供商
  
  # 人格设定
  system_message: |
    你是Hermes Agent，一个全能AI助手。
    请用中文回复用户，提供专业、有用的帮助。
    
  # 工具设置
  enabled_toolsets: ["terminal", "file", "web", "code"]
  
  # 会话设置
  max_iterations: 100                  # 最大工具调用次数
  save_trajectories: true             # 保存执行轨迹

# 界面设置
display:
  # CLI界面皮肤
  skin: "default"                     # 可选: default, ares, mono, slate
  
  # 进度显示
  tool_progress: true                 # 显示工具执行进度
  
  # 动画效果
  spinner: true                       # 启用加载动画

# 网关设置 (可选)
gateway:
  telegram:
    enabled: false                    # 启用Telegram机器人
    token: ""                         # Telegram机器人令牌
  
  discord:
    enabled: false                    # 启用Discord机器人
    token: ""                         # Discord机器人令牌
"""
    
    config_file = f"{hermes_home}/config.yaml"
    with open(config_file, "w", encoding="utf-8") as f:
        f.write(config_template)
    
    print(f"  ✅ 配置文件创建: {config_file}")
    
    return True

def test_installation(install_dir):
    """测试安装是否成功"""
    print("\n🧪 测试安装...")
    
    try:
        # 尝试导入hermes模块
        test_script = f"""
import sys
sys.path.insert(0, '{install_dir}/hermes-agent')
try:
    import hermes
    print("✅ Hermes模块导入成功")
except ImportError as e:
    print(f"❌ Hermes模块导入失败: {{e}}")
    sys.exit(1)
"""
        
        python_path = f"{install_dir}/hermes-agent/venv/bin/python"
        result = subprocess.run([python_path, "-c", test_script], capture_output=True, text=True)
        
        if result.returncode == 0:
            print("  ✅ 安装测试通过")
            return True
        else:
            print("  ❌ 安装测试失败")
            print(f"  错误信息: {result.stderr}")
            return False
    except Exception as e:
        print(f"  ❌ 测试失败: {e}")
        return False

def show_usage_instructions(install_dir):
    """显示使用说明"""
    print("\n" + "="*60)
    print("🚀 安装完成！使用说明")
    print("="*60)
    
    print("\n📁 安装目录:")
    print(f"  Hermes代码: {install_dir}/hermes-agent")
    print(f"  配置文件: ~/.hermes/")
    
    print("\n🚀 启动 Hermes Agent:")
    print(f"  cd {install_dir}/hermes-agent")
    print("  source venv/bin/activate  # 激活虚拟环境")
    print("  python run_agent.py       # 启动Hermes")
    
    print("\n📝 常用命令:")
    print("  /help     - 查看帮助")
    print("  /skills   - 列出可用技能")
    print("  /model    - 切换AI模型")
    print("  /memory   - 管理记忆")
    print("  /exit     - 退出程序")
    
    print("\n🔧 更新 Hermes:")
    print(f"  cd {install_dir}/hermes-agent")
    print("  git pull origin main")
    print("  pip install -r requirements.txt --upgrade")
    
    print("\n💾 备份配置:")
    print("  tar -czf hermes-backup.tar.gz ~/.hermes/")
    
    print("\n🆘 获取帮助:")
    print("  遇到问题可以:")
    print("  1. 查看日志: python run_agent.py --verbose")
    print("  2. 检查API密钥: cat ~/.hermes/.env")
    print("  3. 重置配置: 删除 ~/.hermes/ 目录重新配置")
    
    print("\n" + "="*60)
    print("🎉 恭喜！您现在可以开始使用 Hermes Agent 了！")
    print("="*60)

def main():
    """主函数"""
    print_banner()
    
    # 检查系统要求
    if not check_requirements():
        print("\n⚠️ 系统要求检查失败")
        choice = input("是否继续安装? [y/N]: ").strip().lower()
        if choice != 'y':
            print("安装取消")
            return
    
    # 安装依赖
    if not install_dependencies():
        print("\n❌ 依赖安装失败")
        return
    
    # 克隆仓库
    install_dir = clone_repository()
    if not install_dir:
        print("\n❌ 代码下载失败")
        return
    
    # 设置虚拟环境
    if not setup_virtual_env(install_dir):
        print("\n❌ 虚拟环境设置失败")
        return
    
    # 安装Python包
    if not install_python_packages(install_dir):
        print("\n❌ Python包安装失败")
        return
    
    # 设置配置
    if not setup_configuration():
        print("\n❌ 配置设置失败")
        return
    
    # 测试安装
    if not test_installation(install_dir):
        print("\n⚠️ 安装测试失败，但可能仍可运行")
        choice = input("是否继续? [y/N]: ").strip().lower()
        if choice != 'y':
            return
    
    # 显示使用说明
    show_usage_instructions(install_dir)
    
    # 询问是否立即启动
    choice = input("\n是否立即启动 Hermes Agent? [Y/n]: ").strip().lower()
    if choice != 'n':
        try:
            print("\n🚀 启动 Hermes Agent...")
            cmd = [
                f"{install_dir}/hermes-agent/venv/bin/python",
                f"{install_dir}/hermes-agent/run_agent.py"
            ]
            subprocess.run(cmd)
        except KeyboardInterrupt:
            print("\n👋 Hermes Agent 已停止")
        except Exception as e:
            print(f"\n❌ 启动失败: {e}")
            print("请手动启动: cd {install_dir}/hermes-agent && source venv/bin/activate && python run_agent.py")

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n\n👋 安装向导已取消")
        sys.exit(0)
    except Exception as e:
        print(f"\n❌ 安装向导出错: {e}")
        sys.exit(1)