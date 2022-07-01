import os
import sys
import speedtest
VERSION = "1.0"
DATE = ''
SOURCE_CODE = 'https://github.com/isanadev123/buddy.git'
TYPE = 'Robot'
OS_VERSION = os.uname()
STACKOVERFLOW = True



from subprocess import Popen, PIPE
import requests
import webbrowser
import psutil


#query engine
def buddy():
    try:
        def queryengine():
            global query
            query = input("buddy> ")

            #github engine

        #Init
            if query == 'init':
                os.system('git init')
                print('created repository')
                queryengine()

            elif query == 'add':
                multi = input('do you want to add specific files [y/n] > ')
                if multi == 'y':
                    ask = input('what files do you want to add keep spacing between file names> ')
                    os.system(f'git add {ask}')
                    queryengine()
                else:
                    os.system('git add -A')
                    queryengine()

        #commiting
            elif query == 'commit':
                msg = input('commit message type a for auto generation> ')
                if msg == 'a':
                    auto = 'Changes'
                    os.system(f'git commit -m "{auto}"')
                    queryengine()
                else:
                    os.system(f'git commit -m "{msg}"')
                    queryengine()

            elif query == 'push':
                os.system('git push')

            elif query == 'url':
                url = input('Url: ')
                os.system(f'git remote add origin {url}')

            #autocreate
            elif query == 'autocreate':
                projecturl = input('Url for github repo Https:')
                os.system('git init')
                os.system('git add -A')
                os.system('git commit -m "Started Project"')
                os.system('git branch -M main')
                os.system(f'git remote add origin {projecturl}')
                os.system('git push --set-upstream origin main')
                print('finished process!')
                queryengine()

        #buddy bot details
            elif query == '?':
                print(f'version: {VERSION}')
                print(f'Souce code: {SOURCE_CODE}')
                print(f'type: {TYPE}')
                print(f'system details: {OS_VERSION}')
                queryengine()

        #quit buddy

            elif query == 'quit':
                sys.exit()

            #clear command line
            elif query == 'clear':
                os.system('clear')
                queryengine()

            elif query == 'compile':
                name_of_file = input('file: ')
                os.system(f'python3 -m py_compile {name_of_file}')


            elif 'rn' and '.py' in query:
                q = query.split('rn')[1]
                os.system(f'python3 {q}')
                if STACKOVERFLOW == True:
                    def execute_return(cmd):
                        args = cmd.split()
                        proc = Popen(args, stdout=PIPE, stderr=PIPE)
                        out, err = proc.communicate()
                        return out, err

                    def mak_req(error):
                        resp = requests.get("https://api.stackexchange.com/" +
                                "/2.2/search?order=desc&tagged=python&sort=activity&intitle={}&site=stackoverflow".format(error))
                        return resp.json()


                    def get_urls(json_dict):
                        url_list = []
                        count = 0

                        for i in json_dict['items']:
                            if i['is_answered']:
                                url_list.append(i["link"])
                            count += 1
                            if count == 3 or count == len(i):
                                break
                            
                        for i in url_list:
                            webbrowser.open(i)



                    out, err = execute_return(f"python3 {q}")


                    error = err.decode("utf-8").strip().split("\r\n")[-1]
                    print(error)



                    if error:
                        filter_error = error.split(":")
                        json1 = mak_req(filter_error[0])
                        json2 = mak_req(filter_error[1])
                        json = mak_req(error)
                        get_urls(json1)
                        get_urls(json2)
                        get_urls(json)
                        queryengine()

                    else:
                        print("No errors (buddy ai)")
                        queryengine()


            elif query == 'cpu':
                load1, load5, load15 = psutil.getloadavg()

                cpu_usage = (load15/os.cpu_count()) * 100
                print(f'Cpu usage: {cpu_usage}%')
                queryengine()




            elif query == 'cpu-stats':
                print(psutil.cpu_stats())
                queryengine()

            elif query == 'note':
                name = input('name your note: ')
                n = input('your note: ')
                with open(f'{name}', 'w') as f:
                        f.write(n)
                        f.close()
                        print('saved!')
                        queryengine()


            elif query == 'read-note':
                name = input('name of your note: ')
                with open(f'{name}', 'r') as f:
                    print(f.readlines())
                    queryengine


            elif query == 'itest':
                print('started internet speed test....')
                st = speedtest.Speedtest()
                    # Download Speed
                ds = st.download()
                du  = st.upload()
                def humansize(nbytes):
                        suffixes = ['B', 'KB', 'MB', 'GB', 'TB', 'PB']
                        i = 0
                        while nbytes >= 1024 and i < len(suffixes)-1:
                            nbytes /= 1024.
                            i += 1
                        f = ('%.2f' % nbytes).rstrip('0').rstrip('.')
                        return '%s %s' % (f, suffixes[i])
                    #Readable
                print('download speed: ' + humansize(ds))
                print('upload speed: '+ humansize(du))

                queryengine()


            



            else:
                os.system(query)
                queryengine()






        if STACKOVERFLOW == True:
            print('stackoverflow engine wont be able to get answers about 30% the time but it will try if it fails then it will just exit out of buddy ai and bring you back to normal console mode.')
            queryengine()

        else:
            print('if you want stackoverflow execute in buddt stackoverflow=True')
            queryengine()

    except:
        print('oops we ran into a problem restarting (buddy ai) error type IndexError')
        buddy()


buddy()
