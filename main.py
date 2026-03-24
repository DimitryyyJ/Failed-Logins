import re

def main():
    while True:
        try:
            file_location = input("File location: ")
            dictianory = failedIpCount(file_location)
            break
        except FileNotFoundError:
            print("Incorrect file path")

    while True:
        try:
            action = int(input("1 - Show failed logins IP statistics\n"
                               "2 - Show suspicious IPs\n"
                               "3 - Show most frequent attacker\n"
                               "4 - Print failed logins quantity\n"
                               "5 - Exit\n"))
        except ValueError:
            print("Input numbers, not letters")
        else:
            match action:
                case 1:
                    if len(dictianory) == 0:
                        print("No failed logins found")
                    else:
                        for i in dictianory:
                            print(i, dictianory[i], "failed logins.")

                case 2:
                    suspiciousIp(dictianory)

                case 3:
                    mostFailedIp(dictianory)
                case 4:
                    print(countFailedLogins(file_location))
                case 5:
                    break
                case _:
                    print("Irrelevant command name")





def countFailedLogins(file_location):
    with open(file_location, 'r') as file:
        failed = 0
        while True:
            content = file.readline().lower()
            if not content:
                break
            if "failed login" in content:
                failed += 1
    return failed

def failedIpCount(file_location):
    pattern = r'\d+\.\d+\.\d+\.\d+'
    ips = {}
    with open(file_location, 'r') as file:
        while True:
            content = file.readline().lower()
            if not content:
                break
            if "failed login" in content:
                res = re.search(pattern, content)
                if res:
                    if res.group() in ips:
                        ips[res.group()] += 1
                    else:
                        ips.update({res.group(): 1})


    return ips

def suspiciousIp(ips):
    if len(ips) == 0:
        print("No suspicious IPs found")
        return
    try:
        threshold = int(input("Input threshold: "))
    except ValueError:
        print("Input numbers, not letters")
    else:
        j = 0
        for i in ips:
            if (ips[i] >= threshold):
                print("Suspicious IP", i)
                j+=1
        if j == 0:
            print("No suspicious IPs found")



def mostFailedIp(ips):
    if len(ips) == 0:
        print("No failed logins found")
        return
    maximum = 0
    frequentIp = ""
    for i in ips:
        if ips[i] > maximum:
            frequentIp = i
            maximum = ips[i]


    print("Most frequent attacker", frequentIp, maximum, "failed logins.")

main()