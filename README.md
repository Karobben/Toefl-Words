# Toefl-Words
For remeber the toefl words with your personal style

for run:

python3.* run2.py -i Word-kan-2

python3.* run-t2.py -i Word-kan-2 (this for android termux paltform. due ot some reseaon, there has not suspant wait for input, you must input something or just input Enter to continue. )

chose:
1- quick review: all the words in the list will be printed with 1s suspend. once you input "q", the review will be stopped soon.

2- classify the words: the words will be classified to 4 difference files for further study.

                       input d, delete. the words will go to My.DB (My words)
                       
                       input f, familliar, the words will go to Fm.DB (familiar words)
                       
                       input u, unfamilliar, the words will go to Uf.DB (unfamiliar wors)
                       
                       input t, totally unknown, the words will go to Tu.DB (totally unknow words)
                       
                       input h, show the pronunciation and translation of words, and the sentence with this words on toefl or News
                       input m, the words show on toefl papers and News (it the do show on this database)
                       
                       input hlep, if you forget above...
                       
                       attention : if there have hesitated inner 2s, the words will go to Uf.DB for you.

3- under developing

4- please wait


Word-kan: toefl words and Houge words. The words are sorted by the frequecy of they showed on toefl reading materials.
T.db: tpo reading and the reading paper of the writing.
all.db: recently News from Washington post, USA today, Nature.

hope will you get good grades soon!



正确使用姿势：

1, chmod +x run*  # 给所有程序执行权限

2, ./run-2.py -i Word-Kan-2  # 开始对总库筛选。 时间可能会要的比较多。 输入1 是浏览。 输入2 是分类。 分类可选择 d, f, u, t （前面解释了）

3, ./run-U.py -i Uf.DB（任何单词库都可以，比如换成 My.DB） # 这一步就可以进行拼写练习了。 其实你也大可跳过第一步，直接进行这一步。为了方便复习，这一步被分选的词，都会丢到一天命名的文件夹中。所以每天都有记录，想回头复习哪天，就哪天

4, ./through  -i Uf.DB  -t 3 # 一样，可以看别的 词库。 t后面接时间，可不弄，默认个停留3秒。同事在里面，也可以通过按 回车键直接跳到下一个单词

5, ./run-R.py -i *.DB # 该程序用于复习分选后的数据库。run-repeat 该程序执行以后，选择了 u 以后，单词会继续回到本库的最底层，并不会跑到新的库。
但当使用了f, d or t 选项后，单词变回跑到对应的库里面去。 所以本程序用于复习之前分选好的库

小技巧：

如果有排序需求的，可以直接用 sort exp: sort Un.DB > tmp; mv tmp Un.DB

整合多个词库成一个  cat 1.DB 2.DB 3.DB > 4.DB

简单粗暴好用，轻量
