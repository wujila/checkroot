#### Configuration tutorials of HMA and its variants

Please install and activate only one plugin among the HMA and its variants. In the LSPosed Manager, only the System Framework should be selected as the scope of HMA or its variants. 
After activating, updating, or downgrading the HMA or its variants, please be reminded to reboot the device. 

In HMA or its variants, at least one template should be created first. 
For example, a blacklist template (officially recommended) should be designed, which should include all the applications that should not be detected by others. 
Alternatively, design a whitelist template (user-recommended) that should only include general applications. 

Subsequently, go to the application management tab in HMA or its variants and, for each application that will detect the LRFP environment, do: 

1) Enable hiding; 
2) Select the blacklist or whitelist template you wish to use; and
3) Configure additional invisible or visible applications (corresponding to the blacklist or whitelist mode) if necessary. 

The following operations can be configured dynamically without rebooting the device, configuring in LSPosed Manager, or restarting the specified application. 

- If you want an application to be able to or not be detected by a certain type of application, simply add the application to the template that works for that type of application in the template management of HMA or one of its variants. 
- If you want an application to be able to or not be able to detect certain applications, simply click on the application in the application management of HMA or one of its variants to configure it. 

In fact, it might be better to have a plugin that can hide the app list without manual configuration. Here, we propose the following "cat and mouse" game. 

- Universal Set $U$: All applications
  - Set $S$: Unbootable system applications and bootable critical pre-installed system applications
  - Set $G$: Applications that need to be detected by all applications but do not belong to Set $S$
  - Set $M$: Non-LRFP-environment-detector LRFP applications that require bypassing detections by others (mice)
  - Set $D$: LRFP applications for LRFP environment detection (double roles of cats and mice)
  - Set $C$: Regular Android desktop applications (that are keen on detecting LRFP environments)
    - Subset $C_\textit{CN}$: Regular Android desktop applications released in mainland China
    - Subset $C_\textit{UN}$: All regular Android desktop applications that do not belong to the other subsets of Set $C$

Among them, the variables should satisfy the following relationship, and Set $M$ and Set $D$ together constitute the LRFP applications. 

$$
\begin{cases}
	U = S \cup G \cup M \cup D \cup C \\
	C = \bigcup\limits_{i \in \{\textit{CN}, \textit{UN}, \cdots\}} C_i \\
	\|U\| = \|S\| + \|G\| + \|M\| + \|D\| + \|C\| \\
	\|C\| = \sum\limits_{i \in \{\textit{CN}, \textit{UN}, \cdots\}} \|C_i\|
\end{cases}
$$

For ease of understanding, some possible examples are as follows. 

- Universal Set $U$: This is a non-leaf node
  - Set $S$: ``com.android.settings``
  - Set $G$: ``com.follow.clash``
  - Set $M$: ``io.github.vvb2060.magisk`` and ``bin.mt.plus``
  - Set $D$: ``com.reveny.nativecheck`` and ``com.zhenxi.hunter``
  - Set $C$: This is a non-leaf node
    - Subset $C_\textit{CN}$: ``com.tencent.mm`` and `` com.tencent.mobileqq``
    - Subset $C_\textit{UN}$: ``org.telegram.messenger``

Let $x \rhd y$ represent that $x$ can detect $y$, and $x \not\rhd y$ represent that $x$ cannot detect $y$. Implement the following configurations correspondingly for HMA or one of its variants. 

- $\forall s \in S, s \rhd U, U \rhd s$
- $\forall g \in G, g \rhd U, U \rhd g$
- $\forall m \in M, m \rhd U, S \rhd m, G \rhd m, M \rhd m, D \not\rhd m, C \not\rhd m$
- $\forall d \in D, d \rhd S, d \rhd G, d \not\rhd M, d \rhd d, d \not D - \{d\}, d \rhd C, S \rhd d, G \rhd d, M \rhd d, d \rhd d, D - \{d\} \not\rhd d, C \not\rhd d$
- $\forall c \in C_\textit{CN}, c \rhd S, c \rhd G, c \not\rhd M, c \not\rhd D, c \rhd C_\textit{CN}, c \not\rhd C_\textit{UN}, S \rhd c, G \rhd c, M \rhd c, D \rhd c, C_\textit{CN} \rhd c, C_\textit{UN} \not\rhd c$
- $\forall c \in C_\textit{CN}, c \rhd S, c \rhd G, c \not\rhd M, c \not\rhd D, c \not\rhd C_\textit{CN}, c \rhd C_\textit{UN}, S \rhd c, G \rhd c, M \rhd c, D \rhd c, C_\textit{CN} \not\rhd c, C_\textit{UN} \rhd c$

While people can achieve the above "cat and mouse" game by manually configuring HMA or one of its variants, manual configuration may be a bit cumbersome when new applications are installed, 
or the newly installed applications may be launched before they have been processed, causing problems such as the device being marked. 
Considering the iterations of anti-virus software, if manual configuration is considered the first generation of configuration, 
then the second generation of configuration might be based on cloud databases, the third generation of configuration might be based on the behavioral characteristics of local applications, 
and the fourth generation of configuration might be based on artificial intelligence. 

