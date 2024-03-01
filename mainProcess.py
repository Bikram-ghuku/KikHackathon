import json
import process.courseName as cn
import process.courses as c
import pandas

def getOptions(goals: list) -> list:
    """
    enter goals to send the goals of the student
    impCG to send if student wants to improve CG or go for intrest
    """
    with open('breadth_course.json') as f:
        bcjson = json.load(f)


    df = pandas.read_csv('final_data.csv')

    dictCourse = {}

    for x in c.courses:
        dictCourse[x] = 0

    options = []
    final = []
    for goal in goals:
        with open(f'./fieldsjson/{goal}.json') as file:
            x = json.load(file)
            for i in x:
                dbx = []
                try:
                    y = c.courses
                    cid = y[cn.couseName.index(i)]
                    csvdata = df.loc[df['cid'] == cid]
                    ltp = bcjson[cid]["L-T-P"]
                    #print(cid, "Percentage: ", x[i], "L-T-P: ", ltp)
                    dictCourse[cid] += x[i]
                    for a, b in csvdata.iterrows():
                       dbx.append({'EX': b['EX'], 'A': b['A'], 'B': b['B'], 'C': b['C'], 'D': b['D'], 'P': b['P'], 'F': b['F'], 'session': b['session']})
                    #print(dbx)
                except Exception as e:
                    print(e)
                options.append({'cid': cid, 'L-T-P': ltp, 'prevData': dbx})
    
    for i in options:
        i['percent'] = dictCourse[i['cid']] / len(goals)
        final.append(i)

    return final


print(getOptions(['Aerospace Engineer', 'Cybersecurity Analyst'], True))