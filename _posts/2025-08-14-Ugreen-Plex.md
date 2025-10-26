---
layout: post
title: Ugreen NAS 影音中心
tag: programming
update: 2025-10-24
---

Q: 如何在电视上观看 NAS 里的影片？

A: 最简单方式是使用 DLNA (Digital Living Network Alliance，数字生活网络联盟)。在 NAS 上开启 DLNA 功能后，支持 DLNA 的设备（如电视、电脑、电视盒等）在局域网内可访问NAS设备上的媒体文件（如音乐、视频、图片等文件数据）。

DLNA 服务不仅支持多种常见的媒体格式，还具有自动发现功能，确保您可以在多个设备上同时访问并控制播放的媒体文件。

<span class="env-orange">注意</span>: DLNA服务启用后，所添加的【媒体资源】将被局域网内其它设备匿名访问，为了您的隐私安全，请谨慎添加个人文件夹或敏感资源。

## Ugreen NAS 开启 DLNA 服务

1. 在应用中心安装 DLNA
2. 打开 DLNA 应用，开启 DLNA 服务，并添加媒体资源路径。

电视端会自动发现 NAS 设备，选择对应的 NAS 设备名称，即可浏览并播放 NAS 上的媒体文件。

限制:

1. DLNA 仅支持局域网内访问，无法通过互联网访问 NAS 上的媒体文件。
2. 安全性较低，所有同一局域网内的设备均可访问 DLNA 服务，建议仅添加公共媒体资源文件夹。

___

## Plex Server

Log in to Plex: <https://app.plex.tv/desktop/#!/>


第二种解决方案为 Docker + Plex Server。主要步骤如下：

1. 安装 Docker
2. 创建 Plex 容器
3. 配置 Plex 服务器
4. 访问 Plex 服务器

使用 Docker 面板安装镜像容器前有哪些准备事项？

在使用 UGOS Pro 的 Docker 面板安装容器之前，需要提前创建容器所需的存储空间文件夹和子文件夹，以确保容器能够顺利运行并且数据能够正确存储和管理。

文件夹目录路径建议选择存放在 `/共享文件夹/docker` 目录内。

