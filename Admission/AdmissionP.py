import folium
import googlemaps
import pandas as pd

adm = pd.read_csv('foreign.csv', header=0, usecols=['국가', '일반여권소지자-입국가능여부', '일반여권소지자-입국가능기간'], encoding='utf_8')

maps = googlemaps.Client('AIzaSyCZN-ASzsjW15DPF9rKt2Mgd-EetRk6pwI')

lat = [] #위도
lng = [] #경도

places = adm.iloc[:,0]
places = places.to_string(index=False)

list = places.split()

for place in list:
    geo_location = maps.geocode(place)[0].get('geometry')
    lat.append(geo_location['location']['lat'])
    lng.append(geo_location['location']['lng'])

df = pd.DataFrame({'위도': lat, '경도': lng, '국가': list})

df1 = df[['위도', '경도']].values
df1 = df1.tolist()
df2 = df['국가'].values

# 입국 가능 국가
maps = folium.Map(location=[37.541, 126.986], zoom_start=2, tiles='Stamen Terrain')

for i in df.index:
    folium.Marker(
        location = df1[i],
        tooltip = df2[i],
    ).add_to(maps)

maps

# 일반 여권 소지 시 입국 가능 국가 + 기간 표시 (마우스 커서)
maps2 = folium.Map(location=[37.541, 126.986], zoom_start=2, tiles='Stamen Terrain')

Normal = []
for i in adm.index:
    if adm['일반여권소지자-입국가능여부'][i] == 'Y':
        Normal.append(i)

for i in Normal:
    folium.Marker(
        location = df1[i],
        tooltip = df2[i],
        popup = adm['일반여권소지자-입국가능기간'][i]
    ).add_to(maps2)

maps2

maps.save('Maps.html')
maps2.save('Maps2.html')
