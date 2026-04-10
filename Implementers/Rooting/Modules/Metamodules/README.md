#### Metamodules

Since KernelSU and its variants do not mount system partitions themselves, users need to install metamodules to support rooting-level system modules that require system partition mounting. 
Therefore, compared with other rooting solutions, metamodules are a unique feature of KernelSU and its variants. 

There are many metamodules designed to provide system partition mounting support for rooting-level system modules, with the following three being the main examples. 

- [OverlayFS](https://github.com/KernelSU-Modules-Repo/meta-overlayfs/actions): This is the officially recommended classic metamodule, utilizing the Linux kernel's OverlayFS mechanism for lossless system modification. 
- [Magic Mount](https://github.com/7a72/meta-magic_mount/actions): Based on the traditional Magic Mount logic, this metamodule is suitable for older environments that do not support OverlayFS. 
- [Hybrid Mount](https://github.com/Hybrid-Mount/meta-hybrid_mount/actions): This metamodule works in the hybrid mount mode, but is considered unstable and power-consuming. 

---

#### 元模块

由于 KernelSU 及其变体自身不会挂载系统分区，用户需要安装元模块来支持有系统分区挂载行为的 root 层系统模块。
因此，与其它 root 方案相比，元模块是独属于 KernelSU 及其变体的特性。

用以实现为 root 层系统模块提供系统分区挂载支持的元模块有很多，这里主要列举如下三种。

- [OverlayFS](https://github.com/KernelSU-Modules-Repo/meta-overlayfs/actions)：这是官方推荐的经典元模块，利用 Linux 内核的 OverlayFS 机制进行无损系统修改。
- [Magic Mount](https://github.com/7a72/meta-magic_mount/actions)：基于传统的 Magic Mount 逻辑，该元模块适用于不支持 OverlayFS 的老旧环境。
- [Hybrid Mount](https://github.com/Hybrid-Mount/meta-hybrid_mount/actions)：该元模块以混合挂载模式工作，但目前被认为不稳定且耗电现象明显。
