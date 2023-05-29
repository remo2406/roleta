import streamlit as st


def roleta(ultimoatendido=None):
    ramaisonline = []
    
    

    if ultimoatendido == None:
        ultimoatendido = 5

    n = 1
    for ramal in range(1,6):
        method_name = "statusramal" + str(n)
        if getattr(st.session_state, method_name):
            ramaisonline.append(ramal)
        n += 1
    print(ramaisonline)


    #n = 1

    for f in range(1,6):
        if ultimoatendido+f in ramaisonline:
            return ultimoatendido+f
    for k in range(1,6):
        if k in ramaisonline:
            return k
        #n += 1

    
    
        
            

def altultimoatendido(ramal):    
    st.session_state.ultimoatendido = ramal

def ramalonline(n):
    if n == 1:
        st.session_state.statusramal1 = not st.session_state.statusramal1

    elif n == 2:
        st.session_state.statusramal2 = not st.session_state.statusramal2
        
    elif n == 3:
        st.session_state.statusramal3 = not st.session_state.statusramal3
        
    elif n == 4:
        st.session_state.statusramal4 = not st.session_state.statusramal4
        
    elif n == 5:
        st.session_state.statusramal5 = not st.session_state.statusramal5
    

if __name__ == "__main__":
    ramais = ['1072', '1032', '1031', '1035', '1033']

    numramais = len(ramais)

    st.set_page_config(layout='wide')
    st.header('Roleta Atendimento')
    st.subheader('Ramais')

    col1, col2, col3, col4, col5 = st.columns(numramais)


    with col1:
        numramal = 1
        st.write(ramais[numramal-1])

        if "statusramal1" not in st.session_state or not st.session_state.statusramal1:
            st.session_state.statusramal1 = False
            st.button('Offline',key='ramal1',on_click=ramalonline,args=(1,))

        elif st.session_state.statusramal1:
            st.button('Online',key='ramal1',on_click=ramalonline,args=(1,))
            try:
                if roleta(st.session_state.ultimoatendido) == numramal:
                    st.write('Sua vez de atender!')
                    st.button('Atendido',key='ramal1at',on_click=altultimoatendido,args=(numramal,))
                else:
                    print('Sem ramais retornados')
                    
            except:
                if roleta() == numramal:
                    st.write('Sua vez de atender!')
                    st.button('Atendido',key='ramal1at',on_click=altultimoatendido,args=(numramal,))
                else:
                    print('Sem ramais retornados EXCPT')

        
    with col2:
        numramal = 2
        st.write(ramais[numramal-1])

        if "statusramal2" not in st.session_state or not st.session_state.statusramal2:
            st.session_state.statusramal2 = False
            st.button('Offline',key='ramal2', on_click=ramalonline,args=(2,))

        elif st.session_state.statusramal2:
            st.button('Online',key='ramal2',on_click=ramalonline,args=(2,))
            try:
                if roleta(st.session_state.ultimoatendido) == numramal:
                    st.write('Sua vez de atender!')
                    st.button('Atendido', key='ramal2at', on_click=altultimoatendido,args=(numramal,))
                    
            except:
                if roleta() == numramal:
                    st.write('Sua vez de atender!')
                    st.button('Atendido', key='ramal2at', on_click=altultimoatendido,args=(numramal,))

    with col3:
        numramal = 3
        st.write(ramais[numramal-1])

        if "statusramal3" not in st.session_state or not st.session_state.statusramal3:
            st.session_state.statusramal3 = False
            st.button('Offline',key='ramal3',on_click=ramalonline,args=(3,))

        elif st.session_state.statusramal3:
            st.button('Online',key='ramal3',on_click=ramalonline,args=(3,))
            try:
                if roleta(st.session_state.ultimoatendido) == numramal:
                    st.write('Sua vez de atender!')
                    st.button('Atendido', key='ramal3at', on_click=altultimoatendido,args=(numramal,))
                    
            except:
                if roleta() == numramal:
                    st.write('Sua vez de atender!')
                    st.button('Atendido', key='ramal3at', on_click=altultimoatendido,args=(numramal,))

    with col4:
        numramal = 4
        st.write(ramais[numramal-1])

        if "statusramal4" not in st.session_state or not st.session_state.statusramal4:
            st.session_state.statusramal4 = False
            st.button('Offline',key='ramal4',on_click=ramalonline,args=(4,))

        elif st.session_state.statusramal4:
            st.button('Online',key='ramal4',on_click=ramalonline,args=(4,))
            try:
                if roleta(st.session_state.ultimoatendido) == numramal:
                    st.write('Sua vez de atender!')
                    st.button('Atendido', key='ramal4at', on_click=altultimoatendido,args=(numramal,))
                    
            except:
                if roleta() == numramal:
                    st.write('Sua vez de atender!')
                    st.button('Atendido', key='ramal4at', on_click=altultimoatendido,args=(numramal,))

    with col5:
        numramal = 5
        st.write(ramais[numramal-1])

        if "statusramal5" not in st.session_state or not st.session_state.statusramal5:
            st.session_state.statusramal5 = False
            st.button('Offline',key='ramal5',on_click=ramalonline,args=(5,))

        elif st.session_state.statusramal5:
            st.button('Online',key='ramal5',on_click=ramalonline,args=(5,))
            try:
                if roleta(st.session_state.ultimoatendido) == numramal:
                    st.write('Sua vez de atender!')
                    st.button('Atendido', key='ramal5at', on_click=altultimoatendido,args=(numramal,))
                    
            except:
                if roleta() == numramal:
                    st.write('Sua vez de atender!')
                    st.button('Atendido', key='ramal5at', on_click=altultimoatendido,args=(numramal,))






    



