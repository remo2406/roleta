import streamlit as st
from streamlit_server_state import server_state, server_state_lock, no_rerun
import streamlit.components.v1 as components

def roleta(ultimoatendido=None):
    ramaisonline = []
    
    

    if ultimoatendido == None:
        ultimoatendido = 16

    n = 1
    for ramal in range(1,17):
        method_name = "statusramal" + str(n)
        if getattr(server_state, method_name):
            ramaisonline.append(ramal)
        n += 1


    #n = 1

    for f in range(1,17):
        if ultimoatendido+f in ramaisonline:
            return ultimoatendido+f
    for k in range(1,17):
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
        
    elif n == 10:
        server_state.statusramal5 = not server_state.statusramal5

    elif n == 6:
        server_state.statusramal6 = not server_state.statusramal6

    elif n == 7:
        server_state.statusramal7 = not server_state.statusramal7
        
    elif n == 8:
        server_state.statusramal8 = not server_state.statusramal8
        
    elif n == 9:
        server_state.statusramal9 = not server_state.statusramal9
        
    elif n == 10:
        server_state.statusramal10 = not server_state.statusramal10
    
    elif n == 11:
        server_state.statusramal11 = not server_state.statusramal11

    elif n == 12:
        server_state.statusramal12 = not server_state.statusramal12
        
    elif n == 13:
        server_state.statusramal13 = not server_state.statusramal13
        
    elif n == 14:
        server_state.statusramal14 = not server_state.statusramal14
        
    elif n == 110:
        server_state.statusramal15 = not server_state.statusramal15

    elif n == 16:
        server_state.statusramal16 = not server_state.statusramal16
    
def ChangeButtonColour(widget_label, font_color, background_color='transparent'):
    htmlstr = f"""
        <script>
            var elements = window.parent.document.querySelectorAll('button');
            for (var i = 0; i < elements.length; ++i) {{ 
                if (elements[i].innerText == '{widget_label}') {{ 
                    elements[i].style.color ='{font_color}';
                    elements[i].style.background = '{background_color}'
                }}
            }}
        </script>
        """
    components.html(f"{htmlstr}", height=0, width=0)


