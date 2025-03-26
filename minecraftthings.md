# My Minecraft Developer Chinese Guide
![](https://img.shields.io/badge/license-CC--BY--SA--4.0-green) ![](https://img.shields.io/github/stars/Mouse0w0/MinecraftDeveloperGuide) [![](https://img.shields.io/badge/%E7%A0%81%E4%BA%91-Gitee-red)](https://gitee.com/mirrors_Mouse0w0/MinecraftDeveloperGuide)

**The closure of MCBBS has resulted in the failure of a large number of tutorials. We earnestly request readers to assist the guide in contacting relevant authors to migrate their tutorials in a timely manner.**

**Click the "Watch" button in the upper right corner to get real-time updates on the Chinese guide, and click the "Star" button in the upper right corner to support the compilation of the Chinese guide.**

**You are welcome to submit various Minecraft development-related tutorials, materials, documents, and libraries [here](https://github.com/mouse0w0/MinecraftDeveloperGuide/issues/new?assignees=&labels=&projects=&template=request.yml).**

## Table of Contents
- [How to Ask Questions](#how-to-ask-questions)
- [Common Websites and Resources](#common-websites-and-resources)
- [Java Basics](#java-basics)
- [Forge Mods](#forge-mods)
- [NeoForge Mods](#neoforge-mods)
- [Bukkit/Spigot Plugins](#bukkitspigot-plugins)
- [Fabric Mods](#fabric-mods)
- [BungeeCord Plugins](#bungeecord-plugins)
- [Sponge Plugins](#sponge-plugins)
- [Datapacks](#datapacks)
- [Java Edition Launchers](#java-edition-launchers)
- [Bedrock Edition Servers](#bedrock-edition-servers)
- [Bedrock Edition Addons](#bedrock-edition-addons)
- [Bedrock Edition Mods](#bedrock-edition-mods)
- [NetEase Bedrock Edition](#netease-bedrock-edition)
- [Shader Packs](#shader-packs)
- [Outdated Resources](#outdated-resources)
- [Copyright Notice](#copyright-notice)

## How to Ask Questions
When you encounter a problem that you cannot solve even after **using search engines, consulting relevant documentation, and debugging (if you haven't done the above, please do so immediately)**, you may ask others for help. **When you ask a question, please ensure that you accurately provide the following information:**
- Accurately describe your needs and the actual problem.
- Accurately describe the information of your platform. For example:
    - Java version
    - Development tools used and their versions (e.g., IntelliJ IDEA, Eclipse)
    - Automated build tools used and their versions (e.g., Maven, Gradle)
    - Minecraft version
    - Bukkit/Spigot/Forge/Sponge/Fabric platform and its version
    - Dependent libraries, mods, or plugins and their versions
- Provide your source code or SSCCE (Short, Self-Contained, Correct Example), and upload the complete source code including project description files to a source code hosting platform (such as Gitee, Github).
- Provide your complete logs and crash reports.
- Provide your reference materials (e.g., referring to a specific function of a certain mod).

If you ask a question by posting, please also briefly include the problem description and platform information in your title. For example: "[Forge][1.7.10] NullPointerException when loading Mod"

**Please remember that others' answers are not to be taken for granted.** If you want to learn more about how to ask questions, tips, and etiquette, take a look at [How To Ask Questions The Smart Way](https://lug.ustc.edu.cn/wiki/doc/smart-questions), which will give you a lot of help.

## Common Websites and Resources

### ~~[Minecraft Chinese Forum Development Discussion Section](http://www.mcbbs.net/forum.php?mod=forumdisplay&fid=479)~~

### [Github](https://github.com/)
The world's largest social programming and code hosting website, where you can view the source code of many mods and plugins.

### [Gitee](https://gitee.com/)
A Chinese social programming and code hosting website.

### [Stack Overflow](http://stackoverflow.com/)
The world's largest programming knowledge sharing and learning community, where you can find answers to many programming questions.

### Search Engines [Baidu](https://www.baidu.com)/[Bing](https://www.bing.com)/[Google](https://www.google.com)
Why not Baidu it first if you have any questions?

### ~~[wiki.vg](https://wiki.vg/Main_Page)~~
> wiki.vg is closed. Currently, the Minecraft Wiki is merging relevant content. [Click here to visit the temporary page](https://minecraft.wiki/w/Minecraft_Wiki:Projects/wiki.vg_merge).

A Minecraft reverse engineering and protocol reference documentation website, containing reference documents for network communication protocols, data formats, Mojang authentication protocols, and more for various versions.

### ~~[Minecraft Chinese Forum Development Tutorial Index Thread](http://www.mcbbs.net/thread-54579-1-1.html)~~

### [TeaCon Mod Development Tea Party - Online Minecraft Mod Development Competition](https://www.teacon.cn/)

### [V2 Minecraft Developer Forum](https://www.v2mcdev.com/)

### Other Resources
- [Curse Maven](https://www.cursemaven.com/)
- [Research and Application of Minecraft Entity Movement](http://lovexyn0827.space/mcdocs/docs/Minecraft%E5%AE%9E%E4%BD%93%E8%BF%90%E5%8A%A8%E7%A0%94%E7%A9%B6%E4%B8%8E%E5%BA%94%E7%94%A8/Minecraft%E5%AE%9E%E4%BD%93%E8%BF%90%E5%8A%A8%E7%9B%B8%E5%85%B3%E7%A0%94%E7%A9%B6%E4%B8%8E%E5%BA%94%E7%94%A8)
- [Cross-Loader Mod Development Guide Based on Architectury](https://turou.gitbook.io/arch/)
- [Minecraft Server Development Guide](https://izzel.io/2021/11/13/how-to-minecraft-server/)
- [Adventure Chinese Documentation](https://adventure-docs.minecraft.kim/) ([Github](https://github.com/shaokeyibb/adventure-docs-zh_CN))
- [[Protocol] Teach You How to Ping a Server Externally](https://juejin.cn/post/7120946847312510984)
- ~~[Pattern Matching in Java](https://www.mcbbs.net/thread-1207118-1-1.html)~~
- [Talking About Chunks and Tickets](https://izzel.io/2020/09/09/chunks-and-tickets/)
- ~~[How to Read Crash Reports and Timings?](http://www.mcbbs.net/thread-860103-1-1.html)~~
- [Mixin Official Wiki Chinese Translation](https://mouse0w0.github.io/categories/Mixin/)
- [Domestic Mirror of Minecraft Development Resources Maven Repository](https://blog.lss233.com/lss233minecraft-mod/)
- ~~[How to Use Continuous Integration to Help Development](http://www.mcbbs.net/thread-716920-1-1.html)~~
- ~~[[Debugging Assistance] JRebel - Give You +1s \| No Longer Need to Restart the Client and Use Global Variables](http://www.mcbbs.net/thread-694119-1-1.html)~~

### Domestic Development Communication Communities
- [Teacon Mod Development Tea Party KOOK Channel](https://kook.teacon.cn/)
- [Mouse's Minecraft Development Discussion QQ Group: 345538010](https://jq.qq.com/?_wv=1027&k=5wTKLI7)
- [Bukkit/Spigot Plugin Development Communication QQ Group: 914085636](https://jq.qq.com/?_wv=1027&k=FeUg8OUQ)
- [Sponge Plugin Development Communication QQ Group: 613604130](https://jq.qq.com/?_wv=1027&k=52OlyJ7)

## Java Basics

### 《Java from Beginner to Master》
A widely known Chinese introductory book for Java.

### 《Java 8 Programming Basics (Reference) Official Tutorial》
This book is divided into two volumes. The basics version has less content, while the reference version has more. The Chinese translation is relatively stiff and difficult to understand, and should only be used as a reference.

### 《Core Java》
This book is divided into two volumes and is a time-honored and detailed advanced Java book.

### Java Chinese Online Free Tutorials
> The content has not been verified and is for reference only.

- [Liao Xuefeng](https://www.liaoxuefeng.com/wiki/1252599548343744)
- [Runoob](http://www.runoob.com/java/)
- [W3CSchool](https://www.w3cschool.cn/java/)
- [Yiibai](https://www.yiibai.com/java/)

### Java 8 Documentation ([English](http://docs.oracle.com/javase/8/docs/api/)/[Chinese](https://www.matools.com/api/java8))

### JDK Download
- [Oracle JDK](https://www.oracle.com/java/technologies/java-se-glance.html): Oracle's JDK download. Downloading JDK archives below Java 17 requires login, and commercial use is restricted.
- [OpenJDK](https://openjdk.org/): The original open-source project for JDK.
- [Azul Zulu](https://www.azul.com/downloads/): OpenJDK provided by Azul.
- [BellSoft Liberica JDK](https://bell-sw.com/pages/downloads/): OpenJDK provided by BellSoft.
- [Eclipse Temurin](https://adoptium.net/): OpenJDK provided by the Eclipse Foundation.
- [Amazon Corretto](https://aws.amazon.com/cn/corretto/): OpenJDK provided by Amazon.
- [Microsoft Build of OpenJDK](https://learn.microsoft.com/zh-cn/java/openjdk/download/): OpenJDK provided by Microsoft.
- [Dragonwell](https://dragonwell-jdk.io/): OpenJDK provided by Alibaba Cloud.

### Further Reading
> Further improve your Java programming skills.

- [Google Java Style Guide](http://hawstein.com/2014/01/20/google-java-style/)
- [Design Patterns](https://java-design-patterns.com/zh/)
- [Programming Principles](https://mouse0w0.github.io/2018/10/04/Programming-Principles/)
- Head First Design Patterns ([Douban](https://book.douban.com/subject/2334288/))
- Effective Java ([Douban](https://book.douban.com/subject/30412517/))
- Clean Code: A Handbook of Agile Software Craftsmanship ([Douban](https://book.douban.com/subject/4199741/))
- Clean Architecture: A Craftsman's Guide to Software Structure and Design ([Douban](https://book.douban.com/subject/30333919/))

## Forge Mods

### [【1.19-1.18】Zhengshan Xiaozhong - Forge Mod Development Guide](https://www.teacon.cn/xiaozhong)

### [【1.16】Boson 1.16 Mod Development Tutorial](https://boson.v2mcdev.com/)

### [【1.12.2】Harbinger Forge Mod Development Guide](https://harbinger.covertdragon.team/)

### [【1.8.9】zzzz's Mod Development Tutorial](https://fmltutor.ustc-zzzz.net/)

### Forge Official Documentation
Introduces some of the features added by Forge.
- [English Documentation (Latest Version)](https://mcforge.readthedocs.io/en/latest/)
- [Chinese Translation (1.12.2)](https://mcforge-cn.readthedocs.io/zh/latest/)

### MDK (Minecraft Development Kit)
- [Forge Official Download](http://files.minecraftforge.net/)
- [Minecraft Forge Building Open Environment Network Proxy Configuration Tutorial](https://zekerzhayard.gitbook.io/minecraft-forge-gou-jian-kai-fa-huan-jing-wang-luo-dai-li-pei-zhi-jiao-cheng/)
- [【1.7.10+】Mouse's MDK Offline Package](https://github.com/mouse0w0/forge-mdk-offline) ([Baidu Cloud Disk Extraction Code: jmrv](https://pan.baidu.com/s/1dE0EJnz))
- ~~[Speed Up Mod Environment Configuration by Modifying Hosts](https://www.mcbbs.net/thread-1148912-1-1.html)~~
- ~~[【1.14+】ForgeGradleCN — New MDK Configuration Solution](https://www.mcbbs.net/thread-1076799-1-1.html)~~
- ~~[【1.12.2+】FledgeXu's MDK Offline Package](https://v2mcdev.com/t/topic/249) ([Github](https://github.com/FledgeXu/ForgeGradleOffline/tags))~~

### Simplified Chinese Resources
> Items with strikethrough may have better resources available, or may be outdated, have broken links, or contain misleading or incomplete information, for reference only.

- [【1.20】In-depth Analysis of the High-Version Rendering System - The Demise of GuiComponent and the Rise of GuiGraphics](https://turou.fun/minecraft/render-tutor/)
- [【1.20】Polonium - Advanced Entity Tutorial for 1.20](https://lych.top/polonium/)
- [【1.19】【Bilibili】Flandre Furan's Forge Mod Development Video Tutorial](https://www.bilibili.com/video/BV1mV411u73D)
- [【1.18.2】HoloJaneway Mod Development Tutorial](https://holojaneway.uss-shenzhou.cn/holojaneway)
- [【1.18】Qin Qianjiu's Mod Development Tutorial](https://tt432.github.io/ModdingTutorial118)
- [【1.18.2】Datagen Tutorial Based on Forge](https://skyinr.github.io/DatagenBook/#/zh-cn/)
- [【1.16.5】【Bilibili】Flandre Furan's Forge Mod Development Video Tutorial](https://www.bilibili.com/video/BV1WM4y1K7D5)
- [【1.16.1】Xingduan Suzhao's Forge Mod Development Video Tutorial](https://space.bilibili.com/3537121929332753/channel/collectiondetail?sid=3378523&ctype=0) ([Douyin](https://www.douyin.com/video/7279377986187431202)/[Xigua Video](https://www.ixigua.com/home/2562275897255528/pseries/?preActiveKey=video&list_entrance=userdetail&wid_try=1))
- [Talking About Forge Toolchain](https://izzel.io/2022/09/07/forge-toolchain-teardown/)
- ~~[Hand-in-Hand Mixin+Forge Development Example, From Development Environment Configuration to Mod Release](https://www.mcbbs.net/thread-1386942-1-1.html)~~
- [Cobalt - Rendering Analysis Document](https://zomb-676.github.io/CobaltDocs)
- [Quickly Develop Multi-Block Structures from Examples](https://turou.fun/multiblock-tutor/)
- [Re-analyzing World Generation: Biomes](http://yaossg.com/biome/index.html)
- [Talking About Creatures and AI](https://izzel.io/2021/12/19/living-things/)
- ~~[Detailed Beginner's Tutorial from Forge Installation to Export \| Solutions to Various Errors](https://www.mcbbs.net/thread-1193768-1-3.html)~~
- [A Brief Discussion on TileEntitySpecialRenderer from the Perspective of Examples](https://turou.fun/legacy-render-tutor/)
- [[Inferring Further from Examples to Deepen Mod Development - Section 2] Rainbow Bridge Staff + Building Little Helper = ?](https://turou.fun/analogy/rainbow-gadgets/)
- [[Inferring Further from Examples
