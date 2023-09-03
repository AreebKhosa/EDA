# %%
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import plotly.graph_objects as go
import plotly.express as px

# %% 
#  for find the data types
def differentiate(data ,drop = False):
    if drop == True:
        data = data.dropna()
    integers = data.select_dtypes(include=['int','float'])
    categoric = data.select_dtypes(include=['object'])
    boolean = data.select_dtypes(include=['bool'])
    return integers,categoric,boolean

# %%
# descriptive statistcs function for numeric data types
def describe_data(data, skip_none = True , rep_val = False , trans = True):
    # data = pd.DataFrame(data)
    # data = data.dtypes(include=['int','float'])
    if data.dtypes == 'int64' or data.dtypes == 'float64':
        Varible_type = "Numeric Variable"
        if rep_val == True:
            replace = data.fillna(0,  inplace=True)
        skewness = data.skew(skipna = skip_none)
        variance = data.var(skipna = skip_none)
        kurtosis = data.kurtosis(skipna = skip_none)
        mean = data.mean(skipna = skip_none)
        median = data.median(skipna = skip_none)
        count = data.count()
        std = data.std(skipna = skip_none)
        min = data.min(skipna = skip_none)
        max = data.max(skipna = skip_none)
        dest = len(data.unique())
        dist_per = dest/len(data)*100
        dist_per = '%.2f' % dist_per+"%"
        miss = data.isna().sum()
        miss_per = miss/len(data)*100
        miss_per = '%.2f' % miss_per+"%"
        zeros = (data==0).sum()
        zero_per = zeros/len(data)*100 
        zero_per = '%.2f' % zero_per+"%"
        q1 = data.quantile(q =0.25)
        q3 = data.quantile(q =0.75)
        iqr = q3-q1
        variation = data.std()/data.mean()
        

        description = {
            'Varible_type':Varible_type,
            'Min':min,
            "Q1" : q1,
            'Median':median,
            "Q3" : q3,
            'Max':max,
            "Range":max,
            "IQR":iqr,
            'Mean':mean,
            'Standard Deviation':std,
            'Coefficient of Variation':variation,
            'Variance':variance,
            'Skewness':skewness,
            'Kurtosis':kurtosis,
            # these are short description
            'Zeros':zeros,
            "Zero(%)":zero_per,
            "Unique":dest,
            "Unique(%)":dist_per,
            "Miss":miss,
            "Miss(%)" : miss_per,
            'Count':count,      
        }
    else: 
        Varible_type = "Categoric Variable"
        dest = len(data.unique())
        dist_per = dest/len(data)*100 
        dist_per = '%.2f' % dist_per+"%"
        miss = data.isna().sum()
        miss_per = miss/len(data)*100
        miss_per = '%.2f' % miss_per+"%"
        count = data.count()
        description = {
            'Varible_type':Varible_type,
            "Unique":dest,
            "Unique(%)":dist_per,
            "Miss":miss,
            "Miss(%)" : miss_per,
            'Count':count,
        }
    return description

# %%
# descriptive statistcs function for numeric data types
def describe_DataFrame(data, skip_none = True , rep_val = False , trans = True):
    data = pd.DataFrame(data)
    data = data.select_dtypes(include=['int','float'])
    # if data.dtypes == 'int64' or data.dtypes == 'float64':
    Varible_type = "Numeric Variable"
    if rep_val == True:
        data.fillna(0,  inplace=True)
    skewness = data.skew(skipna = skip_none)
    variance = data.var(skipna = skip_none)
    kurtosis = data.kurtosis(skipna = skip_none)
    mean = data.mean(skipna = skip_none)
    median = data.median(skipna = skip_none)
    count = data.count()
    std = data.std(skipna = skip_none)
    min = data.min(skipna = skip_none)
    max = data.max(skipna = skip_none)
    miss = data.isna().sum()
    miss_per = miss/len(data)*100
    miss_per = round(miss_per,3)
    zeros = (data==0).sum()
    zero_per = zeros/len(data)*100 
    zero_per = round(zero_per,3)
    q1 = data.quantile(q =0.25)
    q3 = data.quantile(q =0.75)
        

    description = {
        'Varible_type':Varible_type,
        'Mean':mean,
        'Median':median,
        'Standard Deviation':std,
        'Skewness':skewness,
        'Variance':variance,
        'Kurtosis':kurtosis,
        'Min':min,
        'Max':max,
        'Count':count,
        'Zeros':zeros,
        "Zero(%)":zero_per,
        "Miss":miss,
        "Miss(%)" : miss_per,
        "Q1" : q1,
        "Q3" : q3
    }
    description = pd.DataFrame(description)
    
    description = description.transpose()
    return description


def find_values(data):
    length = len(data.columns)
    miss = data.isna().sum().max()
    per = miss/len(data)*100
    per = '%.2f' % per+"%"
    total = len(data)
    duplicat = data.duplicated().sum()

    dic = {
        "length":length,
        "tot": total,
        "miss":miss,
        "per":per,
        "dup":duplicat,
    }

    return dic
# %%
#  for find the data types of single variable
def different(data):
    data_type = data.dtypes
    data_name = ""
    if data_type == 'O':
        data_name = "Categoric Variable"
    elif data_type == 'int64':
        data_name = "Numeric Variable"
    elif data_type == 'float64':
        data_name = "Numeric Variable"
    elif data_type == 'bool':
        data_name = "Boolean Variable"

    return data_name

