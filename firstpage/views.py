from django.shortcuts import render
#from django.shortcuts import render_to_response
from django.http import HttpResponse
#we will import pandas
import pandas as pd
import numpy as np

import pandas as pd
import seaborn as sns

import matplotlib.pyplot as plt


before=21

def index(request):
    
    return render(request, 'index.html', {'imp':False})


#this is user defined function to load the csv data into a  dataframe(name=csv)

#from django.views.decorators.cache import cache_control
#@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def result(request):
    from sklearn.ensemble import RandomForestRegressor
    from sklearn.model_selection import train_test_split
    from sklearn.metrics import mean_absolute_error as mae
    if request.method == "POST":
        global file
        file = request.FILES["myFile"]
        csv=pd.read_csv(file)
        print(csv)
        size=csv.shape
        global x
        x=csv.iloc[:,:]
        
        global t
        t=x.dtypes
        print(t)
        cont=x.select_dtypes(include=[np.number])
        disc=x.select_dtypes(exclude=[np.number])
        context={'rows':size[0],'columns':size[1], 'col_name':cont.columns,'disc_col_name':disc.columns,'data':csv}
        return render(request, "mmm.html",context)
    else:   
        return render(request, "index.html")

def saturation(request):
    return render(request, 'mmm.html', {'x':"uri"})

def imp_features(request):
    return render(request, 'mmm.html',{'x':"uri"})
    
def area_plot(request):
    return render(request, 'mmm.html',{'x':"uri",'y':"uri2"})    
       
##this is user defined function to go to the upload html page where is the upload button of csv file
def upload(request):
    return render(request, "upload.html")



def viewdb(request):
    return render(request, 'index.html')

def about(request):
    return render(request, 'resume.html')

def predictMPG(request):
    context={'scoreval':"scoreval",'summary':"reg summary"}
    return render(request, 'result.html',context)


def game(request):

    global before 
    before=21
    context={'win':True}
    return render(request, 'game.html',context)



def matchstick(request):
    
    
    z=int(request.POST.get('pick'))
    
    global before
    
    if(z>0 and z<5):
        after_user=before-z
        print(after_user)
        c=5-z
        after_comp=after_user-c
        before=after_comp
        if(after_comp>0):
            context={'second_time':True,'win':True,'user_pick':z,'after_user':after_user,'comp_pick':c,'after_comp':after_comp}
        else:
            context={'lost':True,'win':False}
    else:
        after_user=before-0
        print(after_user)
        c=0
        after_comp=after_user-c
        before=after_comp
        if(after_comp>0):
            context={'second_time':True,'win':True,'user_pick':z,'after_user':after_user,'comp_pick':c,'after_comp':after_comp}
        else:
            context={'lost':True,'win':False}
    return render(request, 'game.html',context)


def pareto(request):
    c1=request.POST.get('column1')
    c2=request.POST.get('column2')
    import matplotlib.pyplot as plt
    from io import StringIO
    from io import BytesIO
    import base64
    import urllib
    from matplotlib.ticker import PercentFormatter
    
    y=x.groupby(c1).sum().reset_index()
    y=y.sort_values(by=c2,ascending=False)
    y['cumpercentage']=y[c2].cumsum()/y[c2].sum()*100
    
    fig, ax=plt.subplots()
    ax.bar(y[c1],y[c2],color="orange")
    ax2 = ax.twinx()
    
    ax.plot(y[c1],y["cumpercentage"],color="red",marker="D",ms=7)
    ax2.yaxis.set_major_formatter(PercentFormatter(symbol=None, xmax=100))
    
    ax.tick_params(axis="y",colors="blue")
    ax2.tick_params(axis="y",colors="green")
    ax.set_xlabel(c1)
    ax.set_ylabel(c2)
    imgdata=StringIO()
    fig.savefig(imgdata, format='svg')
    imgdata.seek(0)
    
    uri = imgdata.getvalue()
    context={'something2':True , 'graph2':uri}
    return render(request, 'result.html',context)
    

def barplot(request):
    import matplotlib.pyplot as plt
    from io import StringIO
    from io import BytesIO
    import base64
    import urllib
    c1=request.POST.get('column1')
    c2=request.POST.get('column2')
    agg=request.POST.get('aggregation')
    if(agg=="sum"):
        y=x.groupby(c1).sum().reset_index()
    elif(agg=="average"):
        y=x.groupby(c1).mean().reset_index()
    
    fig=plt.figure()
    plt.bar(y[c1],y[c2])
    plt.xlabel(c1)
    plt.ylabel(c2)
    
    imgdata=StringIO()
    fig.savefig(imgdata, format='svg')
    imgdata.seek(0)
    
    uri = imgdata.getvalue()
    context={'something2':True , 'graph2':uri}
    return render(request, 'result.html',context)

def boxplot(request):
  import matplotlib.pyplot as plt
  from io import StringIO
  from io import BytesIO
  import base64
  import urllib
  import seaborn as sns
  c1=request.POST.get('column1')
  #c2=request.POST.get('column2')
  grp=request.POST.get('grp')
  
  fig=plt.figure()
  #plt.boxplot(x[c1])
  #x.boxplot(column=c1, by=grp)
  sns.boxplot(x=grp,y=c1,data=x)
  plt.xlabel(c1)
  plt.ylabel(c1)
  
  imgdata=StringIO()
  fig.savefig(imgdata, format='svg')
  imgdata.seek(0)
  
  uri = imgdata.getvalue()
  #buffer.close()
  
  
  context={'something2':True , 'graph2':uri}
  return render(request, 'result.html',context)


def scatterplot(request):
    import matplotlib.pyplot as plt
    from io import StringIO
    from io import BytesIO
    import base64
    import urllib
    c1=request.POST.get('column1')
    c2=request.POST.get('column2')
    fig=plt.figure()
    plt.scatter(x[c1],x[c2])
    plt.xlabel(c1)
    plt.ylabel(c2)
    imgdata=StringIO()
    fig.savefig(imgdata, format='svg')
    imgdata.seek(0)
    
    
    
    uri = imgdata.getvalue()
    #buffer.close()
    
    context={'something2':True , 'graph2':uri}
    return render(request, 'result.html',context)

def histogram(request):
    import matplotlib.pyplot as plt
    from io import StringIO
    from io import BytesIO
    import base64
    import urllib
    c1=request.POST.get('column1')
    bns=request.POST.get('bins')
    fig=plt.figure()
    plt.hist(x[c1], bins=abs(int(bns)))
    plt.xlabel(c1)
    plt.ylabel("frequency")
    imgdata=StringIO()
    fig.savefig(imgdata, format='svg')
    imgdata.seek(0)
    
    
    
    uri = imgdata.getvalue()
    #buffer.close()
    
    context={'something2':True , 'graph2':uri}
    return render(request, 'result.html',context)


def carry(request):
    return render(request, 'mmm.html',{'x':uri,'y':uri2,'z':uri3,'carry':True})  

def optimise(request):

    return render(request, 'result.html', {'scoreval':x_data.shape, 'summary':data2})
