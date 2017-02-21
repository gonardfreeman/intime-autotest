#TEST DATA FOR KIEV KHARKOV
#testData answers
data = {
    'BVW<30_1': '30',
    'BVW<30_2': '35',
    'BVW<30_5': '40',
    'BVW<30_10': '45',
    'BVW<30_15': '60',
    'BVW<30_20': '70',
    'BVW<30_25': '75',
    'BVW<30_30': '80',
    'BVVW<30_BVW>30_31_positive': '89.3',
    'BVVW<30_BVW<30_30_negative': '89.3',
    'BVW<30_BVVW>30_31_positive': '155',
    'BVW>30BVVW<30_29_negative': '155',
    'BVW>30_BVVW>30_31_positive':'155',
    'BVW<30_BVVW<30_29_negative':'155',
}
#Volume Weight less 30 ['30','35','40','45','60','70','78','80']
dataWL30positive = {
    #BVVW boundary values volume weight
    #BVW boundary values weight
    'BVW<30_1': ['1','15','15','15'],
    'BVW<30_2': ['2','20','20','20'],
    'BVW<30_5': ['5','27','27','27'],
    'BVW<30_10': ['10','34','34','34'],
    'BVW<30_15': ['15','39','39','39'],
    'BVW<30_20': ['20','43','43','43'],
    'BVW<30_25': ['25','46','46','46'],
    'BVW<30_30': ['30','49','49','49']
}
dataWL30negative = {
    #BVVW boundary values volume weight
    #BVW boundary values weight
    'BVW<30_1': ['2','15','15','15'],
    'BVW<30_2': ['3','20','20','20'],
    'BVW<30_5': ['6','27','27','27'],
    'BVW<30_10': ['11','34','34','34'],
    'BVW<30_15': ['16','39','39','39'],
    'BVW<30_20': ['21','43','43','43'],
    'BVW<30_25': ['26','46','46','46'],
    'BVW<30_30': ['31','49','49','49'],
}
#Weight > 30 Volume Weight < 30
dataWM30VWL30positive = {
    #BVVW boundary values volume weight
    #BVW boundary values weight
    'BVVW<30_BVW>30_31_positive': ['31','15','15','15']
}
dataWM30WL30negative = {
    #BVVW boundary values volume weight
    #BVW boundary values weight
    'BVVW<30_BVW<30_30_negative': ['30','15','15','15']
}
#Weight < 30 Volume Weight > 30
dataWL30VWM30positive = {
    #BVVW boundary values volume weight
    #BVW boundary values weight
    'BVW<30_BVVW>30_31_positive': ['29','62','62','62']
}
dataWL30VWM30negative = {
    #BVVW boundary values volume weight
    #BVW boundary values weight
    'BVW>30BVVW<30_29_negative': ['29','20','20','20']
}
#Weight > 30 Volume Weight > 30
dataWM30VWM30positive = {
    #BVVW boundary values volume weight
    #BVW boundary values weight
    'BVW>30_BVVW>30_31_positive': ['31','62','62','62']
}
dataWM30VWM30negative = {
    #BVVW boundary values volume weight
    #BVW boundary values weight
    'BVW<30_BVVW<30_29_negative': ['29','15','15','15']
}