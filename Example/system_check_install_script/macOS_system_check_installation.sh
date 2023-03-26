#!/bin/bash

# 檢查是否需要安裝Xcode Command Line Tools
if ! command -v xcode-select &> /dev/null
then
    echo "Xcode Command Line Tools not found, installing..."
    xcode-select --install
fi

# 檢查Homebrew是否已安裝，如果未安裝則安裝
if ! command -v brew &> /dev/null
then
    echo "Homebrew not found, installing..."
    /bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
fi

# 更新Homebrew
echo "Updating Homebrew..."
brew update
brew upgrade

# 檢查Python 3和pip 3版本
if ! command -v python3 &> /dev/null
then
    echo "Python 3 not found, installing..."
    brew install python@3.10
fi

if ! command -v pip3 &> /dev/null
then
    echo "pip 3 not found, installing..."
    brew install pipenv
fi

echo "Python 3 version: $(python3 --version)"
echo "pip 3 version: $(pip3 --version)"

# 下載並安裝最新版本ssh、sshpass、adb和fastboot
if ! command -v ssh &> /dev/null || ! command -v sshpass &> /dev/null || ! command -v adb &> /dev/null || ! command -v fastboot &> /dev/null
then
    echo "Installing ssh, sshpass, adb, fastboot..."
    brew install openssh sshpass android-platform-tools
fi
