import folium
m = folium.Map(location=[49.8413276, 24.0294036], zoom_start=12, 
    tiles='Stamen Terrain')
​
tooltip = 'Натисни мене!'
​
folium.Marker([49.7916519, 24.046862], popup='<i>Сихів</i>', tooltip=tooltip).add_to(m)
folium.Marker([49.8174143, 24.0216516], popup='<b>УКУ</b>', tooltip=tooltip).add_to(m)
​
m.save('index.html')
