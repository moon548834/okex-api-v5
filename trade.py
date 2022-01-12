import okex.Account_api as Account
import okex.Funding_api as Funding
import okex.Market_api as Market
import okex.Public_api as Public
import okex.Trade_api as Trade
import okex.subAccount_api as SubAccount
import okex.status_api as Status
import json
import threading
import time

def trade():
    i = 0
    while True:
        time.sleep(10)
def cmd():
    f = open ("./.json_key", "r") 
    data = json.load(f)
    api_key = data["apikey"]
    secret_key = data["secretkey"]
    passphrase = data["password"]
    flag = '1'
    f.close()
    while True:
        nonsupport = False
        print('请输入交易的货币: [1] BTC [2] ETH [q] 取消')
        while True:
            digit = input()
            if digit == "1":
                cur = "BTC-USDT"
                break
            elif digit == "2":
                cur = "ETH-USDT"
                break
            elif digit == 'q':
                print('本次交易已取消')
                break
            else:
                nonsupport = True
                print('不支持的选项，请重新输入或者按q退出交易')
                break
        if nonsupport:
            continue
        sid = "buy"
        print('请输入交易方向: [1] 买入 [2] 卖出')
        while True:
            digit = input() 
            if digit == "1":
                side = "buy"
                break
            elif digit == "2":
                side = "sell"
                break
            elif digit == "q":
                print('本次交易已取消')
                break
            else:
                nonsupport = True
                print('不支持的选项，请重新输入或者按q退出交易')
                break
        if nonsupport: 
            continue
        print('请输入买入的数量')
        quota = float(input())
        print('本次交易为', end ='')
        if side == "buy":    
            print('买入', end='')
        else:   
            print('卖出', end='')
        print(str(quota) + '个' + cur)

        print('确认交易请按1，取消交易或重新填写请按q')
        while True:
            digit = input()
            if (digit == "1"):
                print('开始交易')
                tradeAPI = Trade.TradeAPI(api_key, secret_key, passphrase, False, flag)
                result = tradeAPI.place_order(instId=cur, tdMode='cash', side='side',
                                   ordType='market', sz=quota, tgtCcy='base_ccy')
                print(result)
                break
            elif (digit == 'q'):
                print('交易取消')
                break
            else: 
                print('不支持的选项，请重新输入或者按q退出交易')
if __name__ == '__main__':
    thread1 = threading.Thread(target = trade)
    thread2 = threading.Thread(target = cmd)
    thread1.start()
    thread2.start()
    


