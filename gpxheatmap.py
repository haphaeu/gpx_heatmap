import gpxpy
import folium
import numpy
import glob
import os

root = '/home/raf/Documents/Archive/gpx/strava'

print('Working on', root)

gpx_files = glob.glob(os.path.join(root, '**/*.gpx'), recursive=True)

print('Processing {} gpx files.'.format(len(gpx_files)))

tracks = []
for i, gpx_file in enumerate(gpx_files):
    
    print(i + 1, gpx_file, '      ', end='\r')
    
    with open(gpx_file, 'r') as fin:
        
        try:
            gpx = gpxpy.parse(fin)                
        except gpxpy.gpx.GPXException:
            print('\n  ValueError. Skipping. Comma separated values??')
            continue
            
        for track in gpx.tracks:
            
            points = []
            
            for segment in track.segments:        
                for point in segment.points:
                    points.append([point.latitude, point.longitude])
            
            tracks.append(points)

# find a mean point to centralise map
means = []
for track in tracks:
    means.append(numpy.array(track).mean(axis=0))
mean = numpy.array(means).mean(axis=0)
heatmap = folium.Map(location=mean, zoom_start=15)

for points in tracks:
    folium.vector_layers.PolyLine(points).add_to(heatmap)
    
# Save map
heatmap.save("./heatmap.html")
