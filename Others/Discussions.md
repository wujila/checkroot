## Discussions

This document will briefly discuss some reasons for conducting the LRFP. 

### Why Rooting

Ten years ago, Android rooting was seen as a mark of honor that signified advanced technical expertise. 
At that time, manufacturers vied to release one-click root tools. 
Features such as the unfriendly application removal function provided by anti-virus software and the outer screenshot feature in social media were all encouraging users to root their Android devices to unlock these advanced functions. 
That was a flourishing era of everybody rooting. 

Nowadays, device manufacturers are drastically tightening rooting restrictions, and application developers are racking their brains to prevent their apps from running on rooted devices. 
At this time, rooting Android devices is seen as unacceptable, as if people should not have complete control over the phones they buy with their money. 
Anti-virus software is promoting the misconception that rooted devices are more vulnerable, and social media applications silently replace features requiring root privileges with various device environment detections. 
This is an era where Android is only nominally open-source. 

Perhaps, most users believe that modern Android operating systems are already sophisticated enough, eliminating the need for rooting. 
And perhaps, a few of the earlier users are still rooting their Android devices, even though that spellbound era of rooting is over a decade old. 
Of course, some of these users root their devices for gaming cheats—but that is outside the scope of LRFP's discussion. 
If someone asks us why now, we are still rooting? Our answers are here. 

#### Backup and Restore

Even though many modern Android devices come with built-in data migration features, it is still difficult to transfer application data from one Android device to another, especially when the device manufacturers are different. 
More importantly, there are currently no device manufacturers that provide Android devices that can back up application data to a personal computer or mobile terminal without rooting, so that they can be freely restored when needed in the future. 
If your Android device is rooted, it's easy to migrate, back up, and restore contacts, call logs, SMS records, Wi-Fi data, application data, and data under ``/sdcard`` or even ``/data`` to another PC or mobile device. 
Furthermore, on rooted devices, application data can be exported to a location outside the application data directory on the local machine or other devices. If undoing a data change made to an application is needed, just restore the data backed up during its previous state. 
Even more importantly, after migrating, backing up, and restoring data using root privileges, you no longer need to log into each internet application individually or readjust system permissions—this is the convenience we desire. 

#### ``/data`` Management

Outside of ``/sdcard``, the ``/data`` partition stores a lot of data, which is invisible without root privileges. 
This means that if the operating system writes strange folders or files into this blind spot, users will be unaware. 
Furthermore, ``/data/app`` contains many temporary directories for failed installations. These directories begin with ``vmdl`` and contain failed installation packages. 
Each failed installation creates a new folder containing the failed installation package under ``/data/app``. These folders will never be automatically cleaned up. As a matter of fact, they cannot be cleaned by junk cleaners without root privileges. 
This might be one reason why people say Android devices become slow after prolonged use, while iPhones do not. 

Additionally, on some occasions, if the system cannot be booted after updating, users can try to create missing folders under ``/data`` to fix the issue. 

#### Avoiding Superuser Privilege Escalation Vulnerabilities

Currently, most people believe that rooted devices are more vulnerable to attacks. This is certainly true for those who root their devices and install various modules and plugins without reviewing. 
Otherwise, in most cases, the perception that rooted devices are more vulnerable is based on the assumption that ordinary Android desktop application developers want to maintain the integrity of their application data. 
In reality, most users who root their Android devices do not intend to compromise the data integrity of banking applications, or do so for that purpose. 
In recent years, many manufacturers' Android devices have been found to have superuser privilege escalation vulnerabilities. On unrooted phones, attackers can exploit these vulnerabilities to directly escalate privileges to the superuser level and execute dangerous shell code. 
If a user strictly controls their Android device and avoids indiscriminately installing applications, modules, or plugins, a rooted device can actually prevent such vulnerabilities to some extent, thus making it more secure. 

---

## 讨论

本文档将简要讨论执行 LRFP 的一些原因。

### 为什么要切换自定义系统

