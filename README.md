# DLBot_ng_ng

DLBot_ng_ng 是一个基于 WebSocket 的聊天机器人，用于连接到 hack.chat 平台。它能够自动加入指定的聊天频道，并根据预设条件发送和记录消息。

## 目前计划

- [ ] 接收 & 发送消息
- [ ] 消息日志记录
- [ ] 掉线重连
- [ ] RL重连
- [ ] 附身（$chat）
- [ ] 通过配置文件设置用户信息
- [ ] [50%]私信命令处理
- [ ] Update_Message支持
- [ ] 通过配置文件增加命令
- [ ] `$gethistory`读取消息记录
- [ ] WebUI读取消息记录
- [ ] 增加多语言支持
- [ ] 更多……

## 功能

正在研发。

## 配置

在运行机器人之前，请确保在 `user.txt` 文件中正确配置以下内容：

1. 用户名 (`username:`)
2. 密码 (`password:`)
3. 频道名称 (`channel:`)
4. 信任用户识别码列表 (`trustedusers:`)

示例 `user.txt` 内容：

```
username: MyNickname
password: MyPassword
channel: MyChannel
trustedusers: ["Trust1", "Trust2"]
```

## 日志

- **log.log**：记录所有系统日志和消息日志。
- **msg.log**：仅记录聊天消息。

## 依赖

requirements.txt

## 安装

1. 克隆仓库：
    ```bash
    git clone https://github.com/lightworld689/DLBot_ng_ng.git
    ```

2. 安装依赖：
    ```bash
    pip install -r requirements.txt
    ```

3. 运行机器人：
    ```bash
    python main.py
    ```

## 贡献

欢迎贡献代码或提出改进建议。请通过 GitHub 提交 Issue 或 Pull Request。

## 许可证

本项目采用 AGPL-3.0 许可证。详情请参见 [LICENSE](LICENSE) 文件。