from .tokened import get_access_token
from .helper import writer, loader
from time import sleep, time
from datetime import datetime, timezone
from tqdm import tqdm
import requests

headers = {"Authorization": "Bearer " + get_access_token()}

def get_ratio(students):
    cache = loader()
    get_logtime(get_data(students, cache), cache)
    for student in students:
        students[student]['ratio'] = round(students[student].get('logtime', 0)/(students[student].get('level', 0)+0.1), 3)
    writer(students)
    return students
    
def get_data(students, cache=loader()):
    for student in tqdm(students.keys(), total=len(students), desc="Data loaded", smoothing=1):
        if student not in cache or time() - cache[student].get("last_mark", time()) > 36000:
            sleep(0.5)
            stud_data = requests.get(f"https://api.intra.42.fr/v2/users/{student}",
                                    headers=headers)
            students[student]['level'] = round(stud_data.json()['cursus_users'][0]['level'], 2)
            students[student]['projects'] = []
            last_mark = 0
            for project in stud_data.json()['projects_users']:
                if 9 in project["cursus_ids"] and project['marked']:
                    data = {
                        "id": project['project']["id"],
                        "name": project['project']['name'],
                        "mark": project["final_mark"],
                        "valid": project["validated?"],
                    }
                    mark = datetime.fromisoformat(project["marked_at"].replace("Z", "+00:00")).timestamp()
                    if mark > last_mark:
                        last_mark = mark
                    students[student]['projects'].append(data)
            students[student]['last_mark'] = last_mark if last_mark != 0 else time()
        else:
            students[student]['level'] = cache[student].get('level', 0)
            students[student]['projects'] = cache[student].get('projects', [])
            students[student]['last_mark'] = cache[student].get('last_mark', time())
        if student in cache:
            students[student]['logtime'] = cache[student].get('logtime', 0)
            students[student]['last_get'] = cache[student].get('last_get', 0)
    return students

def get_logtime(students, cache=loader()):
    for student in tqdm(students.keys(), total=len(students), desc="Logtime calculated", smoothing=1):
        if student not in cache or time() - cache[student].get("last_get", 0) > 3600:
            sleep(0.5)
            stud_logtime = requests.get(f"https://api.intra.42.fr/v2/users/{student}/locations",
                                        headers=headers)
            total_logtime = 0        
            for session in stud_logtime.json():
                    end = (datetime.fromisoformat(session["end_at"].replace("Z", "+00:00")).timestamp()
                           if session["end_at"] != None
                           else datetime.now(timezone.utc).timestamp())
                    start =  datetime.fromisoformat(session["begin_at"].replace("Z", "+00:00")).timestamp()
                    total_logtime += end - start
            students[student]['logtime'] = total_logtime//3600
            students[student]['last_get'] = time()
        else:
            students[student]['logtime'] = cache[student].get('logtime', 0)
            students[student]['last_get'] = cache[student].get('last_get', time())
        if student in cache:
            students[student]['level'] = cache[student].get('level', 0)
            students[student]['projects'] = cache[student].get('projects', [])
            students[student]['last_mark'] = cache[student].get('last_mark', 0)
    return students

def get_intras():
    students, result = {}, []
    try:
        for i in range(4):
            result.append(requests.get("https://api.intra.42.fr/v2/cursus/9/users?filter[primary_campus_id]=62&filter[pool_year]=2026&filter[pool_month]=july",
                                    headers=headers,
                                    params={"page[number]": i + 1}).json())

        for page in result:
            for student in page:
                students[student['login']] = {}
        print("\nLoading everyone data, please wait ...")
        return students
    except:
        print(f"API error: {result}, try again later !")
