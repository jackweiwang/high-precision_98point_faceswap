from umeyama import umeyama
import numpy as np
import cv2

# def get_src_landmarks(x0, x1, y0, y1, pnts):
#     """
#     x0, x1, y0, y1: (smoothed) bbox coord.
#     pnts: landmarks predicted by MTCNN
#     """
#     src_landmarks = [(int(pnts[i+5][0]-x0), int(pnts[i][0]-y0)) for i in range(5)]
#     #src_landmarks = [(int(pnts[i][0]-0), int(pnts[i+5][0]-0)) for i in range(5)]
#     return src_landmarks
#
# def get_tar_landmarks(img):
#     """
#     img: detected face image
#     """
#     # avg_landmarks = [
#     #     (0.31339227236234224, 0.3259269274198092),
#     #     (0.31075140146108776, 0.7228453709528997),
#     #     (0.5523683107816256, 0.5187296867370605),
#     #     (0.7752419985257663, 0.37262483743520886),
#     #     (0.7759613623985877, 0.6772957581740159)
#     #     ]
#
#
#     img_sz = img.shape
#     tar_landmarks = [(int(xy[0]*img_sz[0]), int(xy[1]*img_sz[1])) for xy in avg_landmarks]
#     return tar_landmarks

avg_landmarks3 =[[2.231152057647705, 34.41873550415039],[4.069259166717529, 51.634613037109375],[5.973801612854004, 68.76493072509766],
               [8.650944709777832, 85.9071273803711],[12.354299545288086, 102.87167358398438],[16.41330909729004, 119.65381622314453],
               [21.219316482543945, 136.26913452148438],[26.588111877441406, 152.562255859375],[33.47843551635742, 168.2899169921875],
               [41.6966438293457, 183.52159118652344],[51.06208419799805, 197.93006896972656],[61.62120819091797, 211.8604736328125],
               [72.54691314697266, 225.03021240234375],[84.306396484375, 237.5502166748047],[98.4856185913086, 247.72496032714844],
               [115.1573715209961, 254.1597442626953],[133.12705993652344, 255.86434936523438],[151.7762908935547, 253.02908325195312],
               [169.0986785888672, 245.30557250976562],[183.22378540039062, 233.91090393066406],[195.38485717773438, 220.2649383544922],
               [206.4640350341797, 206.01547241210938],[216.64556884765625, 191.05918884277344],[225.85731506347656, 175.7383270263672],
               [233.71617126464844, 159.5589141845703],[239.71682739257812, 142.65208435058594],[244.97836303710938, 125.85252380371094],
               [248.58547973632812, 108.3560562133789],[251.6096954345703, 90.58224487304688],[254.01036071777344, 72.88953399658203],
               [255.47462463378906, 55.00135040283203],[256.32769775390625, 37.357601165771484],[256.60223388671875, 19.695512771606445],
               [18.707874298095703, 48.31103515625],[38.70460891723633, 38.22604751586914],[59.69255065917969, 40.76329803466797],
               [80.28235626220703, 44.89830780029297],[100.66791534423828, 49.2402458190918],[101.1113052368164, 59.1024284362793],
               [81.05964660644531, 55.391231536865234],[59.734405517578125, 51.9345703125],[39.33951950073242, 48.879615783691406],
               [144.1809539794922, 46.624595642089844],[165.27867126464844, 40.041534423828125],[186.2083740234375, 33.330665588378906],
               [207.9178009033203, 28.69923210144043],[230.1829071044922, 36.4273796081543],[208.34933471679688, 39.37202072143555],
               [186.8564453125, 44.49140167236328],[165.96878051757812, 50.403202056884766],[144.62200927734375, 56.654354095458984],
               [123.37499237060547, 66.47109985351562],[123.88285064697266, 93.17877960205078],[124.06964111328125, 120.07686614990234],
               [124.56498718261719, 146.08929443359375],[97.1149673461914, 149.6868896484375],[111.53549194335938, 154.89706420898438],
               [127.18264770507812, 157.6581573486328],[143.18161010742188, 152.12574768066406],[158.49319458007812, 146.1137237548828],
               [38.59602737426758, 66.80008697509766],[49.94251251220703, 61.7973518371582],[62.957298278808594, 59.71554183959961],
               [79.94914245605469, 61.899227142333984],[94.0942153930664, 69.87968444824219],[79.12356567382812, 74.54476928710938],
               [63.7374267578125, 75.90013885498047],[50.23701095581055, 73.51408386230469],[156.98130798339844, 66.11508178710938],
               [169.15811157226562, 56.91811752319336],[185.7135467529297, 53.09669876098633],[199.13394165039062, 53.62391662597656],
               [212.2001953125, 57.67414093017578],[201.26658630371094, 65.71823120117188],[187.4761962890625, 69.94796752929688],
               [171.5403594970703, 69.71684265136719],[83.10617065429688, 184.1379852294922],[100.61316680908203, 179.430908203125],
               [119.13333129882812, 177.73143005371094],[129.34608459472656, 178.00515747070312],[139.5096893310547, 176.59141540527344],
               [162.97740173339844, 176.18759155273438],[185.93077087402344, 179.40985107421875],[172.9701690673828, 197.31060791015625],
               [155.76478576660156, 211.23214721679688],[132.8408203125, 216.46746826171875],[111.82939910888672, 213.10537719726562],
               [95.24971771240234, 200.3719940185547],[87.94941711425781, 185.44276428222656],[107.90859985351562, 186.0852508544922],
               [129.9530029296875, 186.94439697265625],[155.69606018066406, 183.5067138671875],[181.04612731933594, 181.10655212402344],
               [158.62767028808594, 193.32579040527344],[132.42271423339844, 199.27572631835938],[108.17445373535156, 195.39035034179688],
               [65.59075927734375, 67.73165893554688],[187.22152709960938, 61.1639518737793]]

