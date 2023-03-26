#!/bin/bash
# 這個腳本首先會更新系統，然後檢查Python 3和pip 3版本是否已安裝，如果未安裝則會安裝它們。接著會檢查ssh、sshpass、adb、fastboot這些工具是否已安裝，如果未安裝則會安裝它們。最後會下載並安裝Python 3.10和pip 3.10，如果它們未安裝的話。

# 如果執行這個腳本時提示"permission denied"錯誤，可以使用chmod命令賦予腳本執行權限： chmod +x linux_system_check_download.sh

# 更新系統
sudo apt-get update
sudo apt-get upgrade -y

# 檢查網路
sudo apt-get install net-tools -y

# 檢查網路IP
ifconfig

# 檢查網路狀態
ping -c 3

# 下載 wget
sudo apt-get install wget -y

# 檢查python3, pip3 是否安裝並安裝
if ! command -v python3 &> /dev/null 
then
    echo 'Error: python3 is not installed.'
    sudo apt-get install python3 -y
fi

if ! command -v pip3 &> /dev/null 
then
    echo 'Error: pip3 is not installed.'
    sudo apt-get install python3-pip -y
fi

echo 'python3 is installed: $(python3 --version)'
echo 'pip3 is installed: $(pip3 --version)'

# 檢查python版本並下載需求的系統套件
if ! command -v ssh &> /dev/null || ! command -v sshpass &> /dev/null || ! command -v adb &> /dev/null || ! command -v fastboot &> /dev/null
then
    echo "Installing ssh, sshpass, adb, fastboot..."
    sudo apt-get install ssh sshpass android-tools-adb android-tools-fastboot
fi

# 檢查python3.10版本並下載需求的系統套件
if ! command -v python3.10 &> /dev/null 
then 
    echo 'Python 3.10 is not installed, installing...'
    wget https://www.python.org/ftp/python/3.10.2/Python-3.10.2.tgz
    tar -xvf Python-3.10.2.tgz
    cd Python-3.10.2
    ./configure --enable-optimizations
    make -j 8
    sudo make altinstall
    cd ..
    rm -rf Python-3.10.2 Python-3.10.2.tgz
    echo 'Python 3.10 is installed: $(python3.10 --version)'
fi

# 檢查pip3.10版本並下載需求的系統套件
if ! command -v pip3.10 &> /dev/null
then
    echo "pip 3.10 not found, installing..."
    sudo apt-get install python3.10-distutils
    wget https://bootstrap.pypa.io/get-pip.py
    sudo python3.10 get-pip.py
    rm get-pip.py
fi
    
