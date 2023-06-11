import csv
import requests
f = open('data.csv', mode='a', encoding='utf8', newline='')
csv_write = csv.DictWriter(f, fieldnames=['排名', '球队', '球员', '场均得分', '命中率', '三分命中率', '罚球命中率'])
csv_write.writeheader()
url = 'https://nba.hupu.com/stats/players'
head = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.127 Safari/537.36'
}
nb = requests.get(url, headers=head).text
from lxml import etree
ls=[]
sb = etree.HTML(nb)
whh = sb.xpath('//tbody/tr[not(@class)]')
for i in whh:
    pm = str(i.xpath('./td[1]/text()')).replace("['", "").replace("']", "")  # 排名
    team = str(i.xpath('./td[3]/a/text()')).replace("['", "").replace("']", "")  # 球队
    name = str(i.xpath('./td[2]/a/text()')).replace("['", "").replace("']", "")  # 球员
    score = str(i.xpath('./td[4]/text()')).replace("['", "").replace("']", "")  # 得分
    mzl = str(i.xpath('./td[6]/text()')).replace("['", "").replace("']", "")  # 命中率
    sfmzl = str(i.xpath('./td[8]/text()')).replace("['", "").replace("']", "")  # 三分命中率
    fqmzl = str(i.xpath('./td[10]/text()')).replace("['", "").replace("']", "")  # 罚球命中率
    print(pm, name, team, score, mzl, sfmzl, fqmzl)
    data_dict = {'排名': pm, '球队': team, '球员': name, '场均得分': score, '命中率': mzl, '三分命中率': sfmzl, '罚球命中率': fqmzl}
    csv_write.writerow(data_dict)
f.close()