avg_landmarks = [[30.514678955078125, 80.42579650878906],[31.217687606811523, 92.4482650756836],[31.442062377929688, 104.16796875],\
                [32.763084411621094, 116.19281768798828],[34.277809143066406, 127.90162658691406],[36.170284271240234, 139.85903930664062],\
                [38.84906005859375, 151.4765167236328],[41.90029525756836, 163.27435302734375],[46.36408996582031, 174.3899383544922],\
                [51.6311149597168, 185.21315002441406],[58.39703369140625, 195.8621826171875],[66.42613983154297, 204.91085815429688],\
                [75.87232971191406, 213.45089721679688],[86.37432861328125, 221.11570739746094],[97.99247741699219, 226.79443359375],\
                [110.9212417602539, 230.49607849121094],[124.2232894897461, 231.82322692871094],[137.3136444091797, 230.99095153808594],\
                [150.83633422851562, 227.31695556640625],[162.92970275878906, 222.29443359375],[173.8717041015625, 214.98329162597656],\
                [183.83078002929688, 207.01242065429688],[192.3173828125, 197.81309509277344],[199.57264709472656, 187.6143341064453],\
                [205.06578063964844, 177.02626037597656],[209.71910095214844, 165.57215881347656],[212.8565673828125, 153.74008178710938],\
                [215.66139221191406, 141.88597106933594],[217.73683166503906, 129.83251953125],[219.44290161132812, 117.59146881103516],\
                [220.87571716308594, 105.73112487792969],[221.9461212158203, 93.79301452636719],[222.69285583496094, 81.34735870361328],\
                [49.42043685913086, 69.49371337890625],[63.58843994140625, 58.98268508911133],[78.71405792236328, 58.27955627441406],\
                [93.10121154785156, 59.88604736328125],[107.13118743896484, 62.36017608642578],[107.13109588623047, 70.62034606933594],\
                [93.22974395751953, 68.47266387939453],[78.40569305419922, 66.76439666748047],[63.556419372558594, 66.6986083984375],\
                [143.6426239013672, 61.233428955078125],[158.56903076171875, 58.194271087646484],[174.3266143798828, 55.92277145385742],\
                [190.1252899169922, 56.62942123413086],[205.03346252441406, 67.48430633544922],[189.81863403320312, 64.61949157714844],\
                [174.18214416503906, 64.75936126708984],[158.7919921875, 66.61560821533203],[143.40182495117188, 69.6292953491211],\
                [124.23175811767578, 82.41342163085938],[123.82228088378906, 98.46682739257812],[122.9432373046875, 114.36054229736328],\
                [122.84186553955078, 129.505126953125],[103.68395233154297, 141.50428771972656],[113.58039855957031, 142.3894805908203],\
                [123.33271789550781, 142.99758911132812],[134.18051147460938, 142.01187133789062],[144.87850952148438, 140.77940368652344],\
                [61.10582733154297, 84.07833862304688],[69.74604797363281, 78.47395324707031],[80.21199035644531, 76.02899169921875],\
                [92.52067565917969, 78.07085418701172],[102.19266510009766, 85.12593841552734],[91.37337493896484, 89.0224380493164],\
                [79.75827026367188, 90.23131561279297],[70.01891326904297, 88.55178833007812],[149.52740478515625, 84.65567779541016],\
                [158.92127990722656, 77.2603988647461],[171.50877380371094, 75.0855712890625],[182.445068359375, 77.52601623535156],\
                [191.2841796875, 83.19480895996094],[182.43606567382812, 88.02413177490234],[172.05335998535156, 89.888916015625],\
                [160.28541564941406, 88.90655517578125],[89.55776977539062, 174.3827362060547],[101.32617950439453, 167.72149658203125],\
                [114.63497924804688, 164.4697723388672],[122.83482360839844, 164.82470703125],[131.55966186523438, 164.33180236816406],\
                [147.0953826904297, 167.7220458984375],[161.8936309814453, 174.5983123779297],[150.32968139648438, 181.8068389892578],\
                [137.28221130371094, 186.4801483154297],[123.55680847167969, 187.17138671875],[110.88375854492188, 185.84986877441406],\
                [99.31942749023438, 181.19949340820312],[92.92103576660156, 174.7727813720703],[108.07563018798828, 173.3674774169922],\
                [122.97026062011719, 173.23509216308594],[140.45001220703125, 172.8534393310547],[158.1939239501953, 174.57040405273438],\
                [141.13583374023438, 175.04562377929688],[123.38207244873047, 175.35841369628906],[107.95369720458984, 174.62806701660156],\
                [81.58295440673828, 83.65118408203125],[172.26219177246094, 82.51985931396484]]



