import time
import multiprocessing


def count(name):
	for i in range(1, 100001):
		print(name," ",i)


num_list = ['p1','p2','p3','p4']

if __name__ == "__main__":
	## 일반처리
	start_time = time.time()
	for num in num_list:
		count(num)

	t_normal = time.time() - start_time

	## 멀티프로세싱
	start_time = time.time()
	pool = multiprocessing.Pool(processes=4)
	pool.map(count, num_list)
	pool.close()
	pool.join()

	mp_normal = time.time() - start_time

	print("--- 일반처리 --\n %s seconds" % (t_normal))
	print("--- 멀티프로세싱 ---\n %s seconds" % (mp_normal))