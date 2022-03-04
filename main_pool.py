from multiprocessing import Pool
import wget
 
def downloader(urls):
    try:
        wget.download('https://test-osjd.rzd.ru/api/media/resources/'+str(urls))
        return 'ok'
    except Exception as ex:
        print(str(ex))
 
if __name__ == '__main__':
    pool = Pool(processes=30)
    urls = list(range(1, 1600000))
    pool.map(downloader, urls)
