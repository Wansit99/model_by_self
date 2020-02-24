
# coding: utf-8

# In[ ]:


#%%
import os
path = r'C:\Users\Wansit\Desktop\第一篇 编程基础\数据\python基础\python基础\作业2和作业3'


# In[ ]:


class Processing():
    def __init__(self,path):
        self.path = path
        
    def made(self):#将图片文件读取出来，并将每个文件名称_标签 写入txt文件
        dirs = os.listdir(path)
        txt = open('{}/test.txt'.format(path),'a')
        for i in dirs:
            now_path = os.path.join(path,i)   
            now_dirs = os.listdir(now_path)
            for j in now_dirs:
                txt.writelines('{}_{}\n'.format(j,i))
        txt.close()
    def random(self):#打乱顺序，获取打乱后的txt文件
        txt = open('{}/test.txt'.format(path),'r')
        list = []
        for line in txt.readlines():
            list.append(line)
        random.shuffle(list)
        txt = open('{}/train.txt'.format(path),'a')
        lens = len(list)
        for line in list[:int(0.7*lens)]:
            txt.writelines('{}'.format(line))
        txt.close()
        
        txt = open('{}/test0.7.txt'.format(path),'a')
        for line in list[int(0.7*lens):]:
            txt.writelines('{}'.format(line))
        txt.close()


# In[ ]:


t = Processing(path)
t.made()
t.random()

