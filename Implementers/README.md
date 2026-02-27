## Implementers

The implementers related to Low-level, Rooting, Zygisk, Riru, and Frameworks are stored here. 

The following tutorial is applicable to the deployment of KernelSU (and its variants), Magisk (and its variants), and Apatch (and its variants) on Android devices. 
For users who wish to deploy KernelSU or one of its variants, please check whether the kernel of the target Android device is a GKI kernel and supported by the rooting solution. 
For users who wish to deploy Magisk (or one of its variants) or Apatch (or one of its variants), 
please check whether the Android version of the target Android device is larger than or equal to the minimum required Android version. 
Throughout the whole tutorials, there is only a computer and an Android device, where the Android device is the one to be rooted. If you have completed a step, please skip it directly. 

- Define
  - The following ``patched_init_boot.img`` refers to the path to the patched ``init_boot`` image file on the computer (please use double quotes to enclose the path if it is necessary)
  - The following ``original_init_boot.img`` refers to the path to the original ``init_boot`` image file on the computer (please use double quotes to enclose the path if it is necessary)
  - The following ``patched_boot.img`` refers to the path to the patched ``boot`` image file on the computer (please use double quotes to enclose the path if it is necessary)
  - The following ``original_boot.img`` refers to the path to the original ``boot`` image file on the computer (please use double quotes to enclose the path if it is necessary)
  - The following ``third_party_recovery.img`` refers to the path to the third-party ``recovery`` image file on the computer (please use double quotes to enclose the path if it is necessary)
  - The following ``original_recovery.img`` refers to the path to the original ``recovery`` image file on the computer (please use double quotes to enclose the path if it is necessary)