# %%
# function for getting categoric values
def cat_count(data):
    val_count = pd.DataFrame(data.value_counts())
    val_count.rename(columns={val_count.columns[0]: 'Counts'}, inplace = True)
    val_count.rename_axis('Values', axis=1,inplace=True)

    val_count['percent'] = round((val_count["Counts"] / len(data) * 100),3)
    return val_count

# %%
# Correlation function for numeric data
def correlation(data,drop = False):
    if drop == True:
        data = data.dropna()
    integers = data.select_dtypes(include=['int','float'])
    cor = round(integers.corr(),3)
    return cor

# %%
# here we are making function for descriptive result priting
def descriptive_results(data):
    dd = describe_data(data),
    dd = dd[0]
    des_dic = list(dd.items())
    return des_dic

#%%
# here we are creating a plot function
def count_plot(data,wid_hig = False ,wid = 7,hig =5):
    if wid_hig == True:
        fig = plt.figure(figsize=(wid,hig))
    else:
        fig = plt.figure()
    counts = cat_count(data)
    if len(counts) <= 12:
        counts.reset_index(inplace=True)
        ax = sns.barplot(y='index', x="percent", data=counts,)

        sns.despine(offset=10, trim=True)
        ax.bar_label(ax.containers[0])
        return fig
    else:
        return "Out Of Range"

    
#%%
# here we are creting box plot
def box_voilen(data , y_axis ,x_lable ,width = 0.3, kind="box"):
    fig = sns.catplot(data=data,y=y_axis, kind=kind,width = width)
    fig.set_xticklabels(rotation=30)
    fig.set_xlabels(x_lable)
    fig.set_ylabels("Values")
    return fig

# %%
# here we are creating donut plot......
def donut_plot(data,hole = 0.4):
    # Use `hole` to create a donut-like pie chart
    counts = cat_count(data)
    if len(counts) <= 15:
        counts.reset_index(inplace=True)
        fig = go.Figure(data=[go.Pie(labels=counts["index"], values=counts["Counts"], hole=hole)])
        return fig
        
    else:
        return "Out Of Range"

#%%
# here we are creating plotly bar chart
def plotly_bar_plot(data):
    counts = cat_count(data)
    if len(counts) <= 15:
        counts.reset_index(inplace=True)
        fig = px.bar(counts, y='Counts', x='index', text_auto='.2s')
        return fig
        
    else:
        return "Out Of Range"

#%%
# here  we create histogram
def plotly_hist_plot(data,x_axis,bargap=0.05):
    fig = px.histogram(data, x=x_axis,
                    marginal="box", # or violin, rug
                    hover_data=data.columns)
    fig.update_layout(bargap=bargap)
    return fig

#%%
# nan values plot
def nan_val(data): 
    nan_columns = []
    nan_values = []

    for column in data.columns:
        nan_columns.append(column)
        nan_values.append(data[column].value_counts().sum())

    fig = px.bar(y=nan_values, x=nan_columns, text_auto='.2s')
    fig.update_layout(
        xaxis_title="Variable",
        yaxis_title="Nan Values",
    )
    return fig


#%%
# here we create plotly box plot
def plotly_box_plot(data,name):
    fig = go.Figure()
    fig.add_trace(go.Box(y=data, name=name, 
        jitter=0.3,
        pointpos=-1.8,
        boxpoints='all',
        ))
    return fig


#%%

#here is the function for creating dist plot
def plotly_dist_plot(data,name):
    fig = go.Figure()
    fig.add_trace(go.Violin(x=data, line_color='lightseagreen', name=name, y0=0))
    # fig.add_trace(go.Violin(x=data, line_color='red', name= 'starting_price', y0=0))

    fig.update_traces(orientation='h', side='positive', meanline_visible=False)
    fig.update_layout(xaxis_showgrid=False, xaxis_zeroline=False)

    fig.update_layout(title=f'<b>Distribution Plot of {name}<b>',
                    xaxis_title='GDP per capita',
                    template="plotly_dark",
                    showlegend=True,
                    paper_bgcolor="white",
                    plot_bgcolor='white', 
                    font=dict(
                        color ='black',
                        )
                    )
    return fig

#%%
# here we created function for creating high corelation of variable
def find_strong_rel(df_corr):
    high_cor = []
    less_cor = []
    for k in df_corr.columns:
        j = 0
        for i in range(len(df_corr[k])):
            if df_corr[k][j] > 0.7 and df_corr[k][j] < 1:
                high_cor.append([k,df_corr.index[j]])
            elif df_corr[k][j] < -0.5:
                less_cor.append([k,df_corr.index[j]])
            j +=1
    return less_cor,high_cor

#%%
# here we write a function for printing unique values 
def unique_count(data):
    uni_count=[]
    j=0
    for i in data:
        coun = len(data[i].unique())
        if coun <= 15:
            uni_count.append(i)
        j+=1
    return uni_count


#%%
def pie_plot(data):
    # Use `hole` to create a donut-like pie chart
    counts = cat_count(data)
    if len(counts) <= 40:
        counts.reset_index(inplace=True)
        fig = go.Figure(data=[go.Pie(labels=counts["index"], values=counts["Counts"], )])
        # fig = px.pie(data,
        #      values=counts["index"],
        #      names=counts["Counts"],)
        return fig
        
    else:
        return "Out Of Range"

#%%
# side histogram
def side_histogram_plot(data,x_axis,wid,hig,bargap=0.02,):
    fig = px.histogram(data, x=x_axis,
                    hover_data=data.columns)
    fig.update_layout(bargap=bargap)
    fig.update_layout(
    autosize=False,
    width=wid,
    height=hig,)
    return fig