import streamlit as st
import streamlit_sync
from streamlit_server_state import server_state, server_state_lock, no_rerun

def roleta(ultimoatendido=None):
    ramaisonline = []
    
    

    if ultimoatendido == None:
        ultimoatendido = 5

    n = 1
    for ramal in range(1,6):
        method_name = "statusramal" + str(n)
        if getattr(server_state, method_name):
            ramaisonline.append(ramal)
        n += 1


    #n = 1

    for f in range(1,6):
        if ultimoatendido+f in ramaisonline:
            return ultimoatendido+f
    for k in range(1,6):
        if k in ramaisonline:
            return k
        #n += 1

    
    
        
            

def altultimoatendido(ramal):    
    server_state.ultimoatendido = ramal

def ramalonline(n):
    if n == 1:
        server_state.statusramal1 = not server_state.statusramal1

    elif n == 2:
        server_state.statusramal2 = not server_state.statusramal2
        
    elif n == 3:
        server_state.statusramal3 = not server_state.statusramal3
        
    elif n == 4:
        server_state.statusramal4 = not server_state.statusramal4
        
    elif n == 5:
        server_state.statusramal5 = not server_state.statusramal5
    

def main():
    ramais = ['1072', '1032', '1031', '1035', '1033']

    numramais = len(ramais)
    

    #with no_rerun:
        #server_state["foo"] = 42

    #st.set_page_config(layout='wide')
    st.header('Roleta Atendimento')
    st.subheader('Ramais')

    col1, col2, col3, col4, col5 = st.columns(numramais)


    with col1:
        numramal = 1
        st.write(ramais[numramal-1])

        if "statusramal1" not in server_state or not server_state.statusramal1:
            server_state.statusramal1 = False
            st.button('Offline',key='ramal1off',on_click=ramalonline,args=(1,))

        elif server_state.statusramal1:
            st.button('Online',key='ramal1on',on_click=ramalonline,args=(1,))
            try:
                if roleta(server_state.ultimoatendido) == numramal:
                    st.write('Sua vez de atender!')
                    st.button('Atendido',key='ramal1at',on_click=altultimoatendido,args=(numramal,))
                    
            except:
                if roleta() == numramal:
                    st.write('Sua vez de atender!')
                    st.button('Atendido',key='ramal1at',on_click=altultimoatendido,args=(numramal,))

        
    with col2:
        numramal = 2
        st.write(ramais[numramal-1])

        if "statusramal2" not in server_state or not server_state.statusramal2:
            server_state.statusramal2 = False
            st.button('Offline',key='ramal2off', on_click=ramalonline,args=(2,))

        elif server_state.statusramal2:
            st.button('Online',key='ramal2on',on_click=ramalonline,args=(2,))
            try:
                if roleta(server_state.ultimoatendido) == numramal:
                    st.write('Sua vez de atender!')
                    st.button('Atendido', key='ramal2at', on_click=altultimoatendido,args=(numramal,))
                    
            except:
                if roleta() == numramal:
                    st.write('Sua vez de atender!')
                    st.button('Atendido', key='ramal2at', on_click=altultimoatendido,args=(numramal,))

    with col3:
        numramal = 3
        st.write(ramais[numramal-1])

        if "statusramal3" not in server_state or not server_state.statusramal3:
            server_state.statusramal3 = False
            st.button('Offline',key='ramal3off',on_click=ramalonline,args=(3,))

        elif server_state.statusramal3:
            st.button('Online',key='ramal3on',on_click=ramalonline,args=(3,))
            try:
                if roleta(server_state.ultimoatendido) == numramal:
                    st.write('Sua vez de atender!')
                    st.button('Atendido', key='ramal3at', on_click=altultimoatendido,args=(numramal,))
                    
            except:
                if roleta() == numramal:
                    st.write('Sua vez de atender!')
                    st.button('Atendido', key='ramal3at', on_click=altultimoatendido,args=(numramal,))

    with col4:
        numramal = 4
        st.write(ramais[numramal-1])

        if "statusramal4" not in server_state or not server_state.statusramal4:
            server_state.statusramal4 = False
            st.button('Offline',key='ramal4off',on_click=ramalonline,args=(4,))

        elif server_state.statusramal4:
            st.button('Online',key='ramal4on',on_click=ramalonline,args=(4,))
            try:
                if roleta(server_state.ultimoatendido) == numramal:
                    st.write('Sua vez de atender!')
                    st.button('Atendido', key='ramal4at', on_click=altultimoatendido,args=(numramal,))
                    
            except:
                if roleta() == numramal:
                    st.write('Sua vez de atender!')
                    st.button('Atendido', key='ramal4at', on_click=altultimoatendido,args=(numramal,))

    with col5:
        numramal = 5
        st.write(ramais[numramal-1])

        if "statusramal5" not in server_state or not server_state.statusramal5:
            server_state.statusramal5 = False
            st.button('Offline',key='ramal5off',on_click=ramalonline,args=(5,))

        elif server_state.statusramal5:
            st.button('Online',key='ramal5on',on_click=ramalonline,args=(5,))
            try:
                if roleta(server_state.ultimoatendido) == numramal:
                    st.write('Sua vez de atender!')
                    st.button('Atendido', key='ramal5at', on_click=altultimoatendido,args=(numramal,))
                    
            except:
                if roleta() == numramal:
                    st.write('Sua vez de atender!')
                    st.button('Atendido', key='ramal5at', on_click=altultimoatendido,args=(numramal,))



#room_name = streamlit_sync.select_room_widget()

#with streamlit_sync.sync(room_name):
main()




    



