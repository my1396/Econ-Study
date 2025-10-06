---
layout: post
title: Ugreen NAS Guide
tag: programming
update: 2025-08-14
---


Useful resources:

- [快速入门教程 Knowledge center](https://support.ugnas.com/knowledgecenter/#/)

- [应用指南 Detail Documentation](https://support.ugnas.com/knowledgecenter/#/detail/eyJ0eXBlIjoidGFnMDAxIiwibGFuZ3VhZ2UiOiJ6aC1DTiIsImlkIjo0MywiY2xpZW50VHlwZSI6IlBDIiwiYXJ0aWNsZVZlcnNpb24iOiIiLCJwYXRoQ29kZSI6InBybzAwMSx3b3RzMWoifQ==)

- [UGREEN 绿联 CN FAQ](https://www.lulian.cn/n_questions/)
- [UGREEN 绿联 搜索](https://www.ugnas.com/search/?keyword=Samba)

Q: What is my NAS IP? \
A: "控制面板"中，找到【网络设置】，点击【网络连接】。可以查看到当前分配给 NAS 设备的 IP 地址。E.g., my IP: `10.0.0.7`.

Q: Which model is my NAS?  
A: 打开【控制面板】→ 点击系统服务中【关于本机】，可以查看到 NAS 的型号和序列号。我的型号为 `DXP2800`.

## 设置用户

新增用户：支持通过“创建”、“邀请”和“导入”三种方式添加新用户。创建用户时，可以设置用户名、密码、角色（普通用户或管理员），并决定是否启用个人文件夹和密码修改等权限。

Q: 如何新增用户？ \
A: 控制面板 → 用户管理。

【用户】选项卡显示当前已创建的用户信息，包含用户名、描述、角色、状态、编辑操作，双击用户名或操作按钮进行编辑用户信息。

已填写电子邮件地址的用户会显示邮箱地址。

单击“新增”按钮，可“创建/邀请/导入”新用户。


--------------------------------------------------------------------------------

权限管理：在“用户管理”中设置用户和用户组的权限，可以控制不同用户对共享文件夹的访问权限，确保数据安全。

个人文件夹管理功能允许**管理员**对绿联 NAS 中的个人文件夹进行集中管理，帮助合理分配存储资源并保障数据安全。

**访问个人文件夹管理**

1. 进入“文件管理”。
2. 在右侧工具栏中，点击“个人文件夹管理”以打开设置页面。
3. 可以按需配置以下选项：
   - 个人文件夹存放位置
   - 访问权限
   - 启用或关闭【用户自主管理权】
     
     启用用户自主管理权后，用户可以自行决定管理员是否可访问其个人文件夹。
   
   - 设置个人文件夹容量限额
4. 保存设置。点击“确定”以保存并生效。


<figure style="display: flex; flex-direction: column; align-items: center; text-align: center;">
<img src="https://drive.google.com/thumbnail?id=1qScOvVIYf_9Jp2QdSkkje0KYNlvqpFoP&sz=w1000" alt="" style="display: block; margin-right: auto; margin-left: auto; zoom:80%;" />
<figcaption>点击文档图标打开个<strong>人文件夹管理窗口</strong>：启用个人文件夹；自主管理权；容量限额。 </figcaption>
</figure>


Q: 如何为用户启用个人文件夹？
A: 创建用户时，默认不开启个人文件夹。若需启用个人文件夹，请在**创建用户**时勾选“启用个人文件夹”选项。若已创建用户但未启用个人文件夹，可在“文件管理”中编辑该用户信息 (如上图)，勾选“启用个人文件夹”后保存即可。


## 文件服务

### SMB协议

SMB协议：允许用户在局域网环境中将 NAS 设备上的共享文件夹挂载到本地设备上，实现文件的集中存储和统一管理。

- 全平台兼容：支持本地电脑（Windows/macOS）、手机或电视等设备，实现集中存储、跨设备访问。
- 大文件高速传输：针对大文件批量读写优化，传输速度得到提升。
- 多版本协议支持：兼容 SMB1/SMB2/SMB2.1/SMB3，灵活适配不同系统需求。

1. 启动 SMB服务：打开“控制面板”应用，点击【文件服务】＞【SMB】。勾选“启用SMB服务“，点击“应用”保存生效。
2. MacOS 挂载 SMB 共享文件夹
   - 打开 Finder，点击“前往”菜单，选择“连接服务器”。
   - 输入 `smb://<NAS_IP>/`，例如 `smb://172.17.70.242`
   - 输入 NAS 设备的用户名和密码进行身份验证，完成验证后，即可看到可供挂载的共享文件夹列表。
3. 选择需要访问的共享文件夹，点击进入即可进行文件的存取与编辑操作。


上传文件

文件管理提供多种从本地计算机上传文件和文件夹至绿联云 NAS 的方法。

--------------------------------------------------------------------------------

## 移动端文件管理



ref: [绿联云移动端/平板文件管理](https://support.ugnas.com/#/detail/eyJpZCI6MTIzLCJ0eXBlIjoidGFnMDAxIiwicGF0aENvZGUiOiJwcm8wMDEsbmo0cHQ3IiwibGFuZ3VhZ2UiOiJ6aC1DTiIsImNsaWVudFR5cGUiOiJNT0JJTEUiLCJhcnRpY2xlVmVyc2lvbiI6IiJ9)


ref: [绿联云移动端文件管理][]

[绿联云移动端文件管理]: https://support.ugnas.com/#/detail/eyJpZCI6MjM4LCJ0eXBlIjoidGFnMDAxIiwicGF0aENvZGUiOiJwcm8wMDEsbmo0cHQ3LDgzZWE5MiIsImxhbmd1YWdlIjoiemgtQ04iLCJjbGllbnRUeXBlIjoiTU9CSUxFIiwiYXJ0aWNsZVZlcnNpb24iOiIifQ==


--------------------------------------------------------------------------------

### UGREENlink 远程访问

[UGREENlink][] 是绿联NAS的一项远程访问功能，允许用户通过手机、电脑或网页端随时随地访问家中的 NAS 设备。启用该服务后，无需公网 IP 或复杂的端口转发设置，即可远程管理和访问 NAS 上的文件。

*UGREENlink* 两种服务**访问方式**

- 方式1: 你可通过网页链接实现远程访问，<https://ug.link/DXP2800-01C7-bC9d>
- 方式2: 或在客户端输入 UGREENlink ID (`DXP2800-01C7-bC9d`) 完成登录。
  
  如何查看 UGREENlink ID:
  
  控制面板 → 设备连接 → 远程访问
  <img src="https://drive.google.com/thumbnail?id=1LV2krpn-goZtGN-7x8oEWam1kMpKqQd1&sz=w1000" alt="" style="display: block; margin-right: auto; margin-left: auto; zoom:80%;" />


[UgreenLink quick start][]

[UGREENlink]: https://support.ugnas.com/knowledgecenter/#/detail/eyJ0eXBlIjoidGFnMDAxIiwibGFuZ3VhZ2UiOiJ6aC1DTiIsImlkIjo5MywiY2xpZW50VHlwZSI6IlBDIiwiYXJ0aWNsZVZlcnNpb24iOiIxLjAiLCJwYXRoQ29kZSI6InBybzAwMSx1cmNhYmksZmFsM3ZsLHRsdjZhMixzcjJsdG0ifQ==

[UgreenLink quick start]: https://support.ugnas.com/knowledgecenter/#/detail/eyJpZCI6MzgzMSwidHlwZSI6InRhZzAwMiIsImxhbmd1YWdlIjoiemgtQ04iLCJjbGllbnRUeXBlIjoiUEMiLCJhcnRpY2xlSW5mb0lkIjo2NDEsImFydGljbGVWZXJzaW9uIjoiIiwicGF0aENvZGUiOiIifQ==

--------------------------------------------------------------------------------

## 同步与备份

UGOS Pro 的同步功能支持在本地绿联云与远程绿联云之间进行数据同步。这意味着无论您在哪一台设备上更新数据，其他设备都能自动获取最新版本，保证数据一致性并避免冲突。此外，系统的备份功能让您可以灵活选择备份目标，包括本地绿联云、文件服务器、PC 电脑，甚至是移动设备（如智能手机）。这种多样化的备份选项确保您的数据在各种使用场景下都能得到安全存储，并且可以随时恢复。

<figure style="display: flex; flex-direction: column; align-items: center; text-align: center;">
<img src="https://drive.google.com/thumbnail?id=1Q6Q8Wh4uI66H0dG_kN3DmcadQK7v3HKz&sz=w1000" alt="" style="display: block; margin-right: auto; margin-left: auto; zoom:50%;" />
<figcaption> NAS 同步功能图示。</figcaption>
</figure>

**安装**

打开【应用中心】→ 搜索【同步与备份】→ 点击安装。


### 同步到绿联云 NAS

如何将本地电脑文件同步到绿联云 NAS？

1. 打开【同步与备份】应用，【创建同步任务】。

2. 填写同步规则
   
   基础规则：
   - 电脑路径: 本地你想要同步的文件夹。也叫做计算机路径。
   - 绿联云路径: NAS 云端储存的文件夹。可以选择 个人文件夹 或者 (用户有权限的) 共享文件夹。
     
     <span class="env-orange">不要直接同步到个人文件夹根目录</span>，建议在个人文件夹内新建一个子文件夹作为同步目标。

     因为一个文件夹只能设置一个同步任务，若直接选择个人文件夹根目录，后续无法再添加其他同步任务。
   
   - 路径只能在创建同步任务时选择，创建后不可更改。如需更改，请删除当前任务并重新创建。
   
   - 同步方向: 默认双向同步。可根据需要选择单向同步。
   <img src="https://drive.google.com/thumbnail?id=1B72heq0rOfHoSll5rfATGwoUk47wsfGn&sz=w1000" alt="" style="display: block; margin-right: auto; margin-left: auto; zoom:80%;" />
   
   在【高级设置】中，您可以进一步配置同步任务的细节：

   **文件过滤**

   在“文件过滤”选项中，您可以选择是否同步前缀为“.”的文件和文件夹。默认情况下，系统不会同步这些隐藏文件和文件夹。若需要同步，可手动勾选相应选项。

   您还可以设置过滤不需要同步的文件名或文件扩展名：

   勾选“过滤以下文件名或文件拓展名”选项，并根据需要调整或新增过滤规则。

   要删除某个过滤规则，将鼠标悬停在格式栏上，点击浮动的“X”进行删除。

   如需新增过滤规则，点击“新增”按钮，输入文件名或扩展名。若输入多个，请用“;”隔开。

   **文件冲突**

   当本地文件和远程文件同时被修改时，可能会发生冲突。您可以选择以下处理方式：
   - 保留最新修改的文件并重新命名旧文件（默认选项）
   - 新文件覆盖旧文件

3. 选择同步策略。若要进行同步，必须运行客户端。退出客户端则停止同步。
   - 实时同步
   - 手动同步：仅当手动点击“立即同步”时才进行同步。

4. 预览
   
   查看同步任务的详细信息，确认无误后点击“创建”。由此开始同步。

5. PC 端桌面托盘程序显示：点击 PC 客户端在任务栏的图标，可查看同步与备份应用程序中各文件的传输状态，并可暂停传输中的任务。
   <img src="https://drive.google.com/thumbnail?id=1BLf0GSyU0nhNZUi2CdXzg2havAkbz2iX&sz=w1000" alt="" style="display: block; margin-right: auto; margin-left: auto; zoom:60%;" />

可打开同步与备份 → 日志，查看同步任务的详细信息。

ref: 

- [绿联云UGOS Pro系统与计算机电脑同步](https://www.ugnas.com/tutorial-detail/id-136.html)
- [如何设置绿联云与PC电脑同步](https://developer.aliyun.com/article/1555034)

--------------------------------------------------------------------------------

### 同步到本地电脑

如何将绿联 NAS 文件同步到本地电脑？

如果您还希望在另一台计算机B上同步这些数据，可以在该计算机上安装绿联云客户端，并使用同步功能将计算机路径设置为指定文件夹，绿联云路径依然为共享文件夹A。通过这种设置，计算机B的数据将与 NAS 云端储存的文件夹保持同步。


--------------------------------------------------------------------------------

**支持的同步方式**

- 双向同步： 这种方式下，两个设备之间的文件修改会相互传递，保持文件在所有设备上的一致性。例如，如果你在电脑上编辑了一个文档，NAS 上的相应文件也会被更新。✅

- 单向同步： 同步功能支持仅将本地数据上传至远程和仅将远程数据下载至本地数据，只从一个源设备复制到目标设备，但不会进行反向同步。这种方式适合备份文件，但不适合频繁修改的工作文件。

--------------------------------------------------------------------------------

**同步的使用场景**

- 多设备协作： 在团队合作中，成员们常常使用不同的设备（如台式机、笔记本、手机）来处理相同的文件。UGOS Pro 的同步功能能够自动保持这些文件在所有设备上的一致性。无论是新增、修改，还是删除文件，所有更改都会即时更新到所有连接的设备上，省去了手动更新或复制的麻烦，确保每个人都能访问到最新版本的文件。

- 远程办公： 无论您是在家中、办公室，还是出差在外，UGOS Pro 的同步功能都能帮助您无缝访问和管理数据。通过自动同步，您可以在不同地点继续处理同一套数据，保持工作流的连贯性和效率。这使得远程办公不再受限于地理位置，工作流程得以顺利进行。

- 备份同步： 同步功能不仅是多设备协作的利器，还是一种有效的数据备份手段。您可以在多个 NAS 设备之间进行数据同步，从而实现冗余备份。即使一个设备发生故障，数据也会安全地保存在其他同步的设备上。这样，数据的安全性得到了显著提升，保障了数据的持续可用性。

- 跨平台数据共享： UGOS Pro 支持多平台的设备，如Windows、macOS。这种跨平台的支持使得在不同操作系统之间共享和同步数据变得轻而易举，无论您使用什么设备，都能享受到一致的数据体验。

- 版本控制： 在文件涉及多个版本更新中，UGOS Pro 的同步功能能帮助团队轻松管理和追踪不同文件版本。

--------------------------------------------------------------------------------


Q: 同步时，电脑必须与 NAS 在同一局域网吗？\
A: 不需要。注册并使用 UGREENLink 服务，即使不在局域网内，用户也可以远程访问NAS。这项服务允许用户通过简单的 ID 和密码从任何地点访问绿联NAS。即使在不同的网络环境下，只要有互联网连接，登陆客户端之后，NAS 和电脑之间的同步也可以正常进行。

--------------------------------------------------------------------------------


### 文件版本管理

启用版本保留功能是避免数据冲突的一项关键措施，特别是在多名用户同时修改同一文件时。通过保留多个版本，您可以确保数据的一致性和安全性。绿联 NAS 支持对本地用户个人文件夹和共享文件夹分别进行版本保留。

安装`文件版本管理`应用

1. 前往 绿联云＞应用中心＞文件版本管理，选择【文件版本管理】后点击安装。
2. 安装【文件版本管理】后，可以直接打开应用程序。您也可以在 【主菜单】 中查看应用图标启动该服务。

注意：<span class="env-green">该应用仅管理员用户可操作</span>。

**开启和设置版本保留功能**

1. 前往【同步与备份】应用 > 管理员设置 > 找到【版本保留】选项，点击开启此功能选项。
   <img src="https://drive.google.com/thumbnail?id=1PLRNRrVAy0mE76ER48UPstEfCRouEoVk&sz=w1000" alt="" style="display: block; margin-right: auto; margin-left: auto; zoom:80%;" />
   
   启用后将**自动**为同步任务关联的个人文件夹和共享文件夹开启版本保留功能。默认保留 8 个版本。如果您不想为同步任务关联的文件夹启用版本保留，可前往【同步与备份>管理员设置】关闭“版本保留”，未启用版本保留的文件将无法找回意外删除的文件。
2. 点击【文件版本管理】，可直接跳转至【文件版本管理】应用进行更多设置。
   <img src="https://drive.google.com/thumbnail?id=1sIRqPXoeFjHO27azf4EqRtbmnYZllKPB&sz=w1000" alt="" style="display: block; margin-right: auto; margin-left: auto; zoom:80%;" />
   
   1. 设置：打开“文件版本管理”应用，点击“设置”按钮，进入设置页面，获取系统所有存在的个人文件夹/共享文件夹。

   2. 模糊搜索：系统可根据文件夹名称模糊搜索您需要设置的文件夹。

   3. 版本保留：可开启或者关闭所有文件夹的版本保留。系统默认保留的版本数量为 8 ，最大数量为 32，您可以根据您的需要设置合适的数量。当生成的版本数量超过限制时，将删除更旧的版本。关闭版本保留后，系统将不会保留该共享文件夹任何历史版本，意外删除的文件无法还原，现有的文件历史版本将一并被删除。

   4. 版本数量：当前文件夹设置的版本保留数量，可随时调整，当版本数量由高往低调整时，系统将会删除额外的版本。

   5. 版本占用：已启用版本保留的文件版本占用空间大小。

ref: [文件版本管理](https://support.ugnas.com/#/detail/eyJpZCI6MjgxLCJ0eXBlIjoidGFnMDAxIiwicGF0aENvZGUiOiJwcm8wMDIsYVR0cjlhIiwibGFuZ3VhZ2UiOiJ6aC1DTiIsImNsaWVudFR5cGUiOiJQQyIsImFydGljbGVWZXJzaW9uIjoiIn0=)


## 在线文档

在线文档功能是基于 OnlyOffice 开源项目开发的一款**协同办公应用**。它提供了**多人在线编辑和协作**的功能，能够满足用户的日常办公需求。与传统云文档服务不同，在线文档将用户数据存储在本地 NAS 设备上，这不仅提升了数据安全性，也避免了依赖第三方云服务的局限性。

1. 多人实时协作编辑: 支持多名用户同时在线编辑同一个文档。

2. 在线文档多格式下载: 支持文本文档、电子表格、演示文稿等主流文档格式的下载，E.g., DOC、DOCX、XLS、XLSX、PPT、PPTX.

3. 文档评论和标注: 支持在文档中添加评论和标注，以便进行反馈和讨论。

4. 文档加密保护: 支持对文档进行加密，增强数据的安全性。

5. 文档分享和导出: 可将文档分享给他人，或导出为本地文件

Issue: 在线文档不支持移动设备端，ipad, 手机等，只能在电脑端使用。

--------------------------------------------------------------------------------


## 为亲友设置使用空间

1. 邀请好友注册账户
   <img src="https://drive.google.com/thumbnail?id=1sPcRxqc8IgaiH0UUp4-zGpl8IUue3x2K&sz=w1000" alt="" style="display: block; margin-right: auto; margin-left: auto; zoom:20%;" />
2. 管理员接受申请
3. 分配权限，为用户设置个人文件夹
4. 申请人下载并登录 <a href="https://apps.apple.com/cn/app/绿联云/id6458647408" target="_blank" rel="noopener noreferrer">绿联云 App</a>，使用 UGREENlink ID 和自己在步骤1设置的账号和密码登录 NAS 设备。
   
   UGREENlink ID: `DXP2800-01C7-bC9d`

## 家庭相册

1. 打开应用中心，下载并安装【相册】应用。
2. 两种选项
    
   <ol type='pi'>
      <li><strong>邀请好友上传</strong>
        <p>上传者无需登录 NAS 账号，打开链接即可上传照片和视频。此方案适合快速 <span class="env-green">收集亲友拍摄的照片</span> 和视频，而朋友无须查看共享相册中的内容。</p>
        <p>新建一个相册，点击右上角【···】更多，选择【邀请好友上传】。</p>
        <img src="https://www.ugnas.com/file/collection/2025072115452881.webp" alt="" style="display: block; margin: 0 auto; zoom:50%;" />
      </li>
      <li><span class="env-green" style="font-weight:bold;">共享相册</span>
        <p>好友需下载 <a href="https://apps.apple.com/cn/app/绿联云/id6458647408" target="_blank" rel="noopener noreferrer">绿联云 App</a> 并登录 NAS 账号。注意需要用 UGREENLink ID 登录。<br>
        登录后可浏览、下载、上传照片和视频。此方案是一个共享文件夹，适合亲友之间共享和管理照片和视频。</p>
        <p>点击菜单栏的 ⛭ 进入设置页面 → 选择 【共享图库】→ 在访问权限下，点击【设置权限】，可添加用户。</p>
      </li>
    </ol>



- 相册可以用来分类管理照片，比如按照旅行、节日等主题创建不同的相册。
- 图库则是一个更大的集合，可以包含多个相册，方便统一管理和浏览所有照片。


**备份相册**

IOS设备的文件夹选择：iOS目前只支持备份“相簿” (Albums) 中的内容，包括以下几类：最近项目、自己创建的相簿、第三方应用创建的相簿、共享相簿、来自Mac的相簿（注意：这个选项只有在关闭 iCloud 时才会显示）。 勾选需要备份的相簿后，点击“确定”即可完成设置。




**绿联知识中心文档:**

- [将手机相片备份到绿联云](https://support.ugnas.com/knowledgecenter-h5/#/articleDetail?articleInfoId=480&clientType=MOBILE)
- [邀请好友上传相片](https://support.ugnas.com/knowledgecenter-h5/#/articleDetail?custom=eyJ0eXBlIjoidGFnMDAyIiwibGFuZ3VhZ2UiOiJ6aC1DTiIsImlkIjoxMDg3LCJhcnRpY2xlSW5mb0lkIjozNjcsImNsaWVudFR5cGUiOiJQQyIsImFydGljbGVWZXJzaW9uIjoiIiwicGF0aENvZGUiOiIifQ%3D%3D)
- [共享图库权限设置](https://support.ugnas.com/knowledgecenter/#/detail/eyJpZCI6MzQ0LCJ0eXBlIjoidGFnMDAxIiwicGF0aENvZGUiOiJwcm8wMDIsZXVrZmptLGtrZ3R6YiIsImxhbmd1YWdlIjoiemgtQ04iLCJjbGllbnRUeXBlIjoiUEMiLCJhcnRpY2xlVmVyc2lvbiI6IiJ9)



--------------------------------------------------------------------------------

**映射网络驱动器**

使用 Samba 服务：通过绿联 NAS 提供的 Samba 服务，可以将 NAS 存储映射为 PC 上的网络驱动器。在“我的电脑”中会显示为一个网络位置，用户可以直接对其进行操作，就像本地硬盘一样。

「Samba」是一种**局域网**内基于SMB网络通讯协议的共享文件服务，它为局域网内不同计算机和联网设备之间提供文件资源的共享服务。局域网内通过Samba，其它设备使用 IP 地址和账号密码，可访问设备上的文件数据，进行传输操作。