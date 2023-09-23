import random
import urllib.parse


def choose_backend(choose_end):
    global backend
    if choose_end == "":
        choose_end = str(random.randint(1, 10))
    # if choose_end == "1":
    #     backend = "https://subcon.dlj.tf/sub?"
    if choose_end == "1":
        backend = "https://pub-api-1.bianyuan.xyz/sub?"
    if choose_end == "2":
        backend = "https://sub.xeton.dev/sub?"
    if choose_end == "3":
        backend = "https://sub.maoxiongnet.com/sub?"
    if choose_end == "4":
        backend = "https://sub.id9.cc/sub?"
    if choose_end == "5":
        backend = "https://api.dler.io/sub?"
    if choose_end == "6":
        backend = "https://api.wcc.best/sub?"
    if choose_end == "7":
        backend = "https://api.tsutsu.one/sub?"
    if choose_end == "8":
        backend = "https://sub.d1.mk/sub?"
    if choose_end == "9":
        backend = "https://api.v1.mk/sub?"
    if choose_end == "10":
        backend = input("请输入自定义后端：")
    print("\n此次转换使用的后端为：" + backend)


def choose_config(choose_con):
    global config
    if choose_con == "":
        choose_con = "1"
    if choose_con == "1":
        config = "https://raw.githubusercontent.com/ACL4SSR/ACL4SSR/master/Clash/config/ACL4SSR_Online.ini"
    if choose_con == "2":
        config = "https://raw.githubusercontent.com/ACL4SSR/ACL4SSR/master/Clash/config/ACL4SSR_Online_Mini.ini"
    if choose_con == "3":
        config = "https://raw.githubusercontent.com/ACL4SSR/ACL4SSR/master/Clash/config/ACL4SSR_Online_Full.ini"
    if choose_con == "4":
        config = "https://cdn.jsdelivr.net/gh/SleepyHeeead/subconverter-config@master/remote-config/universal/no-urltest.ini"
    if choose_con == "5":
        config = "https://cdn.jsdelivr.net/gh/SleepyHeeead/subconverter-config@master/remote-config/universal/urltest.ini"
    if choose_con == "6":
        config = "https://cdn.jsdelivr.net/gh/SleepyHeeead/subconverter-config@master/remote-config/special/basic.ini"
    if choose_con == "7":
        config = "https://gist.githubusercontent.com/tindy2013/1fa08640a9088ac8652dbd40c5d2715b/raw/connershua_new.ini"
    if choose_con == "8":
        config = "https://gist.githubusercontent.com/tindy2013/1fa08640a9088ac8652dbd40c5d2715b/raw/lhie1_dler.ini"
    if choose_con == "9":
        config = input("请输入自定义的规则地址：")
    print("\n此次转换使用配置为：" + config)
    config = urllib.parse.quote(config)


