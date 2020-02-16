import tkinter as tk
import urllib.request
import urllib.parse
import json

def openURL():

    api='https://view.inews.qq.com/g2/getOnsInfo?name=disease_h5&callback=jQuery341024218267927690773_1581677197606&_=1581677197607'

    req = urllib.request.Request(api)
    req.add_header('user-agent','Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.130 Safari/537.36')
    return urllib.request.urlopen(req)

class findData:
    Data = openURL().read().decode('UTF-8')
    Data = Data.split('jQuery341024218267927690773_1581677197606(')[1].split(')')[0]
    c = json.loads(Data)
    ass = json.loads(c['data'])
    
    
    updateTime = ass['lastUpdateTime']
    
    confirm = str(ass['chinaTotal']['confirm'])
    confirmAdd = str(ass['chinaAdd']['confirm'])
    
    suspect = str(ass['chinaTotal']['suspect'])
    suspectAdd = str(ass['chinaAdd']['suspect'])
    
    dead = str(ass['chinaTotal']['dead'])
    deadAdd = str(ass['chinaAdd']['dead'])
    
    heal = str(ass['chinaTotal']['heal'])
    healAdd = str(ass['chinaAdd']['heal'])
    
def window():
    root = tk.Tk()
    Data = findData()

    name = tk.Label(text="疫情信息获取",font=('Microsoft YaHei',15)).grid(row = 0, column = 1,padx = 100)
    
    confirmNum = tk.Label(text="确诊病例数量："+Data.confirm,font=('Microsoft YaHei',10)).grid(row = 1, column = 0)
    confirmAddNum = tk.Label(text="与昨日相比增加："+Data.confirmAdd,font=('Microsoft YaHei',10)).grid(row = 2, column = 0)
    
    suspectNum = tk.Label(text="疑似病例数量："+Data.suspect,font=('Microsoft YaHei',10)).grid(row = 1, column = 1,padx = 20)
    suspectAddNum = tk.Label(text="与昨日相比增加："+Data.suspectAdd,font=('Microsoft YaHei',10)).grid(row = 2, column = 1,padx = 20)
    
    deadNum = tk.Label(text="死亡病例数量："+Data.dead,font=('Microsoft YaHei',10)).grid(row = 1, column = 2,padx = 20)
    deadAddNum = tk.Label(text="与昨日相比增加："+Data.deadAdd,font=('Microsoft YaHei',10)).grid(row = 2, column = 2,padx = 20)
    
    healNum = tk.Label(text="治愈病例数量："+Data.heal,font=('Microsoft YaHei',10)).grid(row = 1, column = 3,padx = 20)
    healAddNum = tk.Label(text="与昨日相比增加："+Data.healAdd,font=('Microsoft YaHei',10)).grid(row = 2, column = 3,padx = 20)
    
    updata =  tk.Label(text="数据更新日期："+Data.updateTime,font=('Microsoft YaHei',10)).grid(row = 3, column = 0)
    dataSource =  tk.Label(text="数据来源：腾讯新闻 新冠肺炎疫情最新动态",font=('Microsoft YaHei',10)).grid(row = 3, column = 3)
    
    
    
    tk.mainloop()
    
if __name__ == '__main__':
    window()