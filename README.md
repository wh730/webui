# dimension-mall

#### 介绍

基于Python + Pytest + Requests 搭建的商城接口自动化测试脚本，实现接口全流程自动化执行、数据驱动、测试报告生成，用于商城后端接口回归测试。

多人合作

#### 软件架构
软件架构说明
dimension-mall/
├── case/ # 测试用例目录，存放各业务接口测试脚本
├── data/ # 测试数据文件，json 格式存储入参、预期结果
├── utils/ # 公共工具类：请求封装、日志、数据库操作、断言工具
├── log/ # 自动化运行日志输出目录
├── png/ # 截图 / 报告图片资源
├── conftest.py # pytest 全局钩子、前置后置操作、全局 fixture
├── pytest.ini # pytest 全局配置文件
├── requirements.txt # 项目依赖包清单
├── run.py # 项目启动入口，一键执行全部用例并生成测试报告

#### 安装教程

1. 克隆本仓库到本地
```bash
git clone https://gitee.com/pan-yan-1/dimension-mall.git

#### 使用说明

在data文件夹中配置对应接口的测试参数（正常场景、异常场景、边界值）
在case目录编写对应模块接口自动化用例
执行自动化脚本（两种方式）
方式 1：直接运行启动文件
bash
运行
python run.py
方式 2：pytest 命令行执行
bash
运行
pytest case/ -s -v
运行完成自动生成测试日志、可视化测试报告

#### 参与贡献

Fork 本仓库到个人账号
新建分支：feat_xxx（新增功能）/ bugfix_xxx（修复用例 bug）
本地提交代码，推送至个人分支
提交 Pull Request 合并到主分支 master


#### 特技

支持数据驱动，用例与测试数据分离，便于维护
统一封装 HTTP 请求，自动携带 token 鉴权
完整日志记录，方便定位接口报错
兼容多环境切换（测试环境 / 预发布环境）
支持接口异常场景、越权、参数非法等健壮性测试
