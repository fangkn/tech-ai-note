
# gin 工程目录结构

```
your-project/
│
├── cmd/                 # 各种可执行程序入口（main.go 放这里）
│   └── server/
│       └── main.go
│
├── configs/             # 配置文件（yaml/json/toml 等）
│   └── config.yaml
│
├── internal/            # 项目内部代码（不对外暴露）
│   ├── api/             # DTO（请求/响应结构）和路由
│   │   ├── v1/
│   │   │   ├── user.go
│   │   │   ├── user_req.go
│   │   │   └── user_resp.go
│   │   └── router.go    # 注册所有路由
│   │
│   ├── handler/         # controller 层（HTTP 入口）
│   │   └── user_handler.go
│   │
│   ├── service/         # 业务逻辑（service 层）
│   │   └── user_service.go
│   │
│   ├── repository/      # 数据访问（DB / Redis / 外部服务）
│   │   └── user_repo.go
│   │
│   ├── model/           # 领域对象、数据库模型（GORM/SQLX struct）
│   │   └── user.go
│   │
│   ├── middleware/      # Gin 中间件
│   │   ├── auth.go
│   │   └── logger.go
│   │
│   ├── pkg/             # 通用工具库（JWT、加密、日志、雪花ID等）
│   │   ├── jwt/
│   │   ├── logger/
│   │   ├── response/
│   │   └── util/
│   │
│   ├── core/            # 应用核心（启动、初始化、配置、DI）
│   │   ├── config.go
│   │   ├── server.go
│   │   ├── init_db.go
│   │   ├── init_redis.go
│   │   └── init_logger.go
│   │
│   ├── job/             # 定时任务 / 异步任务
│   │   └── clean_user_job.go
│   │
│   └── docs/            # swagger / api 文档
│
├── pkg/                 # 可供外部项目复用的 library（非 internal）
│   └── ...              
│
├── scripts/             # shell 脚本、数据库迁移脚本
│   ├── migrate.sh
│   └── build.sh
│
├── test/                # 集成测试、单元测试
│   └── user_test.go
│
├── go.mod
├── go.sum
└── README.md


```