[https://www.zhihu.com/question/450211822](https://www.zhihu.com/question/450211822)

### 为什么要 root

十年前，root 安卓设备被视为一种荣誉的象征，代表着高超的技术水平。
在那时，各大厂商争相推出一键 root 工具。
反病毒软件的山寨软件卸载、社交软件的外部截屏等都在鼓励用户 root 他们的安卓设备以解锁这些高级的功能。
那是一个全民 root 的繁荣时代。

现如今，设备厂商大幅收紧 root 权限，应用厂商绞尽脑汁防止它们的应用在 root 的设备上运行。
在此时，root 安卓设备被视为一种不被允许的行为，似乎人们就不应该完全掌控他们自己花钱买来的手机。
反病毒软件开始弘扬设备 root 后易受攻击的错误观念，社交媒体软件悄悄移除了需要 root 权限的功能入口，取而代之的，是各种各样的设备环境检测。
这是一个安卓仅在名义上开源的时代。

或许，大部分用户认为，当代的安卓手机系统已经足够完善了，没有 root 的需要。
又或许，少数早期的 root 用户依旧在 root 他们的安卓设备，即使那曾经的辉煌已经过去了十余年。
当然，这部分用户中的一些用户是为了游戏开挂——但这，不属于 LRFP 讨论的范畴。
如果，有人现在问我们，为什么还要 root？我们的答案在这里。

#### 备份还原

即使很多当代的安卓设备均自带了数据迁移功能，但仍难以将应用程序数据从一台安卓设备传输到另一台安卓设备，尤其是设备厂商不同时。
更重要的是，目前未见有设备厂商提供的安卓设备能够在不 root 的情况下通过官方方式将应用数据备份至个人电脑或移动终端以供未来有需之时自由地进行还原。
如果安卓设备已 root，则很容易将联系人、通话记录、短信记录、WiFi、应用数据和 ``/sdcard`` 甚至 ``/data`` 下的数据与另一台个人电脑或移动终端之间相互迁移、备份和还原。
更多地，在已 root 的设备上，应用数据可以导出至本机或其它设备的非应用程序数据目录的位置，若希望撤销某个应用程序的某次数据变更，可以通过变更前的数据进行还原。
甚至，使用 root 权限迁移、备份和还原数据后，不需要再逐个登录互联网应用或再次调整系统权限，这是我们所期望的便利。

#### 管理 ``/data`` 下的目录

在 ``/sdcard`` 外，``/data`` 分区下存储着很多数据，如果没有 root，这部分数据是看不到的。
这意味着，如果操作系统在这个盲区中写入了一些奇怪的文件夹或文件，用户将无法知晓。
此外，``/data/app`` 下会放置很多安装失败的临时目录，这些目录以 ``vmdl`` 开头，里面存储了安装失败的安装包。
每有一次失败的安装，``/data/app`` 下就会多一个带有失败安装包的文件夹。这些文件夹不会被自动清理，事实上，它们也无法被没有 root 权限的垃圾清理程序清理。
这或许就是人们说用安卓手机用久了后会卡，而苹果手机不会的原因之一。

此外，有时如果系统在更新后无法启动，用户可以尝试在 ``/data`` 下创建缺失的文件夹来修复该问题。

#### 避免超级用户提权漏洞

目前，大多数人认为，已 root 的设备更易受攻击。对于 root 后不审核而直接安装各种模块、插件的人而言，这是十分正确的。
否则，在大多数情况下，已 root 的设备更易受攻击往往是建立在普通安卓桌面应用开发者希望自己的应用数据能够保持完整的基础上。
事实上，大部分 root 安卓设备的用户，并没有考虑去破坏银行应用的数据完整性，或者说出于此目的而执行的 root。
近年来，不少厂商的安卓设备被曝有超级用户提权漏洞，在未 root 的手机上，攻击者可以利用漏洞直接提权至超级用户权限以执行危险的 shell 代码。
如果用户是一个严格掌控自己的安卓设备且不乱安装应用程序、模块或插件的人，root 的设备反而能在一定程度上阻止此类漏洞，进而更加安全。