Currently, [Bypasser](https://github.com/LRFP-Team/Bypasser) offered a possible second-generation configuration implementation. 
If you wish to own a JSON configuration file generated from cloud databases, you can refer to its HMA configuration generation procedure. 

---

#### 隐藏应用列表及其变体配置教程

请在隐藏应用列表及其变体中仅选择一个来安装。在 LSPosed 管理器中，只应选择系统框架作为隐藏应用列表或其变体的作用域。
激活、升级或降级隐藏应用列表或其变体后，请记得重启设备。

在隐藏应用列表或其变体中，应首先创建至少一个模板。例如，应设计一个黑名单模板（官方推荐），其中应包含所有不希望被其它应用程序检测到的应用程序；或者，设计一个白名单模板（用户推荐），其中应仅包含一般的应用程序。

随后，转到隐藏应用列表或其变体中的应用程序管理，对于将检测“LRFP”环境的每个应用程序，执行：

1) 启用隐藏；
2) 选择要使用的黑名单或白名单模板；
3) 如有需要，配置额外不可见或可见的应用程序（分别对应黑名单或白名单模式）。

以下操作可以在无需重启设备、在 LSPosed 管理器中配置、或重新启动指定的应用程序的情况下动态配置。

- 如果您想让某个应用程序可以或不可以被某类应用程序检测到，只需在隐藏应用列表或其变体的模板管理中将该应用程序放入作用于此类应用程序的模板即可。
- 如果您想让某个应用程序可以或不可以检测到某些应用程序，只需在隐藏应用列表或其变体的应用管理中点击该应用程序进行配置即可。

事实上，或许一个不需要手动配置就能够完成应用列表隐藏的插件会更好，我们在此提出以下“猫和老鼠”游戏。

- 全集 $U$：所有应用程序
  - 集合 $S$：无法启动的系统应用和可启动的关键系统预装应用
  - 集合 $G$：不属于标签 $S$ 但需要检测到所有应用程序
  - 集合 $M$：需要过检但不属于集合 $D$ 的 LRFP 应用（老鼠）
  - 集合 $D$：用于 LRFP 环境检测的 LRFP 应用（既猫又鼠的双重身份）
  - 集合 $C$：（热衷于检测 LRFP 环境的）普通安卓桌面应用（猫）
    - 子集 $C_\textit{CN}$：中国大陆地区发布的普通安卓桌面应用
    - 子集 $C_\textit{UN}$：不归属于集合 $C$ 中其余子集合的所有普通安卓桌面应用

其中，各变量应满足如下关系，集合 $M$ 和 集合 $D$ 共同构成 LRFP 应用。

$$
\begin{cases}
	U = S \cup G \cup M \cup D \cup C \\
	C = \bigcup\limits_{i \in \{\textit{CN}, \textit{UN}, \cdots\}} C_i \\
	\|U\| = \|S\| + \|G\| + \|M\| + \|D\| + \|C\| \\
	\|C\| = \sum\limits_{i \in \{\textit{CN}, \textit{UN}, \cdots\}} \|C_i\|
\end{cases}
$$

为了便于理解，一些可能的例子如下。

- 全集 $U$：这是一个非叶子节点
  - 集合 $S$：``com.android.settings``
  - 集合 $G$：``com.follow.clash``
  - 集合 $M$：``io.github.vvb2060.magisk`` 和 ``bin.mt.plus``
  - 集合 $D$：``com.reveny.nativecheck`` 和 ``com.zhenxi.hunter``
  - 集合 $C$：这是一个非叶子节点
    - 子集 $C_\textit{CN}$：``com.tencent.mm`` 和 `` com.tencent.mobileqq``
    - 子集 $C_\textit{UN}$：``org.telegram.messenger``

令 $x \rhd y$ 表达 $x$ 检测到 $y$，$x \not\rhd y$ 表达 $x$ 检测不到 $y$，构造如下配置，并为隐藏应用列表或其变体进行相应地落地。

- $\forall s \in S, s \rhd U, U \rhd s$
- $\forall g \in G, g \rhd U, U \rhd g$
- $\forall m \in M, m \rhd U, S \rhd m, G \rhd m, M \rhd m, D \not\rhd m, C \not\rhd m$
- $\forall d \in D, d \rhd S, d \rhd G, d \not\rhd M, d \rhd d, d \not D - \{d\}, d \rhd C, S \rhd d, G \rhd d, M \rhd d, d \rhd d, D - \{d\} \not\rhd d, C \not\rhd d$
- $\forall c \in C_\textit{CN}, c \rhd S, c \rhd G, c \not\rhd M, c \not\rhd D, c \rhd C_\textit{CN}, c \not\rhd C_\textit{UN}, S \rhd c, G \rhd c, M \rhd c, D \rhd c, C_\textit{CN} \rhd c, C_\textit{UN} \not\rhd c$
- $\forall c \in C_\textit{CN}, c \rhd S, c \rhd G, c \not\rhd M, c \not\rhd D, c \not\rhd C_\textit{CN}, c \rhd C_\textit{UN}, S \rhd c, G \rhd c, M \rhd c, D \rhd c, C_\textit{CN} \not\rhd c, C_\textit{UN} \rhd c$

人们可以在隐藏应用列表或其变体中通过手工配置实现以上“猫和老鼠”游戏，但在新应用安装时，手工配置可能略显繁琐，或新安装的应用在还未处理过检事宜时就已被启动导致设备被标记等不良问题。
考虑对标反病毒软件思想的迭代，如果将手工配置视为第一代配置，那么第二代配置可能是基于云库的，第三代配置则可能是基于本地应用的行为特征，第四代配置则可能是基于人工智能。

目前，[Bypasser 模块](https://github.com/LRFP-Team/Bypasser)提供了一个可能的第二代配置实现，如果你希望拥有一个基于云库下发的 JSON 配置文件，可参阅其 HMA 配置文件生成过程。
