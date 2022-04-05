import streamlit as st
import pandas as pd
from PIL import Image

# Importacion de Archivos
image = Image.open('Description.jpg')


st.title('Energy in Place')
# Variables de ingreso

st.info('Cálculo de calor almacenado y potencial de generación geoeléctrica usando método volumétrico y valores de parámetros ajustados')

st.warning('''Ecuaciones de energía: 

	Energía en roca y fluido:	Qt = Qr + Qf
	Energía en roca:		Qr = A * h * (rhor * Cr * (1 -phi) *(Ti - Ta))
	Energía en fluidos:		Qf = A * h * (rhof * Cf * phi * (Ti - Ta))
	Potencia de la planta:		P = (Qt * Rf * Ce) / (Pf * t)

	''')

with st.expander('Variables description'):
	st.image(image)
with st.expander('Parámetros del Campo Geotérmico:'):

	columna_1 , columna_2 , columna_3 = st.columns(3)

	with columna_1:
		A = st.number_input('Area [Km2]',5.00,12.00,6.25)
		h = st.number_input('Espesor del reservrio [m]',min_value=0, max_value=2000, value=60 )
		Cr = st.number_input('Calor específico de la roca [kJ/kg °C]',min_value=0.0, max_value=10.0, value=0.9 )
	with columna_2:
		Cf = st.number_input('Calor específico del fluido [kJ/kg °C]',min_value=0.0, max_value=10.0, value=4.2 )
		
		phi = st.number_input('Porosidad de la roca [-]',min_value=0.07, max_value=0.15, value=0.1 )
		Ti = st.number_input('Temperatura media del reservorio [°C]',min_value=140.00, max_value=290.00, value=160.00 )	
	with columna_3:
		Ta = st.number_input('Temperatura de abandono del reservorio [°C]',min_value=0.00, max_value=290.00, value=50.00 )
		rhor = st.number_input('Densidad de la roca  [kg/m3]',min_value=140.00, max_value=4000.00, value=2700.00 )
		rhof = st.number_input('Densidad del fluido [kg/m3]',min_value=0.00, max_value=4000.00, value=997.00 )
	Qr = A*1000000*h*(rhor*Cr*(1-phi)*(Ti-Ta))
	Qf= A*1000000*h*(rhof*Cf*phi*(Ti-Ta))
	Qt= Qr+Qf
	st.write('Calor almacenado en la roca:',  format(Qr,'.4E'))
	st.write('Calor almacennado en el fluido:',  format(Qf,'.4E'))
	st.write('Calor total:', format(Qt,'.4E'))

with st.expander('Parámetros de la Planta Geotérmica:'):
	columna_4 , columna_5 , columna_6 = st.columns(3)
	with columna_4:
		Rf = st.number_input('Factor de recuperación de calor [-]',min_value=0.10, max_value=0.25, value=0.15 )
		Ce = st.number_input('Eficiencia de conversión [-]',min_value=0.00, max_value=2.00, value=0.10 )
	with columna_5:
		Pf = st.number_input('Factor de Planta [-]',min_value=0.00, max_value=2.00, value=0.90 )
	with columna_6:	
		t = st.number_input('Tiempo [years]',min_value=0.00, max_value=100.00, value=30.00 )


	P = Qt*Rf*Ce/(1000*Pf*t*31557600)

	st.success('Potencial de energía: {} Mwe'.format(round(P,4)))