#
avg_landmarks1 = [[35.078060150146484, 64.06729125976562],[36.289886474609375, 76.22138977050781],[37.02362823486328, 88.2292251586914],
                 [39.01308822631836, 100.64545440673828],[41.03062057495117, 112.51614379882812],[42.99650192260742, 124.83826446533203],
                 [45.542903900146484, 136.5175323486328],[48.10205078125, 148.85218811035156],[51.88542938232422, 160.39205932617188],
                 [56.90012741088867, 171.45431518554688],[62.717071533203125, 182.44796752929688],[69.93299865722656, 192.12918090820312],
                 [77.76457214355469, 201.65145874023438],[86.74666595458984, 210.3533477783203],[97.2267074584961, 217.3690185546875],
                 [109.64736938476562, 221.78611755371094],[122.77489471435547, 223.2422637939453],[136.1476593017578, 222.04461669921875],
                 [149.5169677734375, 216.91082763671875],[160.70176696777344, 209.98939514160156],[170.61056518554688, 200.7933807373047],
                 [179.56463623046875, 191.4114990234375],[187.9460906982422, 181.2941131591797],[195.25538635253906, 170.44601440429688],
                 [201.1561737060547, 159.22206115722656],[206.10386657714844, 147.21900939941406],[209.76748657226562, 134.99478149414062],
                 [212.9516143798828, 122.52283477783203],[215.53053283691406, 110.00794219970703],[217.84857177734375, 97.1225357055664],
                 [219.66807556152344, 84.4786376953125],[221.18504333496094, 71.61912536621094],[222.42221069335938, 58.80107498168945],
                 [48.60957717895508, 67.10745239257812],[64.27015686035156, 59.39010238647461],[80.0129623413086, 60.95086669921875],
                 [94.7013931274414, 63.75322723388672],[109.12065887451172, 66.67484283447266],[109.11258697509766, 74.0045166015625],
                 [94.86502075195312, 71.65552520751953],[79.5882797241211, 69.06111907958984],[64.33139038085938, 67.00814056396484],
                 [145.6890411376953, 65.76209259033203],[161.09454345703125, 61.36994552612305],[176.75962829589844, 57.189640045166016],
                 [192.8441619873047, 54.72019577026367],[208.69100952148438, 61.72115707397461],[192.48736572265625, 62.359989166259766],
                 [176.7373504638672, 65.42029571533203],[161.08718872070312, 68.94902038574219],[145.52706909179688, 72.99002075195312],
                 [126.70852661132812, 80.723388671875],[126.1310806274414, 101.09016418457031],[125.05699920654297, 121.11756134033203],
                 [125.10218811035156, 140.83448791503906],[103.33899688720703, 144.01963806152344],[114.24333190917969, 147.27537536621094],
                 [125.72100830078125, 149.27711486816406],[138.0908203125, 146.2925262451172],[150.56832885742188, 142.52108764648438],
                 [61.66769790649414, 80.60255432128906],[71.01822662353516, 76.27550506591797],[81.35086059570312, 74.66043853759766],
                 [93.71319580078125, 76.86229705810547],[103.2112045288086, 83.21373748779297],[92.08921813964844, 86.7829360961914],
                 [80.65206909179688, 87.64498138427734],[70.53404998779297, 85.67667388916016],[152.25643920898438, 81.81403350830078],
                 [161.9134063720703, 74.73515319824219],[174.45022583007812, 72.20075225830078],[184.86622619628906, 73.44625854492188],
                 [194.2032470703125, 77.32289123535156],[185.96653747558594, 83.05155181884766],[175.108642578125, 85.49652099609375],
                 [163.44229125976562, 85.32353210449219],[88.38064575195312, 170.15980529785156],[103.13941955566406, 166.86676025390625],
                 [117.57774353027344, 166.0797882080078],[125.7572250366211, 166.5682373046875],[134.3720703125, 165.54652404785156],
                 [151.19642639160156, 166.56082153320312],[168.1241455078125, 170.31661987304688],[156.96961975097656, 181.87608337402344],
                 [142.9145050048828, 190.04563903808594],[125.96050262451172, 192.12901306152344],[110.15286254882812, 189.70494079589844],
                 [97.6151351928711, 181.03976440429688],[92.04219818115234, 171.2353973388672],[108.8916015625, 172.63621520996094],
                 [125.7394790649414, 173.5141143798828],[144.63058471679688, 172.2008056640625],[164.1181182861328, 171.23068237304688],
                 [146.00340270996094, 177.70277404785156],[125.94993591308594, 179.76663208007812],[107.71800231933594, 177.28211975097656],
                 [82.36244201660156, 81.6081314086914],[175.01686096191406, 78.97344207763672]]

