#coding=utf-8
import gensim
import pandas as pd
def my_function():
 
    model = gensim.models.Word2Vec.load('C:\\Users\\DELL\\Desktop\\NLP\\lesson04\\zhiwiki_news.word2vec')
    print(model.similarity('������','����'))  #���ƶ�Ϊ0.60256344
    print(model.similarity('������','�㽶'))  #���ƶ�Ϊ0.49495476
    # print(model.similarity('�˹�����','������'))
    # print(model.similarity('�ε�', '������'))
 
    result = pd.Series(model.most_similar(u'����Ͱ�')) #���ҽ�����ش�
    print(result)
    result1 = pd.Series(model.most_similar(u'�ʹ�'))
    print(result1)
    print(model.wv['�й�']) #�鿴�й��Ĵ���������������Ĵ�������
 
if __name__ == '__main__':
    my_function()