Ref: [绿联知识中心 Docker](https://support.ugnas.com/knowledgecenter/#/detail/eyJpZCI6MTEyNCwidHlwZSI6InRhZzAwMiIsImxhbmd1YWdlIjoiemgtQ04iLCJjbGllbnRUeXBlIjoiUEMiLCJhcnRpY2xlSW5mb0lkIjozOTAsImFydGljbGVWZXJzaW9uIjoiMS4wIiwicGF0aENvZGUiOiIifQ==)


**详细步骤**

1. 安装 Docker
   
   在应用中心搜索并安装 Docker 应用。Docker is a platform that enables you to run applications in isolated containers.

2. 安装 Plex 镜像

   在 Docker 应用中，点击 “镜像” 选项卡，搜索 `linuxserver/plex` 镜像并安装。

   Click "Download" to fetch the Plex image. This image will be used to create a container.

3. Create a [Folder Structure](https://support.ugnas.com/knowledgecenter/#/detail/eyJpZCI6MTEyNCwidHlwZSI6InRhZzAwMiIsImxhbmd1YWdlIjoiemgtQ04iLCJjbGllbnRUeXBlIjoiUEMiLCJhcnRpY2xlSW5mb0lkIjozOTAsImFydGljbGVWZXJzaW9uIjoiMS4wIiwicGF0aENvZGUiOiIifQ==) for Plex Data

   Before creating the Plex container, create a folder structure to store Plex data. This structure will help organize your media files and Plex configuration.

   Example folder structure:
   ```
   /共享文件夹/docker/plex/
   ├── config/          # Plex configuration files
   ├── movies/         # Movie files
   ├── tvshows/       # TV show files
   └── music/         # Music files
   ```

4. Set Storage Volumes

   When creating the Plex container, set the storage volumes to map the folders created in the previous step to the appropriate paths inside the container.

   Example volume mappings:
   - `/config` -> `/共享文件夹/docker/plex/config`
   - `/movies` -> `/共享文件夹/docker/plex/movies`
   - `/tvshows` -> `/共享文件夹/docker/plex/tvshows`
   - `/music` -> `/共享文件夹/docker/plex/music`

4. Create Plex Container
   
   在镜像下载完成后，我们开始创建容器，在【镜像 > 本地镜像】的列表中选择刚下载的 linuxserver/plex 镜像。点击 "+" 或双击镜像文件创建容器，配置容器参数。

   **基础信息配置**

   - 在容器创建向导的“基础信息”部分，您可以自定义容器的名称，便于后续识别。
   - 启用【自动重启】选项，以确保容器在系统重启或故障时能够自动恢复运行。
   - 勾选启用【显卡能力】。
   
   <img src="https://drive.google.com/thumbnail?id=1V3gWbaRnAltErdPU2L28Dos5lcaHFpIW&sz=w1000" alt="" style="display: block; margin-right: auto; margin-left: auto; zoom:80%;" />

   **存储空间配置**

   - 点击 `/config` 的自动分配按钮，选择要存放 plex 配置文件 config 的文件夹，类型选择读写。建议选择 NAS 中 `/共享文件夹/docker` 目录下的路径，类型选择“读写”，以防止容器在运行期间因权限不足出现问题。
   - 点击添加，选择存放 `transcode`（转码）的文件夹路径， 装载路径 `/transcode`，类型选择读写。
   - 点击添加，选择存放影片资源的文件夹路径，装载路径 `/video`，类型选择读写。
   
   <img src="https://drive.google.com/thumbnail?id=1YryzzgMZiYTL0DKAy_ftqOjh4kO2jmEo&sz=w1000" alt="" style="display: block; margin-right: auto; margin-left: auto; zoom:80%;" />

   **网络配置**

   设置容器的网络模式和端口映射。推荐使用 `host` 网络模式。

   确保配置信息正确后，**点击 “完成” 创建容器**。

5. 访问容器 Web UI
   
   容器启动后，可以通过浏览器访问容器的Web UI，访问URL `http://<NAS_IP>:32400/web`，将 NAS 的 IP 替换成您的 NAS IP 地址。

   我的地址: `http://10.0.0.7:32400/web`
   
   进入 plex 页面后，进行初始化配置，Plex 页面需要时间加载，才会进入媒体库配置。

   - 第一次载入可使用 Google 账号登录。
   - 服务器设置，全部选择**下一步**。在资料媒体库页面，选择媒体类型（电影、电视剧、音乐等），并添加对应的媒体文件夹路径 on your NAS（如 `/videos`）。 

6. Set up TV Plex Client
   
   在支持 Plex 的电视或设备上安装 Plex 客户端应用, 并登录您的 Plex 账号。 连接到您的 Plex 服务器，浏览并播放存储在 NAS 上的媒体文件。

   支持配对码登录。Enter the Plex Claim Token from <https://www.plex.tv/link/> to link your server to your account.

**Optional Settings:**

Network and Access Settings:

   Configure network settings to allow remote access if desired.
   Set appropriate access permissions for different user profiles.


___

关于 Docker

- 不推荐 SSH 终端操作 Docker。
  
  用户可以使用图形界面进行操作，以避免权限问题和数据不一致的风险。
- 目录挂载与存储位置迁移：请谨慎通过文件管理器修改共享文件夹存储位置。当容器所挂载的文件夹发生存储位置的变化，将导致该容器运行异常。

- 镜像拉取：中国大陆地区的用户可能遇到镜像拉取失败或速度缓慢的问题。可以在镜像配置页面设置加速器或代理以解决此问题。

- 硬盘休眠：使用 Docker 可能影响硬盘的休眠状态，具体取决于您所运行的容器及其活动情况。


___

### 基本操作

Q: 如何修改语言?  
A: [登录 Plex 服务器](https://app.plex.tv/desktop/#!/)，点击右上角的扳手工具 <i class="fa-solid fa-wrench"></i>，选择【Account】->【语言】，选择所需语言并保存更改。

___

### Setting Up Remote Access

Plex Media Server allows you to access your media library from outside your local network.

You will need a Remote Watch Pass subscription (as of April 29, 2025).

Different plans for Plex services: [Plex: Free vs Paid](https://support.plex.tv/articles/202526943-plex-free-vs-paid/)

Manage Subscriptions: <https://account.plex.tv/payments>

- Remote Watch Pass: 2 USD/month

[Remote Streaming with Plex](https://support.plex.tv/articles/200289506-remote-access/?utm_campaign=Plex%20Apps&utm_medium=Plex%20Web&utm_source=Plex%20Apps)


[Accessing a Server through Relay](https://support.plex.tv/articles/216766168-accessing-a-server-through-relay/)

Q: What is Relay?  
A: Your Plex Media Server establishes a secure connection to one of our Relay servers. Your app then also connects securely to the same Relay server and accesses the stream from your Plex Media Server.



ref:

- [Plex: Manual Port Forwards for Multiple Servers](https://support.plex.tv/articles/200931138-troubleshooting-remote-access/)

___


Match Metadata

- Songs: Need to click singer name and then go to the song, click the three dots on the right, then "Match" Metadata.
- Movies/TV Shows: Click the three dots on the right of the title, then choose "Match" Metadata.

___

## Android TV 端

使用场景更广泛适用的是安装客户端，自带「影视中心」app 是最方便。Plex 属于第三方播放器，自定义操作更丰富。客户端的问题是，部分电视品牌不支持直接安装，比如 Samsung TV。

U 盘安装

1. 去官网 <https://nas.ugreen.com/pages/app-download> 找到 Android TV 平台的软件包并下载，接着将软件包保存到 U 盘。
2. 将 U 盘插到电视上，电视会自动弹出提示界面，直接打开 U 盘，然后找到对应的 apk 软件包，点击安装就行，风险警告直接忽略就行。

Issue: You <span class="env-orange">cannot</span> install the UGREEN Android TV client directly on a <span class="env-orange">Samsung TV</span> because Samsung uses its own Tizen OS, not Android.

Workaround: Use DLNA or Plex instead.

### 「影视中心」基本操作

在管理员账号下，打开「影视中心」App，点击右上角 <i class="codicon codicon-settings-gear" aria-hidden="true"></i> 图标，进入设置页面。

**添加媒体库**

左侧服务管理菜单选择【媒体库】，可进行媒体库的添加与管理。

- 点击【添加媒体库】，进入新增媒体库弹窗。
- 对于已有的媒体库，可以点击右侧的 `...` 图标，选择进行管理。

媒体库可以编辑以下选项:

- 媒体库名称：输入您对该媒体库的命名，最长20个字符。
- 媒体库语言：选择媒体库的信息语言。
- 媒体文件夹：选择媒体库关联的 NAS 媒体文件夹，支持添加多个文件夹。
- 元数据刮削：绿联云支持 TMDB 和智能识别，勾选以启用刮削器，长按拖拽可以调整优先级，排序靠前的刮削源优先使用，靠前的源未刮削到的字段则启用靠后的刮削源进行刮削补充。
  
  默认 TMDB 及智能识别都启用，TMDB 排序在前。

___

**扫描媒体库**

用户将视频内容存放到媒体库关联文件夹后，正常情况下，影视中心服务会监听对应文件夹，发起入库动作，但如果您需要更快入库，可以选择手动扫描媒体库，您可操作扫描全部已创建的媒体库或单独的媒体库（入口不同）

1. 在媒体库管理界面选择 "扫描全部媒体库" 或单击右键呼出或选择单个媒体库右上角的 `...` 按钮。
2. 点击扫描媒体库时，弹出浮窗，选择扫描模式：

   - 扫描新添加和修改的：仅针对媒体文件夹中的新内容做扫描和刮削。
   - 扫描全部并补充缺失：遍历媒体库中所有视频文件，对缺失的元数据字段做刮削，获取到则填充上。
   - 完整覆盖：遍历媒体库中所有视频文件，刮削并替换所有视频信息字段。

ref: [绿联 NAS 影视中心媒体库管理](https://www.ugnas.com/tutorial-detail/id-69.html)

___

Ref:

- NAS Compare
  - [Tutorial](https://nascompares.com/guide/how-to-install-plex-media-server-on-a-ugreen-nas/)
  - [Youtube Video](https://youtu.be/hpQuSRBprxk)
- [Ugreen Docker Docker 搭建 plex 流媒体服务](https://support.ugnas.com/knowledgecenter/#/detail/eyJpZCI6MTA2NywidHlwZSI6InRhZzAwMiIsImxhbmd1YWdlIjoiemgtQ04iLCJjbGllbnRUeXBlIjoiUEMiLCJhcnRpY2xlSW5mb0lkIjozNjAsImFydGljbGVWZXJzaW9uIjoiMS4wIiwicGF0aENvZGUiOiIifQ==)
- [The Ultimate Guide for Using NAS for Plex](https://nas.ugreen.com/blogs/how-to/best-nas-for-plex-setup)
- [绿联 NAS 电视端怎么用？一文教会你 4 种技巧](https://post.smzdm.com/p/a2xo0dd2/)