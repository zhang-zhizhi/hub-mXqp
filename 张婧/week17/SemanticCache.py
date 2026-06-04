from redisvl.extensions.cache.llm import SemanticCache

# 初始化语义缓存
sem_cache = SemanticCache(
    name="llm_sem_cache",
    redis_url="redis://localhost:6379",
    distance_threshold=0.5,  # 余弦距离阈值，越低越严格
    ttl=3600
)

# 存储 LLM 响应
sem_cache.store(
    prompt="What is the capital of France?",
    response="Paris"
)

# 语义匹配查询（即使措辞不同）
result = sem_cache.check("France's capital city?")
if result:
    print(f"Cache hit: {result[0]['response']}")  # 输出 "Paris"