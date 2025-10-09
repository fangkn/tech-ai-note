
# ollama 资料

1、使用Ollama+OpenWebUI本地部署Gemma谷歌AI开放大模型完整指南:[https://cloud.tencent.com/developer/article/2425136](https://cloud.tencent.com/developer/article/2425136)

2、动手学习 ollama [https://github.com/datawhalechina/handy-ollama/tree/main](https://github.com/datawhalechina/handy-ollama/tree/main)

3、Ollama 支持的模型库列表 [https://ollama.com/library](https://ollama.com/library)

4、ollama 文档 [https://github.com/qianniucity/ollama-doc](https://github.com/qianniucity/ollama-doc)

# ollama 常用命令

```shell
Usage:
  ollama [flags]
  ollama [command]

Available Commands:
  serve       Start ollama
  create      Create a model from a Modelfile
  show        Show information for a model
  run         Run a model
  pull        Pull a model from a registry
  push        Push a model to a registry
  list        List models
  ps          List running models
  cp          Copy a model
  rm          Remove a model
  help        Help about any command

Flags:
  -h, --help      help for ollama
  -v, --version   Show version information
```

# ollama 安装与配置 - Windows 系统篇

> ollama 下载：<https://ollama.com/download>
>
> ollama 官方主页：<https://ollama.com>
>
> ollama 官方 GitHub 源代码仓库：<https://github.com/ollama/ollama>

下载后直接安装。

环境变量配置：

| 参数                     | 标识与配置                                                                                                                                                                                                                          |
| ------------------------ | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| OLLAMA_MODELS            | 表示模型文件的存放目录，默认目录为**当前用户目录**即  `C:\Users%username%.ollama\models`<br />Windows 系统 **建议不要放在C盘**，可放在其他盘（如 `D:\ollama\models`）                                             |
| OLLAMA_HOST              | 表示ollama 服务监听的网络地址，默认为**127.0.0.1** <br />如果想要允许其他电脑访问 Ollama（如局域网中的其他电脑），**建议设置**成 **0.0.0.0**                                                                    |
| OLLAMA_PORT              | 表示ollama 服务监听的默认端口，默认为**11434** <br />如果端口有冲突，可以修改设置成其他端口（如**8080**等）                                                                                                            |
| OLLAMA_ORIGINS           | 表示HTTP 客户端的请求来源，使用半角逗号分隔列表<br />如果本地使用不受限制，可以设置成星号 `*`                                                                                                                                     |
| OLLAMA_KEEP_ALIVE        | 表示大模型加载到内存中后的存活时间，默认为**5m**即 5 分钟<br />（如纯数字300 代表 300 秒，0 代表处理请求响应后立即卸载模型，任何负数则表示一直存活）<br />建议设置成 **24h** ，即模型在内存中保持 24 小时，提高访问速度 |
| OLLAMA_NUM_PARALLEL      | 表示请求处理的并发数量，默认为**1** （即单并发串行处理请求）<br />建议按照实际需求进行调整                                                                                                                                   |
| OLLAMA_MAX_QUEUE         | 表示请求队列长度，默认值为**512** <br />建议按照实际需求进行调整，超过队列长度的请求会被抛弃                                                                                                                                  |
| OLLAMA_DEBUG             | 表示输出 Debug 日志，应用研发阶段可以设置成**1** （即输出详细日志信息，便于排查问题）                                                                                                                                        |
| OLLAMA_MAX_LOADED_MODELS | 表示最多同时加载到内存中模型的数量，默认为**1** （即只能有 1 个模型在内存中）

启动服务， 要在管理员模式下启动。

```shell
ollama serve
```
