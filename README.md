<h1 align="center">pt-captcha---PT验证码识别</h1>
<p align="center">
   验证码 --- 一个<b>验证码识别框架</b> base on an Tencent / Baidu OCR API
</p>

[![Github-image](https://img.shields.io/static/v1?label=Github&message=pt-captcha&color=brightgreen)](https://github.com/seansuny/pt-captcha)
[![Gitee-image](https://img.shields.io/static/v1?label=Gitee&message=pt-captcha&color=brightgreen)](https://gitee.com/seansuny/pt-captcha)
[![docker-version](https://img.shields.io/docker/v/seansuny/pt-captcha?logo=docker&label=Version&color=green)](https://hub.docker.com/r/seansuny/pt-captcha/tags)
[![docker-pulls](https://img.shields.io/docker/pulls/seansuny/pt-captcha?logo=docker&label=Pulls&color=blue)](https://hub.docker.com/r/seansuny/pt-captcha)
[![docker-stars](https://img.shields.io/docker/stars/seansuny/pt-captcha?logo=docker&label=Stars&color=blue)](https://hub.docker.com/r/seansuny/pt-captcha)
[![docker-image-size](https://img.shields.io/docker/image-size/seansuny/pt-captcha?logo=docker&label=amd64%20Size&arch=amd64&color=orange)](https://hub.docker.com/r/seansuny/pt-captcha)
[![docker-image-size](https://img.shields.io/docker/image-size/seansuny/pt-captcha?logo=docker&label=arm64%20Size&arch=arm64&color=orange)](https://hub.docker.com/r/seansuny/pt-captcha)

### PT验证码识别简介
==========

针对 pt 站点常用的验证码进行预处理并调用腾讯/百度的 ocr api 进行识别，通常用于自动签到

大致的使用流程如下：

1. 首先需要开通百度或腾讯任意一个 ocr 服务，获取到 apikey 及 secret
2. 通过设置环境变量的方式进行配置，并启动运行服务（建议使用 docker 运行）
3. 通过 http 接口调用 POST base64 编码的图片数据，接口将响应并返回识别结果

### 使用方式及步骤
==========

#### 申请凭证

首先需要选择一个 ocr 服务提供方申请接入，并拿到 apikey 及 secret 凭证，具体参考：

* [申请百度智能云 OCR 接入](https://github.com/SeanSuny/pt-captcha/blob/main/docs/apply_baidu_ocr.md)
* [申请腾讯云 OCR 接入](https://github.com/SeanSuny/pt-captcha/blob/main/docs/apply_tencent_ocr.md)


#### Docker容器部署方式
* Docker地址 : [https://hub.docker.com/r/seansuny/pt-captcha](https://hub.docker.com/r/seansuny/pt-captcha)

以腾讯云为例，假设已经获取到的凭证已经保存到对应变量：

* apikey: `$TENCENT_SECRET_ID`
* secret: `$TENCENT_SECRET_KEY`

则容器启动命令如下：

```
docker run -d --name pt-captcha \
    --restart=always -p 5500:5000 \
    -e API_KEY="$TENCENT_SECRET_ID" \
    -e SECRET_KEY="$TENCENT_SECRET_KEY" \
    -e OCR_VENDOR="tencent" \
    seansuny/pt-captcha:latest
```

之后就可以通过容器宿主的 `5500` 端口访问


#### 服务测试

假设容器宿主 IP 为 `10.0.0.100`，则可通过以下方式来查看当前使用的哪个服务提供商：

```
curl http://10.0.0.100:5500/current_ocr
```

因为上文中使用了腾讯的服务，所以该命令会返回 `tencent`

#### 图片识别

首先我们需要将验证码图片转为 base64 编码，本仓库 `image` 目录下提供的示例图片为例：

![captcha](https://github.com/SeanSuny/pt-captcha/raw/main/images/example.png)

将其通过代码或者在线网站转成 base64 编码，假设将其赋值到变量 `$IMAGE_BASE64`，然后就可通过 POST 方法调用该接口进行识别，具体方式如下：

```
curl -X POST http://10.0.0.100:你指定的端口/upload \
    -H 'Content-Type: text/json' \
    -d "{\"image\": \"$IMAGE_BASE64\"}"
```

注意上述参数需要严格的 json 格式，必须使用双引号，最终返回数据为：

```
"recognition":"R5B6B4"
```

### 参数
==========

本仓库只提供容器运行方案，对应配置均通过环境变量进行设置：

|变量名|是否必须|说明|
|---|---|---|
| `OCR_VENDOR` | 是 | 目前仅支持 `tencent` 与 `baidu` |
| `API_KEY` | 是 | 认证凭证，对应关系见下方 |
| `SECRET_KEY` |是|认证凭证，对应关系见下方 |
| `API_REGION` | 否 | 调用 api 所在 region，默认使用 `ap-guangzhou` |


各厂商对应 `API_KEY` 与 `SECRET_KEY` 叫法如下：

|提供方| apikey | secret |
|---|---|---|
| 百度 | `API Key` | `Secret Key` |
| 腾讯 | `SecretId` | `SecretKey` |


另外，`API_REGION` 仅在使用腾讯 ocr 接口时有效，其可选值为：

|地域|    取值|
|---|---|
|华北地区(北京)   | `ap-beijing` |
|华南地区(广州)   | `ap-guangzhou` |
|华东地区(上海)   | `ap-shanghai` |
|港澳台地区(中国香港)    | `ap-hongkong` |
|北美地区(多伦多)  | `na-toronto` |


### 鸣谢
==========

[shuosiw](https://github.com/shuosiw/pt_captcha)


### 许可
===========

[MIT](https://cdn.jsdelivr.net/gh/SeanSuny/pt-captcha@main/LICENSE) 许可协议