---
layout: post
title: Mac Dock Management
tag: life
update: 2025-08-14
---

Hiding icons from dock while keeping the application open.

随着运行程序增多，Dock 会显示所有运行的程序图标。对于一些不常用的程序，可能会希望将其从 Dock 中移除，但又不想完全退出程序。本文介绍如何通过修改应用程序的 Info.plist 文件来隐藏 Dock 中的图标。

此方法适用于某些在菜单栏中显示的应用程序，如微信、QQ 等。通过这种方式，可以将这些应用程序的图标从 Dock 中移除，但仍然可以通过菜单栏访问它们。

主要步骤如下：  
备份 plist 文件 → 修改 plist 文件 → codesign 签名 → 重启应用程序

以微信为例，将微信图标从 Dock 中移除，详细步骤如下：

1. 最先需要备份对应的 Info.plist 文件
   
   ```bash
   # 备份对应的Info.plist
   cp xxxx/Info.plist ~/Desktop/Info.plist
   ```
   此步骤是为了防止修改后出现问题，可以随时恢复原来的状态。

   若不想用命令行，可以直接在 Finder 中找到微信应用程序，右键点击“显示包内容”，然后找到 `Contents` 文件夹中的 `Info.plist` 文件，将其复制到桌面或其他安全位置。

2. 用 Vim 辑器打开对应 APP 的 Info.plist 文件
   
   ```bash
   sudo vim /Applications/WeChat.app/Contents/Info.plist
   ```

   输入密码。

3. 修改 Info.plist 文件，添加以下内容

   ```xml
   <key>LSUIElement</key>
   <true/>
   ```
   最终的 Info.plist 文件内容如下所示：
   <img src="https://drive.google.com/thumbnail?id=14M7krm_08aYmI1DWT7TMGx2uAbNlcUsw&sz=w1000" alt="" style="display: block; margin-right: auto; margin-left: auto; zoom:80%;" />

   保存 Info.plist 文件并退出。

4. codesign 重新签名 
   
   ```bash
   sudo codesign -f -s - "/Applications/WeChat.app"
   ```
   输入密码。

5. 重启 app，微信图标就会从 Dock 中消失。可以从菜单栏中打开微信。



--------------------------------------------------------------------------------

Q: 如何重新在 Dock 显示图标?  
A: 只需要删除 Info.plist 中与 `LSUIElement` 键相关的两行代码即可。

--------------------------------------------------------------------------------

Q: 可以隐藏 Mac OS 系统应用吗？  
A: 我尝试过修改 <img src="https://drive.google.com/thumbnail?id=1zPJ5QudJZixhwiFx8GjhU0JoBEDJNuUO&sz=w1000" alt="" style="zoom:5%; vertical-align: middle; " /> Stickies 的 Info.plist 文件，添加 `LSUIElement` 键，但并没有成功。可能是因为系统应用的权限更高，或者有其他限制。


--------------------------------------------------------------------------------

## cDock

<https://github.com/w0lfschild/cDock?tab=readme-ov-file>

Many reviews say cDock is buggy...

- cDock requires [disabling System Integrity Protection](http://osxdaily.com/2015/10/05/disable-rootless-system-integrity-protection-mac-os-x/)


--------------------------------------------------------------------------------

ref:

- [CSDN: Macos上程序坞 (Dock) 栏隐藏 app 图标](https://blog.csdn.net/qq_43619748/article/details/149882407)