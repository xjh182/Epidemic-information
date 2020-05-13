import tkinter as tk
import urllib.request
import urllib.parse
import json

def openURL():

    api='https://view.inews.qq.com/g2/getOnsInfo?name=disease_h5&callback=jQuery341024218267927690773_1581677197606&_=1581677197607'

    req = urllib.request.Request(api)
    req.add_header('user-agent','Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.130 Safari/537.36')
    return urllib.request.urlopen(req)
    
def abroadOpenURL():

    api='https://api.inews.qq.com/newsqa/v1/automation/modules/list?modules=FAutoGlobalStatis,FAutoContinentStatis,FAutoGlobalDailyList,FAutoCountryConfirmAdd'

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
    
    nowConfirm = str(ass['chinaTotal']['nowConfirm'])
    nowConfirmAdd = str(ass['chinaAdd']['nowConfirm'])
    
    importedCase = str(ass['chinaTotal']['importedCase'])
    importedCaseAdd = str(ass['chinaAdd']['importedCase'])
    
    noInfect = str(ass['chinaTotal']['noInfect'])
    noInfectAdd = str(ass['chinaAdd']['noInfect'])
    
    
    abroadData = abroadOpenURL().read().decode('UTF-8')
    abroadC = json.loads(abroadData)
    abroadAss = abroadC['data']
    
    nowAbroadConfirm = str(abroadAss['FAutoGlobalStatis']['nowConfirm'])
    nowAbroadConfirmAdd = str(abroadAss['FAutoGlobalStatis']['nowConfirmAdd'])
    
    AbroadConfirm = str(abroadAss['FAutoGlobalStatis']['confirm'])
    AbroadConfirmAdd = str(abroadAss['FAutoGlobalStatis']['confirmAdd'])
    
    AbroadHeal= str(abroadAss['FAutoGlobalStatis']['heal'])
    AbroadHealAdd = str(abroadAss['FAutoGlobalStatis']['healAdd'])
    
    AbroadDead= str(abroadAss['FAutoGlobalStatis']['dead'])
    AbroadDeadAdd = str(abroadAss['FAutoGlobalStatis']['deadAdd'])
    
    
def window():
    root = tk.Tk()
    root.title("新冠肺炎疫情最新动态")
    Data = findData()

    text = tk.Text(root,width=60,height=40)
    text.pack()
    
    text.insert(tk.INSERT,"国内数据：\n\n")
    text.insert(tk.INSERT,"累计确诊病例数量："+Data.confirm)
    text.insert(tk.INSERT,"    与昨日相比增加："+Data.confirmAdd)
    
    text.insert(tk.INSERT,"\n\n累计死亡病例数量："+Data.dead)
    text.insert(tk.INSERT,"     与昨日相比增加："+Data.deadAdd)
    
    text.insert(tk.INSERT,"\n\n累计治愈病例数量："+Data.heal)
    text.insert(tk.INSERT,"    与昨日相比增加："+Data.healAdd)
    
    text.insert(tk.INSERT,"\n\n\n现有确诊病例数量："+Data.nowConfirm)
    text.insert(tk.INSERT,"    与昨日相比增加："+Data.nowConfirmAdd)
    
    text.insert(tk.INSERT,"\n\n现有疑似病例数量："+Data.suspect)
    text.insert(tk.INSERT,"     与昨日相比增加："+Data.suspectAdd)
    
    text.insert(tk.INSERT,"\n\n现有无症状感染者："+Data.noInfect)
    text.insert(tk.INSERT,"     与昨日相比增加："+Data.noInfectAdd)
    
    text.insert(tk.INSERT,"\n\n\n境外输入病例："+Data.importedCase)
    text.insert(tk.INSERT,"    与昨日相比增加："+Data.importedCaseAdd)
    
    
    text.insert(tk.INSERT,"\n\n\n\n国外数据：\n\n")
    text.insert(tk.INSERT,"现有确诊病例数量："+Data.nowAbroadConfirm)
    text.insert(tk.INSERT,"    与昨日相比增加："+Data.nowAbroadConfirmAdd)
    
    text.insert(tk.INSERT,"\n\n累计确诊病例数量："+Data.AbroadConfirm)
    text.insert(tk.INSERT,"    与昨日相比增加："+Data.AbroadConfirmAdd)
    
    text.insert(tk.INSERT,"\n\n累计治愈病例数量："+Data.AbroadHeal)
    text.insert(tk.INSERT,"    与昨日相比增加："+Data.AbroadHealAdd)
    
    text.insert(tk.INSERT,"\n\n累计死亡病例数量："+Data.AbroadDead)
    text.insert(tk.INSERT,"    与昨日相比增加："+Data.AbroadDeadAdd)
    
    
    text.insert(tk.INSERT,"\n\n\n数据更新日期："+Data.updateTime)
    text.insert(tk.INSERT,"\n数据来源：腾讯新闻 新冠肺炎疫情最新动态")
    
    text.configure(state='disabled')
    
    tk.mainloop()
    
if __name__ == '__main__':
    window()
