<!--
 * @Author       : Sean
 * @Date         : 2022-03-07 15:10:46
 * @LastEditors  : Sean
 * @LastEditTime : 2022-03-10 11:10:41
 * @Description  : 这是由 Sean 创建
 * @FilePath     : /PT_Captcha/docs/apply_tencent_ocr.md
 * Copyright    : Copyright ©2019-2022 Sean,Inc
-->
## 申请腾讯云 OCR 接入

> 其他问题参考：[文字识别接入常见问题](https://cloud.tencent.com/developer/article/1700555)

1. 注册账号（第一次登录需要关联微信账号）：[https://cloud.tencent.com/](https://cloud.tencent.com/)

![step1](https://github.com/SeanSuny/pt_captcha/raw/main/images/step1.png)

2. 开通 OCR 服务：[https://console.cloud.tencent.com/ocr/general](https://console.cloud.tencent.com/ocr/general)

![step2](https://github.com/SeanSuny/pt_captcha/raw/main/images/step2.png)

3. 申请访问密钥（推荐创建子用户只分配 ocr 权限）：[https://console.cloud.tencent.com/cam/capi](https://console.cloud.tencent.com/cam/capi)

![step3](https://github.com/SeanSuny/pt_captcha/raw/main/images/step3.png)
需要注意，腾讯的免费额度不是立即分配的，通常是在整点分配，所以如果创建好账号后调用出现如下报错：
```python
[TencentCloudSDKException] code:ResourcesSoldOut.ChargeStatusException message:计费状态异常
```
可能是免费额度未更新，需要再等待一段时间（过了整点）再尝试

