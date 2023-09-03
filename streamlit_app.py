import streamlit as st
import pandas as pd
import numpy as np 
import seaborn as sns
import matplotlib.pyplot as plt
import streamlit_nested_layout
import Descriptive_functions as des_fun
import plotly.express as px
import openpyxl


st.set_page_config(page_title="First app",page_icon='tada',layout='wide')

data_name = []
with st.container():
    st.subheader('Hi : Welcome to Our Site')
    st.title('Here You Can Do Descriptive Statictics')
    st.header("With Zero Line of Code")
    st.write('---')


# here we are add file upload button
with st.container():
    left_col ,right_col = st.columns(2)
    with left_col:
        st.text("""
                Here you can do descriptive statistic without having any knowladge....\n
                Only you have to upload your Data HERE........\n
                InshaAllah we will make best resutls of your Data..."""
            )
    # file upload button
    with right_col:
        data_file = st.file_uploader('Upload a CSV / Excel. . . . . . . .')
        data_name.append(data_file)

    st.text("\n")
    st.write('---')



def Home():
# now adding title and headings to web app

    # Dictionary
    Overview_dic = [
        "Number of Variables",
        "Number of Observation",
        "Max Total Missing",
        "Max Total Missing(%)",
        "Total Size of Memory",
        "Numeric Variable",
        "Categoric Variable",
        "Boolean Variable"
    ]

    with st.container():

        
        if data_file is not None:
            file_details = {"filename":data_file.name, "filetype":data_file.type,"filesize":data_file.size}
            # here write file detial
            st.write(file_details)
            
            # here we read data and make it as a data frame
            try:
                data = pd.read_csv(data_file)
            except:
                data = pd.read_excel(data_file,engine='openpyxl')
            # here we are calling our functions which we created earlier
            data_type = des_fun.differentiate(data)
            
            data_set = des_fun.find_values(data=data)


            st.markdown("<h1 style='text-align: center; color: grey;'>Results</h1>", unsafe_allow_html=True)

            st.write("---")
            # here we crated a column for describing the data::>..........
            info_col = st.columns([0.5,4,4,0.5])
            with info_col[1]:
                # here we add heading of first column
                st.subheader("Dataset Info")
                inner_col = st.columns(2)
                with inner_col[0]:
                    # For write headings
                    for i in range(len(Overview_dic)-3):
                        st.write(f"**{Overview_dic[i]}**")

                with inner_col[1]:
                    for i in data_set:
                        st.write(f"{data_set[i]}")


            with info_col[2]:
                # here we add heading of Second column
                st.subheader("Variable Types")

                # column of varialble types
                inner_col = st.columns(2)
                with inner_col[0]:

                    # For writing name
                    for i in range(len(Overview_dic)-3,len(Overview_dic)):
                        st.write(f"**{Overview_dic[i]}**")

                
                with inner_col[1]:

                    # here we are using loop for display value of variable
                    for i in data_type:
                        st.write(f"{len(i.columns)}")

            st.write("---")

            # here we create column for describing single variable

            for j  in range(len(data.columns)):
                with st.container():

                    # here we calling function "ending_price"
                    des_results = des_fun.descriptive_results(data= data[data.columns[j]])
                    check_data = des_fun.different(data[data.columns[j]])
                    # print(check_data)


                    # print(len(des_results))
                    # print(des_results[0][1])
                    # print(i)
                    
                    st.markdown(f"<h2 style='text-align: center; color: grey;'>{data.columns[j]}</h2>", unsafe_allow_html=True)
                    st.write("---")

                    Variable_col = st.columns([2.5,5,3])
                    with Variable_col[0]:
                        st.write("\n")

                        # here we entered variable name and its type
                        st.subheader(data.columns[j])
                        st.write(f"**{check_data}**")
                        
                    # here we put some statistics
                    with Variable_col[1]:
                        st.write("\n")
                        # here we are creating two columns mor
                        inner_col = st.columns(2)
                        with inner_col[0]:

                            # for describing data
                            inner_info_col = st.columns(2)
                            with inner_info_col[0]:

                                # here we run loop for get values
                                if check_data == "Numeric Variable":
                                    for i in range(16,21):
                                        st.write(f"**{des_results[i][0]}**")
                                
                                else :
                                    for i in range(1,6):
                                        st.write(f"**{des_results[i][0]}**")


                            
                            # here we add basic info values of data
                            with inner_info_col[1]:

                                # here we run loop for get values
                                
                                if check_data == "Numeric Variable":
                                    for i in range(16,21):
                                        st.write(f"{des_results[i][1]}")
                                
                                elif check_data == "Categoric Variable" :
                                    for i in range(1,6):
                                        st.write(f"{des_results[i][1]}")

                        with inner_col[1]:

                            # for describing data
                            inner_info_col = st.columns(2)
                            if check_data == "Numeric Variable":
                                with inner_info_col[0]:

                                    # here we add values
                                    st.write("**Mean**")
                                    st.write("**Minimum**")
                                    st.write("**Maximum**")
                                    st.write("**Zero(%)**")
                                
                                with inner_info_col[1]:

                                    # here we add values
                                    st.write(f"{des_results[8][1]:.2f}")
                                    st.write(f"{des_results[1][1]:.2f}")
                                    st.write(f"{des_results[5][1]:.2f}")
                                    st.write(f"{des_results[15][1]}")

                    # here we have to make small chart
                    with Variable_col[2]:
                        # here we are creating plots
                        if check_data == "Categoric Variable":
                            try:
                                fig = des_fun.count_plot(data=data[data.columns[j]])
                                st.pyplot(fig)
                            except:
                                st.write("Values are to many")

                        elif check_data == "Numeric Variable":

                            # here we created dis plot
                            fig = des_fun.side_histogram_plot(data=data,x_axis=data.columns[j],wid=400,hig=300)
                            st.plotly_chart(fig)
                            
                    # here we are create expander
                    with st.expander("See Explanation"):

                        # here we are creating tabs for inner col for numeric data
                        if check_data == "Numeric Variable":
                            num_tab = st.tabs(["Statistics", "Charts", "Common Values"])
                            with num_tab[0]:

                                # here we created column for expander statistics
                                tab_col = st.columns([1,3,1,3,1])
                                # quanntile stats column
                                with tab_col[1]:

                                    # heading
                                    st.markdown("<h5 style='text-align: center; color: grey;'>Quantile Statistics</h5>", unsafe_allow_html=True)

                                    inner_tab_col = st.columns(2)
                                    with inner_tab_col[0]:

                                        # here we run loop for get quantile values
                                        for i in range(1,8):
                                            st.write(f"**{des_results[i][0]}**")
                                    
                                    
                                    with inner_tab_col[1]:

                                        # here we run loop for get descriptive values
                                        for i in range(1,8):
                                            st.write(f"{des_results[i][1]:.2f}")
                                    
                                # descriptive stats column
                                with tab_col[3]:

                                # heading
                                    st.markdown("<h5 style='text-align: center; color: grey;'>Descriptive Statistics</h5>", unsafe_allow_html=True)

                                    inner_tab_col = st.columns(2)
                                    with inner_tab_col[0]:

                                        # here we run loop for get descriptive values
                                        for i in range(8,14):
                                            st.write(f"**{des_results[i][0]}**")
                                        
                                    
                                    with inner_tab_col[1]:

                                        # here we run loop for get descriptive values
                                        for i in range(8,14):
                                            st.write(f"{des_results[i][1]:.2f}")

                            # here we are creating charts for numeric data
                            with num_tab[1]:
                                chart_tab_col = st.columns([5,1,5])

                                with chart_tab_col[0]:

                                    st.markdown(f"<h3 style='text-align: center; color: grey;'>Histogram</h3>", unsafe_allow_html=True)
                                    # here we created dis plot
                                    fig = des_fun.plotly_hist_plot(data=data ,x_axis=data.columns[j])
                                    st.plotly_chart(fig, use_container_width=True)
                                
                                with chart_tab_col[2]:

                                    st.markdown(f"<h3 style='text-align: center; color: grey;'>Box</h3>", unsafe_allow_html=True)
                                    fig = des_fun.plotly_box_plot(data=data[data.columns[j]],name=data.columns[j])
                                    st.plotly_chart(fig, use_container_width=True)

                        elif check_data == "Categoric Variable":
                            cat_tab = st.tabs(["Common Value", "Charts",])
                            with cat_tab[0]:
                                cat_data = des_fun.cat_count(data=data[data.columns[j]])
                                st.table(cat_data.head())
                            
                            with cat_tab[1]:
                                chart_tab_col = st.columns([5,1,5])
                                with chart_tab_col[0]:

                                    try:
                                        st.markdown(f"<h3 style='text-align: center; color: grey;'>Donut Plot</h3>", unsafe_allow_html=True)
                                        # here we created dis plot
                                    
                                        fig = des_fun.donut_plot(data=data[data.columns[j]])
                                        st.plotly_chart(fig, use_container_width=True)
                                    except:
                                        st.markdown(f"<p style='text-align: center; color: grey;'>To many values to plot</p>", unsafe_allow_html=True)
                                    
                                with chart_tab_col[2]:

                                    try:
                                        st.markdown(f"<h3 style='text-align: center; color: grey;'>Bar Plot</h3>", unsafe_allow_html=True)
                                        # here we created dis plot
                                    
                                        fig = des_fun.plotly_bar_plot(data=data[data.columns[j]])
                                        st.plotly_chart(fig, use_container_width=True)
                                    except:
                                        st.markdown(f"<p style='text-align: center; color: grey;'>To many values to plot</p>", unsafe_allow_html=True)
        
            #for nan values
            col = st.columns([3,8,3])
            with col[1]:
                st.markdown(f"<h3 style='text-align: center; color: grey;'>Nan Value Plot</h3>", unsafe_allow_html=True)
                st.plotly_chart(des_fun.nan_val(data=data))

                        



