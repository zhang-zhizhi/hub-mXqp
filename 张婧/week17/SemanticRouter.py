from redisvl.extensions.router import Route, SemanticRouter

# 定义路由规则
routes = [
    Route(
        name="greeting",
        references=["hello", "hi", "good morning", "hey"],
        metadata={"priority": 1, "handler": "greeting_handler"},
        distance_threshold=0.3  # 严格匹配
    ),
    Route(
        name="technical_support",
        references=["bug", "error", "not working", "crash"],
        metadata={"priority": 2, "handler": "tech_support_handler"},
        distance_threshold=0.4
    ),
    Route(
        name="sales",
        references=["price", "buy", "purchase", "cost"],
        metadata={"priority": 3, "handler": "sales_handler"},
        distance_threshold=0.5  # 宽松匹配
    )
]

# 构建路由器
router = SemanticRouter(
    name="app_router",
    routes=routes,
    redis_url="redis://localhost:6379"
)

# 路由查询
query = "Hey, good morning!"
match = router(query)
print(f"Routed to: {match.name}")  # 输出 "greeting"

query = "The application keeps crashing"
match = router(query)
print(f"Routed to: {match.name}")  # 输出 "technical_support"