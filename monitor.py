import psutil
import sqlite3
from datetime import datetime
import time
import platform
import pickle
# coding=utf8

cpu = {'cpu_count': 0, 'cpu_count_logical': 0,
       'user': 0, 'system': 0, 'idle': 0, 'cpu_percent': 0}
mem = {'mem_total': 0, 'mem_avaiable': 0,
       'mem_percent': 0, 'mem_used': 0, 'mem_free': 0}

# 磁盘名称
disks = []
# 网卡信息
netcard_info = []

# 获取CPU信息


def get_cpu_info():
    cpu['cpu_count'] = psutil.cpu_count(logical=False)
    cpu['cpu_count_logical'] = psutil.cpu_count()
    cpu_times = psutil.cpu_times()
    cpu['user'] = cpu_times.user
    cpu['system'] = cpu_times.system
    cpu['idle'] = cpu_times.idle
    cpu['cpu_percent'] = psutil.cpu_percent(interval=2)
# 获取内存信息


def get_mem_info():
    mem_info = psutil.virtual_memory()
    mem['mem_total'] = mem_info.total
    mem['mem_available'] = mem_info.available
    mem['mem_percent'] = mem_info.percent
    mem['mem_used'] = mem_info.used
    mem['mem_free'] = mem_info.free
# 获取磁盘


def get_disk_info():
    for id in psutil.disk_partitions():
        disk = {'disk_id': 0, 'disk_total': 0,
                'disk_used': 0, 'disk_free': 0, 'disk_percent': 0}
        if 'cdrom' in id.opts or id.fstype == '':
            continue
        disk_name = id.device.split(':')
        disk['disk_id'] = disk_name[0]
        disk_info = psutil.disk_usage(id.device)
        disk['disk_total'] = disk_info.total
        disk['disk_used'] = disk_info.used
        disk['disk_free'] = disk_info.free
        disk['disk_percent'] = disk_info.percent
        disks.append(disk)
# 获取网卡名称和其ip地址，不包括回环


def get_netcard():
    info = psutil.net_if_addrs()
    for k, v in info.items():
        for item in v:
            if item[0] == 2 and not item[1] == '127.0.0.1':
                netcard_info.append((k, item[1]))


def insert_data():
    get_netcard()
    get_cpu_info()
    get_mem_info()
    get_disk_info()
    conn = sqlite3.connect('app.db')
    c = conn.cursor()
    data = [netcard_info[0][1], platform.platform(), cpu['cpu_count'], cpu['cpu_count_logical'], cpu['cpu_percent'], round(
        mem['mem_total'] / 1073741824, 1), mem['mem_percent'], pickle.dumps(disks), datetime.utcnow()]
    c.execute(
        "INSERT INTO Monitor(ip,platform,cpu_count,cpu_count_logical,cpu_percent,mem_total,mem_percent,disks,insert_time) VALUES (?,?,?,?,?,?,?,?,?)", data)
    # 提交！！！"
    conn.commit()

    # 关闭连接
    conn.close()


def clear_data():
    conn = sqlite3.connect('app.db')
    c = conn.cursor()
    c.execute("delete from Monitor")
    conn.commit()
    conn.close()


if __name__ == '__main__':
    clear_data()
    while True:
        print(time.strftime('%Y-%m-%d %X', time.localtime()))
        insert_data()  # 此处为要执行的任务
        time.sleep(15)