def Correlation():
    st.markdown("# Correlation ❄️")
    st.sidebar.markdown("#Pearson 's Correlation ❄️")
    if data_file is not None:
        file_details = {"filename":data_file.name, "filetype":data_file.type,"filesize":data_file.size}
        # here write file detial
        
        # here we read data and make it as a data frame
        try:
            data = pd.read_csv(data_file)
        except:
            data = pd.read_excel(data_file,engine='openpyxl')
        # here we are calling our functions which we created earlier
        data_type = des_fun.differentiate(data)

        colorscales = px.colors.named_colorscales()

    def change_colorscale(cor,sel_col,hig ,wid):
        
        # print(type(height))
        selected_col = sel_col+"_r"
        fig = px.imshow(cor,text_auto=True,color_continuous_scale=selected_col)
        fig.update_layout(
            width = wid,
            height=hig,)
        st.plotly_chart(fig)

    if data_file is not None:
        with st.container():
            
            cor = des_fun.correlation(data=data)

            outer_col = st.columns([3,8,3])
            with outer_col[1]:
                
                color_select = st.selectbox(
                    'Select Categoric Values',colorscales,4
                )
                height = st.slider('Adjust Height', 400, 800, 600)
                width = st.slider('Adjust Width', 400, 800, 650)
                
            cor_col = st.columns([2,8])
            with cor_col[1]:
                cor_mat = change_colorscale(cor,sel_col = color_select ,hig = height ,wid = width)

            outer_col = st.columns([3,8,3])
            with outer_col[1]:

                st.subheader("Alerts")
                low,high = des_fun.find_strong_rel(cor)
                hig_val = []
                low_val = []
                if high == []:
                    st.warning("No Positive correlated values")
                else:
                    for i in range(len(high)):
                        st.write(f"{i} : **{high[i][0]}** is highly positive Correlated with **{high[i][1]}**")
                        hig_val.append(i)
                if low == []:
                    st.warning("No Strong Negative correlated values")
                else:
                    for i in range(len(low)):
                        st.write(f"**{low[i][0]}** is highly Strong Correlated with **{low[i][1]}**")
                        low_val.append(i)

                
                st.markdown("<h4 style='text-align: center; color: grey;'>Scatter Plots of Co-Related Variables</h4>", unsafe_allow_html=True)
                # st.write("**Strongly Positive Co-Related Variables**") 


                if high == []:
                    st.warning("No Strong Positive correlated values")
                else:
                    pos_cor = st.selectbox(
                        'Positive Correlated Variables',hig_val,0
                    )
                    fig = px.scatter(data, x=high[pos_cor][0], y=high[pos_cor][1], trendline="ols")
                    st.plotly_chart(fig)
                    
                if low == []:
                    st.warning("No Strong Negative correlated values")
                else:
                    pos_cor = st.selectbox(
                        'Negative Correlated Variable',low_val,0
                    )
                    fig = px.scatter(data, x=low[pos_cor][0], y=low[pos_cor][1], trendline="ols")
                    st.plotly_chart(fig)

                        

