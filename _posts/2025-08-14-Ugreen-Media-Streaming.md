---
layout: post
title: Ugreen NAS 影音中心
tag: programming
update: 2025-10-24
---

<a class="top-link hide" href="#" id="js-top">↑</a>

视频资源中心

**Useful repos:**

- [磁力熊](https://www.cilixiong.org)
- [YTS](https://yts.unblockninja.com)
- [1337x](https://www.1337x.to/home/)
- [EXT Torrents](https://ext.to)
  
  [GitHub](https://github.com/ext-torrents/ext-torrents.github.io?tab=readme-ov-file)
- [迅雷电影天堂](https://xunlei8.cc)
  
  [镜像1](https://www.xl720.com/thunder/14220.html)

Q: 如何在电视上观看 NAS 里的影片？

A: 最简单方式是使用 DLNA (Digital Living Network Alliance，数字生活网络联盟)。在 NAS 上开启 DLNA 功能后，支持 DLNA 的设备（如电视、电脑、电视盒等）在局域网内可访问 NAS 设备上的媒体文件（如音乐、视频、图片等文件数据）。

DLNA 服务不仅支持多种常见的媒体格式，还具有自动发现功能，确保您可以在多个设备上同时访问并控制播放的媒体文件。

<span class="env-orange">注意</span>: DLNA 服务启用后，所添加的【媒体资源】将被局域网内其它设备匿名访问，为了您的隐私安全，请谨慎添加个人文件夹或敏感资源。

## Ugreen NAS 开启 DLNA 服务

1. 在应用中心安装 DLNA
2. 打开 DLNA 应用，开启 DLNA 服务，并添加媒体资源路径。

电视端会自动发现 NAS 设备，选择对应的 NAS 设备名称，即可浏览并播放 NAS 上的媒体文件。

**限制:**

1. DLNA 仅支持局域网内访问，无法通过互联网访问 NAS 上的媒体文件。
2. 安全性较低，所有同一局域网内的设备均可访问 DLNA 服务，建议仅添加公共媒体资源文件夹。
3. 功能较为基础，缺乏高级媒体管理和播放功能，如海报墙、字幕支持、媒体库管理等。

___

## Plex Server

Log in to Plex: <https://app.plex.tv/desktop/#!/>

Q: What is Plex? What does Plex do?  
A: Plex is a media server platform that allows you to <span class="env-green">access and stream your personal media collection (movies, TV shows, music, photos, etc.) across various devices at home (using Wifi)</span>. Remote access outside your home network requires a Plex Pass subscription.



为了观看 NAS 里存储的影片，第二种解决方案为 Docker + Plex Server。主要步骤如下：

1. 在 NAS 安装 Docker
2. 安装 Plex 镜像
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
   ├── config/         # Plex configuration files
   ├── movies/         # Movie files
   ├── tvshows/        # TV show files
   └── music/          # Music files
   ```

   - Be sure to separate movie and television content into separate main directories. Otherwise Plex may have difficulty correctly identifying your media. Plex uses specific naming conventions to identify and organize media files, so maintaining a clear folder structure is crucial.
   
   - You can have <span class="env-green">subfolders within these main directories</span>. 
     
     E.g., if you chose to categorize your children's content separate from more "adult" content (e.g. `/TV Shows/Kids/ShowName` vs `/TV Shows/Regular/ShowName`), then you would specify `/TV Shows/Kids` as the source location for a "kids" TV library.

     Or you might want to separate movies by genre (e.g. `/Movies/Action`, `/Movies/Comedy`, etc.). In this case, you would specify `/Movies` as the source location for your movie library, and Plex would recursively scan all subfolders within that directory.

     You can create subfolders within these main directories as needed to further organize your media files. This won't recreate the Plex container. Plex will scan all subfolders automatically.


4. Set Storage Volumes

   When creating the Plex container, set the storage volumes to map the folders created in the previous step to the appropriate paths inside the container.

   Example <a href="#volume-mapping"><span class="env-green">volume mappings</span></a>:
   - `/config` -> `/共享文件夹/docker/plex/config`
   - `/movies` -> `/共享文件夹/docker/plex/movies`
   - `/tvshows` -> `/共享文件夹/docker/plex/tvshows`
   - `/music` -> `/共享文件夹/docker/plex/music`
   
   Changing the volume mappings later is possible. However, it will recreate the container and may lead to loss of existing data if not handled carefully.
     
   The parent directory (i.e., `/movies`, `/tvshows`) is what matters when setting up the library in Plex. Plex will recursively scan all subfolders within the specified directory. In other words, it means that you can change the subfolder structure later without needing to adjust the volume mappings, as long as the parent directory remains the same.

5. Create Plex Container
   
   在镜像下载完成后，我们开始创建容器，在【镜像 > 本地镜像】的列表中选择刚下载的 linuxserver/plex 镜像。点击 "+" 或双击镜像文件创建容器，配置容器参数。

   **基础信息配置**

   - 在容器创建向导的“基础信息”部分，您可以自定义容器的名称，便于后续识别。
   - 启用【自动重启】选项，以确保容器在系统重启或故障时能够自动恢复运行。
   - 勾选启用【显卡能力】。
   
   <img src="https://drive.google.com/thumbnail?id=1V3gWbaRnAltErdPU2L28Dos5lcaHFpIW&sz=w1000" alt="" style="display: block; margin-right: auto; margin-left: auto; zoom:80%;" />

   **存储空间配置** (Volume Mapping)

   - 点击 `/config` 的自动分配按钮，选择要存放 plex 配置文件 config 的文件夹，类型选择读写。建议选择 NAS 中 `/共享文件夹/docker` 目录下的路径，类型选择“读写”，以防止容器在运行期间因权限不足出现问题。
   - 点击添加，选择存放 `transcode`（转码）的文件夹路径， 装载路径 `/transcode`，类型选择读写。
   - 点击添加，选择存放影片资源的文件夹路径，装载路径 `/video`，类型选择读写。
   
   <img src="https://drive.google.com/thumbnail?id=1YryzzgMZiYTL0DKAy_ftqOjh4kO2jmEo&sz=w1000" alt="" style="display: block; margin-right: auto; margin-left: auto; zoom:80%;" />

   **网络配置**

   设置容器的网络模式和端口映射。推荐使用 `host` 网络模式。

   确保配置信息正确后，**点击 “完成” 创建容器**。

6. 访问容器 Web UI
   
   容器启动后，可以通过浏览器访问容器的 Web UI，访问URL `http://<NAS_IP>:32400/web`，将 NAS 的 IP 替换成您的 NAS IP 地址。

   我的地址: `http://10.0.0.7:32400/web`
   
   进入 plex 页面后，进行初始化配置，Plex 页面需要时间加载，才会进入媒体库配置。

   - 第一次载入可使用 Google 账号登录。
   - 服务器设置，全部选择**下一步**。在资料媒体库页面，选择媒体类型（电影、电视剧、音乐等），并添加对应的媒体文件夹路径 on your NAS（如 `/videos`）。 

7. Set up TV Plex Client
   
   在支持 Plex 的电视或设备上安装 Plex 客户端应用, 并登录您的 Plex 账号。 连接到您的 Plex 服务器，浏览并播放存储在 NAS 上的媒体文件。

   支持配对码登录。Enter the Plex Claim Token from <https://www.plex.tv/link/> to link your server to your account.

**Optional Settings:**

Network and Access Settings:

   Configure network settings to allow remote access if desired.
   Set appropriate access permissions for different user profiles.


___

<a id="volume-mapping"></a>
Q: What is a <span class="env-green">**volume mapping**</span> in Docker?  
A: Volume mapping in Docker is a way to link directories on the host machine (your NAS) to directories inside the Docker container. 

```
/movies -> /共享文件夹/docker/plex/movies
```

- `/movies`: This is a virtual path inside the Plex container where Plex expects to find movie files. Plex only knows this path, not the host path.
- `/共享文件夹/docker/plex/movies`: This is the real folder (host path) on your NAS where your movie files are stored.

This is how your host folder looks like on your NAS:

```
/共享文件夹/docker/plex/movies/
├── Adult/
│   └── Movie A.mkv
└── Kids/
    └── Movie B.mkv
```

This is how Plex sees the folder structure inside the container:

```
/movies/
├── Adult/
│   └── Movie A.mkv
└── Kids/
    └── Movie B.mkv
```

Plex will scan the `/movies` directory inside the container and find all your movie files, even though they are actually stored on your NAS at `/共享文件夹/docker/plex/movies`.

You can set subfolders for different user groups (e.g., Adult, Kids) or genres (e.g., Action, Comedy) within the main `/movies` directory. Plex will automatically scan all subfolders within the specified directory.

You can change the subfolder structure later without needing to adjust the volume mappings, as long as the parent directory remains the same. No container rebuild, or config change is needed.


___

See [Here](https://english.cool/movie-genres/) for film genres. Refer to [IMDB](https://www.imdb.com/?ref_=tt_nv_home) for genres of specific movies.

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

Q: How to add local subtitles to videos in Plex? 添加字幕  
A: You can enable [**Local Media Assets**](https://support.plex.tv/articles/200220677-local-media-assets-movies/) and then Plex will scan for subtitle files in the same directory as your media files. You may need to refresh metadata.

Supported subtitle file formats: `.srt`, `.smi`, `.ass`, `.ssa`, `.vtt`.

For the video `MovieName (Release Date).mp4`, its subtitle files need to be named as follows:

-   `MovieName (Release Date).[Language_Code].srt` or
-   `Movies/MovieName (Release Date).[Language_Code].srt`
-   `Movies/MovieName (Release Date).[Language_Code].forced.srt`

Need to include the video name file, plus a language code before the file extension. Don't need the square brackets.

Where `[Language_Code]` is defined by the ISO-639-1 (2-letter) or ISO-639-2/B (3-letter) standard.

- English: `en` or `eng`
- Chinese (Simplified): `zh` or `zho`

Examples:

-  Movie file structure with subtitles:

   ```
   Movies/
   ├── /Avatar (2009)
   │   ├──  Avatar (2009).mkv
   │   ├──  poster.jpg
   │   ├──  Avatar (2009).en.srt
   │   └──  Avatar (2009).fr.srt
   ```

-  TV Episodes file structure with subtitles:

   ```
   TV Shows/
   ├── Absolutely Fabulous/
   │   ├── Season 02/
   │       ├── Absolutely Fabulous - s02e03.avi
   │       ├── Absolutely Fabulous - s02e03.eng.smi
   │       └── Absolutely Fabulous - s02e03.en.forced.smi
   ```

   As of server version 1.41.0 using the Plex Series or Plex Movie agents you can put external subtitles in a subtitle directory.

   Must in the same parent directory of the video files.  
   The folder can be named "**subs**" or "**subtitles**"; case insensitive.

   ```
   TV Shows/
   ├── Absolutely Fabulous/
   │   ├── Season 02/
   │       ├── Absolutely Fabulous - s02e03.avi
   │       ├── subtitles/
   │           ├── Absolutely Fabulous - s02e03.eng.smi
   │           └── Absolutely Fabulous - s02e03.en.forced.smi
   ```

Without language code, Plex apps will show “Unknown” instead of the subtitle language and the automatic process which determines if the subtitle should be shown or not will not work as intended.


ref:

- [Plex Quick Start: Adding Local Subtitles to Your Media](https://support.plex.tv/articles/200471133-adding-local-subtitles-to-your-media/)
- [Plex Guide Collection: Using Subtitles](https://support.plex.tv/articles/categories/your-media/using-subtitles/)
- [Wiki: ISO Language Code](https://en.wikipedia.org/wiki/List_of_ISO_639_language_codes)

Q: What does Local Media Assets do? [↩](https://support.plex.tv/articles/200220677-local-media-assets-movies/)  
A: You might have your own image files for movie posters & backgrounds, subtitles, your own movie "extras", etc. To use these, ensure they are named and organized, and that the Local Media Assets source is enabled and ordered correctly.


___

### FAQ

Q: Why Plex is not adding certain movies or TV shows to my library? [↩︎](https://support.plex.tv/articles/201543057-why-is-some-of-my-content-not-found/)  
A: The biggest reason by far for items to not be found during a library scan is due to <span class="env-orange">naming</span>. 

- The movie scanners will skip content that is named like a television episode (including date-based episodes)
- The TV scanners will skip content that is ***not*** named like a television episode

___

Q: What is the convention for naming my media files? [↩︎](https://support.plex.tv/articles/naming-and-organizing-your-tv-show-files/)  
A: For TV Shows, 

- it is recommended to always include the year alongside the series title in folder and file names, e.g. `/Band of Brothers (2001)/Season 01/Band of Brothers (2001) - s01e01 - Currahee.mkv`
- Be sure to use the English word “Season” when creating season directories, even if your content is in another language.
- Many of our naming instructions mention having Optional_Info at the end of the file name and put it in brackets `[]`, e.g. `/Band of Brothers (2001) - s01e01 - Currahee [1080p Bluray].mkv`, whatever you put in the brackets will be ignored by Plex during matching.

The naming is more relaxed for Movies.


Example of how to organize TV Shows:

```
/TV Shows
   /Doctor Who (1963)
      /Season 01
         Doctor Who (1963) - s01e01 - An Unearthly Child (1).mp4
         Doctor Who (1963) - s01e02 - The Cave of Skulls (2).mp4
   /From the Earth to the Moon (1998)
      /Season 01
         From the Earth to the Moon (1998) - s01e01.mp4
         From the Earth to the Moon (1998) - s01e02.mp4
   /Grey's Anatomy (2005)
      /Season 00
         Grey's Anatomy (2005) - s00e01 - Straight to the Heart.mkv
      /Season 01
         Grey's Anatomy (2005) - s01e01 - pt1.avi
         Grey's Anatomy (2005) - s01e01 - pt2.avi
         Grey's Anatomy (2005) - s01e02 - The First Cut is the Deepest.avi
         Grey's Anatomy (2005) - s01e03.mp4
      /Season 02
         Grey's Anatomy (2005) - s02e01-e03.avi
         Grey's Anatomy (2005) - s02e04.m4v
   /The Colbert Report (2005)
      /Season 08
         The Colbert Report (2005) - 2011-11-15 - Elijah Wood.avi
   /The Office (UK) (2001) {tmdb-2996}
      /Season 01
         The Office (UK) - s01e01 - Downsize.mp4
   / The Office (US) (2005) {tvdb-73244}
      /Season 01
         The Office (US) - s01e01 - Pilot.mkv
```

___

### Setting Up Remote Access

Plex Media Server allows you to access your media library from outside your local network.

You will need a Remote Watch Pass subscription (as of April 29, 2025).

Different plans for Plex services: [Plex: Free vs Paid](https://support.plex.tv/articles/202526943-plex-free-vs-paid/)

Manage Plex Pass Subscriptions: <https://account.plex.tv/payments>

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

1. 去官网 <https://nas.ugreen.com/pages/app-download> 找到 Android TV 平台的 apk 软件包并下载，接着将软件包保存到 U 盘。
2. 将 U 盘插到电视上，电视会自动弹出提示界面，直接打开 U 盘，然后找到对应的 apk 软件包，点击安装就行，风险警告直接忽略就行。

Issue: You <span class="env-orange">cannot</span> install the UGREEN Android TV client directly on a <span class="env-orange">Samsung TV</span> because Samsung uses its own Tizen OS, not Android. You need a `tpk` package to install apps on Samsung Smart TVs.

Workaround: 

1. Use DLNA or Plex instead.
2. 电视盒子
   
   电视盒子可支持安装各种应用程序，如视频播放器、游戏等，扩展电视功能。打破智能电视原有系统的限制，比如 Tizen 不支持 安卓 app。


How to change language on Samsung TV? [↩︎](https://www.samsung.com/ie/support/tv-audio-video/how-do-i-change-the-menu-language-on-my-samsung-tv/)



**Enable Unknown Sources on Samsung TV** [↩︎](https://www.partitionwizard.com/partitionmanager/how-to-install-3rd-party-apps-on-samsung-smart-tv.html)

Usually, third-party applications are regarded as unknown sources by the operating system of Smart TV. But you can turn on the Unknown Sources feature on the Samsung Smart TV. This feature allows you to install the apps without limits.

Go to Settings > System > Add-ons > turn on the switch next to **Unknown Sources**


**Enable the Developer Mode** [↩︎](https://developer.samsung.com/smarttv/develop/getting-started/using-sdk/tv-device.html)

1. Settings > Smart Hub 
2. Navigate to the **Apps** section, click on it, and then you will be asked to enter a **pin**. 
   
   Here you can enter **12345** as the pin, which is the default code for all Samsung Smart TVs. The developer mode configuration popup appears.
3. Switch "Developer mode" to "On".
4. Reboot your Smart TV.

   You can turn off the TV by holding the power button for 2 sec, then restart it.

   When you open the "Apps" panel after the reboot, "Developer mode" is marked at the top of the screen.
   <img src="https://developer.samsung.com/media/3649/tv_device_4.png" alt="" style="display: block; margin-right: auto; margin-left: auto; zoom:80%;" />

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

--------------------------------------------------------------------------------

### 添加外挂字幕

**字幕查找网站:**

-   [Zimuku](https://www.zimuku.org/): 以中文字幕为主，适合查找中文或中英双语字幕。✅
-   [SubHD](https://subhd.tv) 中文字幕
    
    [镜像1](subhd.cc)  
    [镜像2](subhd.me)
-   [OpenSubtitles org](https://www.opensubtitles.org/): 最大的字幕资源库之一，主要是英文字幕。
    
    Use [OpenSubtitles com](https://www.opensubtitles.com/) if .org does not work.  
    [dl.opensubtitles](https://dl.opensubtitles.com)
-   [Subscene](https://sub-scene.com): 提供多语种字幕。
-   [YIFY Subtitles](https://yifysubtitles.ch/movie-imdb/tt26270862)
-   [Sub Source](https://subsource.net), [subf2m](https://subf2m.co)
-   [更多字幕网站推荐](https://videoconverter.wondershare.com/subtitle/top-subtitle-download-sites.html)

___

**播放器如何自动识别本地字幕**

- 字幕文件与视频文件需要位于同一文件夹中
- 命名为与视频文件匹配的名称
  - 视频文件名: `Interlaced.Scenes.S01E06.2024.mkv`
    - `S01E06` 表示第一季第六集，此处非常严格，必须包含 `SxxExx` 格式。
      
      <span class="env-orange">`EPx` 不被识别。</span>
    - `2024` 可以放在紧跟视频名后面，如 `Interlaced.Scenes.2024.S01E06.mkv`
  - 直接命名为视频名: `视频文件名.srt`
  - 可选择添加语言代码: `视频文件名.语言代码.srt`


```
TV Shows/Interlaced Scenes (2024)/
├—— Interlaced.Scenes.S01E06.2024.mkv
├—— Interlaced.Scenes.S01E06.2024.srt
├—— Interlaced.Scenes.S01E06.2024.zh-cn.srt
```

- 可手动添加字幕，但是播放器<span class="env-green">无法保留上次播放字幕文件的记忆</span>，每次播放都需要重新选择。比较麻烦。
- 更加容易的方式:
  - 将字幕文件重命名为与视频文件相同的名称并置于同一文件夹内，播放器会自动识别加载字幕。
  - 用视频处理软件，如 mkvtoolnix，内嵌字幕到视频文件中。→ This is called "softsubbing." [↩︎](https://superuser.com/a/609126)
  - use online tool to burn subtitles into video files → This is called "hardsubbing." 这种方式不是很灵活，相当于永久添加字幕，没办法选择不同语言或者关闭字幕。
- 影视中心播放时，可能需要一段时间加载，等二三十秒左右，字幕才会显示出来。

<span class="env-green">**AI prompts**</span> for subtitle management:

> I need to rename and relocate my subtitle files so that my video player can automatically detect them.
>
> **Requirement:**
>
> - put `.srt` in the same directory as .mp4
> - for `video.mp4`, the subtitle should be named as `video.en.srt`
>
> **Instructions:**
>
> - TV shows path: `~/Downloads/tmp/Prison.Break.S01.1080p.BluRay.x265-RARBG`
> - My subtitle files are in `~/Downloads/tmp/Prison.Break.S01.1080p.BluRay.x265-RARBGSubs/episode_name/name.srt` you should match folder name `Subs/episode_name/` and use the first `.srt` files in the folder, rename to match video, then move to the target directory.

`.py` scirpt is in `./script/match_subtitles.py`

```python
python3 script/match_subtitles.py 
  --video-dir "/path/to/show/season" 
  --subs-dir "/path/to/show/season/Subs" 
  --apply
```

Example;

```
python3 "/Users/menghan/Documents/PhD Courses/Econ-Study/script/match_subtitles.py" --video-dir "/Users/menghan/Downloads/tmp/Prison.Break.S01.1080p.BluRay.x265-RARBG" --subs-dir "/Users/menghan/Downloads/tmp/Prison.Break.S01.1080p.BluRay.x265-RARBG/Subs" --apply
```

如果字幕不是很同步，可以调整字幕的时间轴。

- 1s = 1000 ms

ref: 

- [绿联 NAS 影视中心如何在播放器中添加外挂字幕？](https://www.ugnas.com/play-detail/id-60.html)


## 下载中心


[下载中心]((https://support.ugnas.com/knowledgecenter/#/detail/eyJjb2RlIjoiMiYmMTgzIn0=))具有以下功能特点：

- 丰富的下载方式集成：支持**种子（Torrent）、磁链（magnet）**、HTTP、FTP 等多种下载方式，可下载文件、视频、音乐等各类资源。集成 PT（Private Tracker）下载功能，支持私人追踪器的资源管理规则，用户下载后可继续上传做种，维护资源稳定性。
- 多任务同时下载：允许用户同时下载多个文件，高效利用 NAS 的存储和网络资源，提升下载效率。
- 远程管理：通过手机绿联云 APP 实现远程添加和管理下载任务，用户可随时随地操作，不受时间和空间限制。


___

Ref:

- NAS Compare
  - [Tutorial](https://nascompares.com/guide/how-to-install-plex-media-server-on-a-ugreen-nas/)
  - [Youtube Video](https://youtu.be/hpQuSRBprxk)
- [Ugreen Docker Docker 搭建 plex 流媒体服务](https://support.ugnas.com/knowledgecenter/#/detail/eyJpZCI6MTA2NywidHlwZSI6InRhZzAwMiIsImxhbmd1YWdlIjoiemgtQ04iLCJjbGllbnRUeXBlIjoiUEMiLCJhcnRpY2xlSW5mb0lkIjozNjAsImFydGljbGVWZXJzaW9uIjoiMS4wIiwicGF0aENvZGUiOiIifQ==)
- [The Ultimate Guide for Using NAS for Plex](https://nas.ugreen.com/blogs/how-to/best-nas-for-plex-setup)
- [绿联 NAS 电视端怎么用？一文教会你 4 种技巧](https://post.smzdm.com/p/a2xo0dd2/)
- [绿联 NAS 下载中心使用教程](https://support.ugnas.com/knowledgecenter/#/detail/eyJjb2RlIjoiMiYmMTgzIn0=)
