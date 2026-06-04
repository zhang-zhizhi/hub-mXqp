from redisvl.extensions.message_history import SemanticMessageHistory

# 初始化消息历史
msg_history = SemanticMessageHistory(
    name="chat_session",
    redis_url="redis://localhost:6379",
    distance_threshold=0.7  # 语义相关度阈值
)

# 添加对话消息
msg_history.add_messages([
    {"role": "user", "content": "What is the size of England?"},
    {"role": "llm", "content": "England is about 130,279 square kilometers."},
    {"role": "user", "content": "What about Portugal?"},
    {"role": "llm", "content": "Portugal is approximately 92,090 square kilometers."}
])

# 获取最近消息
recent = msg_history.get_recent(top_k=2)

# 语义检索相关消息（不用精确关键词）
relevant = msg_history.get_relevant("area comparison between countries", top_k=2)