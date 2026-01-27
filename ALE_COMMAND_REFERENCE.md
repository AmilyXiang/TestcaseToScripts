# Alcatel-Lucent VoIP Phone - SSH Command Reference

## 按键操作

### 模拟按键 (推荐使用)
```bash
key sim <key_name> [<modifier>]
```

**可用按键列表：**
```
数字键：
  0, 1, 2, 3, 4, 5, 6, 7, 8, 9, *, #

通话控制：
  DIAL          - 拨号/接听
  RELEASE       - 挂断/释放
  HANDSFREE     - 免提
  MUTE          - 静音

导航键：
  UP, DOWN, LEFT, RIGHT
  OK            - 确认
  HOME          - 主页
  MENU          - 菜单
  EXIT          - 退出
  HELP          - 帮助

音量控制：
  VOLUP         - 音量增加
  VOLDN         - 音量减小

功能键：
  BIS           - BIS键
  MESSAGE       - 消息
  AUDIOHUB      - 音频中心
  HOMEPAGE      - 主页
  TASKMANAGER   - 任务管理器

软键（屏幕底部可编程按钮）：
  SOFTK0, SOFTK1, SOFTK2, SOFTK3, SOFTK4
  SOFTK5, SOFTK6, SOFTK7, SOFTK8, SOFTK9

会议键：
  CONF0, CONF1, CONF2

附加键：
  ADDON0, ADDON1, ADDON2, ADDON3
```

**修饰键（可选）：**
- `short` - 短按（默认）
- `long` - 长按

**示例：**
```bash
# 短按菜单键
key sim MENU

# 长按 HOME 键
key sim HOME long

# 拨号键盘输入
key sim 1
key sim 2
key sim 3

# 导航并确认
key sim DOWN
key sim OK

# 软键点击
key sim SOFTK0
```

### 触摸屏点击
```bash
key ts <regex> [<nth>]
```

**参数说明：**
- `<regex>` - 匹配屏幕文本的正则表达式
- `<nth>` - 可选，第n个匹配项（从1开始）

**示例：**
```bash
# 点击屏幕上的 "Contacts"
key ts "Contacts"

# 点击第2个 "Call" 按钮
key ts "Call" 2

# 点击包含数字的条目
key ts "[0-9]+"
```

### 旧版按键命令（兼容性）
```bash
aommgr shortpress 0 {{KEY}}  # 短按
aommgr longpress 0 {{KEY}}   # 长按
```

---

## 音频模式

### 切换音频模式
```bash
voicemode set handset      # 手柄模式
voicemode set handsfree    # 免提模式
voicemode set idle         # 待机模式
```

### 静音
```bash
mute
```

---

## 屏幕/显示

### 屏幕信息转储
```bash
screen_dump [mode]
```

**可用模式：**
- `standard` - 标准屏幕内容（默认）
- `raw` - 原始屏幕数据
- `softkey` - 软键区域
- `debug` - 调试信息

**示例：**
```bash
# 获取屏幕文本
screen_dump

# 获取软键标签
screen_dump softkey

# 调试模式
screen_dump debug
```

### 截屏
```bash
fbgrabjpg screen.jpg
screen get
cp screen.png /tmp
```

### 检查屏幕显示特定内容
```bash
screen_dump | grep "{{TEXT}}"
screen_dump | grep "icon_emergency"
screen_dump softkey | grep "Call"
```

### 常见图标
```
icon_emergency          # 紧急呼叫
icon_guard              # 保安呼叫
icon_operator           # 接线员
icon_call               # 呼叫
icon_incoming_call      # 来电
icon_outgoing_call      # 去电
icon_hold               # 保持
icon_hangup             # 挂断
icon_conference         # 会议
icon_transfer           # 转接
icon_contacts           # 联系人
icon_call_log           # 通话记录
icon_menu               # 菜单
icon_voicemail          # 语音邮件
icon_dnd                # 勿扰
icon_handsfree          # 免提
icon_headset_usb        # 耳机
```

---

## 数据库查询（通话记录/联系人/按键配置）

### 通话记录
```bash
# 查询所有通话记录
sqlite3 /data/ICTApplication/sipapp/db/database.db "select * from calllogs"

# 查询最近 10 条
sqlite3 /data/ICTApplication/sipapp/db/database.db "select * from calllogs limit 10"

# 删除所有通话记录
sqlite3 /data/ICTApplication/sipapp/db/database.db "delete from calllogs"

# 查找特定号码的记录
sqlite3 /data/ICTApplication/sipapp/db/database.db "select * from calllogs" | grep "911"
```