def Intrective_charts():

    def selected_bar(plot_selection,data,col_name):
        if plot_selection == "Bar":
            dat = pd.DataFrame(data)
            x_axis_val = st.selectbox(
            'Select Categoric Values',col_name,0
            )
            try:
                st.subheader(x_axis_val)
                fig = des_fun.plotly_bar_plot(data=data[x_axis_val])
                st.plotly_chart(fig, use_container_width=True)
            except:
                st.write("sorry")
            
    
    def selected_donut(plot_selection,data,col_name):
        if plot_selection == "Donut":
            dat = pd.DataFrame(data)
            x_axis_val = st.selectbox(
            'Select Categoric Values',col_name,0
            )
            # print(dat[x_axis_val].value_counts())
            try:
                st.subheader(x_axis_val)
                fig = des_fun.donut_plot(data=dat[x_axis_val])
                st.plotly_chart(fig)
            except:
                st.write("sorry")

    def selected_pie(plot_selection,data,col_name):
        if plot_selection == "Pie":
            dat = pd.DataFrame(data)
            x_axis_val = st.selectbox(
            'Select Categoric Values',col_name,0
            )
            # print(dat[x_axis_val].value_counts())
            try:
                st.subheader(x_axis_val)
                fig = des_fun.pie_plot(data=dat[x_axis_val])
                st.plotly_chart(fig)
            except:
                st.write("sorry")

    def selected_dist(plot_selection,data,col_name):
        if plot_selection == "Distribution Plot":
            x_axis_val = st.selectbox(
            'Select Distribution Values',col_name,0
            )
            # st.write(data[x_axis_val])
            col = data.columns
            for i in col:
                if i == x_axis_val:
                    col = i
            fig = des_fun.plotly_dist_plot(data=data[x_axis_val],name=col)
            st.plotly_chart(fig)

    def selected_2d_bar(plot_selection,data,x_axis,y_axis):
        if plot_selection == "2d Bar":
            x_axis_val = st.selectbox(
            'Select X-axis Values',x_axis,0
            )
            y_axis_val = st.selectbox(
            'Select Yaxis Values',y_axis,2
            )
            fig = px.bar(data, x=data[x_axis_val], y=data[y_axis_val])
            st.plotly_chart(fig)
            
    def selected_Hist(plot_selection,data,x_axis):
        if plot_selection == "Histogram":
            x_axis_val = st.selectbox(
            'Select X-axis Values',x_axis,0
            )
            y_axis_val = st.selectbox(
            'Select Yaxis Values',x_axis,1
            )
            fig = px.histogram(data, x=data[x_axis_val], y=data[y_axis_val],
                            marginal="box", # or violin, rug
                            hover_data=data.columns)
            fig.update_layout(bargap=0.05)
            st.plotly_chart(fig)

    def selected_Volien(plot_selection,data,x_axis,y_axis):
        if plot_selection == "Volien":
            x_axis_val = st.selectbox(
            'Select X-axis Values',x_axis,0
            )
            y_axis_val = st.selectbox(
            'Select Yaxis Values',y_axis,2
            )
            fig = px.violin(data, x=data[x_axis_val], y=data[y_axis_val],)
            st.plotly_chart(fig)

    def selected_2dScatter(plot_selection,data,x_axis,y_axis):
        if plot_selection == "2 Variable Scatter":
            x_axis_val = st.selectbox(
            'Select X-axis Values',x_axis,0
            )
            y_axis_val = st.selectbox(
            'Select Yaxis Values',y_axis,2
            )
            fig = px.scatter(data, x=data[x_axis_val], y=data[y_axis_val], trendline="ols")
            st.plotly_chart(fig)

    def selected_3dScatter(plot_selection,data,x_axis,y_axis,hue):
        if plot_selection == "3 Variable Scatter":
            x_axis_val = st.selectbox(
            'Select X-axis Values',x_axis,0
            )
            y_axis_val = st.selectbox(
            'Select Yaxis Values',y_axis,2
            )
            hue = st.selectbox(
            'Select Yaxis Values',hue,2
            )
            fig = px.scatter(data, x=data[x_axis_val], y=data[y_axis_val],color=data[hue], symbol=data[hue])
            st.plotly_chart(fig)

    def selected_box(plot_selection,data,x_axis,y_axis):
        if plot_selection == "Box":
            x_axis_val = st.selectbox(
            'Select X-axis Values',x_axis,0
            )
            y_axis_val = st.selectbox(
            'Select Yaxis Values',y_axis,2
            )
            fig = px.box(data, x=data[x_axis_val], y=data[y_axis_val])
            st.plotly_chart(fig)


    def selected_2d_Hist():
        if plot_selection == "2d Histogram":
            st.write("hi")

    if data_file is not None:
        file_details = {"filename":data_file.name, "filetype":data_file.type,"filesize":data_file.size}
        # here write file detial
        
        # here we read data and make it as a data frame
        try:
            data = pd.read_csv(data_file)
        except:
            data = pd.read_excel(data_file,engine='openpyxl')

        option = des_fun.differentiate(data=data)
        # print(option[0].columns)
        plots_name = ["2 Variable Scatter","3 Variable Scatter","Bar","2d Bar","Donut","Pie","Distribution Plot","Histogram","Heat","Box","Volien","Error Bar","2d Histogram"]


        if data_file is not None:
            with st.container():
                first_col = st.columns([3,8,3])
                with first_col[1]:

                    st.markdown("# Intrective Charts 🎉")
                    st.sidebar.markdown("# Intrective Charts 🎉")

                    unique_con = des_fun.unique_count(data=option[1])
                    # plot selection
                    plot_selection = st.selectbox(
                    'Select Plot which you want to display',plots_name
                    )
                    bar = selected_bar(plot_selection,data = option[1],col_name=option[1].columns)
                    don = selected_donut(plot_selection,data = option[1],col_name=option[1].columns)
                    bar_2d = selected_2d_bar(plot_selection,data = data,x_axis=option[1].columns,y_axis=option[0].columns)
                    # value_coun = data.value_counts()
                    box = selected_box(plot_selection , data = data,x_axis=option[1].columns,y_axis=data.columns)
                    volien = selected_Volien(plot_selection , data = data,x_axis=option[1].columns,y_axis=option[0].columns)
                    hist = selected_Hist(plot_selection , data = data,x_axis=data.columns)
                    dist = selected_dist(plot_selection,data = data , col_name=option[0].columns)
                    sca_2d = selected_2dScatter(plot_selection,data = data,x_axis=option[0].columns,y_axis=option[0].columns)
                    sca_3d = selected_3dScatter(plot_selection,data = data,x_axis=option[0].columns,y_axis=option[0].columns,hue=unique_con)
                    pie = selected_pie(plot_selection,data = option[1],col_name=option[1].columns)
                    


page_names_to_funcs = {
    "Home": Home,
    "Correlation": Correlation,
    "Intrective Charts": Intrective_charts,
}

selected_page = st.sidebar.selectbox("Select a page", page_names_to_funcs.keys())
page_names_to_funcs[selected_page]()
