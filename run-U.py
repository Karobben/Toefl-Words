#!/usr/bin/env python3.7
print("Loading the words list")
import argparse
import pandas as pd
import os
import time
import signal


#命令行输入参数处理
parser = argparse.ArgumentParser()
parser.add_argument('-i','-I','--input')     #输入文件
#获取参数
args = parser.parse_args()
INPUT = args.input
############################
def input_out(a_S):
  class InputTimeoutError(Exception):
    pass
  def interrupted(signum, frame):
    raise InputTimeoutError

  signal.signal(signal.SIGALRM, interrupted)
  signal.alarm(a_S)

  try:
    BB = input()
    signal.alarm(0)  # 读到输入的话重置信号
  except InputTimeoutError:
    BB = 'u'
  return BB
    #print('你的名字是：%s' % name)

def Review_words(INPUT):
    List=pd.read_csv(INPUT,sep='\t',header=None)
    List.index = List[1]
    print(List.index)
    NUM=1
    Y_choice = 'a'
    while Y_choice != "q":
        #print(List.index[NUM])
        NUM = NUM +1
        Word_explan =  List.loc[List.index[NUM]]
        colored = '\x1b[6;35;47m' +  List.index[NUM] + '\x1b[0m'
        print('\n\n\n\x1b[6;41;3m' ,  List.index[NUM] , '\x1b[0m\n\n\n\n')
        time.sleep(1)
        print('\n',Word_explan[2],'\n\n',Word_explan[3],'\n\n',Word_explan[4],'\n\n')
        print(str(Word_explan[5]).replace( List.index[NUM],colored),'\n')
        Y_choice = input_out(1)

def Classify_words(INPUT):
    NUM = 1
    List=pd.read_csv(INPUT,sep='\t',header=None)
    List.index = List[1]
    print("Recognize start")
    #print(Words_list[1][0])
    Y_choice2 = "a"
    #print("2=",Y_choice2)
    while Y_choice2 != "q" :
        #### the prat for "h" - start
        Word_explan =  List.loc[List.index[0]]
        #print(Word_explan[2],'\n\n',Word_explan[3],'\n\n',Word_explan[4],'\n\n')
        #colored = '\x1b[6;35;47m' +  List.index[0] + '\x1b[0m'
        #print(Word_explan[5].replace( List.index[0],colored),'\n')
        #### the part for "h" - end
        print('\n\n\x1b[6;97;6m' + List.index[0] + '\x1b[0m')  # the words with color
        print("\nRecoder:",NUM)
        time.sleep(1)
        os.system('clear')
        print("Do you know this?")
        Word_E= str(List.index[0])
        Y_choice2 = input()
        if Y_choice2 == Word_E :
            print ("\x1b[3;46;6m Your Are Right !! \x1b[0m")
            Word_explan =  List.loc[Word_E]
            print(Word_explan[2],'\n\n',Word_explan[3],'\n\n',Word_explan[4],'\n\n')
            colored = '\x1b[6;35;47m' +  Word_E + '\x1b[0m'
            print(str(Word_explan[5]).replace( Word_E,colored),'\n')
            Y_choice2 = input()
            if Y_choice2 == 'h':
                Word_explan =  List.loc[List.index[0]]
                print(Word_explan[2],'\n\n',Word_explan[3],'\n\n',Word_explan[4],'\n\n')
                colored = '\x1b[6;35;47m' +  List.index[0] + '\x1b[0m'
                print(Word_explan[5].replace( List.index[0],colored),'\n')
            elif Y_choice2 == 'd':
                List = List.drop(List.index[0])
                order_1 = "awk 'NR==1{print}' " + INPUT +  " >tmp "
                os.system(order_1)
                os.system('cat tmp >> My.DB')
                order_2 = "sed -i 1d " + INPUT
                os.system(order_2)
                NUM=NUM+1
            elif Y_choice2 == 'f':
                List = List.drop(List.index[0])
                order_1 = "awk 'NR==1{print}' " + INPUT +  " >tmp"
                os.system(order_1)
                os.system('cat tmp >> Fm.DB')
                order_2 = "sed -i 1d " + INPUT
                os.system(order_2)
                NUM=NUM+1
            elif Y_choice2 == 'u':
                List = List.drop(List.index[0])
                order_1 = "awk 'NR==1{print}' " + INPUT +  " >tmp"
                os.system(order_1)
                os.system('cat tmp >> Uf.DB')
                order_2 = "sed -i 1d " + INPUT
                os.system(order_2)
                NUM=NUM+1
            elif Y_choice2 == 't':
                List = List.drop(List.index[0])
                order_1 = "awk 'NR==1{print}' " + INPUT +  " >tmp"
                os.system(order_1)
                os.system('cat tmp >> Tu.DB')
                order_2 = "sed -i 1d " + INPUT
                os.system(order_2)
                NUM=NUM+1
            elif Y_choice2 == 'm':
                #grep from News
                order_1 = "grep -w -i " + List.index[0] + " all.db"
                AAA=os.popen(order_1).read()
                colored = '\x1b[6;42;30m' +  List.index[0] + '\x1b[0m'
                AAA=str(AAA).replace( List.index[0],colored)
                print(AAA)
                #grep from Toefl
                order_1 = "grep -w -i " + List.index[0] + " T.db"
                AAA=os.popen(order_1).read()
                colored = '\x1b[6;45;30m' +  List.index[0] + '\x1b[0m'
                AAA=str(AAA).replace( List.index[0],colored)
                print(AAA)
            elif Y_choice2 == 'help':
                print("pleas enter:\nd(deleted it)\nf(familiar word)\nu(unfamiliar word)\nt(totally unknow words)\nh(hint)\nm(more)\nq(quit)")
        else:
            print('\x1b[3;45;6mWrong\x1b[0m')


    os.system('rm tmp')

def Choice_challenge():
    print("Let the fun begin")
    print(Words_list)

def Searching_mode():
    print("Search wors")

print("Loading is done")

Y_choice = "a"
while Y_choice != "q" :
    print("Chose a type")
    Y_choice = input()
    if Y_choice == "1":
        Review_words(INPUT)
    elif Y_choice == "2":
        Classify_words(INPUT)
    elif Y_choice == "3":
        Choice_challenge()
    elif Y_choice == "4":
        Searching_mode()
    else:
        print(" pleas chose 1,2,3,4")