def main():
    ramais = ['Andreza', 'Antonio', 'Esther', 'Felipe C', 'Felipe T',
              'Gabriela', 'Júlia', 'Lorrayne', 'Marcelly', 'Maria Clara',
              'Maria Isabella', 'Matheus S', 'Merilu', 'Mykaela',
              'Samantha', 'Taíssa']

    numramais = len(ramais)
    

    #with no_rerun:
        #server_state["foo"] = 42

    #st.set_page_config(layout='wide')
    st.header('Roleta Atendimento')
    st.subheader('Ramais')

    col1, col2, col3, col4, col5 = st.columns(5)
    col6, col7, col8, col9, col10 = st.columns(5)
    col11, col12, col13, col14, col15, col16 = st.columns(6)
    

    with col1:
        numramal = 1
        st.write(ramais[numramal-1])

        if "statusramal1" not in server_state or not server_state.statusramal1:
            server_state.statusramal1 = False
            st.button('Offline',key='ramal1off',on_click=ramalonline,args=(1,))

        elif server_state.statusramal1:
            st.button('Online',key='ramal1on',on_click=ramalonline,args=(1,))
            ChangeButtonColour('Online','#35bf3e')
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
            ChangeButtonColour('Online','#35bf3e')
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
            ChangeButtonColour('Online','#35bf3e')
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
            ChangeButtonColour('Online','#35bf3e')
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
            ChangeButtonColour('Online','#35bf3e')
            try:
                if roleta(server_state.ultimoatendido) == numramal:
                    st.write('Sua vez de atender!')
                    st.button('Atendido', key='ramal5at', on_click=altultimoatendido,args=(numramal,))
                    
            except:
                if roleta() == numramal:
                    st.write('Sua vez de atender!')
                    st.button('Atendido', key='ramal5at', on_click=altultimoatendido,args=(numramal,))

    with col6:
        numramal = 6
        st.write(ramais[numramal-1])

        if "statusramal6" not in server_state or not server_state.statusramal6:
            server_state.statusramal6 = False
            st.button('Offline',key='ramal6off',on_click=ramalonline,args=(6,))

        elif server_state.statusramal6:
            st.button('Online',key='ramal6on',on_click=ramalonline,args=(6,))
            ChangeButtonColour('Online','#35bf3e')
            try:
                if roleta(server_state.ultimoatendido) == numramal:
                    st.write('Sua vez de atender!')
                    st.button('Atendido', key='ramal6at', on_click=altultimoatendido,args=(numramal,))
                    
            except:
                if roleta() == numramal:
                    st.write('Sua vez de atender!')
                    st.button('Atendido', key='ramal6at', on_click=altultimoatendido,args=(numramal,))

    with col7:
        numramal = 7
        st.write(ramais[numramal-1])

        if "statusramal7" not in server_state or not server_state.statusramal7:
            server_state.statusramal7 = False
            st.button('Offline',key='ramal7off',on_click=ramalonline,args=(7,))

        elif server_state.statusramal7:
            st.button('Online',key='ramal7on',on_click=ramalonline,args=(7,))
            ChangeButtonColour('Online','#35bf3e')
            try:
                if roleta(server_state.ultimoatendido) == numramal:
                    st.write('Sua vez de atender!')
                    st.button('Atendido', key='ramal7at', on_click=altultimoatendido,args=(numramal,))
                    
            except:
                if roleta() == numramal:
                    st.write('Sua vez de atender!')
                    st.button('Atendido', key='ramal7at', on_click=altultimoatendido,args=(numramal,))

    with col8:
        numramal = 8
        st.write(ramais[numramal-1])

        if "statusramal8" not in server_state or not server_state.statusramal8:
            server_state.statusramal8 = False
            st.button('Offline',key='ramal8off',on_click=ramalonline,args=(8,))

        elif server_state.statusramal8:
            st.button('Online',key='ramal8on',on_click=ramalonline,args=(8,))
            ChangeButtonColour('Online','#35bf3e')
            try:
                if roleta(server_state.ultimoatendido) == numramal:
                    st.write('Sua vez de atender!')
                    st.button('Atendido', key='ramal8at', on_click=altultimoatendido,args=(numramal,))
                    
            except:
                if roleta() == numramal:
                    st.write('Sua vez de atender!')
                    st.button('Atendido', key='ramal8at', on_click=altultimoatendido,args=(numramal,))

    with col9:
        numramal = 9
        st.write(ramais[numramal-1])

        if "statusramal9" not in server_state or not server_state.statusramal9:
            server_state.statusramal9 = False
            st.button('Offline',key='ramal9off',on_click=ramalonline,args=(9,))

        elif server_state.statusramal9:
            st.button('Online',key='ramal9on',on_click=ramalonline,args=(9,))
            ChangeButtonColour('Online','#35bf3e')
            try:
                if roleta(server_state.ultimoatendido) == numramal:
                    st.write('Sua vez de atender!')
                    st.button('Atendido', key='ramal9at', on_click=altultimoatendido,args=(numramal,))
                    
            except:
                if roleta() == numramal:
                    st.write('Sua vez de atender!')
                    st.button('Atendido', key='ramal9at', on_click=altultimoatendido,args=(numramal,))

    with col10:
        numramal = 10
        st.write(ramais[numramal-1])

        if "statusramal10" not in server_state or not server_state.statusramal10:
            server_state.statusramal10 = False
            st.button('Offline',key='ramal10off',on_click=ramalonline,args=(10,))

        elif server_state.statusramal10:
            st.button('Online',key='ramal10on',on_click=ramalonline,args=(10,))
            ChangeButtonColour('Online','#35bf3e')
            try:
                if roleta(server_state.ultimoatendido) == numramal:
                    st.write('Sua vez de atender!')
                    st.button('Atendido', key='ramal10at', on_click=altultimoatendido,args=(numramal,))
                    
            except:
                if roleta() == numramal:
                    st.write('Sua vez de atender!')
                    st.button('Atendido', key='ramal10at', on_click=altultimoatendido,args=(numramal,))

    with col11:
        numramal = 11
        st.write(ramais[numramal-1])

        if "statusramal11" not in server_state or not server_state.statusramal11:
            server_state.statusramal11 = False
            st.button('Offline',key='ramal11off',on_click=ramalonline,args=(11,))

        elif server_state.statusramal11:
            st.button('Online',key='ramal11on',on_click=ramalonline,args=(11,))
            ChangeButtonColour('Online','#35bf3e')
            try:
                if roleta(server_state.ultimoatendido) == numramal:
                    st.write('Sua vez de atender!')
                    st.button('Atendido', key='ramal11at', on_click=altultimoatendido,args=(numramal,))
                    
            except:
                if roleta() == numramal:
                    st.write('Sua vez de atender!')
                    st.button('Atendido', key='ramal11at', on_click=altultimoatendido,args=(numramal,))

    with col12:
        numramal = 12
        st.write(ramais[numramal-1])

        if "statusramal12" not in server_state or not server_state.statusramal12:
            server_state.statusramal12 = False
            st.button('Offline',key='ramal12off',on_click=ramalonline,args=(12,))

        elif server_state.statusramal12:
            st.button('Online',key='ramal12on',on_click=ramalonline,args=(12,))
            ChangeButtonColour('Online','#35bf3e')
            try:
                if roleta(server_state.ultimoatendido) == numramal:
                    st.write('Sua vez de atender!')
                    st.button('Atendido', key='ramal12at', on_click=altultimoatendido,args=(numramal,))
                    
            except:
                if roleta() == numramal:
                    st.write('Sua vez de atender!')
                    st.button('Atendido', key='ramal12at', on_click=altultimoatendido,args=(numramal,))

    with col13:
        numramal = 13
        st.write(ramais[numramal-1])

        if "statusramal13" not in server_state or not server_state.statusramal13:
            server_state.statusramal13 = False
            st.button('Offline',key='ramal13off',on_click=ramalonline,args=(13,))

        elif server_state.statusramal13:
            st.button('Online',key='ramal13on',on_click=ramalonline,args=(13,))
            ChangeButtonColour('Online','#35bf3e')
            try:
                if roleta(server_state.ultimoatendido) == numramal:
                    st.write('Sua vez de atender!')
                    st.button('Atendido', key='ramal13at', on_click=altultimoatendido,args=(numramal,))
                    
            except:
                if roleta() == numramal:
                    st.write('Sua vez de atender!')
                    st.button('Atendido', key='ramal13at', on_click=altultimoatendido,args=(numramal,))

    with col14:
        numramal = 14
        st.write(ramais[numramal-1])

        if "statusramal14" not in server_state or not server_state.statusramal14:
            server_state.statusramal14 = False
            st.button('Offline',key='ramal14off',on_click=ramalonline,args=(14,))

        elif server_state.statusramal14:
            st.button('Online',key='ramal14on',on_click=ramalonline,args=(14,))
            ChangeButtonColour('Online','#35bf3e')
            try:
                if roleta(server_state.ultimoatendido) == numramal:
                    st.write('Sua vez de atender!')
                    st.button('Atendido', key='ramal14at', on_click=altultimoatendido,args=(numramal,))
                    
            except:
                if roleta() == numramal:
                    st.write('Sua vez de atender!')
                    st.button('Atendido', key='ramal14at', on_click=altultimoatendido,args=(numramal,))

    with col15:
        numramal = 15
        st.write(ramais[numramal-1])

        if "statusramal15" not in server_state or not server_state.statusramal15:
            server_state.statusramal15 = False
            st.button('Offline',key='ramal15off',on_click=ramalonline,args=(15,))

        elif server_state.statusramal15:
            st.button('Online',key='ramal15on',on_click=ramalonline,args=(15,))
            ChangeButtonColour('Online','#35bf3e')
            try:
                if roleta(server_state.ultimoatendido) == numramal:
                    st.write('Sua vez de atender!')
                    st.button('Atendido', key='ramal15at', on_click=altultimoatendido,args=(numramal,))
                    
            except:
                if roleta() == numramal:
                    st.write('Sua vez de atender!')
                    st.button('Atendido', key='ramal15at', on_click=altultimoatendido,args=(numramal,))

    with col16:
        numramal = 16
        st.write(ramais[numramal-1])

        if "statusramal16" not in server_state or not server_state.statusramal16:
            server_state.statusramal16 = False
            st.button('Offline',key='ramal16off',on_click=ramalonline,args=(16,))

        elif server_state.statusramal16:
            st.button('Online',key='ramal16on',on_click=ramalonline,args=(16,))
            ChangeButtonColour('Online','#35bf3e')
            try:
                if roleta(server_state.ultimoatendido) == numramal:
                    st.write('Sua vez de atender!')
                    st.button('Atendido', key='ramal16at', on_click=altultimoatendido,args=(numramal,))
                    
            except:
                if roleta() == numramal:
                    st.write('Sua vez de atender!')
                    st.button('Atendido', key='ramal16at', on_click=altultimoatendido,args=(numramal,))

#room_name = streamlit_sync.select_room_widget()

#with streamlit_sync.sync(room_name):

if __name__ == '__main__':
    main()




    



