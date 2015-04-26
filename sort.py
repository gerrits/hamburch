from xml.dom import minidom
import sys
import os.path
import shutil

map_dir = './karten'
sorted_map_dir = './sorted'

omit_ctr = 0

if not os.path.exists(sorted_map_dir):
        os.makedirs(sorted_map_dir)

for item_id in os.listdir (map_dir):
    current = minidom.parse(map_dir + '/' + item_id + '/' + item_id + '.xml')
    itemlist = current.getElementsByTagName('mods:dateIssued')
    current_date = itemlist[0].firstChild.nodeValue.split(' ', 1)[0]
    
    tiff_path = map_dir + '/' + item_id + '/00000001.tif'

    if not os.path.exists(tiff_path):
        omit_ctr = omit_ctr + 1
        continue
    
    shutil.copy2(tiff_path, 
            sorted_map_dir + '/' + current_date + '_' + item_id + '.tif')
    shutil.copy2(map_dir + '/' + item_id + '/' + item_id + '.xml',
            sorted_map_dir + '/' + current_date + '_' + item_id + '.xml')

print str(omit_ctr) + ' files have been omitted'
