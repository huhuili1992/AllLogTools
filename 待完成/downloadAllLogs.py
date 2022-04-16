
#读取日志并将日志JSON话
import json
import urllib.request
#输入提示
def lang_input():
    input_terminal = ""
    input_content = ""
    input_list = []
    input_terminal = input("Do you want to get Android, IOS, or firmware logs:")
    input_content = input("Please enter Tuya's log address:")
    input_list.extend([input_terminal,input_content])
    print(input_list)
    return input_list

#想要查看日志的终端，根据用户选择返回对应的日志
def select_log_terminal(term,Loadr):
    #temp = {term:LogContent}
    if term.lower() == "Android".lower():
        #调用安卓日志处理函数
        pass
    elif list(temp[0]) == "ios".lower():
        #调用IOS处理函数
        pass
    elif list(temp)[0] == "firmware".lower():
        #调用处理固件日志的函数
        pass

def readFile_jsonDump(Ioslog):

    #将日志字典化
    with open('Ioslog.txt','r') as temp_file:
        json_str = json.dumps(temp_file.read())
        target_str = json.loads(json_str)
        #print(target_str)
        target_dic = json.loads(target_str) #JSON 字符串 字典化
        print(type(target_dic),target_dic)
        #return target_dic

    # 找到字典中的feedbackInfoUrl
    for k in target_dic:
        if k == 'feedbackInfoUrl':
            target_url = target_dic[k]
            print(target_url)

    # 下载URL中的文件到当前目录
    localAdr = "d:/log/log.txt"
    data = urllib.request.urlretrieve(target_url,localAdr,reporthook=loading)
    #print("data 格式:",type(data))
    print("第一次下载的日志信息:\n",data)
    with open(data[0],'r') as tempLog:
        json_log = json.dumps(tempLog.read())
        target_log = json.loads(json_log)
        dic_log = json.loads(target_log)

    for k in dic_log:
        if k == "appLogUrl":
            load_url = dic_log[k]
    target_zip = "d:/log/target.zip"
    target_data = urllib.request.urlretrieve(load_url,target_zip,reporthook=loading)

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

#再写一个Android的日志获取脚本
#写2个下载进度
#写成EXE的工具


if __name__ == '__main__':
    term_and_logaddr = []
    term_and_logaddr = lang_input()


#Ioslog = 'Ioslog'
#log_Dict = readFile_jsonDump(Ioslog)
#print("log_Dict\n",log_Dict)