### 联系人
```bash
sqlite3 /data/ICTApplication/sipapp/db/database.db "select * from contacts"
sqlite3 /data/ICTApplication/sipapp/db/database.db "delete from contacts"
```

### 可编程按键配置
```bash
sqlite3 /data/ICTApplication/sipapp/db/database.db "select * from progkeys"
sqlite3 /data/ICTApplication/sipapp/db/database.db "delete from progkeys"
```

---

## 日志文件

### SIP 模块日志
```bash
cat /var/log/SIPModule.log
cat /var/log/SIPModule.log | grep "{{KEYWORD}}"
tail -n 100 /var/log/SIPModule.log

# 备份日志
cp /var/log/SIPModule.log /tmp/SIPModule.log
```

### 升级日志
```bash
cat /data/log/upgrade.log
tail -n 10 /data/log/upgrade.log
cat /data/log/upgrade.log | grep 'upgrade_notify'
```

### 重置日志
```bash
tail -n 1 /data/log/Reset.log
tail -n 2 /data/log/Reset.log
```

### 设置日志级别
```bash
level SIPModule debug      # 调试级别
level SIPModule err        # 错误级别
level all err              # 所有模块错误级别
```

---

## 系统信息

### 内存
```bash
cat /proc/meminfo | grep MemTotal
cat /proc/meminfo | grep MemFree
free
```

### 进程
```bash
ps | grep ICT
ps | grep {{PROCESS_NAME}}
```

### 日期时间
```bash
date
```

### 配置查询
```bash
less /data/ICTApplication/sipapp/settings.ini | grep ledsManagementMode
less /data/ICTApplication/sipapp/settings.ini | grep telephonyInterphonyMode
dmurl | grep "main url (local"
```

---

## 常用测试操作

### 清空通话记录
```bash
sqlite3 /data/ICTApplication/sipapp/db/database.db "delete from calllogs"
```

### 删除所有日志
```bash
deletelogs
```

### 清空升级日志
```bash
echo "" > /data/log/upgrade.log
# 或
rm -f /data/log/upgrade.log
```

### 重启 SSH 服务
```bash
/etc/init.d/sshd restart
```

### 删除旧的 core 文件
```bash
    rm -f /data/core/core*.*
find /data/core/*.gz -mtime +5 -exec rm -vf {} \;
```

---

## 测试场景示例

### 场景1：拨打紧急呼叫 + 验证屏幕 + 检查日志
```bash
# 1. 按紧急呼叫键（假设映射到某个可编程键）
aommgr shortpress 0 KP_F1

# 2. 验证屏幕显示紧急呼叫图标
screen_dump | grep "icon_emergency"

# 3. 验证屏幕显示 "Outgoing call" 文字
screen_dump | grep "Outgoing call"

# 4. 检查 SIP 日志确认呼叫建立
cat /var/log/SIPModule.log | grep "call established"

# 5. 挂断
aommgr shortpress 0 KP_HANGUP

# 6. 验证通话记录
sqlite3 /data/ICTApplication/sipapp/db/database.db "select * from calllogs" | grep "emergency"
```

### 场景2：检查屏幕显示特定文本
```bash
# 检查标题是否包含 "Choose your programmable key"
screen_dump | grep "Choose your programmable key"

# 检查是否显示红色背景提示
screen_dump | grep "Red background"
```

### 场景3：免提模式测试
```bash
# 切换到免提
voicemode set handsfree

# 验证屏幕显示免提图标
screen_dump | grep "icon_handsfree"
```

---

## 注意事项

1. **按键名称映射**：测试步骤里的"Emergency call"按钮可能对应某个可编程键（F1-F4），需要根据实际配置确定
2. **图标名称**：`screen_dump` 输出的图标名称格式为 `icon_xxx`
3. **数据库路径**：固定为 `/data/ICTApplication/sipapp/db/database.db`
4. **日志路径**：
   - SIP 日志：`/var/log/SIPModule.log`
   - 升级日志：`/data/log/upgrade.log`
5. **物理操作无法自动化**：拿起/挂上听筒（handset）是物理动作，需要手动或机械臂
