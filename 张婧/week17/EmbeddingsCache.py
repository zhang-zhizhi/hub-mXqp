import os
from redisvl.extensions.cache.embeddings import EmbeddingsCache
from redisvl.utils.vectorize import HFTextVectorizer

# 禁用 tokenizers 并行（避免死锁）
os.environ["TOKENIZERS_PARALLELISM"] = "False"

# 初始化嵌入缓存
embed_cache = EmbeddingsCache(
    name="my_embed_cache",
    redis_url="redis://localhost:6379",
    ttl=3600  # 1小时过期
)

# 初始化向量化器（自动使用缓存）
vectorizer = HFTextVectorizer(
    model="sentence-transformers/all-MiniLM-L6-v2",
    cache=embed_cache  # 关键：注入缓存
)

# 使用示例
text = "What is machine learning?"
embedding = vectorizer.embed(text)  # 第一次调用，计算并缓存
embedding_cached = vectorizer.embed(text)  # 第二次调用，命中缓存（极快）