def high_mod():
    global result
    global config
    print(
        "\n====================================================\n\n网友提供的后端链接：\n\n"
        "1. https://pub-api-1.bianyuan.xyz/sub?（边缘订阅）\n"
        "2. https://sub.xeton.dev/sub?(subconverter作者)\n"
        "3. https://sub.maoxiongnet.com/sub?(猫熊)\n"
        "4. https://sub.id9.cc/sub?（品云）\n"
        "5. https://api.dler.io/sub?（sub作者&DlerCloud）\n"
        "6. https://api.wcc.best/sub?（sub-web作者）\n"
        "7. https://api.tsutsu.one/sub?（tsutsu）\n"
        "8. https://sub.d1.mk/sub?（肥羊1 支持hysteria+vless）\n"
        "9. https://api.v1.mk/sub?（肥羊2 支持hysteria+vless）\n"
        "10. 自定义后端")
    choose_end = input("---------------------------------------------\n\n请输入你要选择的后端，回车则随机选择：")
    choose_backend(choose_end)

    print(
        "\n====================================================\n\n常用规则配置：\n1. ACL4SSR_Online 默认版 分组比较全 (与Github同步)\n2. ACL4SSR_Online_Mini 精简版 (与Github同步)\n3. ACL4SSR_Online_Full 全分组 重度用户使用 (与Github同步)\n4. No-Urltest \n5. Urltest\n6. Basic(仅GEOIP CN + Final)\n7. ConnersHua 神机规则 Outbound\n8. lhie1 洞主规则完整版 \n9. 自定义")
    choose_con = input("---------------------------------------------\n\n请输入你要选择的配置规则，回车默认使用配置1：")
    choose_config(choose_con)

    emoji_use = input("\n====================================================\n是否启用emoji（回车默认启用）（y/n）：\n")
    if emoji_use == "n":
        emoji = "false"
        print("不启用emoji")
    else:
        emoji = "true"
        print("启用emoji")
    new_name_use = input(
        "\n====================================================\n是否使用clash新字段名（回车默认启用）（y/n）：\n")
    if new_name_use == "n":
        new_name = "false"
        print("不启用clash新字段名")
    else:
        new_name = "true"
        print("启用clash新字段名")
    sort_use = input("\n====================================================\n是否使用节点排序（回车默认启用）（y/n）：\n")
    if sort_use == "n":
        sort = "false"
        print("不使用节点排序")
    else:
        sort = "true"
        print("使用节点排序")

    tfo = "false"
    scv = "false"
    fdn = "false"
    result = backend + 'target=' + target + "&url=" + url + "&config=" + config + "&emoji=" + emoji + "&tfo=" + tfo + "&scv=" + scv + "&fdn=" + fdn + "&sort=" + sort + "&new_name=" + new_name


def high_mod2():
    global result
    include_use = input(
        "\n====================================================\n只使用含有以下关键字的节点，回车则略过\n（多个关键字以 | 隔开，支持正则表达式）：")
    if include_use == "":
        print("\n不挑选节点")
    else:
        include = include_use
        print("启用以下节点：" + include)
        include = urllib.parse.quote(include)
        result += "&include=" + include
    exclude_use = input(
        "\n====================================================\n排除含有以下关键字的节点，回车则略过\n（多个关键字以 | 隔开，支持正则表达式）：")
    if exclude_use == "":
        print("\n不排除节点")
    else:
        exclude = exclude_use
        exclude = urllib.parse.quote(exclude)
        result += "&exclude=" + exclude
        print("排除以下节点：" + exclude)
    filename_use = input("\n====================================================\n请输入自定义订阅文件名，回车则略过：\n")
    if len(filename_use) == 0:
        print("不使用自定义订阅文件名")
    else:
        filename = filename_use
        result += "&filename=" + filename
        filename = urllib.parse.quote(filename)
        print("使用自定义订阅文件名：" + filename)


print(
    "###################################################\n\n      Subscription Converter Python离线版\n\n###################################################")

print(
    "支持的客户端：\n1.clash\n2.surge3\n3.surge4\n4.quantumult\n5.quantumultX\n6.surfboard\n7.loon\n8.ssandriod\n9.v2ray\n10.ss\n11.ssr\n12.ssd\n13.clashr\n14.suger2")
client = input("---------------------------------------------\n请输入你所使用的客户端:")
if client == "1":
    target = "clash"
if client == "2":
    target = "surge&ver3"
if client == "3":
    target = "surge&ver4"
if client == "4":
    target = "quan"
if client == "5":
    target = "quanx"
if client == "6":
    target = "surboard"
if client == "7":
    target = "loon"
if client == "8":
    target = "sssub"
if client == "9":
    target = "v2ray"
if client == "10":
    target = "ss"
if client == "11":
    target = "ssr"
if client == "12":
    target = "ssd"
if client == "13":
    target = "clashr"
if client == "14":
    target = "surge&ver2"
print("\n你选择了" + target + "客户端")
print(
    "\n====================================================\n支持订阅或ss/ssr/trojan/vmess链接，多个链接请使用  |  分隔")