- If this is the first time for the target Android device to be rooted
  - Deploy the environments of the latest [platform tools](https://developer.android.com/tools/releases/platform-tools) on the computer and make sure the ``adb`` and ``fastboot`` in the search path(s)
  - Install the corresponding drivers for the target Android device on the computer
  - Boot the target Android device normally into the system and connect it to the computer via a satisfactory USB data cable
  - Unlock the bootloader of the target Android device (this will clear all the data of the target Android device if the status of the bootloader is locked)
    - Enable the developer mode on the target Android device by clicking the system or kernel version at least 5 times
    - Enable the ``allow OEM unlocking`` option in the developer options of the target Android device
    - Reboot the target Android device to the bootloader (the following details will not be repeated in the subsequent steps)
      - If the target Android device supports advanced rebooting, then just reboot to the bootloader via the advanced rebooting menu
      - Otherwise
        - Enable the USB debugging option in the developer options of the target Android device
        - Execute ``adb devices`` on the computer
        - Grant permissions to the computer for adb debugging on the target Android device
        - Execute ``adb reboot bootloader`` on the computer
        - Disable the USB debugging option in the developer options of the target Android device
    - Execute ``fastboot oem unlock`` or ``fastboot flashing unlock`` on the computer (different fastboot versions and Android devices will have different instructions)
    - Reboot the target Android device normally into the system
  - Root the target Android device (please use either one of the following methods)
    - Method 1: By flashing a patched partition image file
      - If KernelSU or one of its variants is used
        - Install and launch the latest root manager on the target Android device
        - Record the kernel version shown in the root manager (note that the Android version indicated at the beginning of the kernel version can be different from the one of the target Android device)
        - Use either one of the following modes to patch and flash the partition image file (the GKI mode will take effect if both modes are used)
          - LKM mode (recommended for those have an ``init_boot`` partition and under this condition there must be an A/B architecture)
            - Prepare the patched ``init_boot.img`` (please use either of the following ways)
              - Patch manually (recommended)
                - Extract the ``init_boot.img`` from the 9008, flashing, or OTA package corresponding to the ROM or the active slot of the target Android device
                - Copy the extracted ``init_boot.img`` to the external storage of the target Android device
                - Turn to the main tab of the root manager on the target Android device
                - If the root manager shows ``Installed`` or ``Not Installed``
                  - Click on the element where the statement ``Installed`` or ``Not Installed`` lays
                  - Click ``Select a file`` in the root manager
                  - Use the file manager to select the ``init_boot.img`` placed in the external storage of the target Android device
                  - Select the recorded kernel version
                  - Click ``Patch`` and wait for the patching procedure to complete
                - Otherwise, please consider using Magisk (or one of its variants) or Apatch (or one of its variants)
                - Find the patched ``init_boot.img`` under the Download directory of the target Android device and copy or move it to the computer
              - Search and fetch a corresponding patched ``init_boot.img`` from the Internet or the ROM variants based on the same original ``init_boot.img``
            - Reboot the target Android device to the bootloader
            - Execute ``fastboot getvar current-slot`` on the computer to view the current active slot
            - Execute ``fastboot flash init_boot_a patched_init_boot.img`` (if ``a`` is active) or ``fastboot flash init_boot_b patched_init_boot.img`` (if ``b`` is active) on the computer
            - Reboot the target Android device normally (by selecting the green ``START`` via +/- and pressing the power key on the target Android device or by executing ``fastboot reboot`` on the computer)
            - If the above flashing command fails, please stop here and consider using the GKI mode, Magisk (or one of its variants), or Apatch (or one of its variants)
            - If the target Android device boots normally into the system
              - Launch the corresponding root manager to check whether the target Android device is rooted
              - If not, please retry, consider using the GKI mode, Magisk (or one of its variants), or Apatch (or one of its variants), or give up rooting (remember to restore to the original partitions)
            - Otherwise
              - Long-press the power key and the volume key(s) accordingly to force the target Android device reboot into the bootloader
              - Execute ``fastboot flash init_boot_a original_init_boot.img`` (if ``a`` is active) or ``fastboot flash init_boot_b original_init_boot.img`` (if ``b`` is active) on the computer
              - Reboot the target Android device normally into the system
              - Retry, consider using the GKI mode, Magisk (or one of its variants), or Apatch (or one of its variants), or give up rooting
          - For the GKI mode, please refer to the subsequent tutorials on how to root the target Android device via Magisk (or one of its variants) or Apatch (or one of its variants) for the first time
      - If the GKI mode of KernelSU (or one of its variants), Magisk (or one of its variants), or Apatch (or one of its variants) is used
        - Install and launch the latest root manager on the target Android device
        - Prepare the patched ``boot.imt`` (please use either of the following ways)
          - Patch manually (recommended)
            - Extract the ``boot.img`` from the 9008, flashing, or OTA package corresponding to the ROM or the active slot of the target Android device
            - Copy the extracted ``boot.img`` to the external storage of the target Android device
            - If patching the ``boot.img`` by KernelSU or one of its variants
              - Turn to the main tab of the root manager on the target Android device
              - If the root manager shows ``Installed`` or ``Not Installed``
                - Click on the element where the statement ``Installed`` or ``Not Installed`` lays
                - Click ``Select a file`` in the root manager
                - Use the file manager to select the ``boot.img`` placed in the external storage of the target Android device
                - Select the recorded kernel version
                - Click ``Patch`` and wait for the patching procedure to complete
              - Otherwise, please consider using Magisk (or one of its variants) or Apatch (or one of its variants)
            - If patching the ``boot.img`` by Magisk or one of its variants
              - Turn to the main tab of the root manager on the target Android device
              - Click the first ``Install`` button in the root manager
              - Click ``Select and patch a file`` in the root manager
              - Use the file manager to select the ``boot.img`` placed in the external storage of the target Android device
              - Click ``Start`` and wait for the patching procedure to complete
            - If patching the ``boot.img`` by Apatch or one of its variants
              - Turn to the main tab of the root manager on the target Android device
              - Click the ``Install`` button in the root manager
              - Click ``Select and patch a file`` in the root manager
              - Use the file manager to select the ``boot.img`` placed in the external storage of the target Android device
              - Embed the Cherish Peekaboo kernel module if you wish to
              - Set a password
              - Click ``Patch`` and wait for the patching procedure to complete
            - Find the patched ``boot.img`` under the Download directory of the target Android device and copy or move it to the computer
          - Patch via an OTA link by Magisk or one of its variants
            - Turn to the main tab of the root manager on the target Android device
            - Click the first ``Install`` button in the root manager
            - Click ``Download and patch an image`` in the root manager
            - Enter the OTA link and confirm
          - Search and fetch a corresponding patched ``boot.img`` from the Internet or the ROM variants based on the same original ``boot.img``
        - Reboot the target Android device to the bootloader
        - If the target Android device runs on the non-A/B architecture
          - Execute ``fastboot boot patched_boot.img`` on the computer
          - If the target Android device boots normally into the system after the above command
            - Execute ``fastboot flash boot patched_boot.img`` on the computer
            - Reboot the target Android device (by selecting the green ``START`` via +/- and pressing the power key on the target Android device or by executing ``fastboot reboot`` on the computer)
            - If the above flashing command fails, please stop here and consider retrying or giving up
            - If the target Android device boots normally into the system
              - Launch the corresponding root manager to check whether the target Android device is rooted
              - If not, please retry or give up rooting (remember to restore to the original partitions)
            - Otherwise
              - Long-press the power key and the volume key(s) accordingly to force the target Android device reboot into the bootloader
              - Execute ``fastboot flash boot original_boot.img`` on the computer
              - Reboot the target Android device normally into the system
              - Retry or give up rooting
          - Otherwise, consider retrying or giving up rooting
        - If the target Android device runs on the legacy A/B architecture
          - Execute ``fastboot getvar current-slot`` on the computer to view the current active slot
          - Execute ``fastboot boot patched_boot.img`` on the computer
          - If the target Android device boots normally into the system after the above command
            - Execute ``fastboot flash boot_a patched_boot.img`` (if ``a`` is active) or ``fastboot flash boot_b patched_boot.img`` (if ``b`` is active) on the computer
            - Reboot the target Android device (by selecting the green ``START`` via +/- and pressing the power key on the target Android device or by executing ``fastboot reboot`` on the computer)
            - If the above flashing command fails, please stop here and consider retrying or giving up
            - If the target Android device boots normally into the system
              - Launch the corresponding root manager to check whether the target Android device is rooted
              - If not, please retry or give up rooting (remember to restore to the original partitions)
            - Otherwise
              - Long-press the power key and the volume key(s) accordingly to force the target Android device reboot into the bootloader
              - Execute ``fastboot flash boot_a original_boot.img`` (if ``a`` is active) or ``fastboot flash boot_b original_boot.img`` (if ``b`` is active) on the computer
              - Reboot the target Android device normally into the system
              - Retry or give up rooting
          - Otherwise, consider retrying or giving up rooting
        - If the target Android device runs on the virtual A/B architecture
          - Execute ``fastboot getvar current-slot`` on the computer to view the current active slot
          - Execute ``fastboot flash boot_a patched_boot.img`` (if ``a`` is active) or ``fastboot flash boot_b patched_boot.img`` (if ``b`` is active) on the computer
          - Reboot the target Android device (by selecting the green ``START`` via +/- and pressing the power key on the target Android device or by executing ``fastboot reboot`` on the computer)
          - If the above flashing command fails, please stop here and consider retrying or giving up
          - If the target Android device boots normally into the system
            - Launch the corresponding root manager to check whether the target Android device is rooted
            - If not, please retry or give up rooting (remember to restore to the original partitions)
          - Otherwise
            - Long-press the power key and the volume key(s) accordingly to force the target Android device reboot into the bootloader
            - Execute ``fastboot flash boot_a original_boot.img`` (if ``a`` is active) or ``fastboot flash boot_b original_boot.img`` (if ``b`` is active) on the computer
            - Reboot the target Android device normally into the system
            - Retry or give up rooting
    - Method 2: Via a third-party recovery (only applicable to Magisk and its variants)
      - Rename the APK of the latest Magisk or one of its variants to ``magisk.zip`` and copy it to the target Android device
      - Find and download the third-party recovery image file (like TWRP and OrangeFox) for the target Android device
      - Reboot the target Android device to the bootloader
      - If the target Android device runs on the virtual A/B architecture
        - Execute ``fastboot getvar current-slot`` on the computer to view the current active slot
        - Try to back up the original recovery partition
        - Execute ``fastboot flash recovery_a third_party_recovery.img`` (if ``a`` is active) or ``fastboot flash recovery_b third_party_recovery.img`` (if ``b`` is active) on the computer
        - Reboot the target Android device (by selecting the red ``RECOVERY`` via +/- and pressing the power key on the target Android device or by executing ``fastboot reboot recovery`` on the computer)
        - If the target Android device boots into the recovery mode and can decrypt the ``/data`` partition after inputting the correct password
          - Flash the OrangeFox ZIP in the third-party recovery if using OrangeFox
          - Flash the ``magisk.zip`` in the third-party recovery
          - Reboot the target Android device normally into the system via the third-party recovery
          - If the target Android device boots normally into the system
            - Launch the corresponding root manager to check whether the target Android device is rooted
            - If not, please retry or give up rooting (remember to restore to the original partitions)
          - Otherwise
            - Long-press the power key and the volume key(s) accordingly to force the target Android device reboot into the bootloader
            - Reboot the target Android device (by selecting the red ``RECOVERY`` via +/- and pressing the power key on the target Android device or by executing ``fastboot reboot recovery`` on the computer)
            - Rename the ``magisk.zip`` on the target Android device to ``uninstall.zip`` in the third-party recovery
            - Flash the ``uninstall.zip`` in the third-party recovery
            - Rename the ``uninstall.zip`` on the target Android device back to ``magisk.zip`` in the third-party recovery
            - Reboot the target Android device normally into the system
            - Retry or give up rooting
        - Otherwise
          - Execute ``fastboot flash recovery_a original_recovery.img`` (if ``a`` is active) or ``fastboot flash recovery_b original_recovery.img`` (if ``b`` is active) on the computer
          - Search another third-party recovery, retry, or give up rooting
      - Otherwise
        - Execute ``fastboot boot third_party_recovery.img`` on the computer to make the target Android device temporarily boot into the recovery mode powered by the third-party recovery
        - If the target Android device boots into the recovery mode and can decrypt the ``/data`` partition after inputting the correct password
          - Flash current TWRP (if using TWRP) or the OrangeFox ZIP (if using OrangeFox) in the third-party recovery and test it if you wish to make the third-party recovery permanent
          - Flash the ``magisk.zip`` in the third-party recovery
          - Reboot the target Android device normally into the system via the third-party recovery
          - If the target Android device boots normally into the system
            - Launch the corresponding root manager to check whether the target Android device is rooted
            - If not, please retry or give up rooting (remember to restore to the original partitions)
          - Otherwise
            - Long-press the power key and the volume key(s) accordingly to force the target Android device reboot into the bootloader
            - Reboot the target Android device (by selecting the red ``RECOVERY`` via +/- and pressing the power key on the target Android device or by executing ``fastboot reboot recovery`` on the computer)
            - Rename the ``magisk.zip`` on the target Android device to ``uninstall.zip`` in the third-party recovery
            - Flash the ``uninstall.zip`` in the third-party recovery
            - Rename the ``uninstall.zip`` on the target Android device back to ``magisk.zip`` in the third-party recovery
            - Reboot the target Android device normally into the system
            - Retry or give up rooting
        - Otherwise, search for another third-party recovery, retry, or give up rooting
  - Remove the USB data cable
- Otherwise (please use either one of the following methods)
  - Method 1: Please refer to either of the methods in the first-time rooting
  - Method 2: Install directly in the root manager that already has root privileges on the target Android device and reboot the target Android device normally into the system (recommended)
  - Method 3: Use [Kernel Flasher](https://github.com/fatalcoder524/KernelFlasher)
    - Install Kernel Flasher on the target Android device
    - Grant root privileges to Kernel Flasher in the root manager that already has root privileges
    - Back up the ``/boot`` partition via Kernel Flasher and copy or move it to the computer
    - Search and download the corresponding AnyKernel3 (AK3) from the GitHub
    - Flash the AK3 via Kernel Flasher (the kernel is in the ``/boot`` partition)
    - Reboot the target Android device normally into the system
    - If the target Android device boots normally into the system
      - Install and launch the latest root manager corresponding to the new kernel to check whether the target Android device is rooted (this may be converted from the LKM mode to the GKI mode)
      - If not, please try other methods to root the target Android device
    - Otherwise
      - Long-press the power key and the volume key(s) accordingly to force the target Android device reboot into the bootloader
      - Deploy the environments of the latest [platform tools](https://developer.android.com/tools/releases/platform-tools) and make sure the commands ``adb`` and ``fastboot`` in the search path(s)
      - Install the corresponding drivers for the target Android device on the computer
      - Execute ``fastboot flash original_boot.img`` on the computer
      - Reboot the target Android device normally into the system
      - Use other methods to root the target Android device

The compatibility analysis of some implementations and modules is as follows, where "Y" means compatible and "N" means incompatible. 

| Compatibility | Official Magisk and all variants of KSU | Magisk Alpha | Apatch | Zygisk Next | ReZygisk | NeoZygisk | Shamiko | NoHello | Zygisk Assistant |
| - | - | - | - | - | - | - | - | - | - |
| Official Magisk and all variants of KSU | - | N | N | Y | Y | Y | Y | Y | Y |
| Magisk Alpha | N | - | N | Y | N | Y | Y | Y | Y |
| Apatch | N | N | - | Y | Y | Y | N | Y | Y |
| Zygisk Next | Y | Y | Y | - | N | N | Y | Y | Y |
| ReZygisk | Y | N | Y | N | - | N | Y | Y | Y |
| NeoZygisk | Y | Y | Y | N | N | - | N | N | Y |
| Shamiko | Y | Y | N | Y | Y | N | - | N | Y |
| NoHello | Y | Y | Y | Y | Y | N | N | - | N |
| Zygisk Assistant | Y | Y | Y | Y | Y | Y | Y | N | - |

Therefore, there are the following collocations (partly), where "P" means passed and "F" means failed. For detailed steps of bypassing, please refer to [Bypassers](../Bypassers/README.md). 

| Combination | Native Root Detector | Native Test |
| - | - | - |
| Magisk Alpha + Zygisk Next + PIF + TS + VBMeta Fixer | F | F |
| Magisk Alpha + Zygisk Next + NoHello + PIF + TS + VBMeta Fixer | P | F |
| Magisk Alpha + Zygisk Next + Shamiko + PIF + TS + VBMeta Fixer | P | P |
| Magisk Alpha + Zygisk Next + Shamiko + Zygisk Assistant (Denylist configured) + PIF + TS + VBMeta Fixer | P | F |
| Magisk + Zygisk Next + Shamiko + Zygisk Assistant (Denylist configured) + PIF + TS + VBMeta Fixer | F | F |
| Magisk Alpha + built-in Zygisk + Shamiko + Zygisk Assistant (Denylist configured) + PIF + TS + VBMeta Fixer | P | F |
| Magisk Alpha + built-in Zygisk + Shamiko + PIF + TS + VBMeta Fixer | P | F |
| Magisk Alpha + built-in Zygisk + NoHello + PIF + TS + VBMeta Fixer | P | F |
| Magisk Alpha + built-in Zygisk + PIF + TS + VBMeta Fixer | F | F |
| Magisk Alpha + NeoZygisk + PIF + TS + VBMeta Fixer | F | F |
| Magisk Alpha + NeoZygisk + Zygisk Assistant (Denylist configured) + PIF + TS + VBMeta Fixer | P | F |

It is worth noting that Zygisk Next integrates most of Shamiko's functionalities starting from version 1.3.0 and is compatible with all root implementations. 
Currently, SukiSU Ultra or Magisk Alpha, with Zygisk Next 1.3.0 or higher versions, may be the optimal upstream setup. 

---

## 部署工具

与底层、root、Zygisk、riru 和框架相关的部署工具在此处存储。

以下教程适用于在安卓设备上部署 KernelSU 及其变体、Magisk  及其变体和 Apatch 及其变体。对于希望部署 KernelSU 或其变体之一的用户，请检查目标安卓设备的内核是否为通用内核映像并被 root 方案支持。
对于希望部署 Magisk（或其变体之一）或 Apatch（或其变体之一）的用户，请检查目标安卓设备的安卓版本是否达到最低的安卓版本要求。
教程全文仅提及一台计算机和一台安卓设备，其中的安卓设备即为目标安卓设备。如果某个步骤已被完成，请直接跳过。

- 定义
  - 下文的 ``patched_init_boot.img`` 代指位于计算机中的修补后的 ``init_boot`` 镜像文件路径（请在必要时在路径两端添加一对英文双引号）
  - 下文的 ``original_init_boot.img`` 代指位于计算机中的原始的 ``init_boot`` 镜像文件路径（请在必要时在路径两端添加一对英文双引号）
  - 下文的 ``patched_boot.img`` 代指位于计算机中的修补后的 ``boot`` 镜像文件路径（请在必要时在路径两端添加一对英文双引号）
  - 下文的 ``original_boot.img`` 代指位于计算机中的原始的 ``boot`` 镜像文件路径（请在必要时在路径两端添加一对英文双引号）
  - 下文的 ``third_party_recovery.img`` 代指位于计算机中的第三方 ``recovery`` 镜像文件路径（请在必要时在路径两端添加一对英文双引号）
  - 下文的 ``original_recovery.img`` 代指位于计算机中的原始 ``recovery`` 镜像文件路径（请在必要时在路径两端添加一对英文双引号）
- 如果这是首次 root 目标安卓设备（不是指人的首次操作）
  - 在计算机上部署最新的 [platform tools](https://developer.android.com/tools/releases/platform-tools) 环境并确保 ``adb`` 和 ``fastboot`` 在搜索路径中
  - 在计算机上为目标安卓设备安装相应的驱动
  - 启动目标安卓设备使其正常进入系统并使用一条优质的 USB 数据线将计算机和目标安卓设备进行连接
  - 为目标安卓设备解锁 bootloader（将 bootloader 从锁定状态变成解锁状态会清空目标安卓设备上的所有数据）
    - 通过至少 5 次连续点击系统版本或内核版本来为目标安卓设备启用开发者模式
    - 在目标安卓设备中的开发者选项里启用``允许 OEM 解锁``
    - 重启目标安卓设备到 bootloader（在后续步骤中以下细节不再赘述）
      - 如果目标安卓设备支持高级重启，那么可以直接通过高级重启菜单重启目标安卓设备到 bootloader
      - 否则
        - 在目标安卓设备中的开发者选项里启用 USB 调试选项
        - 在计算机上执行 ``adb devices``
        - 在目标安卓设备中允许计算机执行 adb 调试
        - 在计算机上执行 ``adb reboot bootloader``
        - 在目标安卓设备中的开发者选项里停用 USB 调试选项
    - 在计算机上执行 ``fastboot oem unlock`` 或 ``fastboot flashing unlock``（不同的 fastboot 版本和安卓设备会有不同的指令）
    - 重启目标安卓设备使其正常进入系统
  - Root 目标安卓设备（请使用下列方法中的任一方法）
    - 方法 1：通过刷入一个修补后的分区镜像文件
      - 如果使用的是 KernelSU 或其变体之一
        - 在目标安卓设备上安装并启动最新版 root 管理器
        - 记录 root 管理器中显示的内核版本（注意内核版本起始位置指示的安卓版本可以和目标安卓设备的安卓版本不同）
        - 使用以下模式中的任一模式来修补和刷入分区镜像文件（如果同时使用了两个模式则以 GKI 模式为准）
          - LKM 模式（推荐有 ``init_boot`` 分区的安卓设备使用，在此条件下，该安卓设备一定是 A/B 架构）
            - 准备修补后的 ``init_boot.img``（请使用下列方式中的任一方式）
              - 手动修补（推荐）
                - 从对应于目标安卓设备 ROM 或活动槽位的 9008 包、线刷包或全量包（卡刷包）中提取 ``init_boot.img``
                - 将提取的 ``init_boot.img`` 复制到目标安卓设备的外部存储中
                - 在目标安卓设备上转到 root 管理器的首页
                - 如果 root 管理器显示``已安装``或``未安装``
                  - 点击显示``已安装``或``未安装``文字所在的元素
                  - 在 root 管理器中点击``选择一个文件``
                  - 使用文件管理器选择放置在目标安卓设备的外部存储中的 ``init_boot.img``
                  - 选择之前记录的内核版本
                  - 点击``修补``并等待修补过程完成
                - 否则，请考虑使用 Magisk（或其变体之一）或 Apatch（或其变体之一）
                - 在目标安卓设备的下载目录下找到修补后的 ``init_boot.img`` 并复制或移动它到计算机上
              - 从互联网或基于同一原始 ``init_boot.img`` 的 ROM 的变体中搜索并获取一个对应的修补后的 ``init_boot.img``
            - 重启目标安卓设备到 bootloader
            - 在计算机上执行 ``fastboot getvar current-slot`` 来查看当前的活动槽位
            - 在计算机上执行 ``fastboot flash init_boot_a patched_init_boot.img``（如果槽位 A 活跃）或 ``fastboot flash init_boot_b patched_init_boot.img``（如果槽位 B 活跃）
            - 重启目标安卓设备使其正常进入系统（在目标安卓设备上通过音量 +/- 键选中绿色的 ``START`` 并按下电源键或在计算机上执行 ``fastboot reboot``）
            - 如果上述刷入命令失败，请在此停止并考虑使用 GKI 模式、Magisk（或其变体之一）或 Apatch（或其变体之一）
            - 如果目标安卓设备能够正常进入系统
              - 启动相应的 root 管理器并检查目标安卓设备是否已成功 root
              - 如未 root，请重试，考虑使用 GKI 模式、Magisk（或其变体之一）或 Apatch（或其变体之一），或放弃 root（请记得将全部分区还原为原始分区）
            - 否则
              - 根据目标安卓设备长按电源键和音量键来强制目标安卓设备重启进入 bootloader
              - 在计算机上执行 ``fastboot flash init_boot_a original_init_boot.img``（如果槽位 A 活跃）或 ``fastboot flash init_boot_b original_init_boot.img``（如果槽位 B 活跃）
              - 重启目标安卓设备使其正常进入系统
              - 重试，考虑使用 GKI 模式、Magisk（或其变体之一）或 Apatch（或其变体之一），或放弃 root
          - 对于 GKI 模式，请参阅后续有关如何通过 Magisk（或其变体之一）或 Apatch（或其变体之一）首次 root 目标安卓设备的教程
      - 如果使用的是 KernelSU（或其变体之一）的 GKI 模式、Magisk（或其变体之一）或 Apatch（或其变体之一）
        - 在目标安卓设备上安装并启动最新版 root 管理器
        - 准备修补后的 ``boot.img``（请使用下列方式中的任一方式）
          - 手动修补（推荐）
            - 从对应于目标安卓设备 ROM 或活动槽位的 9008 包、线刷包或全量包（卡刷包）中提取 ``boot.img``
            - 将提取的 ``boot.img`` 复制到目标安卓设备的外部存储中
            - 如果通过 KernelSU 或其变体之一来修补 ``boot.img``
              - 在目标安卓设备上转到 root 管理器的首页
              - 如果 root 管理器显示``已安装``或``未安装``
                - 点击显示``已安装``或``未安装``文字所在的元素
                - 在 root 管理器中点击``选择一个文件``
                - 使用文件管理器选择放置在目标安卓设备的外部存储中的 ``boot.img``
                - 选择之前记录的内核版本
              - 否则，请考虑使用 Magisk（或其变体之一）或 Apatch（或其变体之一）
            - 如果通过 Magisk 或其变体之一来修补 ``boot.img``
              - 在目标安卓设备上转到 root 管理器的首页
              - 点击 root 管理器中的第一个``安装``按钮
              - 点击 root 管理器中的``选择并修补文件``
              - 使用文件管理器选择放置在目标安卓设备的外部存储中的 ``boot.img``
              - 点击``开始``并等待修补过程完成
            - 如果通过 Apatch 或其变体之一来修补 ``boot.img``
              - 在目标安卓设备上转到 root 管理器的首页
              - 点击 root 管理器中的``安装``按钮
              - 点击 root 管理器中的``选择并修补文件``
              - 使用文件管理器选择放置在目标安卓设备的外部存储中的 ``boot.img``
              - 如有需要可嵌入 Cherish Peekaboo 内核模块
              - 设置密码
              - 点击``修补``并等待修补过程完成
            - 在目标安卓设备的下载目录下找到修补后的 ``boot.img`` 并复制或移动它到计算机上
          - 通过 Magisk 或其变体之一的 OTA 链接下载并修补镜像
            - 在目标安卓设备上转到 root 管理器的首页
            - 点击 root 管理器中的第一个``安装``按钮
            - 点击 root 管理器中的``下载并修补映像``
            - 输入 OTA 链接并确认
          - 从互联网或基于同一原始 ``boot.img`` 的 ROM 的变体中搜索并获取一个对应的修补后的 ``boot.img``
        - 重启目标安卓设备到 bootloader
        - 如果目标安卓设备在 non-A/B 架构上运行
          - 在计算机上执行 ``fastboot boot patched_boot.img``
          - 如果目标安卓设备在执行上述命令后正常启动进入系统
            - 在计算机上执行 ``fastboot flash boot patched_boot.img``
            - 重启目标安卓设备使其正常进入系统（在目标安卓设备上通过音量 +/- 键选中绿色的 ``START`` 并按下电源键或在计算机上执行 ``fastboot reboot``）
            - 如果上述刷入命令失败，请在此停止并考虑重试或放弃
            - 如果目标安卓设备能够正常进入系统
              - 启动相应的 root 管理器并检查目标安卓设备是否已成功 root
              - 如未 root，请重试或放弃 root（请记得将全部分区还原为原始分区）
            - 否则
              - 根据目标安卓设备长按电源键和音量键来强制目标安卓设备重启进入 bootloader
              - 在计算机上执行 ``fastboot flash boot original_boot.img``
              - 重启目标安卓设备使其正常进入系统
              - 重试或放弃 root
          - 否则，请考虑重试或放弃 root
        - 如果目标安卓设备在 legacy A/B 架构上运行
          - 在计算机上执行 ``fastboot getvar current-slot`` 来查看当前的活动槽位
          - 在计算机上执行 ``fastboot boot patched_boot.img``
          - 如果目标安卓设备在执行上述命令后正常启动进入系统
            - 在计算机上执行 ``fastboot flash boot_a patched_boot.img``（如果槽位 A 活跃）或 ``fastboot flash boot_b patched_boot.img``（如果槽位 B 活跃）
            - 重启目标安卓设备使其正常进入系统（在目标安卓设备上通过音量 +/- 键选中绿色的 ``START`` 并按下电源键或在计算机上执行 ``fastboot reboot``）
            - 如果上述刷入命令失败，请在此停止并考虑重试或放弃
            - 如果目标安卓设备能够正常进入系统
              - 启动相应的 root 管理器并检查目标安卓设备是否已成功 root
              - 如未 root，请重试或放弃 root（请记得将全部分区还原为原始分区）
            - 否则
              - 根据目标安卓设备长按电源键和音量键来强制目标安卓设备重启进入 bootloader
              - 在计算机上执行 ``fastboot flash boot_a original_boot.img``（如果槽位 A 活跃）或 ``fastboot flash boot_b original_boot.img``（如果槽位 B 活跃）
              - 重启目标安卓设备使其正常进入系统
              - 重试或放弃 root
          - 否则，请考虑重试或放弃 root
        - 如果目标安卓设备在 virtual A/B 架构上运行
          - 在计算机上执行 ``fastboot getvar current-slot`` 来查看当前的活动槽位
          - 在计算机上执行 ``fastboot flash boot_a patched_boot.img``（如果槽位 A 活跃）或 ``fastboot flash boot_b patched_boot.img``（如果槽位 B 活跃）
          - 重启目标安卓设备使其正常进入系统（在目标安卓设备上通过音量 +/- 键选中绿色的 ``START`` 并按下电源键或在计算机上执行 ``fastboot reboot``）
          - 如果上述刷入命令失败，请在此停止并考虑重试或放弃
          - 如果目标安卓设备能够正常进入系统
            - 启动相应的 root 管理器并检查目标安卓设备是否已成功 root
            - 如未 root，请重试或放弃 root（请记得将全部分区还原为原始分区）
          - 否则
            - 根据目标安卓设备长按电源键和音量键来强制目标安卓设备重启进入 bootloader
            - 在计算机上执行 ``fastboot flash boot_a original_boot.img``（如果槽位 A 活跃）或 ``fastboot flash boot_b original_boot.img``（如果槽位 B 活跃）
            - 重启目标安卓设备使其正常进入系统
            - 重试或放弃 root
    - 方法 2：通过第三方恢复（仅对 Magisk 及其变体生效）
      - 将最新版 Magisk 或其变体之一的 APK 重命名为 ``magisk.zip`` 并复制到目标安卓设备上
      - 为目标安卓设备查找并下载第三方恢复镜像文件（例如 TWRP 和 OrangeFox）
      - 重启目标安卓设备到 bootloader
      - 如果目标安卓设备在 virtual A/B 架构上运行
        - 在计算机上执行 ``fastboot getvar current-slot`` 来查看当前的活动槽位
        - 尝试备份原始恢复分区
        - 在计算机上执行 ``fastboot flash recovery_a third_party_recovery.img``（如果槽位 A 活跃）或 ``fastboot flash recovery_b third_party_recovery.img``（如果槽位 B 活跃）
        - 重启目标安卓设备使其进入恢复模式（在目标安卓设备上通过音量 +/- 键选中红色的 ``RECOVERY`` 并按下电源键或在计算机上执行 ``fastboot reboot recovery``）
        - 如果目标安卓设备启动到恢复模式并能够在输入正确的密码后解密 ``/data`` 分区
          - 如果正在使用 OrangeFox 请在第三方恢复中刷入 OrangeFox 的 ZIP 包
          - 在第三方恢复中刷入 ``magisk.zip``
          - 通过第三方恢复将目标安卓设备重启至系统
          - 如果目标安卓设备能够正常进入系统
            - 启动相应的 root 管理器并检查目标安卓设备是否已成功 root
            - 如未 root，请重试或放弃 root（请记得将全部分区还原为原始分区）
          - 否则
            - 根据目标安卓设备长按电源键和音量键来强制目标安卓设备重启进入 bootloader
            - 重启目标安卓设备使其进入恢复模式（在目标安卓设备上通过音量 +/- 键选中红色的 ``RECOVERY`` 并按下电源键或在计算机上执行 ``fastboot reboot recovery``）
            - 通过第三方恢复将目标安卓设备中的 ``magisk.zip`` 重命名为 ``uninstall.zip``
            - 通过第三方恢复刷入 ``uninstall.zip``
            - 通过第三方恢复将目标安卓设备中的 ``uninstall.zip`` 重命名回 ``magisk.zip``
            - 重启目标安卓设备使其正常进入系统
            - 重试或放弃 root
        - 否则
          - 在计算机上执行 ``fastboot flash recovery_a original_recovery.img``（如果槽位 A 活跃）或 ``fastboot flash recovery_b original_recovery.img``（如果槽位 B 活跃）
          - 搜索其它第三方恢复、重试或放弃 root
      - 否则
        - 在计算机中执行 ``fastboot boot third_party_recovery.img`` 以使得目标安卓设备临时启动到由第三方恢复实现的恢复模式
        - 如果目标安卓设备启动到恢复模式并能够在输入正确的密码后解密 ``/data`` 分区
          - 如希望将第三方恢复永久保留可在第三方恢复中刷入当前 TWRP（如果使用的是 TWRP）或 OrangeFox 的 ZIP 包（如果使用的是 OrangeFox）
          - 在第三方恢复中刷入 ``magisk.zip``
          - 通过第三方恢复将目标安卓设备重启至系统
          - 如果目标安卓设备能够正常进入系统
            - 启动相应的 root 管理器并检查目标安卓设备是否已成功 root
            - 如未 root，请重试或放弃 root（请记得将全部分区还原为原始分区）
          - 否则
            - 根据目标安卓设备长按电源键和音量键来强制目标安卓设备重启进入 bootloader
            - 重启目标安卓设备使其进入恢复模式（在目标安卓设备上通过音量 +/- 键选中红色的 ``RECOVERY`` 并按下电源键或在计算机上执行 ``fastboot reboot recovery``）
            - 通过第三方恢复将目标安卓设备中的 ``magisk.zip`` 重命名为 ``uninstall.zip``
            - 通过第三方恢复刷入 ``uninstall.zip``
            - 通过第三方恢复将目标安卓设备中的 ``uninstall.zip`` 重命名回 ``magisk.zip``
            - 重启目标安卓设备使其正常进入系统
            - 重试或放弃 root
        - 否则，搜索其它第三方恢复、重试或放弃 root
  - 移除 USB 数据线
- 否则（请使用下列方法中的任一方法）
  - 方法 1：请使用首次 root 的方法中的任一方法
  - 方法 2：通过目标安卓设备中已具有 root 权限的 root 管理器直接安装并重启目标安卓设备使其正常进入系统（推荐）
  - 方法 3：使用 [Kernel Flasher](https://github.com/fatalcoder524/KernelFlasher)
    - 在目标安卓设备上安装 Kernel Flasher
    - 使用已拥有 root 权限的 root 管理器为 Kernel Flasher 授予 root 权限
    - 通过 Kernel Flasher 备份 ``/boot`` 分区并将其复制或移动到计算机中
    - 从 GitHub 上搜索并下载相应的 AnyKernel3（AK3）
    - 通过 Kernel Flasher 刷入 AK3（内核在 ``boot`` 分区中）
    - 重启目标安卓设备使其正常进入系统
    - 如果目标安卓设备能够正常进入系统
      - 安装并启动与新内核对应的最新版 root 管理器以检查目标安卓设备是否已成功 root（这可能从 LKM 模式转换为 GKI 模式）
      - 如未 root，请尝试使用其它方法 root 目标安卓设备
    - 否则
      - 根据目标安卓设备长按电源键和音量键来强制目标安卓设备重启进入 bootloader
      - 在计算机上部署最新的 [platform tools](https://developer.android.com/tools/releases/platform-tools) 环境并确保 ``adb`` 和 ``fastboot`` 在搜索路径中
      - 在计算机上为目标安卓设备安装相应的驱动
      - 在计算机上执行 ``fastboot flash original_boot.img``
      - 重启目标安卓设备使其正常进入系统
      - 尝试使用其它方法 root 目标安卓设备

一些实现和模块之间的兼容性分析如下，其中 Y 表示兼容，N 表示不兼容。

| 兼容性 | 官方 Magisk 和 KSU 的所有变体 | Magisk Alpha | Apatch | Zygisk Next | ReZygisk | NeoZygisk | Shamiko | NoHello | Zygisk Assistant |
| - | - | - | - | - | - | - | - | - | - |
| 官方 Magisk 和 KSU 的所有变体 | - | N | N | Y | Y | Y | Y | Y | Y |
| Magisk Alpha | N | - | N | Y | N | Y | Y | Y | Y |
| Apatch | N | N | - | Y | Y | Y | N | Y | Y |
| Zygisk Next | Y | Y | Y | - | N | N | Y | Y | Y |
| ReZygisk | Y | N | Y | N | - | N | Y | Y | Y |
| NeoZygisk | Y | Y | Y | N | N | - | N | N | Y |
| Shamiko | Y | Y | N | Y | Y | N | - | N | Y |
| NoHello | Y | Y | Y | Y | Y | N | N | - | N |
| Zygisk Assistant | Y | Y | Y | Y | Y | Y | Y | N | - |

因此，存在以下搭配（部分），其中 P 表示通过，F 表示失败。有关过检的详细步骤，请参阅 [Bypassers](../Bypassers/README.md)。

| Combination | Native Root Detector | Native Test |
| - | - | - |
| Magisk Alpha + Zygisk Next + PIF + TS + VBMeta Fixer | F | F |
| Magisk Alpha + Zygisk Next + NoHello + PIF + TS + VBMeta Fixer | P | F |
| Magisk Alpha + Zygisk Next + Shamiko + PIF + TS + VBMeta Fixer | P | P |
| Magisk Alpha + Zygisk Next + Shamiko + Zygisk Assistant (Denylist configured) + PIF + TS + VBMeta Fixer | P | F |
| Magisk + Zygisk Next + Shamiko + Zygisk Assistant (Denylist configured) + PIF + TS + VBMeta Fixer | F | F |
| Magisk Alpha + built-in Zygisk + Shamiko + Zygisk Assistant (Denylist configured) + PIF + TS + VBMeta Fixer | P | F |
| Magisk Alpha + built-in Zygisk + Shamiko + PIF + TS + VBMeta Fixer | P | F |
| Magisk Alpha + built-in Zygisk + NoHello + PIF + TS + VBMeta Fixer | P | F |
| Magisk Alpha + built-in Zygisk + PIF + TS + VBMeta Fixer | F | F |
| Magisk Alpha + NeoZygisk + PIF + TS + VBMeta Fixer | F | F |
| Magisk Alpha + NeoZygisk + Zygisk Assistant (Denylist configured) + PIF + TS + VBMeta Fixer | P | F |

值得注意的是，Zygisk Next 自 1.3.0 版本起集成了 Shamiko 大部分的功能，且适用于所有的 root 实现。目前，SukiSU Ultra 或 Magisk Alpha，搭配 Zygisk Next 1.3.0 及更高的版本，可能是最好的上游组合。
