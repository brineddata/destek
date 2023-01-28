import re
def logs():
    with open("logdata.txt", "r") as file:
        logdata = file.read()

    host = list(re.findall('\d*\.\d*\.\d*\.\d*', logdata))
    user_name = list(map(lambda u: u[3:-2], list(re.findall('\s-\s.*\[', logdata))))
    time = list(map(lambda t: t[1:-1], list(re.findall('\[.*\]', logdata))))
    request = list(map(lambda r: r[1:-1], list(re.findall('".*"', logdata))))

    one_item = list(map(lambda i: dict({"host": host[i], "user name": user_name[i], "time": time[i], "request": request[i]}), range(len(host))))

    return one_item
logs()