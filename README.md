# Counterstroke

A tool to encode binary data via Chinese (Simplified) characters from the Unihan database based on the total number of strokes a chinese character has.

### Brief Description of Algorithm

For encoding, we convert the input into a hexadecimal payload, the first 4 bits and last 4 bits (ranging in values from 0x0 to 0xF) are provided a 1-to-1 mapping to a stroke count. The stroke count is used to determine one (out of many) chinese characters to represent the 4 bits. This is repeated for the entire input, and the proess is reversed during decoding.

### Examples

It should work on text files, e.g.:

**Run 1**
```sh

$ "The quick brown fox jumps over the lazy dog." | python3 counterstroke.py -e

浐泼绤蒇涩选讷仓脸龙䓓阂玺锛郸囵烬踬钆斗获讻窑机挙䍁铟稆涡鳎伤队贾谂载镲铰锉夸长唡谭羟烂称鳁绺仓惧启纪专疴骥赉剧谄荦掷吗划韦硙侧骍琼敌珑贠户剧鲲贾击渔鲟铑缚邬斗热虏铃骥涩阈孙㘎气厮

$ echo -n "浐泼绤蒇涩选讷仓脸龙䓓阂玺锛郸囵烬踬钆斗获讻窑机挙䍁铟稆涡鳎伤队贾谂载镲铰锉夸长唡谭羟烂称鳁绺仓惧启纪专疴骥赉剧谄荦掷吗划韦硙侧骍琼敌珑贠户剧鲲贾击渔鲟 铑缚邬斗热虏铃骥涩阈孙㘎气厮" | python3 counterstroke.py -d

The quick brown fox jumps over the lazy dog. 
```

**Run 2 (different chinese characters involved)**
```sh
$ echo "The quick brown fox jumps over the lazy dog." | python3 counterstroke.py -e

狲垆埚属铃骁扫计偬闪辄恹馀榄党抢涡瘫孙长颀扩盘尘砺鿸羟铦㭣彝纩劝鸲莴赶攒啯觞约厅钸䌽铬珑递鳃铚书鸾员妇历恳颤阊党桡栉馃负异历笾祎栗鹅铌贰争仅谂辚硁轧绸鲞萝携寻气虑姗家癣痈铢价鹮凤缨% 

$ echo -n "狲垆埚属铃骁扫计偬闪辄恹馀榄党抢涡瘫孙长颀扩盘尘砺<9ff8>羟铦㭣彝纩劝鸲莴赶攒啯觞约厅钸䌽铬珑递鳃铚书鸾员妇历恳颤阊党桡栉馃负异历笾祎栗鹅铌贰争仅谂辚硁轧 绸鲞萝携寻气虑姗家癣痈铢价鹮凤缨" | python3 counterstroke.py -d

The quick brown fox jumps over the lazy dog.% 
```

It also work on other file types (for reference, `biang.jpg` is included in the repo):

```sh
$ cat biang.jpg | python3 counterstroke.py -e | python3 counterstroke.py -d > biang2.jpg
$ md5sum biang.jpg                                                                      
c8bd333910bae7949201b1ca971ead2c  biang.jpg
$ md5sum biang2.jpg
c8bd333910bae7949201b1ca971ead2c  biang2.jpg 
```
