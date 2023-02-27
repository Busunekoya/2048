"""
遊び方
wasd 移動
r リセット
m マスの数を変える(4×4だけではなく、2×2や16×16など、自由に設定可能)
"""
import random

print('2048game')

first_map = []

def map_generate(length):
    new_map = []
    for x in range(length):                                          #空のマップ製作
        for y in range(length):
            new_map.append(0)
    return(new_map)

def run_length(input_map,key_input,length):                                          #キーボード入力と処理データ制作
    output = []
    if key_input == 'w':
        for width in range(length):                                #横
            for wide in range(length):                             #縦
                output.append(input_map[length*width+wide])
    if key_input == 's':
        for width in range(length):                                #横
            for wide in range(length):                             #縦
                output.append(input_map[length*(length-width)-wide-1])
    if key_input == 'a':
        for width in range(length):                                #横
            for wide in range(length):                             #縦
                output.append(input_map[length*wide+width])
    if key_input == 'd':
        for width in range(length):                                #横
            for wide in range(length):                             #縦
                output.append(input_map[length*(wide)-(length-width)])

    return(output)

def no0(date,length):                                                                #計算
    result = []
    for t in range(length):
        change = []
        for y in range(length):                     #0を無くす
            append_number = date[length*t+y]
            if append_number != 0:
                change.append(append_number)
    #lengthの数と同じに0詰め調整
        for i in range(length-len(change)+1):
            change.append(0)

        process = []
        for i in range(length):
            if change[i] == change[i+1]:
                process.append(change[i]+change[i+1])
                del change[i]
                change.insert(i,0)
                del change[i+1]
                change.insert(i+1,0)
            else:
                process.append(change[i])
                del change[i]
                change.insert(i,0)

        process_check=[]
        for i in range(len(process)):
            if process[i] != 0:
                process_check.append(process[i])
        while len(process_check) != length:
            process_check.append(0)
        result += process_check
    return(result)

def map_result_put(key_input,result,length):
    compleate_map = []
    if key_input == 'w':
        for len in range(length):                           #縦
            for wid in range(length):                       #横
                compleate_map.append(result[length*len+wid])
    elif key_input == 's':
        for len in range(length):                           #縦
            for wid in range(length):                       #横
                compleate_map.append(result[length*(length-len-1)+(length-wid-1)])
    elif key_input == 'a':
        for len in range(length):                           #縦
            for wid in range(length):                       #横
                compleate_map.append(result[length*wid+len])
    elif key_input == 'd':
        for len in range(length):                           #縦
            for wid in range(length):                       #横
                compleate_map.append(result[length*wid+(length-len+1)])

    return_str= ''

    for t in range(length):
        for y in range(length):            
            return_str += str(compleate_map[length*y+t])+' '
        return_str += '\n'
    return(compleate_map)

def serch0(input_map):
    where0 = []
    for i in range(len(input_map)):
        if input_map[i] == 0:
            where0.append(i)
    if len(where0) != 0:
        number2or4 = 2
        judge = random.randint(0,5)
        if judge == 6:
            number2or4 = 4
        change = where0[random.randint(1,len(where0))-1]
        del input_map[change]
        input_map.insert(change,number2or4)
    return(input_map)

for i in range(16):                                          #空のマップ製作
        first_map.append(0)

def game():
    length = 4
    map = serch0(map_generate(length))
    while True:
        return_str= ''
        for t in range(length):
            for y in range(length):            
                return_str += str(map[length*y+t])+' '
            return_str += '\n'
        print(return_str)

        key_input = input("↑:w\n↓:s\n←:a\n→:d\nreset:r\nsetting:m\n")

        if len(key_input) != 1 :
            print('No command!')
        
        elif key_input != 'w' and key_input != 'a' and key_input != 's' and key_input != 'd' and key_input != 'r' and key_input != 'm':
            print(key_input,len(key_input))
            print('No command!')

        elif key_input == 'r':
            ryorn = input('Reset the map?Y/n')
            if ryorn == 'Y'or ryorn == 'y':
                map = serch0(map_generate(length))
                print('reset')
            else:
                print('Cancel')
        elif key_input == 'm':
            syorn = input('Reset the map?Y/n')
            if syorn == 'Y' or syorn == 'y':
                print('Change the length. \n Now:'+str(length))
                new_length = input('How long it?')
                if int(new_length) % 1 > 0 or int(new_length) <= 1:
                    print('ERROR')
                else:
                    length = int(new_length)
                    map = serch0(map_generate(length))
            else:print('Cancel')
        else:
            map = serch0(map_result_put(key_input,no0(run_length(map,key_input,length),length),length))

game()

"""
現在判明しているバグ
数字が動いていなくてもコマンドが入力されれば新しく数字が出てきます。
その他、バグを発見された方はこのコメントを改行して書いてもらえるとありがたいです。匿名、記名は構いません。
コマンドの入力後、移動する場合がありますがコラボラトリーの使用上仕方がないものです。    修正不可
"""
