import os


path = "idea.txt"
EXISTING = '' # 既存内容を書き込む


with open(path, mode='r',encoding='utf-8') as f: 
    # 既存内容の保存
    while True:
        s_line = f.readline()
        EXISTING += s_line
        if not s_line:
            break


def out_put_idea(j: 10):
    # アイデアを10個出す
    idea = []

    print("アイデアを10個出してください\n")
    for i in range(j):
        idea += [str(input("{i}>".format(i = i + 1)))]

    # 一つ選ぶ
    print("では、上の内容から良いアイデアを一つだけ選んでください\n")
    while True:
        try:
            number = int(input(">>"))
            if number <= 0 or 11 <= number:
                raise Exception
            break
        except:
            print("1~10の数字を入力してください")
    
    return idea[number - 1]
        

def write_idea():
    # 一つ書き込み
    global EXISTING

    with open(path, mode='w', encoding='utf-8') as f:
        f.write(EXISTING)
        idea = out_put_idea(10)
        EXISTING += idea
        f.write('\n' + idea)
        print("ファイルに保存しました。")
        

def confirm_past_idea():
    # 今まで出してきたアイデアのログ
    # mode=log
    print(EXISTING)

def output_one():
    # 一個のアイデアを出して確認してからファイル保存
    # mode=one
    global EXISTING

    print("一つだけアイデアを出してください\n")
    one_idea = input('>>')
    with open(path, mode='w', encoding='utf-8') as f:
        f.write(EXISTING)
        f.write('\n' + one_idea)
    print("ファイルに保存しました")
    EXISTING +='\n' + one_idea

def brainstorm():
    # 思いつく限りたくさんだす
    # mode=brs
    global EXISTING
    i = 1
    idea = ''

    print("思いつく限りたくさんのアイデアを出し続けてください\n"+ \
          "(何も入力せずにEnterを押すと、モードを終了します)")
    while True:
        puted_idea = input('{i}>'.format(i = i))
        if puted_idea == '':
            break
        idea += '\n' + puted_idea
        i += 1
    EXISTING += idea
    print("ブレインストーミングを終了します")

    with open(path, mode='w', encoding='utf-8') as f: 
        f.write(EXISTING)
    print("ファイルに保存しました")


def apply_key():...
    # TODO パスワード＋ロックかける

def help():
    # help情報を示す。
    print("1) log\n" +
          "2) one\n" +
          "3) brs\n" +
          "4) end")

def select_mode(mode):
    # modeの選択＆そのモードの実行

    if mode == "log" or mode == "1":
        confirm_past_idea()
    elif mode == "one" or mode == "2":
        output_one()
    elif mode == "brs" or mode == "3":
        brainstorm()
    elif mode == "end" or mode == "4":
        print("しゅーりょーします")
        return 0
    elif mode == "mode" or mode == "help" or mode == "exit":
        help()
    else:
        print("そのモードはありません")


if __name__ == "__main__":
    try:
        write_idea()
        
        print("Enterキーを押して終了してください")
        input('') # Enterを押して終了

    except KeyboardInterrupt: # crtl + c or delete ?
        """
        モードの追加
        過去のアイデアのlog確認など
        """
        print("\nここはまだ実験中です\nごりょーしょーください")
            
        while True:    
            mode = input('mode>')
            motivation = select_mode(mode)
            if motivation == 0:
                break

        print("Enterキーを押して終了してください")
        input('') # Enterキーを押して終了