def transformation_from_points(points1, points2):
    points1 = points1.astype(np.float64)
    points2 = points2.astype(np.float64)
    c1 = np.mean(points1, axis=0)
    c2 = np.mean(points2, axis=0)
    points1 -= c1
    points2 -= c2
    s1 = np.std(points1)
    s2 = np.std(points2)
    points1 /= s1
    points2 /= s2
    U, S, Vt = np.linalg.svd(points1.T * points2)
    R = (U * Vt).T
    return np.vstack([np.hstack(((s2 / s1) * R,c2.T - (s2 / s1) * R * c1.T)),np.matrix([0., 0., 1.])])

def warp_im(tar_landmarks):


    pts1 = np.float64(np.matrix([[point[0], point[1]] for point in tar_landmarks]))
    pts2 = np.float64(np.matrix([[point[0], point[1]] for point in avg_landmarks]))
    M = transformation_from_points(pts1, pts2)
    #dst = cv2.warpAffine(img_im, M[:2], (img_im.shape[1], img_im.shape[0]))
    return M


def landmarks_match_mtcnn(src_im, src_landmarks, tar_landmarks): 
    """
    umeyama(src, dst, estimate_scale), 
    src/dst landmarks coord. should be (y, x)
    """
    src_size = src_im.shape
    src_tmp = [(int(xy[1]), int(xy[0])) for xy in src_landmarks]
    dst_tmp = [(int(xy[1]), int(xy[0])) for xy in tar_landmarks]
    #M = cv2.getAffineTransform(src_tmp,dst_tmp)
    M = umeyama(np.array(src_tmp), np.array(dst_tmp), True)[0:2]
    result = cv2.warpAffine(src_im, M, (src_size[1], src_size[0]), borderMode=cv2.BORDER_REPLICATE) 
    return result

def alignlandmarks(src_im, M):
    """
    umeyama(src, dst, estimate_scale),
    src/dst landmarks coord. should be (y, x)
    """
    src_size = src_im.shape
    result = cv2.warpAffine(src_im, M[:2], (src_size[1], src_size[0]))
    return result

def dealignlandmarks(src_im, M):
    """
    umeyama(src, dst, estimate_scale),
    src/dst landmarks coord. should be (y, x)
    """
    MT = np.linalg.inv(M)
    src_size = src_im.shape
    result = cv2.warpAffine(src_im, MT[:2], (src_size[1], src_size[0]))
    return result