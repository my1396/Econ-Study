---
layout: post
title: Mac Hard Drives
tag: life
update: 2025-03-30
---

<a class="top-link hide" href="#" id="js-top">↑</a>

## Mac下移动硬盘的分区

Partition to use separately on windows and mac [↩︎](https://www.jianshu.com/p/5f8b4d9a8922)

Mac 下移动硬盘的分区以及 Time Machine 的备份

刚买的移动硬盘大部分都是 NTFS 格式的，Time Machine 备份磁盘最常见的格式是“Mac OS 扩展”格式，但 Time Machine 还支持 “Mac OS 扩展（区分大小写，日志式）” 和 XSan 格式

1.  APFS 格式 (Apple File System)
    
    APFS 是目前最新的苹果文件系统格式，used by macOS 10.13 or later.

2.  Mac OS 扩展日志 格式 (Mac OS Extended (Journaled) )
    
    Mac OS Extended 是苹果在 macOS 10.12 之前使用的主要文件系统格式。
    此格式 mac 专用，这种格式的硬盘在 PC 上不可见，可以用来给 Time Machine 备份。
    
    Time Machine是苹果官方提供电脑备份的方法，用此种方法备份后可完整还原电脑，包括桌面背景，安装软件，各种配置。如果你的电脑容量是 120G，那么最好留出 200G 左右的空间用作备份。Time Machine 会备份最近几个快照。

    > Use a storage device with at least twice the storage capacity of your Mac.  
    > For example, if your Mac has 1TB of storage, your backup disk should ideally have at least 2TB of storage.

3.  MS-DOS (FAT) 格式
    
    此格式通用，PC 和 mac 都可使用，单个文件不能存入 4G 以上的，像镜像比较大的不适合存入，可以存放一些电影，音乐，照片，文档和 mac 上得一些 dmg 软件等等。

4.  NTFS 格式
    
    此格式只适合在 PC 上用，在 mac 上你的权限是只读，就是说只能看，不能进行任何操作，此格式在 mac 上没有.  
    如果要格式化此格式可以用 Windows 系统或者虚拟机，这种格式可以存储 > 4G的文件，也就是说存储文件不受限制。

5.  EXFAT 格式
    
    exfat 格式是一种适合于闪存的文件系统，为了解决 FAT32 等不支持 4G 及更大文件推出，但是使用时发现 EXFAT 兼容性很差。不稳定，不建议使用。


Q: Does Time Machine back up every file every time? [↩︎](https://support.apple.com/en-us/104984)  
A: The first [backup might take longer than you expect](https://support.apple.com/en-us/102184), but you can continue using your Mac while a backup is underway. Time Machine backs up only the files that changed since the previous backup, so future backups will be faster.

Q: Can I pause a Time Machine backup?  
A: If you disconnect your backup disk from your Mac, Time Machine will automatically resume its backup schedule when you reconnect it to your Mac. Before disconnecting your backup disk, either [eject the backup disk](https://support.apple.com/guide/mac-help/mchl027f1d66/mac) or shut down your Mac.


Q: Which file formats does Samsung TV support?  
A: Samsung TV supports FAT, exFAT, and NTFS file formats for external storage devices.


--------------------------------------------------------------------------------

## APFS

Apple File System (APFS) allocates disk space on demand. When a single APFS container (partition) has multiple volumes, the container's free space is shared and can be allocated to any of the individual volumes as needed. Each volume uses only part of the overall container, so the available space is the total size of the container, minus the size of all volumes in the container.

On your computer, macOS is installed on a set of volumes known as a *volume group*. The volume group consists of one volume used for the system files (named Macintosh HD) and another volume used for data (named Macintosh HD - Data).

ref:

- [Add, delete, or erase APFS volumes in Disk Utility on Mac](https://support.apple.com/guide/disk-utility/add-delete-or-erase-apfs-volumes-dskua9e6a110/22.6/mac/15.0)