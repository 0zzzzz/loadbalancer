try:
    import urllib2
except ImportError:
    import urllib.request as urllib2
import errno
import json
import time
from collections import defaultdict
from multiprocessing import Pool


def main(address):
    last_tot_time = time.time()
    last_reqnumber_per_worker = defaultdict(int)
    last_reqnumber_per_core = defaultdict(int)

    while True:
        try:
            r = urllib2.urlopen(address)
            js = r.read().decode('utf8', 'ignore')
        except IOError as e:
            if e.errno != errno.EINTR:
                raise
            continue
        except:
            raise Exception("unable to get uWSGI statistics")


        dd = json.loads(js)
        rps_per_worker = {}
        rps_per_core = {}
        cores = defaultdict(list)
        dt = time.time() - last_tot_time
        total_rps = 0
        for worker in dd['workers']:
            wid = worker['id']
            curr_reqnumber = worker['requests']
            last_reqnumber = last_reqnumber_per_worker[wid]
            rps_per_worker[wid] = (curr_reqnumber - last_reqnumber) / dt
            total_rps += rps_per_worker[wid]
            last_reqnumber_per_worker[wid] = curr_reqnumber
            for core in worker.get('cores', []):
                if not core['requests']:
                    continue
                wcid = (wid, core['id'])
                curr_reqnumber = core['requests']
                last_reqnumber = last_reqnumber_per_core[wcid]
                rps_per_core[wcid] = (curr_reqnumber - last_reqnumber) / dt
                last_reqnumber_per_core[wcid] = curr_reqnumber
                cores[wid].append(core)
        last_tot_time = time.time()
        time.sleep(10)
        print(f'[{time.ctime()}] Сервер {address.split(":")[2].replace("/", "")} '
                       f'количество запросов в секунду: {int(round(total_rps))}')
        with open('log.txt', 'a') as file:
            file.write(f'[{time.ctime()}] Сервер {address.split(":")[2].replace("/", "")} '
                       f'количество запросов в секунду: {int(round(total_rps))} \n')


if __name__ == '__main__':
    with Pool(processes=5) as pool:
        pool.map(main,
                 [('http://127.0.0.1:9881/'),
                  ('http://127.0.0.1:9882/'),
                  ('http://127.0.0.1:9883/'),
                  ('http://127.0.0.1:9884/'),
                  ('http://127.0.0.1:9885/')
                  ])

