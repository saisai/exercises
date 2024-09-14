import io

import pandas as pd

imageannotation = pd.read_csv(
        io.StringIO(
            """
            Detection,Imagename,Frame_Identifier,TL_x,TL_y,BR_x,BR_y,detection_Confidence,Target_Length,Species,Confidence
0,201503.20150619.181140817.204628.jpg,0,272,142.375,382.5,340,0.475837,0,fish,0.475837
1,201503.20150619.181141498.204632.jpg,3,267.75,6.375,422.875,80.75,0.189145,0,fish,0.189145
2,201503.20150619.181141662.204633.jpg,4,820.25,78.625,973.25,382.5,0.615788,0,fish,0.615788
3,201503.20150619.181141662.204633.jpg,4,1257,75,1280,116,0.307278,0,fish,0.307278
4,201503.20150619.181141834.204634.jpg,5,194,281,233,336,0.586944,0,fish,0.586944
            """
            )
        )

#print(imageannotation)
# (Pretend this comes from a separate file)
imagemetadata = pd.DataFrame({"Imagename": imageannotation.Imagename.unique()})

#print(imagemetadata)
def make_annotation(r):
    return {
            "bbox" : [r.TL_x, r.TL_y, r.BR_x, r.BR_y],
            "species": r.Species,
            }

annotations_by_image = (
        imageannotation.groupby("Imagename")
        .apply(lambda r: r.apply(make_annotation, axis=1).to_list())
        .to_dict()
        )

#print(annotations_by_image)

imagemetadata = pd.DataFrame({"Imagename":imageannotation.Imagename.unique()})
imagemetadata["annotation"] = imagemetadata.Imagename.map(annotations_by_image)

print(imagemetadata)

# https://stackoverflow.com/questions/73815067/execute-iterative-queries-over-a-pandas-dataframe