url = input("\n请输入你要转换的链接地址如果有多条链接，请用 | 分隔：")
print("\n本次转换的链接为：" + url)
url = urllib.parse.quote(url)

print(
    "\n====================================================\n\n请选择想要使用的转换模式：\n---------------------------------------------\n\n基础模式:\n  1. 默认后端、不启用emoji、无额外配置规则 \n\n进阶模式:（可选后端、启用emoji、选择配置规则、选择节点等）\n  2. 默认进阶（+emoji、后端、配置） \n  3. 更多进阶模式（+节点选择/排除、自定义文件名） \n  4. 完全自定义（自定义全部选项）")
choose = input("\n---------------------------------------------\n请选择想要的转换模式:")
if choose == "1":
    print("\n====================================================\n\n*使用基础模式*")
    backend = "https://api.wcc.best/sub?"
    insert = "false"
    basic = backend + 'target=' + target + "&url=" + url + "&insert=" + insert
    # encode = urllib.parse.quote(basic)
    print("\n====================================================\n\n已生成转换链接，复制至客户端下载配置即可使用:\n")
    print(basic)

if choose == "2":
    print("\n====================================================\n\n*使用进阶模式1*")
    high_mod()

    print("\n\n====================================================\n已生成转换链接，复制至客户端下载配置即可使用:\n")
    print(result)

if choose == "3":
    print("\n*使用进阶模式2*")
    high_mod()
    high_mod2()

    print("\n\n====================================================\n已生成转换链接，复制至客户端下载配置即可使用:\n")
    print(result)

if choose == "4":
    print("\n*使用进阶模式3·全部选项自定义*")
    high_mod()
    high_mod2()

    node_list_use = input(
        "\n====================================================\n是否输出为Node Lise（回车默认不启用）（y/n）：\n")
    if node_list_use == "y":
        node_list = "true"
        print("输出为Node Lise")
        result += "&list=" + node_list
    else:
        print("不输出为Node Lise")
    fdn_use = input("\n====================================================\n是否过滤非法节点（回车默认不过滤）（y/n）：\n")
    if fdn_use == "y":
        fdn = "true"
        print("过滤非法节点")
        result += "&fdn=" + fdn
    else:
        print("不过滤非法节点")
    udp_use = input("\n====================================================\n是否启用udp（回车默认不启用）（y/n）：\n")
    if udp_use == "y":
        udp = "true"
        print("过滤启用udp")
        result += "&udp=" + udp
    else:
        print("不过滤启用udp")
    append_type_use = input(
        "\n====================================================\n是否启用节点类型（回车默认不过滤）（y/n）：\n")
    if append_type_use == "y":
        append_type = "true"
        print("启用节点类型")
        result += "&append_typen=" + append_type
    else:
        print("不启用节点类型")
    surge_doh_use = input(
        "\n====================================================\n是否启用Surge.DoH（回车默认不过滤）（y/n）：\n")
    if surge_doh_use == "y":
        surge_doh = "true"
        print("启用Surge.DoH")
        result += "&surge_doh=" + surge_doh
    else:
        print("不启用Surge.DoH")
    clash_doh_use = input(
        "\n====================================================\n是否启用Clash.DoH（回车默认不过滤）（y/n）：\n")
    if clash_doh_use == "y":
        clash_doh = "true"
        print("启用Clash.DoH")
        result += "&clash_doh=" + clash_doh
    else:
        print("不启用Clash.DoH")
    insert_use = input("\n====================================================\n是否启用网易云（回车默认不过滤）（y/n）：\n")
    if insert_use == "y":
        insert = "true"
        print("启用网易云")
        result += "&insert=" + insert
    else:
        print("不启用网易云")

    print("\n\n====================================================\n已生成转换链接，复制至客户端下载配置即可使用:\n")
    print(result)

input("\n\n复制完链接后，请按任意键退出：")
