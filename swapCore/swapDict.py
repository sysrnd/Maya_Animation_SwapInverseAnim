import json
sample = {'arms':{'DRIVER_CLAVICULA_IZQ':(1, 1, 1), 'DRIVER_HOMBRO_IZQ_FK':(1, 1, 1), 'DRIVER_CODO_IZQ':(1, 1, 1), 'DRIVER_CODO_IZQ_FK':(1, 1, 1), 
				'DRIVER_MANO_IZQ':(1, 1, 1), 'DRIVER_MANO_IZQ_FK':(1, 1, 1), 'DRIVER_CANCEL_IZQ_1':(1, 1, 1), 'DRIVER_INDEX_IZQ_1':(1, 1, 1), 
				'DRIVER_MIDDLE_IZQ_1':(1, 1, 1), 'DRIVER_PINKY_SEC_IZQ':(1, 1, 1), 'DRIVER_PINKY_IZQ_1':(1, 1, 1), 'DRIVER_THUMB_IZQ_1':(1, 1, 1)}}
with open('result.json', 'w') as fp:
    json.dump(sample, fp, indent=4)