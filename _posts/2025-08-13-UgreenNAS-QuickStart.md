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
- [主页](https://www.ugnas.com/tutorial) > 文档教程 > 教程与问题，点击右侧 `>` 进入知识中心 > 勾选左侧菜单栏中 `应用指南`

Q: What is my NAS IP? \
A: "控制面板"中，找到【网络设置】，点击【网络连接】。可以查看到当前分配给 NAS 设备的 IP 地址。E.g., my IP: `10.0.0.7`.

Q: Which model is my NAS?  
A: 打开【控制面板】→ 点击系统服务中【关于本机】，可以查看到 NAS 的型号和序列号。我的型号为 <span class="env-green">`DXP2800`</span>.

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


--------------------------------------------------------------------------------

## 文件服务

### 文件管理界面概览


**文件目录**

**文件类型**

| **分类**   | **可见性** | **功能说明**       |
| ---------- | ---------- | --------------- |
| 收藏       | 仅个人可见 | 快速访问常用文件夹。通过右键选择“创建快捷方式”可将文件夹添加至收藏夹。 |
| 个人文件夹  | 仅个人可见 | 个人文件夹是用户存放个人文件数据的地方，只有用户本人和管理员能访问里面的内容，确保隐私安全。开启个人文件夹后，用户可以在文件管理中方便地管理和保护自己的文件。支持**自主管理权**，由管理员启用后可隐藏个人文件夹内容。 |
| 共享文件夹  | 设备用户共享 | 显示与设备内其他用户共享的文件和文件夹，支持协作与资源共享。用户可以将文件夹设置为共享状态，方便团队成员访问和协作。|

**工具栏**

<img src="https://drive.google.com/thumbnail?id=1VK2GMEMqJZNHyOECxutHRh0SF_WGnNcS&sz=w1000" alt="工具栏" style="display: block; margin-right: auto; margin-left: auto; zoom:80%;" />

- 12 号: <i class="fa-solid fa-briefcase"></i>

    - **个人文件夹管理：**开启用户或用户组个人文件夹，设定个人文件夹存放位置，个人文件夹自主管理权，使用限额等功能。
    - **分享管理：**文件/文件夹分享管理，您可以将个人文件或个人文件夹分享给此设备内的用户以及外部用户。
    - **共享文件夹管理：**仅管理员可用，用于查看或管理所有共享文件夹权限、容量和存储位置等。
    - **文件收集管理：**管理当前已创建收集文件链接的文件夹。
    - **文件去重：**查找并删除重复文件，释放存储空间。
    - **回收站管理：**文件回收站功能，启用文件夹回收站后可以管理和恢复已删除的文件。

- 13 号: <i class="codicon codicon-settings-gear" aria-hidden="true" style="font-size: 1.2em; vertical-align: middle;"></i>
  
  文件管理的常规设置，权限设置、速度限制。

- 14 号: 切换列表视图或图标视图。
- 15 号: 按名称、大小、类型或日期等进行升序/降序排列。

ref: [文档教程: 绿联云 UGOS Pro 系统文件管理界面概览](https://www.ugnas.com/tutorial-detail/id-104.html)

--------------------------------------------------------------------------------

### 配置文件管理器

登录<span class="env-green">管理员账号</span>，打开【文件管理】应用，点击右上角的设置图标 <span class="codicon codicon-settings-gear dynamic-setting-icon"></span>，进入文件管理设置页面。


<a id="show-hidden-files"></a>
Q: 如何显示隐藏文件 (以`.`开头的文件)？ \
A: 在“常规设置”中找到“隐藏指定文件”选项。取消勾选 “以 . 开头” 选项，并点击“保存”以使设置生效。

<img src="https://drive.google.com/thumbnail?id=1OMgQoO02XAmXeF-DB4ovkGhCZDb8sPFr&sz=w1000" alt="配置文件管理器" style="display: block; margin-right: auto; margin-left: auto; zoom:80%;" />

ref: [知识库: 4. 配置文件管理器](https://support.ugnas.com/knowledgecenter/#/detail/eyJjb2RlIjoiMiYmNDEyIn0=)


--------------------------------------------------------------------------------

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

## <span class="env-green">同步与备份</span>

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
   
   - 选择**同步方向**
     
     默认双向同步。可根据需要选择单向同步。

     点击<a href="#sync-direction">此处</a>了解如何选择同步方向。
   
   <img src="https://drive.google.com/thumbnail?id=1B72heq0rOfHoSll5rfATGwoUk47wsfGn&sz=w1000" alt="" style="display: block; margin-right: auto; margin-left: auto; zoom:80%;" />
   
   在【高级设置】中，您可以进一步配置同步任务的细节：

  <a id="file-filtering"></a>
   **文件过滤**
   
   <img src="https://drive.google.com/thumbnail?id=1_3zwtsr1IxrLEjUmTa1jd91UtnRoiO4R&sz=w1000" alt="文件过滤" style="display: block; margin-right: auto; margin-left: auto; zoom:80%;" />

   在“文件过滤”选项中，您可以选择是否同步前缀为 “.” 的文件和文件夹。默认情况下，系统<span class="env-green">不会同步这些隐藏文件和文件夹</span>。若需要同步，可手动勾选相应选项。

   > 注意：
   > 
   > 某些配置信息的文件或者文件夹，经常以 "." 开头，如 `.gitignore` (git 过滤文件), `.git/` (git 跟踪文件)。
   > 有时候你可能想要备份这些配置文件到绿联云 NAS 上。
   > 
   > 如果您希望这些隐藏文件也能同步到绿联云 NAS，请确保在 “文件过滤” 选项中勾选 “同步前缀为 . 的文件和文件夹”。

   以 "." 开头的文件在绿联云 UGOS Pro 系统种默认隐藏，不会在文件管理器中显示，除非您在文件管理器的设置中取消隐藏这些文件。[↩](#show-hidden-files)

   <hr>

   您还可以设置过滤不**需要同步的文件名或文件扩展名**：

   勾选 “过滤以下文件名或文件拓展名” 选项，并根据需要调整或新增过滤规则。

   要删除某个过滤规则，将鼠标悬停在格式栏上，点击浮动的 “X” 进行删除。

   如需新增过滤规则，点击 “新增” 按钮，输入文件名或扩展名。若输入多个，请用 “;” 隔开。
   
   > 注意：<span class="env-green">不需要输入完整路径</span>，只需输入 **文件(夹)名** 或 **文件扩展名** 即可。

   <hr>
   
   **文件冲突**

   当本地文件和远程文件同时被修改时，可能会发生冲突。您可以选择以下处理方式：
   - 保留最新修改的文件并重新命名旧文件（默认选项）
   - 新文件覆盖旧文件

3. 选择同步策略。
   
   若要进行同步，必须运行客户端。退出客户端则停止同步。
   
   - 实时同步
   - 手动同步：仅当手动点击“立即同步”时才进行同步。

4. 预览
   
   查看同步任务的详细信息，确认无误后点击“创建”。由此开始同步。

5. PC 端桌面托盘程序显示
   
   点击 PC 客户端在任务栏的图标，可查看同步与备份应用程序中各文件的传输状态，并可暂停传输中的任务。
   
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

<a id="sync-direction"></a>
**支持的同步方向**

- **双向同步**: 这种方式下，两个设备之间的文件修改会相互传递，<span style="color: #00CC66;">保持文件在所有设备上的一致性。</span>
  
  例如，如果你在电脑上编辑了一个文档，NAS 上的相应文件也会被更新。✅
  
  适用于同步协作，频繁改动的文件，确保所有设备上的数据始终保持最新状态。

- **单向同步**: 同步功能支持仅将本地数据上传至远程和仅将远程数据下载至本地数据，只从一个源设备复制到目标设备，但不会进行反向同步。这种方式适合备份文件，但不适合频繁修改的工作文件。
  
  **底层逻辑**: 仅将一端的更改应用到另一端，另一端的更改不会影响源设备的数据。只有一端是权威源。

  - 仅将本地电脑数据同步到 NAS: 适用于需要将本地电脑上的数据备份到 NAS 的场景。NAS 作为备份，不参与编辑。本地电脑端为权威数据端。
    
    ✅ 勾选 "删除电脑文件时，NAS 的文件不同步删除"。此为默认选项。

    <span class="env-green">仅上传</span>本地更改到绿联云。

    <span style="color: #00CC66;">影片、照片</span>等大文件备份推荐使用此方式。影片上传后，可删除本地文件，节省电脑存储空间。单向同步 (电脑 → NAS) 确保不会删除 NAS 端的影片。

    Caveat: 若本地文件修改了 folder structure, NAS 端会新增文件夹并重新上传本地移动的文件，但不会删除 NAS 端多余的文件夹。如此会导致 NAS 端有冗余文件，并且文件上传要花时间。后期仍需要手动清理 NAS 端冗余文件夹。

    Solution: 

    1. 登录非同步账号 (管理员账号) 到绿联云客户端。
    2. 进入共享文件夹，修改文件夹结构。
    3. 在本地电脑端，重复步骤 2 中的操作，保持文件夹结构一致。
    4. 重新登录同步账号，继续同步。
   
    此操作避免 NAS 重新上传所有移动的文件，并可避免冗余文件。缺点是同样的文件夹结构需要在两个端 (本地和 NAS) 手动修改并保持一致。

  - 仅将 NAS 数据同步到本地电脑: 适用于需要将 NAS 上的数据备份到本地电脑的场景。NAS 作为权威数据端。本地电脑只拉取 NAS 上的数据。
    
    ✅ 默认删除 NAS 文件时，电脑的文件不同步删除。(保证本地数据安全。尤其是当 NAS 端数据被误删时，本地端仍保留数据。)

    <span class="env-green">仅下载</span>绿联云远程更改。

    绿联云作为共享中心，存储原始数据，本地电脑接收最新副本。本地的修改和删除不会影响绿联云上的数据。

    此单向同步 (NAS → 电脑) 适合多台电脑从同一 NAS 获取数据，避免数据冲突。适合企业或团队办公使用。我个人没有使用过此此单向同步方式。

ref: [如何实现绿联云NAS与本地计算机的数据同步?](https://www.ugnas.com/tutorial-detail/id-124.html)

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

### 我的备份策略

- **主力机**
  
  主要工作电脑 (Nord 16)

  需要同步的个人文件夹 (不需要共享给其他人):

  - 工作文件 (工作相关)
  - 证件扫描件 (身份证, 驾照, 护照等)

  需要同步的共享文件夹 (可能需要共享给其他人):

  - 电影，音乐，电视剧 (个人收藏)
  - 照片备份

- **备用机**

  轻量办公 (MBP 14 小黑)

  在备用机上，新建一个文件夹用于同步主力机的个人文件夹，可以就叫作 `Nord 16`。

  然后在绿联云客户端上，创建同步任务：
  
  - 电脑路径: `~/Documents/Nord 16`
  - 绿联云路径: `/个人文件夹`
  - 同步方向: 双向同步
  - 高级设置
    
    [文件过滤](#file-filtering): 过滤 git 版本控制文件夹/项目，这些文件手动 fetch-merge 同步。
    
    备用机上: 不要用绿联云和 git 同时管理同一个文件夹。否则会有文件覆盖和数据丢失的风险。

  如此主力机上的个人文件夹就会同步到备用机上，包括工作文件和证件扫描件。git 版本控制文件夹在主力机上有备份，但是不会同步到备用机。

--------------------------------------------------------------------------------

Q: 有的文件夹用 Git 版本控制管理，是否会和绿联云 NAS 的同步功能冲突?  
A: 会混乱。为了保险起见，建议下列做法二选一:

- 备用机在绿联云 NAS 的同步任务中，排除 `.git` 控制的文件夹，不同步 Git 版本控制文件夹。

  <span class="env-green">手动同步 Git 版本控制文件夹到另一台电脑上</span>。
  
  有点麻烦，但是没有冲突覆盖风险。✅

  原则是: 不要 让绿联云同步功能管理 Git 版本控制文件夹。

  ‼️ 数据丢失场景描述: A 为主力机，B 为备用机。A 和 B 都启用绿联云双向同步功能，并且同步同一个 Git 版本控制文件夹。有的文件是在 `.gitignore` 里面的，不会被 Git 版本控制管理。但是绿联云同步功能会同步这些文件。当你在 B 上 pull 远程最新代码后，B 会删除一些本地文件 (因为远程最新代码没有这些文件)。然后绿联云双向同步功能会把 B 上删除的文件同步到 A 上，导致 A 上的文件也被删除了。这样就 BBQ 了。🔥

  > <span class="env-green">备用机上</span>: 所有用 Git 版本控制管理的项目，都加入到绿联云同步任务的过滤规则中。  
  > 
  > 直接添加文件夹名称，不需要完整路径。  
  > 
  > <span class="env-green">主力机上不用过滤 Git 版本控制文件夹。</span>这样主力机上可以正常使用绿联云同步功能。  
  > 但是备用机上做了修改后，主力机上不会同步这些修改。
  > 
  > 在备用机上修改 Git 版本控制文件夹时，第一步就是 fetch-merge 最新代码，然后再进行本地修改。
  > 修改完成后，commit-push 到远程 Git 仓库。  
  > 记得主力机也要 fetch-merge 最新代码。


- 或者，两者并行，以 Git 版本控制为主。❌
  
  ‼️ 这种方式<span class="env-orange">数据丢失风险较大</span>，可能会导致 Git 版本控制文件夹被绿联云同步覆盖。
  
  重要文件被覆盖了就 BBQ 了。🤪

  - 强制覆盖本地代码为远程最新代码 (简单粗暴)
    
    手动控制，确保无冲突误删等。麻烦一点，但是保险。GitHub 远程仓库作为最终版本控制中心还是靠谱的。
  
    每次在本地电脑上修改代码后，commit-push 到远程 Git 仓库。然后在另一台电脑上 pull 最新代码。

    Pull 代码时, 可会有警告提示本地文件被修改，是否覆盖等。此时选择覆盖本地修改即可。

    ```bash
    git fetch origin // 获取远程最新代码
    git reset --hard origin/main // 强制覆盖本地代码为远程最新代码
    ```

    This forces your local branch to match the remote branch, discarding any local changes.

    <hr>

  - 暂存本地修改，合并远程修改 (费事但安全一些，避免误删本地修改)
    
    如果你在备用机上也有本地修改未提交，想要先保存这些修改，可以使用 `git stash` 命令暂存本地修改，之后再应用这些修改。
 
    If you want to keep your local changes and merge them with the remote changes, you can stash your changes before pulling:
 
    ```bash
    git fetch origin                // 获取远程最新代码
    git stash                       // 暂存本地修改
    git reset --hard origin/main    // 强制覆盖本地代码为远程最新代码
    git stash pop                   // 恢复本地修改并尝试合并
    ```
 
    If your branch is named something other than `main` (like `master` or `develop`), replace `origin/main` with `origin/your-branch-name`.


  

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

--------------------------------------------------------------------------------

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

邀请好友加入绿联云 NAS 设备。通过邀请功能，管理员可以轻松地为亲友创建账户，共享照片、视频和文件等。

1. 邀请好友注册账户
   
   以管理员身份登录绿联云。
   
   前往【控制面板 > 用户管理 > 邀请】，进入用户邀请向导。绿联云将自动生成邀请二维码或链接，将其发送给邀请用户。
   
   申请人扫描二维码或点击链接，进入注册页面，根据链接要求填写信息，最后点击 “申请加入” 完成注册。

   <img src="https://drive.google.com/thumbnail?id=1sPcRxqc8IgaiH0UUp4-zGpl8IUue3x2K&sz=w1000" alt="" style="display: block; margin-right: auto; margin-left: auto; zoom:20%;" />

2. 管理员接受申请
   
   当用户提交申请后，您可以在【控制面板 > 用户管理 > 邀请 > 用户邀请】页面的申请列表中，查看所有申请信息。

3. 分配权限，为用户设置个人文件夹
   
   点击申请人的信息，进入“用户审批”页面。在此页面，您可以为该申请人添加备注描述和电子邮件，设置用户的角色权限和所属用户组。
   
   您还可以选择是否为用户开启个人空间，让他们拥有独立的存储空间。

   最后，点击 “同意” 以完成用户邀请流程。

4. 申请人下载并登录 <a href="https://apps.apple.com/cn/app/绿联云/id6458647408" target="_blank" rel="noopener noreferrer">绿联云 App</a>
   
   使用 UGREENlink ID 和自己在步骤 1 设置的账号和密码登录 NAS 设备。
   
   UGREENlink ID: `DXP2800-01C7-bC9d`

   <img src="https://drive.google.com/thumbnail?id=1YgnjpHuDLhl7fa4YIfvZwU3veceWc9Qk&sz=w1000" alt="" style="display: block; margin-right: auto; margin-left: auto; zoom:20%;" />

--------------------------------------------------------------------------------

### 管理用户

以管理员身份登录 UGOS Pro 用户管理页面后，您还可以查看和编辑的 UGOS Pro 系统中已创建用户的信息。

若要编辑已创建用户设置，请按照以下步骤操作：

1.  在【控制面板>用户管理】页面，您可以点击该用户头像或者使用搜索框输入用户名以快速查找用户，然后点击该用户以进入用户详细信息页面。

2.  进入用户详细信息页面后，您可以修改用户密码、用户角色，所在用户组、描述、电子邮件，设置文件读写权限和配额限制，开启或关闭用户个人空间，设置是否允许用户修改密码，以及更改用户账号状态或删除用户账号等信息。

ref: [如何邀请他人成为NAS设备用户？](https://www.ugnas.com/play-detail/id-53.html)

--------------------------------------------------------------------------------

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


___

## NAS 加速方案

下载东西（互联网）和与NAS的传输（局域网）速度理论最高只有 120MB/s 左右，实际在 70~100MB/s。如果是无线wifi 还会有损耗（距离、穿墙、设备能力等），5-60 MB/s 甚至更低也很正常。

内网都升级成全2.5G 读写最大从 120 MB 提升到 260 MB 左右。

Mb (Megabit) to MB (Megabyte) 转换公式：8 Mb (传输速度) = 1 MB (文件大小) 

- 路由器/交换机 千兆 (接口为 1000M 或者 1G) 换 2.5G
  
  路由器顺带升级成了 4 个 2.5G的 小米7000。成功升级为了 2.5G 网络（wifi 接 5G 频段）。
  
  买的时候要考虑路由器上面网线插口的数量，最常见的WIFI路由器，一般都是5个网线插口的（其中1个是主线插口WAN + 4个连接设备用的 LAN），但是也有一些产品，精简了插口数量，比如小米的某些型号，总共就只有4个插口，WAN 占据一个，剩下的设备插口就只有3个了，插口数量需求的多少，根据你自家实际情况来判断。
  比如几台电脑、几个电视盒子、还有 NAS 下载器之类的，其中用 WIFI 的可以排除，追求稳定要插网线的就必须算上。

  <img src="https://drive.google.com/thumbnail?id=1i_bsmLDPJF-56kJhLImMMQQr_GMxyaqE&sz=w1000" alt="" style="display: block; margin-right: auto; margin-left: auto; zoom:80%;" />
  
  如果插网线的设备很多，一般就用上网络交换机了，毕竟常见的WIFI一般就只有4个 LAN 口。

- USB 2.5G 网卡
  
  NAS 有线网络直接连接到路由器。
  
  路由器和绿联之间要用 NAS 自带的 7 类网线，绝大部分电脑的网卡都是千兆的，要升级为更高规格的网卡，可以搭配绿联的2.5G外接网卡，C口 A口都有，百十块钱就搞定。


**更换路由器**

先确认你的宽带服务商是否支持更换路由器。有些宽带套餐会赠送路由器，但如果你选择自购路由器，记得提前联系客服确认兼容性。


Q: 如何查看路由器 LAN 口的网速？  
A: 要查看路由器 LAN 口速度，请通过网线将电脑连接到路由器，然后在电脑上查找网络连接状态。在macOS中，可以在“网络偏好设置”的“硬件”选项中查找速率。 

通过路由器的网关IP地址（如192.168.0.1或192.168.1.1）进入管理界面。查看“网络设置”或“WAN口设置”，通常会显示支持的网络带宽类型。

选购路由器时，确保其支持至少 2.5G 的 WAN 和 LAN 端口。

- WAN 口: 连接着宽带猫，网络从这个口进入路由器，影响着你使用路由器的最大网速
- LAN 口: 网线输出口，一般用来连接电脑、电视等设备，影响着你电脑、电视的网速。
  
  比如说，你的宽带是 200M 的，WAN 口是千兆口（1000M），而 Lan 口是百兆的（100M），那么你如果用网线连接电脑、电视，它们依然是百兆的。

- 看无线 WIFI 的速率：这个就是商家在商品标题中给出的速率，如450M、1200M、2600M等。

1. 购买支持 2.5G 或更高网速的路由器/交换机。将连接猫的网线插入路由器的 WAN 口。
   
   如果你家的宽带，没用用到猫；那么就把入户的那根上网网线，直接插在新路由器的 WAN 接口。

2. 登录路由器管理界面
   
   不同厂商的路由器设置页面是不同的，配置页面的网址，一般都写在路由器背面的出厂标签上面（或者说明书上面肯定也有）

   有的路由器，只要是没有进行过初始配置的，你用浏览器打开任意网页，就会自动跳转到配置页面。

   进入配置页面以后，这里有两种可能性，一种可能性是要求输入厂家出厂自带的‘管理员密码’，这个路由器背面标签上面肯定也有写，看一下就知道了（如果是这种情况，输入管理密码进去以后，记得去路由器的设置菜单里面修改一下管理密码，因为出厂密码过于简单，任何人都猜得到），另外一种情况，就是要求你新输入一个管理密码，这里要记得，管理密码不要过于简单了，尽量复杂一点，但是自己也要记住，以后修改路由器用得着。

3. 设置 WAN 口网络连接类型
   
   通过情况下，此时路由器会自动检测“上网方式”，一般需要2-3秒左右的时间；然后我们根据检测结果，进行对应的设置就可以了。

   - 一般家庭宽带都是动态 IP，不需要额外设置，直接点击下一即可。
   - 如果是电信光纤宽带，可能需要设置 PPPoE 拨号，输入网络运营商给你的宽带账号和密码。如果不记得或者丢失了，可以通过拨打运营商的服务热线解决。

4. 设置 WIFI 信息
   
   - 修改 WIFI 名称和密码，建议使用 WPA2-PSK 或 WPA3-PSK 加密方式，确保网络安全。
   
   现在新买的WIFI路由器，一般都是 2.4G 和 5G 双频的，也就是说，在WIFI设置这里，你可能会看到它让你设置2个热点名字和密码，分别设置就是了，把 5G 频率的那个加上一个后缀用来区分，比如分别叫做 my-wifi 和my-wifi-5G，密码可以一样也可以不一样。

   至于使用的时候，优先用 `-5G` 这个热点，因为 5G 频段的传输速度更快，延迟更低。但是 5G 穿墙性能不如 2.4G。


Q: 什么是 猫 (Modem)?  
A: 猫 (Modem) 是调制解调器的简称，它的功能就是使你的电脑通过拨号连接到指定的网络。

<img src="https://drive.google.com/thumbnail?id=11FVzeAfmEaNwnRib1Q5rGiJ-fT3NpqLn&sz=w1000" alt="" style="display: block; margin-right: auto; margin-left: auto; zoom:80%;" />

ref:

- [提升 NAS 带宽](https://zhuanlan.zhihu.com/p/658640504)
- [家里更换无线路由器后怎么设置](https://www.win7sky.com/zhishi/6950.html)

___

## SSD缓存加速

SSD 缓存 (也称为闪存缓存) 可用于提高 (小) 文件的随机读写性能 → 家用场景用处不大。提升家用速度，主要还是靠升级内网速度到 2.5G。

DXP2800 自带两个 M.2 SSD 插槽 (NVMe 2280 SSD)

Q: What does an M.2 SSD do?  
A: M.2 SSDs can be used as a normal storage drive or as a read/write cache to improve reading and writing performance for frequently accessed data.

Q: HDD+SSD 缓存是如何工作的？  
A: 在绿联 NAS 读取数据时，系统会自动将读取的数据缓存至 SSD 中。如果用户再次访问这些数据，系统可以直接从 SSD 获取，显著提升传输速度。而在写入时，数据会先被缓存到 SSD，再逐步转移到 HDD 上，减少用户等待时间，并减轻 HDD 的工作负载。

SSD 缓存在绿联 NAS 中的实际效果

SSD 缓存的应用场景非常广泛，无论是办公室团队需要共享素材、家庭成员分享旅行影集，还是导入大量照片和文件进行索引，SSD 缓存都能有效提升访问速度和用户体验。特别是在搭建虚拟机，与 UGOS Pro系统进行频繁交互时，SSD 缓存都能潜移默化地加快这些操作的响应速度。


[兼容性列表](https://www.ugnas.com/compatible)

[应用指南: 硬盘管理](https://support.ugnas.com/knowledgecenter/#/detail/eyJpZCI6OTUxLCJ0eXBlIjoidGFnMDAxIiwibGFuZ3VhZ2UiOiJ6aC1DTiIsImNsaWVudFR5cGUiOiJQQyIsImFydGljbGVJbmZvSWQiOjMxNCwiYXJ0aWNsZVZlcnNpb24iOiIxLjAiLCJwYXRoQ29kZSI6InBybzAwMSxqb3pyY2kscGc3NDN1In0=)


安装 M.2 SSD 之后，重启 NAS 设备，然后在【存储管理】中配置 SSD 缓存加速。

注意

- Before inserting or removing any hard drive (including M.2 SSDs) / memory module, please power off the system completely: turn off NAS and disconnect it from power supply.
  
  插拔硬盘前要先关机，并断电，以免数据丢失。

- 拆卸 M.2 SSD 时，需要先前往 绿联云 app 移除 SSD 缓存，否则可能导致数据丢失。
  
  即使设备已关机，未正确移除 SSD 可能导致存储空间损毁。因此，确保缓存数据同步完成后，再进行相关操作。



### 支持的 SSD 缓存类型

绿联 NAS 支持通过将频繁访问的小文件缓存至 SSD，提升随机访问性能。系统支持以下两种类型的缓存模式：

1. 只读缓存：

   只读缓存主要用于加速<span class="env-green">数据读取</span>，适合用于处理那些需要被频繁读取，但很少被修改的数据。

   配置要求：至少 1 块 M.2 NVMe SSD，支持 `Basic` 和 `RAID 0`。

   性能作用：提升随机读取速度。

   适用场景：适合经常读取但很少修改的小文件或添加后几乎不再更改的文件，例如共享的学习资料等。

   数据保护机制：只读缓存存储的是数据副本，即使 SSD 损坏，也不会影响原始数据安全。

2. 读写缓存：

   读写缓存是可以同时加速数据<span class="env-green">读取和写入</span>的技术，适合用于处理那些需要被频繁访问，并且经常被修改或编辑的数据。

   配置要求：至少 **2 块 M.2 NVMe SSD**，支持 <span class="env-green">`RAID 1`</span> 与 `RAID 5`。

   性能作用：同时提升随机读写速度，优化整体 I/O 性能。

   适用场景：适用于频繁读写的小型文件块，例如数据库或虚拟机存储等。

   数据保护机制：当缓存降级时，系统会自动停止新的 I/O 操作，并将缓存数据同步至 HDD。同步完成后，即使 SSD 损坏，也不会导致数据丢失。


ref: 

- [HDD+SSD 缓存是如何工作的？](https://support.ugnas.com/knowledgecenter/#/detail/eyJpZCI6MTM0NSwidHlwZSI6InRhZzAwMiIsImxhbmd1YWdlIjoiemgtQ04iLCJjbGllbnRUeXBlIjoiUEMiLCJhcnRpY2xlSW5mb0lkIjo0NDcsImFydGljbGVWZXJzaW9uIjoiMS4wIiwicGF0aENvZGUiOiIifQ==)
- [如何为存储空间创建 SSD 缓存加速？](https://www.ugnas.com/play-detail/id-25.html)

___

## Connect to NAS via SSH

Q: What is SSH?  
A: SSH is a cryptographic network protocol used to securely log into the local NAS. It’s widely used for system administration and automated scripts.

Q: What can I do with SSH on my NAS?  
A: 通过 SSH，用户可以在远程计算机上执行命令、管理文件系统、查看日志等操作。


### Enable SSH on NAS

进入控制面板 > 终机端 > 勾选启用 SSH 服务。设置允许的端口（默认为 22），建议修改为其他端口以防止其暴露在公网，减少遭受恶意攻击的风险。点击 “应用” 使设置生效。

<img src="https://drive.google.com/thumbnail?id=1SQo_lLyJmGtZ3Mr6-hKORtxOa17v3oCT&sz=w1000" alt="" style="display: block; margin-right: auto; margin-left: auto; zoom:80%;" />

### MacOS 通过 SSH 连接 NAS

打开 终端 (Terminal) 应用，输入以下命令：

```bash
ssh -p port username@NAS_IP
例如
ssh -p 22 ugreen_admin@192.168.31.34 
```

将 username 替换成您的管理员账号，将 NAS_IP 替换成您的 NAS ip 地址，port 替换成您的 SSH 端口号。绿联 NAS 的 IP 地址可以通过【控制面板 > 网络设置 ＞ 网络连接】中查看（如LAN1、LAN2）。

输入您的管理员密码验证登录。

> 不要用其他终端模拟软件。Warp 连接失败，但是自带的 Terminal 可以成功连接。

ref:

- [https://nas.ugreen.com/blogs/how-to/connect-nas-ssh-root-access](https://nas.ugreen.com/blogs/how-to/connect-nas-ssh-root-access)
- [终端机 SSH 使用介绍](https://www.ugnas.com/tutorial-detail/id-190.html)

--------------------------------------------------------------------------------

## FAQ

Q: 如何删除共享文件夹? \
A: 打开文件管理器，在对应文件夹右上角选择【共享文件夹管理】<i class="fa-solid fa-briefcase"></i>，点击删除相应文件夹即可。此操作需要管理员权限，并输入管理员密码。

<img src="https://drive.google.com/thumbnail?id=1zJudt-HphRsW_-Gp2Duga8NWQHbQv0Mk&sz=w1000" alt="" style="display: block; margin-right: auto; margin-left: auto; zoom:80%;" />


Q: 如何打开回收站?  
A: 前往文件管理 > 工具图标 <i class="fa-solid fa-briefcase"></i> > [回收站管理](https://www.ugnas.com/tutorial-detail/id-129.html)。