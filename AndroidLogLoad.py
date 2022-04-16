import json
import urllib.request

def readFile_jsonDump(AndroidLog):
    with open('AndroidLog.txt','r' ) as f:
        json_str = json.dumps(f.read())
        target_str = json.loads(json_str)
        target_dic = json.loads(target_str)  # JSON 字符串 字典化
        print(type(target_dic),target_dic)
    return target_str
#将字符串字典化
def str_changeTo_dic(str_temp):
    json_str = json.dumps(str_temp)
    target_str = json.loads(json_str)
    target_dic = json.loads(target_str)
    return target_dic

def DownLoadingAndriondLog(FirstLogContent):
    LogStorageAddress = "D:\huiTool\AllLogTools\log\AndroidLog\log.txt"
    if FirstLogContent["feedbackInfoUrl"] != "":
        data = urllib.request.urlretrieve(FirstLogContent["feedbackInfoUrl"], LogStorageAddress, reporthook=loading)
        print(data)
        with open(data[0], 'r') as temp_log:
            target_log_txt = str_changeTo_dic(temp_log.read())
            print('target_log_txt:\n',target_log_txt)
        final_log = 'D:\huiTool\AllLogTools\log\AndroidLog\AndroidLog.zip'
        AndroidLogData = urllib.request.urlretrieve(target_log_txt['appLogUrl'],final_log,reporthook=loading)

#显示下载进度
def loading(blocknum,blocksize,totalsize):
    """
    回调函数: 数据传输时自动调用
    blocknum:已经传输的数据块数目
    blocksize:每个数据块字节
    totalsize:总字节
    """
    percent = 100 * blocknum * blocksize / totalsize
    if percent>100:
        percent=100
    print("正在下载>>>%0.2f%%"%percent)


temp_var = readFile_jsonDump('AndroidLog')
temp_dic = str_changeTo_dic(temp_var)
DownLoadingAndriondLog(temp_dic)