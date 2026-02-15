#### Meta Module

The Meta Module is a feature unique to KernelSU and its branches, which are Android kernel-level rooting hiding techniques based on dynamic loading and unloading of kernel modules. 

- [OverlayFS](https://github.com/KernelSU-Modules-Repo/meta-overlayfs/actions): This is the officially recommended classic meta module, utilizing the Linux kernel's OverlayFS mechanism for lossless system modification. 
- [Hybrid Mount](https://github.com/Hybrid-Mount/meta-hybrid_mount/actions): This  meta module works in the hybrid mount mode. 
- [Magic Mount](https://github.com/7a72/meta-magic_mount/actions): Based on the traditional Magic Mount logic, this meta module is suitable for older environments that do not support OverlayFS. 

---

#### 元模块

由于 KernelSU 及其分支自身不会挂载系统分区，用户需要安装元模块来支持有系统分区挂载行为的 root 层系统模块。因此，元模块是独属于 KernelSU 及其分支的特性。

- [OverlayFS](https://github.com/KernelSU-Modules-Repo/meta-overlayfs/actions)：这是官方推荐的经典元模块，利用 Linux 内核的 OverlayFS 机制进行无损系统修改。
- [Hybrid Mount](https://github.com/Hybrid-Mount/meta-hybrid_mount/actions)：该元模块以混合挂载模式工作。
- [Magic Mount](https://github.com/7a72/meta-magic_mount/actions)：基于传统的 Magic Mount 逻辑，该元模块适用于不支持 OverlayFS 的老旧环境。
